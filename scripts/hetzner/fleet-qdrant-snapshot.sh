#!/usr/bin/env bash
# Daily Qdrant snapshot -> local /data/backups/qdrant -> Backblaze B2 (per-app buckets).
#
# Installed on the fleet Hetzner box as /usr/local/sbin/fleet-qdrant-snapshot.sh and run from
# /etc/cron.d/fleet-qdrant (see fleet-qdrant.cron next to this file).  Mirrors the discipline of
# fleet-sqlite-backup.sh: consistent app-level snapshot, checksum, local retention, off-box copy.
#
# The API key is read from the running container's environment at run time and never written to
# disk.  Qdrant writes the snapshot into its snapshots path, which is on the storage volume, so the
# file is moved out with plain mv and then released from Qdrant via the API.
set -euo pipefail

CONTAINER="${QDRANT_CONTAINER:-qdrant-ookh0qmlgrbxlwbbe6lolx6g}"
VOLUME="${QDRANT_VOLUME:-/var/lib/docker/volumes/ookh0qmlgrbxlwbbe6lolx6g_qdrant-storage/_data}"
API="${QDRANT_API:-http://100.69.77.26:6333}"
ROOT="${QDRANT_BACKUP_ROOT:-/data/backups/qdrant}"
KEEP_LOCAL="${QDRANT_KEEP_LOCAL:-2}"          # snapshots per collection kept on the box
KEEP_REMOTE_DAYS="${QDRANT_KEEP_REMOTE_DAYS:-14}"
# collection -> rclone destination (per-app bucket discipline, under the hetzner/ prefix like the SQLite backups)
declare -A DEST=(
  ["socratic-trade"]="b2:jays-socratic-trade-eu/hetzner/qdrant/socratic-trade"
  ["fleet-agents"]="b2:jays-fleet-shared-eu/hetzner/qdrant/fleet-agents"
)

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
LOGDIR=/var/log/fleet-backup
mkdir -p "$ROOT" "$LOGDIR"
LOG="$LOGDIR/qdrant-${STAMP}.log"
exec > >(tee -a "$LOG") 2>&1
echo "[qdrant-snapshot] start $STAMP"

KEY="$(docker inspect "$CONTAINER" --format '{{range .Config.Env}}{{println .}}{{end}}' \
       | sed -n 's/^QDRANT__SERVICE__API_KEY=//p' | head -1)"
if [ -z "$KEY" ]; then
  echo "[qdrant-snapshot] FAIL cannot read API key from container env"
  exit 1
fi
api() { curl -sS --max-time "${3:-1800}" -H "api-key: $KEY" -H 'Content-Type: application/json' -X "$1" "$API$2"; }

if ! curl -sS --max-time 20 -o /dev/null -w '%{http_code}' "$API/healthz" | grep -q '^200$'; then
  echo "[qdrant-snapshot] FAIL qdrant healthz not 200"
  exit 1
fi

FAIL=0
for coll in "${!DEST[@]}"; do
  dest_dir="$ROOT/$coll"
  mkdir -p "$dest_dir"
  echo "[qdrant-snapshot] $coll: creating snapshot"
  resp="$(api POST "/collections/$coll/snapshots?wait=true" 1800 || true)"
  name="$(printf '%s' "$resp" | jq -r '.result.name // empty' 2>/dev/null || true)"
  if [ -z "$name" ]; then
    echo "[qdrant-snapshot] FAIL $coll snapshot API returned no name: $(printf '%s' "$resp" | head -c 200)"
    FAIL=1
    continue
  fi
  src="$VOLUME/snapshots/$coll/$name"
  if [ ! -s "$src" ]; then
    echo "[qdrant-snapshot] FAIL $coll snapshot file missing on volume: $src"
    api DELETE "/collections/$coll/snapshots/$name" 120 >/dev/null || true
    FAIL=1
    continue
  fi
  dest="$dest_dir/${coll}-${STAMP}.snapshot"
  mv "$src" "$dest"
  # Release Qdrant's bookkeeping for the moved file (404 is fine: the file is already gone).
  api DELETE "/collections/$coll/snapshots/$name" 120 >/dev/null 2>&1 || true
  sha256sum "$dest" > "${dest}.sha256"
  echo "[qdrant-snapshot] OK $coll -> $dest ($(du -h "$dest" | awk '{print $1}'))"

  echo "[qdrant-snapshot] $coll: copying to ${DEST[$coll]}"
  # Directory-style copy with --include: the box's scoped B2 key can list and write but not
  # read, and a single-file copy HEADs the destination object (403).  Same pattern as
  # fleet-sqlite-backup.sh.
  if rclone copy "$dest_dir" "${DEST[$coll]}/" --include "*${STAMP}*" --transfers 4 \
       --b2-chunk-size 96M --stats-one-line --stats 60s; then
    echo "[qdrant-snapshot] OK $coll off-box copy"
    # Remote retention.
    rclone delete --min-age "${KEEP_REMOTE_DAYS}d" "${DEST[$coll]}/" || echo "[qdrant-snapshot] WARN $coll remote prune failed"
  else
    echo "[qdrant-snapshot] FAIL $coll off-box copy"
    FAIL=1
  fi

  # Local retention: keep the newest KEEP_LOCAL snapshots (+ their checksums).
  ls -1t "$dest_dir"/*.snapshot 2>/dev/null | tail -n +$((KEEP_LOCAL + 1)) | while read -r old; do
    rm -f "$old" "${old}.sha256"
    echo "[qdrant-snapshot] pruned $(basename "$old")"
  done
done

# Anything Qdrant left behind under snapshots/ (aborted runs) is safe to drop after a day.
find "$VOLUME/snapshots" -type f -name '*.snapshot' -mtime +1 -delete 2>/dev/null || true

echo "[qdrant-snapshot] done fail=$FAIL"
exit $FAIL
