# 2026-09-04 — Sentry Max Features (Fleet Matrix)

Jay + Designer.  Fresh ACP.  Board `af1ab6e9`.  Branch
`grok/sentry-max-features-fleet`.  Worktree
`~/apps/fleet-grok-sentry-max-features`.

Default is the full Sentry product surface on every app that has a project:
Issues, Performance, Replay, Feedback, Crons, Metrics, Logs, Profiling,
Releases, Alerts, Seer, mobile.  Kill switches are sample rates and
explicit `*_ENABLED=false` flags — never a silent code skip.

## Designer omissions (honor until Designer says otherwise)

| Surface | Rule |
|---|---|
| Personal-Site | No Sentry project.  Datadog only. |
| congress-trading-shared | No Sentry project.  Library; consumers report. |
| fleet-ops | No Sentry project.  No runtime. |
| ST / CT **web** session Replay | Sample rate **0%**.  Error Replay stays on (100%). |
| Seer Autofix | Hold.  RCA / Slack `rca_completed` stays. |
| Android | Hold until those tracks ship. |

Listed, not silent: CT iOS session Replay also stays 0% (same filings PII bar
as CT web; error Replay on).  BotFleet Windows has no Sentry SDK (desktop is
not a second project).  Deno has no native profiler equivalent to
`@sentry/profiling-node`.

Prefer Sentry over Datadog for exceptions, replay, and traces.  Do not enable
Datadog Session Replay on the same page.

## Per-app matrix (present vs add)

Legend: **P** = already on main.  **Add** = this lane.  **Omit** = Designer.
**N/A** = no surface.

| App | Issues | Perf | Replay session | Replay error | Feedback | Crons | Metrics | Logs | Profiling | Releases | Alerts | Seer | Mobile |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ST | P | P 0.2 | **Omit 0%** | **Add** (was opt-in off) | **Add** | P `scheduler-tick` | P | P | P server; **Add** iOS 0.1 | P | P org | RCA on; Autofix omit | P Cocoa; Android N/A |
| CT | P Deno | P 0.2 | **Omit 0%** | **Add** browser | **Add** browser | P `withMonitor` | **Add** count on warn | P | Deno native N/A; **Add** iOS 0.1 | P SHA | P org (errors not on PD) | Autofix omit | P Cocoa; **Add** error Replay |
| UM | P | P 0.2 | P 10% | P 100% | **Add** | P scheduler | P | P | **Add** server | P | P org | Autofix omit | no Cocoa |
| DD | P | P 0.2 | P 10% | P 100% | P | CI reporter P | hop spans P | P | **Add** iOS 0.1 | P | P org | Autofix omit | P Cocoa; **Add** Replay; Android omit |
| BF | P | P 0.2 | P 10% | P 100% | P | CI reporter P | gen_ai P | P | **Add** Node session | P | P org | Autofix omit | P Cocoa; **Add** Replay; Windows N/A |
| AR | P | P 0.2 | P 0% (secrets) | P 100% | **Add** (kill-switch) | P rotation | P | P | **Add** iOS 0.1 | P | P org | Autofix omit | P Cocoa; **Add** error Replay; Android omit |
| CL | P | P 0.2 | P 10% | P 100% | P | N/A | P `logo.match` | P | **Add** iOS 0.1 | P | P org | Autofix omit | P Cocoa; **Add** Replay; Android omit |
| PS | **Omit** | — | — | — | — | — | — | — | — | — | — | — | — |
| CTS | **Omit** | — | — | — | — | — | — | — | — | — | — | — | — |
| OPS | **Omit** | — | — | — | — | — | — | — | — | — | — | — | — |
| fleet-infra | P | N/A | N/A | N/A | N/A | P host/CI | N/A | P | N/A | P | P org | Autofix omit | N/A |

## Kill switches

| Flag | Default | Effect |
|---|---|---|
| `NEXT_PUBLIC_SENTRY_REPLAY_ENABLED` / `VITE_SENTRY_REPLAY_ENABLED` / `SENTRY_BROWSER_ENABLED` | on (except ST/CT session sample 0) | `false`/`0`/`off`/`no` disables Replay |
| `*_REPLAY_SESSION_SAMPLE_RATE` | ST/CT/AR web **0**; UM/DD/BF/CL **0.1** | Raise only after Designer |
| `*_REPLAY_ERROR_SAMPLE_RATE` | **1.0** | Error Replay |
| `NEXT_PUBLIC_SENTRY_FEEDBACK_ENABLED` / `VITE_SENTRY_FEEDBACK_ENABLED` / `SENTRY_FEEDBACK_ENABLED` | **on** | `false` hides the widget |
| `SENTRY_TRACES_SAMPLE_RATE` | **0.2** | Performance |
| `SENTRY_PROFILE_SESSION_SAMPLE_RATE` / iOS `profilesSampleRate` | **1** server session / **0.1** iOS | `0` disables Profiling |
| DSN unset | off | Entire SDK inert |

## What this unit does not do

- No Coolify, mint, merge, `--force-ship`, extra-ship, CloudAgent, Composer, on-demand.
- No Personal-Site / CTS / fleet-ops Sentry project.
- No Android SDK.
- No Seer Autofix enable.
- No ST/CT web session Replay above 0%.

## App PRs

One PR per app on `grok/sentry-max-features`, plus this AFC docs PR.

## Verification

- Repo grep: Personal-Site / CTS / fleet-ops still called out as no project.
- ST client source: session sample default `"0"`, error Replay on unless falsy flag, `feedbackIntegration`.
- CT CSP test: no unbounded `*`; Sentry CDN + ingest origins only when DSN present.
- iOS: `profilesSampleRate` present; ST/CT session Replay web 0% unchanged in HTML.
