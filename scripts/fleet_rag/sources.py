"""Source generators for the fleet-agents corpus.

Each `iter_*` function yields `Doc` records (one per source document) that the ingest
orchestrator chunks, scrubs, embeds and upserts.  Generators never write anywhere and never
print; they raise on a hard failure so the orchestrator can record the source as errored.

Sources (payload `source` value):
  board          ~/apps/mac-collab/findings.db   (read-only sqlite; findings + comments)
  effort-log     ~/apps/*-EFFORT-LOG.md + EFFORT-LOG-PROTOCOL.md
  doc            markdown in ai-fleet-coordinator, fleet-ops, the ~/apps protocol docs, CLAUDE.md
  skill          ~/.claude/skills/*/SKILL.md and ~/.cursor/skills/*/SKILL.md
                 (doc_id skill/<tree>/<name>; byte-identical copies collapse to the first tree)
  memory         ~/.claude/projects/*/memory/*.md and ~/.codex/memories/*.md
  apple-note     the iCloud "Coding" folder via notes_export (falls back to the on-disk cache
                 when Notes.app is unavailable and records a warning via `take_warnings`)

Generators cannot reach the ingest report directly, so a non-fatal degradation (the notes
fallback) is appended to the module-level `WARNINGS` list; the orchestrator drains it with
`take_warnings()` after each source and copies the messages into the run report.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import os
import pathlib
import re
import sqlite3
import subprocess
from dataclasses import dataclass, field
from typing import Callable, Iterable, Iterator

HOME = pathlib.Path.home()
APPS_DIR = HOME / "apps"
BOARD_DB = APPS_DIR / "mac-collab" / "findings.db"
BOARD_URL = "https://mac.jays.services/board"
FLEET_REPO = HOME / "Code" / "ai-fleet-coordinator"
FLEET_OPS_REPO = HOME / "Code" / "fleet-ops"
EXTRA_DOCS = (APPS_DIR / "AGENT-SYNC.md", APPS_DIR / "MAC-LOCAL-PROCESSES.md",
              APPS_DIR / "FLEET-UI-COPY.md", HOME / ".claude" / "CLAUDE.md")
SKILL_DIRS = (HOME / ".claude" / "skills", HOME / ".cursor" / "skills")
CLAUDE_PROJECTS = HOME / ".claude" / "projects"
CODEX_MEMORIES = HOME / ".codex" / "memories"
DOC_MAX_BYTES = 400 * 1024

SOURCES = ("board", "effort-log", "doc", "skill", "memory", "apple-note")

WARNINGS: list[str] = []


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def take_warnings() -> list[str]:
    """Return and clear the warnings accumulated since the last call."""
    out = list(WARNINGS)
    WARNINGS.clear()
    return out

# App slug normalisation shared by every source.
APP_ALIASES = {
    "api-usage-monitor": "usage-monitor", "usage-monitor": "usage-monitor", "um": "usage-monitor",
    "socratic-trade": "socratic-trade", "st": "socratic-trade",
    "congress-trade": "congress-trade", "ct": "congress-trade",
    "congress-shared": "congress-trading-shared", "congress-trading-shared": "congress-trading-shared",
    "cts": "congress-trading-shared",
    "fleet": "fleet", "fleet-infra": "fleet", "ai-fleet-coordinator": "fleet", "afl": "fleet",
    "fleet-ops": "fleet-ops",
    "botfleet": "botfleet", "bf": "botfleet", "openmausbot": "botfleet",
    "dealdex": "dealdex", "dd": "dealdex",
    "contactlogo": "contactlogo", "cl": "contactlogo",
    "autorotate": "autorotate", "ar": "autorotate",
    "personal-site": "personal-site", "ps": "personal-site",
    "trading": "trading", "agentic-trading": "trading", "trading-live": "trading",
}

SEAT_ALIASES = {
    "grok": "GROK", "monet": "MONET", "claude": "CLAUDE", "codex": "CODEX", "antigravity": "AG",
    "ag": "AG", "cursor": "CURSOR", "kimi": "KIMI", "owner": "OWNER", "jay": "OWNER",
    "gemini": "AG", "deepseek": "DEEPSEEK", "renoir": "RENOIR", "fleet": "FLEET",
}


@dataclass
class Doc:
    doc_id: str
    title: str
    text_markdown: str
    source: str
    app: str
    category: str
    seat: str
    url: str = ""
    path: str = ""
    created_at_ms: int = 0
    updated_at_ms: int = 0
    extra: dict = field(default_factory=dict)


# --------------------------------------------------------------------------- helpers

def app_slug(raw: str | None, default: str = "fleet") -> str:
    if not raw:
        return default
    key = re.sub(r"[^a-z0-9]+", "-", raw.strip().lower()).strip("-")
    if not key:
        return default
    return APP_ALIASES.get(key, key)


def seat_tag(raw: str | None, default: str = "FLEET") -> str:
    if not raw:
        return default
    tok = re.split(r"[\s(/,]+", raw.strip())[0]
    tok = re.sub(r"[^A-Za-z0-9_\-]", "", tok)
    if not tok:
        return default
    return SEAT_ALIASES.get(tok.lower(), tok.upper())


def parse_ts_ms(value: str | None) -> int:
    """ISO-8601 (with or without zone, with or without fractional seconds) to epoch ms, else 0."""
    if not value:
        return 0
    v = value.strip()
    if v.endswith("Z"):
        v = v[:-1] + "+00:00"
    try:
        d = _dt.datetime.fromisoformat(v)
    except ValueError:
        return 0
    if d.tzinfo is None:
        d = d.astimezone()          # naive stamps are local (Notes, git-less files)
    return int(d.timestamp() * 1000)


def mtime_ms(path: pathlib.Path) -> int:
    try:
        return int(path.stat().st_mtime * 1000)
    except OSError:
        return 0


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def first_heading(md: str, fallback: str) -> str:
    for line in md.splitlines()[:40]:
        m = re.match(r"^#{1,3}\s+(.*?)\s*#*\s*$", line)
        if m and m.group(1).strip():
            return m.group(1).strip()
    return fallback


_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def frontmatter(md: str) -> tuple[dict[str, str], str]:
    """Very small YAML-ish frontmatter reader: flat `key: value` lines at any indent."""
    m = _FRONT.match(md)
    if not m:
        return {}, md
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^\s*([A-Za-z_][A-Za-z0-9_\-]*):\s*(.*?)\s*$", line)
        if km and km.group(2):
            meta.setdefault(km.group(1).lower(), km.group(2).strip().strip('"').strip("'"))
    return meta, md[m.end():]


# --------------------------------------------------------------------------- git helpers

_git_cache: dict[str, dict] = {}


def _git(args: list[str], cwd: pathlib.Path) -> str | None:
    try:
        p = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, timeout=60, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if p.returncode != 0:
        return None
    return p.stdout.decode("utf-8", errors="replace")


def repo_info(path: pathlib.Path) -> dict | None:
    """{"top", "owner", "repo", "branch", "dates": {relpath: epoch_s}} for the repo holding path."""
    start = path if path.is_dir() else path.parent
    top = _git(["rev-parse", "--show-toplevel"], start)
    if not top:
        return None
    top = top.strip()
    if top in _git_cache:
        return _git_cache[top]
    info: dict = {"top": top, "owner": "", "repo": "", "branch": "main", "dates": {}}
    origin = (_git(["remote", "get-url", "origin"], pathlib.Path(top)) or "").strip()
    m = re.search(r"github\.com[:/]([^/]+)/([^/\s]+?)(?:\.git)?$", origin)
    if m:
        info["owner"], info["repo"] = m.group(1), m.group(2)
    head = (_git(["symbolic-ref", "--short", "refs/remotes/origin/HEAD"], pathlib.Path(top)) or "").strip()
    if head.startswith("origin/"):
        info["branch"] = head[len("origin/"):]
    # One log walk gives the latest commit time of every path (first occurrence wins).
    log = _git(["log", "--format=%ct", "--name-only", "--", "."], pathlib.Path(top)) or ""
    cur = 0
    for line in log.splitlines():
        if not line.strip():
            continue
        if re.fullmatch(r"\d+", line.strip()):
            cur = int(line.strip())
        elif line not in info["dates"]:
            info["dates"][line] = cur
    _git_cache[top] = info
    return info


def blob_url(info: dict | None, rel: str) -> str:
    if not info or not info["owner"]:
        return ""
    return f"https://github.com/{info['owner']}/{info['repo']}/blob/{info['branch']}/{rel}"


# --------------------------------------------------------------------------- board

_EFFORT_KEY = re.compile(r"<!--\s*effort-key:[^>]*-->\s*")


def _board_markdown(row: dict, comments: list[dict]) -> str:
    def clean(v) -> str:  # noqa: ANN001
        # The effort-board writeback stamps issue bodies with `<!-- effort-key: <sha1> -->`;
        # it is machine metadata and gitleaks reads it as a credential, so drop it.
        return _EFFORT_KEY.sub("", v).strip() if isinstance(v, str) else ("" if v is None else str(v))

    parts = [f"# {clean(row.get('title')) or 'Untitled finding'}", ""]
    meta = [f"Status: {clean(row.get('status')) or 'open'}"]
    if clean(row.get("severity")):
        meta.append(f"Severity: {clean(row['severity'])}")
    meta.append(f"App: {clean(row.get('app'))}")
    if clean(row.get("source_kind")):
        meta.append(f"Kind: {clean(row['source_kind'])}")
    if clean(row.get("category")):
        meta.append(f"Category: {clean(row['category'])}")
    if clean(row.get("surface")):
        meta.append(f"Surface: {clean(row['surface'])}")
    parts.append("- " + " · ".join(meta))
    people = []
    if clean(row.get("reported_by")):
        people.append(f"Reported by: {clean(row['reported_by'])}")
    if clean(row.get("addressed_by")):
        people.append(f"Addressed by: {clean(row['addressed_by'])}")
    if people:
        parts.append("- " + " · ".join(people))
    where = []
    for k, label in (("source", "Source"), ("repo", "Repo"), ("location", "Location"),
                     ("env", "Env"), ("source_url", "Link")):
        if clean(row.get(k)):
            where.append(f"{label}: {clean(row[k])}")
    if where:
        parts.append("- " + " · ".join(where))
    parts.append(f"- Board id: {clean(row.get('id'))}")
    for k, label in (("description", "Description"), ("recommended_fix", "Recommended fix"),
                     ("resolution", "Resolution")):
        if clean(row.get(k)):
            parts += ["", f"## {label}", "", clean(row[k])]
    if comments:
        parts += ["", "## Comments"]
        for c in comments:
            parts += ["", f"### {clean(c.get('author')) or '?'} — {clean(c.get('created_at'))}", "",
                      clean(c.get("text"))]
    return "\n".join(parts).rstrip() + "\n"


def iter_board(db_path: pathlib.Path | str = BOARD_DB, limit: int | None = None) -> Iterator[Doc]:
    db_path = pathlib.Path(db_path)
    if not db_path.exists():
        raise FileNotFoundError(f"board db not found: {db_path}")
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        comments: dict[str, list[dict]] = {}
        for c in con.execute("SELECT finding_id, author, text, created_at FROM comments "
                             "ORDER BY created_at, rowid"):
            comments.setdefault(c["finding_id"], []).append(dict(c))
        q = "SELECT * FROM findings ORDER BY created_at, rowid"
        if limit:
            q += f" LIMIT {int(limit)}"
        for r in con.execute(q):
            row = dict(r)
            cs = comments.get(row["id"], [])
            created = parse_ts_ms(row.get("created_at"))
            updated = max([parse_ts_ms(row.get("updated_at"))] + [parse_ts_ms(c["created_at"]) for c in cs])
            resolved = bool((row.get("resolution") or "").strip())
            app = app_slug(row.get("app"))
            yield Doc(
                doc_id=f"board/{row['id']}",
                title=(row.get("title") or "").strip() or f"Finding {row['id'][:8]}",
                text_markdown=_board_markdown(row, cs),
                source="board", app=app,
                category="lesson" if resolved else "finding",
                seat=seat_tag(row.get("addressed_by") or row.get("reported_by")),
                url=f"{BOARD_URL}?app={app}",
                path=str(db_path),
                created_at_ms=created or updated,
                updated_at_ms=updated or created,
                extra={"status": row.get("status"), "severity": row.get("severity"),
                       "source_kind": row.get("source_kind")},
            )
    finally:
        con.close()


# --------------------------------------------------------------------------- effort logs

def iter_effort_logs(apps_dir: pathlib.Path | str = APPS_DIR, limit: int | None = None) -> Iterator[Doc]:
    apps_dir = pathlib.Path(apps_dir)
    files = sorted(apps_dir.glob("*-EFFORT-LOG.md"))
    proto = apps_dir / "EFFORT-LOG-PROTOCOL.md"
    if proto.exists():
        files.append(proto)
    n = 0
    for p in files:
        if limit and n >= limit:
            break
        stem = p.stem
        if stem == "EFFORT-LOG-PROTOCOL":
            key, app = "PROTOCOL", "fleet"
        else:
            key = stem[: -len("-EFFORT-LOG")]
            app = app_slug(key)
        md = read_text(p)
        ts = mtime_ms(p)
        n += 1
        yield Doc(doc_id=f"effort-log/{key}", title=first_heading(md, p.name), text_markdown=md,
                  source="effort-log", app=app, category="lesson", seat="FLEET", url="",
                  path=str(p), created_at_ms=ts, updated_at_ms=ts)


# --------------------------------------------------------------------------- docs

def _skip_doc(p: pathlib.Path) -> bool:
    parts = set(p.parts)
    if "node_modules" in parts or ".git" in parts or "backups" in parts:
        return True
    if "reviews" in p.parts and "raw" in p.name.lower():
        return True
    try:
        if p.stat().st_size > DOC_MAX_BYTES:
            return True
    except OSError:
        return True
    return False


def _doc_files(fleet_repo: pathlib.Path, fleet_ops: pathlib.Path,
               extra: Iterable[pathlib.Path]) -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    if fleet_repo.exists():
        files += sorted(fleet_repo.glob("*.md"))
        files += sorted((fleet_repo / "docs").rglob("*.md"))
        files += sorted((fleet_repo / ".claude" / "skills").rglob("SKILL.md"))
    if fleet_ops.exists():
        files += sorted(fleet_ops.glob("*.md"))
    files += [pathlib.Path(x) for x in extra if pathlib.Path(x).exists()]
    seen: set[pathlib.Path] = set()
    out = []
    for f in files:
        rf = f.resolve()
        if rf in seen or not f.is_file() or _skip_doc(f):
            continue
        seen.add(rf)
        out.append(f)
    return out


def doc_from_file(p: pathlib.Path, source: str = "doc", category: str | None = None,
                  app: str = "fleet", seat: str = "FLEET", doc_prefix: str = "doc") -> Doc:
    info = repo_info(p)
    rel = ""
    if info:
        try:
            rel = str(p.resolve().relative_to(pathlib.Path(info["top"]).resolve()))
        except ValueError:
            rel = ""
    if info and rel:
        doc_id = f"{doc_prefix}/{info['repo'] or pathlib.Path(info['top']).name}/{rel}"
        url = blob_url(info, rel)
        created = info["dates"].get(rel, 0) * 1000 or mtime_ms(p)
    else:
        try:
            home_rel = str(p.resolve().relative_to(HOME))
        except ValueError:
            home_rel = str(p.resolve()).lstrip("/")
        doc_id = f"{doc_prefix}/local/{home_rel}"
        url = ""
        created = mtime_ms(p)
    md = read_text(p)
    cat = category or ("runbook" if p.name == "SKILL.md" else "doc")
    return Doc(doc_id=doc_id, title=first_heading(md, p.name), text_markdown=md, source=source,
               app=app, category=cat, seat=seat, url=url, path=str(p),
               created_at_ms=created, updated_at_ms=max(mtime_ms(p), created))


def iter_docs(fleet_repo: pathlib.Path | str = FLEET_REPO, fleet_ops: pathlib.Path | str = FLEET_OPS_REPO,
              extra: Iterable[pathlib.Path] = EXTRA_DOCS, limit: int | None = None) -> Iterator[Doc]:
    files = _doc_files(pathlib.Path(fleet_repo), pathlib.Path(fleet_ops), extra)
    for i, p in enumerate(files):
        if limit and i >= limit:
            break
        app = "fleet-ops" if pathlib.Path(fleet_ops) in p.parents else "fleet"
        yield doc_from_file(p, app=app)


# --------------------------------------------------------------------------- skills

def skill_tree(skill_dir: pathlib.Path) -> str:
    """'~/.claude/skills' -> 'claude', '~/.cursor/skills' -> 'cursor', '/x/claude' -> 'claude'."""
    d = pathlib.Path(skill_dir)
    name = d.parent.name if d.name == "skills" and d.parent.name else d.name
    tree = re.sub(r"[^A-Za-z0-9_\-]+", "-", name.lstrip(".")).strip("-").lower()
    return tree or "local"


def iter_skills(skill_dirs: Iterable[pathlib.Path] = SKILL_DIRS, limit: int | None = None) -> Iterator[Doc]:
    """One Doc per SKILL.md.  doc_id is unique per tree (skill/claude/<name>, skill/cursor/<name>);
    a byte-identical copy in a later tree is skipped (the first tree wins) so the same content is
    not chunked twice under two ids."""
    seen_hash: set[str] = set()
    n = 0
    for d in skill_dirs:
        d = pathlib.Path(d)
        if not d.exists():
            continue
        tree = skill_tree(d)
        for p in sorted(d.glob("*/SKILL.md")):
            if limit and n >= limit:
                return
            md = read_text(p)
            h = hashlib.sha256(md.encode("utf-8")).hexdigest()
            if h in seen_hash:
                continue
            seen_hash.add(h)
            meta, _ = frontmatter(md)
            name = meta.get("name") or p.parent.name
            ts = mtime_ms(p)
            n += 1
            yield Doc(doc_id=f"skill/{tree}/{p.parent.name}", title=name, text_markdown=md, source="skill",
                      app="fleet", category="runbook", seat="FLEET", url="", path=str(p),
                      created_at_ms=ts, updated_at_ms=ts)


# --------------------------------------------------------------------------- memory

_MEMORY_TYPES = {"user": "preference", "feedback": "preference", "project": "lesson",
                 "reference": "infrastructure"}


def project_slug(dirname: str) -> str:
    s = dirname
    for prefix in ("-Users-jay-", "-Users-jay"):
        if s.startswith(prefix):
            s = s[len(prefix):]
            break
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s or "home"


def app_from_project(slug: str) -> str:
    for key in ("congress-trading-shared", "socratic-trade", "congress-trade", "usage-monitor",
                "api-usage-monitor", "botfleet", "openmausbot", "dealdex", "autorotate", "contactlogo",
                "personal-site", "agentic-trading", "trading-live", "trading", "ai-fleet-coordinator"):
        if key in slug:
            return app_slug(key)
    return "fleet"


def _memory_doc(p: pathlib.Path, seat: str, doc_id: str, app: str) -> Doc:
    md = read_text(p)
    meta, _ = frontmatter(md)
    cat = _MEMORY_TYPES.get((meta.get("type") or "").lower(), "lesson")
    title = meta.get("name") or first_heading(md, p.stem)
    ts = mtime_ms(p)
    upd = parse_ts_ms(meta.get("modified")) or ts
    return Doc(doc_id=doc_id, title=title, text_markdown=md, source="memory", app=app, category=cat,
               seat=seat, url="", path=str(p), created_at_ms=min(ts, upd) or ts, updated_at_ms=max(ts, upd))


def iter_memory(claude_projects: pathlib.Path | str = CLAUDE_PROJECTS,
                codex_memories: pathlib.Path | str = CODEX_MEMORIES, limit: int | None = None) -> Iterator[Doc]:
    n = 0
    cp = pathlib.Path(claude_projects)
    if cp.exists():
        for mem_dir in sorted(cp.glob("*/memory")):
            slug = project_slug(mem_dir.parent.name)
            for p in sorted(mem_dir.glob("*.md")):
                if p.name == "MEMORY.md":
                    continue
                if limit and n >= limit:
                    return
                n += 1
                yield _memory_doc(p, "CLAUDE", f"memory/claude/{slug}/{p.name}", app_from_project(slug))
    cm = pathlib.Path(codex_memories)
    if cm.exists():
        for p in sorted(cm.glob("*.md")):
            if limit and n >= limit:
                return
            n += 1
            yield _memory_doc(p, "CODEX", f"memory/codex/{p.name}", "fleet")


# --------------------------------------------------------------------------- apple notes

_BRACKET = re.compile(r"^\s*\[([^\]]+)\]")


def parse_note_title(title: str) -> tuple[str, str]:
    """'[UM, ST, Grok] topic' -> (app, seat).  Multi-app takes the first app."""
    m = _BRACKET.match(title or "")
    app, seat = "fleet", "FLEET"
    if not m:
        return app, seat
    toks = [t.strip() for t in re.split(r"[,/]", m.group(1)) if t.strip()]
    apps: list[str] = []
    for t in toks:
        low = t.lower()
        if low in SEAT_ALIASES and low != "fleet":
            seat = SEAT_ALIASES[low]
        elif re.match(r"^gb-", low):
            seat = t.upper()
        else:
            apps.append(t)
    if apps:
        app = app_slug(apps[0])
    return app, seat


def iter_apple_notes(records: Iterable[dict] | None = None, limit: int | None = None, log=None) -> Iterator[Doc]:
    """Docs from `notes_export.export_notes()` (or pre-fetched records for tests).

    When Notes.app cannot be driven (`NotesUnavailable`) the cached records are served instead;
    the error is logged and recorded as a run warning so the report shows the degradation.
    """
    if records is None:
        from . import notes_export
        from .core import eprint
        log = log or eprint
        try:
            records = notes_export.export_notes(log=log)
        except notes_export.NotesUnavailable as e:
            records = list(notes_export.iter_cached())
            msg = f"apple-note: Notes unavailable ({e}); served {len(records)} cached notes"
            log(f"[apple-note] WARNING {msg}")
            warn(msg)
    from .notes_export import strip_title_line
    n = 0
    for rec in records:
        title = (rec.get("name") or "").strip()
        text = strip_title_line(rec.get("text") or "", title)
        if len(text.strip()) < 20:
            continue                      # empty "New Note" shells
        if limit and n >= limit:
            return
        n += 1
        app, seat = parse_note_title(title)
        created = parse_ts_ms(rec.get("created"))
        updated = parse_ts_ms(rec.get("modified")) or created
        nid = rec.get("id", "")
        yield Doc(doc_id="note/" + nid.replace("x-coredata://", ""), title=title or "Untitled note",
                  text_markdown=text, source="apple-note", app=app, category="note", seat=seat,
                  url="", path="", created_at_ms=created or updated, updated_at_ms=updated)


# --------------------------------------------------------------------------- registry

GENERATORS: dict[str, Callable[..., Iterator[Doc]]] = {
    "board": iter_board,
    "effort-log": iter_effort_logs,
    "doc": iter_docs,
    "skill": iter_skills,
    "memory": iter_memory,
    "apple-note": iter_apple_notes,
}
