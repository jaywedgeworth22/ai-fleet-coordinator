#!/usr/bin/env bash
# Canonical setup for a fresh, isolated checkout of ai-fleet-coordinator
# (Claude Code cloud/remote sandbox, Codespaces, or any throwaway clone).
# Idempotent — safe to re-run.
#
# Claude Code Cloud runs the Setup script from the PARENT of the clone
# (`/home/user`). A bare `bash scripts/cloud-setup.sh` fails with exit 127.
# Use the fleet locator in docs/CLAUDE-CODE-CLOUD-ENVIRONMENTS.md
# or: cd ai-fleet-coordinator && bash scripts/cloud-setup.sh
set -euo pipefail

cd "$(dirname "$0")/.."

echo "==> Python: $(python3 --version 2>/dev/null || echo 'not found')"
echo "==> Checking fleet registry"
python3 scripts/check-fleet-registry.py || echo "==> registry check skipped (ok if extra local-only files)"

echo "==> Setup complete."
echo "    This repo is fleet infra/docs, not a long-running app."
echo "    Verify: python3 scripts/check-fleet-registry.py"
