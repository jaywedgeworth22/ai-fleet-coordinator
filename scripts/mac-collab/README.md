# mac-collab (tracked copy)

Live process: `~/apps/mac-collab/mac-collab-server.py` under pm2 `mac-collab`.
This directory is the git copy. Edit live, then copy here before landing.

Do not serve `global-api-keys`. Names-only: `GET /files/key-names`.
`board show` / `board status` accept unique 8-char id prefixes.
`mac-collab-sync` snapshots `findings.db` under `~/apps/mac-collab/backups/` (14-day keep).
