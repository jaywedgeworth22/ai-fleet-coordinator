"""Retrieval eval over golden.jsonl: Recall@1, Recall@k, MRR.

Each golden row is {"query": ..., "note": ..., plus at least one of
"expect_doc_id_prefix" (hit.doc_id startswith) and "expect_text_contains" (a string or a
list of strings; any one appearing case-insensitively in hit.text counts)}.  A row is a hit
when ANY returned result satisfies EVERY expectation the row carries: when both keys are
present the same hit must match the doc-id prefix AND contain one of the needles.

    python3 -m fleet_rag.eval [--k 5] [--threshold 0.6] [--golden path] [--json]

Exit 1 when Recall@k is below the threshold, 2 on a credential/usage error.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Callable

from .core import FleetRagError

GOLDEN = pathlib.Path(__file__).with_name("golden.jsonl")
THRESHOLD = 0.6


def load_golden(path: pathlib.Path | str = GOLDEN) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                raise FleetRagError(f"{path}:{n}: not valid JSON ({e.msg})") from None
            if not row.get("query"):
                raise FleetRagError(f"{path}:{n}: missing 'query'")
            if not (row.get("expect_doc_id_prefix") or row.get("expect_text_contains")):
                raise FleetRagError(f"{path}:{n}: needs expect_doc_id_prefix or expect_text_contains")
            rows.append(row)
    return rows


def matches(row: dict, hit: dict) -> bool:
    """True when this one hit satisfies every expectation on the golden row.

    A doc-id prefix and a text expectation must BOTH hold when both are present; a row with
    neither never matches (load_golden rejects such rows anyway).
    """
    prefix = row.get("expect_doc_id_prefix")
    needles = row.get("expect_text_contains") or []
    if isinstance(needles, str):
        needles = [needles]
    needles = [n for n in needles if n]
    if prefix and not str(hit.get("doc_id", "")).startswith(prefix):
        return False
    if needles:
        text = str(hit.get("text", "")).lower()
        if not any(n.lower() in text for n in needles):
            return False
    return bool(prefix or needles)


def run_eval(k: int = 5, golden: pathlib.Path | str = GOLDEN,
             search: Callable[..., dict] | None = None) -> dict:
    """Run every golden query through recall_search(limit=k) and score it."""
    if search is None:
        from .recall_api import recall_search
        search = recall_search
    rows = load_golden(golden)
    ranks: list[int | None] = []
    misses: list[dict] = []
    for row in rows:
        hits = search(row["query"], limit=k).get("hits", [])
        rank = next((i + 1 for i, h in enumerate(hits) if matches(row, h)), None)
        ranks.append(rank)
        if rank is None:
            misses.append({"query": row["query"], "note": row.get("note", ""),
                           "top": [(h.get("doc_id", ""), h.get("text", "")[:80].replace("\n", " "))
                                   for h in hits[:3]]})
    n = len(rows)
    return {
        "k": k,
        "n": n,
        "recall_at_1": (sum(1 for r in ranks if r == 1) / n) if n else 0.0,
        "recall_at_k": (sum(1 for r in ranks if r is not None) / n) if n else 0.0,
        "mrr": (sum(1.0 / r for r in ranks if r) / n) if n else 0.0,
        "misses": misses,
    }


def render(res: dict) -> str:
    lines = [f"golden: {res['n']} queries   k={res['k']}",
             f"Recall@1 {res['recall_at_1']:.2f}   Recall@{res['k']} {res['recall_at_k']:.2f}   "
             f"MRR {res['mrr']:.2f}"]
    for m in res["misses"]:
        lines.append(f"MISS  {m['query']}" + (f"   ({m['note']})" if m.get("note") else ""))
        for doc_id, snippet in m["top"]:
            lines.append(f"      top: {doc_id or '-'}  {snippet}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="fleet_rag.eval", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--threshold", type=float, default=THRESHOLD)
    ap.add_argument("--golden", default=str(GOLDEN))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        res = run_eval(a.k, a.golden)
    except FleetRagError as e:
        print(f"eval: {e}", file=sys.stderr)
        return 2
    print(json.dumps(res, indent=2) if a.json else render(res))
    return 0 if res["recall_at_k"] >= a.threshold else 1


if __name__ == "__main__":
    sys.exit(main())
