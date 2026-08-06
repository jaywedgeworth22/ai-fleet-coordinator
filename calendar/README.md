# Fleet calendars + daily digest

Generated artifacts (do not hand-edit ICS; change the scripts/workflows):

| File | What it is |
|------|------------|
| [`agent-activity.ics`](./agent-activity.ics) | Timed VEVENTs per **commit** across fleet repos |
| [`daily-digest.ics`](./daily-digest.ics) | **All-day** VEVENT per day: merged PRs, issues opened/closed, effort-board rows |

## Hosted site (GitHub Pages)

After the `Fleet daily digest + calendars` workflow runs:

```text
https://jaywedgeworth22.github.io/ai-fleet-coordinator/
https://jaywedgeworth22.github.io/ai-fleet-coordinator/digest.md
https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/daily-digest.ics
https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/agent-activity.ics
```

Raw-from-main mirrors (always available even before Pages is enabled):

```text
https://raw.githubusercontent.com/jaywedgeworth22/ai-fleet-coordinator/main/calendar/agent-activity.ics
https://raw.githubusercontent.com/jaywedgeworth22/ai-fleet-coordinator/main/calendar/daily-digest.ics
https://raw.githubusercontent.com/jaywedgeworth22/ai-fleet-coordinator/main/site/digest.md
```

## Subscribe

**Daily outline (recommended for “what shipped today”):** paste the
`daily-digest.ics` HTTPS URL into Apple Calendar → Add Subscription Calendar,
or Google Calendar → From URL.

**Per-commit activity (busy day view):** use `agent-activity.ics`.

## Rebuild

```bash
export GITHUB_TOKEN="$(gh auth token)"   # or FLEET_GITHUB_TOKEN
# optional: live effort boards on this machine
export EFFORT_LOG_DIR=/Users/jay/apps
python3 scripts/build-agent-calendar.py
python3 scripts/build-fleet-daily-digest.py
```

Workflow: `.github/workflows/fleet-activity-site.yml` (every 6h + on script changes).
