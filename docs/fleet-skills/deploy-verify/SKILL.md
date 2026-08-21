---
name: deploy-verify
description: Verify production after a merge or deploy — per-app health URLs, Coolify vs Vercel vs library-tag, backup continuity, and known failure classes. Use after merging to main, after a Coolify/Vercel deploy, when health looks stale, or when the owner asks if prod is up. Do not treat Coolify API status as truth.
---

# Deploy verification (MONET)

Read `/Users/jay/apps/COOLIFY.md` before poking the API.  Prefer **public health + `docker ps` on the box** over Coolify UI/API `status` (that field goes stale).

Operator host (live 2026-08-07+): Hetzner NBG1 **`167.233.254.55`** / `fleet-hetzner-nbg1`.  SSH `ssh -i ~/.ssh/hetzner root@167.233.254.55`.  Dashboard `https://host.jays.services`.

**Retired — do not use:** `135.181.192.190`, `141.148.182.224`, Oracle Tailscale `100.97.154.2`, Coolify UUID `m1os7ijf31bg3fanil152e4b`, token name `COOLIFY_API_TOKEN` on the command line.

## Token split

| Key | Use |
|-----|-----|
| `COOLIFY_SERVER_STATS` | Read-only.  App server-stats panels.  Infisical metrics token. |
| `COOLIFY_AGENTS` | Full deploy/admin.  Agent ops only.  **Never** store this in Infisical as the app's `COOLIFY_API_TOKEN`. |

Load via env, not argv.  Names only from the handoff file: `grep -oE '^[A-Z][A-Z0-9_]*' ~/.secrets/global-api-keys`.  See `secret-handoff`.

If Infisical still has `COOLIFY_API_TOKEN` for metrics, it must equal `COOLIFY_SERVER_STATS`.

## Per-app how merge becomes prod

| App | Production | Mechanism | Health |
|-----|------------|-----------|--------|
| ST | https://socratictrade.com | Coolify auto-deploy on `main`.  UUID `d83b1aykr03uwr32yhgzaiay` (confirm live).  Merge == live — do **not** also click Deploy. | `curl -s https://socratictrade.com/api/health` |
| CT | https://congress.trade | Coolify auto-deploy.  UUID `c11c5hdhuczureb6w2pg20p0`. | `curl -sA 'Mozilla/5.0' https://congress.trade/api/health` (non-browser UAs historically 403) |
| UM | https://usage.jays.services | Coolify on Hetzner.  UUID `yagelvqux9e8l1kztif7bf2o`.  Oracle auto-deploy timer is historical. | `curl -s https://usage.jays.services/api/health` |
| DealDex | https://dealdex.online | **Vercel** on merge.  Do not migrate to Coolify. | `curl -sI https://dealdex.online` |
| Personal-Site | https://jays.services | Vercel behind Cloudflare.  **GitHub merge does not auto-publish live.**  Do not create a second Vercel project on the fleet MCP team. | `curl -sI https://jays.services` |
| CTS | published tag | Library.  Consumers pin the version. | n/a |
| fleet-infra | machine pm2 / this Mac | Not Coolify. | `curl -s https://mac.jays.services/health` |

Prefer live `GET /api/v1/applications` (via a helper that reads the token itself, or Coolify MCP) over memorized UUIDs.

Apps **not** on auto-deploy still use announce-then-deploy (~10 min no-objection on `#agent-sync`, one deployer).  Do not double-trigger: Coolify cancel is unreliable.

## 1. App health (always start here)

ST fields are nested under `.checks` (camelCase):

```bash
curl -s https://socratictrade.com/api/health | jq '.ok, .checks.db, .checks.schedulerAgeSeconds'
```

Expect `ok: true`, `db` ok, scheduler age small if a scheduler exists.  Root may 307 to `/login`.

CT: send a browser User-Agent.  A workflow red X on health is often a **false** Cloudflare challenge, not a failed deploy.

## 2. Coolify API (optional, often 403)

`host.jays.services` has sat behind a Cloudflare allowlist.  A 403 from your laptop is **not** a production outage.

Do not interpolate the token into a command you will see.  Prefer Coolify MCP or a wrapper that reads `COOLIFY_AGENTS` itself.  Expect `status: "finished"` only as a hint — then confirm public health and:

```bash
ssh -i ~/.ssh/hetzner root@167.233.254.55 'docker ps --format "{{.Names}} {{.Status}}"'
```

**Zombie:** a deploy stuck `in_progress` blocks the queue (`concurrent_builds` serializes).  Post `#agent-sync` with the deployment id if you can see it from the box.

**Silent freeze (ST #2545 class):** webhook 200 + healthy `/api/health` on an **old** sha.  Standing watch: ST `.github/workflows/deploy-freshness.yml`.  Do not hand-trigger; inspect the queue.

## 3. Backups (ST/CT/UM SQLite)

Litestream (or the host `/usr/local/sbin/fleet-sqlite-backup.sh`) is the DB path.  Prefer `/api/health` storage fields over browsing R2.

ST:

```bash
curl -s https://socratictrade.com/api/health \
  | jq '.checks.storage | {litestreamAgeSeconds, litestreamStatus, litestreamState, litestreamDegradedReasons}'
```

`storageDegraded: true` or `stale`/`stopped` → escalate immediately on Slack + board.

Litestream 0.5.12 is the pin after 0.5.14 leaked TCP sockets (2026-07-10).  Do not "upgrade" it casually.

Host scripts (cron): `fleet-sqlite-backup.sh`, `fleet-health-verify.sh`, `fleet-backup-verify-weekly.sh`.  Hetzner server backups are the outer layer — not sufficient alone for trading DB RPO.

## 4. Box checks

```bash
ssh -i ~/.ssh/hetzner root@167.233.254.55
df -h / | grep -E 'Use%|^/dev'
ps aux | grep -E 'nixpacks|coolify' | grep -v grep
```

Disk hygiene timer already prunes above high watermarks.  Sustained pressure or a stuck build is a wedged queue — Coolify container logs, not a second deploy click.

Do not revert raised `tcp_mem` sysctl just because a deploy succeeded.

## 5. After verify

Move the effort row to **Deployed** only when you say how you verified.  `closeout` skill.  Rollback: Coolify previous deployment / Vercel rollback — not Mac pm2, not `trading-publish.sh` (retired).

## Canon

- `/Users/jay/apps/COOLIFY.md`
- `/Users/jay/apps/AGENT-SYNC.md` — Production deploys; Coolify tokens
- ST `docs/rollouts/2026-08-07-hetzner-fleet-cutover.md`
- ST `docs/rollouts/2026-07-10-auto-deploy-on.md` (mechanism; UUIDs/IPs in that note may be pre-cutover)
- Skills: `secret-handoff`, `closeout`, `land-lane`
