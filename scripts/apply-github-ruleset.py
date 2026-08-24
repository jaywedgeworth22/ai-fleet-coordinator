#!/usr/bin/env python3
"""Upsert default-branch GitHub rulesets for fleet repos.

User accounts cannot attach org-wide rulesets to future repos (no org).
This is the create-time hook: call from onboard-new-app.sh, or by hand.

Kinds (match fleet-apps.json):
  product / site — PR required, conversation resolution, optional CI checks
  library        — same; never "strict" up-to-date (that saturates CI)
  infra          — PR required, conversation resolution, no default CI check

Never requires approving reviews (solo owner).  Never bypass actors.
Never force-push / delete default branch.  Status checks are not strict.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from typing import Any

RULESET_NAME = "default-main-protection"
GITHUB_ACTIONS_INTEGRATION_ID = 15368
JsonDict = dict[str, Any]


def gh_json(args: list[str], input_obj: Any | None = None) -> tuple[int, Any, str]:
    cmd = ["gh", "api", *args]
    raw_in = None
    if input_obj is not None:
        cmd.extend(["--input", "-"])
        raw_in = json.dumps(input_obj)
    proc = subprocess.run(
        cmd,
        input=raw_in,
        capture_output=True,
        text=True,
        check=False,
    )
    parsed: Any = None
    if proc.stdout.strip():
        try:
            parsed = json.loads(proc.stdout)
        except json.JSONDecodeError:
            parsed = proc.stdout
    return proc.returncode, parsed, proc.stderr


def pull_request_rule() -> JsonDict:
    return {
        "type": "pull_request",
        "parameters": {
            "required_approving_review_count": 0,
            "dismiss_stale_reviews_on_push": False,
            "required_reviewers": [],
            "require_code_owner_review": False,
            "require_last_push_approval": False,
            "required_review_thread_resolution": True,
            "require_extra_approval_for_unattributed_changes": True,
            "allowed_merge_methods": ["merge", "squash", "rebase"],
        },
    }


def status_checks_rule(contexts: list[str]) -> JsonDict:
    return {
        "type": "required_status_checks",
        "parameters": {
            "strict_required_status_checks_policy": False,
            "do_not_enforce_on_create": True,
            "required_status_checks": [
                {
                    "context": name,
                    "integration_id": GITHUB_ACTIONS_INTEGRATION_ID,
                }
                for name in contexts
            ],
        },
    }


def ruleset_body(contexts: list[str]) -> JsonDict:
    rules: list[JsonDict] = [
        {"type": "deletion"},
        {"type": "non_fast_forward"},
        pull_request_rule(),
    ]
    if contexts:
        rules.append(status_checks_rule(contexts))
    return {
        "name": RULESET_NAME,
        "target": "branch",
        "enforcement": "active",
        "bypass_actors": [],
        "conditions": {
            "ref_name": {
                "include": ["~DEFAULT_BRANCH"],
                "exclude": [],
            }
        },
        "rules": rules,
    }


def contexts_for_kind(kind: str, extra: list[str]) -> list[str]:
    if extra:
        return extra
    if kind in {"product", "site", "library"}:
        return []
    return []


def find_named_ruleset(owner_repo: str) -> int | None:
    code, parsed, err = gh_json([f"repos/{owner_repo}/rulesets"])
    if code != 0:
        raise SystemExit(f"list rulesets failed for {owner_repo}: {err.strip()}")
    rows = parsed if isinstance(parsed, list) else []
    for row in rows:
        if isinstance(row, dict) and row.get("name") == RULESET_NAME:
            ident = row.get("id")
            if isinstance(ident, int):
                return ident
    return None


def upsert(owner_repo: str, body: JsonDict, dry_run: bool) -> str:
    existing = find_named_ruleset(owner_repo)
    method = "PUT" if existing is not None else "POST"
    path = (
        f"repos/{owner_repo}/rulesets/{existing}"
        if existing is not None
        else f"repos/{owner_repo}/rulesets"
    )
    if dry_run:
        return f"DRY {method} {path} checks={[c['context'] for r in body['rules'] if r.get('type')=='required_status_checks' for c in r['parameters']['required_status_checks']]}"
    code, parsed, err = gh_json(["--method", method, path], body)
    if code != 0:
        raise SystemExit(f"{method} {path} failed: {err.strip()}")
    ident = parsed.get("id") if isinstance(parsed, dict) else existing
    action = "updated" if existing is not None else "created"
    return f"{action} {owner_repo} ruleset {ident} ({RULESET_NAME})"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="owner/name")
    parser.add_argument(
        "--kind",
        choices=("product", "site", "library", "infra"),
        default="product",
    )
    parser.add_argument(
        "--checks",
        action="append",
        default=[],
        help="Required GitHub Actions check context. Repeatable. Empty = PR gate only.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    owner_repo = args.repo.strip()
    if "/" not in owner_repo:
        raise SystemExit("--repo must be owner/name")
    contexts = [c for c in args.checks if c.strip()]
    if not contexts:
        contexts = contexts_for_kind(args.kind, [])
    body = ruleset_body(contexts)
    print(upsert(owner_repo, body, args.dry_run))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
