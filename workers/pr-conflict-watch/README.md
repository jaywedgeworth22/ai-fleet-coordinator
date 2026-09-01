# pr-conflict-watch

Cloudflare Worker that receives GitHub `pull_request` and `check_suite`/`check_run` webhooks across all of jaywedgeworth22's active repos, and posts to #agent-sync Slack the moment a PR's `mergeable_state` turns `dirty` (real conflict), `blocked`, or `unstable`. Posts again when a flagged PR recovers. Dedupes via a KV namespace so it only alerts on state *changes*, not every webhook delivery.

## Deployed

Worker: `pr-conflict-watch` on the Usage.Jays.Services Cloudflare account (`3a9368057468d0909cafaa85df12d1b7`).
URL: `https://pr-conflict-watch.jays-services.workers.dev`

Registered as a repo webhook (events: `pull_request`, `check_suite`) on all 13 active non-archived/non-fork repos under jaywedgeworth22 as of 2026-08-30: BotFleet, ai-fleet-coordinator, Congress.Trade, botfleet-site, Usage-Monitor, Socratic.Trade, DealDex, Personal-Site, ContactLogo, Autorotate, fleet-ops, congress-trading-shared, ios-app-versions.

## Secrets (Worker secrets, not in this repo)

- `GITHUB_WEBHOOK_SECRET` -- random secret shared with each repo's webhook config, used to verify `X-Hub-Signature-256`.
- `GITHUB_TOKEN` -- read-only GitHub API calls to fetch PR `mergeable_state`.
- `SLACK_BOT_TOKEN` -- posts to `#agent-sync` (channel `C0BEZDJDNKV`) via `chat.postMessage`.

## Redeploy

```bash
cd workers/pr-conflict-watch
CLOUDFLARE_API_TOKEN=... CLOUDFLARE_ACCOUNT_ID=3a9368057468d0909cafaa85df12d1b7 wrangler deploy
```

If secrets need rotating: `wrangler secret put <NAME>`, then re-register each repo's webhook with the new `GITHUB_WEBHOOK_SECRET` via `gh api repos/{owner}/{repo}/hooks/{hook_id}` PATCH.
