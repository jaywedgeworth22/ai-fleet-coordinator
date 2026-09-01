# dsh-runtime helpers (tracked)

Copy into `~/apps/dsh-runtime/` after merge:

- `start-web.sh` — pm2 `dsh-web`, binds `127.0.0.1:3080`
- `serve-tailscale.sh` — Tailscale Serve HTTPS 3080 → loopback 3080

Live ACP bridge stays `../dsh-acp.py` + `../dsh-acp.sh`.  Do not `npx`.
