#!/usr/bin/env bash
# fleet-recall-service bootstrap for a plain python:3.12-slim container (no git, no curl, no pip).
#
# 1. Fetch the public repo tarball with python urllib (reused if RECALL_TARBALL already exists).
# 2. Extract scripts/fleet_rag and scripts/fleet-recall-service into RECALL_APP_DIR.
# 3. exec python3 RECALL_APP_DIR/fleet-recall-service/server.py
#
# Env:
#   RECALL_REF             git ref / branch / tag / sha of jaywedgeworth22/ai-fleet-coordinator (default main)
#   RECALL_APP_DIR         install root (default /app)
#   RECALL_TARBALL         tarball path; reused when present, downloaded there otherwise (default /tmp/fleet-src.tgz)
#   RECALL_TARBALL_URL     override the download URL (tests / mirrors); default is the codeload URL for RECALL_REF
#   RECALL_BOOTSTRAP_ONLY  1 = stop after extracting (tests)
# Everything else (RECALL_API_TOKEN, QDRANT_*, TEI_*, PORT) is read by server.py.  Nothing here
# prints a secret.
set -euo pipefail

REF="${RECALL_REF:-main}"
APP="${RECALL_APP_DIR:-/app}"
TARBALL="${RECALL_TARBALL:-/tmp/fleet-src.tgz}"
REPO_URL="${RECALL_TARBALL_URL:-https://codeload.github.com/jaywedgeworth22/ai-fleet-coordinator/tar.gz/${REF}}"

export REF APP TARBALL REPO_URL
python3 - <<'PY'
import os, sys, tarfile, urllib.request

ref, app, tarball, url = os.environ["REF"], os.environ["APP"], os.environ["TARBALL"], os.environ["REPO_URL"]
if not (os.path.isfile(tarball) and os.path.getsize(tarball) > 0):
    print(f"bootstrap: downloading {url}", flush=True)
    tmp = tarball + ".part"
    with urllib.request.urlopen(url, timeout=180) as r, open(tmp, "wb") as fh:
        fh.write(r.read())
    os.replace(tmp, tarball)
else:
    print(f"bootstrap: reusing {tarball}", flush=True)

wanted = ("fleet_rag/", "fleet-recall-service/")
n = 0
os.makedirs(app, exist_ok=True)
with tarfile.open(tarball, "r:gz") as t:
    members = []
    for m in t.getmembers():
        parts = m.name.split("/", 2)          # <repo-ref>/scripts/<rest>
        if len(parts) != 3 or parts[1] != "scripts" or not parts[2].startswith(wanted):
            continue
        if not (m.isfile() or m.isdir()):
            continue
        m.name = parts[2]
        members.append(m)
    kwargs = {"filter": "data"} if sys.version_info >= (3, 12) else {}
    t.extractall(app, members=members, **kwargs)
    n = sum(1 for m in members if m.isfile())
server = os.path.join(app, "fleet-recall-service", "server.py")
if not os.path.isfile(server):
    print(f"bootstrap: {server} missing after extract (ref={ref}); aborting", flush=True)
    sys.exit(1)
print(f"bootstrap: extracted {n} files from ref {ref} into {app}", flush=True)
PY

if [ "${RECALL_BOOTSTRAP_ONLY:-0}" = "1" ]; then
  echo "bootstrap: RECALL_BOOTSTRAP_ONLY=1, not starting the server"
  exit 0
fi
exec python3 "${APP}/fleet-recall-service/server.py"
