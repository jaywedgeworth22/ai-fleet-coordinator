# Claude Code Cloud environments (fleet)

How to attach every fleet GitHub repo to [Claude Code on the web](https://claude.ai/code)
and give each one a setup script that actually starts.

## Why existing environments fail

Claude Code Cloud runs the **Setup script** from the **parent** of the clone
(`/home/user`), not the repo root. `git clone` creates a subdirectory named after
the repo (`Socratic.Trade/`, `Congress.Trade/`, …).

A Setup script field of `bash scripts/cloud-setup.sh` therefore exits **127**:

```
bash: scripts/cloud-setup.sh: No such file or directory
```

Socratic.Trade documented this on 2026-07-06
(`docs/rollouts/2026-07-06-cloud-setup-script-cwd-fix.md`). Congress.Trade and
later apps still shipped the bare command.

`.devcontainer/devcontainer.json` `postCreateCommand` does **not** need the `cd`.
Devcontainers already set `workspaceFolder` to the repo root.

## Canonical Setup script (paste this in every environment)

Use the same locator for every app. It works whether cwd is the clone or the
parent of the clone:

```bash
set -euo pipefail
if [ -f scripts/cloud-setup.sh ]; then
  exec bash scripts/cloud-setup.sh
fi
shopt -s nullglob
matches=(*/scripts/cloud-setup.sh)
if [ "${#matches[@]}" -eq 1 ]; then
  exec bash "${matches[0]}"
fi
echo "ERROR: scripts/cloud-setup.sh not found from $(pwd)" >&2
ls -la >&2
exit 1
```

Equivalent one-liner if you prefer the repo name:

```bash
cd <RepoName> && bash scripts/cloud-setup.sh
```

Do **not** point Claude Code Cloud at `startup.sh`. Those files are Cursor Cloud
start helpers (`cd /workspace` + background `npm run dev`) and will fail or hang
in a Claude setup script.

## Network and env vars

| Field | Fleet default |
|-------|----------------|
| Network access | **Full** (Infisical, Coolify, private package fetches, `mac.jays.services`) |
| Environment variables | Non-secret selectors only. No API keys. Cloud environments have no secrets store; anyone who can open the dialog can read the values. |
| Base branch | `main` |

Do not paste Infisical client secrets, Slack tokens, or `MAC_COLLAB_TOKEN` into
the environment dialog. Apps that need Infisical stay keyless in cloud and
resolve secrets only when identities are injected by a later, private path.

## Repos to add on claude.ai/code

Add each GitHub repo as a Claude Code project, then create (or edit) a named
cloud environment. Suggested environment name = repo name.

| Repo | `~/Code` | Setup does |
|------|----------|------------|
| `jaywedgeworth22/Socratic.Trade` | Socratic.Trade | `npm ci` at repo root |
| `jaywedgeworth22/Congress.Trade` | Congress.Trade | `npm ci --include=dev` in `app/` |
| `jaywedgeworth22/Usage-Monitor` | Usage-Monitor | `npm ci --include=dev` |
| `jaywedgeworth22/DealDex` | DealDex | `npm ci --include=dev` |
| `jaywedgeworth22/Personal-Site` | Personal-Site | `npm ci --include=dev` in `site/` |
| `jaywedgeworth22/Autorotate` | Autorotate | `npm ci --include=dev` in `apps/web/` |
| `jaywedgeworth22/ContactLogo` | ContactLogo | `npm ci --include=dev` in `web/` |
| `jaywedgeworth22/ai-fleet-coordinator` | ai-fleet-coordinator | registry check only |
| `jaywedgeworth22/congress-trading-shared` | congress-trading-shared | `npm ci --include=dev` + build |
| `jaywedgeworth22/fleet-ops` | fleet-ops | docs-only no-op |

`Pionex` under `~/Code` is not a git repo. Skip it.

## How to add / edit in the UI

There is no settings URL. On [claude.ai/code](https://claude.ai/code):

1. Connect the GitHub repo if it is missing from the repo picker.
2. Open the cloud-environment selector (cloud icon above the message box).
3. **Add cloud environment**, or hover an existing one and open the settings icon.
4. Name it after the repo. Set network to **Full**. Paste the locator above into
   **Setup script**. Save.
5. Archive stale environments that still use `bash scripts/cloud-setup.sh` after
   you have a working replacement — do not delete (archive only).

CLI `/remote-env` only **selects** an environment. It cannot create or edit one.

## New-app onboarding

`scripts/onboard-new-app.sh` should leave `scripts/cloud-setup.sh` in the new
repo. Then add the GitHub repo on claude.ai/code and paste the locator. See
[ONBOARDING-NEW-APP.md](ONBOARDING-NEW-APP.md).
