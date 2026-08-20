# Jay's Daily Coding-Related Activities

_Generated 2026-08-19 21:32 CDT · timezone America/Chicago_

Sources: merged PRs, issues opened/closed, effort-board bullets (`docs/EFFORT-LOG.md`).
Agent names are stripped from titles; HTML site shows logos instead.

- **HTML:** https://jaywedgeworth22.github.io/ai-fleet-coordinator/
- **ICS (daily outline):** https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/daily-digest.ics
- **ICS (per-commit activity):** https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/agent-activity.ics

## 2026-08-20

*0 PRs merged · 0 issues opened · 0 issues closed · 6 effort rows*

### Effort board

- **ST** `Cursor` Alert repeat lock — IN PR #2877 2026-08-20 (branch `cursor/alert-repeat-lock-2b9b`, cluster `alert-repeat-lock`). Same alert not delivered twice in 60s. `price_alert` in sent-row repeat-dedup (fingerprint = alert id). `provider_degraded` / `budget_alert` / `kill_switch` share the lock. Health/usage no longer double-send Pushover. Usage-limit 6h cooldown latches onl
- **ST** `Cursor` Wire dead tax / webhook / preset controls (`dead-controls`) — IN PR 2026-08-20 (branch `cursor/wire-dead-controls-8b69`). Results subtractFromResults, policy webhook Send test, Strategy preset CRUD. Rollout: `docs/rollouts/2026-08-20-wire-dead-controls.md`
- **ST** `Cursor` Alert repeat lock — IN PR #2877 2026-08-20 (cluster `alert-repeat-lock`, branch `cursor/alert-repeat-lock-2b9b`). 60s same-fingerprint delivery lock. Rollout: `docs/rollouts/2026-08-20-alert-repeat-lock.md`
- **CT** `Cursor` `Claude` 2026-08-20 — COMPLETED/MERGED #2037 (`90b5f597`) — DATACORRECTNESS-01/02 + stock-only $ KPI default (-10) (issue #2032). Same real-world trade counts once (canonical key + source precedence primary > manual > local_mac > competitor_backfill). Competitor injector defaults ($1,001–$15,000, filed_date=tx_date) are not published; UI says "bracket unavailable". Headline Net Flow
- **CT** `Cursor` 2026-08-20 — IN PR #2026 — OGE on House/Senate adaptive probe schedule; server-first fetch (Senate Mac-first) (issue #2025, branch `cursor/oge-adaptive-probe-5522`). `decideSourcePoll` accepts `executive` (weekday 15-minute floor, weekend hourly; no invented peaks). `OGE_POLL_INTERVAL_SEC` unused. Discovery fetch: OGE + House direct-first then Mac/scout relay; Senate eFD stays rela
- **shared** `Cursor` Retire leftover Deno Deploy current-shape in usage-telemetry-v2 rollout (2026-08-20). COMPLETED. Docs-only. `docs/rollouts/2026-07-21-usage-telemetry-v2.md` now says Congress.Trade on Coolify. Dated history stays. No package API change. PR #275. Live Mac board needs reconciliation

## 2026-08-19

*27 PRs merged · 80 issues opened · 5 issues closed · 215 effort rows*

### Merged PRs

- **CT** [#2022](https://github.com/jaywedgeworth22/Congress.Trade/pull/2022): docs(review): full-app expert panel review — 24 lenses, 467 verified findings _(by jaywedgeworth22)_
- **CT** [#2024](https://github.com/jaywedgeworth22/Congress.Trade/pull/2024): Poll OGE executive index every 15 minutes _(by jaywedgeworth22)_
- **CT** [#2026](https://github.com/jaywedgeworth22/Congress.Trade/pull/2026): OGE adaptive probe schedule; server-first fetch (Senate Mac-first) _(by jaywedgeworth22)_
- **CT** [#2037](https://github.com/jaywedgeworth22/Congress.Trade/pull/2037): Dedupe trades, stop fabricating competitor brackets, stock-only $ KPIs _(by jaywedgeworth22)_
- **CT** [#2043](https://github.com/jaywedgeworth22/Congress.Trade/pull/2043): Mark DATACORRECTNESS #2037 completed/merged in the effort log _(by jaywedgeworth22)_
- **CT** [#2044](https://github.com/jaywedgeworth22/Congress.Trade/pull/2044): docs: strengthen two-spaces rule to cover chat replies and internal prose _(by jaywedgeworth22)_
- **CT** [#2045](https://github.com/jaywedgeworth22/Congress.Trade/pull/2045): docs: correct two-spaces guidance to use literal &nbsp; entity, not raw NBSP _(by jaywedgeworth22)_
- **CT** [#2046](https://github.com/jaywedgeworth22/Congress.Trade/pull/2046): docs: add Planned effort-log rows for the 2026-08-19 full-app review _(by jaywedgeworth22)_
- **ST** [#2857](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2857): iOS Guardrails names + fold #2849 Desk subtitle _(by jaywedgeworth22)_
- **ST** [#2858](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2858): docs(review): 2026-08-18 full-app expert-panel review — desktop web + mobile web + iOS _(by jaywedgeworth22)_
- **ST** [#2859](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2859): docs(review): Part II — adversarial re-verify, gap coverage, deduped fix plan _(by jaywedgeworth22)_
- **ST** [#2864](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2864): docs(review): commit the audit board + machine-readable work items _(by jaywedgeworth22)_
- **ST** [#2865](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2865): fix(alerts): evaluate user-scoped quotes, do not fail silent _(by jaywedgeworth22)_
- **ST** [#2872](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2872): fix(home): real proposal ids, honest tones, keyboard rows _(by jaywedgeworth22)_
- **ST** [#2877](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2877): fix(alerts): 60s same-alert delivery lock (cluster alert-repeat-lock) _(by jaywedgeworth22)_
- **ST** [#2879](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2879): fix(market): session-aware cache TTL, not calendar-day freeze _(by jaywedgeworth22)_
- **ST** [#2881](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2881): docs(review): record the four owner decisions from the full-app review _(by jaywedgeworth22)_
- **ST** [#2882](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2882): fix(orders): do not auto-replace orders we do not own _(by jaywedgeworth22)_
- **ST** [#2887](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2887): fix(copy): guardrail claims match advisory engine _(by jaywedgeworth22)_
- **ST** [#2888](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2888): fix(run): scope Red Team, retry and learned directives to the run's account _(by jaywedgeworth22)_
- **ST** [#2889](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2889): fix(console): wire dead tax/webhook/preset controls _(by jaywedgeworth22)_
- **ST** [#2890](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2890): docs: strengthen two-spaces rule to cover chat replies and internal prose _(by jaywedgeworth22)_
- **ST** [#2893](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2893): docs: state HOW to emit the two-space gap so it is visible _(by jaywedgeworth22)_
- **ST** [#2894](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2894): docs: add Planned effort-log rows for the 2026-08-19 full-app review _(by jaywedgeworth22)_
- **shared** `Cursor` [#275](https://github.com/jaywedgeworth22/congress-trading-shared/pull/275): docs: Congress.Trade host is Coolify, not Deno Deploy _(by jaywedgeworth22)_
- **shared** [#276](https://github.com/jaywedgeworth22/congress-trading-shared/pull/276): docs: strengthen two-spaces rule to cover chat replies and internal prose _(by jaywedgeworth22)_
- **shared** [#277](https://github.com/jaywedgeworth22/congress-trading-shared/pull/277): docs: correct two-spaces guidance to use literal &nbsp; entity, not raw NBSP _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1994](https://github.com/jaywedgeworth22/Congress.Trade/issues/1994): 2026-08-18 — IN PR #1993 — #1991 iOS Admin + Review Queue (branch
- **CT** [#2005](https://github.com/jaywedgeworth22/Congress.Trade/issues/2005): 2026-08-18 — IN PROGRESS — No public extract card; Admin nav badges;
- **CT** [#2023](https://github.com/jaywedgeworth22/Congress.Trade/issues/2023): OGE executive poll interval: 15 minutes (keep 10m failure backoff)
- **CT** [#2025](https://github.com/jaywedgeworth22/Congress.Trade/issues/2025): OGE executive on House/Senate adaptive probe schedule
- **ST** [#2870](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2870): claim: price-alert-evaluation (review cluster)

### Issues opened

- **CT** [#2023](https://github.com/jaywedgeworth22/Congress.Trade/issues/2023): OGE executive poll interval: 15 minutes (keep 10m failure backoff)
- **CT** [#2025](https://github.com/jaywedgeworth22/Congress.Trade/issues/2025): OGE executive on House/Senate adaptive probe schedule
- **CT** [#2027](https://github.com/jaywedgeworth22/Congress.Trade/issues/2027): claim: apns-fanout-filers-join (DELIVERYALERTS-02)
- **CT** [#2029](https://github.com/jaywedgeworth22/Congress.Trade/issues/2029): P0: webhook mount + APNs query + politician 404 + delivery secret + Apple refund
- **CT** [#2031](https://github.com/jaywedgeworth22/Congress.Trade/issues/2031): IOSENGINEERING-14: iOS compile + XCTest must be a required CI check
- **CT** [#2032](https://github.com/jaywedgeworth22/Congress.Trade/issues/2032): Dedupe trades, stop fabricating competitor brackets, default stock-only $ KPIs
- **CT** [#2033](https://github.com/jaywedgeworth22/Congress.Trade/issues/2033): OPSRELIABILITY-01: every main merge 502s congress.trade for ~60s (docs-only included)
- **CT** [#2034](https://github.com/jaywedgeworth22/Congress.Trade/issues/2034): In-app account deletion (LEGALCOMPLIANCE-01, Guideline 5.1.1(v))
- **CT** [#2035](https://github.com/jaywedgeworth22/Congress.Trade/issues/2035): Docs: retire Deno Deploy / Turso as current-shape
- **CT** [#2039](https://github.com/jaywedgeworth22/Congress.Trade/issues/2039): ENGINEERINGQUALITY-01: Wire real Sentry for Deno production
- **CT** [#2047](https://github.com/jaywedgeworth22/Congress.Trade/issues/2047): 2026-08-19 — PLANNED — [Review] Data integrity: duplicates, fabricated
- **CT** [#2048](https://github.com/jaywedgeworth22/Congress.Trade/issues/2048): 2026-08-19 — PLANNED — [Review] Engineering foundations, reliability
- **CT** [#2049](https://github.com/jaywedgeworth22/Congress.Trade/issues/2049): 2026-08-19 — PLANNED — [Review] Delivery and alerts: the paid feature
- **CT** [#2050](https://github.com/jaywedgeworth22/Congress.Trade/issues/2050): 2026-08-19 — PLANNED — [Review] Legal, licensing and disclosure (20
- **CT** [#2051](https://github.com/jaywedgeworth22/Congress.Trade/issues/2051): 2026-08-19 — PLANNED — [Review] Money path: subscriptions
- **CT** [#2052](https://github.com/jaywedgeworth22/Congress.Trade/issues/2052): 2026-08-19 — PLANNED — [Review] App Store review blockers and Apple
- **CT** [#2053](https://github.com/jaywedgeworth22/Congress.Trade/issues/2053): 2026-08-19 — PLANNED — [Review] iOS app quality: correctness, native
- **CT** [#2054](https://github.com/jaywedgeworth22/Congress.Trade/issues/2054): 2026-08-19 — PLANNED — [Review] Web UX: navigation, sharing, filtering
- **CT** [#2055](https://github.com/jaywedgeworth22/Congress.Trade/issues/2055): 2026-08-19 — PLANNED — [Review] Accessibility on web and iOS (57
- **CT** [#2056](https://github.com/jaywedgeworth22/Congress.Trade/issues/2056): 2026-08-19 — PLANNED — [Review] Copy, terminology and the visual
- **CT** [#2057](https://github.com/jaywedgeworth22/Congress.Trade/issues/2057): 2026-08-19 — PLANNED — [Review] Growth, discovery, SEO and sharing (33
- **CT** [#2058](https://github.com/jaywedgeworth22/Congress.Trade/issues/2058): 2026-08-19 — PLANNED — [Review] Security and exposure (19 findings
- **CT** [#2059](https://github.com/jaywedgeworth22/Congress.Trade/issues/2059): 2026-08-19 — PLANNED — [Review] Client/API contract drift between web
- **CT** [#2060](https://github.com/jaywedgeworth22/Congress.Trade/issues/2060): 2026-08-19 — PLANNED — [Review] Web performance and caching (18
- **ST** [#2866](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2866): Review clusters: Conductor tranche-1 claims (2026-08-19)
- **ST** [#2867](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2867): claim: placement-outcome-truth (review cluster)
- **ST** [#2868](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2868): claim: ios-state-outcome-truth (review cluster)
- **ST** [#2869](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2869): claim: green-request-schema (review cluster)
- **ST** [#2870](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2870): claim: price-alert-evaluation (review cluster)
- **ST** [#2871](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2871): claim: merge-gate-blindspots docs-skip only (review cluster)
- **ST** [#2875](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2875): claim: alert-repeat-lock (same alert ≤1 per 60s)
- **ST** [#2880](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2880): Review tranche-1 : run-scoped-account + per-account-visibility
- **ST** [#2891](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2891): Alert repeat lock — IN PR #2877 2026-08-20 (cluster
- **ST** [#2895](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2895): 2026-08-19 — PLANNED — [Review] Account-scoped write paths have no
- **ST** [#2896](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2896): 2026-08-19 — PLANNED — [Review] Broker I/O is unbounded in time and
- **ST** [#2897](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2897): 2026-08-19 — PLANNED — [Review] Day P&L reads $0.00 and shorts mint
- **ST** [#2898](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2898): 2026-08-19 — PLANNED — [Review] Coach coerces invalid tool inputs
- **ST** [#2899](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2899): 2026-08-19 — PLANNED — [Review] The console ships server DB internals
- **ST** [#2900](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2900): 2026-08-19 — PLANNED — [Review] RAG mirroring pins the single
- **ST** [#2901](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2901): 2026-08-19 — PLANNED — [Review] Bull strict JSON schema is invalid, so
- **ST** [#2902](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2902): 2026-08-19 — PLANNED — [Review] Home's latest-run rows use synthetic
- **ST** [#2903](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2903): 2026-08-19 — PLANNED — [Review] Identity resolution falls back to the
- **ST** [#2904](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2904): 2026-08-19 — PLANNED — [Review] iOS shows the previous account's data
- **ST** [#2905](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2905): 2026-08-19 — PLANNED — [Review] Calendar-day freshness math freezes
- **ST** [#2906](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2906): 2026-08-19 — PLANNED — [Review] Automation cancel-replaces orders it
- **ST** [#2907](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2907): 2026-08-19 — PLANNED — [Review] Multi-account screens show the active
- **ST** [#2908](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2908): 2026-08-19 — PLANNED — [Review] Approve reports success when nothing
- **ST** [#2909](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2909): 2026-08-19 — PLANNED — [Review] Price alerts stop evaluating silently
- **ST** [#2910](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2910): 2026-08-19 — PLANNED — [Review] Quote pipeline fabricates asOf and
- **ST** [#2911](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2911): 2026-08-19 — PLANNED — [Review] Run-scoped code re-resolves the
- **ST** [#2912](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2912): 2026-08-19 — PLANNED — [Review] Hand-mirrored Swift decoders drift
- **ST** [#2913](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2913): 2026-08-19 — PLANNED — [Review] Approving is starved by the run lock
- **ST** [#2914](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2914): 2026-08-19 — PLANNED — [Review] Performance tiles print numbers
- **ST** [#2915](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2915): 2026-08-19 — PLANNED — [Review] Non-owner content can reach the
- **ST** [#2916](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2916): 2026-08-19 — PLANNED — [Review] Realized-P&L ledger reads the oldest
- **ST** [#2917](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2917): 2026-08-19 — PLANNED — [Review] Shipped copy asserts guardrails the
- **ST** [#2918](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2918): 2026-08-19 — PLANNED — [Review] Shipped controls whose backend does
- **ST** [#2919](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2919): 2026-08-19 — PLANNED — [Review] The required merge gate never compiles
- **ST** [#2920](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2920): 2026-08-19 — PLANNED — [Review] The phone build inherits desktop
- **ST** [#2921](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2921): 2026-08-19 — PLANNED — [Review] Entry paths lose their destination or
- **ST** [#2922](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2922): 2026-08-19 — PLANNED — [Review] Tone tokens fail WCAG AA at the sizes
- **ST** [#2923](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2923): 2026-08-19 — PLANNED — [Review] Operator surfaces present
- **ST** [#2924](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2924): 2026-08-19 — PLANNED — [Review] A notification's lifecycle ends before
- **ST** [#2925](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2925): 2026-08-19 — PLANNED — [Review] Sessions are unrevocable 30-day bearer
- **ST** [#2926](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2926): 2026-08-19 — PLANNED — [Review] Each broker adapter rewrites the
- **ST** [#2927](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2927): 2026-08-19 — PLANNED — [Review] Shared console overlay and menu
- **ST** [#2928](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2928): 2026-08-19 — PLANNED — [Review] Console pages disagree about where
- **ST** [#2929](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2929): 2026-08-19 — PLANNED — [Review] One transient response or one bad row
- **ST** [#2930](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2930): 2026-08-19 — PLANNED — [Review] Model choice, receipts and cost each
- **ST** [#2931](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2931): 2026-08-19 — PLANNED — [Review] Nothing pages when the desk stops, and
- **ST** [#2932](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2932): 2026-08-19 — PLANNED — [Review] The suite covers shapes but not money
- **ST** [#2933](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2933): 2026-08-19 — PLANNED — [Review] Document structure and accessible
- **ST** [#2934](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2934): 2026-08-19 — PLANNED — [Review] First console paint waits on a large
- **ST** [#2935](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2935): 2026-08-19 — PLANNED — [Review] Owner copy rules are unenforced on the
- **ST** [#2936](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2936): 2026-08-19 — PLANNED — [Review] iOS project-level hygiene: no privacy
- **ST** [#2937](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2937): 2026-08-19 — PLANNED — [Review] iOS renders a read-only subset of the
- **ST** [#2938](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2938): 2026-08-19 — PLANNED — [Review] Phone layouts are the desktop tree at
- **ST** [#2939](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2939): 2026-08-19 — PLANNED — [Review] The public site's two halves do not
- **UM** [#1241](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1241): Docs: Deno Deploy is retired; Coolify is the Congress.Trade host
- **fleet** [#43](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/43): mac.jays.services collab read (LIVE)

### Effort board

- **ST** `Cursor` Price alert evaluation — IN PR 2026-08-19 (branch `cursor/fix-price-alert-evaluation-1a3d`). Part II cluster `price-alert-evaluation`. User-scoped cascade quotes, logged errors, staleness gate, `isValidAppSymbol`. Rollout: `docs/rollouts/2026-08-19-price-alert-evaluation.md`
- **ST** `Cursor` Home proposal rows — real ids, honest tones, keyboard rows — IN PR 2026-08-19 (branch `cursor/home-proposal-rows-8a57`). Review cluster `home-proposal-rows` (`dweb-01`, `dweb-18`, `a11y-01`). Strategy trace carries persisted proposal id; Home Approve uses real id; error/failed not green; row is keyboard button with SymbolButton sibling. Rollout: `docs/rollouts/2026-0
- **ST** `Cursor` Session-aware market cache freshness (`market-cache-freshness` / mdi-01) — IN PR 2026-08-19 (branch `cursor/market-cache-freshness-5ee3`). Friday 10:00 ET cache writes no longer extend to Monday; TTL extension waits until session close (incl. early closes). `isBarSeriesFresh` is session-counted. Rollout: `docs/rollouts/2026-08-19-market-cache-freshness.md`
- **ST** `Cursor` Order provenance guard — IN PR 2026-08-19 (branch `cursor/order-provenance-guard-197e`). Auto stale-exit skips bracket legs + non-app orders; owner-cancelled protective stops tombstoned; bracket stale-limit alerts suppressed. Rollout: `docs/rollouts/2026-08-19-order-provenance-guard.md`
- **ST** `Cursor` Copy: guardrail claims match advisory engine (`copy-claims-and-rulings`) — IN PR 2026-08-19 (branch `cursor/copy-guardrail-claims-19ca`). `src/lib/guardrail-copy.ts` canonical sentences; macro/Guardrails/public/iOS aligned; paper/live ceremony stripped; Mock removed from Coach pickers; Terms §8 shared pool + `LEGAL_NOTICE_VERSION=2`. Engine unchanged. Rollout: `docs
- **ST** `Cursor` iOS Home / Guardrails parity vs live web — IN PR #2857 2026-08-19 (branch `cursor/ios-web-parity-502f`, SHA `e2f56f21`). #2856 is on `main` (`a8a0a65b`); TF 1.0.68 is behind. Current main already maps Indices via `joinedIndexList`. Folds #2849 Desk subtitle; empty-universe copy now matches web Guardrails (`S&P 500`), not a missing Strategy page. Did not add iOS inde
- **ST** `Cursor` Indices common names on all surfaces — COMPLETED/MERGED 2026-08-19 #2856 `a8a0a65b`. Live leak: Guardrails → Universe → Indices printed `sp500, nasdaqComposite, dow30, nyseComposite`. Web selected-set + Scan chips + Desk + policy-diff use `formatIndexUniverseList` / `indexUniverseLabel`. TF 1.0.68 is still the pre-#2855 binary; iOS chrome leftover is `cursor/ios-web
- **ST** `Cursor` Indices labels (`S&P 500`, not `sp500`) — COMPLETED/MERGED 2026-08-19 #2855 `b27de85c`. Copy/UI only. iOS Guardrails + policy-diff mapped; live selected-set + Scan chips still leaked (follow-up `cursor/indices-common-names-3381`). `includedIndices` / `IndexUniverse` ids stay. Rollout: `docs/rollouts/2026-08-19-indices-display-labels.md`
- **ST** `Cursor` Robinhood max-10 quote chunk for 250-name gather — IN PR #2852 2026-08-19 (branch `cursor/robinhood-quote-chunk-befc`, rebased onto #2853 `df1f5a37`). Roth `9d71dda4` llm=0 then `stalled_no_progress` 01:29:44Z. Live error: `too many symbols (max 10, got 250)` at 00:59:15Z. Chunk `get_equity_quotes` / tradability / fundamentals to 10. congress.trade 404 must not latc
- **ST** `Cursor` Manual Run once drain must resume a claimed worker — COMPLETED/MERGED 2026-08-19 #2853 `df1f5a37`. HTTP kick claimed `queued`→`running`; drain selected only `queued` (1372 skipped). Heartbeat + same-id resume + `after()` + 8m gather deadline. Remaining gather-pricing hole is #2852
- **ST** `Cursor` iOS Scan last-good on 503 refresh — IN PROGRESS 2026-08-19 (branch `cursor/ios-scan-last-good-503-b104`). Live web Refresh 503s then keeps the Aug 18 7:25:13 PM universe; iOS looked empty because it has no last-good path. Seed before Yahoo whole-set; keep valid seed rows; snapshot `latestScan`; iOS keeps names on a failed refresh. Do not merge/deploy/bounce. Do not
- **ST** `Cursor` iOS Scan last-good on 503 refresh — IN PR #2850 2026-08-19 (branch `cursor/ios-scan-last-good-503-b104`). Live web Refresh 503s then keeps the Aug 18 7:25:13 PM universe; iOS looked empty because it has no last-good path. Seed before Yahoo whole-set; keep valid seed rows; snapshot `latestScan`; iOS keeps names on a failed refresh. Do not merge/deploy/bounce. Do not
- **ST** `Cursor` iOS Scan last-good on 503 refresh — IN PR #2850 2026-08-19 (branch `cursor/ios-scan-last-good-503-b104`, rebased onto `c55c2e64`). ASC: testers on TF 1.0.68 `581467e1` already have #2830+#2831. Live `/api/scan` still 503s without names. Seed-first `/api/scan` is the 1.0.68-compatible fix; iOS `latestScan` kept for the next TF. Do not merge/deploy/bounce/second TF
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Account-scoped write paths have no guards: one click can arm Autopilot or reactivate a draining account (P1, tranche Now, effort M). importAccountSettings (src/lib/db-profiles.ts:895) strips only identity and user-level fields, so strategyAuthority copies through and a single "Import settings" click can flip a live account from Ask-first to Autop
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Identity resolution falls back to the owner instead of failing closed (P1, tranche Now, effort M). middleware.ts:385-388 sets trustedEmail = PRIMARY_EMAIL whenever isAuthConfigured() is false, and nothing asserts AUTH_SECRET in production — instrumentation.ts:47 asserts only ENCRYPTION_KEY — so a selective env regr... Findings tool: `https://mac
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Calendar-day freshness math freezes screener, OHLC and enrichment caches during live sessions (P1, tranche Now, effort M). Freshness is measured in calendar days, not trading sessions. Findings tool: `https://mac.jays.services/board?app=socratic-trade` (external_uid `market-cache-freshness`, Bearer token in `~/.secrets/mac-collab.env`)
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Hand-mirrored Swift decoders drift from route payloads with no contract test — live stop-losses render as em-dashes (P1, tranche Now, effort M). FullPolicy decodes stopLossPct/trailingStopPct/shortStopLossPct from top-level CodingKeys (ios/SocraticTrade/DeskModels.swift:383-388) while GET /api/policy returns them nested under riskRules (src/lib/t
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Non-owner content can reach the always-trusted strategy prompt with no human and a scanner that is inert in production (P2, tranche Now, effort M). src/lib/learning-review.ts:640-663 applies any 'keep' verdict with no riskTier exclusion, and applyApprovedPending (src/lib/learned-context/store.ts:397-405) merges strategy-directive rows straight in
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Shipped copy asserts guardrails the engine does not have and reintroduces the paper/live ceremony the owner ruled out (P1, tranche Next, effort M). app/console/macro/indicators.ts:698/706 and again at :753 tell the owner that below-median buys are "hard-vetoed" in risk-off/crisis regimes, while src/lib/strategy-risk.ts:187-197 keeps and tags them
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Shipped controls whose backend does nothing, or something other than the label claims (P1, tranche Next, effort M). policy.taxSettings.subtractFromResults is written by app/console/strategy/tax-settings.tsx:213 and read by nothing in the Results render path (app/console/results/page.tsx:940-994 renders P&L unmodified), so "Show res... Findings t
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] A notification's lifecycle ends before delivery is known, and the tap lands on the wrong screen (P2, tranche Next, effort M). src/lib/alerts.ts:88-89 flips the alert to the one-shot 'triggered' state before sendNotification is awaited, and sendNotification never throws on total delivery failure (src/lib/notifications.ts:265-279 folds every e
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Console pages disagree about where things live, how they save, and how they are searched (P2, tranche Next, effort L). Three different save models coexist across the Configure pages (app/console/guardrails/page.tsx:335), and two numeric fields PATCH on every keystroke against the blur-commit pattern every sibling uses (app/console/set... Finding
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Model choice, receipts and cost each derive from a stale or partial source (P2, tranche Next, effort M). src/lib/model-rotation.ts:73 hardcodes a 'dead' OpenRouter list that drops slugs the live catalog still serves; app/console/components/approval-card.tsx:127 asserts 'this run's rotation pick, not a failover' even when... Findings tool: `https
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] Nothing pages when the desk stops, and the backup/disk story is unverified (P2, tranche Next, effort L). app/api/health/route.ts:88 and :128 set checks.schedulerStale and checks.tradingLiveness.degraded without changing the 200 (ok flips only at :78 and :279), and nothing pushes on them — src/lib/scheduler.ts has a singl... Findings tool: `https
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] The suite covers shapes but not money paths, reaches the live internet, and serializes 14 minutes into every run (P2, tranche Next, effort L). vitest.config.ts has no setupFiles at all — only a globalSetup that plumbs TMPDIR — so nothing prevents a test from reaching SiliconFlow, SEC or Yahoo (STATUS.md still records those 404s), and maxWorkers:1
- **ST** `Claude` 2026-08-19 — PLANNED — [Review] iOS renders a read-only subset of the screens it mirrors (P2, tranche Later, effort L). Coach replies print raw markdown (ios/SocraticTrade/CoachView.swift:272) and its Suggested Draft cannot be staged although the copy says to approve it in Proposals (:323); the Scan header advertises three side-by-side... Findings tool: `https://mac.jays.servi
- **ST** `Codex` Wire the getRedTeamEfficacy scorecard into the console — DEPLOYED
- **ST** `Codex` Batch typed-confirm flow for LIVE proposals in approvals triage
- **ST** `Claude` PR #1095 inline-Bear bare-array recovery + #1097 docs close-out
- **ST** `Grok` Prefer Pushover over Resend — COMPLETED via #2698. Litestream-wedge remainder is not this lane. Issue #2697 first line preserved historically
- **ST** `Claude` Durable litestream remote-inventory cache — COMPLETED. Issue #2694 closed
- **ST** #838/#837/#1319 via PR #2459 (prompt fencing, headline first-seen, approval 4xx)
- **ST** P2.4 congress_share_daily: 60m failure backoff + activeDailySharePromise single-flight already on main; residual outer IfDue single-flight in residual PR
- **ST** P2.6 order_placement_uncertain → #2459 / strategy placement classification
- **ST** P2.9 LLM failover + scheduler jitter already wired; UI exposes llmFallbackModels (seeding remains owner decision #1324)
- **ST** P3 feed coalesce, KNOWN_GLOBAL System-wide, storage_warning type, evidence_age LRU, protective-stop attribution largely on main
- **ST** Console topCandidates.slice crash fixed via safeTopCandidates on main
- **ST** iOS Coach → Insights rename already on main (InsightsView)
- **ST** Merged PRs closed as DEPLOYED on board: #2488 framework reopen, #2450 Run once A6, #2442 TestFlight ship, #2429 congress filing skill, #2413 plain nav B1, #2398 no direct FMP/Quiver/UW, #2444 auto-pause
- **ST** `Codex` SEC/RAG P0 occurrence identity + durable manifest/job state ( program; RAG-B03/B06/B07)
- **ST** `Codex` SEC/RAG P1 retrieval/strategy consumption redesign ( program; RAG-B11/B12/B13/B18)
- **ST** `Cursor` `Antigravity` ~~Disentangle PR #805: land — P0/P1 commit and — health slice as separate merges
- **ST** `Cursor` ~~Migrate legacy regime:current row to per-user keys at first tick after the P0 fix lands
- **ST** Resolve main-protection ruleset review gate that leaves all-green PRs stuck BLOCKED (OWNER, S)
- **ST** `Claude` check-pin required-status-context merge deadlock fix (branch
- **ST** `Cursor` Corpus re-embed scoped-run purge gate fix (branch
- **ST** `Cursor` Stop placement intent authoritative-absence fix (branch
- **ST** `Codex` Production-path RAG evaluator (worktree `/Users/jay/.codex/worktrees/rag-production-eval-20260721`, branch `codex/rag-production-eval-20260721`) — IN PROGRESS. DB evaluator and Pinecone hosted-inference benchmark are locally committed; focused tests, scoped lint, TypeScript, and diff-check are green. Parent integration/PR remains pending. Both paths are bounded a
- **ST** `Codex` Production-path RAG evaluator (worktree `/Users/jay/.codex/worktrees/rag-production-eval-20260721`, branch `codex/rag-production-eval-20260721`) — IN PROGRESS. DB evaluator and Pinecone hosted-inference benchmark are locally committed; benchmark follow-up adds empty-set refusal, absolute CLI spend caps, model-default reranking, and provider usage receipts. Focuse
- **ST** `Claude` BRANCH PROTECTION TEMPORARILY RELAXED to break a 34-PR merge deadlock
- **ST** `Claude` CI-load trim: Playwright Smoke off every PR (worktree `ci-trim-smoke`
- **ST** `Claude` Which-key visibility + "agents never create API keys" ruling (worktree
- **ST** `Claude` `Codex` PR #1776 review-thread closeout: all 4 — findings fixed
- **ST** `Claude` Three new RapidAPI-backed enrichment providers: Mboum Finance, YH
- **ST** `Claude` Which-key visibility + "agents never create API keys" ruling (worktree
- **ST** `Claude` Usage-compliance Wave 2 (ST lane): telemetry gaps + OpenRouter classifier
- **ST** `Antigravity` `Claude` handoff §7 ports: coach-note archive + coach-note/lesson vector writers
- **ST** `Claude` `Antigravity` [ on 's lane] PR #1775 review-thread closeout — scoped re-embed progress
- **ST** `Antigravity` `Claude` handoff §7 ports: coach-note archive + coach-note/lesson vector writers
- **ST** `Claude` handoff §7 ports: coach-note archive + coach-note/lesson vector writers
- **ST** `Claude` OpenRouter credit signal on /api/health (branch `monet/openrouter-credit-health`
- **ST** `outcome-engine` — outcome writer (matured outcomes onto decision cases), multi-horizon
- **ST** `episodic-retrieval` — new `experience-memory.ts`: decision-time k-NN analogs +
- **ST** `coaching-durable` — coach notes through `ingestLearned` (origin `coach`), kill the silent
- **ST** `reflection-decompose` — done, pushed, awaiting the landing train (branch
- **ST** Prune stale abandoned local-only branches from origin (June 21–29 experiments) (OWNER, M) — ~40 origin branches are ahead of main with NO PR and last activity June 21–29 (agent/claude-, safety/, feat/, reliability/, sim/funded-test-account, etc.). They are stale experiments from the pre-worktree era, add noise to every branch scan, and confuse abandoned-work triage. Audit which are
- **ST** `Codex` Production-path RAG evaluator (worktree `/Users/jay/.codex/worktrees/rag-production-eval-20260721`, branch `codex/rag-production-eval-20260721`) — IN PROGRESS. Read-only corpus evaluator and DB case schema implemented; focused tests, scoped lint, and TypeScript green; committed locally and awaiting parent integration/PR. No provider/corpus/production mutation
- **ST** `Claude` BRANCH PROTECTION TEMPORARILY RELAXED to break a 34-PR merge deadlock
- **ST** `Antigravity` Watchlist & Order Row Button Tooltip Alignment — MERGED AS `07c2da3f` / AUTO-DEPLOY VERIFICATION PENDING. Aligned watchlist action button and order row action button tooltips to the right (`align="right"`) to prevent clipping at the screen's right edge. Passed verification gate (tsc, lint, test, build)
- **ST** `Codex` Admin authorization fail-closed hardening
- **ST** `Claude` Settings auto-save everywhere — ✅ COMPLETED
- **ST** `Claude` (6 rows, risk lane) — COMPLETED. Red-Team fail-open->policy-aware routing; vol-targeting sizing +
- **ST** `Claude` Durable pre-network stop-placement intent + atomic idempotent
- **ST** `Cursor` LLM cooldown + draining-account purge safety (PR #1845, branch `cursor/critical-bug-management-2b05`) — IN PROGRESS → landing. Code + rollout present; STATUS/EFFORT-LOG filled for handoff gate. Commit author identity: subsequent commits use noreply; squash-merge lands under PR merge identity
- **ST** `Claude` Tradier: broker-connection-only, no duplicate API-key Settings
- **ST** `Claude` Console radius + micro-type token sweep (branch `monet/console-token-sweep`
- **ST** `Claude` Settings de-iOS restoration + admin-link-in-chrome + site-wide UI expert review
- **ST** `Claude` `Codex` Bracket sibling-leg teardown: adversarial review follow-up + — P1 catch
- **ST** `Claude` Alpaca + Tradier bracket sibling-leg cancellation
- **ST** `Claude` Green/Red picker label coloring + Green Team/Red Team/Bull/Bear copy sweep
- **ST** `Claude` 2-3 day activity audit: find unresolved issues — COMPLETED
- **ST** Enrichment starvation: force-included scan candidates (holdings + event outliers) never
- **ST** `Claude` usage-cap pickup
- **ST** `Claude` Short stop-loss default (8%) + surface short settings in main Essentials
- **ST** `Claude` Model Stats drawer widened on desktop — COMPLETED
- **ST** `Claude` Scoring-factor weight tooltips — COMPLETED
- **ST** `Claude` Picker copy: "Proposer"/"Reviewer" + AI-review panel "Strategist"
- **ST** Settings affordance and tooltip pass - add clearer option descriptions/tooltips
- **ST** Universal ticker detail drawer parity - restore old-site discoverability by
- **ST** Intro landing fixes: viewport-true fallback box + eased retarget + fade gated on real
- **ST** `Claude` PRs #1019 / #1021 — RAG: server-side as-of Pinecone filter + persist-pool v2 (2 owner-approved
- **ST** `Claude` PRs #970 / #973 / #974 / #977 / #979 — next-wave RAG retrieval-quality + corpus-integrity
- **ST** `Antigravity` PR #844 - `claude/pr805-remediation`: P0 checkRegimeFlip RMW fix + P1 backlog + — connection-health
- **ST** `Claude` Global learning reads + batched advisory review of proposals ( cloud, branch
- **ST** `Claude` Per-team reasoning levels + rotation auto-effort + usage/Learning-Review links
- **ST** `Claude` PR #979 - Persist retrieved candidate pool for RAG analyzability
- **ST** `Claude` PR #1019 - Server-side point-in-time (as-of) filtering in Pinecone
- **ST** `Claude` PR #1021 - persist-pool-v2: pre-rankPool candidate pool + per-stage drop dispositions
- **ST** `Claude` PR #977 - Corpus-coverage receipt for requested-but-empty filings doc types
- **ST** PR #973 - RAG golden-eval expansion: episodic-analog cases + single-vs-multi-query (#822)
- **ST** `Claude` PR #970 - Typed retrieval-status receipt
- **ST** `Claude` PR #974 - Held-position retrieval scope
- **ST** PR #816 - Prompt-safety CR-H: fencing + deterministic injection receipts for the money-path
- **ST** PR #819 - Wire `usage-budget` Phase 2 (advisory-first, owner-overridable enforcement) into
- **ST** `Claude` PR #820 - Durable due-jobs substrate for 15m/1h intraday outcome sampling . Merged to
- **ST** `Claude` PR #822 - HyDE + evidence-derived multi-query retrieval for filings RAG, flag-gated
- **ST** `Codex` Coach chat -> framework primitives — ✅ COMPLETED via PR #810
- **ST** `Codex` Scan table column customization parity — ✅ COMPLETED via PR #806
- **ST** `Antigravity` Harden HMAC Security & Persistent Idempotency for webhooks — ✅ COMPLETED via PR #854. Updated `congress-webhook-auth.ts` to validate `X-Signature` header via HMAC SHA256. Created `processed_webhooks` db table and integrated persistent DB check in `markSeen` alongside in-memory cache to ensure persistent idempotency across server restarts. Lint and tests green
- **ST** `Claude` PRs #816 / #819 / #820 / #822 — planned-backlog train: prompt-safety fencing, usage-budget
- **ST** `Codex` PR #810 - Coach chat -> framework primitives . Merged to `main`
- **ST** `Codex` PR #806 - Scan table column customization parity . Merged to `main`
- **ST** `Claude` Pre-policy vetoes advisory-overridable — merged PR #814 (verify+smoke green)
- **ST** `Claude` Full-suite test determinism: de-flake order-confirmation-status + chat-orchestrator-search-knowledge — merged PR #812
- **ST** `Claude` Guardrails → overridable preferences (denylist) ( risk lane) — merged PR #799
- **ST** `Codex` PR #807 - Approvals triage upgrades + alert center . Merged to `main`
- **ST** `Claude` PR #694 - Effort-issues sync secondary-rate-limit hardening . Merged to `main`
- **CT** `Cursor` 2026-08-19 — COMPLETED/MERGED #2024 (`e7082218`) — Poll OGE executive index every 15 minutes (issue #2023). Superseded the same day by issue #2025 / adaptive `probeSchedule`. The 15-minute figure remains only as the weekday coverage floor
- **CT** `Claude` 2026-08-19 — IN PR — Full-app expert panel review (branch `claude/full-app-review-2026-08-19`, worktree `~/apps/congress — review`). 24 expert lenses over desktop web, mobile web, iOS on `main` (simulator) and the shipped App Store build 1.0.75. Report-only, no product code touched. 467 verified findings (P0 10 / P1 48 / P2 148 / P3 173 / P4 88), 222 duplicates merged, 3 refut
- **CT** `Cursor` 2026-08-19 — COMPLETED/MERGED #2020 (`ba699ffb`) — Remove Largest Buys / Largest Sells from Trends (issue #2019, branch `cursor/remove-trends-extremes-4d19`). Follow-up to #2017. Drop the two Trends cards entirely (titles, HIDE, tables, wrappers). Metric cards and filters stay. Filter-by-side is the path. Gates: typecheck clean; 259 files / 3180 tests; CI typecheck+test + gitleak
- **CT** `Cursor` 2026-08-19 — COMPLETED/MERGED #2017 (`c845af79`) — Mobile web UI polish (issue #2016, branch `cursor/web-ui-mobile-polish-4d19`). One filter row on Trends + Trades (timeframe shrinks to content; compact "3 Months"). Drop Snapshot heading + Largest Buys/Sells blurbs. Restore pre-#1963 Light/Dark/System segmented control (icon + label). Delete Capitol Ledger / Style row. One Upgrad
- **CT** `Cursor` 2026-08-19 — IN PR #2013 — ToS / Privacy Policy share one heading + theme chrome (branch `cursor/legal-pages-theme-parity-6140`). Both routes already use `legalHtml.ts` `shell()`, but that shell was dark-only and ignored `ui-theme`. One layout path: PP navy title / Effective date / numbered h2 / system sans as the dark reference; Light / Dark / System from the site switch (default l
- **CT** `Cursor` 2026-08-19 — COMPLETED/MERGED #2010 (`a573bce0`) — Remove broken email magic-link sign-in (issue #2008, branch `cursor/remove-email-signin-3f56`). Website sign-in sheet drops Email / Send Link. iOS hamburger + Settings `SignInPanel` drops Email Link (`POST /auth/magic/request`). Apple + Google stay. Backend magic routes left in place (dead UI). No Resend/token rebuild. Gates: ty
- **CT** `Cursor` 2026-08-19 — COMPLETED/MERGED #2002 (`85691594`) — No public extract card; Admin nav badges; selector due-now drain (issue #2003, branch `cursor/extract-banner-eligible-drain-9c3d`). No halt/Ack Halt banner or button. Review Queue + Admin nav badges only. Drain is 1 selector-eligible / due-now doc (not health `eligible`). Attempt-capped cascade is health-terminal. No OpenRouter r
- **CT** `Cursor` 2026-08-19 — COMPLETED/MERGED #2002 (`85691594`) — No public extract card; Admin nav badges; selector due-now drain (issue #2003). No halt/Ack Halt control. 1 selector-eligible-due drain/min. No OpenRouter reply-routing. Coolify auto-deploy on main
- **CT** `Claude` Usage-compliance Wave 2 (CT lane): OpenRouter classifier metadata + generation-id capture (branch `claude/usage-compliance-ct`, worktree outside repo tree; — handoff pickup per `/Users/jay/apps/HANDOFF-usage-compliance-classifier- .md` + DESIGN-usage-compliance-classifier.md §2, incl. the RESOLVED flat-under-`trace` correction). Shared pin bumped v1.8.x
- **CT** `Codex` Backend delivery + ingestion reliability hardening — INTEGRATED +
- **CT** `Codex` Billing + platform security hardening — INTEGRATED LOCALLY + ADVERSARIALLY REVIEWED
- **CT** `Codex` iOS client correctness + performance hardening — INTEGRATED LOCALLY + REVIEWED
- **CT** `Claude` GPT-5.6 bake-off evaluation prep + usage/cost tracking harness — BUILT + PUSHED
- **CT** `Claude` Fix dead auto-publish gate: AGREEMENT_AUTOPUBLISH_MODEL_B was broken 2 weeks
- **CT** `Claude` Review-queue automation: model choice + multi-model consensus + escalation cascade
- **CT** `Codex` global coordination + fleet monitoring setup
- **CT** `Codex` Cloud Slack + effort-log readiness across all four apps
- **CT** Audit production schema drift from the three failed Deploy runs (OWNER, S) — Confirm whether
- **CT** `Claude` De-duplicate effort-issues sync when a row's first line changes
- **CT** Root cause of free-tier Class A pace ~162%: Litestream L0 PutObject per SQLite commit under `load_prices_st` bulk load
- **CT** (2) Loader: `analysis/massive-bulk-load/load_prices_st.py` + `load_prices.py` now batch with ` — commit-every 50` (fetch outside write lock; multi-ticker single commit). Host loader restarted root: `/tmp/load_prices_st.py — commit-every 50` state `/tmp/st_load_state.json`
- **CT** (3) Litestream: host `/etc/litestream/congress.yml` `sync-interval: 5m` (was 30s); service restarted; log shows `sync-interval=5m0s`
- **CT** (4) R2 cleanup on `congress-trade-bucket`: bulk/ kept last 3 dates only (−0.93 GiB), competitors/ deleted (−0.80 GiB), `_ops/usage-telemetry/` deleted (3759 objs). Tracked storage ~5.9 → ~3.8 GiB
- **CT** No app code/deploy required for this ops unit
- **CT** `Antigravity` `Gemini` OpenRouter Model Consolidation & Mistral OCR Integration — IN PROGRESS (PR #521 open, awaiting CI). Swapped direct model endpoints (OpenAI, , Anthropic, xAI) for their OpenRouter equivalents across default candidates, keeping native Mistral OCR as fallback. Updated settings validation to check underlying providers so multiple OpenRouter models can coexist in one lineup. Refac
- **CT** Live: `/api/health` costProfile paid; OpenRouter reads working (same row counts, field-level disagree remains on many legacy 2022 review docs). Autopublish enqueues 10+/tick. Review still ~1.9k (soft low_confidence + bad_asset_name + provider-gap)
- **CT** Live: `/api/health` costProfile paid; OpenRouter reads working (same row counts, field-level disagree remains on many legacy 2022 review docs). Autopublish enqueues 10+/tick. Review still ~1.9k (soft low_confidence + bad_asset_name + provider-gap)
- **CT** `Cursor` full reconcile (this chat + sister cloud `bc-df4b4649`): all GitHub Issues closed, boards synced. PR #898 fixed the effort-issues sync classifier (stops reopening finished rows). R2 proxy endpoint deployed via PR #912. Deno live ingestion parity handled. Owner-gated items (analytics, subscription login, R2 enablement, key ops, watcher-cron) resolved. Open GitHub issues went from
- **CT** `Codex` #714 P2 timestamp-sort follow-up — MERGED via #775 integration. Future-date clamp preserves full timestamp precision (dashboardHtml tests on main)
- **CT** `Codex` #749 Deno deploy PR conflict/comment closeout — SUPERSEDED / landed with Deno Deploy path
- **CT** `Codex` Deno live ingestion code path — MERGED PRs #754/#756/#757/#758/#760/#762/#764/#766/#769. Ops/parity follow-up remains in Active above
- **CT** `Antigravity` Time Filter Dropdown & Section Heading Styling — MERGED via #775. `#trGlobalWindow` on main
- **CT** `Claude` PR #649/555 deploy split — CLOSED (not merged); production deploy is `deploy-deno.yml`
- **CT** Deferred audit High/Medium (batchExtract Promise.all uploads, visionLlm chunking, PWA touch targets) — ALREADY ON MAIN (pMap concurrency 25; PR #541 massive-context skip; PR #419 a11y). Large `dashboardHtml.ts` → PWA migration remains a product program, not an open hotfix
- **CT** Deno Deploy & Turso Target: Integrated Deno server entrypoints (`src/deno/main.ts`), Deno Hono routing (`src/app.ts`), and Deno queue handlers (`src/queueHandlers.ts`). Updated `package.json` deploy script to use `deployctl` targeting Deno Deploy (`congress-trade`) and Turso database. Deprecated Cloudflare Workers / D1
- **CT** Top-Level Timeframe Filter: Added a single top-level Timeframe dropdown (`#trGlobalWindow`) to the Trends view toolbar, defaulting to Past 3 Months (`90d`). Styled section heading timeframes in italics (`<em class="tr-window-label">`)
- **CT** CI Runner Policy: Fixed `check-actions-runner-policy.mjs` error by updating `.github/workflows/auto-update-prs.yml` to target `[self-hosted, congress-ci]` and pinning action to commit SHA
- **CT** Fonts: Imported custom Zilla Slab font (Regular & Bold) into the Xcode project, registered in `.pbxproj` via `INFOPLIST_KEY_UIAppFonts`, and applied globally in SwiftUI via `App.swift`
- **CT** App Icon: Updated `AppIcon.appiconset` with the new custom logo resized to standard 1024x1024 resolution
- **CT** Portrait & Logo Porting: Integrated phase-based `AsyncImage` with party/chamber emoji fallbacks for profile pictures. Set up dynamic company logo fetches requesting light theme variants from the `/api/logos/ticker` endpoint, falling back to a monogram for non-ticker asset types (like House type codes)
- **CT** `Cursor` Executive Defaults & Cache Safety: Split `defaultChambers` from `initialChambers` so default UI selections include Executive disclosures while keeping backend default compatibility intact. Added `cacheHasExecutiveTrades()` checks on `cursorStore` to prevent mixed-cache sync — bugs
- **CT** Segmented Appearance Settings: Surfaced a segmented control in the Watchlist tab supporting "Match System", "Light", and "Dark" selections, updating the preferred color scheme at the application level
- **CT** Verification: Clean Xcode simulator build succeeded, and backend typecheck + full test suite passed
- **CT** PR 605 (SwiftUI Client): Clamped backoff delay to a max of 15 seconds in `CongressTradeStore.swift` to resolve UI freeze during 429 rate limiting. Squash-merged
- **CT** PR 607 (Ingestion Gaps): Integrated and merged to resolve ingestion discovery gaps
- **CT** PR 606 (Subscription Lifecycle): Implemented `POST /api/admin/subscriptions/:id/rotate-secret` (shown-once Bearer rotation) and `POST /api/admin/subscriptions/:id/deactivate` (frees slot from total quota, disables delivery). Updated SSE loop to query active status from D1 on each tick to terminate deactivated streams immediately. Resolved rebase conflicts in `migrations.ts` and `migrati
- **CT** `Antigravity` Deferred Audit Report Items — PLANNED/DEFERRED. The following items from the comprehensive audit report remain deferred for future work
- **CT** Backend: Refactor sequential uploads in `batchExtract.ts` to use `Promise.all()` (High); Re-evaluate PDF chunking in `visionLlm.ts` to leverage large context windows/caching (Medium); Implement robust JSON parsing instead of regex in `visionLlm.ts` and `bakeoff.ts` (Medium); Address memory pressure in `textPdf.ts` and string manipulation overhead in `consensus.ts` (Low)
- **CT** Frontend: Fix PWA mobile grid overflow and touch targets; migrate the 7,145-line `dashboardHtml.ts` logic to the modular Next.js PWA
- **CT** `Codex` Review Queue current drain + durable automation integration — DEPLOYED
- **CT** `Codex` Whole-app improvement roadmap implementation — IMPLEMENTATION COMPLETE LOCALLY +
- **CT** `Claude` `Codex` autofix: migrate CI loop from Anthropic to DeepSeek — DEPLOYED
- **CT** (record production Worker releases here after explicit owner-approved deploys)
- **CT** Follow-ups batch: brand archive + Zilla wordmark + exec filer enrichment + workerd diagnostics
- **CT** `Claude` Ingestion fetch outage: R2 known-length regression fix + dead-letter recovery
- **CT** `Claude` Executive-branch (Trump) trade tracking — OGE Form 278-T ingestion — BUILT
- **CT** `Claude` Public latency showcase + public delivery education + anti-scrape hardening
- **CT** `Claude` Shared-dep tokenless git-dependency switch . Both halves merged
- **CT** `Claude` PR #162 - Effort-issues sync secondary-rate-limit hardening . Merged to `main`
- **CT** (seeded empty — see repo git history for pre-protocol work)
- **CT** `Claude` 2026-08-19 — PLANNED — [Review] Delivery and alerts: the paid feature does not deliver (29 findings — P0:2 P1:7 P2:6 P3:11 P4:3). From the 2026-08-19 full-app review (467 curated findings across 14 themes). Track status, mark addressed, and comment on fixes: `https://mac.jays.services/board?app=congress-trade&severity=P0,P1,P2` (Bearer token in `~/.secrets/mac-collab.env`) or
- **CT** Web: delivery pause/resume/delete + filter editing (unassigned, M)
- **CT** Wave 4 go-live: configure auth + Stripe paywall services (unassigned, M) — board reservation
- **UM** `Codex` Infisical provider-credential auto-sync ( delegated implementation + security/runtime reviewers, owner-directed
- **UM** `Codex` Remaining-provider automatic enrichment implementation wave ( + provider teams
- **UM** `Antigravity` App-wide UI/UX Responsive and Accessibility Refinements — COMPLETED: Adding skeleton loaders, fixing table responsiveness on mobile, and semantic HTML fixes in ProviderCard. Merged implicitly into `main` via PR #66
- **UM** Bound generic usage-ingest request bodies before JSON decoding (unassigned, S) — MERGED PR #311 / DEPLOYED. OTLP ingest uses
- **UM** `Antigravity` Generic Service Cost Tracking & Project Schema Update — MERGED PR #66 / DEPLOYED. — COMPLETED: Decoupling API from Service in Provider, adding `Project` and `ProviderProjectAllocation` tables via Prisma to allow fractional cost attribution. (From architecture audit)
- **UM** `Claude` Fix /api/budget-status 401: exclude it from the dashboard-session middleware matcher — MERGED PR #58 / DEPLOYED
- **UM** `Antigravity` Resolve Agent Sync Relay noise and Anthropic must-keep-funded alerts — MERGED PR #113 / DEPLOYED. Updated `ensureAgentSyncProviderSeeded` to automatically disable the Agent Sync Relay provider on startup/poll, silencing the spurious missing_snapshot PagerDuty alerts. Also added a migration step in the same boot sequence to unflag `mustKeepFunded` for Anthropic since Anthropic does
- **UM** `Grok` iOS staleness banners + fetch coalescing + subscriptions read UI (P2, M) — PLANNED. Wire `BudgetStaleness`; single in-flight `BudgetStore` fetch; surface `APIClient.subscriptions()`
- **UM** `Grok` Producer retry-storm contract (ST/CT/OTLP wrappers) (P0, L, cross-repo) — PLANNED. Honor Retry-After; exponential backoff + circuit breaker; treat HTTP 202 as success regardless of `accepted`; never spin on `accepted: 0`. Cross-board rows on Socratic.Trade / Congress.Trade / shared as needed. Evidence: historical OOM→35rps overage
- **UM** `Grok` Dark-mode pass on Projects, Attention, Sentry, dashboard chrome (P1, S) — PLANNED. Complements residual dark-mode planned row
- **UM** `Grok` Cross-repo telemetry contract CI lock (P1, M) — PLANNED. Shared package vectors/enums vs `usage-telemetry.ts`; pin version. Cross: congress-trading-shared
- **UM** `Grok` Producer hard rules: always occurredAt ISO + explicit per-call idempotencyKey (P1, M, cross-repo) — PLANNED. Fix random-UUID when occurredAt missing; normalize ISO in basis only with coordinated bump
- **UM** `Grok` Optional verified-preferred cash mode for OpenRouter when coverage high (P2, L) — PLANNED. Audit layer today does not correct budgets
- **UM** Capture exact OpenAI, Mistral, and Google recurring subscription terms (unassigned, M). Current production has no local Subscription rows for these providers, and the integrated official usage/cost APIs do not expose the owner's consumer subscription purchase terms. Import an exact receipt or owner-supplied amount, currency, cadence, current-period start/end, renewal behavior, provider
- **UM** Implement OTLP logs ingestion (unassigned, L, deliberately deferred) — `/api/otlp/v1/logs`
- **shared** Renamed remaining "Agentic Trading" references to "Socratic Trade" (PR #119)
- **shared** Added Zod schemas for AmountBracket, Subscription, and SseMessage (PR #119)
- **shared** Expanded client.ts and SseParser test coverage to 337 tests (PR #119)
- **shared** Refined AmountBracketSchema to reject inverted bounds (PR #119)
- **shared** Fixed TypeScript 6.0.3 and Zod v4 compatibility issues in tsup/schemas (PR #119)
- **shared** Unified ticker normalizer regex & preferred/depositary helper functions (PR #97)
- **shared** Relocated STOCK Act AmountBracket definitions & snapping/matching helpers (PR #97)
- **shared** Aligned Zod schemas for ClientAsset and ClientTrade with production API outputs (PR #98)
- **shared** Vitest CI test suite execution with strict code coverage minimum thresholds (PR #96)
- **shared** Tokenless smoke-install verification job in CI (PR #96)
- **shared** Corrected docs/RELEASE.md consumer notification list (PR #96)
- **shared** CongressTradeClient + SUBSCRIPTIONS API path (PR #55)
- **shared** balance/limit metricTypes (PR #56)
- **shared** createCongressEvent helper and type dedup (PR #57)
- **shared** Dependabot + weekly CI audit (PR #54)
- **shared** (n/a for pre-1.3.0 — library package; "deployed" = version published/consumed by apps)
- **shared** `Codex` Protect immutable release tags and enable repository-native security controls
- **shared** `Claude` `Codex` autofix reusable workflow: migrate from Anthropic to DeepSeek
- **shared** Make exact-pin drift checks tokenless, symmetric, and fail-closed (cross-app, P1/M)
- **shared** `Antigravity` Split `TICKER_ALIASES` into rename-vs-acquisition classes — shared portion done in v1.3.0; consumer migration pending. ATVI→MSFT is

## 2026-08-18

*39 PRs merged · 21 issues opened · 80 issues closed · 9 effort rows*

### Merged PRs

- **CT** [#1989](https://github.com/jaywedgeworth22/Congress.Trade/pull/1989): chore(deps): bump @aws-sdk/client-s3 from 3.1110.0 to 3.1111.0 in /app _(by dependabot[bot])_
- **CT** [#1990](https://github.com/jaywedgeworth22/Congress.Trade/pull/1990): Fix false extract auth halt so cheap path can run _(by jaywedgeworth22)_
- **CT** `Grok` [#1992](https://github.com/jaywedgeworth22/Congress.Trade/pull/1992): fix(storage): stop leaking R2 Unauthorized as /raw 500 _(by jaywedgeworth22)_
- **CT** [#1993](https://github.com/jaywedgeworth22/Congress.Trade/pull/1993): iOS Admin panel and Review Queue (#1991) _(by jaywedgeworth22)_
- **CT** [#1995](https://github.com/jaywedgeworth22/Congress.Trade/pull/1995): iOS Admin: session Bearer + no ADMIN_TOKEN field (#1991) _(by jaywedgeworth22)_
- **CT** `Grok` [#1997](https://github.com/jaywedgeworth22/Congress.Trade/pull/1997): Apply Buys/Sells filter to Trends analytics _(by jaywedgeworth22)_
- **CT** `Grok` [#1998](https://github.com/jaywedgeworth22/Congress.Trade/pull/1998): Close out Trends side-filter board row _(by jaywedgeworth22)_
- **CT** `Grok` [#1999](https://github.com/jaywedgeworth22/Congress.Trade/pull/1999): Apply shared filters to every Trends surface _(by jaywedgeworth22)_
- **CT** `Grok` [#2000](https://github.com/jaywedgeworth22/Congress.Trade/pull/2000): Close out filters-everywhere board row _(by jaywedgeworth22)_
- **CT** `Grok` [#2001](https://github.com/jaywedgeworth22/Congress.Trade/pull/2001): Restore party and multi-side from the URL _(by jaywedgeworth22)_
- **CT** [#2002](https://github.com/jaywedgeworth22/Congress.Trade/pull/2002): No public extract card; Admin nav badges; selector due-now drain _(by jaywedgeworth22)_
- **CT** [#2004](https://github.com/jaywedgeworth22/Congress.Trade/pull/2004): Publish cheap openRouterText PTRs at the 0.55 bar _(by jaywedgeworth22)_
- **CT** [#2006](https://github.com/jaywedgeworth22/Congress.Trade/pull/2006): Close out #2002 effort-log claim _(by jaywedgeworth22)_
- **CT** [#2010](https://github.com/jaywedgeworth22/Congress.Trade/pull/2010): Remove broken email magic-link sign-in _(by jaywedgeworth22)_
- **CT** [#2012](https://github.com/jaywedgeworth22/Congress.Trade/pull/2012): Close out #2010 effort-log claim _(by jaywedgeworth22)_
- **CT** [#2013](https://github.com/jaywedgeworth22/Congress.Trade/pull/2013): Share ToS and Privacy Policy heading and theme chrome _(by jaywedgeworth22)_
- **CT** [#2017](https://github.com/jaywedgeworth22/Congress.Trade/pull/2017): Polish mobile web chrome: one filter row, restore theme switcher, drop Capitol Ledger _(by jaywedgeworth22)_
- **CT** [#2018](https://github.com/jaywedgeworth22/Congress.Trade/pull/2018): Close out #2017 effort-log claim _(by jaywedgeworth22)_
- **CT** [#2020](https://github.com/jaywedgeworth22/Congress.Trade/pull/2020): Remove Largest Buys and Largest Sells from Trends _(by jaywedgeworth22)_
- **CT** [#2021](https://github.com/jaywedgeworth22/Congress.Trade/pull/2021): Close out #2020 in the effort log _(by jaywedgeworth22)_
- **ST** [#2800](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2800): fix(rag): stop parking Pinecone writes on a 15-WU local-MTD remainder _(by jaywedgeworth22)_
- **ST** [#2812](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2812): fix(health): one dead rag-embed must not 503 Docker or halt autonomy _(by jaywedgeworth22)_
- **ST** [#2829](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2829): fix(llm): stop require_parameters=true on every OpenRouter body _(by jaywedgeworth22)_
- **ST** [#2830](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2830): fix(scan): Nasdaq screener UA + retry so Scan returns names _(by jaywedgeworth22)_
- **ST** [#2831](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2831): fix(llm): Green 400 must fail over; do not pick terra first _(by jaywedgeworth22)_
- **ST** `Grok` `Cursor` [#2832](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2832): docs(effort): close Review UX leftover; leave favicon to _(by jaywedgeworth22)_
- **ST** [#2840](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2840): fix(rag): pack embed POSTs under the bge-m3 8192 window _(by jaywedgeworth22)_
- **ST** [#2844](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2844): docs(rag): close #2840 batch-window effort as merged _(by jaywedgeworth22)_
- **ST** [#2845](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2845): fix(broker): retry slow first getAccounts after deploy swap _(by jaywedgeworth22)_
- **ST** [#2847](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2847): Close sweep-failed request so Manual Run once is not locked _(by jaywedgeworth22)_
- **ST** [#2848](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2848): Pause ROIC/FTS so Manual Run once can reach Green _(by jaywedgeworth22)_
- **ST** [#2850](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2850): iOS Scan keeps last-good universe when Refresh 503s _(by jaywedgeworth22)_
- **ST** [#2851](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2851): fix(console): guard module-scope process.uptime so /console/connections renders (#2848 follow-up) _(by jaywedgeworth22)_
- **ST** [#2852](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2852): fix(quotes): chunk Robinhood get_equity_quotes to max 10 _(by jaywedgeworth22)_
- **ST** [#2853](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2853): Resume claimed Manual Run once so drain can start Green _(by jaywedgeworth22)_
- **ST** [#2855](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2855): Show “S&P 500”, not “sp500”, on Indices rows _(by jaywedgeworth22)_
- **ST** [#2856](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2856): Show common index names on every Indices surface _(by jaywedgeworth22)_
- **fleet** `Grok` [#41](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/41): docs: Shellular — ACP argv and — :12419 _(by jaywedgeworth22)_
- **fleet** `Grok` [#42](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/42): docs: shared — for local chat control _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1474](https://github.com/jaywedgeworth22/Congress.Trade/issues/1474): 2026-08-05 — R2 Class A emergency pause (host litestream-congress
- **CT** [#1475](https://github.com/jaywedgeworth22/Congress.Trade/issues/1475): iOS TestFlight agent ship pipeline (cross-app) — IN PR 2026-08-04 (ST
- **CT** [#1476](https://github.com/jaywedgeworth22/Congress.Trade/issues/1476): 2026-08-06T14:19Z — IN PROGRESS — Latency week focus: track
- **CT** [#1477](https://github.com/jaywedgeworth22/Congress.Trade/issues/1477): 2026-08-06T05:10Z — IN PROGRESS — Web+iOS filter parity, brand header
- **CT** [#1483](https://github.com/jaywedgeworth22/Congress.Trade/issues/1483): Full-product review follow-ups 2026-08-06 (unassigned; hand-made issues
- **CT** [#1497](https://github.com/jaywedgeworth22/Congress.Trade/issues/1497): 2026-08-07 — COMPLETED — Capitalize Congress/Congressional in product
- **CT** [#1514](https://github.com/jaywedgeworth22/Congress.Trade/issues/1514): 2026-08-07T16:09Z — IN PROGRESS — Agreement cascade: soft free-text must
- **CT** [#1539](https://github.com/jaywedgeworth22/Congress.Trade/issues/1539): 2026-08-08T18:55Z — IN PROGRESS — iOS xcodeproj brand rename
- **CT** [#1542](https://github.com/jaywedgeworth22/Congress.Trade/issues/1542): 2026-08-09 — IN PR — Web punch list #2 — web chrome + drawers (Lanes
- **CT** [#1543](https://github.com/jaywedgeworth22/Congress.Trade/issues/1543): 2026-08-09 — IN PR (auto-merge enabled) — iOS punch list lane I1+I2
- **CT** [#1545](https://github.com/jaywedgeworth22/Congress.Trade/issues/1545): 2026-08-08T20:40Z — IN PR — Root cause: empty SQLITEWEBPASSWORD →
- **CT** [#1548](https://github.com/jaywedgeworth22/Congress.Trade/issues/1548): 2026-08-09 — IN PR (auto-merge enabled) — iOS multi-select filter pills
- **CT** [#1552](https://github.com/jaywedgeworth22/Congress.Trade/issues/1552): 2026-08-09 — IN PR (auto-merge enabled) — Web owner follow-up batch #2
- **CT** [#1559](https://github.com/jaywedgeworth22/Congress.Trade/issues/1559): 2026-08-09 — IN PR (auto-merge enabled) — iOS Sign in with Apple +
- **CT** [#1563](https://github.com/jaywedgeworth22/Congress.Trade/issues/1563): 2026-08-09 — IN PR (auto-merge enabled) — SECURITY: Apple JWS x5c full
- **CT** [#1567](https://github.com/jaywedgeworth22/Congress.Trade/issues/1567): 2026-08-09 — IN PR (auto-merge enabled) — Trades-tab count accuracy (3
- **CT** [#1578](https://github.com/jaywedgeworth22/Congress.Trade/issues/1578): 2026-08-09 — IN PR (auto-merge enabled) — Review-queue false "all done"
- **CT** [#1580](https://github.com/jaywedgeworth22/Congress.Trade/issues/1580): 2026-08-09 — IN PR (auto-merge enabled) — Ingestion pipeline autonomy
- **CT** [#1591](https://github.com/jaywedgeworth22/Congress.Trade/issues/1591): 2026-08-09 — DEPLOYED — Lane 2: deterministic-only stuck-filing
- **CT** [#1598](https://github.com/jaywedgeworth22/Congress.Trade/issues/1598): 2026-08-09 — IN PR (auto-merge enabled) — Icon/tooltip color fixes
- **CT** [#1601](https://github.com/jaywedgeworth22/Congress.Trade/issues/1601): 2026-08-09T22:21Z — IN PROGRESS — Social OG share image light refresh
- **CT** [#1616](https://github.com/jaywedgeworth22/Congress.Trade/issues/1616): 2026-08-09 — COMPLETED/MERGED (#1613) — Owner web/iOS UX punchlist
- **CT** [#1619](https://github.com/jaywedgeworth22/Congress.Trade/issues/1619): 2026-08-09 5:55pm CT — COMPLETED — Senate 5-year historical backfill
- **CT** [#1625](https://github.com/jaywedgeworth22/Congress.Trade/issues/1625): 2026-08-10 12:55am CT — COMPLETED — 5-year/3-branch reconciliation
- **CT** [#1626](https://github.com/jaywedgeworth22/Congress.Trade/issues/1626): 2026-08-09 9:30pm CT — superseded by the 12:55am completion row above
- **CT** [#1628](https://github.com/jaywedgeworth22/Congress.Trade/issues/1628): 2026-08-10 1:08am CT — IN PROGRESS — OpenRouter app classifier
- **CT** [#1636](https://github.com/jaywedgeworth22/Congress.Trade/issues/1636): 2026-08-10 — IN PR — Price staleness root-cause fix
- **CT** [#1642](https://github.com/jaywedgeworth22/Congress.Trade/issues/1642): 2026-08-10 — IN PR — Member identity cleanup: campaign-sign names
- **CT** [#1659](https://github.com/jaywedgeworth22/Congress.Trade/issues/1659): 2026-08-10 1:45am CT — DEPLOYED — Owner UI feedback lane: buys/sells
- **CT** [#1666](https://github.com/jaywedgeworth22/Congress.Trade/issues/1666): 2026-08-10 — IN PR — Trade-details grid, delivery — labels
- **CT** [#1673](https://github.com/jaywedgeworth22/Congress.Trade/issues/1673): 2026-08-10 — IN PR — Web UX trades chrome + full UI expert review
- **CT** [#1674](https://github.com/jaywedgeworth22/Congress.Trade/issues/1674): 2026-08-10 ~afternoon CT — IN PROGRESS/LANDING — iOS auth Settings
- **CT** [#1676](https://github.com/jaywedgeworth22/Congress.Trade/issues/1676): 2026-08-10 — COMPLETED/DEPLOYED — Full member-identity +
- **CT** [#1677](https://github.com/jaywedgeworth22/Congress.Trade/issues/1677): 2026-08-10 — COMPLETED/DEPLOYED — Identity resolver v2
- **CT** [#1686](https://github.com/jaywedgeworth22/Congress.Trade/issues/1686): 2026-08-10 1:15pm CT — COMPLETED/DEPLOYED — congress.trade 6h45m
- **CT** [#1687](https://github.com/jaywedgeworth22/Congress.Trade/issues/1687): 2026-08-10 1:15pm CT — IN PROGRESS (owner-blocked) — iOS App Store 1.0
- **CT** [#1699](https://github.com/jaywedgeworth22/Congress.Trade/issues/1699): 2026-08-10 8:55pm CT — IN PR — Social share cards rebuilt: near-white
- **CT** [#1718](https://github.com/jaywedgeworth22/Congress.Trade/issues/1718): 2026-08-11 12:40pm CT — COMPLETED/APPLIED — Deploy pile-up: serialized
- **CT** [#1719](https://github.com/jaywedgeworth22/Congress.Trade/issues/1719): 2026-08-11 — IN PR (#1713) — Scanned-PDF extraction recovery
- **CT** [#1735](https://github.com/jaywedgeworth22/Congress.Trade/issues/1735): 2026-08-11 — IN PR — Admin panel: LLM spend by model + live LlamaParse
- **CT** [#1736](https://github.com/jaywedgeworth22/Congress.Trade/issues/1736): 2026-08-11 1:05pm CT — COMPLETED — Outage post-mortem closed out
- **CT** [#1753](https://github.com/jaywedgeworth22/Congress.Trade/issues/1753): 2026-08-11 5:07pm CT — IN PR (#1750) — iOS Assets directory: data
- **CT** [#1765](https://github.com/jaywedgeworth22/Congress.Trade/issues/1765): 2026-08-11 ~2:05pm CT — COMPLETED/MERGED (#1711, #1724) — App
- **CT** [#1804](https://github.com/jaywedgeworth22/Congress.Trade/issues/1804): 2026-08-12 12:22pm CT — IN PR — Effort Issues Sync: retry transient
- **CT** [#1805](https://github.com/jaywedgeworth22/Congress.Trade/issues/1805): 2026-08-12 ~8:20pm CT — COMPLETED — Open-issues resolve batch: dead
- **CT** [#1806](https://github.com/jaywedgeworth22/Congress.Trade/issues/1806): 2026-08-12 ~6:40pm CT — COMPLETED/APPLIED — iOS version naming is now
- **CT** [#1807](https://github.com/jaywedgeworth22/Congress.Trade/issues/1807): 2026-08-12 4:45am CT — MERGED (#1782, deployed via auto-merge)
- **CT** [#1808](https://github.com/jaywedgeworth22/Congress.Trade/issues/1808): 2026-08-12 2:05am CT — IN PR — Member photos: licence check widened
- **CT** [#1809](https://github.com/jaywedgeworth22/Congress.Trade/issues/1809): 2026-08-11 ~12:35pm CT — COMPLETED/DEPLOYED — Full — chat closeout +
- **CT** [#1826](https://github.com/jaywedgeworth22/Congress.Trade/issues/1826): 2026-08-12 — COMPLETED/MERGED (#1821 f204c688) — Fleet deploy-guard
- **CT** [#1827](https://github.com/jaywedgeworth22/Congress.Trade/issues/1827): 2026-08-12 — COMPLETED/MERGED (#1820 7634fe61) — Land remaining open PRs
- **CT** [#1828](https://github.com/jaywedgeworth22/Congress.Trade/issues/1828): 2026-08-12 12:25pm CT — COMPLETED/MERGED via #1820 (7634fe61;
- **CT** [#1829](https://github.com/jaywedgeworth22/Congress.Trade/issues/1829): 2026-08-12 — COMPLETED/MERGED (#1796 4e6371d8; closeout PR #1798
- **CT** [#1830](https://github.com/jaywedgeworth22/Congress.Trade/issues/1830): 2026-08-12 1:25pm CT — IN PR — Effort Issues Sync: the transport retry
- **CT** [#1831](https://github.com/jaywedgeworth22/Congress.Trade/issues/1831): 2026-08-12 — IN PROGRESS — iOS Directory/Trades/Trends chrome: Name sort
- **CT** [#1838](https://github.com/jaywedgeworth22/Congress.Trade/issues/1838): 2026-08-13 3:37pm CT — IN PROGRESS — CI and iOS ship never ran on
- **CT** [#1861](https://github.com/jaywedgeworth22/Congress.Trade/issues/1861): 2026-08-14 — IN PROGRESS — iOS Trades sort grouping + search-slot status
- **CT** [#1955](https://github.com/jaywedgeworth22/Congress.Trade/issues/1955): 2026-08-17 — IN PROGRESS — Review Queue chips name the extraction
- **CT** [#1971](https://github.com/jaywedgeworth22/Congress.Trade/issues/1971): 2026-08-17 — IN PR #1963 — #1529 design convergence + #1459 Capitol
- **CT** [#1991](https://github.com/jaywedgeworth22/Congress.Trade/issues/1991): iOS admin panel + review queue (clients/ios, same /api/admin/ as web)
- **CT** [#2007](https://github.com/jaywedgeworth22/Congress.Trade/issues/2007): 2026-08-19 — COMPLETED/MERGED #2002 (85691594) — No public extract
- **CT** [#2008](https://github.com/jaywedgeworth22/Congress.Trade/issues/2008): Remove broken email magic-link sign-in
- **CT** [#2016](https://github.com/jaywedgeworth22/Congress.Trade/issues/2016): Polish mobile web chrome: one filter row, restore theme switcher, drop Capitol Ledger
- **CT** [#2019](https://github.com/jaywedgeworth22/Congress.Trade/issues/2019): Remove Largest Buys and Largest Sells from Trends
- **ST** [#2752](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2752): Review UX: fast approve, live vs proposed price, Retry Red Team, clearer agent controls
- **ST** [#2774](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2774): 2026-08-16 — IN PROGRESS — Review UX: fast approve, live vs proposed
- **ST** [#2775](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2775): 2026-08-15 — IN PROGRESS — Website favicon: cropped offset candlestick
- **ST** [#2776](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2776): Fix ST Litestream wedge and prefer Pushover over Resend
- **ST** [#2777](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2777): Durable litestream remote-inventory cache (PR #2665
- **ST** [#2786](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2786): Green-Team empty/malformed failover +
- **ST** [#2789](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2789): Retire FilingAPI.dev — use ROIC.ai only — IN PROGRESS
- **ST** [#2836](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2836): 2026-08-16 — COMPLETED via #2757 — Review UX: fast approve, live vs
- **ST** [#2837](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2837): Prefer Pushover over Resend — COMPLETED via #2698
- **ST** [#2838](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2838): Durable litestream remote-inventory cache — COMPLETED
- **ST** [#2839](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2839): 2026-08-17 — CANCELLED — FilingAPI Plus checkout. Owner later kept the
- **ST** [#2843](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2843): rag-embed DeepInfra batch-window 400 — IN PROGRESS
- **ST** [#2846](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2846): rag-embed DeepInfra batch-window 400
- **shared** [#248](https://github.com/jaywedgeworth22/congress-trading-shared/issues/248): ISO 8601 UTC date/time formatting contract
- **shared** [#265](https://github.com/jaywedgeworth22/congress-trading-shared/issues/265): Effort-sync transport-level retry — IN PR
- **shared** [#273](https://github.com/jaywedgeworth22/congress-trading-shared/issues/273): 2026-08-17 — BOARD HYGIENE — ISO 8601 already shipped as v2.3.0

### Issues opened

- **CT** [#1988](https://github.com/jaywedgeworth22/Congress.Trade/issues/1988): [Socratic.Trade] Data sources overhaul: fix STOPPED lanes, strip QQ, FMP
- **CT** [#1991](https://github.com/jaywedgeworth22/Congress.Trade/issues/1991): iOS admin panel + review queue (clients/ios, same /api/admin/ as web)
- **CT** [#1994](https://github.com/jaywedgeworth22/Congress.Trade/issues/1994): 2026-08-18 — IN PR #1993 — #1991 iOS Admin + Review Queue (branch
- **CT** [#1996](https://github.com/jaywedgeworth22/Congress.Trade/issues/1996): 2026-08-18 — IN PR #1995 — #1991 iOS Admin session Bearer (follow-up
- **CT** [#2003](https://github.com/jaywedgeworth22/Congress.Trade/issues/2003): Public Extraction Halted banner + eligible-due drain (nav badges)
- **CT** [#2005](https://github.com/jaywedgeworth22/Congress.Trade/issues/2005): 2026-08-18 — IN PROGRESS — No public extract card; Admin nav badges;
- **CT** [#2007](https://github.com/jaywedgeworth22/Congress.Trade/issues/2007): 2026-08-19 — COMPLETED/MERGED #2002 (85691594) — No public extract
- **CT** [#2008](https://github.com/jaywedgeworth22/Congress.Trade/issues/2008): Remove broken email magic-link sign-in
- **CT** [#2009](https://github.com/jaywedgeworth22/Congress.Trade/issues/2009): OpenRouter reply-routing: no halt latch on garbage/Unauthorized
- **CT** [#2016](https://github.com/jaywedgeworth22/Congress.Trade/issues/2016): Polish mobile web chrome: one filter row, restore theme switcher, drop Capitol Ledger
- **CT** [#2019](https://github.com/jaywedgeworth22/Congress.Trade/issues/2019): Remove Largest Buys and Largest Sells from Trends
- **ST** [#2833](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2833): Live prod triage 2026-08-18
- **ST** [#2835](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2835): 2026-08-15 — IN PROGRESS — Website favicon: cropped offset candlestick
- **ST** [#2836](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2836): 2026-08-16 — COMPLETED via #2757 — Review UX: fast approve, live vs
- **ST** [#2837](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2837): Prefer Pushover over Resend — COMPLETED via #2698
- **ST** [#2838](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2838): Durable litestream remote-inventory cache — COMPLETED
- **ST** [#2839](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2839): 2026-08-17 — CANCELLED — FilingAPI Plus checkout. Owner later kept the
- **ST** [#2843](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2843): rag-embed DeepInfra batch-window 400 — IN PROGRESS
- **ST** [#2846](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2846): rag-embed DeepInfra batch-window 400
- **shared** [#273](https://github.com/jaywedgeworth22/congress-trading-shared/issues/273): 2026-08-17 — BOARD HYGIENE — ISO 8601 already shipped as v2.3.0
- **shared** [#274](https://github.com/jaywedgeworth22/congress-trading-shared/issues/274): 2026-08-17 — BOARD HYGIENE — July 2026 cross-app leftovers parked

### Effort board

- **CT** `Grok` `Cursor` 2026-08-18 — IN PROGRESS — Cheap openRouterText publish bar (branch `grok/extract-halt-banner`, worktree `~/apps/congress — halt`). Yielded public halt banner + eligible-due start to — #2002. Complementary: `openRouterText` on `text_pdf`/`senate_html` uses the 0.55 deterministic gate so 14 live electronic PTRs at minConfidence 0.6 can drain. Terminal-only review lefto
- **CT** `Grok` 2026-08-18 — IN PROGRESS — URL restore for party + multi-side (branch `grok/filter-url-restore`). `fty=B,S` restored nothing; party never entered the URL. `meta.party` on `party=D,R` reported `"D"`
- **CT** `Grok` 2026-08-18 — COMPLETED/DEPLOYED #1999 (`9f938735`) — Shared filters on every surface (branch `grok/filters-everywhere`). Live AAPL `type=B` is 373/373/0 (unfiltered 777/373/402). Drawers and iOS sheets now send the same chips. TestFlight hourly ship still needed for the installed app
- **CT** `Grok` 2026-08-18 — COMPLETED/DEPLOYED #1997 (`5ecdb8da`) — Trends Buys/Sells chip is cosmetic (branch `grok/trends-side-filter`). Live `type=B` summary is 1446/1446/0 (was identical to mixed 2185/1446/726). Web sends `type=` now. Installed iOS picks it up on the next TestFlight hourly ship
- **CT** `Cursor` 2026-08-18 — IN PR #1995 — #1991 iOS Admin session Bearer (follow-up after #1993, branch `cursor/ios-admin-session-auth-d6f8`). #1993 landed a token field; this removes it. Gate: `GET /auth/me` → `admin.allowed` on the existing session Bearer. Backend: admin middleware + `/auth/me` use `getCurrentUserFromRequest` (cookie or Bearer). No iOS ADMIN_TOKEN field / Keychain slot. Same
- **CT** `Grok` 2026-08-18 — IN PROGRESS — RAW_FILES Unauthorized stalled new trades (branch `grok/prod-raw-500-stale-tx`). Live `/raw` 500 `Unauthorized`; latest tx 169h old. Dead `AWS_`/`CLOUDFLARE_R2_` S3 key. Working `R2_ARCHIVE_` copied onto those Infisical keys; congress-app restarted. Storage-smoke 200; PDFs serve. Requeued 320 outbox + 272 `filing.new`. Code: honest 503 + worker 300s b
- **CT** `Cursor` 2026-08-18 — IN PR #1990 — False extract auth halt (branch `cursor/extract-auth-halt-aabd`). Live halt `b315b98d-…` is bare `Unauthorized` ($0 spend, 4s, 2 House docs with R2 already stored), not a dead OpenRouter key. Key still `sk-or-v`…`3aa7` / sha12 `450ceab9559f`; `/api/v1/auth/key` 200, $2 remaining of $2/day. Classifier no longer treats source-fetch / admin / Clerk 401 statu
- **CT** `Cursor` 2026-08-18 — IN PR #1985 — Cheap-first House extract (branch `cursor/extract-cheap-path-8b05`). Typed/electronic House PTRs (20xxxxxx) do not hit OpenRouter Files. Local text + optional Flash-Lite text chat first. Files/vision only for real 822/911 scans. Letterhead / column-header / row-limit / missing-date+malformed-amount hard-stop before the agreement trio. Stay on the $2/day
- **CT** `Cursor` 2026-08-18 — IN PR #1995 — #1991 iOS Admin session Bearer (follow-up after #1993, branch `cursor/ios-admin-session-auth-d6f8`). #1993 landed a token field; this removes it. Gate: `GET /auth/me` → `admin.allowed` on the existing session Bearer. Backend: admin middleware + `/auth/me` use `getCurrentUserFromRequest` (cookie or Bearer). No iOS ADMIN_TOKEN field / Keychain slot

## 2026-08-17

*52 PRs merged · 71 issues opened · 97 issues closed · 16 effort rows*

### Merged PRs

- **CT** [#1899](https://github.com/jaywedgeworth22/Congress.Trade/pull/1899): chore(deps): bump hono from 4.13.1 to 4.13.2 in /app in the cloudflare group _(by dependabot[bot])_
- **CT** [#1900](https://github.com/jaywedgeworth22/Congress.Trade/pull/1900): chore(deps): bump @aws-sdk/client-s3 from 3.1107.0 to 3.1110.0 in /app _(by dependabot[bot])_
- **CT** [#1901](https://github.com/jaywedgeworth22/Congress.Trade/pull/1901): chore(deps): bump unpdf from 1.8.0 to 1.8.1 in /app _(by dependabot[bot])_
- **CT** [#1902](https://github.com/jaywedgeworth22/Congress.Trade/pull/1902): chore(deps): bump @google/genai from 2.16.0 to 2.17.1 in /app _(by dependabot[bot])_
- **CT** [#1903](https://github.com/jaywedgeworth22/Congress.Trade/pull/1903): fix(latency): stop calling silent probes healthy _(by jaywedgeworth22)_
- **CT** [#1904](https://github.com/jaywedgeworth22/Congress.Trade/pull/1904): docs: mark latency-probe silence closeout deployed _(by jaywedgeworth22)_
- **CT** `Grok` [#1905](https://github.com/jaywedgeworth22/Congress.Trade/pull/1905): docs(effort): board hygiene — close stale In Progress _(by jaywedgeworth22)_
- **CT** [#1951](https://github.com/jaywedgeworth22/Congress.Trade/pull/1951): Fix filter chrome, trades table, and Delivery latency _(by jaywedgeworth22)_
- **CT** [#1952](https://github.com/jaywedgeworth22/Congress.Trade/pull/1952): Mark filter chrome / Delivery latency effort row deployed _(by jaywedgeworth22)_
- **CT** [#1954](https://github.com/jaywedgeworth22/Congress.Trade/pull/1954): Show Review Queue extraction model ids, not OpenRouter _(by jaywedgeworth22)_
- **CT** [#1956](https://github.com/jaywedgeworth22/Congress.Trade/pull/1956): Mark Review Queue model-chip work merged on the effort board _(by jaywedgeworth22)_
- **CT** [#1958](https://github.com/jaywedgeworth22/Congress.Trade/pull/1958): Filings hygiene: delete probe row and reconcile review desync (#1576 #1574) _(by jaywedgeworth22)_
- **CT** [#1960](https://github.com/jaywedgeworth22/Congress.Trade/pull/1960): Diagnose House FD ZIP as healthy (#1577) _(by jaywedgeworth22)_
- **CT** [#1961](https://github.com/jaywedgeworth22/Congress.Trade/pull/1961): fix(senate): fall back to direct eFD when the Mac relay is down _(by jaywedgeworth22)_
- **CT** [#1963](https://github.com/jaywedgeworth22/Congress.Trade/pull/1963): feat(ui): web adopts iOS language + Capitol Ledger style option _(by jaywedgeworth22)_
- **CT** [#1970](https://github.com/jaywedgeworth22/Congress.Trade/pull/1970): fix(ui): drop header/filter seam and unclip filter menus _(by jaywedgeworth22)_
- **CT** `Cursor` [#1972](https://github.com/jaywedgeworth22/Congress.Trade/pull/1972): Add — Cloud dev environment for the Deno backend _(by jaywedgeworth22)_
- **CT** [#1974](https://github.com/jaywedgeworth22/Congress.Trade/pull/1974): Report-only security and operations audit (2026-08-17) _(by jaywedgeworth22)_
- **CT** [#1975](https://github.com/jaywedgeworth22/Congress.Trade/pull/1975): docs: backend durability audit (read-only) _(by jaywedgeworth22)_
- **CT** [#1977](https://github.com/jaywedgeworth22/Congress.Trade/pull/1977): Audit extraction halt, page on stop, and resume files-prepaid safely _(by jaywedgeworth22)_
- **CT** [#1984](https://github.com/jaywedgeworth22/Congress.Trade/pull/1984): fix(ios): remove web Stripe checkout from native Premium surfaces _(by jaywedgeworth22)_
- **CT** [#1985](https://github.com/jaywedgeworth22/Congress.Trade/pull/1985): Cheap-first House extract: no OpenRouter Files on electronic PTRs _(by jaywedgeworth22)_
- **ST** [#2765](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2765): build(deps): bump next from 16.3.0 to 16.3.1 in the next-react group _(by dependabot[bot])_
- **ST** [#2766](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2766): build(deps): bump @sentry/nextjs from 10.69.0 to 10.70.0 in the observability group _(by dependabot[bot])_
- **ST** [#2767](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2767): build(deps): bump lucide-react from 1.29.0 to 1.31.0 _(by dependabot[bot])_
- **ST** [#2768](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2768): build(deps): bump @pinecone-database/pinecone from 8.0.0 to 8.2.0 _(by dependabot[bot])_
- **ST** [#2769](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2769): build(deps): bump jose from 6.2.5 to 6.2.8 _(by dependabot[bot])_
- **ST** [#2771](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2771): fix(llm): dash Mistral OpenRouter slug and stop lease-lost vendor pages _(by jaywedgeworth22)_
- **ST** `Grok` [#2772](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2772): docs(effort): board hygiene — close stale In Progress _(by jaywedgeworth22)_
- **ST** [#2784](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2784): fix(llm): Green Team malformed failover + credits-exhausted run_failed hint _(by jaywedgeworth22)_
- **ST** [#2787](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2787): SUPERSEDED: Retire FilingAPI.dev — owner reversed; see #2792 _(by jaywedgeworth22)_
- **ST** [#2791](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2791): Wire settings-search catalog into the command palette _(by jaywedgeworth22)_
- **ST** [#2799](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2799): Stop treating the Pinecone Standard trial as the Starter 2M monthly wall _(by jaywedgeworth22)_
- **ST** [#2802](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2802): docs(audit): cross-app coordination among ST, CT, UM, CTS, DealDex, and fleet _(by jaywedgeworth22)_
- **ST** [#2809](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2809): docs(audit): Stripe + StoreKit purchases end-to-end (report only) _(by jaywedgeworth22)_
- **ST** [#2810](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2810): docs(audit): 2026-08-17 blind-spots register (report-only) _(by jaywedgeworth22)_
- **ST** [#2811](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2811): docs(audit): Pinecone store-more vs condense-first for Green/Red _(by jaywedgeworth22)_
- **ST** [#2815](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2815): Legal clickwrap, mandatory data-pool, keep multi-user isolation _(by jaywedgeworth22)_
- **ST** [#2819](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2819): fix(learning): drop leftover 20+5 transfer-gate docs; paper cost = OOS 20 bps _(by jaywedgeworth22)_
- **ST** [#2820](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2820): feat(rag): hybrid processed writes and safe junk prune _(by jaywedgeworth22)_
- **ST** [#2821](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2821): Per-user LLM daily budget in Settings and iOS (not Infisical) _(by jaywedgeworth22)_
- **ST** [#2822](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2822): docs(ops): scratch-only Litestream B2 restore drill receipts _(by jaywedgeworth22)_
- **ST** [#2823](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2823): docs(ops): restore-drill decrypt and R2 retain=1 now VERIFIED _(by jaywedgeworth22)_
- **ST** [#2824](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2824): docs(ops): pin restore-drill receipts; Coolify watch_paths omit _(by jaywedgeworth22)_
- **ST** [#2825](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2825): fix(ios): IRA wash-sale N/A, ordinary copy, bidirectional caps _(by jaywedgeworth22)_
- **ST** [#2826](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2826): docs: mark per-user AI daily budget #2821 completed _(by jaywedgeworth22)_
- **ST** [#2827](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2827): fix(tax): do not tax-loss harvest in Roth or Traditional IRAs _(by jaywedgeworth22)_
- **UM** [#1231](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1231): chore(deps): bump the npm-minor-and-patch group with 8 updates _(by dependabot[bot])_
- **UM** [#1232](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1232): chore(deps): bump postal-mime from 2.7.6 to 3.0.0 _(by dependabot[bot])_
- **fleet** `Grok` [#40](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/40): docs: effort-board hygiene note _(by jaywedgeworth22)_
- **shared** [#271](https://github.com/jaywedgeworth22/congress-trading-shared/pull/271): chore(deps): bump anthropics/claude-code-action from 1.0.187 to 1.0.193 _(by dependabot[bot])_
- **shared** `Grok` [#272](https://github.com/jaywedgeworth22/congress-trading-shared/pull/272): docs(effort): board hygiene — close stale In Progress _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1459](https://github.com/jaywedgeworth22/Congress.Trade/issues/1459): Adopt 'Capitol Ledger' mock elements from congresstrade.grok.me (style option + structural wins)
- **CT** [#1498](https://github.com/jaywedgeworth22/Congress.Trade/issues/1498): 2026-08-07T07:30Z — IN PROGRESS — App Store publish + scorecard hotfix
- **CT** [#1499](https://github.com/jaywedgeworth22/Congress.Trade/issues/1499): 2026-08-07T07:30Z — COMPLETED/DEPLOYED — OR budget circuit + per-doc
- **CT** [#1508](https://github.com/jaywedgeworth22/Congress.Trade/issues/1508): 2026-08-07T15:32Z — COMPLETED/DEPLOYED — Logo.dev prod wire (#1505)
- **CT** [#1510](https://github.com/jaywedgeworth22/Congress.Trade/issues/1510): 2026-08-07T15:36Z — COMPLETED — Landed iOS PRs #1500/#1501/#1502/#1504;
- **CT** [#1515](https://github.com/jaywedgeworth22/Congress.Trade/issues/1515): 2026-08-07T16:07Z — COMPLETED/DEPLOYED — Web light+dark brand lockups
- **CT** [#1529](https://github.com/jaywedgeworth22/Congress.Trade/issues/1529): Design convergence: web adopts the iOS app's design language (one system on both)
- **CT** [#1571](https://github.com/jaywedgeworth22/Congress.Trade/issues/1571): 2026-08-09T03:57Z — IN PROGRESS — Hi-res brand lockup + white-letter
- **CT** [#1576](https://github.com/jaywedgeworth22/Congress.Trade/issues/1576): Data hygiene: delete manual test-probe row S — should-not-exist-zzzz from prod filings
- **CT** [#1577](https://github.com/jaywedgeworth22/Congress.Trade/issues/1577): Check whether the House bulk FD ZIP fetch is degraded (186 persisted rows stuck filed_date-NULL past catch-up window)
- **CT** [#1587](https://github.com/jaywedgeworth22/Congress.Trade/issues/1587): 2026-08-09T04:33Z — COMPLETED/DEPLOYED — Trades pager + autonomous
- **CT** [#1604](https://github.com/jaywedgeworth22/Congress.Trade/issues/1604): Senate ingestion relay depends on an ephemeral tunnel + one agent's Mac staying on
- **CT** [#1623](https://github.com/jaywedgeworth22/Congress.Trade/issues/1623): 2026-08-10 12:50am CT — COMPLETED (code+ops) — Review-queue form-chrome
- **CT** [#1624](https://github.com/jaywedgeworth22/Congress.Trade/issues/1624): 2026-08-10 12:43am CT — IN PROGRESS — Review-queue manual assist +
- **CT** [#1630](https://github.com/jaywedgeworth22/Congress.Trade/issues/1630): 2026-08-10 1:32am CT — IN PR — OpenRouter purpose tags + workspace
- **CT** [#1634](https://github.com/jaywedgeworth22/Congress.Trade/issues/1634): 2026-08-10 1:37am CT — IN PR — District ordinals (1ˢᵗ/2ⁿᵈ/…) + count
- **CT** [#1639](https://github.com/jaywedgeworth22/Congress.Trade/issues/1639): 2026-08-10 1:57am CT — IN PR — OG lockup cards + brand asset archive
- **CT** [#1646](https://github.com/jaywedgeworth22/Congress.Trade/issues/1646): 2026-08-10 2:50am CT — DEPLOYED — Loud liveness lane complete
- **CT** [#1653](https://github.com/jaywedgeworth22/Congress.Trade/issues/1653): 2026-08-10 ~3:50am CT — COMPLETED/DEPLOYED — Vision-worker spin-loop
- **CT** [#1657](https://github.com/jaywedgeworth22/Congress.Trade/issues/1657): 2026-08-10 ~4:15am CT — COMPLETED/DEPLOYED — Stored-copy-only
- **CT** [#1671](https://github.com/jaywedgeworth22/Congress.Trade/issues/1671): 2026-08-10 ~afternoon CT — COMPLETED/MERGED (#1665) — iOS auth Settings
- **CT** [#1690](https://github.com/jaywedgeworth22/Congress.Trade/issues/1690): 2026-08-10 7:41PM CT — COMPLETED/DEPLOYED (#1684) — Admin auth: stale
- **CT** [#1720](https://github.com/jaywedgeworth22/Congress.Trade/issues/1720): 2026-08-11 — COMPLETED/DEPLOYED — Latency/scout full closeout
- **CT** [#1721](https://github.com/jaywedgeworth22/Congress.Trade/issues/1721): 2026-08-10 — COMPLETED/DEPLOYED — Latency scout handoff (#1678 + #1681)
- **CT** [#1907](https://github.com/jaywedgeworth22/Congress.Trade/issues/1907): 2026-08-17 — COMPLETED/DEPLOYED #1903 (1292feb3) — Latency probes silent
- **CT** [#1908](https://github.com/jaywedgeworth22/Congress.Trade/issues/1908): 2026-08-17 — BOARD HYGIENE — previous Active / In Progress dump (all
- **CT** [#1909](https://github.com/jaywedgeworth22/Congress.Trade/issues/1909): 2026-08-13 8:50pm CT — COMPLETED/MERGED (#1846 27e9c59d) + DEPLOYED
- **CT** [#1910](https://github.com/jaywedgeworth22/Congress.Trade/issues/1910): 2026-08-13 8:42pm CT — COMPLETED/MERGED (#1844 48a3d9f7) + TestFlight
- **CT** [#1911](https://github.com/jaywedgeworth22/Congress.Trade/issues/1911): 2026-08-13 8:35pm CT — COMPLETED/MERGED (#1843 c8c30154) + DEPLOYED
- **CT** [#1912](https://github.com/jaywedgeworth22/Congress.Trade/issues/1912): 2026-08-13 8:05pm CT — COMPLETED/MERGED (#1842 7620ac8a) — Drop
- **CT** [#1913](https://github.com/jaywedgeworth22/Congress.Trade/issues/1913): 2026-08-13 3:37pm CT — IN PROGRESS — CI and iOS ship never ran on
- **CT** [#1914](https://github.com/jaywedgeworth22/Congress.Trade/issues/1914): 2026-08-12 — IN PROGRESS — Troubleshoot UM Platforms degraded (CF CT
- **CT** [#1915](https://github.com/jaywedgeworth22/Congress.Trade/issues/1915): 2026-08-12 — DEPLOYED — Land remaining open PRs to production. Inventory
- **CT** [#1916](https://github.com/jaywedgeworth22/Congress.Trade/issues/1916): 2026-08-12 — COMPLETED/MERGED (#1821 f204c688) — Fleet deploy-guard
- **CT** [#1917](https://github.com/jaywedgeworth22/Congress.Trade/issues/1917): 2026-08-13 — COMPLETED/MERGED — Mobile & Web UI Polish
- **CT** [#1918](https://github.com/jaywedgeworth22/Congress.Trade/issues/1918): Filter chrome + trades table + Delivery filing latency
- **CT** [#1919](https://github.com/jaywedgeworth22/Congress.Trade/issues/1919): 2026-08-12 — COMPLETED/MERGED (#1823) — UI Polish, Desktop Layout
- **CT** [#1920](https://github.com/jaywedgeworth22/Congress.Trade/issues/1920): 2026-08-12 — COMPLETED/MERGED (#1810 f34b81ac) — iOS
- **CT** [#1921](https://github.com/jaywedgeworth22/Congress.Trade/issues/1921): 2026-08-12 — COMPLETED/MERGED (#1796 4e6371d8) — iOS console debug
- **CT** [#1922](https://github.com/jaywedgeworth22/Congress.Trade/issues/1922): 2026-08-11 ~11:12pm CT — COMPLETED/MERGED (#1711, #1724, #1770
- **CT** [#1923](https://github.com/jaywedgeworth22/Congress.Trade/issues/1923): 2026-08-11 ~12:20pm CT — COMPLETED/DEPLOYED — Chat closeout: enrichment
- **CT** [#1924](https://github.com/jaywedgeworth22/Congress.Trade/issues/1924): 2026-08-11 — IN PR (#1713) — Scanned-PDF extraction recovery
- **CT** [#1925](https://github.com/jaywedgeworth22/Congress.Trade/issues/1925): 2026-08-10 — COMPLETED/DEPLOYED — P0 review autonomy (A1/A3/A4) +
- **CT** [#1926](https://github.com/jaywedgeworth22/Congress.Trade/issues/1926): 2026-08-10 — IN PROGRESS — Directory chrome: larger People/Assets
- **CT** [#1927](https://github.com/jaywedgeworth22/Congress.Trade/issues/1927): 2026-08-10 ~afternoon CT — COMPLETED/MERGED — Resolve PR conflicts until
- **CT** [#1928](https://github.com/jaywedgeworth22/Congress.Trade/issues/1928): 2026-08-10 ~afternoon CT — COMPLETED/DEPLOYED — Committee/photo/price
- **CT** [#1929](https://github.com/jaywedgeworth22/Congress.Trade/issues/1929): 2026-08-10 — COMPLETED — Review-queue full drain (no OpenRouter) +
- **CT** [#1930](https://github.com/jaywedgeworth22/Congress.Trade/issues/1930): 2026-08-10 1:08am CT — SUPERSEDED — OpenRouter app classifier
- **CT** [#1931](https://github.com/jaywedgeworth22/Congress.Trade/issues/1931): 2026-08-10 1:45am CT — DEPLOYED — Owner UI feedback lane: buys/sells
- **CT** [#1932](https://github.com/jaywedgeworth22/Congress.Trade/issues/1932): 2026-08-10 12:55am CT — COMPLETED — 5-year/3-branch reconciliation
- **CT** [#1933](https://github.com/jaywedgeworth22/Congress.Trade/issues/1933): 2026-08-09 10:55pm CT — superseded by the 12:55am completion row above
- **CT** [#1934](https://github.com/jaywedgeworth22/Congress.Trade/issues/1934): 2026-08-09 5:55pm CT — COMPLETED — Senate 5-year historical backfill
- **CT** [#1935](https://github.com/jaywedgeworth22/Congress.Trade/issues/1935): 2026-08-09T22:31Z — COMPLETED/DEPLOYED — Social OG share image light
- **CT** [#1936](https://github.com/jaywedgeworth22/Congress.Trade/issues/1936): 2026-08-09T22:16Z — COMPLETED/DEPLOYED — Social OG share image: light bg
- **CT** [#1937](https://github.com/jaywedgeworth22/Congress.Trade/issues/1937): 2026-08-08T20:40Z — RECOVERED + IN PR — sqlite-web empty password
- **CT** [#1938](https://github.com/jaywedgeworth22/Congress.Trade/issues/1938): 2026-08-08T18:58Z — COMPLETED — iOS xcodeproj brand rename
- **CT** [#1939](https://github.com/jaywedgeworth22/Congress.Trade/issues/1939): 2026-08-07T16:17Z — COMPLETED/DEPLOYED — Agreement soft free-text + ST
- **CT** [#1940](https://github.com/jaywedgeworth22/Congress.Trade/issues/1940): 2026-08-07 — COMPLETED — Real iOS App Store screenshots uploaded
- **CT** [#1941](https://github.com/jaywedgeworth22/Congress.Trade/issues/1941): 2026-08-07 — IN PROGRESS — Land all open PRs to deploy. Resolve
- **CT** [#1942](https://github.com/jaywedgeworth22/Congress.Trade/issues/1942): 2026-08-07T06:10Z — IN PROGRESS — iOS BrandTitle ~50% larger in sticky
- **CT** [#1943](https://github.com/jaywedgeworth22/Congress.Trade/issues/1943): 2026-08-06T14:19Z — IN PROGRESS — Latency week focus: track
- **CT** [#1944](https://github.com/jaywedgeworth22/Congress.Trade/issues/1944): [2026-08-05] R2 free-tier survival: labels + Class A halt — HOST DONE +
- **CT** [#1945](https://github.com/jaywedgeworth22/Congress.Trade/issues/1945): 2026-08-11 — COMPLETED/DEPLOYED — Chat closeout batch. Trades UX #1669;
- **CT** [#1946](https://github.com/jaywedgeworth22/Congress.Trade/issues/1946): 2026-08-10 — COMPLETED/DEPLOYED — Web UX trades chrome (#1669 516df274)
- **CT** [#1947](https://github.com/jaywedgeworth22/Congress.Trade/issues/1947): 2026-08-06 — COMPLETED — Second CT self-hosted CI runner. Reassigned the
- **CT** [#1948](https://github.com/jaywedgeworth22/Congress.Trade/issues/1948): Land open PR queue to production — COMPLETE 2026-08-12
- **CT** [#1949](https://github.com/jaywedgeworth22/Congress.Trade/issues/1949): [2026-08-07] Fleet UI copy canon (Title Case headings; value casing;
- **CT** [#1950](https://github.com/jaywedgeworth22/Congress.Trade/issues/1950): [2026-08-07] R2 alert identity (subject Pushover logo + sent-from) +
- **CT** [#1957](https://github.com/jaywedgeworth22/Congress.Trade/issues/1957): 2026-08-17 — COMPLETED/MERGED #1954 (ad9827f5) — Review Queue chips
- **ST** [#2437](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2437): Quote cascade freshness + stale→limit never block — IN
- **ST** [#2467](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2467): iOS tab rename Coach → Insights — IN PROGRESS 2026-08-04
- **ST** [#2468](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2468): UX PR-B4 Settings sticky TOC / jump chips — IN PROGRESS
- **ST** [#2511](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2511): 2026-08-05 — COMPLETED + DEPLOYED — Open PR #2489 merged: activity-audit
- **ST** [#2558](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2558): P1: settings-search catalog (searchSettings/SETTINGS_FIELDS/glossary) is fully built but wired to no UI — wire into command palette; also indexes a phantom field
- **ST** [#2566](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2566): 2026-08-05 — COMPLETED (merged #2538 2e55e075 + DEPLOYED 2026-08-06
- **ST** [#2567](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2567): 2026-08-05 — IN PROGRESS — Fix inflated account % return (synthetic
- **ST** [#2568](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2568): Data sources overhaul (matrix, FMP OFF, soft health
- **ST** [#2569](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2569): Non-FMP data sources STOPPED fix (soft limits + Nasdaq
- **ST** [#2570](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2570): 2026-08-05 — COMPLETED + DEPLOYED via PR #2490 14f3cace 2026-08-05 (was
- **ST** [#2571](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2571): 2026-08-05 — COMPLETED + DEPLOYED via PR #2498 d614d708 2026-08-05 (was
- **ST** [#2575](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2575): [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger +
- **ST** [#2577](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2577): P2: five Green-Team runs failed Aug 6 with OpenRouter 'Empty response' across models — failover didn't save the run; correlate with credits-low
- **ST** [#2582](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2582): [2026-08-07] Fix paper vs-SPY ~+50% deposit+invest sparse snaps — IN
- **ST** [#2609](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2609): Unstick open PRs → main/prod (#2597 always-auto-merge;
- **ST** [#2630](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2630): Default light theme (fleet ruling) — IN PROGRESS
- **ST** [#2660](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2660): CI script fixes: Sentry app tag + branchless
- **ST** [#2694](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2694): Durable litestream remote-inventory cache (PR #2665's
- **ST** [#2746](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2746): ROIC transcript refresh stacked every tick and crashed prod
- **ST** [#2753](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2753): Review UX: approve speed, live vs proposed price, Retry Red Team, agent controls, PWA off
- **ST** [#2770](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2770): Fix Green Team OpenRouter slugs and stop paging lease-lost as Pinecone/rerank outages
- **ST** [#2778](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2778): FilingAPI optional key, degrade gracefully
- **ST** [#2779](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2779): 2026-08-17 — BOARD HYGIENE — moved the following verified-merged rows
- **ST** [#2780](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2780): Litestream L2/L3 + FilingAPI + ROIC earnings universe
- **ST** [#2781](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2781): 2026-08-14 — COMPLETED (docs in UM #1180) — Backup restore-proof (no ST
- **ST** [#2782](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2782): iOS full desk (Coach, Scan, Guardrails, Results, Data
- **ST** [#2783](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2783): Quote sheet Key Stats + fill/position card tap — YIELDED
- **ST** [#2790](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2790): [OWNER] FilingAPI Plus checkout. SUPERSEDED 2026-08-17

### Issues opened

- **CT** [#1906](https://github.com/jaywedgeworth22/Congress.Trade/issues/1906): 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control
- **CT** [#1907](https://github.com/jaywedgeworth22/Congress.Trade/issues/1907): 2026-08-17 — COMPLETED/DEPLOYED #1903 (1292feb3) — Latency probes silent
- **CT** [#1908](https://github.com/jaywedgeworth22/Congress.Trade/issues/1908): 2026-08-17 — BOARD HYGIENE — previous Active / In Progress dump (all
- **CT** [#1909](https://github.com/jaywedgeworth22/Congress.Trade/issues/1909): 2026-08-13 8:50pm CT — COMPLETED/MERGED (#1846 27e9c59d) + DEPLOYED
- **CT** [#1910](https://github.com/jaywedgeworth22/Congress.Trade/issues/1910): 2026-08-13 8:42pm CT — COMPLETED/MERGED (#1844 48a3d9f7) + TestFlight
- **CT** [#1911](https://github.com/jaywedgeworth22/Congress.Trade/issues/1911): 2026-08-13 8:35pm CT — COMPLETED/MERGED (#1843 c8c30154) + DEPLOYED
- **CT** [#1912](https://github.com/jaywedgeworth22/Congress.Trade/issues/1912): 2026-08-13 8:05pm CT — COMPLETED/MERGED (#1842 7620ac8a) — Drop
- **CT** [#1913](https://github.com/jaywedgeworth22/Congress.Trade/issues/1913): 2026-08-13 3:37pm CT — IN PROGRESS — CI and iOS ship never ran on
- **CT** [#1914](https://github.com/jaywedgeworth22/Congress.Trade/issues/1914): 2026-08-12 — IN PROGRESS — Troubleshoot UM Platforms degraded (CF CT
- **CT** [#1915](https://github.com/jaywedgeworth22/Congress.Trade/issues/1915): 2026-08-12 — DEPLOYED — Land remaining open PRs to production. Inventory
- **CT** [#1916](https://github.com/jaywedgeworth22/Congress.Trade/issues/1916): 2026-08-12 — COMPLETED/MERGED (#1821 f204c688) — Fleet deploy-guard
- **CT** [#1917](https://github.com/jaywedgeworth22/Congress.Trade/issues/1917): 2026-08-13 — COMPLETED/MERGED — Mobile & Web UI Polish
- **CT** [#1918](https://github.com/jaywedgeworth22/Congress.Trade/issues/1918): Filter chrome + trades table + Delivery filing latency
- **CT** [#1919](https://github.com/jaywedgeworth22/Congress.Trade/issues/1919): 2026-08-12 — COMPLETED/MERGED (#1823) — UI Polish, Desktop Layout
- **CT** [#1920](https://github.com/jaywedgeworth22/Congress.Trade/issues/1920): 2026-08-12 — COMPLETED/MERGED (#1810 f34b81ac) — iOS
- **CT** [#1921](https://github.com/jaywedgeworth22/Congress.Trade/issues/1921): 2026-08-12 — COMPLETED/MERGED (#1796 4e6371d8) — iOS console debug
- **CT** [#1922](https://github.com/jaywedgeworth22/Congress.Trade/issues/1922): 2026-08-11 ~11:12pm CT — COMPLETED/MERGED (#1711, #1724, #1770
- **CT** [#1923](https://github.com/jaywedgeworth22/Congress.Trade/issues/1923): 2026-08-11 ~12:20pm CT — COMPLETED/DEPLOYED — Chat closeout: enrichment
- **CT** [#1924](https://github.com/jaywedgeworth22/Congress.Trade/issues/1924): 2026-08-11 — IN PR (#1713) — Scanned-PDF extraction recovery
- **CT** [#1925](https://github.com/jaywedgeworth22/Congress.Trade/issues/1925): 2026-08-10 — COMPLETED/DEPLOYED — P0 review autonomy (A1/A3/A4) +
- **CT** [#1926](https://github.com/jaywedgeworth22/Congress.Trade/issues/1926): 2026-08-10 — IN PROGRESS — Directory chrome: larger People/Assets
- **CT** [#1927](https://github.com/jaywedgeworth22/Congress.Trade/issues/1927): 2026-08-10 ~afternoon CT — COMPLETED/MERGED — Resolve PR conflicts until
- **CT** [#1928](https://github.com/jaywedgeworth22/Congress.Trade/issues/1928): 2026-08-10 ~afternoon CT — COMPLETED/DEPLOYED — Committee/photo/price
- **CT** [#1929](https://github.com/jaywedgeworth22/Congress.Trade/issues/1929): 2026-08-10 — COMPLETED — Review-queue full drain (no OpenRouter) +
- **CT** [#1930](https://github.com/jaywedgeworth22/Congress.Trade/issues/1930): 2026-08-10 1:08am CT — SUPERSEDED — OpenRouter app classifier
- **CT** [#1931](https://github.com/jaywedgeworth22/Congress.Trade/issues/1931): 2026-08-10 1:45am CT — DEPLOYED — Owner UI feedback lane: buys/sells
- **CT** [#1932](https://github.com/jaywedgeworth22/Congress.Trade/issues/1932): 2026-08-10 12:55am CT — COMPLETED — 5-year/3-branch reconciliation
- **CT** [#1933](https://github.com/jaywedgeworth22/Congress.Trade/issues/1933): 2026-08-09 10:55pm CT — superseded by the 12:55am completion row above
- **CT** [#1934](https://github.com/jaywedgeworth22/Congress.Trade/issues/1934): 2026-08-09 5:55pm CT — COMPLETED — Senate 5-year historical backfill
- **CT** [#1935](https://github.com/jaywedgeworth22/Congress.Trade/issues/1935): 2026-08-09T22:31Z — COMPLETED/DEPLOYED — Social OG share image light
- **CT** [#1936](https://github.com/jaywedgeworth22/Congress.Trade/issues/1936): 2026-08-09T22:16Z — COMPLETED/DEPLOYED — Social OG share image: light bg
- **CT** [#1937](https://github.com/jaywedgeworth22/Congress.Trade/issues/1937): 2026-08-08T20:40Z — RECOVERED + IN PR — sqlite-web empty password
- **CT** [#1938](https://github.com/jaywedgeworth22/Congress.Trade/issues/1938): 2026-08-08T18:58Z — COMPLETED — iOS xcodeproj brand rename
- **CT** [#1939](https://github.com/jaywedgeworth22/Congress.Trade/issues/1939): 2026-08-07T16:17Z — COMPLETED/DEPLOYED — Agreement soft free-text + ST
- **CT** [#1940](https://github.com/jaywedgeworth22/Congress.Trade/issues/1940): 2026-08-07 — COMPLETED — Real iOS App Store screenshots uploaded
- **CT** [#1941](https://github.com/jaywedgeworth22/Congress.Trade/issues/1941): 2026-08-07 — IN PROGRESS — Land all open PRs to deploy. Resolve
- **CT** [#1942](https://github.com/jaywedgeworth22/Congress.Trade/issues/1942): 2026-08-07T06:10Z — IN PROGRESS — iOS BrandTitle ~50% larger in sticky
- **CT** [#1943](https://github.com/jaywedgeworth22/Congress.Trade/issues/1943): 2026-08-06T14:19Z — IN PROGRESS — Latency week focus: track
- **CT** [#1944](https://github.com/jaywedgeworth22/Congress.Trade/issues/1944): [2026-08-05] R2 free-tier survival: labels + Class A halt — HOST DONE +
- **CT** [#1945](https://github.com/jaywedgeworth22/Congress.Trade/issues/1945): 2026-08-11 — COMPLETED/DEPLOYED — Chat closeout batch. Trades UX #1669;
- **CT** [#1946](https://github.com/jaywedgeworth22/Congress.Trade/issues/1946): 2026-08-10 — COMPLETED/DEPLOYED — Web UX trades chrome (#1669 516df274)
- **CT** [#1947](https://github.com/jaywedgeworth22/Congress.Trade/issues/1947): 2026-08-06 — COMPLETED — Second CT self-hosted CI runner. Reassigned the
- **CT** [#1948](https://github.com/jaywedgeworth22/Congress.Trade/issues/1948): Land open PR queue to production — COMPLETE 2026-08-12
- **CT** [#1949](https://github.com/jaywedgeworth22/Congress.Trade/issues/1949): [2026-08-07] Fleet UI copy canon (Title Case headings; value casing;
- **CT** [#1950](https://github.com/jaywedgeworth22/Congress.Trade/issues/1950): [2026-08-07] R2 alert identity (subject Pushover logo + sent-from) +
- **CT** [#1953](https://github.com/jaywedgeworth22/Congress.Trade/issues/1953): 2026-08-17 — PLANNED / OWNER — Renew Quiver plan + replace
- **CT** [#1955](https://github.com/jaywedgeworth22/Congress.Trade/issues/1955): 2026-08-17 — IN PROGRESS — Review Queue chips name the extraction
- **CT** [#1957](https://github.com/jaywedgeworth22/Congress.Trade/issues/1957): 2026-08-17 — COMPLETED/MERGED #1954 (ad9827f5) — Review Queue chips
- **CT** [#1962](https://github.com/jaywedgeworth22/Congress.Trade/issues/1962): 2026-08-17 4:10pm CT — IN PR — Filings hygiene #1576 + #1574 (branch
- **CT** [#1968](https://github.com/jaywedgeworth22/Congress.Trade/issues/1968): 2026-08-16 — PLANNED / OWNER — Website Sign in with Apple Infisical
- **CT** [#1969](https://github.com/jaywedgeworth22/Congress.Trade/issues/1969): 2026-08-17 — IN PROGRESS — #1577 House bulk FD ZIP diagnosis (branch
- **CT** [#1971](https://github.com/jaywedgeworth22/Congress.Trade/issues/1971): 2026-08-17 — IN PR #1963 — #1529 design convergence + #1459 Capitol
- **CT** [#1980](https://github.com/jaywedgeworth22/Congress.Trade/issues/1980): 2026-08-17 — IN PR #1974 — Report-only security/operations audit
- **CT** [#1982](https://github.com/jaywedgeworth22/Congress.Trade/issues/1982): 2026-08-15 — PLANNED / OWNER — App Store 1.0 review. Submitted
- **CT** [#1983](https://github.com/jaywedgeworth22/Congress.Trade/issues/1983): 2026-08-17 — IN PR #1977 — Production extraction incident audit +
- **CT** [#1987](https://github.com/jaywedgeworth22/Congress.Trade/issues/1987): FMP collection on latency system + Mac scout as OFF
- **ST** [#2770](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2770): Fix Green Team OpenRouter slugs and stop paging lease-lost as Pinecone/rerank outages
- **ST** [#2773](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2773): 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control
- **ST** [#2774](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2774): 2026-08-16 — IN PROGRESS — Review UX: fast approve, live vs proposed
- **ST** [#2775](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2775): 2026-08-15 — IN PROGRESS — Website favicon: cropped offset candlestick
- **ST** [#2776](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2776): Fix ST Litestream wedge and prefer Pushover over Resend
- **ST** [#2777](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2777): Durable litestream remote-inventory cache (PR #2665
- **ST** [#2778](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2778): FilingAPI optional key, degrade gracefully
- **ST** [#2779](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2779): 2026-08-17 — BOARD HYGIENE — moved the following verified-merged rows
- **ST** [#2780](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2780): Litestream L2/L3 + FilingAPI + ROIC earnings universe
- **ST** [#2781](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2781): 2026-08-14 — COMPLETED (docs in UM #1180) — Backup restore-proof (no ST
- **ST** [#2782](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2782): iOS full desk (Coach, Scan, Guardrails, Results, Data
- **ST** [#2783](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2783): Quote sheet Key Stats + fill/position card tap — YIELDED
- **ST** [#2786](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2786): Green-Team empty/malformed failover +
- **ST** [#2789](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2789): Retire FilingAPI.dev — use ROIC.ai only — IN PROGRESS
- **ST** [#2790](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2790): [OWNER] FilingAPI Plus checkout. SUPERSEDED 2026-08-17

### Effort board

- **CT** `Cursor` 2026-08-17 — IN PR #1984 — P0 iOS no web Stripe checkout (branch `cursor/ios-no-web-checkout-738b`). App Review 3.1.1 from #1981: Delivery + empty-IAP no longer offer website Stripe checkout. Footer Pricing never Safari-opens `/pricing`. StoreKit/IAP, Restore, entitlements, existing products, and Manage Subscription (App Store vs existing Stripe portal) stay. Rebased onto main aft
- **CT** `Cursor` 2026-08-17 — IN PR — Read-only backend durability audit (branch `cursor/backend-durability-audit-b96f`). Report only: `docs/audits/2026-08-17-backend-durability.md`. Live `/api/health` HTTP 200 + JSON `stalled` (leftover OpenRouter files-prepaid halt, 316 DLQ, 149h freshness); Litestream age 2s; Senate relay up; cost profile `paid`. Accounts for open #1964 Coolify overlap (merge ≠
- **CT** `Cursor` 2026-08-17 — IN PR #1970 — Web filter chrome: no blue seam, red sell arrow, working dropdowns (branch `cursor/header-filter-seam-901b`). Header + filter bar lose the ` — border` hairline. ` — ct-main-pad` tracks the 22px phone padding so the sticky row no longer leaves a moving gap. Sell arrow is ` — sell` red. `.ios-filter` wrappers no longer inherit chip `overflow:hidden`; menus pi
- **CT** `Cursor` 2026-08-17 — IN PR #1961 — #1604 Senate relay durability (branch `cursor/senate-relay-durable-0d0e`). Named tunnel already permanent. `#1610` `/fetch-doc` kept. Direct eFD fallback when the Mac origin 502s. `GET /api/health/senate-relay` + `senate_relay` pipeline check. Gates: typecheck clean; 252 files / 3083 tests. Remaining host dependency documented
- **CT** `Grok` 2026-08-17 — COMPLETED/DEPLOYED #1951 (`c6d685b5`) — Filter chrome + trades table + Delivery latency (branch `grok/filters-table-latency`, #1918). Live sha `c6d685b5`. Filters full-bleed flush under header. Hidden-tab resize no longer paints 62px Politician. Public Filing Latency at end of Delivery (web+iOS); Trends link; hide both if behind on most providers; admin always
- **CT** `Grok` 2026-08-17 — COMPLETED/DEPLOYED #1903 (`1292feb3`) — Latency probes silent 95h (branch `grok/latency-probes-silent`). Owner was right. `/api/health/latency` 503, UptimeRobot DOWN 3d11h. Agents treated `operationalStatus=running` + stale scorecard + Quiver `lastSuccess=now` as healthy. FMP slot-1 200; rotation burned slot-2 429. Quiver 403 swallowed as 0-row success. UW 401 since A
- **CT** `Cursor` 2026-08-17 — IN PR #1977 — Production extraction incident audit + safety fixes (branch `cursor/prod-incident-audit-f506`). One branch/PR. Read-only catalog of every unresolved review_queue row + stranded/skipped/failed filings vs Clerk FD ZIP / eFD / OGE. No bulk Confirm/Reject. Aug 10 Files 402 was a $2/day key-limit prepaid hold on a funded key (fingerprint only). `local_
- **CT** `Cursor` 2026-08-17 — IN PR #1974 — Report-only security/operations audit (branch `cursor/security-ops-audit-3227`). Auth/admin boundaries, secrets, OpenRouter/Files API, billing/halt, notification/page paths, prod mutations, audit logs, PII, deps, deploy/rollback, backups/recovery. Output `docs/audits/2026-08-17-security-operations.md`. No secret values. No live destructive ops. Di
- **CT** `Cursor` 2026-08-17 — IN PROGRESS — #1577 House bulk FD ZIP diagnosis (branch `cursor/house-fd-zip-1577-e2df`). Live GET of `{YEAR}FD.ZIP` is 200 + complete (2026 rebuilt today, 1,553 members / 353 dated PTRs). Official persisted House `filed_date` NULL is now 0; 317/317 `H-2026-` persisted ids are in today's index. Remaining NULLs: 881 `not_found` frontier-probe ids (0/881 in Clerk ZIP
- **CT** `Cursor` `Grok` 2026-08-17 4:10pm CT — IN PR — Filings hygiene #1576 + #1574 (branch `cursor/filings-hygiene-1576-1574-9e2a`). Dry-run-default `POST /api/admin/filings-hygiene` deletes only the exact probe `S — should-not-exist-zzzz` (refuses if any transactions exist) and stamps resolved-review desync to `persisted` / `error` / `verified_empty`. Hourly sweep no longer writes invalid
- **CT** `Grok` `Claude` 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control board. Zero open PRs on 2026-08-17. — CI/ship landed as #1837; trades-sort as #1860; directory chrome as #1705; filter/iOS/ASC-prep rows already merged. First lines of the previous Active dump preserved under Recently completed. Rename of the Historical archive heading (below) is so effort-issues-sync does
- **CT** `Cursor` 2026-08-17 — COMPLETED/MERGED #1954 (`ad9827f5`) — Review Queue chips name the extraction model, not OpenRouter (branch `cursor/review-queue-model-chips-844a`). Pending chips were rendering `m.provider` so OpenRouter looked like the model. Chip + bake-off table show the real model id; tooltip keeps provider + model + confidence; missing model falls back to "unknown model". API
- **CT** `Grok` 2026-08-17 — COMPLETED/DEPLOYED #1903 (`1292feb3`) — Latency probes silent 95h (branch `grok/latency-probes-silent`). Owner was right. FMP live again; Quiver HTTP_403; UW 401. Owner: renew Quiver + UW token
- **CT** `Grok` 2026-08-17 — BOARD HYGIENE — previous Active / In Progress dump (all landed). First lines unchanged
- **CT** `Grok` 2026-08-17 — PLANNED / OWNER — Renew Quiver plan + replace UNUSUALWHALES_API_KEY. Latency probe closeout #1903 deployed; Quiver is HTTP_403 (upgrade plan), UW is 401 invalid token
- **shared** `Grok` 2026-08-17 — BOARD HYGIENE — ISO 8601 already shipped as v2.3.0 (Deployed). First line preserved

## 2026-08-16

*42 PRs merged · 7 issues opened · 6 issues closed · 19 effort rows*

### Merged PRs

- **CT** [#1885](https://github.com/jaywedgeworth22/Congress.Trade/pull/1885): fix(health): Infisical sources on /api/health; AGENT_SYNC shared-only _(by jaywedgeworth22)_
- **CT** [#1886](https://github.com/jaywedgeworth22/Congress.Trade/pull/1886): docs: point AGENTS/CLAUDE at ⭐️ Background Jobs Master List _(by jaywedgeworth22)_
- **CT** [#1887](https://github.com/jaywedgeworth22/Congress.Trade/pull/1887): docs: mark #1885 health Infisical shared-only as live _(by jaywedgeworth22)_
- **CT** [#1888](https://github.com/jaywedgeworth22/Congress.Trade/pull/1888): docs: store version 1.0.0 + custom EULA + beta review _(by jaywedgeworth22)_
- **CT** `Grok` [#1889](https://github.com/jaywedgeworth22/Congress.Trade/pull/1889): Earlier/later latency, local Senate relay, live quote snapshots _(by jaywedgeworth22)_
- **CT** [#1890](https://github.com/jaywedgeworth22/Congress.Trade/pull/1890): fix(ios): tab footer buttons + support@congress.trade _(by jaywedgeworth22)_
- **CT** [#1891](https://github.com/jaywedgeworth22/Congress.Trade/pull/1891): docs: App Review 2.1 notes and recording receipt _(by jaywedgeworth22)_
- **CT** [#1892](https://github.com/jaywedgeworth22/Congress.Trade/pull/1892): fix(ios): compile direction(of:) for TestFlight archive _(by jaywedgeworth22)_
- **CT** `Grok` [#1893](https://github.com/jaywedgeworth22/Congress.Trade/pull/1893): Lead/Lag only when median and average agree _(by jaywedgeworth22)_
- **CT** `Grok` [#1894](https://github.com/jaywedgeworth22/Congress.Trade/pull/1894): Restyle open Account sheet; fix first-tap member 404 _(by jaywedgeworth22)_
- **CT** [#1895](https://github.com/jaywedgeworth22/Congress.Trade/pull/1895): fix(web): solid tab bar, admin in settings, Apple tap _(by jaywedgeworth22)_
- **CT** `Grok` [#1896](https://github.com/jaywedgeworth22/Congress.Trade/pull/1896): Stripe checkout race, iOS IAP Pricing, color #h later _(by jaywedgeworth22)_
- **CT** `Grok` [#1897](https://github.com/jaywedgeworth22/Congress.Trade/pull/1897): Solid filter chrome, working account menu, fat side arrows _(by jaywedgeworth22)_
- **CT** `Grok` [#1898](https://github.com/jaywedgeworth22/Congress.Trade/pull/1898): Effort-log closeout for #1897 web chrome _(by jaywedgeworth22)_
- **ST** [#2737](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2737): Keep one weekly R2 cold snapshot _(by jaywedgeworth22)_
- **ST** [#2740](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2740): feat(ios): show Proposals For Review with proposed, live, and target prices _(by jaywedgeworth22)_
- **ST** [#2741](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2741): feat(sources): ROIC universe transcripts, FilingAPI probe, Litestream L1 suffix _(by jaywedgeworth22)_
- **ST** [#2742](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2742): feat(desk): ticker sheet shows lot, exit plan, and other-account size _(by jaywedgeworth22)_
- **ST** [#2743](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2743): feat(overlays,polymarket): Strategy overlay CRUD + sector/macro tilts _(by jaywedgeworth22)_
- **ST** [#2744](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2744): fix(overlays): match classified regime enums, not persisted labels _(by jaywedgeworth22)_
- **ST** [#2747](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2747): fix(sources): complete 13F/ARK ingest after empty first refresh _(by jaywedgeworth22)_
- **ST** [#2748](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2748): Latest-first RAG ingest + Pinecone trial fuse park _(by jaywedgeworth22)_
- **ST** [#2750](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2750): fix(roic): single-flight transcript refresh so ticks cannot crash prod _(by jaywedgeworth22)_
- **ST** [#2751](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2751): fix(engine): rotation fail-open, Red timeout, Alpaca pennies, ingest unstick _(by jaywedgeworth22)_
- **ST** [#2754](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2754): docs: mark #2740 Proposals for Review as merged on main _(by jaywedgeworth22)_
- **ST** [#2755](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2755): docs: ASC EULA write + Coolify rolling already off _(by jaywedgeworth22)_
- **ST** `Grok` [#2756](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2756): docs: ASC EULA write + Coolify rolling already off _(by jaywedgeworth22)_
- **ST** [#2757](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2757): fix(review): speed approve, show prices, retry Red Team, clarify agent controls _(by jaywedgeworth22)_
- **ST** [#2758](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2758): fix(sources): use official ARK CSV when document-table is CF-blocked _(by jaywedgeworth22)_
- **ST** [#2759](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2759): docs: mark 13F/ARK/Form 4 idea sources completed on production _(by jaywedgeworth22)_
- **ST** [#2760](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2760): Approve proposer corpus storage design (rev 3) _(by jaywedgeworth22)_
- **ST** [#2761](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2761): docs: record TestFlight 1.0.36 for Proposals for Review _(by jaywedgeworth22)_
- **ST** [#2763](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2763): feat(roic): harvest Individual history local-first before the tier ends _(by jaywedgeworth22)_
- **ST** [#2764](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2764): ops(rag): enable VECTOR_ASOF_STRICT in Infisical prod _(by jaywedgeworth22)_
- **UM** `Grok` [#1225](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1225): Add an iOS Computers tab for Mac heartbeat stats _(by jaywedgeworth22)_
- **UM** `Grok` [#1226](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1226): Close weekly-R2 board rows and surface ST Litestream tier wedges _(by jaywedgeworth22)_
- **UM** [#1228](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1228): Put Host Usage on the Server tab and stop hiding ST Litestream _(by jaywedgeworth22)_
- **UM** [#1229](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1229): Mark the Host Usage and ST Litestream lane completed _(by jaywedgeworth22)_
- **UM** [#1230](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1230): docs: custom EULA + beta review for Client and Local _(by jaywedgeworth22)_
- **fleet** `Grok` [#37](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/37): Move Mac always-on jobs to pm2 and add a down-watch _(by jaywedgeworth22)_
- **fleet** `Grok` [#38](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/38): mac-process-watch restarts always-on Mac jobs _(by jaywedgeworth22)_
- **fleet** `Grok` [#39](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/39): Keep scheduled Mac jobs able to fire _(by jaywedgeworth22)_

### Issues closed

- **ST** [#2724](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2724): Collapse model versions onto family identity for Results / benchmarks / history
- **ST** [#2728](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2728): Stop boot-reseeding Gemini/DeepSeek keys onto the primary account
- **ST** [#2735](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2735): 13F + ARK + Form 4 as live idea sources
- **ST** [#2738](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2738): Litestream L2/L3 + FilingAPI 401 + ROIC universe transcripts
- **ST** [#2745](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2745): 48h prod error triage: Pinecone daily write fuse
- **UM** [#1181](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1181): 2026-08-14 — IN PROGRESS — Backup restore-proof + honest gatesOverallOk

### Issues opened

- **ST** [#2745](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2745): 48h prod error triage: Pinecone daily write fuse
- **ST** [#2746](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2746): ROIC transcript refresh stacked every tick and crashed prod
- **ST** [#2749](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2749): Rotation fail-closed + Red timeout + Alpaca penny 422 + RAG ingest unstick
- **ST** [#2752](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2752): Review UX: fast approve, live vs proposed price, Retry Red Team, clearer agent controls
- **ST** [#2753](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2753): Review UX: approve speed, live vs proposed price, Retry Red Team, agent controls, PWA off
- **ST** [#2762](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2762): Merge shepherd status
- **UM** [#1227](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1227): 2026-08-14 — COMPLETED/MERGED #1180 — Backup restore-proof + honest

### Effort board

- **CT** `Grok` 2026-08-16 — COMPLETED/DEPLOYED #1897 (`cc70ed9f`) — Desktop web chrome: solid white header through filters, Export CSV, Delivery menu, Manage Subscription, Admin/Review, fat side arrows (branch `grok/web-chrome-filters`). Live `/api/health` sha `cc70ed9f`. `showView()` added; CSV dialog moved off hidden `#view-trades`; Admin/Review stay in the account menu so the token box is reachab
- **CT** `Grok` 2026-08-16 — COMPLETED/DEPLOYED #1896 (`791475dd`) — Pricing checkout race + iOS IAP footer + average later color. Live `/pricing` shows Monthly $5 / Annual $50 + Start Free Trial after `/auth/me`. iOS footer Pricing opens StoreKit. Whole `#h later` figure is red/green. Trends ahead-gate uses median+average
- **CT** `Grok` 2026-08-16 — IN PR #1895 — Web chrome: admin in settings, solid tab bar like ST, sticky header, Apple tap (branch `grok/web-chrome`). Website SIWA still needs Infisical APPLE_SERVICES_ID + team/key/.p8
- **CT** `Grok` 2026-08-16 — COMPLETED/MERGED #1894 — Account sheet theme + first-tap member 404 (branch `grok/ios-sheet-theme`). Light restyles the open Account sheet. `/member` sort is a real query string (was path-encoded 404). TestFlight on next hourly ship
- **CT** `Grok` 2026-08-16 — COMPLETED/DEPLOYED #1893 (`8a2e72f2`) — Latency Lead/Lag wording + match audit (branch `grok/latency-lead-lag`). Lead or Lag only when median and average agree; Mixed when they split; earlier/later colored on the subtitle. Live: FMP 16-1 Lead (13.1h / 12.2h earlier); Quiver 13-0 Lead; UW Mixed (24m earlier / 5.7h later). Scope 161 of 502. FMP fake losses were an Aug 11
- **CT** `Grok` 2026-08-16 — COMPLETED — ASC version 1.0.0 + EULA + beta review (branch `grok/asc-eula-100`). Store version 1.0.0. EULA `7591ac97-…`. Beta review filled. What's New blocked on first version. Coolify already off rolling. 2.1 reply not touched
- **CT** `Grok` 2026-08-16 — COMPLETED/DEPLOYED #1889 (`a7f3d678`) — Earlier/later latency + local Senate relay + live quote snapshots (branch `grok/lead-wording-scout-relay`). Site live: earlier green / later red, no +/−. Scout 351→380 Senate rows via `:8899/fetch-ptr`. `latency_price_snapshots` migrated. House/Senate/Executive polling ok. Latency probes still stalled 73h
- **CT** `Grok` 2026-08-16 — COMPLETED/MERGED #1890 (`fb23e74a`) — iOS tab footer buttons + support@congress.trade (branch `grok/ios-footer-buttons`). Tab `AppLegalFooter` uses `LegalFooterLinks`. TestFlight still needs to pick this up for App Review
- **CT** `Grok` 2026-08-16 — COMPLETED/MERGED #1891 (`c17e12e5`) — App Review Guideline 2.1 notes + recording receipt (branch `grok/asc-21-review-reply`). Docs + merge=union on STATUS/PLAN/EFFORT-LOG. ASC reply/resubmit is still owner-facing if review is not yet WAITING_FOR_REVIEW
- **CT** `Grok` 2026-08-16 — COMPLETED/MERGED #1882 — Keep only the newest weekly R2 archive. Extra weeklies + `_ops` deleted live. Host Sunday job prunes older `weekly/` stamps
- **CT** `Grok` `Claude` 2026-08-16 — IN PR — Rename Apple Note pointer to `⭐️ Background Jobs Master List` (branch `grok/note-title`, worktree `~/apps/congress — title`). AGENTS.md + .md only
- **CT** `Grok` 2026-08-16 — COMPLETED/DEPLOYED #1885 (`a50c09e5`) — Health Infisical sources + AGENT_SYNC shared-only (branch `grok/health-infisical-shared`). Live `/api/health` `checks.secrets`: shared ok/65, app ok/145, no values. `AGENT_SYNC_` only in shared-at-ct. Pipeline `status:stalled` is existing autopilot/senate, not this change
- **CT** `Grok` 2026-08-16 — IN PR #1882 — Keep only the newest weekly R2 archive (branch `grok/r2-weekly-retain-one`). Deleted extra weeklies + `_ops`. Live `weekly/congress-trade-20260816T001501Z.db`. `raw/` filings still on R2 (product store)
- **UM** `Grok` 2026-08-16 — COMPLETED — ASC EULA + beta review for Client and Local (branch `grok/asc-eula-100`). Custom EULAs on both apps. Beta review contacts filled. What's New blocked on first versions. Versions already 1.0.0
- **UM** `Grok` 2026-08-16 — COMPLETED/MERGED #1228 `8c19b1fe` — Host Usage on Server tab + Platforms overflow + ST Litestream 503. ST was briefly `exited:unhealthy` (~05:25Z restart); Live Litestream showed Unknown because peer health 503'd and ST had no B2 prefix. Host was not resource-critical (15 GiB RAM, 46G free). Host Usage is now the Server tab; Platforms overflow fixed; ST `trading-live/` l
- **UM** `Grok` 2026-08-16 — COMPLETED/MERGED #1226 — Fleet Backups: surface ST compaction-tier wedges (branch `grok/peer-litestream-tiers`). ST L0 is fresh but L2 is empty/wedged; UM treated missing top-level litestreamAgeSeconds as “not present” and hid it. Not stealing ST L2 unstick (`grok/litestream-filingapi-roic`)
- **UM** `Grok` 2026-08-16 — IN PR — Rename Apple Note pointer to `⭐️ Background Jobs Master List` (branch `grok/note-title`). Owner retitled the pinned Coding note; AGENTS.md uses the exact new title
- **UM** `Grok` 2026-08-16 — COMPLETED/MERGED #1223 — R2 is weekly-archive-only. UM historic LTX deleted; `usage-monitor-prod-v3` is weekly gz only (now `prod-2026-08-16T04-00-08Z`). CT extra weeklies pruned; #1882 merged. ST weekly `cold-snapshots/app-2026-08-16.db` (4.67 GB) verified; Aug 9 copy deleted. ST #2737 retain-1 rematched, auto-merge armed
- **UM** `Grok` 2026-08-16 — IN PROGRESS — iOS Computers tab from Mac heartbeat (branch `grok/ios-computers-tab`, worktree `~/apps/usage — computers`). New pin-able tab for `/api/health/mac` (CPU/memory/disk + process flags). Also recovered UM 503: Hetzner `/tmp` tmpfs was 100% full of restore-drill SQLite copies

## 2026-08-15

*31 PRs merged · 7 issues opened · 4 issues closed · 16 effort rows*

### Merged PRs

- **CT** `Grok` [#1876](https://github.com/jaywedgeworth22/Congress.Trade/pull/1876): docs: point agents at Mac background-jobs master list _(by jaywedgeworth22)_
- **CT** [#1877](https://github.com/jaywedgeworth22/Congress.Trade/pull/1877): Record submitting iOS 1.0 for App Review _(by jaywedgeworth22)_
- **CT** [#1878](https://github.com/jaywedgeworth22/Congress.Trade/pull/1878): Add PrivacyInfo and a Tahoe GM App Store ship _(by jaywedgeworth22)_
- **CT** [#1879](https://github.com/jaywedgeworth22/Congress.Trade/pull/1879): Record the Tahoe GM App Store resubmit _(by jaywedgeworth22)_
- **CT** [#1881](https://github.com/jaywedgeworth22/Congress.Trade/pull/1881): fix(ios): parse tab footer links and sign latency lead/lag _(by jaywedgeworth22)_
- **CT** [#1882](https://github.com/jaywedgeworth22/Congress.Trade/pull/1882): Keep only the newest weekly R2 archive _(by jaywedgeworth22)_
- **CT** [#1884](https://github.com/jaywedgeworth22/Congress.Trade/pull/1884): fix(ui): Trends order, ticker #/$, Directory pager, Khanna dates _(by jaywedgeworth22)_
- **ST** [#2704](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2704): iOS full desk: Coach, Scan, Guardrails, Results, Data Sources _(by jaywedgeworth22)_
- **ST** [#2707](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2707): feat(trading): Kalshi macro context, Alpaca short buy-stops, paper options _(by jaywedgeworth22)_
- **ST** [#2708](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2708): feat(apns): accept APNS_P8 and cover protective-halt push _(by jaywedgeworth22)_
- **ST** [#2729](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2729): fix(keys): stop boot-reseeding Gemini/DeepSeek onto Connections _(by jaywedgeworth22)_
- **ST** `Grok` [#2730](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2730): docs: point agents at Mac background-jobs master list _(by jaywedgeworth22)_
- **ST** [#2732](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2732): docs(agents): forbid grepping secrets files for KEY=value lines _(by jaywedgeworth22)_
- **ST** [#2733](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2733): Persist strategy-run id and return 202 before executing _(by jaywedgeworth22)_
- **ST** [#2734](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2734): Add DEBUG launch args for App Store screenshot tabs _(by jaywedgeworth22)_
- **ST** [#2736](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2736): feat(sources): operational 13F, ARK holdings, and Form 4 _(by jaywedgeworth22)_
- **ST** [#2739](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2739): docs: point AGENTS at ⭐️ Background Jobs Master List _(by jaywedgeworth22)_
- **UM** `Grok` [#1215](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1215): docs: two spaces apply to App Store review notes _(by jaywedgeworth22)_
- **UM** `Grok` [#1218](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1218): docs: bind Mac background-jobs master list in AGENTS.md _(by jaywedgeworth22)_
- **UM** [#1219](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1219): Ship App Store binaries from GitHub-hosted Tahoe GM _(by jaywedgeworth22)_
- **UM** [#1220](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1220): Record the Tahoe GM App Store resubmit _(by jaywedgeworth22)_
- **UM** [#1221](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1221): Record weekly R2 running on all three apps _(by jaywedgeworth22)_
- **UM** [#1223](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1223): Treat Cloudflare R2 as weekly archive only _(by jaywedgeworth22)_
- **UM** [#1224](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1224): docs: point AGENTS at ⭐️ Background Jobs Master List _(by jaywedgeworth22)_
- **fleet** `Grok` [#31](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/31): docs: Mac background-jobs master list (always-on vs on-demand) _(by jaywedgeworth22)_
- **fleet** [#32](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/32): docs(agents): forbid grepping secrets files for KEY=value lines _(by jaywedgeworth22)_
- **fleet** [#33](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/33): docs: point fleet instructions at ⭐️ Background Jobs Master List _(by jaywedgeworth22)_
- **fleet** `Grok` [#34](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/34): docs: refresh Mac process list after always-on restart _(by jaywedgeworth22)_
- **fleet** `Grok` [#35](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/35): docs: launchd helper inventory (vision/xcode/imessage/pm2) _(by jaywedgeworth22)_
- **fleet** `Grok` [#36](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/36): docs: Mac process list after launchd diagnose _(by jaywedgeworth22)_
- **shared** [#269](https://github.com/jaywedgeworth22/congress-trading-shared/pull/269): Record local main fast-forward on the effort board _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1880](https://github.com/jaywedgeworth22/Congress.Trade/issues/1880): iOS tab footer links + latency lead/lag signs
- **CT** [#1883](https://github.com/jaywedgeworth22/Congress.Trade/issues/1883): Trends layout, Directory pager, Khanna recent-trade dates
- **UM** [#1139](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1139): [FLEET] R2 archive creds live-check — PARTIAL 2026-08-12. UM first weekly
- **shared** [#270](https://github.com/jaywedgeworth22/congress-trading-shared/issues/270): Fast-forward local main after Mac-storage prune

### Issues opened

- **CT** [#1880](https://github.com/jaywedgeworth22/Congress.Trade/issues/1880): iOS tab footer links + latency lead/lag signs
- **CT** [#1883](https://github.com/jaywedgeworth22/Congress.Trade/issues/1883): Trends layout, Directory pager, Khanna recent-trade dates
- **ST** [#2731](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2731): Website favicon: cropped offset candlestick ST, transparent
- **ST** [#2735](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2735): 13F + ARK + Form 4 as live idea sources
- **ST** [#2738](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2738): Litestream L2/L3 + FilingAPI 401 + ROIC universe transcripts
- **UM** [#1222](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1222): [FLEET] R2 archive creds live-check — COMPLETED 2026-08-15. UM weekly
- **shared** [#270](https://github.com/jaywedgeworth22/congress-trading-shared/issues/270): Fast-forward local main after Mac-storage prune

### Effort board

- **CT** `Grok` 2026-08-15 — COMPLETED/MERGED #1884 — Trends layout + Directory pager + Khanna recent-trade dates (branch `grok/ios-trends-khanna`, worktree `~/apps/congress — khanna`). Buys vs Sells under Rising Activity; What Is Being Traded drops rank #s and gets #/$. Directory pager left like Trades, not sticky unless bottom chrome is removed. Ro Khanna sheet listed Dec 2025 because GET
- **CT** `Grok` 2026-08-15 — COMPLETED/MERGED #1881 — iOS tab footer links + latency lead/lag signs (branch `grok/ios-lead-footer`, worktree `~/apps/congress — lead-footer`, #1880). Owner screenshot: Trends legal row prints raw markdown and Support mails `congress.trade@jays.services`; FMP/UW show negative averages in green as "Preliminary lead" while live medians are ahead. Fix: parse footer m
- **CT** `Grok` 2026-08-15 — COMPLETED — Weekly R2 on ST+CT + prune leftover LTX. CT weekly ok: `weekly/congress-trade-20260815T211942Z.db` after new account-write token, host rclone `[r2]`, Infisical `R2_ARCHIVE_`, receipt at `/data/congress-trade/.r2-archive-status.json`. Sunday host cron has working `[r2]`
- **CT** `Grok` 2026-08-15 — COMPLETED — Resubmitted iOS 1.0 from Tahoe GM. #1878 merged. Build `202608150702` attached. Review `37412b30` WAITING_FOR_REVIEW (held 10+ min; prior beta-host binaries flipped faster). Rollout: `docs/rollouts/2026-08-15-invalid-binary-gm-resubmit.md`
- **CT** `Grok` `Claude` 2026-08-15 — COMPLETED/MERGED #1876 — Point CT AGENTS.md / .md at Mac background-jobs master list. Canonical `~/apps/MAC-LOCAL-PROCESSES.md` + pinned Note `[FLEET, ] Mac background jobs master list`
- **CT** `Grok` 2026-08-15 — COMPLETED — IAP copy is Webhooks + SSE + CSV; Premium available in all 175 territories at Apple-equalized prices. Monthly/annual loc + review notes + listing PREMIUM line updated. 175 prices each. iOS heading PRs #1864/#1871 are on the site (live `cf9efbd5`) but not on TestFlight 1.0.14 — ships were dying on a stale archive lock from Aug 14 16:56; lock removed so the in
- **CT** `Grok` 2026-08-15 — IN PR #1875 — Apple 3-day billing grace, paid-to-paid only. ASC live THREE_DAYS / PAID_TO_PAID_ONLY / prod+sandbox. Webhook applies DID_FAIL_TO_RENEW / GRACE_PERIOD_EXPIRED. Branch `grok/apple-billing-grace`
- **CT** `Grok` 2026-08-15 — COMPLETED — Submitted iOS 1.0 for App Review. Submission `07474276`. Live `WAITING_FOR_REVIEW` (build 1.0.14). Rollout in repo `docs/rollouts/2026-08-15-asc-submit-1-0.md`
- **CT** `Grok` `Claude` [FLEET] Finish — Mac-storage prune + CT App Store leftover — COMPLETED 2026-08-15. Removed leftover CT worktrees (0 open PRs). `UIBackgroundModes` on main is only `remote-notification` (used by APNs). `processing` is not in git history. App Store `INVALID_BINARY` was the attached 1.0.7 binary, already replaced with TestFlight 1.0.14 (`PREPARE_FOR_SUBMISSION`, not submitted). See
- **UM** `Grok` 2026-08-15 — COMPLETED — Weekly R2 on all 3 apps + ST leftover LTX prune. UM/CT/ST weekly health ok. CT 401 fixed. ST leftover R2 LTX deleted. Receipt: `docs/rollouts/2026-08-15-weekly-r2-all-three.md`
- **UM** `Grok` 2026-08-15 — COMPLETED — Resubmitted Client+Local from Tahoe GM. #1219 merged. Builds `202608150703` / `202608150708`. Reviews `c0cacf28` / `da7d7fb2` WAITING_FOR_REVIEW (held 10+ min). Rollout: `docs/rollouts/2026-08-15-invalid-binary-gm-resubmit.md`
- **UM** `Grok` 2026-08-15 — IN PROGRESS — Fix App Store INVALID_BINARY + resubmit Client+Local (branch `grok/asc-invalid-binary-gm`). Both 1.0.0 still INVALID_BINARY. This Mac is macOS 27 beta; regular ios-ship already skips beta hosts. Vendor fleet script + GitHub-hosted macos-26 GM workflow. Rollout: `docs/rollouts/2026-08-15-invalid-binary-gm-host.md`
- **UM** `Grok` 2026-08-15 — IN PR — Point UM AGENTS.md at Mac background-jobs master list (branch `grok/mac-process-list`). Binding paragraph + existing table row. Canonical `~/apps/MAC-LOCAL-PROCESSES.md`
- **UM** `Grok` 2026-08-15 — COMPLETED/MERGED #1216 `b8017489` — Jay Old R2 leftovers are not live usage (branch `grok/r2-old-not-enabled`). REST 10042 → “R2 not enabled”; no 116.7 GB bar; no 70% trip. Weekly R2 + frequent B2 is the design: UM both working; ST/CT B2 live, weekly `archive_not_run`
- **UM** `Grok` [FLEET] R2 archive creds live-check — COMPLETED 2026-08-15. UM weekly still ok. ST historic LIST + Aug 9 cold snapshot remain; leftover R2 LTX pruned. CT weekly 401 fixed with a new account-write token in Infisical + host rclone `[r2]`; live key `weekly/congress-trade-20260815T211942Z.db`
- **shared** `Grok` Fast-forward local main after Mac-storage prune — COMPLETED 2026-08-15. Discarded stale In-Progress row for already-merged #260/#262. `git pull — ff-only` `c1f6787` → `88c72b3`. 0 open PRs

## 2026-08-14

*61 PRs merged · 17 issues opened · 12 issues closed · 27 effort rows*

### Merged PRs

- **CT** [#1851](https://github.com/jaywedgeworth22/Congress.Trade/pull/1851): feat(apns): send official-trade and review-needed pushes _(by jaywedgeworth22)_
- **CT** [#1856](https://github.com/jaywedgeworth22/Congress.Trade/pull/1856): chore(deps-dev): bump @typescript-eslint/parser from 8.66.0 to 8.67.0 in /app _(by dependabot[bot])_
- **CT** [#1857](https://github.com/jaywedgeworth22/Congress.Trade/pull/1857): chore(deps): bump @aws-sdk/client-s3 from 3.1106.0 to 3.1107.0 in /app _(by dependabot[bot])_
- **CT** [#1858](https://github.com/jaywedgeworth22/Congress.Trade/pull/1858): chore(deps-dev): bump @typescript-eslint/eslint-plugin from 8.66.0 to 8.67.0 in /app _(by dependabot[bot])_
- **CT** [#1859](https://github.com/jaywedgeworth22/Congress.Trade/pull/1859): docs: AGENTS start-here table + stronger economics _(by jaywedgeworth22)_
- **CT** `Grok` [#1860](https://github.com/jaywedgeworth22/Congress.Trade/pull/1860): Group Trades sort flip with Date; search slot for reload _(by jaywedgeworth22)_
- **CT** `Grok` [#1862](https://github.com/jaywedgeworth22/Congress.Trade/pull/1862): Keep Manage Subscription from emptying the Premium list _(by jaywedgeworth22)_
- **CT** `Grok` [#1863](https://github.com/jaywedgeworth22/Congress.Trade/pull/1863): Mobile filters match iOS; fix SIWA 404 _(by jaywedgeworth22)_
- **CT** `Grok` [#1864](https://github.com/jaywedgeworth22/Congress.Trade/pull/1864): Tighten Trends headings and drop extra section explainers _(by jaywedgeworth22)_
- **CT** `Grok` [#1865](https://github.com/jaywedgeworth22/Congress.Trade/pull/1865): Close out Trends headings copy as deployed _(by jaywedgeworth22)_
- **CT** [#1867](https://github.com/jaywedgeworth22/Congress.Trade/pull/1867): docs(ios): verify Premium intro offer is 2 weeks on ASC and Stripe _(by jaywedgeworth22)_
- **CT** [#1868](https://github.com/jaywedgeworth22/Congress.Trade/pull/1868): docs(billing): trial copy already matches the 2-week offer _(by jaywedgeworth22)_
- **CT** `Grok` [#1869](https://github.com/jaywedgeworth22/Congress.Trade/pull/1869): iOS TestFlight auto-ship once per hour _(by jaywedgeworth22)_
- **CT** `Grok` [#1870](https://github.com/jaywedgeworth22/Congress.Trade/pull/1870): Legal footer on the Trends tab _(by jaywedgeworth22)_
- **CT** `Grok` [#1871](https://github.com/jaywedgeworth22/Congress.Trade/pull/1871): Pin filters, #/$, no heading windows, iOS Directory Assets _(by jaywedgeworth22)_
- **CT** `Grok` [#1872](https://github.com/jaywedgeworth22/Congress.Trade/pull/1872): Make the mobile filter bar actually stick _(by jaywedgeworth22)_
- **CT** `Grok` [#1873](https://github.com/jaywedgeworth22/Congress.Trade/pull/1873): docs(ios): record attaching TestFlight 1.0.14 to App Store 1.0 _(by jaywedgeworth22)_
- **CT** `Grok` [#1874](https://github.com/jaywedgeworth22/Congress.Trade/pull/1874): docs: two-space rule + App Store listing audit _(by jaywedgeworth22)_
- **CT** `Grok` [#1875](https://github.com/jaywedgeworth22/Congress.Trade/pull/1875): fix(billing): honor Apple 3-day paid-to-paid billing grace _(by jaywedgeworth22)_
- **ST** [#2691](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2691): fix(notifications): neutral risk_advisory tail after #2682 _(by jaywedgeworth22)_
- **ST** [#2692](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2692): fix(quote): map Yahoo 52w floor, persist fundamentals, tap whole fill/position cards _(by jaywedgeworth22)_
- **ST** [#2703](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2703): feat(ops): ungate congress share, bounded 8-K bodies, and CSP report-only _(by jaywedgeworth22)_
- **ST** `Claude` [#2705](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2705): docs: iOS .md + xcodebuild-without-MCP rule _(by jaywedgeworth22)_
- **ST** [#2709](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2709): fix(health): grade an EMPTY litestream compaction level instead of calling it normal _(by jaywedgeworth22)_
- **ST** [#2710](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2710): docs: close out PR #2709 on the effort board and STATUS snapshot _(by jaywedgeworth22)_
- **ST** [#2711](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2711): docs: AGENTS start-here table + stronger economics _(by jaywedgeworth22)_
- **ST** [#2712](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2712): docs(agents): record that the local verify gate compiles no Swift _(by jaywedgeworth22)_
- **ST** `Grok` [#2713](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2713): Surface R2 weekly status on /api/health _(by jaywedgeworth22)_
- **ST** `Grok` [#2716](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2716): Pin the 1-hour iOS TestFlight ship gate _(by jaywedgeworth22)_
- **ST** `Claude` [#2717](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2717): docs: — App/Issue Audit owner-decision leftovers _(by jaywedgeworth22)_
- **ST** `Claude` [#2718](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2718): docs: close — loading-graphic / Lato leftover _(by jaywedgeworth22)_
- **ST** [#2719](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2719): fix(rag): bound per-document FTS mirror with durable resume _(by jaywedgeworth22)_
- **ST** [#2720](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2720): fix(quotes): retry dead Alpaca sockets; stop one-blip Autopilot halt _(by jaywedgeworth22)_
- **ST** [#2721](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2721): feat(r5): scoped locks, memory decay, overlay library, chat cancel, scorecard alpha _(by jaywedgeworth22)_
- **ST** `Grok` [#2723](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2723): docs: two spaces apply to App Store review notes _(by jaywedgeworth22)_
- **ST** [#2725](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2725): fix(llm): collapse model versions onto catalog family identity _(by jaywedgeworth22)_
- **ST** [#2727](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2727): fix(ui): Title Case account-config capability chips _(by jaywedgeworth22)_
- **UM** `Grok` [#1189](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1189): Close four Cloudflare accounts effort as deployed _(by jaywedgeworth22)_
- **UM** [#1190](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1190): docs: AGENTS start-here table + stronger economics _(by jaywedgeworth22)_
- **UM** `Grok` [#1191](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1191): Show R2 weekly for Socratic.Trade and Congress.Trade _(by jaywedgeworth22)_
- **UM** [#1192](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1192): docs: explain the two catch-alls (iCloud apex, Worker receipts) _(by jaywedgeworth22)_
- **UM** `Grok` `Claude` [#1194](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1194): Finish — cf-token-map.sh _(by jaywedgeworth22)_
- **UM** `Grok` [#1195](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1195): Document the 1-hour iOS TestFlight ship gate _(by jaywedgeworth22)_
- **UM** `Grok` [#1196](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1196): Mark cf-token-map.sh completed _(by jaywedgeworth22)_
- **UM** `Grok` [#1198](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1198): Open the iOS More sheet tall enough for every tab _(by jaywedgeworth22)_
- **UM** `Grok` [#1200](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1200): Mark More-sheet height as merged on the effort board _(by jaywedgeworth22)_
- **UM** `Grok` [#1202](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1202): Point the start-here table at the Mac process list _(by jaywedgeworth22)_
- **UM** `Grok` [#1204](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1204): Show R2 usage as GB / 10 GB Free Tier with a fill bar _(by jaywedgeworth22)_
- **UM** `Grok` [#1206](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1206): Fix R2 usage reads and widen the free-tier bar _(by jaywedgeworth22)_
- **UM** `Grok` [#1209](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1209): Mark R2 layout + usage-read fix merged on the effort board _(by jaywedgeworth22)_
- **UM** `Grok` `Claude` [#1210](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1210): Finish — receipts-worker leftovers _(by jaywedgeworth22)_
- **UM** `Grok` [#1211](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1211): Keep Infisical address only in the Dockerfile _(by jaywedgeworth22)_
- **UM** `Grok` [#1214](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1214): Mark receipts-worker leftovers merged on the effort board _(by jaywedgeworth22)_
- **UM** `Grok` [#1216](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1216): Ignore GraphQL leftovers when R2 is not enabled _(by jaywedgeworth22)_
- **UM** `Grok` [#1217](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1217): Mark Jay Old R2-not-enabled merged on the effort board _(by jaywedgeworth22)_
- **fleet** [#25](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/25): docs: onboard links + subagent/economics wording _(by jaywedgeworth22)_
- **fleet** `Grok` [#26](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/26): Register — as a standing fleet seat _(by jaywedgeworth22)_
- **fleet** `Grok` [#27](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/27): Add — to the Agent Seat table _(by jaywedgeworth22)_
- **fleet** [#28](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/28): Register Personal-Site (PS) in the fleet registries _(by jaywedgeworth22)_
- **fleet** `Grok` [#29](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/29): Inventory Mac local processes and require agents to list them _(by jaywedgeworth22)_
- **fleet** `Grok` [#30](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/30): docs: two spaces after every sentence, including App Store review notes _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1716](https://github.com/jaywedgeworth22/Congress.Trade/issues/1716): 2026-08-11 1:05pm CT — COMPLETED — Outage post-mortem closed out
- **CT** [#1717](https://github.com/jaywedgeworth22/Congress.Trade/issues/1717): 2026-08-11 ~12:56pm CT — IN PROGRESS — App review top-to-bottom &
- **CT** [#1866](https://github.com/jaywedgeworth22/Congress.Trade/issues/1866): Verify ASC Premium intro offer is 2 weeks ( leftover from #1835)
- **ST** [#2714](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2714): RTH quotes ~1200s stale + origin timeouts from dead Alpaca sockets
- **ST** [#2715](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2715): Bound per-document FTS mirror with durable resume (embed_queued soak)
- **ST** [#2726](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2726): Account-config capabilities: Title Case Fractional Shares / Whole Shares / Regular + Extended
- **UM** [#1188](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1188): 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch
- **UM** [#1193](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1193): Finish cf-token-map.sh for Cloudflare token/account map
- **UM** [#1197](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1197): iOS More sheet opens at half height
- **UM** [#1199](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1199): 2026-08-14 — IN PR #1198 — iOS More sheet opens at ~50% (branch
- **UM** [#1205](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1205): 2026-08-14 — IN PROGRESS — R2 card: GB / 10 GB Free Tier + colored bar
- **UM** [#1207](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1207): 2026-08-14 — IN PROGRESS — R2 card layout + UM/Old usage read (branch

### Issues opened

- **CT** [#1861](https://github.com/jaywedgeworth22/Congress.Trade/issues/1861): 2026-08-14 — IN PROGRESS — iOS Trades sort grouping + search-slot status
- **CT** [#1866](https://github.com/jaywedgeworth22/Congress.Trade/issues/1866): Verify ASC Premium intro offer is 2 weeks ( leftover from #1835)
- **ST** [#2714](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2714): RTH quotes ~1200s stale + origin timeouts from dead Alpaca sockets
- **ST** [#2715](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2715): Bound per-document FTS mirror with durable resume (embed_queued soak)
- **ST** [#2724](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2724): Collapse model versions onto family identity for Results / benchmarks / history
- **ST** [#2726](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2726): Account-config capabilities: Title Case Fractional Shares / Whole Shares / Regular + Extended
- **ST** [#2728](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2728): Stop boot-reseeding Gemini/DeepSeek keys onto the primary account
- **UM** [#1193](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1193): Finish cf-token-map.sh for Cloudflare token/account map
- **UM** [#1197](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1197): iOS More sheet opens at half height
- **UM** [#1199](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1199): 2026-08-14 — IN PR #1198 — iOS More sheet opens at ~50% (branch
- **UM** [#1201](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1201): 2026-08-14 — COMPLETED/MERGED #1198 2ac7b9d4 — iOS More sheet opens at
- **UM** [#1203](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1203): 2026-08-14 — IN PROGRESS — Point UM AGENTS.md at Mac process list
- **UM** [#1205](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1205): 2026-08-14 — IN PROGRESS — R2 card: GB / 10 GB Free Tier + colored bar
- **UM** [#1207](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1207): 2026-08-14 — IN PROGRESS — R2 card layout + UM/Old usage read (branch
- **UM** [#1208](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1208): 2026-08-14 — COMPLETED/MERGED #1204 — R2 card: GB / 10 GB Free Tier +
- **UM** [#1212](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1212): 2026-08-14 — COMPLETED/MERGED #1206 8c1d6dd0 — R2 card layout + UM/Old
- **UM** [#1213](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1213): 2026-08-14 — COMPLETED — Pickup — chat “Usage monitor multi-platform

### Effort board

- **CT** `Grok` 2026-08-14 — COMPLETED — Two-space fleet rule + App Store 1.0 listing audit. Review notes were 1-month + Congress-only. Now 2-week trial, House/Senate/Executive, two spaces. Protocol: AGENT-SYNC § Two spaces. Branch `grok/two-spaces-asc`
- **CT** `Grok` 2026-08-14 — COMPLETED — Attached TestFlight 1.0.14 (`202608141034`) to App Store version 1.0. Replaced rejected `1.0.7` attachment. Version left `INVALID_BINARY` and is now `PREPARE_FOR_SUBMISSION`. Stale Aug 13 review submission `52e2a06f` set to `CANCELING`. Not submitted for review. ASC state only
- **CT** `Grok` [FLEET] Unstick all open PRs so they merge and auto-deploy — IN PROGRESS 2026-08-14. Owner: resolve conflicts, comments, and anything else so every open PR across all apps lands on main. Inventory: ST #2720 CONFLICTING, #2719/#2718/#2708/#2707/#2705/#2704/#2703 UNKNOWN, #2691/#2689 MERGEABLE/BLOCKED (CI), CT #1851 CONFLICTING+gitleaks; UM/fleet/DealDex/Personal/CTS have zero open PRs. No
- **CT** `Grok` 2026-08-14 — COMPLETED/MERGED (#1869 `ce852623`) — iOS TestFlight auto-ship once per hour + keep seq-before-gate (branch `grok/ios-ship-hourly`). Follow-up #1870 puts AppLegalFooter on Trends. Owner: unbuilt iOS updates may ship hourly. `DEFAULT_MIN_INTERVAL_SEC` 9000 → 3600 in the shared fleet script (covers socratic/congress/usage/usage-local). Gate still runs before `next_build_seq`;
- **CT** `Grok` 2026-08-14 — COMPLETED/MERGED (#1871 `86601689`) — Sticky filters + #/$ + iOS Directory Assets. Buys vs Sells is `#` / `$`. No italic timeframe after headings. Filter bar stays visible while scrolling. iOS Directory People|Assets. Coolify webhook queued `gbhqqnmzz1afnxhvotrn2gli`
- **CT** `Grok` 2026-08-14 — COMPLETED/MERGED (#1863 `38167663`) + DEPLOYED — Mobile web filters match iOS + SIWA start route. Dropdowns, glass tab bar, Democrats/Republicans/Other / Ind. GET `/auth/apple/start` no longer 404s
- **CT** `Grok` 2026-08-14 — COMPLETED/MERGED (#1868 `fa2dc62f`) — Trial runbook leftover after #1867 (branch `grok/ct-trial-copy`, worktree `~/apps/congress — copy`). #1867 already verified ASC `TWO_WEEKS` + Infisical 14. This PR rewrote `wave4-auth-billing.md` (still taught 1-month / `STRIPE_TRIAL_DAYS=30`) and the `legalHtml.test.ts` header. No ASC writes
- **CT** `Grok` `Claude` 2026-08-14 — COMPLETED/MERGED (#1867 `de9b655b`) — Premium trial ASC + Stripe verify (branch `grok/premium-trial-verify`). — leftover from #1835: intro offer IS 2 weeks. Live ASC: both `trade.congress.premium.monthly` / `.annual` are `FREE_TRIAL` / `TWO_WEEKS` (start 2026-08-12, no end); US $5 / $50. Infisical prod `STRIPE_TRIAL_DAYS=14`. Copy already matches. No price/trial ch
- **CT** `Grok` 2026-08-14 — COMPLETED — Mac Trends "Request failed" was a prod 502, not a client bug. Owner screenshot of the Mac app empty Market Snapshot. Cloudflare returned `error code: 502` while Coolify deploy `cfjrymrj1vzk2xbmoii0tt6i` (sha `38167663286d`, PR #1863) removed congress-app (~90s gap 20:57:13Z-20:58:47Z). Cancelled stacked restart `acfik7mvw0sobeoolclb917y` so it would not bounc
- **UM** `Grok` 2026-08-14 — COMPLETED — Two-space rule: App Store review notes are not exempt (branch `grok/two-spaces-asc-rule`). Owner: two spaces after every period everywhere, including ASC review notes. AGENTS.md stanza now names App Review notes and IAP review notes and points at `AGENT-SYNC.md` § Two spaces
- **UM** `Grok` `Claude` 2026-08-14 — IN PROGRESS — Coolify Infisical address off Coolify (branch `grok/coolify-dockerfile-address`). Dockerfile already bakes `INFISICAL_ENV` + `INFISICAL_UM_PROJECT_ID`. Deleted those two from Coolify prod+preview. Coolify now only `INFISICAL_CLIENT_ID`/`_SECRET`. `USAGE_INGEST_TOKEN` already matched Infisical in `~/.secrets/global-api-keys`; pulled 's missing `ANTIGRA
- **UM** `Grok` `Claude` 2026-08-14 — COMPLETED/MERGED #1210 `ec6737b5` + auditor DEPLOYED — Finish — receipts-worker leftovers (branch `grok/receipts-auditor-git-closeout`). Inbox already Git-linked to Usage-Monitor. Auditor redeployed (lifecycle 180-day rule verified, version `471b79ce`). Uptime incident title off Oracle. Turso is leftover `file:` names, not hosted. Receipt: `docs/rollouts/2026-08-14
- **UM** `Grok` 2026-08-14 — IN PROGRESS — iOS TestFlight auto-ship once per hour (branch `grok/ios-ship-hourly`). Comment-only: `ios-ship.yml` now documents `DEFAULT_MIN_INTERVAL_SEC=3600`. Runtime script (this repo's ship path) already updated. Sibling CT owns the script; ST owns the pin
- **UM** `Grok` 2026-08-14 — IN PR #1191 — Fleet Backups: R2 Weekly row for ST+CT (branch `grok/fleet-r2-weekly-peers`). Peer `checks.storage.r2Weekly` → `r2-historic` location on Socratic.Trade and Congress.Trade. Missing field → `ok: null` / `peer_r2_weekly_missing` (does not degrade the app). Does not change UM `buildR2HistoricLocation` / `gatesOverallOk`
- **UM** `Grok` Onboarding links + subagent/economics wording — IN PROGRESS 2026-08-14 (branch `grok/docs-onboard-links`). AGENTS.md start-here table + stronger Delegation stanza. Docs only
- **UM** `Grok` 2026-08-14 — DEPLOYED — Four Cloudflare provider rows. #1185 + oneshot #1187 live as `d674904`. Four ON rows (UJS …d1b7 / ST …2e79 / CT …1ae9 / Old …8c73). Seed is create-once; dashboard switch stays yours. Distinct `CLOUDFLARE_JAY_` + `CLOUDFLARE_ST_` restored in UM Infisical
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1180 — Backup restore-proof + honest gatesOverallOk (branch `grok/backup-restore-proof`). UM/CT B2 restore PASS; ST latest B2 was non-contiguous (later L1 suffix work). `gatesOverallOk` honest. CT weekly 401 later fixed 2026-08-15 with an account-write token. Receipt: `docs/rollouts/2026-08-14-backup-restore-proof.md`
- **UM** `Grok` `Gemini` Price — 3.7 Flash for cost derivation — IN PROGRESS 2026-08-14 (branch ` -3-7-flash`, worktree `~/apps/usage — 37`). Runtime lookup override for ` -3.7-flash` / `:batch`. LiteLLM snapshot dump left alone
- **UM** `Grok` `Claude` Finish — cf-token-map.sh — COMPLETED/MERGED 2026-08-14 (#1194 `94b1f91a`, #1193). Value-blind Infisical→Cloudflare account probe. Live: fleet/CT/legacy/R2_USAGE share one all-accounts token; JAY is a distinct all-accounts token; ST is Socratic-only
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1206 `8c1d6dd0` — R2 card layout + UM/Old usage read (branch `grok/r2-bar-layout-and-um-read`). Bar as wide as the GB / 10 GB line, more row gap, vertically center labels. UM+Jay Old failed because month-long GraphQL storage dumps (337–416 KiB) overflowed the 256 KiB probe cap; shrink to 24h latest-per-bucket + 1 MiB trusted GraphQL cap. #1204 alr
- **UM** `Grok` `Claude` 2026-08-14 — COMPLETED — Pickup — chat “Usage monitor multi-platform section”. Platforms tab (#1099) and key/config bundle (#1145) already merged. Import Keys is already on Local TestFlight (last ship `1ac20f23` contains `9870d0ad`). Leftover R2 UM/Old false-unavailable + bar layout landed as #1206. Owner still needs `~/.secrets/umkeys-pass` (chmod 600) before a real AirDr
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1204 — R2 card: GB / 10 GB Free Tier + colored bar (branch `grok/r2-usage-bar`). Drop “% of free tier” text. Show used / 10 GB Free Tier and a fill bar (green / amber / red by closeness to 10 GB)
- **UM** `Grok` 2026-08-14 — IN PROGRESS — Point UM AGENTS.md at Mac process list (branch `grok/mac-local-processes`). One table row. Canonical list is `~/apps/MAC-LOCAL-PROCESSES.md`
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1198 `2ac7b9d4` — iOS More sheet opens at ~50% (branch `grok/ios-more-sheet-height`). Fitted custom detent, cap 88%. All 7 destinations on screen. Closed #1197
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1180 — Backup restore-proof + honest gatesOverallOk (branch `grok/backup-restore-proof`). UM/CT B2 restore PASS; ST latest B2 was non-contiguous (later L1 suffix work). `gatesOverallOk` honest. CT weekly 401 later fixed 2026-08-15 with an account-write token. Receipt: `docs/rollouts/2026-08-14-backup-restore-proof.md`
- **UM** `Grok` 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch `grok/um-cf-four-accounts`). Live DB had 0 cloudflare rows. Boot seeds Usage.Jays.Services / ST / CT / Jay Old. UJS token is CLOUDFLARE_JAY_ first. Fleet fallback for Old. Adapter routes `cloudflare-`
- **UM** `Grok` 2026-08-14 — IN PROGRESS — Apex iCloud MX + receipts Worker catch-all (branch `grok/apex-icloud-receipts-routing`). Owner: `@jays.services` → iCloud; `receipts.jays.services` → receipt-inbox Worker. Live DNS already cut over (apex `mx01`/`mx02.mail.icloud.com`, SPF `include:icloud.com`; receipts CF MX unchanged; catch-all now Worker). Docs PR #1182 (auto-merge). Do not repai

## 2026-08-13

*71 PRs merged · 22 issues opened · 12 issues closed · 11 effort rows*

### Merged PRs

- **CT** `Grok` [#1824](https://github.com/jaywedgeworth22/Congress.Trade/pull/1824): Fix deploy-guard blindness: Coolify lists deploys as numeric-key objects _(by jaywedgeworth22)_
- **CT** `Grok` [#1825](https://github.com/jaywedgeworth22/Congress.Trade/pull/1825): Publish CT Litestream age on /api/health _(by jaywedgeworth22)_
- **CT** [#1832](https://github.com/jaywedgeworth22/Congress.Trade/pull/1832): feat(ui): UI polish, single-row controls, Apple sign-in and Committee Conflicts parity _(by jaywedgeworth22)_
- **CT** [#1833](https://github.com/jaywedgeworth22/Congress.Trade/pull/1833): fix(ops): add container healthchecks to sqlite-web and scan-cpu-worker services in docker-compose.yml _(by jaywedgeworth22)_
- **CT** [#1834](https://github.com/jaywedgeworth22/Congress.Trade/pull/1834): fix(scout): reuse Senate eFD session so 503 maintenance pages stop false-alarming _(by jaywedgeworth22)_
- **CT** [#1835](https://github.com/jaywedgeworth22/Congress.Trade/pull/1835): fix(ios): confirm App Store purchases in one round trip, and one Premium screen _(by jaywedgeworth22)_
- **CT** [#1836](https://github.com/jaywedgeworth22/Congress.Trade/pull/1836): docs: mark iOS Premium paywall/IAP work merged and deployed (#1835) _(by jaywedgeworth22)_
- **CT** [#1837](https://github.com/jaywedgeworth22/Congress.Trade/pull/1837): fix(ci): give CI and iOS ship a trigger that survives a bot merge _(by jaywedgeworth22)_
- **CT** [#1839](https://github.com/jaywedgeworth22/Congress.Trade/pull/1839): fix(ci): a skipped backstop tick must not count as proof of verification _(by jaywedgeworth22)_
- **CT** [#1840](https://github.com/jaywedgeworth22/Congress.Trade/pull/1840): Docs: iOS settings leftovers already landed on main _(by jaywedgeworth22)_
- **CT** [#1841](https://github.com/jaywedgeworth22/Congress.Trade/pull/1841): ops: skip empty /data/prod.db in the 6h fleet dump _(by jaywedgeworth22)_
- **CT** `Grok` [#1842](https://github.com/jaywedgeworth22/Congress.Trade/pull/1842): Drop inaccurate Congressional labels on mixed H/S/E surfaces _(by jaywedgeworth22)_
- **CT** `Grok` [#1843](https://github.com/jaywedgeworth22/Congress.Trade/pull/1843): Take over leftover web+iOS filter-bar work _(by jaywedgeworth22)_
- **CT** `Grok` [#1844](https://github.com/jaywedgeworth22/Congress.Trade/pull/1844): Directory sort dropdown and politician photo fallback _(by jaywedgeworth22)_
- **CT** `Grok` [#1846](https://github.com/jaywedgeworth22/Congress.Trade/pull/1846): Add the Trades asset-class dropdown and export the live filters _(by jaywedgeworth22)_
- **CT** `Grok` [#1847](https://github.com/jaywedgeworth22/Congress.Trade/pull/1847): Effort-log closeout for Directory photo/sort (#1844) _(by jaywedgeworth22)_
- **CT** `Gemini` [#1848](https://github.com/jaywedgeworth22/Congress.Trade/pull/1848): Bump default — Flash to 3.7 _(by jaywedgeworth22)_
- **CT** `Grok` [#1849](https://github.com/jaywedgeworth22/Congress.Trade/pull/1849): Close out the Trades asset-class leftover as deployed _(by jaywedgeworth22)_
- **CT** `Claude` [#1850](https://github.com/jaywedgeworth22/Congress.Trade/pull/1850): docs: iOS .md + xcodebuild-without-MCP rule _(by jaywedgeworth22)_
- **CT** `Grok` [#1852](https://github.com/jaywedgeworth22/Congress.Trade/pull/1852): Watchdog: probe local /api/health so Traefik blips cannot spend the restart budget _(by jaywedgeworth22)_
- **CT** [#1853](https://github.com/jaywedgeworth22/Congress.Trade/pull/1853): Stop calling a stale OpenRouter files-balance halt quota _(by jaywedgeworth22)_
- **CT** `Grok` [#1854](https://github.com/jaywedgeworth22/Congress.Trade/pull/1854): Watchdog: skip remediates while Coolify already has a deploy in flight _(by jaywedgeworth22)_
- **CT** `Grok` [#1855](https://github.com/jaywedgeworth22/Congress.Trade/pull/1855): Trades chrome, light theme sheet, kill All Assets, rank sectors by net _(by jaywedgeworth22)_
- **ST** [#2656](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2656): Ship Socratic iOS to TestFlight from the Mac runner _(by jaywedgeworth22)_
- **ST** [#2668](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2668): fix(brokers): venue contract + park Public; eToro/Webull not connectable _(by jaywedgeworth22)_
- **ST** [#2669](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2669): feat(rag): 24h SEC TTL, enable paid retrieval, Settings-driven knobs _(by jaywedgeworth22)_
- **ST** [#2670](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2670): fix(ui): show Saving… on in-flight writes; bind ROIC Individual _(by jaywedgeworth22)_
- **ST** [#2672](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2672): perf(framework, dashboard): remove 150ms delay, cache session, parallelize dashboard _(by jaywedgeworth22)_
- **ST** [#2673](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2673): fix(ios): remove UpsideDown orientation and stack wordmark _(by jaywedgeworth22)_
- **ST** [#2675](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2675): docs: splash rollout note and accurate slow-load copy _(by jaywedgeworth22)_
- **ST** [#2676](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2676): fix(ios): restore UIInterfaceOrientationPortraitUpsideDown _(by jaywedgeworth22)_
- **ST** [#2677](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2677): fix(ios): restore UIInterfaceOrientationPortraitUpsideDown _(by jaywedgeworth22)_
- **ST** [#2678](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2678): fix(ios): restore UIInterfaceOrientationPortraitUpsideDown _(by jaywedgeworth22)_
- **ST** [#2679](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2679): fix(alerts): stop RH MCP schema 400s, Pinecone 40960 overflow, and overloaded-429 pages _(by jaywedgeworth22)_
- **ST** [#2680](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2680): fix(ingest): adaptive FTS-mirror batching - 250ms synchronous-stretch budget stops event-loop pinning _(by jaywedgeworth22)_
- **ST** [#2681](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2681): feat(ios): APNs push — entitlement, honest environment, tap routing, sign-out withdrawal _(by jaywedgeworth22)_
- **ST** [#2682](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2682): fix(notifications): remove banned force-include pattern, add real-toggle backfill _(by jaywedgeworth22)_
- **ST** [#2683](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2683): fix(ops): persist litestream remote-inventory snapshot durably _(by jaywedgeworth22)_
- **ST** [#2684](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2684): fix(admin): honest server stats — delete six fabricated CI runners, never assert an unmeasured service list _(by jaywedgeworth22)_
- **ST** [#2685](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2685): fix(ops): make litestream compaction failures loud (health, log-scan, config) _(by jaywedgeworth22)_
- **ST** [#2687](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2687): fix(ci): stop bot merges from landing on main with zero workflow runs _(by jaywedgeworth22)_
- **ST** [#2688](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2688): fix(health): drop live usage-monitor 409 collisions and probe /api/ready _(by jaywedgeworth22)_
- **ST** `Claude` [#2693](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2693): docs: pickup + quota-cap inventory and dispositions _(by jaywedgeworth22)_
- **ST** [#2696](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2696): Sign off alert emails as Socratic.Trade _(by jaywedgeworth22)_
- **ST** [#2698](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2698): Prefer Pushover over Resend for ST alerts _(by jaywedgeworth22)_
- **ST** [#2699](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2699): Docs: surgical B2 L1 delete _(by jaywedgeworth22)_
- **ST** [#2701](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2701): fix(health): degrade data providers only on paid-tier mismatch or probe failure _(by jaywedgeworth22)_
- **ST** `Gemini` [#2702](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2702): Bump default — Flash class to 3.7 _(by jaywedgeworth22)_
- **ST** [#2706](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2706): Fix rotation timeouts emptying Autopilot runs _(by jaywedgeworth22)_
- **UM** `Grok` [#1161](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1161): Fix Platforms backup lag and overnight Peer App Health _(by jaywedgeworth22)_
- **UM** [#1162](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1162): docs(effort): claim fleet confirm-merged/deployed pass _(by jaywedgeworth22)_
- **UM** [#1163](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1163): fix(platforms): omit B2 Litestream when litestreamPrefix is explicitly null _(by jaywedgeworth22)_
- **UM** [#1164](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1164): chore(gitignore): protect Apple private keys with .p8 rule _(by jaywedgeworth22)_
- **UM** [#1165](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1165): fix(ci): give CI and iOS ship a trigger that survives a bot merge _(by jaywedgeworth22)_
- **UM** [#1167](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1167): Serve backup-row copy so phones update without a new IPA _(by jaywedgeworth22)_
- **UM** [#1168](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1168): Hide LLM stay-funded and add the Old Cloudflare account _(by jaywedgeworth22)_
- **UM** [#1169](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1169): fix(ops): do not hard-degrade Peer App Health on filingapi 401 _(by jaywedgeworth22)_
- **UM** [#1171](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1171): Sign off Resend emails as Usage Monitor _(by jaywedgeworth22)_
- **UM** [#1173](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1173): Prefer Pushover over Resend for UM alerts _(by jaywedgeworth22)_
- **UM** [#1174](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1174): Give iOS-touching main commits a Mac ship that bot merges still fire _(by jaywedgeworth22)_
- **UM** `Gemini` [#1175](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1175): Price — 3.7 Flash for token-cost derivation _(by jaywedgeworth22)_
- **UM** [#1177](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1177): Close out GH_PAT iOS ship board row after #1167 and #1174 _(by jaywedgeworth22)_
- **UM** `Claude` [#1178](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1178): docs: iOS .md + xcodebuild-without-MCP rule _(by jaywedgeworth22)_
- **UM** [#1179](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1179): feat(alerts): send budget and provider alerts over APNs _(by jaywedgeworth22)_
- **UM** [#1180](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1180): Report backup layer gates honestly and prove B2 restore _(by jaywedgeworth22)_
- **UM** [#1182](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1182): docs: restore apex iCloud MX and receipts Worker catch-all _(by jaywedgeworth22)_
- **UM** [#1184](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1184): docs: close apex iCloud mail effort as deployed _(by jaywedgeworth22)_
- **UM** `Grok` [#1185](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1185): Seed all four Cloudflare accounts as UM providers _(by jaywedgeworth22)_
- **UM** `Grok` [#1187](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1187): Seed Cloudflare rows once; leave the operator switch alone _(by jaywedgeworth22)_
- **fleet** [#23](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/23): Add DealDex to the fleet and write app/agent onboard playbooks _(by jaywedgeworth22)_
- **fleet** [#24](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/24): docs: iOS agent build-loop policy (no Xcode MCP) _(by jaywedgeworth22)_

### Issues closed

- **ST** [#2578](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2578): P1: Tradier rejects bracket orders with sub-penny limit prices (HTTP 400 'must use up to 2 decimal places') — NWG order lost to formatting
- **ST** [#2592](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2592): P2: PWA delete-account collapsed button has no onClick — danger zone can never be opened from the UI
- **ST** [#2593](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2593): P2: strategy.ts regenerates proposalId between receipt-emit and persist — orphaned receipts (source fix for the BUY/TRADE feed dup)
- **ST** [#2695](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2695): Alert emails need (sent by Socratic.Trade) footer
- **ST** [#2700](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2700): Provider-tier honesty: do not degrade on a matching lower plan
- **UM** [#1170](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1170): Alert emails need (sent by Usage Monitor) footer
- **UM** [#1172](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1172): Prefer Pushover over Resend for alert delivery
- **UM** [#1176](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1176): GHPAT + iOS ship + land #1167 — IN PROGRESS 2026-08-13
- **UM** [#1183](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1183): 2026-08-14 — IN PROGRESS — Apex iCloud MX + receipts Worker catch-all
- **UM** [#1186](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1186): 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch
- **shared** [#267](https://github.com/jaywedgeworth22/congress-trading-shared/issues/267): Land open PR queue — COMPLETED 2026-08-12
- **shared** [#268](https://github.com/jaywedgeworth22/congress-trading-shared/issues/268): Cloud protocol bootstrap — COMPLETED

### Issues opened

- **CT** [#1826](https://github.com/jaywedgeworth22/Congress.Trade/issues/1826): 2026-08-12 — COMPLETED/MERGED (#1821 f204c688) — Fleet deploy-guard
- **CT** [#1827](https://github.com/jaywedgeworth22/Congress.Trade/issues/1827): 2026-08-12 — COMPLETED/MERGED (#1820 7634fe61) — Land remaining open PRs
- **CT** [#1828](https://github.com/jaywedgeworth22/Congress.Trade/issues/1828): 2026-08-12 12:25pm CT — COMPLETED/MERGED via #1820 (7634fe61;
- **CT** [#1829](https://github.com/jaywedgeworth22/Congress.Trade/issues/1829): 2026-08-12 — COMPLETED/MERGED (#1796 4e6371d8; closeout PR #1798
- **CT** [#1830](https://github.com/jaywedgeworth22/Congress.Trade/issues/1830): 2026-08-12 1:25pm CT — IN PR — Effort Issues Sync: the transport retry
- **CT** [#1831](https://github.com/jaywedgeworth22/Congress.Trade/issues/1831): 2026-08-12 — IN PROGRESS — iOS Directory/Trades/Trends chrome: Name sort
- **CT** [#1838](https://github.com/jaywedgeworth22/Congress.Trade/issues/1838): 2026-08-13 3:37pm CT — IN PROGRESS — CI and iOS ship never ran on
- **ST** [#2686](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2686): On-demand quote sheet drops fundamentals; fill/position cards only tap the logo
- **ST** [#2694](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2694): Durable litestream remote-inventory cache (PR #2665's
- **ST** [#2695](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2695): Alert emails need (sent by Socratic.Trade) footer
- **ST** [#2697](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2697): Fix ST Litestream wedge and prefer Pushover over Resend
- **ST** [#2700](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2700): Provider-tier honesty: do not degrade on a matching lower plan
- **UM** [#1166](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1166): CI and iOS ship never ran on bot-merged PRs — IN
- **UM** [#1170](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1170): Alert emails need (sent by Usage Monitor) footer
- **UM** [#1172](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1172): Prefer Pushover over Resend for alert delivery
- **UM** [#1176](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1176): GHPAT + iOS ship + land #1167 — IN PROGRESS 2026-08-13
- **UM** [#1181](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1181): 2026-08-14 — IN PROGRESS — Backup restore-proof + honest gatesOverallOk
- **UM** [#1183](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1183): 2026-08-14 — IN PROGRESS — Apex iCloud MX + receipts Worker catch-all
- **UM** [#1186](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1186): 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch
- **UM** [#1188](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1188): 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch
- **shared** [#267](https://github.com/jaywedgeworth22/congress-trading-shared/issues/267): Land open PR queue — COMPLETED 2026-08-12
- **shared** [#268](https://github.com/jaywedgeworth22/congress-trading-shared/issues/268): Cloud protocol bootstrap — COMPLETED

### Effort board

- **UM** `Grok` Real APNs HTTP/2 send for budget/alert pages — IN PROGRESS 2026-08-13 (branch `grok/apns-send`). Register path already existed. Sender reads APNS_KEY_ID / APNS_TEAM_ID / APNS_BUNDLE_ID / APNS_P8 (or APNS_PRIVATE_KEY_B64). Tests mock transport and never hit Apple. No UM .p8 on disk; Infisical prod has no APNS_ yet
- **UM** `Grok` `Claude` iOS agent build-loop policy — IN PROGRESS 2026-08-13 (branch `grok/ios-agent-rules`, worktree `~/apps/usage — rules`). Docs/hooks only: `ios/CLAUDE.md`, AGENTS stanza, — pbxproj write-block. xcodebuild via bash is pre-approved; do not stand up Xcode MCP
- **UM** `Grok` Prefer Pushover over Resend for alerts — IN PR 2026-08-13 (branch `grok/litestream-fix-and-pushover`). Skip email when Pushover is configured. Keep `(sent by Usage Monitor)` on remaining mail
- **UM** `Grok` Alert email sign-off (sent by Usage Monitor) — MERGED 2026-08-13 #1171. Resend HTML now ends with `(sent by Usage Monitor)`
- **UM** `Grok` Peer App Health last-resort FilingAPI 401 — IN PROGRESS 2026-08-13 (branch `grok/peer-health-last-resort`). ST env FILINGAPI 401s (35/35). Last-resort scarce; drop from hard failedDependencies so the card matches a healthy ST process
- **UM** `Grok` `Claude` Pickup + leftovers — IN PR #1168 2026-08-13 (branch `grok/pickup-um-cf-accounts`). Hide Must stay funded for LLM/AI providers (API still accepts later re-enable). Add fourth CF fleet slot Jay (Old) via `CLOUDFLARE_OLD_ACCOUNT_ID`. Infisical account id written (len 32). No token minted. Rollout: `docs/rollouts/2026-08-13-pickup-stay-funded-and-cf-accounts.md`
- **UM** `Grok` [FLEET] Confirm merged/deployed — IN PROGRESS 2026-08-13. Owner: make sure all merged/deployed. UM open PRs 0; prod live `8c38773f` (#1161). Closed ST #2674 (scratch wipe/list). CT/ST Coolify deploys already running for current main
- **UM** `Grok` 2026-08-13 — IN PR — Platforms backup/peer-health cards were lying (branch `grok/platforms-backup-truth`). ST B2 Litestream Lagging 2d: list tail used `prefix+"z"` which is after `trading-live/app.db/…` so it never saw live LTX. CT B2/Live Not Configured: UM listed `congress-live/` but the replica is `congress-trade/db.sqlite`. Peer App Health Degraded 08fcc353: overnight VIX/Cboe `ok:f
- **UM** `Claude` CI and iOS ship never ran on bot-merged PRs — IN PROGRESS 2026-08-13 3:37pm CT (branch `monet/ci-ship-trigger-bot-merge`). A PR merged by `github-actions[bot]` lands on `main` and dispatches ZERO workflow runs: GitHub raises no workflow events for actions taken with `GITHUB_TOKEN`, and `auto-merge-prs.yml` arms auto-merge with exactly that token. PR #1145 (bot-me
- **UM** `Claude` [2026-08-13] R2 kill-switch cleared + auto-resume made durable + Coolify env consolidated into Infisical + prod deploy freeze broken — MERGED PR #1144 (`0f215f59`), #1146 (`c7dffe00`), #1147. Owner approved clearing the switch, fixing the resume gap, and stripping Coolify to only what cannot live in Infisical. (1) `r2Historic.autoDisabled: false` in prod for the first time
- **UM** `Grok` GH_PAT + iOS ship + land #1167 — IN PROGRESS 2026-08-13 (branch `grok/um-ios-ship-ghpat`). Set repo secret `GH_PAT` on UM/ST/CT (names verified). Expand `ios-ship.yml` paths to `ios/` + ship wrappers. Land #1167 backup-row copy. Mark #953 HISTORICAL. No TestFlight upload: host is macOS 27.0 beta (`26A5406e`); Xcode.app is 26.6. Keepout ST #2687 and CT #1845

## 2026-08-12

*110 PRs merged · 29 issues opened · 38 issues closed · 12 effort rows*

### Merged PRs

- **CT** `Grok` [#1709](https://github.com/jaywedgeworth22/Congress.Trade/pull/1709): docs(effort): — closeout + App Store WAITING_FOR_REVIEW _(by jaywedgeworth22)_
- **CT** [#1726](https://github.com/jaywedgeworth22/Congress.Trade/pull/1726): fix(web): close the label/value void in every ledger row (Trends flow rows, drawers, tooltip, admin cards) _(by jaywedgeworth22)_
- **CT** [#1747](https://github.com/jaywedgeworth22/Congress.Trade/pull/1747): feat(client-api): server-side asset-class filter + canonical asset category on trade rows _(by jaywedgeworth22)_
- **CT** [#1749](https://github.com/jaywedgeworth22/Congress.Trade/pull/1749): fix(web): replace party emoji icons with colored dots _(by jaywedgeworth22)_
- **CT** [#1754](https://github.com/jaywedgeworth22/Congress.Trade/pull/1754): feat(latency): make server/Mac handoff a real lease, not a hint — stop double-polling providers _(by jaywedgeworth22)_
- **CT** [#1756](https://github.com/jaywedgeworth22/Congress.Trade/pull/1756): fix(client-api): recover firstSeenAt/filedDate for filings-less rows + OG follow-ups _(by jaywedgeworth22)_
- **CT** [#1757](https://github.com/jaywedgeworth22/Congress.Trade/pull/1757): fix(web): sign every lead figure, add the matched-of-total scope line, and drop the "Exec" prefix from executive titles _(by jaywedgeworth22)_
- **CT** [#1773](https://github.com/jaywedgeworth22/Congress.Trade/pull/1773): types(spend): add LLM_DOC_USD_CEILING and provider ceiling aliases to Env interface _(by jaywedgeworth22)_
- **CT** [#1774](https://github.com/jaywedgeworth22/Congress.Trade/pull/1774): feat(spend): convert LlamaParse daily usage governor and Admin UI to credit-based metering _(by jaywedgeworth22)_
- **CT** [#1775](https://github.com/jaywedgeworth22/Congress.Trade/pull/1775): feat(ios): optimize layout adaptively for iPad and macOS regular size classes _(by jaywedgeworth22)_
- **CT** [#1776](https://github.com/jaywedgeworth22/Congress.Trade/pull/1776): feat(spend): set DEFAULT_LLAMAPARSE_DAILY_CREDIT_CEILING to 175 credits/day (7,000 / 40 days pace) _(by jaywedgeworth22)_
- **CT** [#1777](https://github.com/jaywedgeworth22/Congress.Trade/pull/1777): feat(spend): set DEFAULT_LLAMAPARSE_DAILY_CREDIT_CEILING to 1,750 credits/day for 7-key pool _(by jaywedgeworth22)_
- **CT** [#1778](https://github.com/jaywedgeworth22/Congress.Trade/pull/1778): fix(r2Usage): correct stale litestream→R2 backup status claim _(by jaywedgeworth22)_
- **CT** [#1779](https://github.com/jaywedgeworth22/Congress.Trade/pull/1779): fix(scout): move the Senate relay onto the named tunnel — the relay hostname is now permanent _(by jaywedgeworth22)_
- **CT** [#1780](https://github.com/jaywedgeworth22/Congress.Trade/pull/1780): fix(ios): prevent Theme text wrapping, replace Settings tab with header menu, improve Apple ID auth error handling, and bump version to 1.0.4 (build 4) _(by jaywedgeworth22)_
- **CT** [#1781](https://github.com/jaywedgeworth22/Congress.Trade/pull/1781): feat(ops): rebuild continuous Litestream replication to Backblaze B2 _(by jaywedgeworth22)_
- **CT** [#1782](https://github.com/jaywedgeworth22/Congress.Trade/pull/1782): feat(photos): widen licence policy from gate to record; fill 4 of 7 remaining gaps _(by jaywedgeworth22)_
- **CT** [#1783](https://github.com/jaywedgeworth22/Congress.Trade/pull/1783): fix(deploy-guard): stop going blind, and coalesce while a build is running _(by jaywedgeworth22)_
- **CT** [#1784](https://github.com/jaywedgeworth22/Congress.Trade/pull/1784): fix(scout): repoint the Senate relay at the tunnel that actually exists _(by jaywedgeworth22)_
- **CT** [#1785](https://github.com/jaywedgeworth22/Congress.Trade/pull/1785): fix(spend,ops): stop advertising un-ingestible work; cap every container _(by jaywedgeworth22)_
- **CT** [#1786](https://github.com/jaywedgeworth22/Congress.Trade/pull/1786): fix(ci): run gitleaks directly so a green scan stops failing the job _(by jaywedgeworth22)_
- **CT** [#1787](https://github.com/jaywedgeworth22/Congress.Trade/pull/1787): docs(effort-log): record R2 backup remediation _(by jaywedgeworth22)_
- **CT** [#1788](https://github.com/jaywedgeworth22/Congress.Trade/pull/1788): fix(auth): preserve request origin for local dev requests in baseUrl() _(by jaywedgeworth22)_
- **CT** [#1789](https://github.com/jaywedgeworth22/Congress.Trade/pull/1789): ci(ios): compile CongressTrade on the owned Mac runner, stable Xcode 26 asserted _(by jaywedgeworth22)_
- **CT** [#1790](https://github.com/jaywedgeworth22/Congress.Trade/pull/1790): docs(effort): closeout PR #1709 rebase + App Store status correction _(by jaywedgeworth22)_
- **CT** [#1791](https://github.com/jaywedgeworth22/Congress.Trade/pull/1791): test(photos): de-brittle the attribution-header test + restore the #1782 effort-log record _(by jaywedgeworth22)_
- **CT** [#1792](https://github.com/jaywedgeworth22/Congress.Trade/pull/1792): docs(rollout) + fix(gitignore): correct the litestream-B2 backup-posture claim; anchor app/bin/ ignore _(by jaywedgeworth22)_
- **CT** [#1793](https://github.com/jaywedgeworth22/Congress.Trade/pull/1793): docs(effort): 1.0.# versioning — +1 every rebuild, same string in both fields _(by jaywedgeworth22)_
- **CT** [#1794](https://github.com/jaywedgeworth22/Congress.Trade/pull/1794): Ship Congress.Trade iOS to TestFlight from the Mac runner _(by jaywedgeworth22)_
- **CT** [#1795](https://github.com/jaywedgeworth22/Congress.Trade/pull/1795): chore(ios-fleet): version the fleet TestFlight ship tooling in-repo _(by jaywedgeworth22)_
- **CT** `Grok` [#1796](https://github.com/jaywedgeworth22/Congress.Trade/pull/1796): Fix iOS Google OAuth session drop and drop leftover Xcode project _(by jaywedgeworth22)_
- **CT** [#1797](https://github.com/jaywedgeworth22/Congress.Trade/pull/1797): docs(effort): open-issues resolve batch closeout _(by jaywedgeworth22)_
- **CT** [#1799](https://github.com/jaywedgeworth22/Congress.Trade/pull/1799): fix(ios-fleet): make the ship script agree with App Store Connect and the project file _(by jaywedgeworth22)_
- **CT** [#1800](https://github.com/jaywedgeworth22/Congress.Trade/pull/1800): fix(ci): retry transient transport failures in Effort Issues Sync _(by jaywedgeworth22)_
- **CT** [#1802](https://github.com/jaywedgeworth22/Congress.Trade/pull/1802): fix(ios-fleet): refuse — sync-project-version on a dry-run _(by jaywedgeworth22)_
- **CT** [#1803](https://github.com/jaywedgeworth22/Congress.Trade/pull/1803): Wire probeSchedule into the runtime tick, nested inside the probe lease _(by jaywedgeworth22)_
- **CT** `Grok` [#1810](https://github.com/jaywedgeworth22/Congress.Trade/pull/1810): iOS sort labels, Trades/Trends chrome, Account Sign Out _(by jaywedgeworth22)_
- **CT** [#1811](https://github.com/jaywedgeworth22/Congress.Trade/pull/1811): fix(ios-ship): make the duplicate-build guard able to fire, and stop wedging on a stale lock _(by jaywedgeworth22)_
- **CT** [#1812](https://github.com/jaywedgeworth22/Congress.Trade/pull/1812): fix(ci-observability): drop branch from the Sentry CI fingerprint, repair the stale cron key _(by jaywedgeworth22)_
- **CT** [#1813](https://github.com/jaywedgeworth22/Congress.Trade/pull/1813): fix(ci): shrink page size when an Effort Issues Sync response won't transfer _(by jaywedgeworth22)_
- **CT** [#1814](https://github.com/jaywedgeworth22/Congress.Trade/pull/1814): fix(deploy-guard): survive truncated deployment reads while a build is in flight _(by jaywedgeworth22)_
- **CT** [#1815](https://github.com/jaywedgeworth22/Congress.Trade/pull/1815): chore(gitignore): ignore Apple .p8 auth keys _(by jaywedgeworth22)_
- **CT** [#1816](https://github.com/jaywedgeworth22/Congress.Trade/pull/1816): docs(effort-log): record ASC build tidy across all four fleet apps _(by jaywedgeworth22)_
- **CT** [#1817](https://github.com/jaywedgeworth22/Congress.Trade/pull/1817): fix(ios-ship): evaluate the ship gate before consuming a build number, and make the parenthetical mean something _(by jaywedgeworth22)_
- **CT** [#1818](https://github.com/jaywedgeworth22/Congress.Trade/pull/1818): docs(effort-log): close out the iOS ship-gate ordering + build-number scheme lane (#1817) _(by jaywedgeworth22)_
- **CT** [#1819](https://github.com/jaywedgeworth22/Congress.Trade/pull/1819): fix(ios-ship): give the drift guard a caller, and ship all four apps _(by jaywedgeworth22)_
- **CT** `Grok` [#1820](https://github.com/jaywedgeworth22/Congress.Trade/pull/1820): Land remaining open PRs: zero-downtime deploy scripts + #1798 closeout _(by jaywedgeworth22)_
- **CT** `Grok` [#1821](https://github.com/jaywedgeworth22/Congress.Trade/pull/1821): Fix fleet deploy-guard: Coolify /api/v1/deploy is POST now _(by jaywedgeworth22)_
- **CT** [#1822](https://github.com/jaywedgeworth22/Congress.Trade/pull/1822): docs(effort-log): close out the remaining-open-PR landing (#1820, #1821) _(by jaywedgeworth22)_
- **CT** [#1823](https://github.com/jaywedgeworth22/Congress.Trade/pull/1823): fix(ui/ingestion): optimize directory perf, normalize crypto tickers, fix card pairing & layout, and clean asset parser errors _(by jaywedgeworth22)_
- **ST** [#2641](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2641): feat(health): per-tier litestream backup-status detection + admin panel _(by jaywedgeworth22)_
- **ST** [#2646](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2646): docs: oss-lessons learnings, strategy id fix, bracket limits, and market analysis dashboard card _(by jaywedgeworth22)_
- **ST** [#2647](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2647): feat(ios): customizable glass tab bar with web mobile-tabs parity _(by jaywedgeworth22)_
- **ST** [#2648](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2648): ci(ios): compile SocraticTrade on the owned Mac runner, stable Xcode 26 asserted _(by jaywedgeworth22)_
- **ST** [#2650](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2650): fix(health): watch litestream compaction levels 2 and 3 too _(by jaywedgeworth22)_
- **ST** [#2651](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2651): feat(ios): customizable glass tab bar with web mobile-tabs parity _(by jaywedgeworth22)_
- **ST** [#2652](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2652): feat: lessons from daily_stock_analysis round 1 — watchlist digest, news relevance gating, proposal repair receipts _(by jaywedgeworth22)_
- **ST** [#2653](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2653): feat(console, ios): symbol taps open the company drawer everywhere + iOS fills-card redesign and SymbolInfoSheet _(by jaywedgeworth22)_
- **ST** [#2654](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2654): fix(db): boot migrations under BEGIN IMMEDIATE — rolling deploys can no longer crash-loop on SQLITE_BUSY _(by jaywedgeworth22)_
- **ST** [#2655](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2655): feat: external-repo lessons round 2 — benchmark-alpha grading, live signal-health monitor, cancel-dust advisory _(by jaywedgeworth22)_
- **ST** [#2658](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2658): fix(ios): watchlist wrap, account-switch feedback, admin portal, P&L _(by jaywedgeworth22)_
- **ST** [#2659](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2659): fix(ci): tag Sentry CI events with app + drop branch from fingerprint; retry transport failures in effort sync _(by jaywedgeworth22)_
- **ST** [#2661](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2661): fix(health): stop ~28 false "connection failed" Sentry issues at the root _(by jaywedgeworth22)_
- **ST** [#2662](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2662): feat(mobile): order.cancel command over the shared console cancel path _(by jaywedgeworth22)_
- **ST** [#2663](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2663): feat(brokers): connected-venue history first, Public/eToro/Webull, CopyTrader intel _(by jaywedgeworth22)_
- **ST** `Grok` [#2664](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2664): Knob sync: UM read token + Hetzner SSH _(by jaywedgeworth22)_
- **ST** [#2665](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2665): fix(health): litestream tier monitor had ZERO production coverage - rebuild on sources that exist _(by jaywedgeworth22)_
- **ST** [#2666](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2666): feat: backlog round 3 — proposal scorecard, lookahead audit, PIT fundamentals chain, Polymarket context _(by jaywedgeworth22)_
- **ST** [#2667](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2667): fix(console, ios): stop the false "couldn't load" card, phone-correct load graphic, candlestick iOS splash, Lato everywhere _(by jaywedgeworth22)_
- **UM** [#1094](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1094): docs(effort): rebase hygiene closeout onto current main _(by jaywedgeworth22)_
- **UM** `Antigravity` [#1100](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1100): feat : local quota collector via existing ingest contract, Infisical-backed _(by jaywedgeworth22)_
- **UM** [#1110](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1110): feat(mac-health): add Mac host health monitoring endpoints, Operations card, watchdog script, and active Anthropic/Kimi subscriptions _(by jaywedgeworth22)_
- **UM** [#1111](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1111): fix(platforms): report Infisical identity failures per scope, not wholesale _(by jaywedgeworth22)_
- **UM** [#1112](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1112): feat(ios): Server Status tab + customizable glass tab bar _(by jaywedgeworth22)_
- **UM** [#1113](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1113): fix(subscriptions-backups): update Anthropic/Kimi active subscriptions to /mo and add B2 Litestream tail probe _(by jaywedgeworth22)_
- **UM** [#1114](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1114): fix(platforms): verify Cloudflare account-owned tokens at the right endpoint _(by jaywedgeworth22)_
- **UM** [#1117](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1117): fix(providers): retire Deno Deploy — unused, only produces alert noise _(by jaywedgeworth22)_
- **UM** [#1118](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1118): ci(ios): compile UsageMonitor on the owned Mac runner, stable Xcode 26 asserted _(by jaywedgeworth22)_
- **UM** [#1120](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1120): feat(backup): weekly verified R2 archive with prune-after-verify _(by jaywedgeworth22)_
- **UM** [#1121](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1121): Ship Usage Monitor iOS apps to TestFlight from the Mac runner _(by jaywedgeworth22)_
- **UM** [#1122](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1122): feat(providers): retire oracle + kimi/moonshot; policy: no LLM provider may demand funding _(by jaywedgeworth22)_
- **UM** [#1124](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1124): Stop painting historic R2 green and stop Client ops timeouts _(by jaywedgeworth22)_
- **UM** [#1125](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1125): Board: close iOS R2 Historic debug after #1124 _(by jaywedgeworth22)_
- **UM** [#1127](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1127): docs(backup): record the seeded R2_ARCHIVE_ Infisical keys _(by jaywedgeworth22)_
- **UM** [#1128](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1128): Correction to #1122: LLM mustKeepFunded clear is one-time, owner stays in control _(by jaywedgeworth22)_
- **UM** [#1129](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1129): fix(effort-sync): retry transport failures so one dropped response body cannot kill the run _(by jaywedgeworth22)_
- **UM** [#1131](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1131): fix(alerts): stop manufacturing Twilio discrepancies + close two PagerDuty strand paths _(by jaywedgeworth22)_
- **UM** [#1133](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1133): docs(effort-log): move the PagerDuty alert-correctness row to merged _(by jaywedgeworth22)_
- **UM** [#1134](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1134): fix(docker): retry + HTTP/1.1 on the Infisical CLI download _(by jaywedgeworth22)_
- **UM** `Antigravity` [#1136](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1136): fix : make the launchd collector job survive its two real failure modes _(by jaywedgeworth22)_
- **UM** `Antigravity` [#1137](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1137): docs(effort-log): record the — collector landing and the R2 kill-switch finding _(by jaywedgeworth22)_
- **UM** [#1138](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1138): Record first verified UM weekly R2 archive _(by jaywedgeworth22)_
- **UM** [#1143](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1143): fix(platforms): read Stripe's pre-2017 transfers_enabled payouts field _(by jaywedgeworth22)_
- **UM** [#1144](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1144): fix(r2): make auto-resume survive a restart, not just the process _(by jaywedgeworth22)_
- **UM** [#1145](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1145): feat(local-keys): propagate provider keys/config from the Mac to the Local app _(by jaywedgeworth22)_
- **UM** [#1146](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1146): fix(docker): fail the build when litestream cannot be fetched (unblocks all deploys) _(by jaywedgeworth22)_
- **UM** [#1147](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1147): chore(secrets): Infisical as sole source of truth — Coolify 25 env vars down to 8 _(by jaywedgeworth22)_
- **UM** [#1148](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1148): docs(effort-log): close out the R2 kill-switch, Infisical consolidation and deploy-freeze fix _(by jaywedgeworth22)_
- **UM** [#1152](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1152): chore(lint): ESLint 9.39.5 + eslint-config-next 16.3.0 flat config _(by jaywedgeworth22)_
- **UM** [#1154](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1154): docs(effort): close out the open-PR landing queue _(by jaywedgeworth22)_
- **UM** [#1157](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1157): docs(effort): restore original first lines for #1113 and #1152 _(by jaywedgeworth22)_
- **UM** [#1159](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1159): Call the R2 row a weekly archive, not a historic freeze _(by jaywedgeworth22)_
- **UM** `Grok` [#1160](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1160): Prefer fleet Cloudflare token on Platforms CF/R2 cards _(by jaywedgeworth22)_
- **fleet** [#19](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/19): feat(fleet): mobile push alerts, Needs Owner banners, and rich Slack cards _(by jaywedgeworth22)_
- **fleet** [#20](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/20): docs(fleet): TestFlight 1.0.N versioning policy, Central Time release notes, and mobile feedback instructions _(by jaywedgeworth22)_
- **fleet** [#21](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/21): docs(fleet): prohibit agent names in TestFlight release notes & format PR #s on Apple Notes timestamp row _(by jaywedgeworth22)_
- **shared** `Codex` [#260](https://github.com/jaywedgeworth22/congress-trading-shared/pull/260): chore: standardize — Cloud coordination setup _(by jaywedgeworth22)_
- **shared** [#262](https://github.com/jaywedgeworth22/congress-trading-shared/pull/262): chore(deps): bump anthropics/claude-code-action from 1.0.183 to 1.0.187 _(by dependabot[bot])_
- **shared** [#264](https://github.com/jaywedgeworth22/congress-trading-shared/pull/264): fix(effort-sync): retry transport failures so one dropped response body cannot kill the run _(by jaywedgeworth22)_
- **shared** [#266](https://github.com/jaywedgeworth22/congress-trading-shared/pull/266): docs(effort): close the landed #262/#260 PR queue _(by jaywedgeworth22)_

### Issues closed

- **ST** [#2657](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2657): iOS: watchlist ticker chips wrap mid-symbol (SPCX → SP/CX)
- **UM** [#979](https://github.com/jaywedgeworth22/Usage-Monitor/issues/979): Issue/effort hygiene + replica age align with 1h Litestream sync
- **UM** [#980](https://github.com/jaywedgeworth22/Usage-Monitor/issues/980): Overview money UX: global budget, projected breakdown, quiet stale, ROIC
- **UM** [#990](https://github.com/jaywedgeworth22/Usage-Monitor/issues/990): Install replica-status probe + R2 kill reason (2026-08-05) — IN PR. SSH
- **UM** [#992](https://github.com/jaywedgeworth22/Usage-Monitor/issues/992): Fix auto-deploy race when main advances mid-build (2026-08-05) — IN PR
- **UM** [#1003](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1003): Orange brand + segmented History control + uncrowded nav (2026-08-05)
- **UM** [#1006](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1006): R2 fleet ST/CT pushover-parity card + iOS inline titles (2026-08-05)
- **UM** [#1011](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1011): iOS app icons: clean orange ring + Local full-width LOCAL stripe (no
- **UM** [#1019](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1019): Rename compose project oracle → usage-monitor (clear container names)
- **UM** [#1031](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1031): [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger +
- **UM** [#1034](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1034): [2026-08-07] Backblaze B2 provider web + iOS Local — PR #1033
- **UM** [#1048](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1048): [2026-08-07] Local iOS ↔ web parity wave 1 — IN PROGRESS. Overview
- **UM** [#1050](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1050): [2026-08-07] Local catalog connect wave 2 — IN PROGRESS. ChatGPT row
- **UM** [#1052](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1052): [2026-08-07] Litestream primary → Backblaze B2 (leave R2 historic) — IN
- **UM** [#1054](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1054): Hetzner deploy observer + Coolify SOURCECOMMIT revision (2026-08-07)
- **UM** [#1064](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1064): Mobile nav brand label always visible ("Usage Monitor") — IN PR #1063
- **UM** [#1067](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1067): OpenRouter credit probe endpoint + dedicated UptimeRobot
- **UM** [#1082](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1082): [2026-08-10] Fleet backup locations (B2 dumps + Litestream per UM/ST/CT)
- **UM** [#1083](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1083): Default light theme — IN PROGRESS 2026-08-10 (branch
- **UM** [#1084](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1084): ST OOM + Coolify/ST ops visibility — IN PROGRESS
- **UM** [#1085](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1085): ASC store listing + screenshots + App Store prep (Client + Local) — IN
- **UM** [#1086](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1086): Coolify B2 replica heartbeat (fix envactiveunverified)
- **UM** [#1103](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1103): [Uptime] Usage Monitor production is stale vs main
- **UM** [#1116](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1116): [2026-08-11] Fleet backups + host prevention indicators LANDED
- **UM** [#1119](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1119): [2026-08-12] Mac Host Monitoring & Active Anthropic/Kimi Subscriptions — IN
- **UM** [#1123](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1123): iOS R2 Historic shows green OK for never-run weekly archive; Client ops endpoints time out
- **UM** [#1126](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1126): iOS R2 Historic false-green + Client ops timeouts + 0.1.0
- **UM** [#1132](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1132): [2026-08-12] PagerDuty alert correctness: false Twilio discrepancies +
- **UM** [#1135](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1135): [Uptime] Usage Monitor production is stale vs main
- **UM** [#1141](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1141): [2026-08-12] — quota collector finished against the real CLI
- **UM** [#1142](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1142): [2026-08-12] R2 free-tier kill-switch: pinned in config, not held by
- **UM** [#1150](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1150): [2026-08-13] R2 kill-switch cleared + auto-resume made durable +
- **UM** [#1151](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1151): [2026-08-11] Effort hygiene closeout — COMPLETED. Closed stale
- **UM** [#1153](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1153): [2026-08-12] Mac Host Monitoring & Active Anthropic/Kimi Subscriptions — IN
- **UM** [#1155](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1155): Land open PR queue to production — MERGED 2026-08-12
- **UM** [#1156](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1156): [2026-08-12] Mac Host Monitoring & Active Anthropic/Kimi Subscriptions
- **UM** [#1158](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1158): ESLint 9 + eslint-config-next 16.3.0 flat-config — IN PR
- **fleet** [#22](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/22): Mac runner: Xcode 26 CI runners for CT/ST/UM + xcode.jays.services health endpoint

### Issues opened

- **CT** [#1804](https://github.com/jaywedgeworth22/Congress.Trade/issues/1804): 2026-08-12 12:22pm CT — IN PR — Effort Issues Sync: retry transient
- **CT** [#1805](https://github.com/jaywedgeworth22/Congress.Trade/issues/1805): 2026-08-12 ~8:20pm CT — COMPLETED — Open-issues resolve batch: dead
- **CT** [#1806](https://github.com/jaywedgeworth22/Congress.Trade/issues/1806): 2026-08-12 ~6:40pm CT — COMPLETED/APPLIED — iOS version naming is now
- **CT** [#1807](https://github.com/jaywedgeworth22/Congress.Trade/issues/1807): 2026-08-12 4:45am CT — MERGED (#1782, deployed via auto-merge)
- **CT** [#1808](https://github.com/jaywedgeworth22/Congress.Trade/issues/1808): 2026-08-12 2:05am CT — IN PR — Member photos: licence check widened
- **CT** [#1809](https://github.com/jaywedgeworth22/Congress.Trade/issues/1809): 2026-08-11 ~12:35pm CT — COMPLETED/DEPLOYED — Full — chat closeout +
- **ST** [#2657](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2657): iOS: watchlist ticker chips wrap mid-symbol (SPCX → SP/CX)
- **ST** [#2660](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2660): CI script fixes: Sentry app tag + branchless
- **UM** [#1115](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1115): [2026-08-11] Mac TestFlight launch fix, Xcode.app enforcement & OpenRouter
- **UM** [#1116](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1116): [2026-08-11] Fleet backups + host prevention indicators LANDED
- **UM** [#1119](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1119): [2026-08-12] Mac Host Monitoring & Active Anthropic/Kimi Subscriptions — IN
- **UM** [#1123](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1123): iOS R2 Historic shows green OK for never-run weekly archive; Client ops endpoints time out
- **UM** [#1126](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1126): iOS R2 Historic false-green + Client ops timeouts + 0.1.0
- **UM** [#1130](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1130): Effort-sync transport-level retry — IN PR 2026-08-12
- **UM** [#1132](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1132): [2026-08-12] PagerDuty alert correctness: false Twilio discrepancies +
- **UM** [#1135](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1135): [Uptime] Usage Monitor production is stale vs main
- **UM** [#1139](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1139): [FLEET] R2 archive creds live-check — PARTIAL 2026-08-12. UM first weekly
- **UM** [#1140](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1140): [2026-08-12] PagerDuty alert correctness: false Twilio discrepancies +
- **UM** [#1141](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1141): [2026-08-12] — quota collector finished against the real CLI
- **UM** [#1142](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1142): [2026-08-12] R2 free-tier kill-switch: pinned in config, not held by
- **UM** [#1149](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1149): Local Invalid Binary fix (App Groups profiles +
- **UM** [#1150](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1150): [2026-08-13] R2 kill-switch cleared + auto-resume made durable +
- **UM** [#1151](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1151): [2026-08-11] Effort hygiene closeout — COMPLETED. Closed stale
- **UM** [#1153](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1153): [2026-08-12] Mac Host Monitoring & Active Anthropic/Kimi Subscriptions — IN
- **UM** [#1155](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1155): Land open PR queue to production — MERGED 2026-08-12
- **UM** [#1156](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1156): [2026-08-12] Mac Host Monitoring & Active Anthropic/Kimi Subscriptions
- **UM** [#1158](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1158): ESLint 9 + eslint-config-next 16.3.0 flat-config — IN PR
- **fleet** [#22](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/22): Mac runner: Xcode 26 CI runners for CT/ST/UM + xcode.jays.services health endpoint
- **shared** [#265](https://github.com/jaywedgeworth22/congress-trading-shared/issues/265): Effort-sync transport-level retry — IN PR

### Effort board

- **UM** `Grok` 2026-08-12 — IN PR — Platforms Cloudflare/R2 false-degraded: UM still held legacy per-account tokens (branch `grok/platforms-cf-fleet-token`). Screenshot: CT Token rejected + R2 usage 1/3. Infisical CT/JAY/R2_USAGE tokens were not the fleet token; probe preferred R2_USAGE_API_TOKEN (old JAY) then CLOUDFLARE_CT_API_TOKEN (revoked account-owned). Synced CLOUDFLARE_FLEET_API_TOKEN into tho
- **UM** `Grok` Mac runner TestFlight auto-ship for Usage + Local — IN PROGRESS 2026-08-12 (branch `grok/ios-tf-runner-fix`). `ios-build.yml` only unsigned-compiles; adding `ios-ship.yml` that archives both `usage` and `usage-local` on the Mac runner after iOS changes land on main
- **UM** `Claude` [2026-08-12] PagerDuty alert correctness: false Twilio discrepancies + two permanent-strand paths — MERGED PR #1131 2026-08-12 (auto-deploys). PD #64/#70 were `usage_reconciliation_discrepancy` on two Twilio rows because the reconciler compared the real bill against ZERO pushed telemetry (delta = 100% of the bill; no tolerance short of 1.0 absorbs it) — `reportedEventCount === 0`
- **UM** `Claude` Effort-sync transport-level retry — IN PR 2026-08-12 (branch `claude/effort-sync-transport-retry`). `http_request` in `scripts/sync-effort-issues.py` caught only `urllib.error.HTTPError`, so transport failures escaped the function, never reached the rate-limit retry in `GitHubClient._request`, and killed the whole run (production: `IncompleteRead(714456 bytes read
- **UM** `Claude` `Antigravity` [2026-08-12] — quota collector finished against the real CLI + launchd job live — MERGED PR #1100 (`469fc598`) + #1136 (`8ea014a4`). Picked up a cloud session's handoff that could not reach `agy`, Infisical, the host or Xcode. The guessed parser was wrong in two data-losing ways: real `agy -p "/usage" — output-format json` carries a structured `command.data.groups[]
- **UM** `Claude` [2026-08-12] R2 free-tier kill-switch: pinned in config, not held by usage — CHECKED, one owner decision open. The persisted flag `/data/r2-disabled-70pct.flag` is absent; the switch is engaged purely through Coolify env vars `LITESTREAM_EMERGENCY_DISABLE=true` + `R2_WRITES_DISABLED=true`, set in both production and preview scopes. That answers the auto-resume question structu
- **UM** `Grok` Land open PR queue to production — MERGED 2026-08-12, deploy queued. Open UM count 0. #1094 hygiene `0c6329b4`, #1113 Anthropic/Kimi $200/mo + B2 Litestream tail probe `17831d32`, #1152 ESLint 9.39.5 + eslint-config-next 16.3.0 flat config `ff0364ee` (superseded Dependabot #1070/#1071). Coolify webhook deploys queued to main HEAD `ff0364ee`
- **UM** `Grok` ESLint 9 + eslint-config-next 16.3.0 flat-config — IN PR #1152 2026-08-12 (branch `grok/eslint9-flat-config`, auto-merge squash). Coordinated bump superseding Dependabot #1070/#1071 (closed). Local `eslint .` 0 errors. Config-only; Next already 16.3.0. New React Compiler hook rules left off
- **UM** `Antigravity` `Claude` `Grok` [2026-08-12] Mac Host Monitoring & Active Anthropic/Kimi Subscriptions — IN PR #1113 ( landing). Mac host monitoring already on main. Remaining: seed active Anthropic — Max/Team and Kimi VIP at $200/mo, B2 Litestream tail probe so high-volume prefixes scan newer WAL files, and Congress.Trade `congress-live/` prefix. Branch `ag/update-subscriptions-and-litestream-backups`
- **UM** `Grok` iOS R2 Historic false-green + Client ops timeouts + 0.1.0 version — MERGED PR #1124 2026-08-12 (`418b2f3c`, issue #1123). Historic R2 no longer reports ok when the weekly archive is missing/stale; iOS shows Lagging instead of a green "weekly freeze". Client ops GETs use 60s; server overlaps/parallelizes the Coolify+R2+B2 fan-out and serves stale operations on refre
- **shared** `Grok` `Claude` `Codex` Land open PR queue — COMPLETED 2026-08-12. Squash-merged #262 (`976e73e`, — code-action 1.0.183→1.0.187) after update-branch; prior verify fail was the pre-existing nanoid audit, already fixed on main (3.3.18). Squash-merged #260 (`ebe1f95`, — Cloud coordination) after update-branch + review fixes (`d5d923d`: Slack `ok:true` check, `[Congress-Tra
- **shared** `Codex` `Grok` Cloud protocol bootstrap — COMPLETED 2026-08-12 — land. PR #260 merged as `ebe1f95`. Repo-local `.codex/setup.sh` / `.codex/maintenance.sh`, `scripts/codex-coordination.sh`, and Apple Notes cloud handoff. Review threads resolved before merge

## 2026-08-11

*89 PRs merged · 19 issues opened · 4 issues closed · 4 effort rows*

### Merged PRs

- **CT** [#1698](https://github.com/jaywedgeworth22/Congress.Trade/pull/1698): fix(latency): handoff after 3 successive server errors (not 6h silence) _(by jaywedgeworth22)_
- **CT** [#1700](https://github.com/jaywedgeworth22/Congress.Trade/pull/1700): fix(ops): scout env crash, rapidapi handoff exclude, senate-relay pm2 _(by jaywedgeworth22)_
- **CT** [#1701](https://github.com/jaywedgeworth22/Congress.Trade/pull/1701): docs(effort): latency/scout chat closeout _(by jaywedgeworth22)_
- **CT** [#1702](https://github.com/jaywedgeworth22/Congress.Trade/pull/1702): chore(deps-dev): bump eslint from 10.8.0 to 10.8.1 in /app _(by dependabot[bot])_
- **CT** [#1703](https://github.com/jaywedgeworth22/Congress.Trade/pull/1703): chore(deps): bump @aws-sdk/client-s3 from 3.1105.0 to 3.1106.0 in /app _(by dependabot[bot])_
- **CT** [#1704](https://github.com/jaywedgeworth22/Congress.Trade/pull/1704): chore(deps-dev): bump @types/node from 26.1.2 to 26.2.0 in /app _(by dependabot[bot])_
- **CT** [#1705](https://github.com/jaywedgeworth22/Congress.Trade/pull/1705): fix(ui): directory chrome — wide toggle, no H-scroll, hide Type _(by jaywedgeworth22)_
- **CT** [#1706](https://github.com/jaywedgeworth22/Congress.Trade/pull/1706): feat(enrichment+extraction): committees/photos/prices + review autonomy P0 _(by jaywedgeworth22)_
- **CT** [#1707](https://github.com/jaywedgeworth22/Congress.Trade/pull/1707): fix(ops): serialize + coalesce + rate-limit Coolify deploys; cover scan-cpu-worker in CI _(by jaywedgeworth22)_
- **CT** [#1708](https://github.com/jaywedgeworth22/Congress.Trade/pull/1708): fix(ci,ops): repair scan-cpu-worker job deps; preserve force-rebuild when coalescing _(by jaywedgeworth22)_
- **CT** [#1710](https://github.com/jaywedgeworth22/Congress.Trade/pull/1710): fix(ios): export compliance + production APS for App Store resubmit _(by jaywedgeworth22)_
- **CT** [#1711](https://github.com/jaywedgeworth22/Congress.Trade/pull/1711): fix(ios): enable Mac Designed for iPad/iPhone execution and update effort log _(by jaywedgeworth22)_
- **CT** [#1712](https://github.com/jaywedgeworth22/Congress.Trade/pull/1712): fix(autonomy+ios): A2/A5 drains + Mac TestFlight launch _(by jaywedgeworth22)_
- **CT** [#1713](https://github.com/jaywedgeworth22/Congress.Trade/pull/1713): feat(extraction): garbage_ratio review-queue triage + securities_ref wiring _(by jaywedgeworth22)_
- **CT** [#1714](https://github.com/jaywedgeworth22/Congress.Trade/pull/1714): fix(ios): enforce stable Xcode in the repo ship wrapper, never Xcode-beta _(by jaywedgeworth22)_
- **CT** [#1715](https://github.com/jaywedgeworth22/Congress.Trade/pull/1715): docs(effort): outage closeout — alert-storm mechanism, stable Xcode, token rotation _(by jaywedgeworth22)_
- **CT** [#1722](https://github.com/jaywedgeworth22/Congress.Trade/pull/1722): docs(effort): correct "rotated" -> "re-synced" for the Infisical Coolify token _(by jaywedgeworth22)_
- **CT** [#1723](https://github.com/jaywedgeworth22/Congress.Trade/pull/1723): docs(ux): commit the UX findings and defect record lost to a machine crash _(by jaywedgeworth22)_
- **CT** [#1724](https://github.com/jaywedgeworth22/Congress.Trade/pull/1724): feat(health): add Mac health endpoints, cross-monitoring self-healing watchdog, and spend optimization _(by jaywedgeworth22)_
- **CT** [#1725](https://github.com/jaywedgeworth22/Congress.Trade/pull/1725): fix(retention): stop the daily sweep destroying archived filings _(by jaywedgeworth22)_
- **CT** [#1727](https://github.com/jaywedgeworth22/Congress.Trade/pull/1727): fix(ios): survive a stale SwiftData trade cache instead of trapping on first paint _(by jaywedgeworth22)_
- **CT** [#1728](https://github.com/jaywedgeworth22/Congress.Trade/pull/1728): docs(extraction): LlamaParse tier decision + live pipeline wiring _(by jaywedgeworth22)_
- **CT** [#1729](https://github.com/jaywedgeworth22/Congress.Trade/pull/1729): fix(web): directory columns, mobile KPI overflow, false performance gate, count scope _(by jaywedgeworth22)_
- **CT** [#1730](https://github.com/jaywedgeworth22/Congress.Trade/pull/1730): docs(agents): document the Cloudflare token trap; add fleet token + edge cache rule _(by jaywedgeworth22)_
- **CT** [#1731](https://github.com/jaywedgeworth22/Congress.Trade/pull/1731): fix(ios): honest detail sheets — Top Performers stat, ticker-less rows, ledger geometry _(by jaywedgeworth22)_
- **CT** [#1732](https://github.com/jaywedgeworth22/Congress.Trade/pull/1732): docs(agents): retire legacy Cloudflare credentials; fleet token is the only one _(by jaywedgeworth22)_
- **CT** [#1733](https://github.com/jaywedgeworth22/Congress.Trade/pull/1733): feat(admin): LLM spend by model + live LlamaParse credit balance panel _(by jaywedgeworth22)_
- **CT** [#1734](https://github.com/jaywedgeworth22/Congress.Trade/pull/1734): chore(ios): rename the Xcode project container to CongressTrade.xcodeproj _(by jaywedgeworth22)_
- **CT** [#1737](https://github.com/jaywedgeworth22/Congress.Trade/pull/1737): docs(effort-log): close out the xcodeproj rename (#1734 landed) _(by jaywedgeworth22)_
- **CT** [#1738](https://github.com/jaywedgeworth22/Congress.Trade/pull/1738): fix(ios): Trends tab paints the numbers the API actually returns _(by jaywedgeworth22)_
- **CT** [#1739](https://github.com/jaywedgeworth22/Congress.Trade/pull/1739): fix(ios): truthful trade count, coalesced refreshes, one control language on Trades; Delivery that admits what it does _(by jaywedgeworth22)_
- **CT** [#1740](https://github.com/jaywedgeworth22/Congress.Trade/pull/1740): fix(backend): one bucket per sector, and disclosure-form scaffolding out of asset names _(by jaywedgeworth22)_
- **CT** [#1741](https://github.com/jaywedgeworth22/Congress.Trade/pull/1741): fix(agreement): stop spending model calls on deterministically-parsed formats _(by jaywedgeworth22)_
- **CT** [#1742](https://github.com/jaywedgeworth22/Congress.Trade/pull/1742): fix(ios): remove build stand-ins that shipped into Components.swift by mistake _(by jaywedgeworth22)_
- **CT** [#1743](https://github.com/jaywedgeworth22/Congress.Trade/pull/1743): fix(ios): merge duplicate sector labels; order market cap by size _(by jaywedgeworth22)_
- **CT** [#1744](https://github.com/jaywedgeworth22/Congress.Trade/pull/1744): docs: mirror delegation-for-context-economy directive _(by jaywedgeworth22)_
- **CT** [#1745](https://github.com/jaywedgeworth22/Congress.Trade/pull/1745): docs(effort-log): close out the iOS Trends sector-merge follow-up _(by jaywedgeworth22)_
- **CT** [#1746](https://github.com/jaywedgeworth22/Congress.Trade/pull/1746): fix(ios): shared ledger row, grey header glyphs, one sign-in stack, and a Settings tab that stops repeating itself _(by jaywedgeworth22)_
- **CT** [#1748](https://github.com/jaywedgeworth22/Congress.Trade/pull/1748): handoff: district in the member leaderboard (no code change — needs builders.ts owner) _(by jaywedgeworth22)_
- **CT** [#1750](https://github.com/jaywedgeworth22/Congress.Trade/pull/1750): feat(ios): Assets directory data layer + self-contained screen _(by jaywedgeworth22)_
- **CT** [#1751](https://github.com/jaywedgeworth22/Congress.Trade/pull/1751): fix(web): drawer close X matches back-button grey, not blue-tinted dim _(by jaywedgeworth22)_
- **CT** [#1752](https://github.com/jaywedgeworth22/Congress.Trade/pull/1752): fix(ui): roll trillion+ market caps up to $X.XXt _(by jaywedgeworth22)_
- **CT** [#1755](https://github.com/jaywedgeworth22/Congress.Trade/pull/1755): feat(client-api): company-drawer analytics on /ticker/:ticker, Trends endpoint verification, and the real $-filter contract _(by jaywedgeworth22)_
- **CT** [#1758](https://github.com/jaywedgeworth22/Congress.Trade/pull/1758): fix(latency): make the provider matcher actually match _(by jaywedgeworth22)_
- **CT** [#1759](https://github.com/jaywedgeworth22/Congress.Trade/pull/1759): feat(photos): our own head-focused member face pack — 47 of 55 missing photos filled _(by jaywedgeworth22)_
- **CT** [#1760](https://github.com/jaywedgeworth22/Congress.Trade/pull/1760): feat(ingestion): measured-yield adaptive probe cadence (proportional allocation of a fixed budget) _(by jaywedgeworth22)_
- **CT** [#1761](https://github.com/jaywedgeworth22/Congress.Trade/pull/1761): fix(ingestion): hash window content in the probe-schedule cache key _(by jaywedgeworth22)_
- **CT** [#1762](https://github.com/jaywedgeworth22/Congress.Trade/pull/1762): fix(classifier): stop sending typed PDFs down the paid vision path _(by jaywedgeworth22)_
- **CT** [#1763](https://github.com/jaywedgeworth22/Congress.Trade/pull/1763): fix(scout): Senate outage — upstream Akamai maintenance, plus the backoff and tunnel defects it exposed _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1764](https://github.com/jaywedgeworth22/Congress.Trade/pull/1764): docs(effort): sync — completed tasks entry _(by jaywedgeworth22)_
- **CT** [#1766](https://github.com/jaywedgeworth22/Congress.Trade/pull/1766): fix(latency): guard the coverage join so a broken numerator cannot publish 0% _(by jaywedgeworth22)_
- **CT** [#1767](https://github.com/jaywedgeworth22/Congress.Trade/pull/1767): fix(client-api): default GET /api/client/v1/feed to newest-first _(by jaywedgeworth22)_
- **CT** [#1768](https://github.com/jaywedgeworth22/Congress.Trade/pull/1768): docs(agents): correct Oracle→Hetzner infra + document live-credential verification _(by jaywedgeworth22)_
- **CT** [#1769](https://github.com/jaywedgeworth22/Congress.Trade/pull/1769): feat(vendor): sync congress-trading-shared to v2.5.2 _(by jaywedgeworth22)_
- **CT** [#1770](https://github.com/jaywedgeworth22/Congress.Trade/pull/1770): feat(spend,admin,latency): $0.25 per-doc cap, 30D admin extraction metrics & latency match boost _(by jaywedgeworth22)_
- **CT** [#1771](https://github.com/jaywedgeworth22/Congress.Trade/pull/1771): feat(spend,dedupe,latency): Infisical spend knob audit, auto-dedupe split filers, 100% latency reconciliation _(by jaywedgeworth22)_
- **CT** [#1772](https://github.com/jaywedgeworth22/Congress.Trade/pull/1772): docs(effort-log): update effort log for PRs #1770 and #1771 _(by jaywedgeworth22)_
- **ST** [#2632](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2632): fix(infra): correct stale Hetzner/Coolify config causing server-metrics panel failure _(by jaywedgeworth22)_
- **ST** [#2633](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2633): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2634](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2634): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2635](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2635): docs(rollout): confirm litestream OOM leak root cause — stuck B2 compaction anchor _(by jaywedgeworth22)_
- **ST** [#2636](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2636): docs(rollout): flag litestream OOM kill cadence is accelerating (51->19min gaps) _(by jaywedgeworth22)_
- **ST** [#2637](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2637): fix(ios): add exponential backoff retry and offline snapshot caching, fix Mac TestFlight Xcode toolchain path, add iPad device family target _(by jaywedgeworth22)_
- **ST** [#2638](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2638): feat(ui): display all timestamps in Central Time; settings copy fixes _(by jaywedgeworth22)_
- **ST** [#2639](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2639): fix(ios): restore version build-variable substitution, apply 1.0.1 regimen _(by jaywedgeworth22)_
- **ST** [#2640](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2640): feat(ios): new app icon - dollar-sign candlesticks, lightened background _(by jaywedgeworth22)_
- **ST** [#2642](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2642): feat(ios): new app icon - dollar-sign candlesticks, lightened background _(by jaywedgeworth22)_
- **ST** [#2643](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2643): feat(console, mobile): Desktop Web & Mobile PWA UX enhancements _(by jaywedgeworth22)_
- **ST** [#2644](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2644): feat(deps): bump congress-trading-shared to v2.5.2 and support B side in coerceCongressTrade _(by jaywedgeworth22)_
- **ST** [#2645](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2645): feat(console, mobile): Desktop Web & Mobile PWA UX enhancements _(by jaywedgeworth22)_
- **UM** [#1089](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1089): docs(effort): close fleet backups + host prevention + Local TF ship _(by jaywedgeworth22)_
- **UM** [#1091](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1091): docs(ios): Invalid Binary investigation (App Groups + beta host) _(by jaywedgeworth22)_
- **UM** [#1092](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1092): fix(ios): UserDefaults required-reason in PrivacyInfo manifests _(by jaywedgeworth22)_
- **UM** [#1093](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1093): fix(ops): prefer Coolify SOURCE_COMMIT over stale GIT_COMMIT_SHA _(by jaywedgeworth22)_
- **UM** [#1095](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1095): fix(ios): lower deployment target to iOS 17.0 + Invalid Binary ASC snapshot _(by jaywedgeworth22)_
- **UM** [#1096](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1096): fix(deploy): bake SOURCE_COMMIT into Coolify image _(by jaywedgeworth22)_
- **UM** [#1098](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1098): fix(ios, probe): Mac TestFlight launch fix, Xcode.app enforcement & OpenRouter onboarding key filter _(by jaywedgeworth22)_
- **UM** [#1099](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1099): feat(platforms): all-platform status section + iOS Platforms tab and web parity _(by jaywedgeworth22)_
- **UM** [#1101](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1101): fix(ios-tests): make the Swift test target compile again _(by jaywedgeworth22)_
- **UM** [#1102](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1102): fix(ios): green the Swift test suite — one real product bug, two vacuous harnesses _(by jaywedgeworth22)_
- **UM** [#1104](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1104): feat(deps): bump congress-trading-shared to v2.5.2 _(by jaywedgeworth22)_
- **UM** [#1105](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1105): fix(safari): set objectVersion to 70 for stable Xcode compatibility _(by jaywedgeworth22)_
- **UM** [#1106](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1106): refactor(ci): rename Oracle deploy observer to match Coolify/Hetzner reality _(by jaywedgeworth22)_
- **UM** [#1107](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1107): fix(ci): superseded deploy observers cancel themselves instead of failing _(by jaywedgeworth22)_
- **UM** [#1108](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1108): feat(scripts): add the value-blind Infisical helper fleet canon expects _(by jaywedgeworth22)_
- **UM** [#1109](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1109): fix(ops): tighten release-drift grace window to 2 hours _(by jaywedgeworth22)_
- **fleet** [#18](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/18): docs(fleet): Apple Notes pin/unpin shortcut instructions & universal fleet processes _(by jaywedgeworth22)_
- **shared** [#261](https://github.com/jaywedgeworth22/congress-trading-shared/pull/261): chore(deps-dev): bump publint from 0.3.22 to 0.3.23 _(by dependabot[bot])_
- **shared** [#263](https://github.com/jaywedgeworth22/congress-trading-shared/pull/263): feat(release): 2.5.2 — TxType B/S/E coercion, sub-$1k bracket tier, TransactionsQueryInput export _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1688](https://github.com/jaywedgeworth22/Congress.Trade/issues/1688): 2026-08-10 — IN PROGRESS — Latency scout handoff: server-first probes;
- **UM** [#1056](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1056): [Uptime] Usage Monitor production is stale vs main
- **UM** [#1087](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1087): iOS Client Monitor: backup layers + Hetzner host usage
- **UM** [#1088](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1088): ASC store listing + screenshots + App Store prep (Client + Local)

### Issues opened

- **CT** [#1699](https://github.com/jaywedgeworth22/Congress.Trade/issues/1699): 2026-08-10 8:55pm CT — IN PR — Social share cards rebuilt: near-white
- **CT** [#1716](https://github.com/jaywedgeworth22/Congress.Trade/issues/1716): 2026-08-11 1:05pm CT — COMPLETED — Outage post-mortem closed out
- **CT** [#1717](https://github.com/jaywedgeworth22/Congress.Trade/issues/1717): 2026-08-11 ~12:56pm CT — IN PROGRESS — App review top-to-bottom &
- **CT** [#1718](https://github.com/jaywedgeworth22/Congress.Trade/issues/1718): 2026-08-11 12:40pm CT — COMPLETED/APPLIED — Deploy pile-up: serialized
- **CT** [#1719](https://github.com/jaywedgeworth22/Congress.Trade/issues/1719): 2026-08-11 — IN PR (#1713) — Scanned-PDF extraction recovery
- **CT** [#1720](https://github.com/jaywedgeworth22/Congress.Trade/issues/1720): 2026-08-11 — COMPLETED/DEPLOYED — Latency/scout full closeout
- **CT** [#1721](https://github.com/jaywedgeworth22/Congress.Trade/issues/1721): 2026-08-10 — COMPLETED/DEPLOYED — Latency scout handoff (#1678 + #1681)
- **CT** [#1735](https://github.com/jaywedgeworth22/Congress.Trade/issues/1735): 2026-08-11 — IN PR — Admin panel: LLM spend by model + live LlamaParse
- **CT** [#1736](https://github.com/jaywedgeworth22/Congress.Trade/issues/1736): 2026-08-11 1:05pm CT — COMPLETED — Outage post-mortem closed out
- **CT** [#1753](https://github.com/jaywedgeworth22/Congress.Trade/issues/1753): 2026-08-11 5:07pm CT — IN PR (#1750) — iOS Assets directory: data
- **CT** [#1765](https://github.com/jaywedgeworth22/Congress.Trade/issues/1765): 2026-08-11 ~2:05pm CT — COMPLETED/MERGED (#1711, #1724) — App
- **UM** [#1082](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1082): [2026-08-10] Fleet backup locations (B2 dumps + Litestream per UM/ST/CT)
- **UM** [#1083](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1083): Default light theme — IN PROGRESS 2026-08-10 (branch
- **UM** [#1084](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1084): ST OOM + Coolify/ST ops visibility — IN PROGRESS
- **UM** [#1085](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1085): ASC store listing + screenshots + App Store prep (Client + Local) — IN
- **UM** [#1086](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1086): Coolify B2 replica heartbeat (fix envactiveunverified)
- **UM** [#1087](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1087): iOS Client Monitor: backup layers + Hetzner host usage
- **UM** [#1088](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1088): ASC store listing + screenshots + App Store prep (Client + Local)
- **UM** [#1103](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1103): [Uptime] Usage Monitor production is stale vs main

### Effort board

- **UM** `Antigravity` [2026-08-11] Mac TestFlight launch fix, Xcode.app enforcement & OpenRouter onboarding key filter — IN PR. Guard BGTaskScheduler on isIOSAppOnMac (Mac TF launch fix), enforce DEVELOPER_DIR=/Applications/Xcode.app in ship scripts, filter onboarding/test keys & require positive limitUsd in evaluateKeys for UptimeRobot. Branch `grok/mac-tf-xcode-app-ship`
- **UM** `Grok` Local Invalid Binary fix (App Groups profiles + PrivacyInfo + re-ship) — OPEN 2026-08-11. Portal profiles regenerated (groups fixed); PrivacyInfo shipped; TF VALID. App Store review still Invalid Binary — host is macOS 27 beta (`BuildMachineOSBuild=26A5353q`); owner must rebuild on stable macOS/Xcode Cloud. Rollout note in repo. (PR #1090 closed unmerged; invest
- **UM** `Grok` [2026-08-11] Effort hygiene closeout — COMPLETED. Closed stale in-progress GitHub mirrors whose PRs were already on main: issues #1086 #1085 #1084 #1083 #1082 #1067 #1064 #1054 #1052 #1050 #1048 #1034 #1031 #1019 #1011 #1006 #1003 #992 #990 #980 #979 (state_reason=completed, each cites merge PR/sha). Left open: Invalid Binary (board-only residual), #953 P0 SQLite, #981 receipt-inb
- **UM** `Grok` [2026-08-11] Fleet backups + host prevention indicators LANDED (#1080/#1081). Local iOS 202608110223 uploaded (ITS encryption+app group); 1.0.0 PREPARE_FOR_SUBMISSION with new build. Prod UM restarted for HCLOUD_TOKEN; Host Stats live. — COMPLETED

## 2026-08-10

*85 PRs merged · 33 issues opened · 7 issues closed · 7 effort rows*

### Merged PRs

- **CT** [#1620](https://github.com/jaywedgeworth22/Congress.Trade/pull/1620): fix(review-queue): drop PTR form-chrome OCR flood _(by jaywedgeworth22)_
- **CT** [#1621](https://github.com/jaywedgeworth22/Congress.Trade/pull/1621): docs(effort): review-queue form-chrome closeout _(by jaywedgeworth22)_
- **CT** [#1622](https://github.com/jaywedgeworth22/Congress.Trade/pull/1622): docs(effort): 5-year/3-branch reconciliation COMPLETE — verified vs official sources _(by jaywedgeworth22)_
- **CT** [#1627](https://github.com/jaywedgeworth22/Congress.Trade/pull/1627): feat(openrouter): unify app classifier tags for usage visualization _(by jaywedgeworth22)_
- **CT** [#1629](https://github.com/jaywedgeworth22/Congress.Trade/pull/1629): feat(openrouter): purpose tags + CT workspace classifier runbook _(by jaywedgeworth22)_
- **CT** [#1631](https://github.com/jaywedgeworth22/Congress.Trade/pull/1631): fix(ui): spell out buys/sells, repair Trends card layout, stored review docs _(by jaywedgeworth22)_
- **CT** [#1632](https://github.com/jaywedgeworth22/Congress.Trade/pull/1632): feat(ui): ordinal districts + thousand-separated counts (display-only) _(by jaywedgeworth22)_
- **CT** [#1635](https://github.com/jaywedgeworth22/Congress.Trade/pull/1635): fix(prices): unthrottle peer price refresh + fix freshness watchdog blind spot _(by jaywedgeworth22)_
- **CT** [#1637](https://github.com/jaywedgeworth22/Congress.Trade/pull/1637): feat(ui): site-heading OG cards + archive unused brand assets _(by jaywedgeworth22)_
- **CT** [#1638](https://github.com/jaywedgeworth22/Congress.Trade/pull/1638): ops: scheduled box disk hygiene + health-recover label-only match _(by jaywedgeworth22)_
- **CT** [#1640](https://github.com/jaywedgeworth22/Congress.Trade/pull/1640): Member identity cleanup: campaign-sign display names, bioguide dedupe, executive titles _(by jaywedgeworth22)_
- **CT** [#1641](https://github.com/jaywedgeworth22/Congress.Trade/pull/1641): feat(health): loud per-chamber polling + latency-probe liveness with Pushover alarms _(by jaywedgeworth22)_
- **CT** `Claude` [#1644](https://github.com/jaywedgeworth22/Congress.Trade/pull/1644): Scoped public health endpoints for UptimeRobot polling + latency monitors _(by jaywedgeworth22)_
- **CT** [#1645](https://github.com/jaywedgeworth22/Congress.Trade/pull/1645): docs(effort): loud-liveness lane closeout — #1641/#1644 deployed, monitors live _(by jaywedgeworth22)_
- **CT** [#1647](https://github.com/jaywedgeworth22/Congress.Trade/pull/1647): chore(deps): bump hono from 4.13.0 to 4.13.1 in /app in the cloudflare group _(by dependabot[bot])_
- **CT** [#1648](https://github.com/jaywedgeworth22/Congress.Trade/pull/1648): chore(deps): bump @google/genai from 2.15.0 to 2.16.0 in /app _(by dependabot[bot])_
- **CT** [#1649](https://github.com/jaywedgeworth22/Congress.Trade/pull/1649): chore(deps): bump @aws-sdk/client-s3 from 3.1102.0 to 3.1105.0 in /app _(by dependabot[bot])_
- **CT** [#1650](https://github.com/jaywedgeworth22/Congress.Trade/pull/1650): fix(vision): stop local-vision spin loop (attempt cap + honest park) _(by jaywedgeworth22)_
- **CT** [#1652](https://github.com/jaywedgeworth22/Congress.Trade/pull/1652): docs(effort): vision-worker spin-loop #1650 closeout _(by jaywedgeworth22)_
- **CT** [#1654](https://github.com/jaywedgeworth22/Congress.Trade/pull/1654): fix(ingestion): vision/scan workers always use stored R2 copy _(by jaywedgeworth22)_
- **CT** [#1656](https://github.com/jaywedgeworth22/Congress.Trade/pull/1656): docs(effort): stored-copy-only #1654 closeout _(by jaywedgeworth22)_
- **CT** [#1658](https://github.com/jaywedgeworth22/Congress.Trade/pull/1658): docs(effort): UI lane closeout — #1631 deployed + disk-full incident (re-landed) _(by jaywedgeworth22)_
- **CT** [#1660](https://github.com/jaywedgeworth22/Congress.Trade/pull/1660): fix(identity): resolver v2 — diminutive/nickname bridging for the remaining duplicate clusters _(by jaywedgeworth22)_
- **CT** `Cursor` [#1661](https://github.com/jaywedgeworth22/Congress.Trade/pull/1661): fix(ui,analytics): trade-details grid, delivery — labels, honest performance metric + competitor attribution repair _(by jaywedgeworth22)_
- **CT** [#1663](https://github.com/jaywedgeworth22/Congress.Trade/pull/1663): fix(scan-cpu-worker): copy form_chrome.py into image _(by jaywedgeworth22)_
- **CT** [#1664](https://github.com/jaywedgeworth22/Congress.Trade/pull/1664): fix(ops): stop proxy-reattach network churn; make watchdog able to recover and page _(by jaywedgeworth22)_
- **CT** [#1665](https://github.com/jaywedgeworth22/Congress.Trade/pull/1665): fix(ios): Apple Sign In enable path + ST-style Google button, trim Settings _(by jaywedgeworth22)_
- **CT** [#1668](https://github.com/jaywedgeworth22/Congress.Trade/pull/1668): docs(effort): closeout #1665 Apple Sign In + Settings polish _(by jaywedgeworth22)_
- **CT** [#1669](https://github.com/jaywedgeworth22/Congress.Trade/pull/1669): fix(ui): trades chrome — export menu, auth group, match count, dual pager, whole-row open _(by jaywedgeworth22)_
- **CT** [#1670](https://github.com/jaywedgeworth22/Congress.Trade/pull/1670): docs(effort): closeout — congress.trade 6h45m outage + iOS 1.0 submission state _(by jaywedgeworth22)_
- **CT** `Grok` [#1672](https://github.com/jaywedgeworth22/Congress.Trade/pull/1672): docs(effort): close out web UX trades chrome #1669 _(by jaywedgeworth22)_
- **CT** [#1675](https://github.com/jaywedgeworth22/Congress.Trade/pull/1675): docs(effort): full session closeout — names, dedupe, committees, exec titles, performance metric, competitor repair _(by jaywedgeworth22)_
- **CT** [#1678](https://github.com/jaywedgeworth22/Congress.Trade/pull/1678): fix(latency): server-first probes with Mac scout fallback + R2 raw upload _(by jaywedgeworth22)_
- **CT** `Grok` [#1679](https://github.com/jaywedgeworth22/Congress.Trade/pull/1679): docs: review-queue drain lessons + no-OpenRouter autonomy backlog _(by jaywedgeworth22)_
- **CT** [#1681](https://github.com/jaywedgeworth22/Congress.Trade/pull/1681): fix(scout): throttle latency posts + skip senate wall raw loops _(by jaywedgeworth22)_
- **CT** [#1682](https://github.com/jaywedgeworth22/Congress.Trade/pull/1682): fix(ui): review table 7-row scroll + admin token verify _(by jaywedgeworth22)_
- **CT** [#1683](https://github.com/jaywedgeworth22/Congress.Trade/pull/1683): fix(ui/admin): review/history docs open stored copy, never government _(by jaywedgeworth22)_
- **CT** [#1684](https://github.com/jaywedgeworth22/Congress.Trade/pull/1684): fix(admin): stale ADMIN_TOKEN no longer blocks allowlisted session _(by jaywedgeworth22)_
- **CT** [#1689](https://github.com/jaywedgeworth22/Congress.Trade/pull/1689): docs: close out admin auth stale-bearer fallthrough (#1684) _(by jaywedgeworth22)_
- **CT** [#1691](https://github.com/jaywedgeworth22/Congress.Trade/pull/1691): feat(og): rebuild social share cards — white field, quiet label, product graphic _(by jaywedgeworth22)_
- **CT** [#1692](https://github.com/jaywedgeworth22/Congress.Trade/pull/1692): fix(ui): default theme is light (owner ruling) _(by jaywedgeworth22)_
- **CT** [#1693](https://github.com/jaywedgeworth22/Congress.Trade/pull/1693): docs: two spaces between sentences — all contexts _(by jaywedgeworth22)_
- **CT** [#1694](https://github.com/jaywedgeworth22/Congress.Trade/pull/1694): feat(og): politician share cards carry the seat (D-CA-17) _(by jaywedgeworth22)_
- **CT** [#1695](https://github.com/jaywedgeworth22/Congress.Trade/pull/1695): fix(og): executive filers show their position, not a blank seat _(by jaywedgeworth22)_
- **CT** [#1696](https://github.com/jaywedgeworth22/Congress.Trade/pull/1696): fix(ui): By Asset Type matches Market Cap flow-row layout _(by jaywedgeworth22)_
- **CT** [#1697](https://github.com/jaywedgeworth22/Congress.Trade/pull/1697): fix(ios): dark brand lockup was missing letters; rebuild from pristine eagle _(by jaywedgeworth22)_
- **ST** `Grok` [#2597](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2597): ci+docs: always auto-merge non-draft PRs; Apple Notes close-out _(by jaywedgeworth22)_
- **ST** `Codex` [#2603](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2603): chore: standardize — Cloud coordination setup _(by jaywedgeworth22)_
- **ST** [#2606](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2606): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2608](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2608): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2610](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2610): build(deps): bump next from 16.2.12 to 16.3.0 in the next-react group _(by dependabot[bot])_
- **ST** [#2611](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2611): build(deps): bump the observability group with 2 updates _(by dependabot[bot])_
- **ST** [#2612](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2612): build(deps): bump react-virtuoso from 4.18.10 to 4.18.11 _(by dependabot[bot])_
- **ST** [#2613](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2613): build(deps): bump lucide-react from 1.24.0 to 1.29.0 _(by dependabot[bot])_
- **ST** [#2614](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2614): build(deps-dev): bump eslint-config-next from 16.2.12 to 16.3.0 _(by dependabot[bot])_
- **ST** [#2615](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2615): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2616](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2616): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2617](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2617): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2618](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2618): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2619](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2619): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2620](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2620): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2621](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2621): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2622](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2622): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2623](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2623): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2624](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2624): fix(ios): replace invalid SF Symbol bell.badge.plus with bell.badge _(by jaywedgeworth22)_
- **ST** [#2625](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2625): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2626](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2626): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2627](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2627): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2628](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2628): fix(ui): default light theme + two-space copy rule _(by jaywedgeworth22)_
- **ST** [#2629](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2629): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2631](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2631): fix(ios): two spaces between sentences in all user-facing copy _(by jaywedgeworth22)_
- **UM** [#1066](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1066): feat(openrouter): public credit + per-key limit probe for UptimeRobot _(by jaywedgeworth22)_
- **UM** [#1068](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1068): chore(deps): bump the npm-minor-and-patch group with 5 updates _(by dependabot[bot])_
- **UM** [#1069](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1069): chore(deps): bump @jaywedgeworth22/congress-trading-shared from v2.4.0 to v2.5.1 _(by dependabot[bot])_
- **UM** [#1072](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1072): fix(backup): Coolify B2 replica heartbeat for /api/ready _(by jaywedgeworth22)_
- **UM** [#1073](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1073): feat(ios/asc): App Store listing, screenshots, public privacy/support _(by jaywedgeworth22)_
- **UM** [#1074](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1074): docs(effort): close ASC store listing + screenshots lane _(by jaywedgeworth22)_
- **UM** [#1075](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1075): feat(ios): Client Monitor backup layers + Hetzner host usage _(by jaywedgeworth22)_
- **UM** [#1076](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1076): docs(effort): close Client Monitor backup/host metrics lane (#1075) _(by jaywedgeworth22)_
- **UM** [#1077](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1077): feat(ops): full ST health + Coolify fleet on Operations _(by jaywedgeworth22)_
- **UM** [#1078](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1078): fix(ui): default theme is light (owner ruling) _(by jaywedgeworth22)_
- **UM** [#1079](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1079): docs: two spaces between sentences in all contexts (ASC) _(by jaywedgeworth22)_
- **UM** [#1080](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1080): feat(ops): fleet backup status per app and location (UM/ST/CT) _(by jaywedgeworth22)_
- **UM** [#1081](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1081): feat(ops): host risk indicators and poll history for prevention _(by jaywedgeworth22)_
- **fleet** [#17](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/17): style(digest): legend 2-col table layout + Created spacing _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1618](https://github.com/jaywedgeworth22/Congress.Trade/issues/1618): 2026-08-09 9:30pm CT — IN PROGRESS (pipeline draining)
- **CT** [#1643](https://github.com/jaywedgeworth22/Congress.Trade/issues/1643): 2026-08-10 2:03am CT — DEPLOYED — Box disk hygiene + health-recover
- **CT** [#1651](https://github.com/jaywedgeworth22/Congress.Trade/issues/1651): 2026-08-10 ~3:40am CT — IN PROGRESS — Vision-worker spin-loop defect
- **CT** [#1655](https://github.com/jaywedgeworth22/Congress.Trade/issues/1655): 2026-08-10 ~4:05am CT — IN PROGRESS — Stored-copy-only vision/scan
- **CT** [#1662](https://github.com/jaywedgeworth22/Congress.Trade/issues/1662): 2026-08-10 — IN PR — Identity resolver v2: diminutive/nickname
- **CT** [#1667](https://github.com/jaywedgeworth22/Congress.Trade/issues/1667): 2026-08-10 — MERGED (#1660) — Identity resolver v2
- **CT** [#1685](https://github.com/jaywedgeworth22/Congress.Trade/issues/1685): 2026-08-10 7:34PM CT — IN PROGRESS — Admin auth: stale bearer falls

### Issues opened

- **CT** [#1623](https://github.com/jaywedgeworth22/Congress.Trade/issues/1623): 2026-08-10 12:50am CT — COMPLETED (code+ops) — Review-queue form-chrome
- **CT** [#1624](https://github.com/jaywedgeworth22/Congress.Trade/issues/1624): 2026-08-10 12:43am CT — IN PROGRESS — Review-queue manual assist +
- **CT** [#1625](https://github.com/jaywedgeworth22/Congress.Trade/issues/1625): 2026-08-10 12:55am CT — COMPLETED — 5-year/3-branch reconciliation
- **CT** [#1626](https://github.com/jaywedgeworth22/Congress.Trade/issues/1626): 2026-08-09 9:30pm CT — superseded by the 12:55am completion row above
- **CT** [#1628](https://github.com/jaywedgeworth22/Congress.Trade/issues/1628): 2026-08-10 1:08am CT — IN PROGRESS — OpenRouter app classifier
- **CT** [#1630](https://github.com/jaywedgeworth22/Congress.Trade/issues/1630): 2026-08-10 1:32am CT — IN PR — OpenRouter purpose tags + workspace
- **CT** [#1634](https://github.com/jaywedgeworth22/Congress.Trade/issues/1634): 2026-08-10 1:37am CT — IN PR — District ordinals (1ˢᵗ/2ⁿᵈ/…) + count
- **CT** [#1636](https://github.com/jaywedgeworth22/Congress.Trade/issues/1636): 2026-08-10 — IN PR — Price staleness root-cause fix
- **CT** [#1639](https://github.com/jaywedgeworth22/Congress.Trade/issues/1639): 2026-08-10 1:57am CT — IN PR — OG lockup cards + brand asset archive
- **CT** [#1642](https://github.com/jaywedgeworth22/Congress.Trade/issues/1642): 2026-08-10 — IN PR — Member identity cleanup: campaign-sign names
- **CT** [#1643](https://github.com/jaywedgeworth22/Congress.Trade/issues/1643): 2026-08-10 2:03am CT — DEPLOYED — Box disk hygiene + health-recover
- **CT** [#1646](https://github.com/jaywedgeworth22/Congress.Trade/issues/1646): 2026-08-10 2:50am CT — DEPLOYED — Loud liveness lane complete
- **CT** [#1651](https://github.com/jaywedgeworth22/Congress.Trade/issues/1651): 2026-08-10 ~3:40am CT — IN PROGRESS — Vision-worker spin-loop defect
- **CT** [#1653](https://github.com/jaywedgeworth22/Congress.Trade/issues/1653): 2026-08-10 ~3:50am CT — COMPLETED/DEPLOYED — Vision-worker spin-loop
- **CT** [#1655](https://github.com/jaywedgeworth22/Congress.Trade/issues/1655): 2026-08-10 ~4:05am CT — IN PROGRESS — Stored-copy-only vision/scan
- **CT** [#1657](https://github.com/jaywedgeworth22/Congress.Trade/issues/1657): 2026-08-10 ~4:15am CT — COMPLETED/DEPLOYED — Stored-copy-only
- **CT** [#1659](https://github.com/jaywedgeworth22/Congress.Trade/issues/1659): 2026-08-10 1:45am CT — DEPLOYED — Owner UI feedback lane: buys/sells
- **CT** [#1662](https://github.com/jaywedgeworth22/Congress.Trade/issues/1662): 2026-08-10 — IN PR — Identity resolver v2: diminutive/nickname
- **CT** [#1666](https://github.com/jaywedgeworth22/Congress.Trade/issues/1666): 2026-08-10 — IN PR — Trade-details grid, delivery — labels
- **CT** [#1667](https://github.com/jaywedgeworth22/Congress.Trade/issues/1667): 2026-08-10 — MERGED (#1660) — Identity resolver v2
- **CT** [#1671](https://github.com/jaywedgeworth22/Congress.Trade/issues/1671): 2026-08-10 ~afternoon CT — COMPLETED/MERGED (#1665) — iOS auth Settings
- **CT** [#1673](https://github.com/jaywedgeworth22/Congress.Trade/issues/1673): 2026-08-10 — IN PR — Web UX trades chrome + full UI expert review
- **CT** [#1674](https://github.com/jaywedgeworth22/Congress.Trade/issues/1674): 2026-08-10 ~afternoon CT — IN PROGRESS/LANDING — iOS auth Settings
- **CT** [#1676](https://github.com/jaywedgeworth22/Congress.Trade/issues/1676): 2026-08-10 — COMPLETED/DEPLOYED — Full member-identity +
- **CT** [#1677](https://github.com/jaywedgeworth22/Congress.Trade/issues/1677): 2026-08-10 — COMPLETED/DEPLOYED — Identity resolver v2
- **CT** [#1685](https://github.com/jaywedgeworth22/Congress.Trade/issues/1685): 2026-08-10 7:34PM CT — IN PROGRESS — Admin auth: stale bearer falls
- **CT** [#1686](https://github.com/jaywedgeworth22/Congress.Trade/issues/1686): 2026-08-10 1:15pm CT — COMPLETED/DEPLOYED — congress.trade 6h45m
- **CT** [#1687](https://github.com/jaywedgeworth22/Congress.Trade/issues/1687): 2026-08-10 1:15pm CT — IN PROGRESS (owner-blocked) — iOS App Store 1.0
- **CT** [#1688](https://github.com/jaywedgeworth22/Congress.Trade/issues/1688): 2026-08-10 — IN PROGRESS — Latency scout handoff: server-first probes;
- **CT** [#1690](https://github.com/jaywedgeworth22/Congress.Trade/issues/1690): 2026-08-10 7:41PM CT — COMPLETED/DEPLOYED (#1684) — Admin auth: stale
- **ST** [#2609](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2609): Unstick open PRs → main/prod (#2597 always-auto-merge;
- **ST** [#2630](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2630): Default light theme (fleet ruling) — IN PROGRESS
- **UM** [#1067](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1067): OpenRouter credit probe endpoint + dedicated UptimeRobot

### Effort board

- **UM** `Grok` [2026-08-10] Fleet backup locations (B2 dumps + Litestream per UM/ST/CT) on server-metrics + Operations + iOS Host Usage — IN PR
- **UM** `Grok` Default light theme — IN PROGRESS 2026-08-10 (branch `grok/default-light-theme`). Web+iOS light default
- **UM** `Grok` ST OOM + Coolify/ST ops visibility — IN PROGRESS 2026-08-10 (branch `grok/st-ops-fleet-visibility`). Full ST health + Coolify fleet Operations card; host OOM/backup ops. Rollout: `docs/rollouts/2026-08-10-st-oom-and-fleet-ops-visibility.md`
- **UM** `Grok` ASC store listing + screenshots + App Store prep (Client + Local) — IN PROGRESS 2026-08-10 2:06pm CT. Public /privacy+/support; ASC en-US copy/categories/review/build attach; age rating set; 20 screenshots uploaded (iPhone 6.7 + iPad 12.9) COMPLETE; listing pack docs/asc/. Branch `grok/asc-store-listing-screenshots`. Privacy pages need prod deploy before Submit for Review
- **UM** `Grok` Coolify B2 replica heartbeat (fix env_active_unverified) — MERGED PR #1072 2026-08-10. Live B2 was fine; `/api/ready` backup red for missing side-channel. Host probe + Infisical path installed live (`replicaOk=true`). Code: in-container heartbeat + Coolify probe
- **UM** `Grok` iOS Client Monitor: backup layers + Hetzner host usage — MERGED PR #1075 2026-08-10 7:08pm CT. Local/B2/R2 historic backup layers on `/api/ready` + Settings; dual-auth `/api/server-metrics` for Hetzner host + Coolify apps (self + fleet)
- **UM** `Grok` ASC store listing + screenshots + App Store prep (Client + Local) — COMPLETED 2026-08-10 2:10pm CT. PR #1073 merged. ASC en-US copy/categories/age/review/builds + 20 screenshots COMPLETE. Public /privacy+/support shipped. Submit for Review still owner gate

## 2026-08-09

*29 PRs merged · 14 issues opened · 6 issues closed · 2 effort rows*

### Merged PRs

- **CT** `Claude` [#1590](https://github.com/jaywedgeworth22/Congress.Trade/pull/1590): docs(effort): closeout Lane 2 deterministic recovery _(by jaywedgeworth22)_
- **CT** [#1592](https://github.com/jaywedgeworth22/Congress.Trade/pull/1592): fix(health): signal only on genuinely stuck filings (provider stubs + legacy resolutions) _(by jaywedgeworth22)_
- **CT** [#1593](https://github.com/jaywedgeworth22/Congress.Trade/pull/1593): docs(agents): Apple Notes [APP, Agent] title + timestamp row _(by jaywedgeworth22)_
- **CT** [#1594](https://github.com/jaywedgeworth22/Congress.Trade/pull/1594): fix(ui): table grow/shrink on col resize + plain cleaning notes _(by jaywedgeworth22)_
- **CT** [#1595](https://github.com/jaywedgeworth22/Congress.Trade/pull/1595): fix(ui/web): themed-ink exchange toggle + real semantic legend colors _(by jaywedgeworth22)_
- **CT** `Claude` [#1596](https://github.com/jaywedgeworth22/Congress.Trade/pull/1596): fix(ios): restore broken main build; confirm Exchange filter already ships _(by jaywedgeworth22)_
- **CT** [#1597](https://github.com/jaywedgeworth22/Congress.Trade/pull/1597): fix(ios): Max Miller profile decode + build repair _(by jaywedgeworth22)_
- **CT** [#1600](https://github.com/jaywedgeworth22/Congress.Trade/pull/1600): fix(brand): light social OG share image with current eagle _(by jaywedgeworth22)_
- **CT** [#1602](https://github.com/jaywedgeworth22/Congress.Trade/pull/1602): fix(senate): thread env.SENATE_RELAY_URL explicitly (fixes intermittent WAF block) _(by jaywedgeworth22)_
- **CT** [#1603](https://github.com/jaywedgeworth22/Congress.Trade/pull/1603): docs(effort): Senate 5yr sweep — Docker hairpin NAT root cause + Cloudflare tunnel fix _(by jaywedgeworth22)_
- **CT** `Codex` [#1606](https://github.com/jaywedgeworth22/Congress.Trade/pull/1606): chore: standardize — Cloud coordination setup _(by jaywedgeworth22)_
- **CT** [#1608](https://github.com/jaywedgeworth22/Congress.Trade/pull/1608): docs(effort): Senate 5yr sweep COMPLETE — final results + House/Exec gap finding _(by jaywedgeworth22)_
- **CT** [#1610](https://github.com/jaywedgeworth22/Congress.Trade/pull/1610): fix(senate): route document fetches through the relay too, not just search _(by jaywedgeworth22)_
- **CT** [#1611](https://github.com/jaywedgeworth22/Congress.Trade/pull/1611): docs(effort): 3-branch gap root causes + fixes closeout _(by jaywedgeworth22)_
- **CT** [#1613](https://github.com/jaywedgeworth22/Congress.Trade/pull/1613): Owner UX punchlist: Trends formatting sweep, Directory People/Assets, Delivery overhaul, committees sync _(by jaywedgeworth22)_
- **CT** `Claude` [#1615](https://github.com/jaywedgeworth22/Congress.Trade/pull/1615): docs(effort): — punchlist closeout (#1613 merged) _(by jaywedgeworth22)_
- **CT** `Claude` [#1617](https://github.com/jaywedgeworth22/Congress.Trade/pull/1617): docs(effort): restamp — rows owner-local CT (UTC Z deprecated on boards) _(by jaywedgeworth22)_
- **ST** [#2598](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2598): feat(rag): monthly Pinecone write-unit breaker — stop paid re-embed churn on exhausted quota _(by jaywedgeworth22)_
- **ST** [#2599](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2599): fix(rag): "database is locked" is OUR SQLite, not a Pinecone outage _(by jaywedgeworth22)_
- **ST** [#2600](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2600): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2601](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2601): docs(agents): Apple Notes [APP, Agent] title + timestamp row _(by jaywedgeworth22)_
- **ST** [#2602](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2602): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2604](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2604): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **ST** [#2605](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2605): feat(rag): monthly Pinecone write-unit PACE guard + trial throughput audit _(by jaywedgeworth22)_
- **UM** [#1062](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1062): docs(agents): Apple Notes [APP, Agent] title + timestamp row _(by jaywedgeworth22)_
- **UM** [#1063](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1063): fix(nav): always show Usage Monitor brand next to icon on mobile _(by jaywedgeworth22)_
- **UM** `Codex` [#1065](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1065): chore: standardize — Cloud coordination setup _(by jaywedgeworth22)_
- **fleet** `Grok` [#15](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/15): docs(fleet): Apple Notes [APP, Agent] + timestamp standard _(by jaywedgeworth22)_
- **fleet** [#16](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/16): style(digest): polish activity site UI _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1586](https://github.com/jaywedgeworth22/Congress.Trade/issues/1586): 2026-08-09 — IN PR (auto-merge enabled) — Lane 2: deterministic-only
- **CT** [#1599](https://github.com/jaywedgeworth22/Congress.Trade/issues/1599): 2026-08-09 — IN PR (auto-merge enabled) — iOS Exchange filter confirm +
- **CT** [#1605](https://github.com/jaywedgeworth22/Congress.Trade/issues/1605): 2026-08-09T22:55Z — IN PROGRESS — Senate 5-year historical backfill
- **CT** [#1609](https://github.com/jaywedgeworth22/Congress.Trade/issues/1609): 2026-08-09T22:55Z — COMPLETED — Senate 5-year historical backfill
- **CT** [#1612](https://github.com/jaywedgeworth22/Congress.Trade/issues/1612): 2026-08-10T02:30Z — IN PROGRESS (pipeline draining) — 5-year/3-branch
- **CT** [#1614](https://github.com/jaywedgeworth22/Congress.Trade/issues/1614): 2026-08-09 — IN PR (auto-merge intended) — Owner web/iOS UX punchlist

### Issues opened

- **CT** [#1591](https://github.com/jaywedgeworth22/Congress.Trade/issues/1591): 2026-08-09 — DEPLOYED — Lane 2: deterministic-only stuck-filing
- **CT** [#1598](https://github.com/jaywedgeworth22/Congress.Trade/issues/1598): 2026-08-09 — IN PR (auto-merge enabled) — Icon/tooltip color fixes
- **CT** [#1599](https://github.com/jaywedgeworth22/Congress.Trade/issues/1599): 2026-08-09 — IN PR (auto-merge enabled) — iOS Exchange filter confirm +
- **CT** [#1601](https://github.com/jaywedgeworth22/Congress.Trade/issues/1601): 2026-08-09T22:21Z — IN PROGRESS — Social OG share image light refresh
- **CT** [#1604](https://github.com/jaywedgeworth22/Congress.Trade/issues/1604): Senate ingestion relay depends on an ephemeral tunnel + one agent's Mac staying on
- **CT** [#1605](https://github.com/jaywedgeworth22/Congress.Trade/issues/1605): 2026-08-09T22:55Z — IN PROGRESS — Senate 5-year historical backfill
- **CT** [#1607](https://github.com/jaywedgeworth22/Congress.Trade/issues/1607): House + Executive 2024-2025 coverage dip — House 2025 fully absent
- **CT** [#1609](https://github.com/jaywedgeworth22/Congress.Trade/issues/1609): 2026-08-09T22:55Z — COMPLETED — Senate 5-year historical backfill
- **CT** [#1612](https://github.com/jaywedgeworth22/Congress.Trade/issues/1612): 2026-08-10T02:30Z — IN PROGRESS (pipeline draining) — 5-year/3-branch
- **CT** [#1614](https://github.com/jaywedgeworth22/Congress.Trade/issues/1614): 2026-08-09 — IN PR (auto-merge intended) — Owner web/iOS UX punchlist
- **CT** [#1616](https://github.com/jaywedgeworth22/Congress.Trade/issues/1616): 2026-08-09 — COMPLETED/MERGED (#1613) — Owner web/iOS UX punchlist
- **CT** [#1618](https://github.com/jaywedgeworth22/Congress.Trade/issues/1618): 2026-08-09 9:30pm CT — IN PROGRESS (pipeline draining)
- **CT** [#1619](https://github.com/jaywedgeworth22/Congress.Trade/issues/1619): 2026-08-09 5:55pm CT — COMPLETED — Senate 5-year historical backfill
- **UM** [#1064](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1064): Mobile nav brand label always visible ("Usage Monitor") — IN PR #1063

### Effort board

- **UM** `Grok` OpenRouter credit probe endpoint + dedicated UptimeRobot — IN PROGRESS 2026-08-09 11:45pm CT. `GET /api/openrouter-credits` uses management key for account /credits + per-key limit_remaining; new UptimeRobot keyword monitor (ST health monitor unchanged). Rollout: `docs/rollouts/2026-08-10-openrouter-credit-probe-uptimerobot.md`
- **UM** `Grok` Mobile nav brand label always visible ("Usage Monitor") — IN PR #1063 2026-08-09. Nav currently hides title below sm; show icon+text on mobile. Website: Usage Monitor; iOS apps keep CFBundleDisplayName (Usage Client/Local Monitor)

## 2026-08-08

*56 PRs merged · 32 issues opened · 24 issues closed · 0 effort rows*

### Merged PRs

- **CT** [#1516](https://github.com/jaywedgeworth22/Congress.Trade/pull/1516): fix(secrets/ios): Infisical aliases + cream AppIcon _(by jaywedgeworth22)_
- **CT** `Grok` [#1517](https://github.com/jaywedgeworth22/Congress.Trade/pull/1517): feat(ui): click politician, trade, or company anywhere _(by jaywedgeworth22)_
- **CT** `Grok` [#1518](https://github.com/jaywedgeworth22/Congress.Trade/pull/1518): fix(logos): reject empty logo.dev bodies and fall through _(by jaywedgeworth22)_
- **CT** [#1519](https://github.com/jaywedgeworth22/Congress.Trade/pull/1519): ci: always enable auto-merge on non-draft PRs _(by jaywedgeworth22)_
- **CT** [#1520](https://github.com/jaywedgeworth22/Congress.Trade/pull/1520): ci: hosted-runner fallback via CT_CI_RUNNER gate (oracle box down) _(by jaywedgeworth22)_
- **CT** [#1521](https://github.com/jaywedgeworth22/Congress.Trade/pull/1521): fix(server): silence CSP and 404 noise from console _(by jaywedgeworth22)_
- **CT** `Claude` [#1522](https://github.com/jaywedgeworth22/Congress.Trade/pull/1522): fix(ios): wire ticker/politician tap-through on Trends rows _(by jaywedgeworth22)_
- **CT** [#1524](https://github.com/jaywedgeworth22/Congress.Trade/pull/1524): fix(deps): bump nanoid — unblocks the repo-wide red Audit gate _(by jaywedgeworth22)_
- **CT** `Claude` [#1525](https://github.com/jaywedgeworth22/Congress.Trade/pull/1525): fix(delivery): server-side asset display-name resolver _(by jaywedgeworth22)_
- **CT** [#1528](https://github.com/jaywedgeworth22/Congress.Trade/pull/1528): fix(members): dedupe split filer identities + party label + perf (#1452, #1454) _(by jaywedgeworth22)_
- **CT** `Claude` [#1531](https://github.com/jaywedgeworth22/Congress.Trade/pull/1531): feat(ui): owner UX work order — toolbar groups, mobile menu, latency placement, click-anywhere _(by jaywedgeworth22)_
- **CT** [#1532](https://github.com/jaywedgeworth22/Congress.Trade/pull/1532): fix(ui): Trends shared filter row parity on desktop (verifier follow-up to #1531) _(by jaywedgeworth22)_
- **CT** [#1533](https://github.com/jaywedgeworth22/Congress.Trade/pull/1533): feat(ui): design convergence — adopt app design language _(by jaywedgeworth22)_
- **CT** [#1535](https://github.com/jaywedgeworth22/Congress.Trade/pull/1535): fix(ui): mobile count-row grid via ID specificity (design-QA follow-up to #1533) + board closeout _(by jaywedgeworth22)_
- **CT** `Grok` [#1538](https://github.com/jaywedgeworth22/Congress.Trade/pull/1538): fix(ios): rename xcodeproj to Congress.Trade.xcodeproj _(by jaywedgeworth22)_
- **CT** `Claude` [#1540](https://github.com/jaywedgeworth22/Congress.Trade/pull/1540): feat(ios): owner punch list #2 — chrome, sort, pages, People tab, menu _(by jaywedgeworth22)_
- **CT** `Claude` [#1541](https://github.com/jaywedgeworth22/Congress.Trade/pull/1541): feat(ui): owner punch list #2 — web chrome + drawers _(by jaywedgeworth22)_
- **CT** `Grok` [#1544](https://github.com/jaywedgeworth22/Congress.Trade/pull/1544): fix(ops): stop sqlite-web crash loop that 502'd congress.trade _(by jaywedgeworth22)_
- **CT** [#1546](https://github.com/jaywedgeworth22/Congress.Trade/pull/1546): chore: congress-trade@1.0.0 package identity _(by jaywedgeworth22)_
- **CT** `Claude` [#1547](https://github.com/jaywedgeworth22/Congress.Trade/pull/1547): feat(ios): multi-select filter menus _(by jaywedgeworth22)_
- **CT** [#1550](https://github.com/jaywedgeworth22/Congress.Trade/pull/1550): docs: off-host backups live (B2 primary + weekly R2 pending token) _(by jaywedgeworth22)_
- **CT** `Claude` [#1551](https://github.com/jaywedgeworth22/Congress.Trade/pull/1551): fix(ui): owner follow-up batch — badge clip P1 + 11 Trends/mobile fixes _(by jaywedgeworth22)_
- **CT** [#1553](https://github.com/jaywedgeworth22/Congress.Trade/pull/1553): feat(auth,billing): Sign in with Apple + StoreKit 2 IAP backend, entitlement Stripe-OR-Apple _(by jaywedgeworth22)_
- **CT** [#1555](https://github.com/jaywedgeworth22/Congress.Trade/pull/1555): docs(effort-log): closeout Apple backend lane _(by jaywedgeworth22)_
- **CT** [#1557](https://github.com/jaywedgeworth22/Congress.Trade/pull/1557): fix(ui): sticky Slowest Filers header + remove dead 60px table gutter _(by jaywedgeworth22)_
- **CT** `Claude` [#1558](https://github.com/jaywedgeworth22/Congress.Trade/pull/1558): feat(ios): Sign in with Apple + StoreKit 2 IAP client _(by jaywedgeworth22)_
- **CT** [#1560](https://github.com/jaywedgeworth22/Congress.Trade/pull/1560): SECURITY: lock down live unverified Apple premium-grant endpoint _(by jaywedgeworth22)_
- **CT** `Claude` [#1561](https://github.com/jaywedgeworth22/Congress.Trade/pull/1561): fix(ios): route Manage Subscription by entitlement source, harden Apple sign-in _(by jaywedgeworth22)_
- **CT** `Claude` [#1562](https://github.com/jaywedgeworth22/Congress.Trade/pull/1562): fix(security): full X.509 path validation for Apple JWS x5c chain _(by jaywedgeworth22)_
- **CT** `Grok` [#1564](https://github.com/jaywedgeworth22/Congress.Trade/pull/1564): feat(ui/ops): trades << < > >> pager + autonomous uptime recovery _(by jaywedgeworth22)_
- **CT** [#1565](https://github.com/jaywedgeworth22/Congress.Trade/pull/1565): docs(ios): TestFlight ship receipt + ASC API-key signing runbook _(by jaywedgeworth22)_
- **CT** `Claude` [#1566](https://github.com/jaywedgeworth22/Congress.Trade/pull/1566): fix(ui): trades count accuracy + stable table layout _(by jaywedgeworth22)_
- **CT** [#1569](https://github.com/jaywedgeworth22/Congress.Trade/pull/1569): fix(feed): name search returned zero for real senators; zero-result totals froze _(by jaywedgeworth22)_
- **CT** `Grok` [#1570](https://github.com/jaywedgeworth22/Congress.Trade/pull/1570): feat(brand): hi-res lockup + transparent web icons; opaque iOS AppIcon _(by jaywedgeworth22)_
- **CT** [#1573](https://github.com/jaywedgeworth22/Congress.Trade/pull/1573): fix(review-queue): make review_queue.resolved=1 an honest signal _(by jaywedgeworth22)_
- **CT** [#1579](https://github.com/jaywedgeworth22/Congress.Trade/pull/1579): fix(ingestion): autonomy fixes so pipeline self-heals without an operator _(by jaywedgeworth22)_
- **CT** `Grok` [#1581](https://github.com/jaywedgeworth22/Congress.Trade/pull/1581): fix(ios): owner AppIcon plate (opaque only) _(by jaywedgeworth22)_
- **CT** [#1582](https://github.com/jaywedgeworth22/Congress.Trade/pull/1582): fix(ingestion): autonomy sweeps + health were blind to the exact backlog they target _(by jaywedgeworth22)_
- **CT** `Claude` [#1583](https://github.com/jaywedgeworth22/Congress.Trade/pull/1583): fix(extraction): OGE 278-T parser for stuck executive-branch filings _(by jaywedgeworth22)_
- **CT** `Grok` [#1584](https://github.com/jaywedgeworth22/Congress.Trade/pull/1584): docs(effort): closeout trades pager + uptime recovery #1564 _(by jaywedgeworth22)_
- **CT** `Grok` [#1585](https://github.com/jaywedgeworth22/Congress.Trade/pull/1585): docs(agents): Apple Notes close-out seat + living updates _(by jaywedgeworth22)_
- **CT** `Claude` [#1588](https://github.com/jaywedgeworth22/Congress.Trade/pull/1588): chore(admin): add read-only /debug-raw-text/:id diagnostic _(by jaywedgeworth22)_
- **CT** `Claude` [#1589](https://github.com/jaywedgeworth22/Congress.Trade/pull/1589): fix(extraction): ogeText must not split merged text on newlines _(by jaywedgeworth22)_
- **ST** [#2586](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2586): fix(settings): rename Phone push channel to ntfy.sh, drop recommended badge _(by jaywedgeworth22)_
- **ST** [#2587](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2587): feat(backup): weekly R2 cold snapshot of prod SQLite (second-provider DR) _(by jaywedgeworth22)_
- **ST** [#2588](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2588): fix(console): real /console/decisions index page (#2556) _(by jaywedgeworth22)_
- **ST** [#2589](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2589): fix(results): data-integrity wave B — sanity-bound inferred transfers, SPY-unavailable state, lot-ledger reconciliation (#2557, #2548) _(by jaywedgeworth22)_
- **ST** [#2590](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2590): fix(feed): route ingest/embed audits to System, fold BUY/TRADE duplicate rows, roll up no-op embed audits (#2553) _(by jaywedgeworth22)_
- **ST** [#2591](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2591): fix(mobile): PWA market session + collapsed receipts; iOS SSE connected indicator (#2559, #2551) _(by jaywedgeworth22)_
- **ST** [#2594](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2594): feat(console): sentence-gap copy rule + Proposals empty-state merge (owner mobile punch list 2026-08-08, items 1-2) _(by jaywedgeworth22)_
- **ST** [#2595](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2595): style(chrome): Run-once glyph = emoji bolt (owner preference 2026-08-08) — chrome button + empty-state inline reference _(by jaywedgeworth22)_
- **ST** [#2596](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2596): feat(rag): monthly Pinecone write-unit breaker — stop paid re-embed churn on exhausted quota _(by jaywedgeworth22)_
- **UM** [#1057](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1057): feat(web): iOS client AppIcon for favicon, nav, and PWA _(by jaywedgeworth22)_
- **UM** [#1059](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1059): ci: always enable auto-merge on non-draft PRs _(by jaywedgeworth22)_
- **UM** `Grok` [#1060](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1060): docs(agents): Apple Notes close-out seat + living updates _(by jaywedgeworth22)_
- **UM** [#1061](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1061): fix(ios): declare no non-exempt encryption for TestFlight _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1452](https://github.com/jaywedgeworth22/Congress.Trade/issues/1452): Data: duplicate member identities split trade history (e.g. 'Michael T. McCaul' vs 'Michael McCaul')
- **CT** [#1454](https://github.com/jaywedgeworth22/Congress.Trade/issues/1454): Perf: /api/members takes ~6s — People tab stuck on 'Loading directory…'
- **CT** [#1455](https://github.com/jaywedgeworth22/Congress.Trade/issues/1455): Owner decision: Filing Latency Comparison widget placement + copy (currently self-reports 8% win vs Quiver on every public tab)
- **CT** [#1456](https://github.com/jaywedgeworth22/Congress.Trade/issues/1456): Mobile: brand logo hidden behind 3-button theme toggle at 375px; disclaimer auto-expanded eats first screen
- **CT** [#1526](https://github.com/jaywedgeworth22/Congress.Trade/issues/1526): 2026-08-08T14:49Z — IN PR (auto-merge enabled) — iOS entity
- **CT** [#1527](https://github.com/jaywedgeworth22/Congress.Trade/issues/1527): 2026-08-08 — PR OPEN (auto-merge queued) — Server-side asset
- **CT** [#1530](https://github.com/jaywedgeworth22/Congress.Trade/issues/1530): 2026-08-08 — IN PR — Members directory dedupe + perf (#1452, #1454)
- **CT** [#1534](https://github.com/jaywedgeworth22/Congress.Trade/issues/1534): 2026-08-08T16:29Z — IN PR (auto-merge enabled) — Design convergence
- **CT** [#1536](https://github.com/jaywedgeworth22/Congress.Trade/issues/1536): 2026-08-08 — COMPLETED — Owner UX work-order wave + review-issue fixes
- **CT** [#1554](https://github.com/jaywedgeworth22/Congress.Trade/issues/1554): 2026-08-09 — IN PR — Apple backend: Sign in with Apple + StoreKit 2
- **CT** [#1556](https://github.com/jaywedgeworth22/Congress.Trade/issues/1556): 2026-08-09 — MERGED (162163b2) — Apple backend: Sign in with Apple +
- **CT** [#1568](https://github.com/jaywedgeworth22/Congress.Trade/issues/1568): 2026-08-09T00:31Z — IN PROGRESS — Trades pager <<<> >> + autonomous
- **ST** [#2547](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2547): P1: shared-package lockfile drift — manifest pins congress-trading-shared v2.5.1, lockfile ships 2.5.0 (filingDate member-skill dependency not deployed)
- **ST** [#2548](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2548): P1: open-lots ledger contradicts live positions (T long 91.119 vs actual short −1.881; AXP lot with no position) — tax/wash-sale numbers built on wrong lots
- **ST** [#2549](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2549): P1: two short positions sit unmanaged (Protection '—') because shortSellingEnabled is off with shorts on the book — needs an attention banner
- **ST** [#2551](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2551): P1: PWA proposal cards need the console's collapsed-receipt treatment (raw [Sizing]/[Risk] wall on mobile)
- **ST** [#2552](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2552): P2: Red Team critic failures are under-surfaced — show cause on the chip and track failure rate (4 of 5 pending proposals had no working critic)
- **ST** [#2553](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2553): P2: Activity feed signal-to-noise — duplicate BUY/TRADE rows per action, SEC-ingest flood bypasses the System group, per-minute no-op embed audits
- **ST** [#2554](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2554): P2: cross-surface run-state vocabulary — PWA says 'Running' while console says 'Paused · market closed' for the same account
- **ST** [#2555](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2555): P2: alert center fatigue — per-condition mute/snooze + single provider-outage rollup row
- **ST** [#2556](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2556): P1: Home 'All Decisions' link 404s — /console/decisions has no index page (verified live)
- **ST** [#2557](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2557): P1: inflated account return persists AFTER #2536 — phantom $36.5k inferred withdrawal + SPY benchmark 0.00% (live repro on build containing the fix)
- **ST** [#2559](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2559): P2: mobile stream/session state bugs — iOS 'Live updates' indicator stays false on healthy idle stream; PWA Market metric always renders 'Closed' (marketSession type drift)
- **ST** [#2562](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2562): P2/P3: stale-copy + dead-code polish batch — FMP mentions in live tooltips/captions, paper-mode vocabulary, Coach/Assistant label, dead event, dark-mode candle colors, misc iOS

### Issues opened

- **CT** [#1523](https://github.com/jaywedgeworth22/Congress.Trade/issues/1523): Latency comparison undercounts cross-source matches — methodology redesign (owner request 2026-08-08)
- **CT** [#1526](https://github.com/jaywedgeworth22/Congress.Trade/issues/1526): 2026-08-08T14:49Z — IN PR (auto-merge enabled) — iOS entity
- **CT** [#1527](https://github.com/jaywedgeworth22/Congress.Trade/issues/1527): 2026-08-08 — PR OPEN (auto-merge queued) — Server-side asset
- **CT** [#1529](https://github.com/jaywedgeworth22/Congress.Trade/issues/1529): Design convergence: web adopts the iOS app's design language (one system on both)
- **CT** [#1530](https://github.com/jaywedgeworth22/Congress.Trade/issues/1530): 2026-08-08 — IN PR — Members directory dedupe + perf (#1452, #1454)
- **CT** [#1534](https://github.com/jaywedgeworth22/Congress.Trade/issues/1534): 2026-08-08T16:29Z — IN PR (auto-merge enabled) — Design convergence
- **CT** [#1536](https://github.com/jaywedgeworth22/Congress.Trade/issues/1536): 2026-08-08 — COMPLETED — Owner UX work-order wave + review-issue fixes
- **CT** [#1537](https://github.com/jaywedgeworth22/Congress.Trade/issues/1537): Deploy: brief 'no available server' downtime on every Coolify container swap
- **CT** [#1539](https://github.com/jaywedgeworth22/Congress.Trade/issues/1539): 2026-08-08T18:55Z — IN PROGRESS — iOS xcodeproj brand rename
- **CT** [#1542](https://github.com/jaywedgeworth22/Congress.Trade/issues/1542): 2026-08-09 — IN PR — Web punch list #2 — web chrome + drawers (Lanes
- **CT** [#1543](https://github.com/jaywedgeworth22/Congress.Trade/issues/1543): 2026-08-09 — IN PR (auto-merge enabled) — iOS punch list lane I1+I2
- **CT** [#1545](https://github.com/jaywedgeworth22/Congress.Trade/issues/1545): 2026-08-08T20:40Z — IN PR — Root cause: empty SQLITEWEBPASSWORD →
- **CT** [#1548](https://github.com/jaywedgeworth22/Congress.Trade/issues/1548): 2026-08-09 — IN PR (auto-merge enabled) — iOS multi-select filter pills
- **CT** [#1549](https://github.com/jaywedgeworth22/Congress.Trade/issues/1549): iOS: pre-existing testSetTradeTypeSendsTypeQueryParam mock race (flaky on main)
- **CT** [#1552](https://github.com/jaywedgeworth22/Congress.Trade/issues/1552): 2026-08-09 — IN PR (auto-merge enabled) — Web owner follow-up batch #2
- **CT** [#1554](https://github.com/jaywedgeworth22/Congress.Trade/issues/1554): 2026-08-09 — IN PR — Apple backend: Sign in with Apple + StoreKit 2
- **CT** [#1556](https://github.com/jaywedgeworth22/Congress.Trade/issues/1556): 2026-08-09 — MERGED (162163b2) — Apple backend: Sign in with Apple +
- **CT** [#1559](https://github.com/jaywedgeworth22/Congress.Trade/issues/1559): 2026-08-09 — IN PR (auto-merge enabled) — iOS Sign in with Apple +
- **CT** [#1563](https://github.com/jaywedgeworth22/Congress.Trade/issues/1563): 2026-08-09 — IN PR (auto-merge enabled) — SECURITY: Apple JWS x5c full
- **CT** [#1567](https://github.com/jaywedgeworth22/Congress.Trade/issues/1567): 2026-08-09 — IN PR (auto-merge enabled) — Trades-tab count accuracy (3
- **CT** [#1568](https://github.com/jaywedgeworth22/Congress.Trade/issues/1568): 2026-08-09T00:31Z — IN PROGRESS — Trades pager <<<> >> + autonomous
- **CT** [#1571](https://github.com/jaywedgeworth22/Congress.Trade/issues/1571): 2026-08-09T03:57Z — IN PROGRESS — Hi-res brand lockup + white-letter
- **CT** [#1574](https://github.com/jaywedgeworth22/Congress.Trade/issues/1574): One-time backfill: reconcile 547 filings rows desynced from resolved review_queue state
- **CT** [#1575](https://github.com/jaywedgeworth22/Congress.Trade/issues/1575): scanned_pdf corpus needs vision/OCR extraction — deliberately out of scope for the deterministic autonomy fix
- **CT** [#1576](https://github.com/jaywedgeworth22/Congress.Trade/issues/1576): Data hygiene: delete manual test-probe row S — should-not-exist-zzzz from prod filings
- **CT** [#1577](https://github.com/jaywedgeworth22/Congress.Trade/issues/1577): Check whether the House bulk FD ZIP fetch is degraded (186 persisted rows stuck filed_date-NULL past catch-up window)
- **CT** [#1578](https://github.com/jaywedgeworth22/Congress.Trade/issues/1578): 2026-08-09 — IN PR (auto-merge enabled) — Review-queue false "all done"
- **CT** [#1580](https://github.com/jaywedgeworth22/Congress.Trade/issues/1580): 2026-08-09 — IN PR (auto-merge enabled) — Ingestion pipeline autonomy
- **CT** [#1586](https://github.com/jaywedgeworth22/Congress.Trade/issues/1586): 2026-08-09 — IN PR (auto-merge enabled) — Lane 2: deterministic-only
- **CT** [#1587](https://github.com/jaywedgeworth22/Congress.Trade/issues/1587): 2026-08-09T04:33Z — COMPLETED/DEPLOYED — Trades pager + autonomous
- **ST** [#2592](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2592): P2: PWA delete-account collapsed button has no onClick — danger zone can never be opened from the UI
- **ST** [#2593](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2593): P2: strategy.ts regenerates proposalId between receipt-emit and persist — orphaned receipts (source fix for the BUY/TRADE feed dup)

## 2026-08-07

*50 PRs merged · 33 issues opened · 22 issues closed · 7 effort rows*

### Merged PRs

- **CT** `Grok` [#1451](https://github.com/jaywedgeworth22/Congress.Trade/pull/1451): feat(latency): single UW key + RAPIDAPI Infisical _(by jaywedgeworth22)_
- **CT** [#1461](https://github.com/jaywedgeworth22/Congress.Trade/pull/1461): docs: full-product review 2026-08-06 + effort-board audit fixes _(by jaywedgeworth22)_
- **CT** `Grok` [#1463](https://github.com/jaywedgeworth22/Congress.Trade/pull/1463): fix(scout): restore run-scout.sh PM2 entrypoint _(by jaywedgeworth22)_
- **CT** `Grok` [#1464](https://github.com/jaywedgeworth22/Congress.Trade/pull/1464): fix(latency): dual free FMP keys + RapidAPI congress 404 default-off _(by jaywedgeworth22)_
- **CT** [#1465](https://github.com/jaywedgeworth22/Congress.Trade/pull/1465): fix(r2): CT subject token, sent-from, digest at 20Z _(by jaywedgeworth22)_
- **CT** [#1466](https://github.com/jaywedgeworth22/Congress.Trade/pull/1466): fix(export): premium CSV is full match set, no silent row cap _(by jaywedgeworth22)_
- **CT** [#1467](https://github.com/jaywedgeworth22/Congress.Trade/pull/1467): docs(ui): fleet copy canon + iOS inline nav titles _(by jaywedgeworth22)_
- **CT** [#1468](https://github.com/jaywedgeworth22/Congress.Trade/pull/1468): feat(ios): pictographic theme control + fleet UI copy _(by jaywedgeworth22)_
- **CT** [#1469](https://github.com/jaywedgeworth22/Congress.Trade/pull/1469): fix(ios): logos, amount k/m ranges, Trends toolbar _(by jaywedgeworth22)_
- **CT** [#1470](https://github.com/jaywedgeworth22/Congress.Trade/pull/1470): fix(ios): trade logos, amount k/m, politicians label _(by jaywedgeworth22)_
- **CT** [#1471](https://github.com/jaywedgeworth22/Congress.Trade/pull/1471): fix(ui): spell out politicians when roomy, pol/pols when tight _(by jaywedgeworth22)_
- **CT** [#1472](https://github.com/jaywedgeworth22/Congress.Trade/pull/1472): fix(ios): enlarge BrandTitle ~50% in sticky nav bar _(by jaywedgeworth22)_
- **CT** `Grok` [#1473](https://github.com/jaywedgeworth22/Congress.Trade/pull/1473): feat(extraction): OR budget circuit, per-doc cap, coverage scorecard _(by jaywedgeworth22)_
- **CT** `Grok` [#1484](https://github.com/jaywedgeworth22/Congress.Trade/pull/1484): fix(ops): scorecard join filings; sqlite-web loopback port _(by jaywedgeworth22)_
- **CT** `Grok` [#1485](https://github.com/jaywedgeworth22/Congress.Trade/pull/1485): docs(effort): closeout OR scorecard PR #1473 _(by jaywedgeworth22)_
- **CT** `Grok` [#1489](https://github.com/jaywedgeworth22/Congress.Trade/pull/1489): fix(ios): repair TickerDetailView navigationTitle compile break _(by jaywedgeworth22)_
- **CT** [#1491](https://github.com/jaywedgeworth22/Congress.Trade/pull/1491): fix(ios): real App Store screenshots from latest UI _(by jaywedgeworth22)_
- **CT** [#1492](https://github.com/jaywedgeworth22/Congress.Trade/pull/1492): fix(ios): real App Store screenshots from latest UI _(by jaywedgeworth22)_
- **CT** [#1493](https://github.com/jaywedgeworth22/Congress.Trade/pull/1493): fix(copy): capitalize Congress and Congressional as proper nouns _(by jaywedgeworth22)_
- **CT** [#1494](https://github.com/jaywedgeworth22/Congress.Trade/pull/1494): chore(deps): bump @aws-sdk/client-s3 from 3.1101.0 to 3.1102.0 in /app _(by dependabot[bot])_
- **CT** [#1495](https://github.com/jaywedgeworth22/Congress.Trade/pull/1495): chore(deps-dev): bump @typescript-eslint/eslint-plugin from 8.65.0 to 8.66.0 in /app _(by dependabot[bot])_
- **CT** [#1496](https://github.com/jaywedgeworth22/Congress.Trade/pull/1496): chore(deps-dev): bump @typescript-eslint/parser from 8.65.0 to 8.66.0 in /app _(by dependabot[bot])_
- **CT** `Grok` [#1500](https://github.com/jaywedgeworth22/Congress.Trade/pull/1500): fix(ios): deployment target 17.0 — fix Invalid Binary _(by jaywedgeworth22)_
- **CT** `Grok` [#1501](https://github.com/jaywedgeworth22/Congress.Trade/pull/1501): fix(ios): brand lockup spacing + 10% scale _(by jaywedgeworth22)_
- **CT** `Grok` [#1502](https://github.com/jaywedgeworth22/Congress.Trade/pull/1502): fix(ios): compact All filter chips; hide APNs debug token _(by jaywedgeworth22)_
- **CT** `Grok` [#1504](https://github.com/jaywedgeworth22/Congress.Trade/pull/1504): fix(ios): cream 3D AppIcon for TestFlight / App Store _(by jaywedgeworth22)_
- **CT** `Grok` [#1505](https://github.com/jaywedgeworth22/Congress.Trade/pull/1505): fix(logos): LOGO_DEV_TOKEN alias + local ticker pack _(by jaywedgeworth22)_
- **CT** `Grok` [#1507](https://github.com/jaywedgeworth22/Congress.Trade/pull/1507): docs: Logo.dev #1505 deploy closeout _(by jaywedgeworth22)_
- **CT** `Grok` [#1509](https://github.com/jaywedgeworth22/Congress.Trade/pull/1509): docs(effort): closeout iOS PRs #1500–#1504 _(by jaywedgeworth22)_
- **CT** [#1511](https://github.com/jaywedgeworth22/Congress.Trade/pull/1511): fix(ui/ios): owner-spaced light + white-letter dark brand lockups _(by jaywedgeworth22)_
- **CT** `Grok` [#1513](https://github.com/jaywedgeworth22/Congress.Trade/pull/1513): fix(agreement): soft free-text + ST infer so cascade auto-publishes _(by jaywedgeworth22)_
- **ST** [#2580](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2580): fix(ios): title-case UI headings/buttons; quieter Live/Paper copy _(by jaywedgeworth22)_
- **ST** [#2581](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2581): fix(perf): neutralize deposit+invest gaps so paper vs-SPY is not +50% _(by jaywedgeworth22)_
- **ST** [#2583](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2583): docs: README + deployment + GitHub About for Alpaca/Tradier/Robinhood + Hetzner _(by jaywedgeworth22)_
- **ST** [#2584](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2584): feat(backup): active litestream replica → Backblaze B2 _(by jaywedgeworth22)_
- **UM** [#1021](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1021): fix(ui): More only when needed + provider table layout _(by jaywedgeworth22)_
- **UM** [#1035](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1035): feat: 7/3/1d renewal notices + receipt no-double-count copy _(by jaywedgeworth22)_
- **UM** [#1036](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1036): fix(ios): Providers taps, backup status, timeframe, split EOM projection _(by jaywedgeworth22)_
- **UM** [#1038](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1038): docs: effort closeout for iOS reliability PR #1036 _(by jaywedgeworth22)_
- **UM** [#1039](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1039): fix(ios-local): product label "on-device self-host" _(by jaywedgeworth22)_
- **UM** [#1041](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1041): feat(ui): fleet copy — not reported, lowercase k, inline titles _(by jaywedgeworth22)_
- **UM** [#1042](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1042): fix(ios): no-budget card + Title Case copy (ST parity) _(by jaywedgeworth22)_
- **UM** [#1044](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1044): docs: adopt FLEET-UI-COPY.md as sole UI copy canon _(by jaywedgeworth22)_
- **UM** [#1045](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1045): docs: effort closeout cites FLEET-UI-COPY.md _(by jaywedgeworth22)_
- **UM** [#1047](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1047): feat(ios-local): web parity wave 1 — overview, providers, EOM split _(by jaywedgeworth22)_
- **UM** [#1049](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1049): feat(ios-local): catalog connection wave — ChatGPT, abilities, ensure-all _(by jaywedgeworth22)_
- **UM** [#1051](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1051): feat(ops): Litestream primary to Backblaze B2; leave R2 historic _(by jaywedgeworth22)_
- **UM** [#1053](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1053): fix(ops): Hetzner deploy observer + Coolify SOURCE_COMMIT revision _(by jaywedgeworth22)_
- **UM** [#1055](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1055): feat(ios): circuit icons — arrows (Usage Monitor) + lock (Local) _(by jaywedgeworth22)_
- **UM** [#1058](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1058): feat(ios): Usage Client/Local Monitor names + matching bundle IDs _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1412](https://github.com/jaywedgeworth22/Congress.Trade/issues/1412): 2026-08-05 — IN PR — #1040 extract dashboard assets PR #1406; #1039
- **CT** [#1413](https://github.com/jaywedgeworth22/Congress.Trade/issues/1413): 2026-08-05 — IN PROGRESS — Land remaining open PRs #1407/#1409/#1410
- **CT** [#1432](https://github.com/jaywedgeworth22/Congress.Trade/issues/1432): 2026-08-06T05:10Z — IN PROGRESS — Web+iOS filter parity, brand header
- **CT** [#1435](https://github.com/jaywedgeworth22/Congress.Trade/issues/1435): 2026-08-06T05:18Z — COMPLETED — Latency honesty: FMP merge + QQ
- **CT** [#1445](https://github.com/jaywedgeworth22/Congress.Trade/issues/1445): 2026-08-06T14:19Z — IN PROGRESS — Latency week focus: track
- **CT** [#1449](https://github.com/jaywedgeworth22/Congress.Trade/issues/1449): 2026-08-06T18:35Z — IN PROGRESS — iOS APNs register: fix delivery must
- **CT** [#1478](https://github.com/jaywedgeworth22/Congress.Trade/issues/1478): 2026-08-06 — COMPLETED — Full-product review (owner request): web + iOS
- **CT** [#1479](https://github.com/jaywedgeworth22/Congress.Trade/issues/1479): 2026-08-06T18:35Z — COMPLETED/DEPLOYED 2026-08-06T19:06Z — iOS APNs
- **CT** [#1480](https://github.com/jaywedgeworth22/Congress.Trade/issues/1480): 2026-08-06T12:34Z — COMPLETED 2026-08-06T12:43Z — LATENCY FOCUS
- **CT** [#1481](https://github.com/jaywedgeworth22/Congress.Trade/issues/1481): 2026-08-06 — COMPLETED/DEPLOYED 2026-08-06T06:07Z — Latency probe yield
- **CT** [#1482](https://github.com/jaywedgeworth22/Congress.Trade/issues/1482): 2026-08-04 — R2 free-tier opt (ST/CT/UM). Class A pace ST 74%/CT 123%;
- **CT** [#1486](https://github.com/jaywedgeworth22/Congress.Trade/issues/1486): 2026-08-07T07:15Z — IN PROGRESS — OR budget circuit (2–3 then hourly) +
- **CT** [#1487](https://github.com/jaywedgeworth22/Congress.Trade/issues/1487): 2026-07-19 — Conflict-resolution merge of current main into PR #620
- **CT** [#1488](https://github.com/jaywedgeworth22/Congress.Trade/issues/1488): [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger +
- **CT** [#1506](https://github.com/jaywedgeworth22/Congress.Trade/issues/1506): 2026-08-07T15:19Z — IN PROGRESS — Logo.dev prod wire: land PR #1505
- **CT** [#1512](https://github.com/jaywedgeworth22/Congress.Trade/issues/1512): 2026-08-07T16:04Z — IN PROGRESS — Web light+dark brand lockup from owner
- **ST** [#2546](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2546): P0 (owner decision): prod DB litestream→R2 replication PAUSED since Aug 4 — no continuous backup; R2 free-tier pressure fleet-wide
- **UM** [#1029](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1029): [Uptime] Usage Monitor Oracle origin readiness failure
- **UM** [#1037](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1037): [2026-08-07] iOS: Providers tap reliability, backup status restore
- **UM** [#1040](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1040): [2026-08-07] iOS: Providers tap reliability, backup status restore
- **UM** [#1043](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1043): [2026-08-07] iOS no-budget card + Title Case copy (ST e4e229e0 parity)
- **UM** [#1046](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1046): [2026-08-07] iOS no-budget card + Title Case + FLEET-UI-COPY canon

### Issues opened

- **CT** [#1474](https://github.com/jaywedgeworth22/Congress.Trade/issues/1474): 2026-08-05 — R2 Class A emergency pause (host litestream-congress
- **CT** [#1475](https://github.com/jaywedgeworth22/Congress.Trade/issues/1475): iOS TestFlight agent ship pipeline (cross-app) — IN PR 2026-08-04 (ST
- **CT** [#1476](https://github.com/jaywedgeworth22/Congress.Trade/issues/1476): 2026-08-06T14:19Z — IN PROGRESS — Latency week focus: track
- **CT** [#1477](https://github.com/jaywedgeworth22/Congress.Trade/issues/1477): 2026-08-06T05:10Z — IN PROGRESS — Web+iOS filter parity, brand header
- **CT** [#1478](https://github.com/jaywedgeworth22/Congress.Trade/issues/1478): 2026-08-06 — COMPLETED — Full-product review (owner request): web + iOS
- **CT** [#1479](https://github.com/jaywedgeworth22/Congress.Trade/issues/1479): 2026-08-06T18:35Z — COMPLETED/DEPLOYED 2026-08-06T19:06Z — iOS APNs
- **CT** [#1480](https://github.com/jaywedgeworth22/Congress.Trade/issues/1480): 2026-08-06T12:34Z — COMPLETED 2026-08-06T12:43Z — LATENCY FOCUS
- **CT** [#1481](https://github.com/jaywedgeworth22/Congress.Trade/issues/1481): 2026-08-06 — COMPLETED/DEPLOYED 2026-08-06T06:07Z — Latency probe yield
- **CT** [#1482](https://github.com/jaywedgeworth22/Congress.Trade/issues/1482): 2026-08-04 — R2 free-tier opt (ST/CT/UM). Class A pace ST 74%/CT 123%;
- **CT** [#1483](https://github.com/jaywedgeworth22/Congress.Trade/issues/1483): Full-product review follow-ups 2026-08-06 (unassigned; hand-made issues
- **CT** [#1486](https://github.com/jaywedgeworth22/Congress.Trade/issues/1486): 2026-08-07T07:15Z — IN PROGRESS — OR budget circuit (2–3 then hourly) +
- **CT** [#1487](https://github.com/jaywedgeworth22/Congress.Trade/issues/1487): 2026-07-19 — Conflict-resolution merge of current main into PR #620
- **CT** [#1488](https://github.com/jaywedgeworth22/Congress.Trade/issues/1488): [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger +
- **CT** [#1490](https://github.com/jaywedgeworth22/Congress.Trade/issues/1490): Uptime Alert: congress.trade health returned HTTP 502
- **CT** [#1497](https://github.com/jaywedgeworth22/Congress.Trade/issues/1497): 2026-08-07 — COMPLETED — Capitalize Congress/Congressional in product
- **CT** [#1498](https://github.com/jaywedgeworth22/Congress.Trade/issues/1498): 2026-08-07T07:30Z — IN PROGRESS — App Store publish + scorecard hotfix
- **CT** [#1499](https://github.com/jaywedgeworth22/Congress.Trade/issues/1499): 2026-08-07T07:30Z — COMPLETED/DEPLOYED — OR budget circuit + per-doc
- **CT** [#1506](https://github.com/jaywedgeworth22/Congress.Trade/issues/1506): 2026-08-07T15:19Z — IN PROGRESS — Logo.dev prod wire: land PR #1505
- **CT** [#1508](https://github.com/jaywedgeworth22/Congress.Trade/issues/1508): 2026-08-07T15:32Z — COMPLETED/DEPLOYED — Logo.dev prod wire (#1505)
- **CT** [#1510](https://github.com/jaywedgeworth22/Congress.Trade/issues/1510): 2026-08-07T15:36Z — COMPLETED — Landed iOS PRs #1500/#1501/#1502/#1504;
- **CT** [#1512](https://github.com/jaywedgeworth22/Congress.Trade/issues/1512): 2026-08-07T16:04Z — IN PROGRESS — Web light+dark brand lockup from owner
- **CT** [#1514](https://github.com/jaywedgeworth22/Congress.Trade/issues/1514): 2026-08-07T16:09Z — IN PROGRESS — Agreement cascade: soft free-text must
- **CT** [#1515](https://github.com/jaywedgeworth22/Congress.Trade/issues/1515): 2026-08-07T16:07Z — COMPLETED/DEPLOYED — Web light+dark brand lockups
- **ST** [#2582](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2582): [2026-08-07] Fix paper vs-SPY ~+50% deposit+invest sparse snaps — IN
- **UM** [#1037](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1037): [2026-08-07] iOS: Providers tap reliability, backup status restore
- **UM** [#1040](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1040): [2026-08-07] iOS: Providers tap reliability, backup status restore
- **UM** [#1043](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1043): [2026-08-07] iOS no-budget card + Title Case copy (ST e4e229e0 parity)
- **UM** [#1046](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1046): [2026-08-07] iOS no-budget card + Title Case + FLEET-UI-COPY canon
- **UM** [#1048](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1048): [2026-08-07] Local iOS ↔ web parity wave 1 — IN PROGRESS. Overview
- **UM** [#1050](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1050): [2026-08-07] Local catalog connect wave 2 — IN PROGRESS. ChatGPT row
- **UM** [#1052](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1052): [2026-08-07] Litestream primary → Backblaze B2 (leave R2 historic) — IN
- **UM** [#1054](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1054): Hetzner deploy observer + Coolify SOURCECOMMIT revision (2026-08-07)
- **UM** [#1056](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1056): [Uptime] Usage Monitor production is stale vs main

### Effort board

- **UM** `Grok` [2026-08-07] iOS no-budget card + Title Case + FLEET-UI-COPY canon — MERGED #1042 + #1044. No $ when unbudgeted; Title Case headings/buttons; sentence values. Canon: docs/FLEET-UI-COPY.md
- **UM** `Grok` [2026-08-07] iOS: Providers tap reliability, backup status restore, projects multi-app, timeframe wire, split EOM projections — MERGED PR #1036. Providers Button+path taps; Backup Lagging (not app Down); chart range → usage-events; EOM split usage+fixed+renewals; seeded ST+UM projects live
- **UM** `Grok` Hetzner deploy observer + Coolify SOURCE_COMMIT revision (2026-08-07) — IN PR. Pin PRODUCTION_ORIGIN_IPV4=167.233.254.55; drop backup.ok gate on observer; identity reads SOURCE_COMMIT. PR queue #1041/#1035/#1021 already merged
- **UM** `Grok` [2026-08-07] Local catalog connect wave 2 — IN PROGRESS. ChatGPT row, connection abilities UX, rename seed, ensure-all providers persist, flesh catalog. Branch `grok/local-catalog-connect-wave2`
- **UM** `Grok` [2026-08-07] Litestream primary → Backblaze B2 (leave R2 historic) — IN PROGRESS. Bucket jays-usage-monitor-eu; preflight accepts B2; R2 kill does not stop B2. Branch `grok/litestream-b2-primary`
- **UM** `Grok` [2026-08-07] Local iOS ↔ web parity wave 1 — IN PROGRESS. Overview hero/stats/EOM split, providers search/filter/sort, projects rollup + subs money surface. Branch `grok/local-web-parity-wave1`
- **UM** `Grok` [2026-08-07] Backblaze B2 provider web + iOS Local — PR #1033 (auto-merge). Builtin adapter + Local poll; branch `grok/backblaze-usage-monitor`

## 2026-08-06

*32 PRs merged · 58 issues opened · 22 issues closed · 4 effort rows*

### Merged PRs

- **CT** `Grok` [#1430](https://github.com/jaywedgeworth22/Congress.Trade/pull/1430): fix(latency)+feat(ui): honest FMP merge, QQ timing, shared filter chrome _(by jaywedgeworth22)_
- **CT** `Grok` [#1433](https://github.com/jaywedgeworth22/Congress.Trade/pull/1433): fix(latency): rotate FMP paths/keys — one avenue per cycle _(by jaywedgeworth22)_
- **CT** `Grok` [#1436](https://github.com/jaywedgeworth22/Congress.Trade/pull/1436): docs(effort): closeout FMP multi-avenue rotate #1433 _(by jaywedgeworth22)_
- **CT** `Grok` [#1438](https://github.com/jaywedgeworth22/Congress.Trade/pull/1438): feat(latency): yield-weighted cadence + per-source daily budgets _(by jaywedgeworth22)_
- **CT** `Grok` [#1439](https://github.com/jaywedgeworth22/Congress.Trade/pull/1439): docs(effort): closeout latency yield-budget #1438 _(by jaywedgeworth22)_
- **CT** `Grok` [#1442](https://github.com/jaywedgeworth22/Congress.Trade/pull/1442): fix(latency): ST RAPIDAPI_KEY + FMP fleet capacity _(by jaywedgeworth22)_
- **CT** `Grok` [#1444](https://github.com/jaywedgeworth22/Congress.Trade/pull/1444): docs(latency): week-focus plan + performance tracker _(by jaywedgeworth22)_
- **CT** [#1446](https://github.com/jaywedgeworth22/Congress.Trade/pull/1446): fix(ios): APNs device registration (register_device) _(by jaywedgeworth22)_
- **CT** [#1447](https://github.com/jaywedgeworth22/Congress.Trade/pull/1447): fix(ios): APNs device registration (register_device) [CI re-fire] _(by jaywedgeworth22)_
- **CT** [#1448](https://github.com/jaywedgeworth22/Congress.Trade/pull/1448): docs(effort): closeout APNs device registration PR #1446 _(by jaywedgeworth22)_
- **ST** [#2541](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2541): feat(rag): section-aware extractive highlights v2 (no gen LLM) _(by jaywedgeworth22)_
- **ST** [#2542](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2542): feat(health): auto re-probe STOPPED API connection lanes (3–6h) _(by jaywedgeworth22)_
- **ST** [#2543](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2543): feat(settings): per-user source knobs + full plan-tier ladders _(by jaywedgeworth22)_
- **ST** [#2544](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2544): fix(data): re-verify plan-tier quotas from live vendor docs _(by jaywedgeworth22)_
- **ST** `Claude` [#2564](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2564): docs: full-product review 2026-08-06 — findings, deploy-freeze RCA/repair, board+STATUS corrections _(by jaywedgeworth22)_
- **ST** [#2565](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2565): fix(ios): clearer 522 login errors + ASPresentationAnchor for iOS 26 _(by jaywedgeworth22)_
- **ST** [#2572](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2572): docs: Hetzner fleet cutover + backups/health (2026-08-07) _(by jaywedgeworth22)_
- **ST** [#2573](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2573): fix(r2): subject Pushover logo + sent-from + staggered peer checks _(by jaywedgeworth22)_
- **ST** [#2574](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2574): feat(ios): brand login like website candlestick wordmark _(by jaywedgeworth22)_
- **ST** [#2579](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2579): feat(rotation): representation-weighted "__rotate__" pick (2x underrepresented) _(by jaywedgeworth22)_
- **UM** [#1017](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1017): feat(local): realistic EOM projections, poll adapters, import, widget _(by jaywedgeworth22)_
- **UM** [#1018](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1018): refactor(deploy): rename compose project oracle → usage-monitor _(by jaywedgeworth22)_
- **UM** [#1020](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1020): feat(ux): timeframe redesign + professional polish (web + iOS) _(by jaywedgeworth22)_
- **UM** [#1022](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1022): fix(r2): tip-prune soft-cap + 6h retention (free-tier refill) _(by jaywedgeworth22)_
- **UM** [#1023](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1023): docs(effort): close out R2 tip-prune #1022 _(by jaywedgeworth22)_
- **UM** [#1024](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1024): fix(ios): restore UsageMonitor + LocalUsageMonitor simulator builds _(by jaywedgeworth22)_
- **UM** [#1025](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1025): docs(effort): close out iOS build fix #1024 _(by jaywedgeworth22)_
- **UM** [#1030](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1030): fix(r2): sent-from footer + subject tokens + digest hour 8 _(by jaywedgeworth22)_
- **UM** [#1032](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1032): fix(r2): sent-from footer only for non-self subject logos _(by jaywedgeworth22)_
- **UM** [#1033](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1033): feat(providers): Backblaze B2 storage inventory + billing estimate (web + iOS Local) _(by jaywedgeworth22)_
- **fleet** [#12](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/12): docs: prior messages stay in scope (all agents) _(by jaywedgeworth22)_
- **fleet** [#14](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/14): fix(site): standardize digest legend chips + agent-tag logos _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1191](https://github.com/jaywedgeworth22/Congress.Trade/issues/1191): Uptime Alert: congress.trade health returned HTTP 502
- **CT** [#1431](https://github.com/jaywedgeworth22/Congress.Trade/issues/1431): 2026-08-06T05:18Z — IN PROGRESS — Latency honesty: FMP merge + QQ
- **CT** [#1434](https://github.com/jaywedgeworth22/Congress.Trade/issues/1434): 2026-08-06 — IN PROGRESS — FMP multi-avenue rotate (one path+key per
- **CT** [#1437](https://github.com/jaywedgeworth22/Congress.Trade/issues/1437): 2026-08-06 — COMPLETED — FMP multi-avenue rotate — COMPLETED/DEPLOYED
- **CT** [#1440](https://github.com/jaywedgeworth22/Congress.Trade/issues/1440): 2026-08-06 — IN PROGRESS — Latency probe yield bands + per-source daily
- **CT** [#1441](https://github.com/jaywedgeworth22/Congress.Trade/issues/1441): 2026-08-06 — COMPLETED/DEPLOYED 2026-08-06T06:07Z — Latency probe yield
- **CT** [#1443](https://github.com/jaywedgeworth22/Congress.Trade/issues/1443): 2026-08-06T12:34Z — IN PROGRESS — LATENCY FOCUS: RapidAPI from ST
- **ST** [#2464](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2464): 2026-08-05 — IN PROGRESS — Open PR #2443: fix(quotes): Tradier sandbox
- **ST** [#2465](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2465): 2026-08-05 — IN PROGRESS — Open PR #2445: fix(ios): Apple Sign-In width
- **ST** [#2466](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2466): 2026-08-05 — IN PROGRESS — Open PR #2459: fix: prompt fencing, headline
- **ST** [#2501](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2501): 2026-08-05 — IN PROGRESS — P0 security residual (#1159): decryptValue
- **ST** [#2512](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2512): 2026-08-05 — IN PROGRESS — Open PR #2445: iOS Sign-In width cap + SSE
- **ST** [#2513](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2513): 2026-08-05 — IN PROGRESS — Open PR #2443: Tradier sandbox venue-aligned
- **ST** [#2514](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2514): 2026-08-05 — IN PROGRESS — Residual issues batch (B4 Settings TOC full
- **ST** [#2534](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2534): Data sources overhaul (matrix, FMP OFF, soft health
- **ST** [#2535](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2535): Non-FMP data sources STOPPED fix (soft limits + Nasdaq
- **ST** [#2537](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2537): 2026-08-05 — IN PROGRESS — Fix inflated account % return (synthetic
- **ST** [#2539](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2539): 2026-08-05 — IN PROGRESS — Multi-period TWR: split at each
- **UM** [#1026](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1026): Fix iOS Xcode build: ISO8601 public + Section title/footer +
- **UM** [#1027](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1027): R2 free-tier refill: tip-prune + 6h retention + litestream auto-resume
- **UM** [#1028](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1028): Fix iOS Xcode build: ISO8601 public + Section title/footer +
- **fleet** [#13](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/13): fix(site): standardize digest legend + agent tag → logo stripping

### Issues opened

- **CT** [#1429](https://github.com/jaywedgeworth22/Congress.Trade/issues/1429): Web+iOS filter parity, brand header, latency FMP, delivery delete, keyboard UX
- **CT** [#1431](https://github.com/jaywedgeworth22/Congress.Trade/issues/1431): 2026-08-06T05:18Z — IN PROGRESS — Latency honesty: FMP merge + QQ
- **CT** [#1432](https://github.com/jaywedgeworth22/Congress.Trade/issues/1432): 2026-08-06T05:10Z — IN PROGRESS — Web+iOS filter parity, brand header
- **CT** [#1434](https://github.com/jaywedgeworth22/Congress.Trade/issues/1434): 2026-08-06 — IN PROGRESS — FMP multi-avenue rotate (one path+key per
- **CT** [#1435](https://github.com/jaywedgeworth22/Congress.Trade/issues/1435): 2026-08-06T05:18Z — COMPLETED — Latency honesty: FMP merge + QQ
- **CT** [#1437](https://github.com/jaywedgeworth22/Congress.Trade/issues/1437): 2026-08-06 — COMPLETED — FMP multi-avenue rotate — COMPLETED/DEPLOYED
- **CT** [#1440](https://github.com/jaywedgeworth22/Congress.Trade/issues/1440): 2026-08-06 — IN PROGRESS — Latency probe yield bands + per-source daily
- **CT** [#1441](https://github.com/jaywedgeworth22/Congress.Trade/issues/1441): 2026-08-06 — COMPLETED/DEPLOYED 2026-08-06T06:07Z — Latency probe yield
- **CT** [#1443](https://github.com/jaywedgeworth22/Congress.Trade/issues/1443): 2026-08-06T12:34Z — IN PROGRESS — LATENCY FOCUS: RapidAPI from ST
- **CT** [#1445](https://github.com/jaywedgeworth22/Congress.Trade/issues/1445): 2026-08-06T14:19Z — IN PROGRESS — Latency week focus: track
- **CT** [#1449](https://github.com/jaywedgeworth22/Congress.Trade/issues/1449): 2026-08-06T18:35Z — IN PROGRESS — iOS APNs register: fix delivery must
- **CT** [#1452](https://github.com/jaywedgeworth22/Congress.Trade/issues/1452): Data: duplicate member identities split trade history (e.g. 'Michael T. McCaul' vs 'Michael McCaul')
- **CT** [#1453](https://github.com/jaywedgeworth22/Congress.Trade/issues/1453): Feed: default view shows primary+historic duplicate rows; asset display names unnormalized
- **CT** [#1454](https://github.com/jaywedgeworth22/Congress.Trade/issues/1454): Perf: /api/members takes ~6s — People tab stuck on 'Loading directory…'
- **CT** [#1455](https://github.com/jaywedgeworth22/Congress.Trade/issues/1455): Owner decision: Filing Latency Comparison widget placement + copy (currently self-reports 8% win vs Quiver on every public tab)
- **CT** [#1456](https://github.com/jaywedgeworth22/Congress.Trade/issues/1456): Mobile: brand logo hidden behind 3-button theme toggle at 375px; disclaimer auto-expanded eats first screen
- **CT** [#1457](https://github.com/jaywedgeworth22/Congress.Trade/issues/1457): Polish: console/network noise on every anonymous page load (guaranteed 404s/401 + CSP-blocked analytics beacon)
- **CT** [#1458](https://github.com/jaywedgeworth22/Congress.Trade/issues/1458): UX: ?view deep-link ids don't match visible tab names; unknown values silently rewritten
- **CT** [#1459](https://github.com/jaywedgeworth22/Congress.Trade/issues/1459): Adopt 'Capitol Ledger' mock elements from congresstrade.grok.me (style option + structural wins)
- **CT** [#1460](https://github.com/jaywedgeworth22/Congress.Trade/issues/1460): Expansion: committee data, backtest horizon labels, filer-owner display, member photos in directory
- **CT** [#1462](https://github.com/jaywedgeworth22/Congress.Trade/issues/1462): Cross-app: vendored congress-trading-shared is v2.0.0; shared repo is at v2.5.1 — audit drift
- **ST** [#2545](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2545): P0: Deploy pipeline froze all day 2026-08-06 — SSH exec stream dies mid-build under shared-box load; add freshness alert + isolate CT OCR load
- **ST** [#2546](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2546): P0 (owner decision): prod DB litestream→R2 replication PAUSED since Aug 4 — no continuous backup; R2 free-tier pressure fleet-wide
- **ST** [#2547](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2547): P1: shared-package lockfile drift — manifest pins congress-trading-shared v2.5.1, lockfile ships 2.5.0 (filingDate member-skill dependency not deployed)
- **ST** [#2548](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2548): P1: open-lots ledger contradicts live positions (T long 91.119 vs actual short −1.881; AXP lot with no position) — tax/wash-sale numbers built on wrong lots
- **ST** [#2549](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2549): P1: two short positions sit unmanaged (Protection '—') because shortSellingEnabled is off with shorts on the book — needs an attention banner
- **ST** [#2550](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2550): P1 coordination: congress.trade + usage-monitor lanes degraded from prod's view (11s CT response, 6.9s UM latency, SSE flaps) — widen backoff, verify consumers tolerate it
- **ST** [#2551](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2551): P1: PWA proposal cards need the console's collapsed-receipt treatment (raw [Sizing]/[Risk] wall on mobile)
- **ST** [#2552](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2552): P2: Red Team critic failures are under-surfaced — show cause on the chip and track failure rate (4 of 5 pending proposals had no working critic)
- **ST** [#2553](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2553): P2: Activity feed signal-to-noise — duplicate BUY/TRADE rows per action, SEC-ingest flood bypasses the System group, per-minute no-op embed audits
- **ST** [#2554](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2554): P2: cross-surface run-state vocabulary — PWA says 'Running' while console says 'Paused · market closed' for the same account
- **ST** [#2555](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2555): P2: alert center fatigue — per-condition mute/snooze + single provider-outage rollup row
- **ST** [#2556](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2556): P1: Home 'All Decisions' link 404s — /console/decisions has no index page (verified live)
- **ST** [#2557](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2557): P1: inflated account return persists AFTER #2536 — phantom $36.5k inferred withdrawal + SPY benchmark 0.00% (live repro on build containing the fix)
- **ST** [#2558](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2558): P1: settings-search catalog (searchSettings/SETTINGS_FIELDS/glossary) is fully built but wired to no UI — wire into command palette; also indexes a phantom field
- **ST** [#2559](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2559): P2: mobile stream/session state bugs — iOS 'Live updates' indicator stays false on healthy idle stream; PWA Market metric always renders 'Closed' (marketSession type drift)
- **ST** [#2560](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2560): P1: iOS release-readiness batch — Close-only/Wind-down controls missing, no APNs despite alert copy promising it, ITSAppUsesNonExemptEncryption/privacy manifest absent, no web-console deep links
- **ST** [#2561](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2561): P1/P2: console accessibility batch — light-theme chip contrast fails AA, Sheet Escape closes stacked surfaces, tooltip/columns-popover/meter gaps
- **ST** [#2562](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2562): P2/P3: stale-copy + dead-code polish batch — FMP mentions in live tooltips/captions, paper-mode vocabulary, Coach/Assistant label, dead event, dark-mode candle colors, misc iOS
- **ST** [#2563](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2563): P3: curl-only server capabilities with no UI entry — tuning-dry-run, learning-ledger, backtest-ic, audit query
- **ST** [#2566](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2566): 2026-08-05 — COMPLETED (merged #2538 2e55e075 + DEPLOYED 2026-08-06
- **ST** [#2567](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2567): 2026-08-05 — IN PROGRESS — Fix inflated account % return (synthetic
- **ST** [#2568](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2568): Data sources overhaul (matrix, FMP OFF, soft health
- **ST** [#2569](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2569): Non-FMP data sources STOPPED fix (soft limits + Nasdaq
- **ST** [#2570](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2570): 2026-08-05 — COMPLETED + DEPLOYED via PR #2490 14f3cace 2026-08-05 (was
- **ST** [#2571](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2571): 2026-08-05 — COMPLETED + DEPLOYED via PR #2498 d614d708 2026-08-05 (was
- **ST** [#2575](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2575): [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger +
- **ST** [#2576](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2576): P2: robinhood-broker MCP calls fail with 'unexpected additional properties [symbol, symbols]' — schema drift with the Robinhood connector (x3 on Aug 6)
- **ST** [#2577](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2577): P2: five Green-Team runs failed Aug 6 with OpenRouter 'Empty response' across models — failover didn't save the run; correlate with credits-low
- **ST** [#2578](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2578): P1: Tradier rejects bracket orders with sub-penny limit prices (HTTP 400 'must use up to 2 decimal places') — NWG order lost to formatting
- **UM** [#1019](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1019): Rename compose project oracle → usage-monitor (clear container names)
- **UM** [#1026](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1026): Fix iOS Xcode build: ISO8601 public + Section title/footer +
- **UM** [#1027](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1027): R2 free-tier refill: tip-prune + 6h retention + litestream auto-resume
- **UM** [#1028](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1028): Fix iOS Xcode build: ISO8601 public + Section title/footer +
- **UM** [#1029](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1029): [Uptime] Usage Monitor Oracle origin readiness failure
- **UM** [#1031](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1031): [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger +
- **UM** [#1034](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1034): [2026-08-07] Backblaze B2 provider web + iOS Local — PR #1033
- **fleet** [#13](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/13): fix(site): standardize digest legend + agent tag → logo stripping

### Effort board

- **UM** `Grok` Fix iOS Xcode build: ISO8601 public + Section title/footer + LockScreenView public (2026-08-06) — MERGED PR #1024. LocalExport needed public LocalStore.ISO8601; ProviderManagementInventory invalid Section("title"){ } footer; LocalAppLockGate needed public LockScreenView; LocalRootView drop @MainActor default AppSettings(). Both schemes BUILD SUCCEEDED. Squash `cac46b64`
- **UM** `Grok` R2 free-tier refill: tip-prune + 6h retention + litestream auto-resume (2026-08-06) — MERGED #1022 / HOST OPS DONE. Live prune 8.92→0.40 GiB; kill cleared; litestream sync=2h retention=6h live; soft tip-prune@50% + watcher resume + js-yaml 4.3.1 override
- **UM** `Grok` [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger + own backup line — IN PROGRESS / landing. Subject free-tier → that app's PUSHOVER_ token; footer `(sent from APP)`; peer checks UTC phase; digests UM≥08/ST=14/CT≥20; Hetzner 24h floor. Branch `grok/r2-pushover-subject-identity`
- **UM** `Grok` Rename compose project oracle → usage-monitor (clear container names) (2026-08-06) — IN PR. Containers usage-monitor-app-1 / usage-monitor-caddy-1; retire legacy oracle-app-; deploy cutover handles mid-rename

## 2026-08-05

*99 PRs merged · 121 issues opened · 331 issues closed · 22 effort rows*

### Merged PRs

- **CT** [#1346](https://github.com/jaywedgeworth22/Congress.Trade/pull/1346): fix(ux): calendar position after P chip, shared Trends/Trades filters, BrandTitle header, compact disclaimer, and human-readable volume period dates _(by jaywedgeworth22)_
- **CT** [#1350](https://github.com/jaywedgeworth22/Congress.Trade/pull/1350): UI Fixes and Latency Correction _(by jaywedgeworth22)_
- **CT** [#1367](https://github.com/jaywedgeworth22/Congress.Trade/pull/1367): feat(ui): default theme preference to system _(by jaywedgeworth22)_
- **CT** [#1369](https://github.com/jaywedgeworth22/Congress.Trade/pull/1369): docs: close out open-PR resolve effort _(by jaywedgeworth22)_
- **CT** [#1371](https://github.com/jaywedgeworth22/Congress.Trade/pull/1371): fix(ui): update title and icon to proper eagle lockup, Congress.Trade casing _(by jaywedgeworth22)_
- **CT** [#1372](https://github.com/jaywedgeworth22/Congress.Trade/pull/1372): fix(ui): use correct eagle bag icon and nuke old eagle assets _(by jaywedgeworth22)_
- **CT** [#1373](https://github.com/jaywedgeworth22/Congress.Trade/pull/1373): Lower delivery subscription quota to 2 per user _(by jaywedgeworth22)_
- **CT** [#1374](https://github.com/jaywedgeworth22/Congress.Trade/pull/1374): fix(latency): live-only races; max match all 3 providers _(by jaywedgeworth22)_
- **CT** [#1376](https://github.com/jaywedgeworth22/Congress.Trade/pull/1376): docs: effort-board hygiene (Issues alignment) _(by jaywedgeworth22)_
- **CT** [#1400](https://github.com/jaywedgeworth22/Congress.Trade/pull/1400): feat: gate pdf viewing behind premium entitlement _(by jaywedgeworth22)_
- **CT** [#1401](https://github.com/jaywedgeworth22/Congress.Trade/pull/1401): feat: Add PDF access to premium features copy _(by jaywedgeworth22)_
- **CT** [#1402](https://github.com/jaywedgeworth22/Congress.Trade/pull/1402): chore: housekeeping sweep + filers full_name index _(by jaywedgeworth22)_
- **CT** [#1404](https://github.com/jaywedgeworth22/Congress.Trade/pull/1404): fix(fmp): free keys latency-monitoring only _(by jaywedgeworth22)_
- **CT** [#1405](https://github.com/jaywedgeworth22/Congress.Trade/pull/1405): fix(ui): apply proper eagle horizontal lockup and restore Congress.Trade casing _(by jaywedgeworth22)_
- **CT** [#1406](https://github.com/jaywedgeworth22/Congress.Trade/pull/1406): fix(ui): extract dashboard base64 assets to app/public (#1040) _(by jaywedgeworth22)_
- **CT** [#1407](https://github.com/jaywedgeworth22/Congress.Trade/pull/1407): feat(delivery): web pause/resume/delete + filter editing (#1039) _(by jaywedgeworth22)_
- **CT** `Grok` [#1408](https://github.com/jaywedgeworth22/Congress.Trade/pull/1408): fix(ingest): accept filing.local_wait_check in durable queue _(by jaywedgeworth22)_
- **CT** [#1409](https://github.com/jaywedgeworth22/Congress.Trade/pull/1409): fix(ios): use proper eagle lockup for app icon and capitalize Congress.Trade in copy _(by jaywedgeworth22)_
- **CT** [#1410](https://github.com/jaywedgeworth22/Congress.Trade/pull/1410): docs: close shipped planned effort items _(by jaywedgeworth22)_
- **CT** [#1415](https://github.com/jaywedgeworth22/Congress.Trade/pull/1415): fix(brand): site-heading eagle+bag app icon (no letters/seal) _(by jaywedgeworth22)_
- **CT** [#1416](https://github.com/jaywedgeworth22/Congress.Trade/pull/1416): docs(r2): Class A free-tier emergency pause of litestream-congress _(by jaywedgeworth22)_
- **CT** `Grok` [#1417](https://github.com/jaywedgeworth22/Congress.Trade/pull/1417): feat(latency): FMP family OFF by default + dual-path race _(by jaywedgeworth22)_
- **CT** [#1419](https://github.com/jaywedgeworth22/Congress.Trade/pull/1419): docs(backup): fleet steady-state policy (CT 15m continuous) _(by jaywedgeworth22)_
- **CT** [#1420](https://github.com/jaywedgeworth22/Congress.Trade/pull/1420): fix(latency): FMP probes default ON for Congress.Trade _(by jaywedgeworth22)_
- **CT** [#1421](https://github.com/jaywedgeworth22/Congress.Trade/pull/1421): fix(ios): SettingsView build break + FilterChip + display name _(by jaywedgeworth22)_
- **CT** [#1422](https://github.com/jaywedgeworth22/Congress.Trade/pull/1422): fix(brand): capitalize Congress.Trade in Pushover alerts and copy _(by jaywedgeworth22)_
- **CT** [#1423](https://github.com/jaywedgeworth22/Congress.Trade/pull/1423): fix(ui): transparent eagle+bag favicon for browser tab _(by jaywedgeworth22)_
- **CT** [#1424](https://github.com/jaywedgeworth22/Congress.Trade/pull/1424): fix(ui/ios): sharper eagle favicon + Congress.Trade product name _(by jaywedgeworth22)_
- **CT** [#1425](https://github.com/jaywedgeworth22/Congress.Trade/pull/1425): fix(scan-cpu-worker): pin deps so Coolify deploys succeed _(by jaywedgeworth22)_
- **CT** [#1426](https://github.com/jaywedgeworth22/Congress.Trade/pull/1426): fix(ui): bump favicon cache-buster to v=9 _(by jaywedgeworth22)_
- **CT** [#1427](https://github.com/jaywedgeworth22/Congress.Trade/pull/1427): docs: second Congress.Trade CI runner (oracle-congress-ci-2) _(by jaywedgeworth22)_
- **ST** [#2443](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2443): fix(quotes): Tradier sandbox uses delayed venue prices as authoritative _(by jaywedgeworth22)_
- **ST** [#2445](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2445): fix(ios): Apple Sign-In width cap + SSE events request defaults _(by jaywedgeworth22)_
- **ST** [#2459](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2459): fix: prompt fencing, headline first-seen, approval 4xx classification _(by jaywedgeworth22)_
- **ST** `Grok` [#2460](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2460): docs: mark auto-pause #2444 completed + deployed _(by jaywedgeworth22)_
- **ST** [#2461](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2461): docs: effort-board hygiene (Issues alignment) _(by jaywedgeworth22)_
- **ST** [#2488](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2488): fix(console): reopenable framework proposals + Accept vs Applied legend _(by jaywedgeworth22)_
- **ST** [#2489](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2489): fix(exits): activity-audit P2.7 cancel settle multi-poll + P2.8 failing alert _(by jaywedgeworth22)_
- **ST** [#2490](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2490): fix(ux,share): B4 settings TOC + activity-audit residuals + board hygiene _(by jaywedgeworth22)_
- **ST** `Grok` [#2491](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2491): docs: mark — 2026-08-05 PR/issue batch completed on effort board _(by jaywedgeworth22)_
- **ST** [#2492](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2492): docs: mark activity-audit P2.6–P2.9 board rows completed _(by jaywedgeworth22)_
- **ST** [#2497](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2497): fix(test): update reasoning capability test assertions for o1 model family _(by jaywedgeworth22)_
- **ST** [#2498](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2498): fix(security): audit hash chain (v67) + decryptValue reject plaintext (P0) _(by jaywedgeworth22)_
- **ST** [#2503](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2503): feat(market-data): durable shared symbol_field_latest (per-field timestamps) _(by jaywedgeworth22)_
- **ST** [#2504](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2504): fix: activity-audit leftovers P3 residuals + board hygiene _(by jaywedgeworth22)_
- **ST** [#2505](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2505): Fix data provider cascade and shared library types _(by jaywedgeworth22)_
- **ST** [#2510](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2510): fix(scheduler): never schedule test-broker autonomy + owner RAG rulings _(by jaywedgeworth22)_
- **ST** [#2526](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2526): fix(health): critical deps OK when user-keyed lane is healthy _(by jaywedgeworth22)_
- **ST** [#2527](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2527): fix(health): do not 503 critical deps when a user-keyed lane is healthy _(by jaywedgeworth22)_
- **ST** [#2528](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2528): fix(ui): vertically center collapsed "You're set" card header _(by jaywedgeworth22)_
- **ST** [#2529](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2529): fix(r2): free-tier survival — Socratic Trade label + 15m litestream + kill banner _(by jaywedgeworth22)_
- **ST** [#2530](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2530): docs(backup): fleet steady-state policy (ST 15m continuous) _(by jaywedgeworth22)_
- **ST** [#2531](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2531): feat(data): sources overhaul — matrix, FMP OFF, soft health, tiers, provenance, ROIC transcripts _(by jaywedgeworth22)_
- **ST** [#2532](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2532): feat(admin): data catalog, RAG completeness %, field→sources explorer _(by jaywedgeworth22)_
- **ST** [#2533](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2533): feat(rag): multi-source SEC + earnings transcripts with trade highlights _(by jaywedgeworth22)_
- **ST** [#2536](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2536): fix(perf): stop inflated account % return on paper/sandbox accounts _(by jaywedgeworth22)_
- **ST** [#2538](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2538): fix(perf): multi-period TWR — capital regimes + chained SPY _(by jaywedgeworth22)_
- **ST** [#2540](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2540): feat(data): provider-neutral Settings + ROIC tiers and working transcripts _(by jaywedgeworth22)_
- **UM** [#949](https://github.com/jaywedgeworth22/Usage-Monitor/pull/949): feat(overview): Global Budget, projected cost breakdown, quiet stale, ROIC _(by jaywedgeworth22)_
- **UM** [#950](https://github.com/jaywedgeworth22/Usage-Monitor/pull/950): docs: effort-board hygiene (Issues alignment) _(by jaywedgeworth22)_
- **UM** [#951](https://github.com/jaywedgeworth22/Usage-Monitor/pull/951): feat(ios-widget): choose overall or project budget _(by jaywedgeworth22)_
- **UM** [#973](https://github.com/jaywedgeworth22/Usage-Monitor/pull/973): fix: refresh when due; Manual not Stale for never-pollable _(by jaywedgeworth22)_
- **UM** [#975](https://github.com/jaywedgeworth22/Usage-Monitor/pull/975): feat(ops): R2 fleet free-tier card + calm backup readiness _(by jaywedgeworth22)_
- **UM** [#976](https://github.com/jaywedgeworth22/Usage-Monitor/pull/976): fix(ops): 3h replica freshness budget for 1h Litestream sync _(by jaywedgeworth22)_
- **UM** [#978](https://github.com/jaywedgeworth22/Usage-Monitor/pull/978): docs(effort): close out completed board rows after #976 _(by jaywedgeworth22)_
- **UM** [#982](https://github.com/jaywedgeworth22/Usage-Monitor/pull/982): fix(ios): distinct UM Local identity so both apps coexist _(by jaywedgeworth22)_
- **UM** [#983](https://github.com/jaywedgeworth22/Usage-Monitor/pull/983): feat(ios): teal Local icon + short home name so both apps coexist _(by jaywedgeworth22)_
- **UM** [#984](https://github.com/jaywedgeworth22/Usage-Monitor/pull/984): feat: R2 fleet card pushover-parity + iOS inline tab titles _(by jaywedgeworth22)_
- **UM** [#985](https://github.com/jaywedgeworth22/Usage-Monitor/pull/985): fix(ops): remove brittle wait_for_backup_advancement _(by jaywedgeworth22)_
- **UM** [#986](https://github.com/jaywedgeworth22/Usage-Monitor/pull/986): test: remove wait_for_backup_advancement from oracle deploy checks _(by jaywedgeworth22)_
- **UM** [#987](https://github.com/jaywedgeworth22/Usage-Monitor/pull/987): refactor(ios): LocalUsageMonitor name + bundle ID _(by jaywedgeworth22)_
- **UM** [#988](https://github.com/jaywedgeworth22/Usage-Monitor/pull/988): docs(ios): Local free App Store ID services.jays.local.usage.monitor _(by jaywedgeworth22)_
- **UM** [#989](https://github.com/jaywedgeworth22/Usage-Monitor/pull/989): fix(ops): replica probe R2 free-tier kill reason + install _(by jaywedgeworth22)_
- **UM** [#991](https://github.com/jaywedgeworth22/Usage-Monitor/pull/991): fix(deploy): allow main tip to advance mid exact-SHA deploy _(by jaywedgeworth22)_
- **UM** [#993](https://github.com/jaywedgeworth22/Usage-Monitor/pull/993): feat(ios): Local Usage Monitor fleet provider catalog _(by jaywedgeworth22)_
- **UM** [#994](https://github.com/jaywedgeworth22/Usage-Monitor/pull/994): fix(deploy): finish exact-SHA cutover even if main tip advances _(by jaywedgeworth22)_
- **UM** [#995](https://github.com/jaywedgeworth22/Usage-Monitor/pull/995): fix(deploy): 30m SQLite backup timeout for large prod DB _(by jaywedgeworth22)_
- **UM** [#996](https://github.com/jaywedgeworth22/Usage-Monitor/pull/996): docs: billing API coverage research (LLMs + partial sources) _(by jaywedgeworth22)_
- **UM** [#998](https://github.com/jaywedgeworth22/Usage-Monitor/pull/998): feat: full historical catalog + Hetzner MTD estimate _(by jaywedgeworth22)_
- **UM** [#999](https://github.com/jaywedgeworth22/Usage-Monitor/pull/999): fix(ui): orange brand, Display nav, segmented history control _(by jaywedgeworth22)_
- **UM** [#1001](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1001): fix(deploy): continue exact-SHA when main tip advances mid-build _(by jaywedgeworth22)_
- **UM** [#1002](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1002): feat: complete Local historical catalog + Hetzner poll (Voyage/Oracle/Hetzner both apps) _(by jaywedgeworth22)_
- **UM** [#1004](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1004): docs(effort): mark orange brand + history UI #999 merged _(by jaywedgeworth22)_
- **UM** [#1007](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1007): fix(r2): Congress.Trade label + ListObjects cache (free tier) _(by jaywedgeworth22)_
- **UM** [#1008](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1008): ops(backup): steady free-tier policy — 1 local copy max _(by jaywedgeworth22)_
- **UM** [#1009](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1009): fix(ios): clean orange ring + Local full-width LOCAL stripe icons _(by jaywedgeworth22)_
- **UM** [#1010](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1010): fix(ios): stop empty SF Symbol log spam from TimeframePicker _(by jaywedgeworth22)_
- **UM** [#1012](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1012): fix(ios): seed truth (no fake Vercel/CF/Robinhood fees) + swipe-delete confirm _(by jaywedgeworth22)_
- **UM** [#1013](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1013): fix(ios): hide broken Fetch, edit/delete, Local spend honesty _(by jaywedgeworth22)_
- **UM** [#1014](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1014): feat(ios): Local parity-plus — alerts, projects, export, App Lock _(by jaywedgeworth22)_
- **UM** [#1015](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1015): docs(design): timeframe + professional polish UX panel _(by jaywedgeworth22)_
- **UM** [#1016](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1016): fix(ui): hide project-budgets system provider from Connections _(by jaywedgeworth22)_
- **fleet** [#5](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/5): docs: Apple Notes Coding + pin for owner review docs _(by jaywedgeworth22)_
- **fleet** [#6](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/6): docs: reaffirm Slack SENDER + repo + PEER|FLEET policy _(by jaywedgeworth22)_
- **fleet** [#7](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/7): docs: standard Slack header + ALWAYS read policy _(by jaywedgeworth22)_
- **fleet** [#8](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/8): docs: claim/complete board + issues + Slack every work unit _(by jaywedgeworth22)_
- **fleet** [#9](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/9): feat(site): fleet daily digest (HTML/MD/ICS) + GitHub Pages _(by jaywedgeworth22)_
- **fleet** [#10](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/10): feat(site): light theme, repo colors, agent logos _(by jaywedgeworth22)_
- **fleet** [#11](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/11): fix(site): Jay owner asset, no Owner chip on digest _(by jaywedgeworth22)_

### Issues closed

- **CT** [#155](https://github.com/jaywedgeworth22/Congress.Trade/issues/155): Sentry CI failure reporter — copy the additive sentry-ci-report.yml
- **CT** [#157](https://github.com/jaywedgeworth22/Congress.Trade/issues/157): Owner decision: should public subscription creation require login? (unassigned
- **CT** [#158](https://github.com/jaywedgeworth22/Congress.Trade/issues/158): Owner decision: should analytics routes become premium-only? (unassigned, M)
- **CT** [#170](https://github.com/jaywedgeworth22/Congress.Trade/issues/170): global coordination + fleet monitoring setup
- **CT** [#171](https://github.com/jaywedgeworth22/Congress.Trade/issues/171): Sentry CI failure reporter — IN PROGRESS 2026-07-05, implemented
- **CT** [#174](https://github.com/jaywedgeworth22/Congress.Trade/issues/174): Audit production schema drift from the three failed Deploy runs (OWNER, S)
- **CT** [#180](https://github.com/jaywedgeworth22/Congress.Trade/issues/180): De-duplicate effort-issues sync when a row's first line changes
- **CT** [#197](https://github.com/jaywedgeworth22/Congress.Trade/issues/197): Cloud Slack + effort-log readiness across all four apps
- **CT** [#205](https://github.com/jaywedgeworth22/Congress.Trade/issues/205): Architecture & Shared Dependency — 2026-07-05. Use createCongressEvent
- **CT** [#223](https://github.com/jaywedgeworth22/Congress.Trade/issues/223): De-crash and de-challenge the Uptime Monitor workflow — COMPLETED
- **CT** [#224](https://github.com/jaywedgeworth22/Congress.Trade/issues/224): Land cursor/assigned-tasks: commit, rebase onto main, drop already-merged hunks
- **CT** [#230](https://github.com/jaywedgeworth22/Congress.Trade/issues/230): Add manual queue reprocess button to admin dashboard — COMPLETED
- **CT** [#233](https://github.com/jaywedgeworth22/Congress.Trade/issues/233): Consolidate usage telemetry clients in consumer apps - COMPLETED
- **CT** [#277](https://github.com/jaywedgeworth22/Congress.Trade/issues/277): GPT-5.6 bake-off evaluation prep + usage/cost tracking harness
- **CT** [#278](https://github.com/jaywedgeworth22/Congress.Trade/issues/278): Fix dead auto-publish gate: AGREEMENTAUTOPUBLISHMODELB was broken 2 weeks
- **CT** [#279](https://github.com/jaywedgeworth22/Congress.Trade/issues/279): FMP pacer safety + shared-budget accounting + EDGAR throttle — IN
- **CT** [#280](https://github.com/jaywedgeworth22/Congress.Trade/issues/280): Review-queue automation: model choice + multi-model consensus + escalation
- **CT** [#281](https://github.com/jaywedgeworth22/Congress.Trade/issues/281): Fix the production deploy health gate blocked by Cloudflare managed challenge
- **CT** [#282](https://github.com/jaywedgeworth22/Congress.Trade/issues/282): Adopt the docs/rollouts/ note convention in Congress.Trade AGENTS.md
- **CT** [#283](https://github.com/jaywedgeworth22/Congress.Trade/issues/283): Rescue — stash into a committed, pushed branch + PR — MERGED
- **CT** [#286](https://github.com/jaywedgeworth22/Congress.Trade/issues/286): Backend delivery + ingestion reliability hardening
- **CT** [#287](https://github.com/jaywedgeworth22/Congress.Trade/issues/287): iOS client correctness + performance hardening — INTEGRATED
- **CT** [#288](https://github.com/jaywedgeworth22/Congress.Trade/issues/288): PWA release hardening + CI coverage — INTEGRATED LOCALLY
- **CT** [#289](https://github.com/jaywedgeworth22/Congress.Trade/issues/289): Billing + platform security hardening — INTEGRATED LOCALLY +
- **CT** [#313](https://github.com/jaywedgeworth22/Congress.Trade/issues/313): Beautify iOS SwiftUI Prototype App — IN PROGRESS 2026-07-12. Refactored
- **CT** [#323](https://github.com/jaywedgeworth22/Congress.Trade/issues/323): Matched congress-trading-shared v1.5.0 consumer pin ( implementation
- **CT** [#324](https://github.com/jaywedgeworth22/Congress.Trade/issues/324): Fix Uptime Monitor compact-JSON output framing
- **CT** [#325](https://github.com/jaywedgeworth22/Congress.Trade/issues/325): Implement estvalue column in transactions table — COMPLETED 2026-07-11
- **CT** [#326](https://github.com/jaywedgeworth22/Congress.Trade/issues/326): Refactor client API routes — COMPLETED 2026-07-11. Splitting the
- **CT** [#327](https://github.com/jaywedgeworth22/Congress.Trade/issues/327): Codebase Performance & Queues — COMPLETED 2026-07-11. Fix silent DLQ
- **CT** [#328](https://github.com/jaywedgeworth22/Congress.Trade/issues/328): Improvements — COMPLETED 2026-07-11 (PR #266 merged)
- **CT** [#329](https://github.com/jaywedgeworth22/Congress.Trade/issues/329): Acquisition-vs-rename guard for ticker aliases — COMPLETED
- **CT** [#330](https://github.com/jaywedgeworth22/Congress.Trade/issues/330): Congress push/SSE contract repair — COMPLETED 2026-07-11
- **CT** [#331](https://github.com/jaywedgeworth22/Congress.Trade/issues/331): Prep the shared-pkg v1.3.0 adoption PR as a matched pair behind the owner tag
- **CT** [#333](https://github.com/jaywedgeworth22/Congress.Trade/issues/333): Merge shared ag/client-and-ticker + release v1.3.1 so app PRs can pin a tag not
- **CT** [#334](https://github.com/jaywedgeworth22/Congress.Trade/issues/334): Consolidate 's six overlapping PRs #182-#187 into one stacked/sequenced
- **CT** [#335](https://github.com/jaywedgeworth22/Congress.Trade/issues/335): Remove stray patch.py scratch script from antigravity/performance-queues (#186)
- **CT** [#342](https://github.com/jaywedgeworth22/Congress.Trade/issues/342): Audit Tier 1 Fixes (surgical unblocks) — IN PROGRESS 2026-07-12. Fixing
- **CT** [#400](https://github.com/jaywedgeworth22/Congress.Trade/issues/400): Adversarial final review of benchmark reliability repair
- **CT** [#403](https://github.com/jaywedgeworth22/Congress.Trade/issues/403): Production benchmark failure diagnosis and reliability repair ( + expert
- **CT** [#406](https://github.com/jaywedgeworth22/Congress.Trade/issues/406): Local Infisical bootstrap credential wiring — FINAL REVIEW P2S FIXED
- **CT** [#427](https://github.com/jaywedgeworth22/Congress.Trade/issues/427): Adopt immutable congress-trading-shared v1.7.1 in Congress.Trade ( + peer
- **CT** [#428](https://github.com/jaywedgeworth22/Congress.Trade/issues/428): Final Infisical bootstrap line-mapping repair ( verifier/builder, S)
- **CT** [#429](https://github.com/jaywedgeworth22/Congress.Trade/issues/429): Fresh adversarial landing review of Infisical bootstrap wiring
- **CT** [#430](https://github.com/jaywedgeworth22/Congress.Trade/issues/430): Independent security review of local Infisical bootstrap wiring
- **CT** [#431](https://github.com/jaywedgeworth22/Congress.Trade/issues/431): Usage telemetry stable-key replay hotfix ( + verifier team, M) — COMPLETED
- **CT** [#432](https://github.com/jaywedgeworth22/Congress.Trade/issues/432): Persistent chamber benchmark history, measured cost/latency, per-branch A/B/C
- **CT** [#444](https://github.com/jaywedgeworth22/Congress.Trade/issues/444): 2026-07-15 — Completed — prod one-doc all-model benchmark validation +
- **CT** [#445](https://github.com/jaywedgeworth22/Congress.Trade/issues/445): 2026-07-15 — Implementation complete locally / PR-deploy pending
- **CT** [#451](https://github.com/jaywedgeworth22/Congress.Trade/issues/451): 2026-07-15 — In Progress — Fix false-positive Shared package pin check
- **CT** [#458](https://github.com/jaywedgeworth22/Congress.Trade/issues/458): → handoff tail: shared v1.8.0 consumption — IN
- **CT** [#523](https://github.com/jaywedgeworth22/Congress.Trade/issues/523): OpenRouter Model Consolidation & Mistral OCR Integration — IN PROGRESS (PR
- **CT** [#537](https://github.com/jaywedgeworth22/Congress.Trade/issues/537): 2026-07-17 — In Progress — Incorporate the owner-directed full-app
- **CT** [#565](https://github.com/jaywedgeworth22/Congress.Trade/issues/565): 2026-07-17 — In Progress — Telemetry failsafe: circuit breaker + move
- **CT** [#574](https://github.com/jaywedgeworth22/Congress.Trade/issues/574): 2026-07-17 — In Progress (PR #555 open, not merged) — Split production
- **CT** [#578](https://github.com/jaywedgeworth22/Congress.Trade/issues/578): 2026-07-18 — In Progress / production partial — All-open-PR
- **CT** [#580](https://github.com/jaywedgeworth22/Congress.Trade/issues/580): 2026-07-18 — In progress (PR #556) — Dry-run agreement lineup provider
- **CT** [#581](https://github.com/jaywedgeworth22/Congress.Trade/issues/581): 2026-07-18 — In Progress (PR #570, auto-merge armed)
- **CT** [#582](https://github.com/jaywedgeworth22/Congress.Trade/issues/582): 2026-07-18 — Completed / merged as a685a97 / production verified
- **CT** [#583](https://github.com/jaywedgeworth22/Congress.Trade/issues/583): 2026-07-18 — COMPLETED / MERGED / PRODUCTION VERIFIED — Coolify-only
- **CT** [#586](https://github.com/jaywedgeworth22/Congress.Trade/issues/586): 2026-07-18 — In Progress (PR #571, auto-merge armed)
- **CT** [#615](https://github.com/jaywedgeworth22/Congress.Trade/issues/615): Post — activation lane (iOS, billing, backfill) — IN PROGRESS / PR
- **CT** [#624](https://github.com/jaywedgeworth22/Congress.Trade/issues/624): PR #619 review-only assist (2026-07-18 21:47 CDT)
- **CT** [#634](https://github.com/jaywedgeworth22/Congress.Trade/issues/634): 2026-07-19 — Conflict-resolution merge (PR #627) — merged current
- **CT** [#643](https://github.com/jaywedgeworth22/Congress.Trade/issues/643): Benchmark model-catalog filtering & UI tweaks (2026-07-19)
- **CT** [#644](https://github.com/jaywedgeworth22/Congress.Trade/issues/644): Merge current origin/main into
- **CT** [#645](https://github.com/jaywedgeworth22/Congress.Trade/issues/645): 2026-07-19 — Conflict-resolution merge of current main into PR #620
- **CT** [#647](https://github.com/jaywedgeworth22/Congress.Trade/issues/647): [COPILOT] All-open-PR merge readiness (#620, #625–#632;
- **CT** [#661](https://github.com/jaywedgeworth22/Congress.Trade/issues/661): 2026-07-18 — In Progress (PR #620, auto-merge armed) — Hard resource
- **CT** [#667](https://github.com/jaywedgeworth22/Congress.Trade/issues/667): 2026-07-19 — In Progress (PR #653, squash auto-merge armed)
- **CT** [#668](https://github.com/jaywedgeworth22/Congress.Trade/issues/668): Delivery/client input hardening, command lifecycle
- **CT** [#669](https://github.com/jaywedgeworth22/Congress.Trade/issues/669): Monitor-informed budget throttle: GET
- **CT** [#699](https://github.com/jaywedgeworth22/Congress.Trade/issues/699): 2026-07-19 — In Progress (PR #627, auto-merge armed) — Backlog
- **CT** [#700](https://github.com/jaywedgeworth22/Congress.Trade/issues/700): Usage-compliance Wave 2 (CT lane): OpenRouter
- **CT** [#701](https://github.com/jaywedgeworth22/Congress.Trade/issues/701): Delivery/client input hardening, command lifecycle
- **CT** [#887](https://github.com/jaywedgeworth22/Congress.Trade/issues/887): Resolve stale In Progress + terra/luna rate-card +
- **CT** [#888](https://github.com/jaywedgeworth22/Congress.Trade/issues/888): Restore Deno live ingestion and data-completeness path
- **CT** [#889](https://github.com/jaywedgeworth22/Congress.Trade/issues/889): (Historical In Progress rows from 2026-07-12…2026-07-22 below were left for
- **CT** [#890](https://github.com/jaywedgeworth22/Congress.Trade/issues/890): 2026-07-21 — Time Filter Dropdown — MERGED via #775 (was In Progress on
- **CT** [#891](https://github.com/jaywedgeworth22/Congress.Trade/issues/891): Critical bug automation: client command stale-reclaim
- **CT** [#892](https://github.com/jaywedgeworth22/Congress.Trade/issues/892): PR #776 — MERGED
- **CT** [#893](https://github.com/jaywedgeworth22/Congress.Trade/issues/893): OpenRouter Opus 4.8 rate-card hotfix — MERGED PR #674
- **CT** [#924](https://github.com/jaywedgeworth22/Congress.Trade/issues/924): 2026-07-24 — In Progress — Review/ingest backlog drain — fix
- **CT** [#999](https://github.com/jaywedgeworth22/Congress.Trade/issues/999): [2026-07-27] Autopilot tick continuation silent-drop — MERGED & DEPLOYED
- **CT** [#1030](https://github.com/jaywedgeworth22/Congress.Trade/issues/1030): iOS: register congresstrade:// URL scheme — sign-in callback broken
- **CT** [#1031](https://github.com/jaywedgeworth22/Congress.Trade/issues/1031): Backend: SSE live-tail cross-region fallback (unassigned, S)
- **CT** [#1032](https://github.com/jaywedgeworth22/Congress.Trade/issues/1032): Backend: coalesce lease.assertOwned round trips on queue hot path (unassigned
- **CT** [#1033](https://github.com/jaywedgeworth22/Congress.Trade/issues/1033): Web: OG/Twitter/meta tags + favicon/manifest (unassigned, S)
- **CT** [#1034](https://github.com/jaywedgeworth22/Congress.Trade/issues/1034): Web: deep links (?trade/?ticker/?member) + copy-link buttons (unassigned, M)
- **CT** [#1035](https://github.com/jaywedgeworth22/Congress.Trade/issues/1035): Owner decision: CSV export gate vs copy contradiction (unassigned, S)
- **CT** [#1036](https://github.com/jaywedgeworth22/Congress.Trade/issues/1036): iOS: premium gating + upgrade path on Alerts tab (unassigned, M)
- **CT** [#1037](https://github.com/jaywedgeworth22/Congress.Trade/issues/1037): iOS: watchlist editor UI (or decouple from delivery filter) (unassigned, M)
- **CT** [#1038](https://github.com/jaywedgeworth22/Congress.Trade/issues/1038): iOS: ticker detail screen + filing PDF viewer (unassigned, M)
- **CT** [#1040](https://github.com/jaywedgeworth22/Congress.Trade/issues/1040): Web: extract base64 assets from the 833KB dashboardHtml.ts (unassigned, M)
- **CT** [#1041](https://github.com/jaywedgeworth22/Congress.Trade/issues/1041): iOS: replaceCache -> transactional upsert (unassigned, S)
- **CT** [#1042](https://github.com/jaywedgeworth22/Congress.Trade/issues/1042): Both clients: server-side search wiring (unassigned, M)
- **CT** [#1043](https://github.com/jaywedgeworth22/Congress.Trade/issues/1043): Backend: query optimizations batch (unassigned, M)
- **CT** [#1045](https://github.com/jaywedgeworth22/Congress.Trade/issues/1045): Web UX batch: splash persistence, visibility-aware polling, URL-synced filters
- **CT** [#1049](https://github.com/jaywedgeworth22/Congress.Trade/issues/1049): Housekeeping sweep (unassigned, S)
- **CT** [#1252](https://github.com/jaywedgeworth22/Congress.Trade/issues/1252): [2026-07-31] Price-needs export — DEPLOYED via PR #1193 (73cac4ed). Live
- **CT** [#1253](https://github.com/jaywedgeworth22/Congress.Trade/issues/1253): [2026-07-30][KIMI] Unblock PR merges (Actions outage) + Deno retirement
- **CT** [#1268](https://github.com/jaywedgeworth22/Congress.Trade/issues/1268): [2026-08-03] Pipeline Robustification (M3 / R3) — COMPLETED. Implemented
- **CT** [#1269](https://github.com/jaywedgeworth22/Congress.Trade/issues/1269): [2026-08-03] Local Vision Worker & Bounded Wait State (M1 / R1)
- **CT** [#1270](https://github.com/jaywedgeworth22/Congress.Trade/issues/1270): [2026-08-03] Data Integrity & Deduplication (M4 / R4) — COMPLETED
- **CT** [#1271](https://github.com/jaywedgeworth22/Congress.Trade/issues/1271): [2026-08-03] Deterministic House PTR Extraction (M2 / R2) — COMPLETED
- **CT** [#1281](https://github.com/jaywedgeworth22/Congress.Trade/issues/1281): [2026-08-03] Clean app icon update (no ring, no S T letters) — MERGED PR
- **CT** [#1282](https://github.com/jaywedgeworth22/Congress.Trade/issues/1282): [2026-08-03] Dark mode brand logo wordmark recoloring — MERGED PR #1275
- **CT** [#1293](https://github.com/jaywedgeworth22/Congress.Trade/issues/1293): [2026-08-03] Clean Dark Logo Wordmark & Artifact Removal — MERGED PR #1291
- **CT** [#1294](https://github.com/jaywedgeworth22/Congress.Trade/issues/1294): 2026-08-03 — COMPLETED + DEPLOYED — Rohit Khanna → Ro Khanna member
- **CT** [#1296](https://github.com/jaywedgeworth22/Congress.Trade/issues/1296): 2026-08-03 — COMPLETED + DEPLOYED — Review queue clear + nested SQLite
- **CT** [#1307](https://github.com/jaywedgeworth22/Congress.Trade/issues/1307): 2026-08-04 — COMPLETED + DEPLOYED — Member drawer dual performance vs
- **CT** [#1308](https://github.com/jaywedgeworth22/Congress.Trade/issues/1308): [2026-08-04] R2 Class A hygiene (loader batch + litestream 5m + storage
- **CT** [#1313](https://github.com/jaywedgeworth22/Congress.Trade/issues/1313): 2026-08-04 — COMPLETED — Latency thorough overhaul (agreement candidate
- **CT** [#1316](https://github.com/jaywedgeworth22/Congress.Trade/issues/1316): 2026-08-04 — COMPLETED — Latency scoreboard thoroughness (#1311)
- **CT** [#1317](https://github.com/jaywedgeworth22/Congress.Trade/issues/1317): 2026-08-04 — COMPLETED — Latency scoreboard thoroughness. Concurrent
- **CT** [#1325](https://github.com/jaywedgeworth22/Congress.Trade/issues/1325): 2026-08-04 — COMPLETED — Latency match density (#1320 + #1322)
- **CT** [#1326](https://github.com/jaywedgeworth22/Congress.Trade/issues/1326): 2026-08-04 — COMPLETED — Latency match density. Find more real
- **CT** [#1331](https://github.com/jaywedgeworth22/Congress.Trade/issues/1331): 2026-08-04 — COMPLETED — UX P0 review fixes (web+iOS). PR #1329 merged
- **CT** [#1332](https://github.com/jaywedgeworth22/Congress.Trade/issues/1332): 2026-08-04 — COMPLETED + DEPLOYED — Resolve all open PRs → production
- **CT** [#1333](https://github.com/jaywedgeworth22/Congress.Trade/issues/1333): 2026-08-04 — COMPLETED (code) / PARTIAL (data density) — Latency probe &
- **CT** [#1334](https://github.com/jaywedgeworth22/Congress.Trade/issues/1334): 2026-08-03 — Prices from App B only + ST bulk load + DLQ clear. Owner
- **CT** [#1335](https://github.com/jaywedgeworth22/Congress.Trade/issues/1335): 2026-08-03 — KIMI takeover (max-plan cap mid-flight) — OPS COMPLETE
- **CT** [#1336](https://github.com/jaywedgeworth22/Congress.Trade/issues/1336): 2026-08-04 — COMPLETED + DEPLOYED — Executive feed hygiene (PR #1287
- **CT** [#1338](https://github.com/jaywedgeworth22/Congress.Trade/issues/1338): 2026-08-04 — COMPLETED — Fix SAVE badge contrast & top-right CTA button
- **CT** [#1353](https://github.com/jaywedgeworth22/Congress.Trade/issues/1353): 2026-08-05T02:28Z — COMPLETED + DEPLOYED — Queues, Latency metrics, UI
- **CT** [#1354](https://github.com/jaywedgeworth22/Congress.Trade/issues/1354): 2026-08-05T01:19Z — COMPLETED — UX Trends & Trades Filter Parity, Header
- **CT** [#1355](https://github.com/jaywedgeworth22/Congress.Trade/issues/1355): 2026-08-05 — COMPLETED + DEPLOYED — Pricing $5/$50 + 30d trial, delivery
- **CT** [#1356](https://github.com/jaywedgeworth22/Congress.Trade/issues/1356): 2026-08-05T01:45Z — COMPLETED + DEPLOYED — Canonical txtype B (Buy)
- **CT** [#1357](https://github.com/jaywedgeworth22/Congress.Trade/issues/1357): 2026-08-04 — COMPLETED — UX wave2 Premium CSV + product + iOS. PR #1342
- **CT** [#1358](https://github.com/jaywedgeworth22/Congress.Trade/issues/1358): 2026-08-04 — COMPLETED — UX wave2 integrate PR. Branch
- **CT** [#1359](https://github.com/jaywedgeworth22/Congress.Trade/issues/1359): 2026-08-04 — COMPLETED (sub-lane) — UX wave2 WEB. Branch
- **CT** [#1360](https://github.com/jaywedgeworth22/Congress.Trade/issues/1360): 2026-08-04 — COMPLETED (sub-lane) — Premium CSV API gate verify. Branch
- **CT** [#1361](https://github.com/jaywedgeworth22/Congress.Trade/issues/1361): 2026-08-05T00:20Z — COMPLETED + DEPLOYED — Product labels
- **CT** [#1362](https://github.com/jaywedgeworth22/Congress.Trade/issues/1362): 2026-08-04 — COMPLETED — UX wave2 RESTART (agent team). Branch
- **CT** [#1363](https://github.com/jaywedgeworth22/Congress.Trade/issues/1363): 2026-08-04 — COMPLETED (sub-lane) — Premium CSV UI. Branch
- **CT** [#1364](https://github.com/jaywedgeworth22/Congress.Trade/issues/1364): 2026-08-04 — COMPLETED (branch pushed, no PR) — UX wave2 iOS lane
- **CT** [#1365](https://github.com/jaywedgeworth22/Congress.Trade/issues/1365): 2026-08-04 — COMPLETED — UX wave2 agent team. Branch
- **CT** [#1366](https://github.com/jaywedgeworth22/Congress.Trade/issues/1366): 2026-08-04 — COMPLETED — UX wave2: Premium CSV + review improvements
- **CT** [#1368](https://github.com/jaywedgeworth22/Congress.Trade/issues/1368): 2026-08-05 — IN PROGRESS — Resolve open PRs → production. Merged main
- **CT** [#1370](https://github.com/jaywedgeworth22/Congress.Trade/issues/1370): 2026-08-05 — COMPLETED + DEPLOYED — Resolve all open PRs → production
- **CT** [#1375](https://github.com/jaywedgeworth22/Congress.Trade/issues/1375): 2026-08-05 — In Progress — Latency live-only max match. Race only live
- **CT** [#1377](https://github.com/jaywedgeworth22/Congress.Trade/issues/1377): 2026-08-05 — IN PROGRESS — Lower delivery subscription quota to 2 per
- **CT** [#1378](https://github.com/jaywedgeworth22/Congress.Trade/issues/1378): COMPLETED (already on main; board hygiene 2026-08-05 ): Web
- **CT** [#1379](https://github.com/jaywedgeworth22/Congress.Trade/issues/1379): COMPLETED (already on main; board hygiene 2026-08-05 ): Web: deep links
- **CT** [#1380](https://github.com/jaywedgeworth22/Congress.Trade/issues/1380): 2026-08-05 — IN PROGRESS — Lower delivery subscription quota to 2 per
- **CT** [#1381](https://github.com/jaywedgeworth22/Congress.Trade/issues/1381): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision: CSV
- **CT** [#1382](https://github.com/jaywedgeworth22/Congress.Trade/issues/1382): COMPLETED (already on main; board hygiene 2026-08-05 ): Web
- **CT** [#1383](https://github.com/jaywedgeworth22/Congress.Trade/issues/1383): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision
- **CT** [#1384](https://github.com/jaywedgeworth22/Congress.Trade/issues/1384): COMPLETED (already on main; board hygiene 2026-08-05 ): Web: deep links
- **CT** [#1385](https://github.com/jaywedgeworth22/Congress.Trade/issues/1385): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision
- **CT** [#1386](https://github.com/jaywedgeworth22/Congress.Trade/issues/1386): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision: CSV
- **CT** [#1387](https://github.com/jaywedgeworth22/Congress.Trade/issues/1387): 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment)
- **CT** [#1388](https://github.com/jaywedgeworth22/Congress.Trade/issues/1388): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision
- **CT** [#1389](https://github.com/jaywedgeworth22/Congress.Trade/issues/1389): 2026-08-05 — Board hygiene final: closed 14 stale Active rows
- **CT** [#1390](https://github.com/jaywedgeworth22/Congress.Trade/issues/1390): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision
- **CT** [#1391](https://github.com/jaywedgeworth22/Congress.Trade/issues/1391): 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment)
- **CT** [#1392](https://github.com/jaywedgeworth22/Congress.Trade/issues/1392): 2026-08-05 — Board hygiene final: closed 14 stale Active rows
- **CT** [#1393](https://github.com/jaywedgeworth22/Congress.Trade/issues/1393): 2026-08-05 — Board hygiene: moved 88 Active/Planned → Completed (incl
- **CT** [#1394](https://github.com/jaywedgeworth22/Congress.Trade/issues/1394): 2026-08-05 — Board hygiene: moved 88 Active/Planned → Completed (incl
- **CT** [#1395](https://github.com/jaywedgeworth22/Congress.Trade/issues/1395): 2026-08-05 — COMPLETED — Latency live-only max match (#1374). Race only
- **CT** [#1396](https://github.com/jaywedgeworth22/Congress.Trade/issues/1396): 2026-08-05 — COMPLETED — Latency live-only max match (#1374). Race only
- **CT** [#1397](https://github.com/jaywedgeworth22/Congress.Trade/issues/1397): 2026-08-05 — Board hygiene: moved 88 Active/Planned → Completed (incl
- **CT** [#1398](https://github.com/jaywedgeworth22/Congress.Trade/issues/1398): 2026-08-05 — COMPLETED — Latency live-only max match (#1374). Race only
- **CT** [#1399](https://github.com/jaywedgeworth22/Congress.Trade/issues/1399): 2026-08-05 — Board hygiene: moved 19 Active/Planned → Deployed
- **CT** [#1403](https://github.com/jaywedgeworth22/Congress.Trade/issues/1403): 2026-08-05 — IN PROGRESS — Housekeeping + query index (#1049/#1043
- **CT** [#1411](https://github.com/jaywedgeworth22/Congress.Trade/issues/1411): 2026-08-05 — IN PROGRESS — FMP free keys latency-only. Branch
- **CT** [#1414](https://github.com/jaywedgeworth22/Congress.Trade/issues/1414): 2026-08-05 — COMPLETED — Straightforward planned effort closeout (board
- **CT** [#1418](https://github.com/jaywedgeworth22/Congress.Trade/issues/1418): 2026-08-05 — COMPLETED — FMP latency family OFF (grey) + dual-path race
- **CT** [#1428](https://github.com/jaywedgeworth22/Congress.Trade/issues/1428): 2026-08-06 — COMPLETED — Second CT self-hosted CI runner. Reassigned
- **ST** [#834](https://github.com/jaywedgeworth22/Socratic.Trade/issues/834): Production release + post-deploy money-path verification of the 2026-07-05
- **ST** [#837](https://github.com/jaywedgeworth22/Socratic.Trade/issues/837): Headline first-seen timestamps to close the evidence-age receipt gap
- **ST** [#838](https://github.com/jaywedgeworth22/Socratic.Trade/issues/838): Extend prompt fencing and injection receipts beyond the money path
- **ST** [#961](https://github.com/jaywedgeworth22/Socratic.Trade/issues/961): ~~Disentangle PR #805: land — P0/P1 commit and — health slice as separate
- **ST** [#962](https://github.com/jaywedgeworth22/Socratic.Trade/issues/962): ~~Migrate legacy regime:current row to per-user keys at first tick after the P0
- **ST** [#966](https://github.com/jaywedgeworth22/Socratic.Trade/issues/966): Prune stale abandoned local-only branches from origin (June 21–29 experiments)
- **ST** [#1290](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1290): Enrichment starvation: force-included scan candidates (holdings + event
- **ST** [#1357](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1357): Activity-audit item 10: account-attribution sweep in strategy.ts +
- **ST** [#1756](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1756): Socratic server/infrastructure panel reliability ( delegated
- **ST** [#1763](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1763): PR #1735 proposed-model attribution display contract
- **ST** [#1767](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1767): PR #1760 review/comment/conflict closeout (branch
- **ST** [#1772](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1772): OpenRouter credit signal on /api/health (branch
- **ST** [#1797](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1797): Usage-compliance Wave 2 (ST lane): telemetry gaps +
- **ST** [#1798](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1798): handoff §7 ports: coach-note archive +
- **ST** [#1799](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1799): Serial 6-lane landing train (operator session
- **ST** [#1800](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1800): PR #1735 proposed-model attribution display contract
- **ST** [#1802](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1802): CI shallow-checkout recovery (PR #1741, branch
- **ST** [#1803](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1803): CI event-SHA checkout pin (PR #1742, branch
- **ST** [#1832](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1832): Shared package bump to 904ea96a (Congress.Trade PR
- **ST** [#1837](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1837): Which-key visibility + "agents never create API keys"
- **ST** [#1860](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1860): Purge Voyage AI SDK and standardize RAG on OpenRouter BAAI
- **ST** [#1861](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1861): Multi-wave expert-review implementation (claimed
- **ST** [#1862](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1862): Full multi-expert app review (claimed 2026-07-20)
- **ST** [#1863](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1863): Unstick red/stuck PRs #1829/#1827/#1792/#1780
- **ST** [#1864](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1864): Use OpenRouter "latest" Aliases for Anthropic Models
- **ST** [#1865](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1865): [Socratic.Trade+CT+UM] Resume all open — desktop sessions (claimed
- **ST** [#1866](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1866): Fix date-dependent wash sale test flake in chat draft
- **ST** [#1867](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1867): BRANCH PROTECTION TEMPORARILY RELAXED to break a 34-PR
- **ST** [#1868](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1868): CI-load trim: Playwright Smoke off every PR (worktree
- **ST** [#1869](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1869): CI package-lock fix + unblocking 38 open PRs (worktree
- **ST** [#1870](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1870): Owner-directed open-PR merge sweep + prod auto-reboot
- **ST** [#1871](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1871): PR #1776 review-thread closeout: all 4 — connector
- **ST** [#1872](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1872): Three new RapidAPI-backed enrichment providers: Mboum
- **ST** [#1873](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1873): handoff §7 ports: coach-note archive +
- **ST** [#1874](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1874): Admin console shell parity (PR #1740, branch
- **ST** [#1878](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1878): [ on 's lane] PR #1775 review-thread closeout — scoped
- **ST** [#1880](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1880): Stop placement intent authoritative-absence fix (branch
- **ST** [#1881](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1881): Corpus re-embed scoped-run purge gate fix (branch
- **ST** [#1882](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1882): check-pin required-status-context merge deadlock fix
- **ST** [#1887](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1887): Native iOS mobile-first product replacement — COMPLETED 2026-07-22 via
- **ST** [#1893](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1893): CI pending-run collapse (branch
- **ST** [#1894](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1894): Use OpenRouter "latest" Aliases for Anthropic Models
- **ST** [#1895](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1895): [Socratic.Trade+CT+UM] Resume all open — desktop sessions (claimed
- **ST** [#1896](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1896): Native iOS mobile-first product replacement — IN PROGRESS 2026-07-22
- **ST** [#1897](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1897): [CORRECTION 2026-07-22] Native iOS mobile-first product replacement — COMPLETED
- **ST** [#1899](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1899): Shared-package pin-check queue unblock (original PR
- **ST** [#1900](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1900): Usage telemetry v2 producer adoption (branch
- **ST** [#1954](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1954): forgotten-PR audit — DONE 2026-07-22. Closed
- **ST** [#1958](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1958): Robinhood guardrail cap resilience (branch
- **ST** [#1959](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1959): Salvage #1906 market-data rename-vs-acquisition via
- **ST** [#1962](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1962): Dark mode near-black retint (branch
- **ST** [#1963](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1963): UI Redesign: Proposal Slide-out Drawer and Inline Approval
- **ST** [#1966](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1966): PR #1892 review-thread closeout round 2 — PUSHED/THREADS
- **ST** [#1967](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1967): PR #1892 P2 review threads (rerank nomemory + sec-8k
- **ST** [#1968](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1968): [ team] RAG strategic-performance implementation program
- **ST** [#1969](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1969): Managed RAG ingestion provider-authority gate (branch
- **ST** [#1970](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1970): Managed RAG ingestion provider-authority gate (branch
- **ST** [#1971](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1971): [ team] RAG strategic-performance implementation program
- **ST** [#1972](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1972): [ sublane] Read-only Turso/libSQL and Pinecone Assistant
- **ST** [#1973](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1973): [ sublane] Bounded post-rerank parent-context expansion
- **ST** [#1974](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1974): Production-path RAG evaluator (worktree
- **ST** [#1975](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1975): Production-path RAG evaluator (worktree
- **ST** [#1976](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1976): Production-path RAG evaluator (worktree
- **ST** [#1983](https://github.com/jaywedgeworth22/Socratic.Trade/issues/1983): [OWNER REMINDER][ 2026-07-22] Enable default-off RAG
- **ST** [#2142](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2142): Correction 2026-07-22 — [Socratic.Trade] PR #1792 hosted typecheck
- **ST** [#2161](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2161): SEC/RAG P0 corpus truth + frozen 1,000-CIK universe ( program;
- **ST** [#2162](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2162): SEC/RAG P0 occurrence identity + durable manifest/job state ( program;
- **ST** [#2163](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2163): SEC/RAG P0 DOM/iXBRL parser + tokenizer-aware section/table chunker
- **ST** [#2166](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2166): SEC/RAG P1 retrieval/strategy consumption redesign ( program;
- **ST** [#2170](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2170): Enrichment starvation: force-included scan candidates (holdings + event
- **ST** [#2171](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2171): Activity-audit P2.5: notification status recorder lies ("Not sent" on 1035/1035
- **ST** [#2173](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2173): CI standard rollout (cross-app, unassigned) — SUPERSEDED / PARTIAL
- **ST** [#2174](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2174): Wave-2 memory/RAG core — SUPERSEDED by
- **ST** [#2175](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2175): Owner ratification: Rule 4 fundamentals-veto overridability — COMPLETED
- **ST** [#2176](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2176): Open PRs for the stalled w2-coaching-durable and w2-reflection-decompose
- **ST** [#2177](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2177): Sweep settings-table keys for remaining cross-user shared-row races
- **ST** [#2178](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2178): risk-row handback — SUPERSEDED / HISTORICAL ( correction
- **ST** [#2179](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2179): Resolve main-protection ruleset review gate that leaves all-green PRs stuck
- **ST** [#2180](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2180): Rebase/merge-forward PR #372 onto current main — COMPLETED via #372 merge
- **ST** [#2202](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2202): Coolify/Hetzner runners only + monitor (branch
- **ST** [#2222](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2222): Fix vs-SPY benchmark accuracy (cash-flow-aware TWR)
- **ST** [#2223](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2223): PR merge drain + Actions runner unblock (land
- **ST** [#2236](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2236): [OWNER REMINDER][ 2026-07-22] Enable default-off RAG
- **ST** [#2238](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2238): Dormant features readiness
- **ST** [#2239](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2239): RAG enablement + Exit Contract B1 + branch prune
- **ST** [#2246](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2246): Free-first enrichment cascade + coverage report
- **ST** [#2247](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2247): Alpaca/orders "300+ pending" inflation (doneforday
- **ST** [#2290](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2290): [KIMI] OSS-lessons program: docs/oss-lessons.md + task brain
- **ST** [#2291](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2291): [KIMI] Generalized preview renderers for mutating operations
- **ST** [#2292](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2292): [KIMI] nofx-style consecutive-miss safety mode — In Progress
- **ST** [#2293](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2293): [Fleet] Shut down Oracle Actions runners; all repos GitHub-hosted CI
- **ST** [#2297](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2297): [KIMI] OSS-lessons program: docs/oss-lessons.md + task brain
- **ST** [#2298](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2298): [KIMI] Generalized preview renderers for mutating operations
- **ST** [#2301](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2301): [KIMI] nofx-style consecutive-miss safety mode
- **ST** [#2302](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2302): [KIMI] Generalized preview renderers for mutating operations
- **ST** [#2306](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2306): Backtest-integrity suite for the learning loop — PARTIALLY
- **ST** [#2307](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2307): [KIMI] Backtest-integrity §6 slice 1: rule significance testing
- **ST** [#2311](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2311): [2026-07-30] Share App A price-needs for congressional S&P performance
- **ST** [#2328](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2328): [KIMI] Backtest-integrity §6 slice 3: qlib walk-forward window
- **ST** [#2329](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2329): [KIMI] Time-bounded (PIT) proposal evidence for the auto-tuner
- **ST** [#2336](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2336): Brokerage-model order-state hardening — PARTIALLY IMPLEMENTED
- **ST** [#2346](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2346): [2026-08-01] Repair PR #2344 (shared v2.4.1 bump) — landing. 's bump
- **ST** [#2357](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2357): [2026-08-01] Peer reads: skip App A echo tier — landing. The token-gated
- **ST** [#2412](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2412): UX program RESTART implementer blitz — IN PROGRESS
- **ST** [#2452](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2452): UX PR-A1 honest run skip statuses in UI — IN PR
- **ST** [#2454](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2454): UX Wave B IA — COMPLETED 2026-08-05 (PR #2425 / B1
- **ST** [#2455](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2455): UX Wave C speed — COMPLETED 2026-08-05 (PR #2423) (C1
- **ST** [#2462](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2462): UX implementer team RESTARTED 2026-08-04 ~session: 8
- **ST** [#2463](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2463): UX Wave D residual (D3 iOS command feedback if not covered)
- **ST** [#2469](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2469): 2026-08-05 — Board hygiene: moved 3 Active/Planned → Deployed
- **ST** [#2470](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2470): Open PR drain → main/prod — COMPLETED + DEPLOYED
- **ST** [#2471](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2471): 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment)
- **ST** [#2472](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2472): 2026-08-05 — Board hygiene final: closed 35 stale Active rows
- **ST** [#2473](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2473): UX Wave A implementation blitz — IN PROGRESS 2026-08-04
- **ST** [#2474](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2474): 2026-08-05 — Board hygiene: moved 81 Active/Planned → Completed (incl
- **ST** [#2475](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2475): UX team progress 2026-08-05 ~00:40Z: MERGED #2411 A4+A5
- **ST** [#2476](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2476): UX implementer team RESTART status 2026-08-05: MERGED
- **ST** [#2477](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2477): UX PR-C3 scan table virtualization (TableVirtuoso) — IN
- **ST** [#2478](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2478): UX B3+E2+E3 polish — COMPLETED 2026-08-04 (PR #2426
- **ST** [#2479](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2479): UX improvement program (web + PWA + iOS) — COMPLETED
- **ST** [#2480](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2480): UX Wave D mobile/iOS parity — COMPLETED 2026-08-05 (PR
- **ST** [#2481](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2481): UX PR-A2 approval card progressive disclosure
- **ST** [#2482](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2482): UX PR-A3 first-run readiness checklist hero — IN PR
- **ST** [#2483](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2483): UX PR-A4 + PR-A5 Guardrails Advanced collapsed + PWA
- **ST** [#2484](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2484): UX Wave D PR-D1+D2 iOS brand teal + Home hero — IN PR
- **ST** [#2485](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2485): UX PR-D4 PWA polish — IN PR 2026-08-04 (PR #2416, branch
- **ST** [#2486](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2486): Paper-account learning parity in Learning Review
- **ST** [#2487](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2487): UX program Waves A–E — DEPLOYED to production 2026-08-05
- **ST** [#2502](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2502): 2026-08-05 — COMPLETED (in PR) — P0 Security residual: audit hash chain
- **ST** [#2509](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2509): 2026-08-05 — COMPLETED — Activity-audit leftovers board hygiene +
- **ST** [#2515](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2515): 2026-08-05 — COMPLETED (code on main; board hygiene) — Issue/effort
- **ST** [#2516](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2516): 2026-08-05 — COMPLETED + DEPLOYED — fix: prompt fencing, headline
- **ST** [#2517](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2517): 2026-08-05 — COMPLETED + DEPLOYED — fix(console): reopenable framework
- **ST** [#2518](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2518): 2026-08-05 — COMPLETED + DEPLOYED — fix(ux): single primary Run once
- **ST** [#2519](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2519): 2026-08-05 — COMPLETED + DEPLOYED — feat(congress): filing-date member
- **ST** [#2520](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2520): 2026-08-05 — COMPLETED + DEPLOYED — feat(console): plain-language nav UX
- **ST** [#2521](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2521): 2026-08-04 — COMPLETED + DEPLOYED — fix(data): never call FMP/Quiver/UW
- **ST** [#2522](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2522): 2026-08-05 — COMPLETED + DEPLOYED — feat(ios): TestFlight agent ship
- **ST** [#2523](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2523): 2026-08-05 — COMPLETED on main — iOS tab rename Coach → Insights
- **ST** [#2524](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2524): 2026-08-05 — COMPLETED on main — Console topCandidates.slice crash
- **UM** [#952](https://github.com/jaywedgeworth22/Usage-Monitor/issues/952): Overview money UX: global budget, projected breakdown, quiet stale, ROIC
- **UM** [#954](https://github.com/jaywedgeworth22/Usage-Monitor/issues/954): Production recovery after deploy cutover gap (2026-08-05) — DEPLOYED
- **UM** [#955](https://github.com/jaywedgeworth22/Usage-Monitor/issues/955): Design: mobile full-parity + phone self-host topology (2026-08-04)
- **UM** [#956](https://github.com/jaywedgeworth22/Usage-Monitor/issues/956): Wire web design tokens into Tailwind + primary chrome (2026-08-05)
- **UM** [#957](https://github.com/jaywedgeworth22/Usage-Monitor/issues/957): UX deferred wave 2 (wizard/mobile cards/nav/charts/iOS depth)
- **UM** [#958](https://github.com/jaywedgeworth22/Usage-Monitor/issues/958): Full web+iOS UX overhaul (review execution) (2026-08-04) — COMPLETED +
- **UM** [#959](https://github.com/jaywedgeworth22/Usage-Monitor/issues/959): Land open PR queue + deploy host patches to production (2026-08-04)
- **UM** [#960](https://github.com/jaywedgeworth22/Usage-Monitor/issues/960): Deploy preflight SQLite integrity timeout 120→900s (2026-08-04) — MERGED
- **UM** [#961](https://github.com/jaywedgeworth22/Usage-Monitor/issues/961): Land open PR queue to production (2026-08-04) — COMPLETE / PROD ON MAIN
- **UM** [#962](https://github.com/jaywedgeworth22/Usage-Monitor/issues/962): audit remediation sweep (2026-08-01..02) — COMPLETE
- **UM** [#963](https://github.com/jaywedgeworth22/Usage-Monitor/issues/963): Receipt inbox live on Jays.Services 2026-07-29
- **UM** [#964](https://github.com/jaywedgeworth22/Usage-Monitor/issues/964): R2 entitlement verified + usage-monitor-receipts
- **UM** [#965](https://github.com/jaywedgeworth22/Usage-Monitor/issues/965): 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment)
- **UM** [#966](https://github.com/jaywedgeworth22/Usage-Monitor/issues/966): 2026-08-05 — Board hygiene final: closed 1 stale Active rows
- **UM** [#967](https://github.com/jaywedgeworth22/Usage-Monitor/issues/967): Receipt inbox addresses chosen 2026-07-27. Fallback
- **UM** [#968](https://github.com/jaywedgeworth22/Usage-Monitor/issues/968): iOS Overview: remove truncated “Budget is always this…” toolbar caption
- **UM** [#969](https://github.com/jaywedgeworth22/Usage-Monitor/issues/969): R2 free-tier 70% auto-shutoff fix (2026-08-03)
- **UM** [#970](https://github.com/jaywedgeworth22/Usage-Monitor/issues/970): Whole-app read-only audit (2026-08-01) — COMPLETED / CRITICAL INCIDENT
- **UM** [#971](https://github.com/jaywedgeworth22/Usage-Monitor/issues/971): Receipt inbox Worker + Email Routing (post-R2 bucket)
- **UM** [#972](https://github.com/jaywedgeworth22/Usage-Monitor/issues/972): [Uptime] Usage Monitor Oracle origin readiness failure
- **UM** [#977](https://github.com/jaywedgeworth22/Usage-Monitor/issues/977): Issue/effort hygiene + replica age align with 1h Litestream sync
- **UM** [#1005](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1005): Orange brand + segmented History control + uncrowded nav (2026-08-05)

### Issues opened

- **CT** [#1368](https://github.com/jaywedgeworth22/Congress.Trade/issues/1368): 2026-08-05 — IN PROGRESS — Resolve open PRs → production. Merged main
- **CT** [#1370](https://github.com/jaywedgeworth22/Congress.Trade/issues/1370): 2026-08-05 — COMPLETED + DEPLOYED — Resolve all open PRs → production
- **CT** [#1375](https://github.com/jaywedgeworth22/Congress.Trade/issues/1375): 2026-08-05 — In Progress — Latency live-only max match. Race only live
- **CT** [#1377](https://github.com/jaywedgeworth22/Congress.Trade/issues/1377): 2026-08-05 — IN PROGRESS — Lower delivery subscription quota to 2 per
- **CT** [#1378](https://github.com/jaywedgeworth22/Congress.Trade/issues/1378): COMPLETED (already on main; board hygiene 2026-08-05 ): Web
- **CT** [#1379](https://github.com/jaywedgeworth22/Congress.Trade/issues/1379): COMPLETED (already on main; board hygiene 2026-08-05 ): Web: deep links
- **CT** [#1380](https://github.com/jaywedgeworth22/Congress.Trade/issues/1380): 2026-08-05 — IN PROGRESS — Lower delivery subscription quota to 2 per
- **CT** [#1381](https://github.com/jaywedgeworth22/Congress.Trade/issues/1381): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision: CSV
- **CT** [#1382](https://github.com/jaywedgeworth22/Congress.Trade/issues/1382): COMPLETED (already on main; board hygiene 2026-08-05 ): Web
- **CT** [#1383](https://github.com/jaywedgeworth22/Congress.Trade/issues/1383): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision
- **CT** [#1384](https://github.com/jaywedgeworth22/Congress.Trade/issues/1384): COMPLETED (already on main; board hygiene 2026-08-05 ): Web: deep links
- **CT** [#1385](https://github.com/jaywedgeworth22/Congress.Trade/issues/1385): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision
- **CT** [#1386](https://github.com/jaywedgeworth22/Congress.Trade/issues/1386): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision: CSV
- **CT** [#1387](https://github.com/jaywedgeworth22/Congress.Trade/issues/1387): 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment)
- **CT** [#1388](https://github.com/jaywedgeworth22/Congress.Trade/issues/1388): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision
- **CT** [#1389](https://github.com/jaywedgeworth22/Congress.Trade/issues/1389): 2026-08-05 — Board hygiene final: closed 14 stale Active rows
- **CT** [#1390](https://github.com/jaywedgeworth22/Congress.Trade/issues/1390): COMPLETED (already on main; board hygiene 2026-08-05 ): Owner decision
- **CT** [#1391](https://github.com/jaywedgeworth22/Congress.Trade/issues/1391): 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment)
- **CT** [#1392](https://github.com/jaywedgeworth22/Congress.Trade/issues/1392): 2026-08-05 — Board hygiene final: closed 14 stale Active rows
- **CT** [#1393](https://github.com/jaywedgeworth22/Congress.Trade/issues/1393): 2026-08-05 — Board hygiene: moved 88 Active/Planned → Completed (incl
- **CT** [#1394](https://github.com/jaywedgeworth22/Congress.Trade/issues/1394): 2026-08-05 — Board hygiene: moved 88 Active/Planned → Completed (incl
- **CT** [#1395](https://github.com/jaywedgeworth22/Congress.Trade/issues/1395): 2026-08-05 — COMPLETED — Latency live-only max match (#1374). Race only
- **CT** [#1396](https://github.com/jaywedgeworth22/Congress.Trade/issues/1396): 2026-08-05 — COMPLETED — Latency live-only max match (#1374). Race only
- **CT** [#1397](https://github.com/jaywedgeworth22/Congress.Trade/issues/1397): 2026-08-05 — Board hygiene: moved 88 Active/Planned → Completed (incl
- **CT** [#1398](https://github.com/jaywedgeworth22/Congress.Trade/issues/1398): 2026-08-05 — COMPLETED — Latency live-only max match (#1374). Race only
- **CT** [#1399](https://github.com/jaywedgeworth22/Congress.Trade/issues/1399): 2026-08-05 — Board hygiene: moved 19 Active/Planned → Deployed
- **CT** [#1403](https://github.com/jaywedgeworth22/Congress.Trade/issues/1403): 2026-08-05 — IN PROGRESS — Housekeeping + query index (#1049/#1043
- **CT** [#1411](https://github.com/jaywedgeworth22/Congress.Trade/issues/1411): 2026-08-05 — IN PROGRESS — FMP free keys latency-only. Branch
- **CT** [#1412](https://github.com/jaywedgeworth22/Congress.Trade/issues/1412): 2026-08-05 — IN PR — #1040 extract dashboard assets PR #1406; #1039
- **CT** [#1413](https://github.com/jaywedgeworth22/Congress.Trade/issues/1413): 2026-08-05 — IN PROGRESS — Land remaining open PRs #1407/#1409/#1410
- **CT** [#1414](https://github.com/jaywedgeworth22/Congress.Trade/issues/1414): 2026-08-05 — COMPLETED — Straightforward planned effort closeout (board
- **CT** [#1418](https://github.com/jaywedgeworth22/Congress.Trade/issues/1418): 2026-08-05 — COMPLETED — FMP latency family OFF (grey) + dual-path race
- **CT** [#1428](https://github.com/jaywedgeworth22/Congress.Trade/issues/1428): 2026-08-06 — COMPLETED — Second CT self-hosted CI runner. Reassigned
- **ST** [#2462](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2462): UX implementer team RESTARTED 2026-08-04 ~session: 8
- **ST** [#2463](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2463): UX Wave D residual (D3 iOS command feedback if not covered)
- **ST** [#2464](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2464): 2026-08-05 — IN PROGRESS — Open PR #2443: fix(quotes): Tradier sandbox
- **ST** [#2465](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2465): 2026-08-05 — IN PROGRESS — Open PR #2445: fix(ios): Apple Sign-In width
- **ST** [#2466](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2466): 2026-08-05 — IN PROGRESS — Open PR #2459: fix: prompt fencing, headline
- **ST** [#2467](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2467): iOS tab rename Coach → Insights — IN PROGRESS 2026-08-04
- **ST** [#2468](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2468): UX PR-B4 Settings sticky TOC / jump chips — IN PROGRESS
- **ST** [#2469](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2469): 2026-08-05 — Board hygiene: moved 3 Active/Planned → Deployed
- **ST** [#2470](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2470): Open PR drain → main/prod — COMPLETED + DEPLOYED
- **ST** [#2471](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2471): 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment)
- **ST** [#2472](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2472): 2026-08-05 — Board hygiene final: closed 35 stale Active rows
- **ST** [#2473](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2473): UX Wave A implementation blitz — IN PROGRESS 2026-08-04
- **ST** [#2474](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2474): 2026-08-05 — Board hygiene: moved 81 Active/Planned → Completed (incl
- **ST** [#2475](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2475): UX team progress 2026-08-05 ~00:40Z: MERGED #2411 A4+A5
- **ST** [#2476](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2476): UX implementer team RESTART status 2026-08-05: MERGED
- **ST** [#2477](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2477): UX PR-C3 scan table virtualization (TableVirtuoso) — IN
- **ST** [#2478](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2478): UX B3+E2+E3 polish — COMPLETED 2026-08-04 (PR #2426
- **ST** [#2479](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2479): UX improvement program (web + PWA + iOS) — COMPLETED
- **ST** [#2480](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2480): UX Wave D mobile/iOS parity — COMPLETED 2026-08-05 (PR
- **ST** [#2481](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2481): UX PR-A2 approval card progressive disclosure
- **ST** [#2482](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2482): UX PR-A3 first-run readiness checklist hero — IN PR
- **ST** [#2483](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2483): UX PR-A4 + PR-A5 Guardrails Advanced collapsed + PWA
- **ST** [#2484](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2484): UX Wave D PR-D1+D2 iOS brand teal + Home hero — IN PR
- **ST** [#2485](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2485): UX PR-D4 PWA polish — IN PR 2026-08-04 (PR #2416, branch
- **ST** [#2486](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2486): Paper-account learning parity in Learning Review
- **ST** [#2487](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2487): UX program Waves A–E — DEPLOYED to production 2026-08-05
- **ST** [#2493](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2493): Activity-audit P2.6: orderplacementuncertain misclassifies definitive
- **ST** [#2494](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2494): Activity-audit P2.7: stale-exit cancel settle multi-poll — COMPLETED + DEPLOYED
- **ST** [#2495](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2495): Activity-audit P2.8: synthetic-stop fail alert — COMPLETED + DEPLOYED
- **ST** [#2496](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2496): Activity-audit P2.9: LLM failover + cadence jitter — COMPLETED 2026-08-05
- **ST** [#2499](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2499): P0 Security (5) — COMPLETED 2026-08-05 ( + prior ). P0-1 rate-limit
- **ST** [#2500](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2500): P1 Mechanical fixes (9) — MOSTLY COMPLETED 2026-08-05 ( hygiene). P1-1/2
- **ST** [#2501](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2501): 2026-08-05 — IN PROGRESS — P0 security residual (#1159): decryptValue
- **ST** [#2502](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2502): 2026-08-05 — COMPLETED (in PR) — P0 Security residual: audit hash chain
- **ST** [#2506](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2506): Activity-audit P2 backlog (from docs/reviews/2026-07-09-activity-feed-audit.md)
- **ST** [#2507](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2507): Activity-audit P2.4: congresssharedaily retry storm — COMPLETED + DEPLOYED
- **ST** [#2508](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2508): Activity-audit P3 batch (8 small items) — COMPLETED 2026-08-05 (board hygiene +
- **ST** [#2509](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2509): 2026-08-05 — COMPLETED — Activity-audit leftovers board hygiene +
- **ST** [#2511](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2511): 2026-08-05 — COMPLETED + DEPLOYED — Open PR #2489 merged: activity-audit
- **ST** [#2512](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2512): 2026-08-05 — IN PROGRESS — Open PR #2445: iOS Sign-In width cap + SSE
- **ST** [#2513](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2513): 2026-08-05 — IN PROGRESS — Open PR #2443: Tradier sandbox venue-aligned
- **ST** [#2514](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2514): 2026-08-05 — IN PROGRESS — Residual issues batch (B4 Settings TOC full
- **ST** [#2515](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2515): 2026-08-05 — COMPLETED (code on main; board hygiene) — Issue/effort
- **ST** [#2516](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2516): 2026-08-05 — COMPLETED + DEPLOYED — fix: prompt fencing, headline
- **ST** [#2517](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2517): 2026-08-05 — COMPLETED + DEPLOYED — fix(console): reopenable framework
- **ST** [#2518](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2518): 2026-08-05 — COMPLETED + DEPLOYED — fix(ux): single primary Run once
- **ST** [#2519](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2519): 2026-08-05 — COMPLETED + DEPLOYED — feat(congress): filing-date member
- **ST** [#2520](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2520): 2026-08-05 — COMPLETED + DEPLOYED — feat(console): plain-language nav UX
- **ST** [#2521](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2521): 2026-08-04 — COMPLETED + DEPLOYED — fix(data): never call FMP/Quiver/UW
- **ST** [#2522](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2522): 2026-08-05 — COMPLETED + DEPLOYED — feat(ios): TestFlight agent ship
- **ST** [#2523](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2523): 2026-08-05 — COMPLETED on main — iOS tab rename Coach → Insights
- **ST** [#2524](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2524): 2026-08-05 — COMPLETED on main — Console topCandidates.slice crash
- **ST** [#2525](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2525): Activity-audit owner decisions (4) — COMPLETED 2026-08-05 (owner rulings
- **ST** [#2534](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2534): Data sources overhaul (matrix, FMP OFF, soft health
- **ST** [#2535](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2535): Non-FMP data sources STOPPED fix (soft limits + Nasdaq
- **ST** [#2537](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2537): 2026-08-05 — IN PROGRESS — Fix inflated account % return (synthetic
- **ST** [#2539](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2539): 2026-08-05 — IN PROGRESS — Multi-period TWR: split at each
- **UM** [#952](https://github.com/jaywedgeworth22/Usage-Monitor/issues/952): Overview money UX: global budget, projected breakdown, quiet stale, ROIC
- **UM** [#953](https://github.com/jaywedgeworth22/Usage-Monitor/issues/953): [OWNER ACTION REQUIRED] P0 deleted-live-SQLite recovery (2026-08-01) — ACTIVE
- **UM** [#954](https://github.com/jaywedgeworth22/Usage-Monitor/issues/954): Production recovery after deploy cutover gap (2026-08-05) — DEPLOYED
- **UM** [#955](https://github.com/jaywedgeworth22/Usage-Monitor/issues/955): Design: mobile full-parity + phone self-host topology (2026-08-04)
- **UM** [#956](https://github.com/jaywedgeworth22/Usage-Monitor/issues/956): Wire web design tokens into Tailwind + primary chrome (2026-08-05)
- **UM** [#957](https://github.com/jaywedgeworth22/Usage-Monitor/issues/957): UX deferred wave 2 (wizard/mobile cards/nav/charts/iOS depth)
- **UM** [#958](https://github.com/jaywedgeworth22/Usage-Monitor/issues/958): Full web+iOS UX overhaul (review execution) (2026-08-04) — COMPLETED +
- **UM** [#959](https://github.com/jaywedgeworth22/Usage-Monitor/issues/959): Land open PR queue + deploy host patches to production (2026-08-04)
- **UM** [#960](https://github.com/jaywedgeworth22/Usage-Monitor/issues/960): Deploy preflight SQLite integrity timeout 120→900s (2026-08-04) — MERGED
- **UM** [#961](https://github.com/jaywedgeworth22/Usage-Monitor/issues/961): Land open PR queue to production (2026-08-04) — COMPLETE / PROD ON MAIN
- **UM** [#962](https://github.com/jaywedgeworth22/Usage-Monitor/issues/962): audit remediation sweep (2026-08-01..02) — COMPLETE
- **UM** [#963](https://github.com/jaywedgeworth22/Usage-Monitor/issues/963): Receipt inbox live on Jays.Services 2026-07-29
- **UM** [#964](https://github.com/jaywedgeworth22/Usage-Monitor/issues/964): R2 entitlement verified + usage-monitor-receipts
- **UM** [#965](https://github.com/jaywedgeworth22/Usage-Monitor/issues/965): 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment)
- **UM** [#966](https://github.com/jaywedgeworth22/Usage-Monitor/issues/966): 2026-08-05 — Board hygiene final: closed 1 stale Active rows
- **UM** [#967](https://github.com/jaywedgeworth22/Usage-Monitor/issues/967): Receipt inbox addresses chosen 2026-07-27. Fallback
- **UM** [#968](https://github.com/jaywedgeworth22/Usage-Monitor/issues/968): iOS Overview: remove truncated “Budget is always this…” toolbar caption
- **UM** [#969](https://github.com/jaywedgeworth22/Usage-Monitor/issues/969): R2 free-tier 70% auto-shutoff fix (2026-08-03)
- **UM** [#970](https://github.com/jaywedgeworth22/Usage-Monitor/issues/970): Whole-app read-only audit (2026-08-01) — COMPLETED / CRITICAL INCIDENT
- **UM** [#971](https://github.com/jaywedgeworth22/Usage-Monitor/issues/971): Receipt inbox Worker + Email Routing (post-R2 bucket)
- **UM** [#972](https://github.com/jaywedgeworth22/Usage-Monitor/issues/972): [Uptime] Usage Monitor Oracle origin readiness failure
- **UM** [#977](https://github.com/jaywedgeworth22/Usage-Monitor/issues/977): Issue/effort hygiene + replica age align with 1h Litestream sync
- **UM** [#979](https://github.com/jaywedgeworth22/Usage-Monitor/issues/979): Issue/effort hygiene + replica age align with 1h Litestream sync
- **UM** [#980](https://github.com/jaywedgeworth22/Usage-Monitor/issues/980): Overview money UX: global budget, projected breakdown, quiet stale, ROIC
- **UM** [#981](https://github.com/jaywedgeworth22/Usage-Monitor/issues/981): Receipt inbox Worker + Email Routing (post-R2 bucket)
- **UM** [#990](https://github.com/jaywedgeworth22/Usage-Monitor/issues/990): Install replica-status probe + R2 kill reason (2026-08-05) — IN PR. SSH
- **UM** [#992](https://github.com/jaywedgeworth22/Usage-Monitor/issues/992): Fix auto-deploy race when main advances mid-build (2026-08-05) — IN PR
- **UM** [#1003](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1003): Orange brand + segmented History control + uncrowded nav (2026-08-05)
- **UM** [#1005](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1005): Orange brand + segmented History control + uncrowded nav (2026-08-05)
- **UM** [#1006](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1006): R2 fleet ST/CT pushover-parity card + iOS inline titles (2026-08-05)
- **UM** [#1011](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1011): iOS app icons: clean orange ring + Local full-width LOCAL stripe (no

### Effort board

- **UM** `Grok` Hide internal project-budgets system provider from Connections UI (2026-08-05) — IN PR. Filter list/detail APIs; block edit/delete/activate; keep alert FK carrier + self-heal isActive=false. Features unchanged
- **UM** `Grok` Local seed truth + swipe-delete confirm (2026-08-05) — IN PR. Seed no longer invents Vercel/CF/Robinhood fees; bootstrap scrubs known ghosts; swipe→Delete→confirm on Local providers + remote Settings inventories. Branch `grok/local-seed-truth-swipe-delete`
- **UM** `Grok` Full historical provider coverage both apps — Voyage/Oracle/Hetzner + complete Local catalog (2026-08-05) — IN PR. Local: all 42 defs + extras, Hetzner poll, seed historical shells; remote Hetzner MTD via #998; Voyage blind/sub both; Oracle cash remote-only; research dual-app matrix
- **UM** `Grok` Full historical catalog + Hetzner MTD estimate + Voyage/Oracle truth (2026-08-05) — IN PR. Local: all 42 defs + historical; Hetzner poll on Local; remote Hetzner pro-rates catalog run-rate into totalCost; research notes Voyage still no API, Oracle cash on remote only
- **UM** `Grok` Billing API coverage research (LLMs + partial providers) (2026-08-05) — IN PR. Hard dig: Render OpenAPI has no invoice paths; xAI has invoice list API; consumer Max/Plus/SuperGrok console-only; matrix in docs/research/2026-08-05-billing-api-coverage.md
- **UM** `Grok` Local Usage Monitor fleet provider catalog + poll adapters (2026-08-05) — IN PR. Catalog of ~40 fleet providers; poll: OpenRouter/OpenAI/DeepSeek/Anthropic Admin; seed templates; searchable Add Provider UI
- **UM** `Grok` Rename Local app → LocalUsageMonitor / Local Usage Monitor / services.jays.local.usage.monitor (2026-08-05) — IN PR. Target, scheme, display name, bundle ID, app group, deep link, Keychain service
- **UM** `Grok` iOS dual-app identity: distinct name/icon so Local doesn't look like remote (2026-08-05) — IN PR #982. Teal LOCAL icon, home-screen "UM Local", PRODUCT_NAME split, on-device banner; docs how to install both side-by-side
- **UM** `Grok` R2 fleet metrics (3 apps) + calm backup readiness (2026-08-05) — MERGED PR #975. Ops card for ST/CT/UM free-tier; backup no longer gates `/api/ready` ok; litestream sync 1h. Branch `grok/r2-fleet-metrics-and-backup-calm`
- **UM** `Grok` Orange brand + segmented History control + uncrowded nav (2026-08-05) — MERGED PR #999 / squash `5fc6316c`. Favicon-matched ` — um-accent` #f97316; History chips (24h/7d/30d/90d + More); Display menu; login restored; primary CTAs orange. Auto-deploy will pick up on main
- **UM** `Grok` Production recovery after deploy cutover gap (2026-08-05) — DEPLOYED / LIVE VERIFIED. Origin returned Caddy 502 while host auto-deploy cutover ran `9acf9951`→`08be8a96` (writer stopped during SQLite cutover + cold start ~3m). Receipt `status=deployed` at 2026-08-05T02:52:49Z; public `/api/health` + `/api/ready?strict=1` ok at exact `08be8a96` (db/scheduler/backup/startup green)
- **UM** `Grok` Wire web design tokens into Tailwind + primary chrome (2026-08-05) — MERGED PR #939. Squash `7d070031`. Deduped ` — um-` CSS vars, bridged accent/radius into Tailwind, adopted `bg-accent` / `accent-soft` on Nav, empty states, command palette, Money/Alerts CTAs. CI green (verify/gitleaks/CodeQL); auto-merge squash landed
- **UM** `Grok` iOS app icons: clean orange ring + Local full-width LOCAL stripe (no phone) (2026-08-05) — IN PROGRESS. Remove broken off-center nubs on remote orange mark; Local drops tiny phone, large LOCAL on full bottom white stripe. Branch `grok/ios-appicon-local-stripe`
- **UM** `Grok` R2 fleet ST/CT pushover-parity card + iOS inline titles (2026-08-05) — IN PR #984. Fleet card status/source/limits/top buckets; iOS tab roots `.inline` title; empty SF Symbol guards. Branch `grok/r2-fleet-ios-chrome`
- **UM** `Grok` Orange brand + segmented History control + uncrowded nav (2026-08-05) — IN PR #999. Favicon-matched ` — um-accent` #f97316; History chips (24h/7d/30d/90d + More); Display menu; login restored; primary CTAs orange. Branch `grok/brand-orange-nav-ui`
- **UM** `Grok` Fix auto-deploy race when main advances mid-build (2026-08-05) — IN PR. ensure_mirror no longer requires origin/main tip == selected SHA; fetch exact SHA + ancestor check. Unblocks deploys failing after long BuildKit cache work while concurrent merges land
- **UM** `Grok` Install replica-status probe + R2 kill reason (2026-08-05) — IN PR. SSH to Oracle `ubuntu@141.148.182.224`: installed probe/timer with 10800s budget. R2 free-tier kill flag present since 06:04Z (no litestream process; LTX stopped). Probe now short-circuits kill flag as `r2_free_tier_disabled` and app passes probe reason through; reinstall after merge
- **UM** `Grok` Issue/effort hygiene + replica age align with 1h Litestream sync (2026-08-05) — MERGED PR #976. Closed #974 (would revert #975); closed #952/#971; #972 auto-closed. Replica max-age 3600→10800s; service name usage-monitor; iOS checklist omits backup gate
- **UM** `Grok` Overview money UX: global budget, projected breakdown, quiet stale, ROIC builtin (2026-08-05) — MERGED PR #949. Branch `grok/overview-budget-projection-ux`. Global Budget set-from-hero; projected click → renewals+usage breakdown; suppress stale_snapshot nags; ROIC blind provider seed; known renewals include one-term next bill
- **UM** `Grok` 2026-08-05 — COMPLETED — Board hygiene (cross-app Issues alignment). CT/ST/UM effort boards reconciled; open Issues = real WIP only
- **UM** `Grok` 2026-08-05 — Board hygiene final: closed 1 stale Active rows (merged/abandoned/superseded)
- **UM** `Grok` iOS Overview: remove truncated “Budget is always this…” toolbar caption (2026-08-05) — IN PROGRESS. Branch `grok/ios-drop-budget-always-caption`. Drop unhelpful faint disclaimer under month picker; keep accessibility hint

## 2026-08-04

*100 PRs merged · 40 issues opened · 11 issues closed · 8 effort rows*

### Merged PRs

- **CT** [#1265](https://github.com/jaywedgeworth22/Congress.Trade/pull/1265): build(deps): bump @google/genai from 2.14.0 to 2.15.0 in /app _(by dependabot[bot])_
- **CT** [#1266](https://github.com/jaywedgeworth22/Congress.Trade/pull/1266): build(deps): bump @aws-sdk/client-s3 from 3.1098.0 to 3.1101.0 in /app _(by dependabot[bot])_
- **CT** [#1302](https://github.com/jaywedgeworth22/Congress.Trade/pull/1302): feat(analytics): dual member performance vs S&P on politician detail _(by jaywedgeworth22)_
- **CT** [#1305](https://github.com/jaywedgeworth22/Congress.Trade/pull/1305): fix(ops): batch price loader commits to cut R2 Class A burn _(by jaywedgeworth22)_
- **CT** [#1306](https://github.com/jaywedgeworth22/Congress.Trade/pull/1306): fix(latency): only score concurrent races for lead/win stats _(by jaywedgeworth22)_
- **CT** [#1309](https://github.com/jaywedgeworth22/Congress.Trade/pull/1309): fix(extraction): require distinct models, not providers, for agreement _(by jaywedgeworth22)_
- **CT** [#1311](https://github.com/jaywedgeworth22/Congress.Trade/pull/1311): feat(latency): thorough scoreboard — concurrent density + transparency _(by jaywedgeworth22)_
- **CT** `Grok` [#1314](https://github.com/jaywedgeworth22/Congress.Trade/pull/1314): feat(vision): replace kimi-cli with OpenRouter — vision _(by jaywedgeworth22)_
- **CT** [#1315](https://github.com/jaywedgeworth22/Congress.Trade/pull/1315): feat: Relax latency scoreboard gates to 14-day window & 2-match preliminary threshold _(by jaywedgeworth22)_
- **CT** [#1318](https://github.com/jaywedgeworth22/Congress.Trade/pull/1318): feat: Set disclosure latency probe interval to 1 minute _(by jaywedgeworth22)_
- **CT** `Grok` [#1319](https://github.com/jaywedgeworth22/Congress.Trade/pull/1319): feat(vision): primary local — CLI via xAI subscription _(by jaywedgeworth22)_
- **CT** [#1320](https://github.com/jaywedgeworth22/Congress.Trade/pull/1320): fix(latency): denser match + first_seen heal for concurrent races _(by jaywedgeworth22)_
- **CT** [#1322](https://github.com/jaywedgeworth22/Congress.Trade/pull/1322): fix(latency): stop inventing CT-ahead heals from pre-window stamps _(by jaywedgeworth22)_
- **CT** [#1323](https://github.com/jaywedgeworth22/Congress.Trade/pull/1323): fix(latency): repair CT-ahead floor heal artifacts _(by jaywedgeworth22)_
- **CT** [#1324](https://github.com/jaywedgeworth22/Congress.Trade/pull/1324): feat: Achieve 100% parity between iOS Trends view and Web dashboard _(by jaywedgeworth22)_
- **CT** [#1327](https://github.com/jaywedgeworth22/Congress.Trade/pull/1327): fix: Bundle ZillaSlab custom fonts in Xcode target and set clean light eagle app icon _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1328](https://github.com/jaywedgeworth22/Congress.Trade/pull/1328): app icon and zilla font fix _(by jaywedgeworth22)_
- **CT** [#1329](https://github.com/jaywedgeworth22/Congress.Trade/pull/1329): fix(ux): P0 web + iOS review fixes _(by jaywedgeworth22)_
- **CT** [#1330](https://github.com/jaywedgeworth22/Congress.Trade/pull/1330): UI cleanup: clean transaction tags, asset names, and performance metrics _(by jaywedgeworth22)_
- **CT** [#1337](https://github.com/jaywedgeworth22/Congress.Trade/pull/1337): fix(ui): improve green SAVE badge contrast and header Upgrade CTA alignment _(by jaywedgeworth22)_
- **CT** [#1339](https://github.com/jaywedgeworth22/Congress.Trade/pull/1339): feat(ui): default light theme with Light/Dark/System control _(by jaywedgeworth22)_
- **CT** [#1340](https://github.com/jaywedgeworth22/Congress.Trade/pull/1340): feat: Buy/Sell/Exchange product labels; B buy alias _(by jaywedgeworth22)_
- **CT** [#1342](https://github.com/jaywedgeworth22/Congress.Trade/pull/1342): feat(ux): Premium CSV + web product + iOS wave2 _(by jaywedgeworth22)_
- **CT** [#1344](https://github.com/jaywedgeworth22/Congress.Trade/pull/1344): feat: store buys as B; auto-translate Purchase/P on ingest _(by jaywedgeworth22)_
- **CT** [#1345](https://github.com/jaywedgeworth22/Congress.Trade/pull/1345): feat(billing): $5/$50 + 30d trial, delivery edit, Apple IAP _(by jaywedgeworth22)_
- **CT** [#1348](https://github.com/jaywedgeworth22/Congress.Trade/pull/1348): feat(ios): agent TestFlight ship path without Xcode UI _(by jaywedgeworth22)_
- **CT** [#1349](https://github.com/jaywedgeworth22/Congress.Trade/pull/1349): fix(brand): restore exact owner-provided eagle app icon (no redesigns) _(by jaywedgeworth22)_
- **CT** [#1351](https://github.com/jaywedgeworth22/Congress.Trade/pull/1351): ci: auto-enable squash auto-merge for congress-trading-shared PRs _(by jaywedgeworth22)_
- **CT** [#1352](https://github.com/jaywedgeworth22/Congress.Trade/pull/1352): fix: Queues, Latency metrics, UI copy fixes _(by jaywedgeworth22)_
- **ST** [#2367](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2367): build(deps): bump @sentry/nextjs from 10.68.0 to 10.69.0 in the observability group _(by dependabot[bot])_
- **ST** [#2368](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2368): build(deps-dev): bump @playwright/test from 1.62.0 to 1.62.1 in the testing group _(by dependabot[bot])_
- **ST** [#2369](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2369): build(deps): bump jose from 6.2.3 to 6.2.5 _(by dependabot[bot])_
- **ST** [#2370](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2370): build(deps-dev): bump @types/react from 19.2.17 to 19.2.18 _(by dependabot[bot])_
- **ST** [#2371](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2371): build(deps): bump better-sqlite3 from 12.11.1 to 13.0.2 _(by dependabot[bot])_
- **ST** [#2375](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2375): fix(mobile): make account.activate immediate so iOS Use no longer hangs _(by jaywedgeworth22)_
- **ST** `Grok` [#2381](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2381): feat(history): ROIC.ai OHLC cascade on ST (CT peer-only) _(by jaywedgeworth22)_
- **ST** [#2383](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2383): feat(rag): add OpenRouter classifier enrichment to vector-db embed+rerank paths _(by jaywedgeworth22)_
- **ST** `Grok` [#2384](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2384): fix(docker): slim image so Coolify deploys stop timing out _(by jaywedgeworth22)_
- **ST** `Grok` [#2386](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2386): fix(docker): keep docs/benchmarks for model-stats build _(by jaywedgeworth22)_
- **ST** [#2387](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2387): fix(test): update reasoning capability test assertions for o1 model family _(by jaywedgeworth22)_
- **ST** `Grok` [#2388](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2388): fix(docker): drop recursive chown (Coolify 30m budget) _(by jaywedgeworth22)_
- **ST** `Grok` [#2389](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2389): fix(docker): USER root so Coolify prod-start can write data dir _(by jaywedgeworth22)_
- **ST** `Grok` [#2390](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2390): fix(docker): drop scripts/eval so Next typecheck passes in image _(by jaywedgeworth22)_
- **ST** `Grok` [#2391](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2391): fix(docker): rebuild better-sqlite3 for bookworm glibc _(by jaywedgeworth22)_
- **ST** `Grok` [#2392](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2392): fix(docker): rebuild better-sqlite3 after prune (GLIBC) _(by jaywedgeworth22)_
- **ST** `Grok` [#2393](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2393): fix(docker): force node-gyp rebuild of better-sqlite3 after prune _(by jaywedgeworth22)_
- **ST** `Grok` [#2395](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2395): fix(learning): treat paper-account trades as first-class evidence _(by jaywedgeworth22)_
- **ST** [#2397](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2397): fix(test): update reasoning capability test assertions for o1 model family _(by jaywedgeworth22)_
- **ST** [#2398](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2398): fix(data): never call FMP/Quiver/UW; use Congress.Trade _(by jaywedgeworth22)_
- **ST** [#2399](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2399): fix(test): update reasoning capability test assertions for o1 model family _(by jaywedgeworth22)_
- **ST** [#2400](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2400): docs: UX improvement program sequenced PR plan (PR-0) _(by jaywedgeworth22)_
- **ST** [#2410](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2410): docs: claim UX program RESTART implementer blitz _(by jaywedgeworth22)_
- **ST** [#2411](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2411): ux(A4+A5): collapse Advanced rulebook; PWA Proposals noun _(by jaywedgeworth22)_
- **ST** [#2413](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2413): feat(console): plain-language nav labels (UX PR-B1) _(by jaywedgeworth22)_
- **ST** [#2414](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2414): feat(console): UX A2 approval card density + sticky CTAs _(by jaywedgeworth22)_
- **ST** [#2417](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2417): feat(console): UX A3 first-run readiness checklist hero _(by jaywedgeworth22)_
- **ST** [#2418](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2418): feat(strategy): UX A1 honest run skip statuses in UI _(by jaywedgeworth22)_
- **ST** [#2423](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2423): perf(console): UX Wave C speed (cache, P&L, scan virtuoso, memo) _(by jaywedgeworth22)_
- **ST** [#2424](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2424): feat(ios,mobile): UX Wave D mobile/iOS/PWA parity _(by jaywedgeworth22)_
- **ST** [#2425](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2425): feat(console): UX Wave B IA — plain nav, Autonomy panel, Settings TOC _(by jaywedgeworth22)_
- **ST** [#2426](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2426): feat(console): UX B3 Strategy structure + E polish _(by jaywedgeworth22)_
- **ST** [#2429](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2429): feat(congress): prefer filing-date member skill from CT dual performance _(by jaywedgeworth22)_
- **ST** [#2431](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2431): fix(congress): dual member performance skill scores (Wave D follow-up) _(by jaywedgeworth22)_
- **ST** `Grok` [#2433](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2433): fix(quotes): stop accepting ~15m delayed feeds as cascade-fresh _(by jaywedgeworth22)_
- **ST** [#2435](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2435): fix(ios): rename Coach tab to Insights _(by jaywedgeworth22)_
- **ST** [#2438](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2438): fix(test): update reasoning capability test assertions for o1 model family _(by jaywedgeworth22)_
- **ST** [#2442](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2442): feat(ios): agent TestFlight ship path without Xcode UI _(by jaywedgeworth22)_
- **ST** `Grok` [#2444](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2444): feat(broker): auto-pause strategy when orders cannot be placed _(by jaywedgeworth22)_
- **ST** [#2447](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2447): ci: auto-enable squash auto-merge for congress-trading-shared PRs _(by jaywedgeworth22)_
- **ST** [#2448](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2448): docs: UX program Waves A–E complete _(by jaywedgeworth22)_
- **ST** [#2449](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2449): docs: mark UX program design status Waves A–E complete _(by jaywedgeworth22)_
- **ST** [#2450](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2450): fix(ux): single primary Run once + expert panel quick wins (PR-A6) _(by jaywedgeworth22)_
- **UM** [#904](https://github.com/jaywedgeworth22/Usage-Monitor/pull/904): chore(deps): bump the npm-minor-and-patch group with 6 updates _(by dependabot[bot])_
- **UM** [#908](https://github.com/jaywedgeworth22/Usage-Monitor/pull/908): chore(deps): bump next from 15.5.21 to 16.2.12 _(by dependabot[bot])_
- **UM** [#919](https://github.com/jaywedgeworth22/Usage-Monitor/pull/919): docs: effort log for global-api-keys provider account fill _(by jaywedgeworth22)_
- **UM** [#923](https://github.com/jaywedgeworth22/Usage-Monitor/pull/923): feat(receipt-inbox): accept any @receipts.jays.services address _(by jaywedgeworth22)_
- **UM** [#925](https://github.com/jaywedgeworth22/Usage-Monitor/pull/925): fix(deploy): raise production SQLite integrity preflight timeouts to 900s _(by jaywedgeworth22)_
- **UM** [#927](https://github.com/jaywedgeworth22/Usage-Monitor/pull/927): fix(openrouter): prefer management/admin key for generation verification _(by jaywedgeworth22)_
- **UM** [#928](https://github.com/jaywedgeworth22/Usage-Monitor/pull/928): feat: settings management UI (web & iOS) and APNs native push notifications _(by jaywedgeworth22)_
- **UM** [#929](https://github.com/jaywedgeworth22/Usage-Monitor/pull/929): docs: mirror effort log for settings & APNs push completion (#928) _(by jaywedgeworth22)_
- **UM** [#930](https://github.com/jaywedgeworth22/Usage-Monitor/pull/930): fix(deploy): R2 kill-switch acceptance + cutover resilience gates _(by jaywedgeworth22)_
- **UM** [#931](https://github.com/jaywedgeworth22/Usage-Monitor/pull/931): fix(deploy): stop auto-deploy repair churn under R2 kill switch _(by jaywedgeworth22)_
- **UM** [#932](https://github.com/jaywedgeworth22/Usage-Monitor/pull/932): docs(effort): mark PR queue + deploy resilience complete on prod _(by jaywedgeworth22)_
- **UM** [#934](https://github.com/jaywedgeworth22/Usage-Monitor/pull/934): feat(ux): full web + iOS product polish from top-to-bottom review _(by jaywedgeworth22)_
- **UM** [#935](https://github.com/jaywedgeworth22/Usage-Monitor/pull/935): fix(r2): disaster-recovery backups + hard 70% free-tier policy _(by jaywedgeworth22)_
- **UM** [#936](https://github.com/jaywedgeworth22/Usage-Monitor/pull/936): feat(ux): wave-2 nav pages, charts, mobile cards, iOS intelligence _(by jaywedgeworth22)_
- **UM** [#937](https://github.com/jaywedgeworth22/Usage-Monitor/pull/937): fix(r2): live S3 storage meter; never kill on stale GraphQL _(by jaywedgeworth22)_
- **UM** [#938](https://github.com/jaywedgeworth22/Usage-Monitor/pull/938): fix(ios): repair widget Face ID redaction compile break _(by jaywedgeworth22)_
- **UM** [#939](https://github.com/jaywedgeworth22/Usage-Monitor/pull/939): feat(ux): wire design tokens into Tailwind + primary chrome _(by jaywedgeworth22)_
- **UM** [#940](https://github.com/jaywedgeworth22/Usage-Monitor/pull/940): docs: effort board closeout for design-token PR #939 _(by jaywedgeworth22)_
- **UM** [#941](https://github.com/jaywedgeworth22/Usage-Monitor/pull/941): docs: mark UX improvements deployed (088763fd) _(by jaywedgeworth22)_
- **UM** [#942](https://github.com/jaywedgeworth22/Usage-Monitor/pull/942): feat(ios): dual apps — remote client + Usage Monitor Local _(by jaywedgeworth22)_
- **UM** [#943](https://github.com/jaywedgeworth22/Usage-Monitor/pull/943): feat(ios): agent TestFlight ship path + Release archive fixes _(by jaywedgeworth22)_
- **UM** [#944](https://github.com/jaywedgeworth22/Usage-Monitor/pull/944): fix(ios): drop truncated Overview timeframe disclaimer _(by jaywedgeworth22)_
- **UM** [#945](https://github.com/jaywedgeworth22/Usage-Monitor/pull/945): ci: auto-enable squash auto-merge for congress-trading-shared PRs _(by jaywedgeworth22)_
- **UM** [#946](https://github.com/jaywedgeworth22/Usage-Monitor/pull/946): feat(ios): Usage Monitor Local Milestone A (on-device data plane) _(by jaywedgeworth22)_
- **UM** [#947](https://github.com/jaywedgeworth22/Usage-Monitor/pull/947): docs: mark Local Milestone A #946 merged on effort board _(by jaywedgeworth22)_
- **UM** [#948](https://github.com/jaywedgeworth22/Usage-Monitor/pull/948): docs(effort): close merged issue mirrors + prod recovery note _(by jaywedgeworth22)_
- **shared** [#258](https://github.com/jaywedgeworth22/congress-trading-shared/pull/258): feat(api): dual-anchor member performance (filingDate + tradeDate) _(by jaywedgeworth22)_
- **shared** [#259](https://github.com/jaywedgeworth22/congress-trading-shared/pull/259): ci: auto-enable squash auto-merge on all PRs _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1341](https://github.com/jaywedgeworth22/Congress.Trade/issues/1341): 2026-08-04T23:58Z — IN PROGRESS — Product labels Buy/Sell/Exchange (B
- **CT** [#1343](https://github.com/jaywedgeworth22/Congress.Trade/issues/1343): 2026-08-04 — IN PROGRESS — UX wave2 WEB lane. Branch grok/ux-wave2-web
- **CT** [#1347](https://github.com/jaywedgeworth22/Congress.Trade/issues/1347): 2026-08-05T01:02Z — IN PROGRESS — Canonical txtype B (Buy) storage
- **ST** [#2458](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2458): UX improvement program Waves A–E — COMPLETED 2026-08-05
- **UM** [#824](https://github.com/jaywedgeworth22/Usage-Monitor/issues/824): Blank dashboard skeleton on mobile+desktop (2026-07-27) — IN PROGRESS
- **UM** [#899](https://github.com/jaywedgeworth22/Usage-Monitor/issues/899): [Uptime] Usage Monitor production is stale vs main
- **UM** [#914](https://github.com/jaywedgeworth22/Usage-Monitor/issues/914): R2 free-tier 70% auto-shutoff fix (2026-08-03)
- **UM** [#922](https://github.com/jaywedgeworth22/Usage-Monitor/issues/922): Docs: R2 primary (not Garage) + R2 free-tier spike
- **UM** [#924](https://github.com/jaywedgeworth22/Usage-Monitor/issues/924): Coolify agents rewire + OpenRouter CT + receipt domain intake + legacy
- **UM** [#926](https://github.com/jaywedgeworth22/Usage-Monitor/issues/926): Deploy preflight SQLite integrity timeout 120→900s (2026-08-04) — IN
- **UM** [#933](https://github.com/jaywedgeworth22/Usage-Monitor/issues/933): [Uptime] Usage Monitor Oracle origin readiness failure

### Issues opened

- **CT** [#1307](https://github.com/jaywedgeworth22/Congress.Trade/issues/1307): 2026-08-04 — COMPLETED + DEPLOYED — Member drawer dual performance vs
- **CT** [#1308](https://github.com/jaywedgeworth22/Congress.Trade/issues/1308): [2026-08-04] R2 Class A hygiene (loader batch + litestream 5m + storage
- **CT** [#1313](https://github.com/jaywedgeworth22/Congress.Trade/issues/1313): 2026-08-04 — COMPLETED — Latency thorough overhaul (agreement candidate
- **CT** [#1316](https://github.com/jaywedgeworth22/Congress.Trade/issues/1316): 2026-08-04 — COMPLETED — Latency scoreboard thoroughness (#1311)
- **CT** [#1317](https://github.com/jaywedgeworth22/Congress.Trade/issues/1317): 2026-08-04 — COMPLETED — Latency scoreboard thoroughness. Concurrent
- **CT** [#1325](https://github.com/jaywedgeworth22/Congress.Trade/issues/1325): 2026-08-04 — COMPLETED — Latency match density (#1320 + #1322)
- **CT** [#1326](https://github.com/jaywedgeworth22/Congress.Trade/issues/1326): 2026-08-04 — COMPLETED — Latency match density. Find more real
- **CT** [#1331](https://github.com/jaywedgeworth22/Congress.Trade/issues/1331): 2026-08-04 — COMPLETED — UX P0 review fixes (web+iOS). PR #1329 merged
- **CT** [#1332](https://github.com/jaywedgeworth22/Congress.Trade/issues/1332): 2026-08-04 — COMPLETED + DEPLOYED — Resolve all open PRs → production
- **CT** [#1333](https://github.com/jaywedgeworth22/Congress.Trade/issues/1333): 2026-08-04 — COMPLETED (code) / PARTIAL (data density) — Latency probe &
- **CT** [#1334](https://github.com/jaywedgeworth22/Congress.Trade/issues/1334): 2026-08-03 — Prices from App B only + ST bulk load + DLQ clear. Owner
- **CT** [#1335](https://github.com/jaywedgeworth22/Congress.Trade/issues/1335): 2026-08-03 — KIMI takeover (max-plan cap mid-flight) — OPS COMPLETE
- **CT** [#1336](https://github.com/jaywedgeworth22/Congress.Trade/issues/1336): 2026-08-04 — COMPLETED + DEPLOYED — Executive feed hygiene (PR #1287
- **CT** [#1338](https://github.com/jaywedgeworth22/Congress.Trade/issues/1338): 2026-08-04 — COMPLETED — Fix SAVE badge contrast & top-right CTA button
- **CT** [#1341](https://github.com/jaywedgeworth22/Congress.Trade/issues/1341): 2026-08-04T23:58Z — IN PROGRESS — Product labels Buy/Sell/Exchange (B
- **CT** [#1343](https://github.com/jaywedgeworth22/Congress.Trade/issues/1343): 2026-08-04 — IN PROGRESS — UX wave2 WEB lane. Branch grok/ux-wave2-web
- **CT** [#1347](https://github.com/jaywedgeworth22/Congress.Trade/issues/1347): 2026-08-05T01:02Z — IN PROGRESS — Canonical txtype B (Buy) storage
- **CT** [#1353](https://github.com/jaywedgeworth22/Congress.Trade/issues/1353): 2026-08-05T02:28Z — COMPLETED + DEPLOYED — Queues, Latency metrics, UI
- **CT** [#1354](https://github.com/jaywedgeworth22/Congress.Trade/issues/1354): 2026-08-05T01:19Z — COMPLETED — UX Trends & Trades Filter Parity, Header
- **CT** [#1355](https://github.com/jaywedgeworth22/Congress.Trade/issues/1355): 2026-08-05 — COMPLETED + DEPLOYED — Pricing $5/$50 + 30d trial, delivery
- **CT** [#1356](https://github.com/jaywedgeworth22/Congress.Trade/issues/1356): 2026-08-05T01:45Z — COMPLETED + DEPLOYED — Canonical txtype B (Buy)
- **CT** [#1357](https://github.com/jaywedgeworth22/Congress.Trade/issues/1357): 2026-08-04 — COMPLETED — UX wave2 Premium CSV + product + iOS. PR #1342
- **CT** [#1358](https://github.com/jaywedgeworth22/Congress.Trade/issues/1358): 2026-08-04 — COMPLETED — UX wave2 integrate PR. Branch
- **CT** [#1359](https://github.com/jaywedgeworth22/Congress.Trade/issues/1359): 2026-08-04 — COMPLETED (sub-lane) — UX wave2 WEB. Branch
- **CT** [#1360](https://github.com/jaywedgeworth22/Congress.Trade/issues/1360): 2026-08-04 — COMPLETED (sub-lane) — Premium CSV API gate verify. Branch
- **CT** [#1361](https://github.com/jaywedgeworth22/Congress.Trade/issues/1361): 2026-08-05T00:20Z — COMPLETED + DEPLOYED — Product labels
- **CT** [#1362](https://github.com/jaywedgeworth22/Congress.Trade/issues/1362): 2026-08-04 — COMPLETED — UX wave2 RESTART (agent team). Branch
- **CT** [#1363](https://github.com/jaywedgeworth22/Congress.Trade/issues/1363): 2026-08-04 — COMPLETED (sub-lane) — Premium CSV UI. Branch
- **CT** [#1364](https://github.com/jaywedgeworth22/Congress.Trade/issues/1364): 2026-08-04 — COMPLETED (branch pushed, no PR) — UX wave2 iOS lane
- **CT** [#1365](https://github.com/jaywedgeworth22/Congress.Trade/issues/1365): 2026-08-04 — COMPLETED — UX wave2 agent team. Branch
- **CT** [#1366](https://github.com/jaywedgeworth22/Congress.Trade/issues/1366): 2026-08-04 — COMPLETED — UX wave2: Premium CSV + review improvements
- **ST** [#2412](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2412): UX program RESTART implementer blitz — IN PROGRESS
- **ST** [#2437](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2437): Quote cascade freshness + stale→limit never block — IN
- **ST** [#2452](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2452): UX PR-A1 honest run skip statuses in UI — IN PR
- **ST** [#2454](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2454): UX Wave B IA — COMPLETED 2026-08-05 (PR #2425 / B1
- **ST** [#2455](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2455): UX Wave C speed — COMPLETED 2026-08-05 (PR #2423) (C1
- **ST** [#2458](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2458): UX improvement program Waves A–E — COMPLETED 2026-08-05
- **UM** [#924](https://github.com/jaywedgeworth22/Usage-Monitor/issues/924): Coolify agents rewire + OpenRouter CT + receipt domain intake + legacy
- **UM** [#926](https://github.com/jaywedgeworth22/Usage-Monitor/issues/926): Deploy preflight SQLite integrity timeout 120→900s (2026-08-04) — IN
- **UM** [#933](https://github.com/jaywedgeworth22/Usage-Monitor/issues/933): [Uptime] Usage Monitor Oracle origin readiness failure

### Effort board

- **UM** `Grok` Local Milestone A implementation (2026-08-04) — MERGED PR #946. Shipped SQLiteLocalStore (design DDL), Keychain, OpenRouter adapter, BudgetEngine+materializer, full Local UI. Sim BUILD SUCCEEDED. Branch grok/usage-monitor-local-milestone-a
- **UM** `Grok` Dual iOS apps: UsageMonitor (live sync) + UsageMonitorLocal (on-device) (2026-08-04) — IN PR #942. Separate app target/scheme/bundle/app group; LocalStore+LocalDataPlane scaffold; Local sim build green. Owner keeps remote client; Local for phone-only App Store path
- **UM** `Grok` iOS TestFlight agent ship pipeline (cross-app) — IN PR 2026-08-04 (ST #2442 / CT #1348 / UM #943); IPA export verified; upload blocked on ASC API key handoff 2026-08-04. Fleet script + per-repo wrappers so agents can archive/sign/upload without Xcode UI. Bundle IDs: trade.socratic.app / trade.congress.ios / services.jays.usage.monitor. Team CC8UTF7ATG. Branch grok/ios-testflight-ship. N
- **UM** `Grok` Design: mobile full-parity + phone self-host topology (2026-08-04) — COMPLETE (phone-only pivot approved). Product answer: native Swift data plane ON the phone (local SQLite/GRDB, Keychain keys, opportunistic poll). Not phone→remote host. Public App Store target. Doc: `docs/designs/2026-08-04-mobile-parity-and-phone-self-host.md`. Review rounds closed 0 open
- **UM** `Grok` UX deferred wave 2 (wizard/mobile cards/nav/charts/iOS depth) (2026-08-04) — COMPLETED + DEPLOYED (2026-08-05). Live production `088763fd` includes #934/#936 UX, #938 widget privacy, #939 design tokens. `/api/health` + `/api/ready?strict=1` green; dashboard routes redirect-auth as expected
- **UM** `Grok` Full web+iOS UX overhaul (review execution) (2026-08-04) — COMPLETED + DEPLOYED (2026-08-05). Live on production `088763fd` with full UX recommendation set (hero, attention, density/PWA, nav routes, palette, charts, wizard, iOS intelligence/widget privacy, design tokens)
- **UM** `Grok` Land open PR queue + deploy host patches to production (2026-08-04) — COMPLETE / PROD ON MAIN. Prior queue cleared (#919/#904/#908/#925/#929; closed majors #905/#906/#907). Residual: host-only deploy patches → landed PR #930 (R2 kill-switch acceptance, pre-stop LTX, curl -sS ready, 5400s build, image re-verify) + PR #931 (poller repair-churn under kill switch). Infisical
- **UM** `Grok` Deploy preflight SQLite integrity timeout 120→900s (2026-08-04) — MERGED PR #925. `preflight_current_production` integrity_check + foreign_key_check timeouts 120→900s; die_host retained; comment on ~800MB+ load. CI green; squash-merged

## 2026-08-03

*39 PRs merged · 15 issues opened · 4 issues closed · 0 effort rows*

### Merged PRs

- **CT** [#1267](https://github.com/jaywedgeworth22/Congress.Trade/pull/1267): feat: Ingestion pipeline improvements _(by jaywedgeworth22)_
- **CT** [#1273](https://github.com/jaywedgeworth22/Congress.Trade/pull/1273): docs: scanned-backlog local-vision rollout + effort-log mirror [KIMI] _(by jaywedgeworth22)_
- **CT** [#1274](https://github.com/jaywedgeworth22/Congress.Trade/pull/1274): feat(vision-worker): real extraction engine via local kimi-cli vision [KIMI] _(by jaywedgeworth22)_
- **CT** [#1277](https://github.com/jaywedgeworth22/Congress.Trade/pull/1277): feat(scan-cpu-worker): server CPU scanned PTR path (no Mac, no LLM) _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1278](https://github.com/jaywedgeworth22/Congress.Trade/pull/1278): fix(brand): update app icon to clean eagle with money bag (no ring, no S T letters) _(by jaywedgeworth22)_
- **CT** [#1280](https://github.com/jaywedgeworth22/Congress.Trade/pull/1280): Migrate local dev services to pm2 _(by jaywedgeworth22)_
- **CT** [#1283](https://github.com/jaywedgeworth22/Congress.Trade/pull/1283): fix(ui): default H/S/P filters selected, fix header logo, align filter chips, and format company names _(by jaywedgeworth22)_
- **CT** [#1284](https://github.com/jaywedgeworth22/Congress.Trade/pull/1284): fix: nested SQLite txn + textPdf conf floor (review queue) _(by jaywedgeworth22)_
- **CT** [#1286](https://github.com/jaywedgeworth22/Congress.Trade/pull/1286): docs: review queue closeout (effort log) _(by jaywedgeworth22)_
- **CT** [#1287](https://github.com/jaywedgeworth22/Congress.Trade/pull/1287): fix(exec): competitor orphans, PAS OGE, notes→asset, EXEC identity _(by jaywedgeworth22)_
- **CT** `Grok` [#1288](https://github.com/jaywedgeworth22/Congress.Trade/pull/1288): feat(prices): sole price source = Socratic.Trade / App B _(by jaywedgeworth22)_
- **CT** [#1289](https://github.com/jaywedgeworth22/Congress.Trade/pull/1289): fix(identity): map Rohit Khanna → Ro Khanna and merge filer forks _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1291](https://github.com/jaywedgeworth22/Congress.Trade/pull/1291): fix(ui): clean dark logo wordmark letters and remove white block artifact _(by jaywedgeworth22)_
- **CT** [#1292](https://github.com/jaywedgeworth22/Congress.Trade/pull/1292): docs: closeout Rohit→Ro Khanna identity merge _(by jaywedgeworth22)_
- **CT** `Grok` [#1298](https://github.com/jaywedgeworth22/Congress.Trade/pull/1298): docs(ops): R2 free-tier litestream opt (60s/36h host) _(by jaywedgeworth22)_
- **CT** [#1299](https://github.com/jaywedgeworth22/Congress.Trade/pull/1299): fix(latency): exact-hash join match + scoreboard/iOS honesty gates _(by jaywedgeworth22)_
- **CT** [#1301](https://github.com/jaywedgeworth22/Congress.Trade/pull/1301): fix(latency): scoreboard window honesty + backfill stamps _(by jaywedgeworth22)_
- **ST** [#2363](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2363): feat(db): migration v65 — created_at indexes for retention pruning [KIMI] _(by jaywedgeworth22)_
- **ST** [#2364](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2364): docs(rollout): storage hygiene execution + security disclosure _(by jaywedgeworth22)_
- **ST** [#2365](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2365): Data-cascade Round 2/3: 6 new free providers + Yahoo/AV/Finnhub hardening _(by jaywedgeworth22)_
- **ST** `Claude` [#2366](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2366): mobile PWA: accounts section, realtime approval feedback, de-emphasized delete (owner feedback 2026-08-02) _(by jaywedgeworth22)_
- **ST** `Claude` [#2372](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2372): mobile PWA: accounts section, realtime approval feedback, de-emphasized delete (owner feedback 2026-08-02) _(by jaywedgeworth22)_
- **ST** `Claude` [#2373](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2373): mobile PWA: accounts section, realtime approval feedback, de-emphasized delete (owner feedback 2026-08-02) _(by jaywedgeworth22)_
- **ST** `Claude` [#2374](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2374): mobile PWA: accounts section, realtime approval feedback, de-emphasized delete (owner feedback 2026-08-02) _(by jaywedgeworth22)_
- **ST** `Claude` [#2376](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2376): mobile PWA: accounts section, realtime approval feedback, de-emphasized delete (owner feedback 2026-08-02) _(by jaywedgeworth22)_
- **ST** [#2377](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2377): fix(console): stop dashboard white-screen on partial latestScan topCandidates _(by jaywedgeworth22)_
- **ST** `Claude` [#2378](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2378): mobile PWA: accounts section, realtime approval feedback, de-emphasized delete (owner feedback 2026-08-02) _(by jaywedgeworth22)_
- **ST** `Grok` [#2379](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2379): ops(r2): kill-switch resume + Class A throttle ( ←KIMI takeover) _(by jaywedgeworth22)_
- **ST** [#2380](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2380): feat(rag): add OpenRouter classifier enrichment to vector-db embed+rerank paths _(by jaywedgeworth22)_
- **ST** `Grok` [#2382](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2382): ops(r2): free-tier litestream 60s/24h _(by jaywedgeworth22)_
- **UM** [#875](https://github.com/jaywedgeworth22/Usage-Monitor/pull/875): chore(deps): bump github/codeql-action/analyze from 4.37.0 to 4.37.3 _(by dependabot[bot])_
- **UM** [#909](https://github.com/jaywedgeworth22/Usage-Monitor/pull/909): feat(ios): update app category to Developer Tools and display name to Usage Monitor _(by jaywedgeworth22)_
- **UM** [#910](https://github.com/jaywedgeworth22/Usage-Monitor/pull/910): feat: calendar month/year timeframe picker (web + iOS) _(by jaywedgeworth22)_
- **UM** [#911](https://github.com/jaywedgeworth22/Usage-Monitor/pull/911): fix(r2): enforce free-tier shutoff from real GraphQL metrics _(by jaywedgeworth22)_
- **UM** [#913](https://github.com/jaywedgeworth22/Usage-Monitor/pull/913): docs(effort): mark R2 free-tier shutoff PR #911 merged _(by jaywedgeworth22)_
- **UM** `Grok` [#915](https://github.com/jaywedgeworth22/Usage-Monitor/pull/915): ops(r2): free-tier 48h retention + 60s sync _(by jaywedgeworth22)_
- **UM** [#916](https://github.com/jaywedgeworth22/Usage-Monitor/pull/916): docs: production Litestream target is Cloudflare R2, not Garage _(by jaywedgeworth22)_
- **UM** [#917](https://github.com/jaywedgeworth22/Usage-Monitor/pull/917): fix(r2): free-tier prune, 48h retention, UM-owned kill-switch alerts _(by jaywedgeworth22)_
- **UM** [#920](https://github.com/jaywedgeworth22/Usage-Monitor/pull/920): feat: Pushover alert delivery channel, email disable flag, and stale snapshot severity downgrade _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1272](https://github.com/jaywedgeworth22/Congress.Trade/issues/1272): [2026-08-02] Improvement Wave: Web Deep Links, Meta/Social Unfurls, and iOS
- **UM** [#912](https://github.com/jaywedgeworth22/Usage-Monitor/issues/912): R2 free-tier 70% auto-shutoff fix (2026-08-03) — IN
- **UM** [#918](https://github.com/jaywedgeworth22/Usage-Monitor/issues/918): Docs: R2 primary (not Garage) + R2 free-tier spike
- **UM** [#921](https://github.com/jaywedgeworth22/Usage-Monitor/issues/921): Add missing provider accounts from global-api-keys.env (2026-08-03)

### Issues opened

- **CT** [#1268](https://github.com/jaywedgeworth22/Congress.Trade/issues/1268): [2026-08-03] Pipeline Robustification (M3 / R3) — COMPLETED. Implemented
- **CT** [#1269](https://github.com/jaywedgeworth22/Congress.Trade/issues/1269): [2026-08-03] Local Vision Worker & Bounded Wait State (M1 / R1)
- **CT** [#1270](https://github.com/jaywedgeworth22/Congress.Trade/issues/1270): [2026-08-03] Data Integrity & Deduplication (M4 / R4) — COMPLETED
- **CT** [#1271](https://github.com/jaywedgeworth22/Congress.Trade/issues/1271): [2026-08-03] Deterministic House PTR Extraction (M2 / R2) — COMPLETED
- **CT** [#1272](https://github.com/jaywedgeworth22/Congress.Trade/issues/1272): [2026-08-02] Improvement Wave: Web Deep Links, Meta/Social Unfurls, and iOS
- **CT** [#1281](https://github.com/jaywedgeworth22/Congress.Trade/issues/1281): [2026-08-03] Clean app icon update (no ring, no S T letters) — MERGED PR
- **CT** [#1282](https://github.com/jaywedgeworth22/Congress.Trade/issues/1282): [2026-08-03] Dark mode brand logo wordmark recoloring — MERGED PR #1275
- **CT** [#1293](https://github.com/jaywedgeworth22/Congress.Trade/issues/1293): [2026-08-03] Clean Dark Logo Wordmark & Artifact Removal — MERGED PR #1291
- **CT** [#1294](https://github.com/jaywedgeworth22/Congress.Trade/issues/1294): 2026-08-03 — COMPLETED + DEPLOYED — Rohit Khanna → Ro Khanna member
- **CT** [#1296](https://github.com/jaywedgeworth22/Congress.Trade/issues/1296): 2026-08-03 — COMPLETED + DEPLOYED — Review queue clear + nested SQLite
- **UM** [#912](https://github.com/jaywedgeworth22/Usage-Monitor/issues/912): R2 free-tier 70% auto-shutoff fix (2026-08-03) — IN
- **UM** [#914](https://github.com/jaywedgeworth22/Usage-Monitor/issues/914): R2 free-tier 70% auto-shutoff fix (2026-08-03)
- **UM** [#918](https://github.com/jaywedgeworth22/Usage-Monitor/issues/918): Docs: R2 primary (not Garage) + R2 free-tier spike
- **UM** [#921](https://github.com/jaywedgeworth22/Usage-Monitor/issues/921): Add missing provider accounts from global-api-keys.env (2026-08-03)
- **UM** [#922](https://github.com/jaywedgeworth22/Usage-Monitor/issues/922): Docs: R2 primary (not Garage) + R2 free-tier spike

## 2026-08-02

*44 PRs merged · 12 issues opened · 8 issues closed · 0 effort rows*

### Merged PRs

- **CT** [#1227](https://github.com/jaywedgeworth22/Congress.Trade/pull/1227): fix(sse): close streams gracefully at the deadline instead of aborting _(by jaywedgeworth22)_
- **CT** `Claude` `Cursor` [#1238](https://github.com/jaywedgeworth22/Congress.Trade/pull/1238): fix(deploy+db): revision receipt, three migrate hazards, and the — trigger gap _(by jaywedgeworth22)_
- **CT** `Claude` [#1243](https://github.com/jaywedgeworth22/Congress.Trade/pull/1243): test(migrations): fail when a migration never reaches production _(by jaywedgeworth22)_
- **CT** `Claude` [#1244](https://github.com/jaywedgeworth22/Congress.Trade/pull/1244): fix(deploy): drop build.args from compose — it breaks Coolify deploys _(by jaywedgeworth22)_
- **CT** [#1245](https://github.com/jaywedgeworth22/Congress.Trade/pull/1245): fix(admin): retry migration statements on SQLITE_BUSY and support ALLOW_UNKNOWN_BUILD_SHA _(by jaywedgeworth22)_
- **CT** [#1246](https://github.com/jaywedgeworth22/Congress.Trade/pull/1246): fix(security): exclude sensitive KV prefixes from SQLite and purge leaked tokens (P1-2) _(by jaywedgeworth22)_
- **CT** [#1247](https://github.com/jaywedgeworth22/Congress.Trade/pull/1247): feat(health): add deep pipeline health monitoring and 403 provider classification (P0-2) _(by jaywedgeworth22)_
- **CT** [#1248](https://github.com/jaywedgeworth22/Congress.Trade/pull/1248): fix(ui): dynamic MAX_PUBLIC_FEED_OFFSET and free CSV export hints (P1-8) _(by jaywedgeworth22)_
- **CT** [#1249](https://github.com/jaywedgeworth22/Congress.Trade/pull/1249): fix(jobs): durable queue and outbox retention sweep with indexes (P1-17) _(by jaywedgeworth22)_
- **CT** [#1250](https://github.com/jaywedgeworth22/Congress.Trade/pull/1250): fix(ios): 1024x1024 RGB app icon and PushNotificationManager symbol fixes (P0-6, P0-7) _(by jaywedgeworth22)_
- **CT** `Codex` [#1251](https://github.com/jaywedgeworth22/Congress.Trade/pull/1251): docs: update effort log for completed — audit remediation _(by jaywedgeworth22)_
- **CT** `Claude` [#1262](https://github.com/jaywedgeworth22/Congress.Trade/pull/1262): docs(handoff): cross-app audit resolution record _(by jaywedgeworth22)_
- **CT** [#1263](https://github.com/jaywedgeworth22/Congress.Trade/pull/1263): fix(ios): APNs token persistence & backend sync wiring (#1048) _(by jaywedgeworth22)_
- **CT** [#1264](https://github.com/jaywedgeworth22/Congress.Trade/pull/1264): fix(ios): App Category to Finance & Display Name to Congress.Trade _(by jaywedgeworth22)_
- **ST** [#2338](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2338): chore(litestream): retention 48h — measured growth math for guaranteed free-tier fit [KIMI] _(by jaywedgeworth22)_
- **ST** [#2347](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2347): fix(peer-reads): skip the App A read-back tier when serving App A itself _(by jaywedgeworth22)_
- **ST** [#2349](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2349): build(npm): committish-free allowScripts key (npm-12-proof); correct EALLOWSCRIPTS root-cause record _(by jaywedgeworth22)_
- **ST** [#2350](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2350): feat(console): /console/connections route-local skeleton instead of full-screen loader (finding 22 residual) _(by jaywedgeworth22)_
- **ST** `Claude` [#2351](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2351): mobile PWA: accounts section, realtime approval feedback, de-emphasized delete (owner feedback 2026-08-02) _(by jaywedgeworth22)_
- **ST** [#2352](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2352): feat(broker): declarative per-broker order-type constraint validation at the placement choke point (§7 slice 2) _(by jaywedgeworth22)_
- **ST** [#2353](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2353): Data-cascade: weekend-freshness Stage 1/2 + provider hardening Round 1 + FMP test fix _(by jaywedgeworth22)_
- **ST** [#2354](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2354): feat(broker): per-account broker-mutation lease — §7 slice 3 PR-1 (risk lanes + backstop) _(by jaywedgeworth22)_
- **ST** [#2356](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2356): fix(audit): write-hygiene — dedupe skip spam, bound run payloads, retention prune [KIMI] _(by jaywedgeworth22)_
- **ST** [#2358](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2358): docs(handoff): R2 resume go/no-go receipts + prod-wedge incident state _(by jaywedgeworth22)_
- **ST** `Claude` [#2359](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2359): mobile PWA: accounts section, realtime approval feedback, de-emphasized delete (owner feedback 2026-08-02) _(by jaywedgeworth22)_
- **ST** [#2360](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2360): fix(perf): defuse the market-scan-freshness prod wedge — index, stamp probes, boot grace, scan deadline, knob backoff _(by jaywedgeworth22)_
- **ST** [#2361](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2361): feat(broker): strategy/approval placement windows under the account mutation lease — §7 slice 3 PR-2 (completes slice 3) _(by jaywedgeworth22)_
- **ST** `Claude` [#2362](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2362): fix(prod): exit-0 outage — pid1 signal re-raise + npm signal black hole; boot supervisor + exit-code contract _(by jaywedgeworth22)_
- **UM** [#873](https://github.com/jaywedgeworth22/Usage-Monitor/pull/873): chore(deps): bump actions/checkout from 7.0.0 to 7.0.1 _(by dependabot[bot])_
- **UM** [#874](https://github.com/jaywedgeworth22/Usage-Monitor/pull/874): chore(deps): bump actions/setup-python from 6.3.0 to 7.0.0 _(by dependabot[bot])_
- **UM** [#877](https://github.com/jaywedgeworth22/Usage-Monitor/pull/877): feat(readiness): detect unlinked, missing, and replaced SQLite database files in /api/ready _(by jaywedgeworth22)_
- **UM** [#878](https://github.com/jaywedgeworth22/Usage-Monitor/pull/878): sec(web): bounded request bodies, input validation, and CSRF origin checks _(by jaywedgeworth22)_
- **UM** [#881](https://github.com/jaywedgeworth22/Usage-Monitor/pull/881): fix(telemetry): bound occurredAt queries to now and limit ingest future clock skew (P1) _(by jaywedgeworth22)_
- **UM** [#883](https://github.com/jaywedgeworth22/Usage-Monitor/pull/883): fix(ingest): fold status snapshot creation into ingest transaction and round totalRequests (P2) _(by jaywedgeworth22)_
- **UM** [#893](https://github.com/jaywedgeworth22/Usage-Monitor/pull/893): fix(r2-usage): create temp files safely (CodeQL js/insecure-temporary-file) _(by jaywedgeworth22)_
- **UM** [#894](https://github.com/jaywedgeworth22/Usage-Monitor/pull/894): ci/ops: full documented gate in CI, sustained release-drift alerting, raw-telemetry boundary docs _(by jaywedgeworth22)_
- **UM** `Claude` [#895](https://github.com/jaywedgeworth22/Usage-Monitor/pull/895): fix(ui): contrast tokens in table/cards and 503 guard on — cost-check _(by jaywedgeworth22)_
- **UM** [#896](https://github.com/jaywedgeworth22/Usage-Monitor/pull/896): fix(ios): remove unused Networking target dependency from PushScaffold _(by jaywedgeworth22)_
- **UM** [#897](https://github.com/jaywedgeworth22/Usage-Monitor/pull/897): fix(ingest): rate-limit ordering and per-event sourceApp validation in OTLP metrics _(by jaywedgeworth22)_
- **UM** `Claude` [#898](https://github.com/jaywedgeworth22/Usage-Monitor/pull/898): docs: final update to effort log for — audit remediation closeout _(by jaywedgeworth22)_
- **UM** [#900](https://github.com/jaywedgeworth22/Usage-Monitor/pull/900): fix(ingest): real cumulative negative-adjustment bounds and pre-authoritative replay dedupe _(by jaywedgeworth22)_
- **UM** [#901](https://github.com/jaywedgeworth22/Usage-Monitor/pull/901): fix(a11y): AA-compliant muted text, status GRAY badge, and the missing ux-a11y component tests _(by jaywedgeworth22)_
- **UM** [#902](https://github.com/jaywedgeworth22/Usage-Monitor/pull/902): docs: sync effort-log mirror for audit-remediation completion _(by jaywedgeworth22)_
- **UM** [#903](https://github.com/jaywedgeworth22/Usage-Monitor/pull/903): ci: measured coverage gate with ratcheted thresholds and lcov artifact _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1254](https://github.com/jaywedgeworth22/Congress.Trade/issues/1254): [2026-08-02] — audit remediation — COMPLETED (ALL 10 P0/P1 ITEMS LANDED
- **CT** [#1255](https://github.com/jaywedgeworth22/Congress.Trade/issues/1255): [2026-07-29] Graceful handling and inline messaging for unconfigured Google
- **CT** [#1256](https://github.com/jaywedgeworth22/Congress.Trade/issues/1256): [2026-07-29] Add Source Health & Error Frequency Timeline Graphic to Admin
- **CT** [#1257](https://github.com/jaywedgeworth22/Congress.Trade/issues/1257): [2026-07-29][KIMI] Implement open-source-lessons backlog — COMPLETED (4/4
- **CT** [#1258](https://github.com/jaywedgeworth22/Congress.Trade/issues/1258): [2026-07-29] Competitor latency analysis (7-day QQ/UW comparison) +
- **CT** [#1259](https://github.com/jaywedgeworth22/Congress.Trade/issues/1259): [2026-07-28] Resolve all open PRs (#1112, #1096) and land fixes — MERGED PR
- **CT** [#1260](https://github.com/jaywedgeworth22/Congress.Trade/issues/1260): [2026-07-28] Double site side buffers/margins and card/section spacing
- **CT** [#1261](https://github.com/jaywedgeworth22/Congress.Trade/issues/1261): [2026-08-01] Read-only whole-app improvement audit — REPORT DELIVERED

### Issues opened

- **CT** [#1252](https://github.com/jaywedgeworth22/Congress.Trade/issues/1252): [2026-07-31] Price-needs export — DEPLOYED via PR #1193 (73cac4ed). Live
- **CT** [#1253](https://github.com/jaywedgeworth22/Congress.Trade/issues/1253): [2026-07-30][KIMI] Unblock PR merges (Actions outage) + Deno retirement
- **CT** [#1254](https://github.com/jaywedgeworth22/Congress.Trade/issues/1254): [2026-08-02] — audit remediation — COMPLETED (ALL 10 P0/P1 ITEMS LANDED
- **CT** [#1255](https://github.com/jaywedgeworth22/Congress.Trade/issues/1255): [2026-07-29] Graceful handling and inline messaging for unconfigured Google
- **CT** [#1256](https://github.com/jaywedgeworth22/Congress.Trade/issues/1256): [2026-07-29] Add Source Health & Error Frequency Timeline Graphic to Admin
- **CT** [#1257](https://github.com/jaywedgeworth22/Congress.Trade/issues/1257): [2026-07-29][KIMI] Implement open-source-lessons backlog — COMPLETED (4/4
- **CT** [#1258](https://github.com/jaywedgeworth22/Congress.Trade/issues/1258): [2026-07-29] Competitor latency analysis (7-day QQ/UW comparison) +
- **CT** [#1259](https://github.com/jaywedgeworth22/Congress.Trade/issues/1259): [2026-07-28] Resolve all open PRs (#1112, #1096) and land fixes — MERGED PR
- **CT** [#1260](https://github.com/jaywedgeworth22/Congress.Trade/issues/1260): [2026-07-28] Double site side buffers/margins and card/section spacing
- **CT** [#1261](https://github.com/jaywedgeworth22/Congress.Trade/issues/1261): [2026-08-01] Read-only whole-app improvement audit — REPORT DELIVERED
- **ST** [#2357](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2357): [2026-08-01] Peer reads: skip App A echo tier — landing. The token-gated
- **UM** [#899](https://github.com/jaywedgeworth22/Usage-Monitor/issues/899): [Uptime] Usage Monitor production is stale vs main

## 2026-08-01

*54 PRs merged · 5 issues opened · 7 issues closed · 0 effort rows*

### Merged PRs

- **CT** [#1215](https://github.com/jaywedgeworth22/Congress.Trade/pull/1215): security: purge live secrets from app/.prod.vars _(by jaywedgeworth22)_
- **CT** [#1216](https://github.com/jaywedgeworth22/Congress.Trade/pull/1216): Durable failed-job requeue for extraction catch-up _(by jaywedgeworth22)_
- **CT** [#1217](https://github.com/jaywedgeworth22/Congress.Trade/pull/1217): Fix main-red: scrubbed KNOWN_PROJECT_IDS duplicate keys (TS1117) _(by jaywedgeworth22)_
- **CT** [#1218](https://github.com/jaywedgeworth22/Congress.Trade/pull/1218): feat(enrichment): FMP_ENRICHMENT_ENABLED gate (default off) — FMP keys latency-only _(by jaywedgeworth22)_
- **CT** [#1219](https://github.com/jaywedgeworth22/Congress.Trade/pull/1219): feat(cron): CT_TICK_DEADLINE_MS override for tick deadline _(by jaywedgeworth22)_
- **CT** [#1220](https://github.com/jaywedgeworth22/Congress.Trade/pull/1220): Fix requeue intra-batch duplicate dedupe violation _(by jaywedgeworth22)_
- **CT** [#1221](https://github.com/jaywedgeworth22/Congress.Trade/pull/1221): docs(board): fmp-latency-only closeout _(by jaywedgeworth22)_
- **CT** `Claude` [#1222](https://github.com/jaywedgeworth22/Congress.Trade/pull/1222): fix(ui): repair regex escapes eaten by the dashboard template literal _(by jaywedgeworth22)_
- **CT** [#1223](https://github.com/jaywedgeworth22/Congress.Trade/pull/1223): fix(ingest): retry transient fetch 403/404 + dual-stage ingest-retry-errored [KIMI] _(by jaywedgeworth22)_
- **CT** `Claude` [#1224](https://github.com/jaywedgeworth22/Congress.Trade/pull/1224): Handoff: cross-app integration audit (paused by owner) _(by jaywedgeworth22)_
- **CT** [#1226](https://github.com/jaywedgeworth22/Congress.Trade/pull/1226): docs: rollout note + effort-log mirror for #1223 [KIMI] _(by jaywedgeworth22)_
- **CT** [#1228](https://github.com/jaywedgeworth22/Congress.Trade/pull/1228): fix(security): trust X-Forwarded-Proto for Secure cookies + HSTS (P0-3) _(by jaywedgeworth22)_
- **CT** [#1229](https://github.com/jaywedgeworth22/Congress.Trade/pull/1229): fix(docker): fail closed on sqlite-web auth and remove hardcoded password literals (P1-3) _(by jaywedgeworth22)_
- **CT** [#1230](https://github.com/jaywedgeworth22/Congress.Trade/pull/1230): fix(admin): fail POST /migrate on unhandled SQL errors or schema readiness failure (P1-4) _(by jaywedgeworth22)_
- **CT** [#1231](https://github.com/jaywedgeworth22/Congress.Trade/pull/1231): fix(ci): repair broken workflows auto-update-prs and shared-package-pin-check (P1-9) _(by jaywedgeworth22)_
- **CT** [#1232](https://github.com/jaywedgeworth22/Congress.Trade/pull/1232): fix(db): enforce sequence-authoritative cursor_seq and repair poisoned cursors (P0-1) _(by jaywedgeworth22)_
- **CT** [#1233](https://github.com/jaywedgeworth22/Congress.Trade/pull/1233): fix(client): enforce one-time secret claim for command-issued credentials (P1-1) _(by jaywedgeworth22)_
- **CT** [#1234](https://github.com/jaywedgeworth22/Congress.Trade/pull/1234): fix: telemetry and budget gate fixes _(by jaywedgeworth22)_
- **CT** `Claude` [#1235](https://github.com/jaywedgeworth22/Congress.Trade/pull/1235): docs(effort-log): update effort log for completed — audit remediation tasks _(by jaywedgeworth22)_
- **CT** [#1237](https://github.com/jaywedgeworth22/Congress.Trade/pull/1237): fix(monitor): remove INGEST_TOKEN fallback trap in monitorBudgetGate _(by jaywedgeworth22)_
- **CT** `Claude` [#1239](https://github.com/jaywedgeworth22/Congress.Trade/pull/1239): docs(effort-log): cross-app audit closeout _(by jaywedgeworth22)_
- **ST** [#2326](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2326): fix(r2-usage): per-metric alert basis — storage absolute, ops pace floored [KIMI] _(by jaywedgeworth22)_
- **ST** [#2327](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2327): feat(tuning): time-bounded (PIT) proposal evidence — cut tuner evidence at the OOS fold start (§6 follow-up) _(by jaywedgeworth22)_
- **ST** [#2330](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2330): docs(r2): alert-basis verification addendum _(by jaywedgeworth22)_
- **ST** [#2331](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2331): fix(macro,regime): keyless VIX cascade + suppress Unknown-side regime flaps _(by jaywedgeworth22)_
- **ST** [#2332](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2332): feat(r2-usage): monitor all three Cloudflare accounts' R2 free tiers [KIMI] _(by jaywedgeworth22)_
- **ST** [#2333](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2333): Expose portfolio fetch errors in UI to fix hidden fallback _(by jaywedgeworth22)_
- **ST** [#2334](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2334): chore(litestream): snapshot retention 720h → 168h (R2 free-tier headroom) [KIMI] _(by jaywedgeworth22)_
- **ST** [#2335](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2335): feat(broker): per-broker order-status conformance tables — oss-lessons §7 slice 1 [KIMI] _(by jaywedgeworth22)_
- **ST** `Claude` [#2337](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2337): feat: complete 's cross-app audit tasks _(by jaywedgeworth22)_
- **ST** [#2339](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2339): docs(rollout): per-app R2 backup consolidation _(by jaywedgeworth22)_
- **ST** [#2340](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2340): build: bump congress-trading-shared to v2.4.0 _(by jaywedgeworth22)_
- **ST** `Codex` [#2341](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2341): feat(audit): — external-review remediation Wave 1 & 2 (30 findings) _(by jaywedgeworth22)_
- **ST** [#2342](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2342): feat: meter OHLC cascade and rate limit peer reads _(by jaywedgeworth22)_
- **ST** [#2343](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2343): feat: push all screener refs in nightly share _(by jaywedgeworth22)_
- **ST** [#2344](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2344): build: bump congress-trading-shared to v2.4.1 _(by jaywedgeworth22)_
- **ST** [#2345](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2345): build: restore allowScripts + regenerate lockfile for shared v2.4.1 _(by jaywedgeworth22)_
- **ST** [#2348](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2348): docs(deploy): webhook-secret repair receipts, verified end-to-end; STATUS de-spliced; stale Coolify uuid fixed _(by jaywedgeworth22)_
- **UM** [#869](https://github.com/jaywedgeworth22/Usage-Monitor/pull/869): feat(litestream): update backup target to Cloudflare R2 and normalize AWS_ secret names _(by jaywedgeworth22)_
- **UM** [#870](https://github.com/jaywedgeworth22/Usage-Monitor/pull/870): feat(r2-usage): add daily Pushover updates & 70% free tier emergency kill-switch _(by jaywedgeworth22)_
- **UM** [#871](https://github.com/jaywedgeworth22/Usage-Monitor/pull/871): docs: flag Oracle production deploy stall on effort board _(by jaywedgeworth22)_
- **UM** [#876](https://github.com/jaywedgeworth22/Usage-Monitor/pull/876): build: bump congress-trading-shared to v2.4.0 _(by jaywedgeworth22)_
- **UM** [#879](https://github.com/jaywedgeworth22/Usage-Monitor/pull/879): ux(a11y): screen reader semantics, error boundary notices, and keyboard accessibility _(by jaywedgeworth22)_
- **UM** [#880](https://github.com/jaywedgeworth22/Usage-Monitor/pull/880): refactor(ios): push scaffold simplification and unit test suite _(by jaywedgeworth22)_
- **UM** [#882](https://github.com/jaywedgeworth22/Usage-Monitor/pull/882): fix(materializer): atomic writer-locked settlement and optimistic status/watermark revision predicate (P1) _(by jaywedgeworth22)_
- **UM** [#884](https://github.com/jaywedgeworth22/Usage-Monitor/pull/884): fix(ingest): aggregate batch and 30-day cumulative negative subscription adjustment limits (P2) _(by jaywedgeworth22)_
- **UM** [#885](https://github.com/jaywedgeworth22/Usage-Monitor/pull/885): fix(ingest): per-producer token scoping and isolated rate-limit buckets (P2) _(by jaywedgeworth22)_
- **UM** [#886](https://github.com/jaywedgeworth22/Usage-Monitor/pull/886): fix(project-resolver): resumable keyset sweep for unattributed events and dotted metadata matching (P2) _(by jaywedgeworth22)_
- **UM** [#887](https://github.com/jaywedgeworth22/Usage-Monitor/pull/887): fix(ingest): make top-level validated project field authoritative in metadata (P2) _(by jaywedgeworth22)_
- **UM** [#889](https://github.com/jaywedgeworth22/Usage-Monitor/pull/889): fix(projects): parse and validate Project creation and update payloads (P3) _(by jaywedgeworth22)_
- **UM** [#890](https://github.com/jaywedgeworth22/Usage-Monitor/pull/890): fix(providers): deduplicate allocation projectIds and cap array length (P3) _(by jaywedgeworth22)_
- **UM** `Claude` [#892](https://github.com/jaywedgeworth22/Usage-Monitor/pull/892): docs: update effort log for completed — audit remediation sweep _(by jaywedgeworth22)_
- **shared** [#256](https://github.com/jaywedgeworth22/congress-trading-shared/pull/256): feat: export strict CongressTradeEvent payload shapes _(by jaywedgeworth22)_
- **shared** `Antigravity` [#257](https://github.com/jaywedgeworth22/congress-trading-shared/pull/257): export congress trade event _(by jaywedgeworth22)_

### Issues closed

- **UM** [#844](https://github.com/jaywedgeworth22/Usage-Monitor/issues/844): [KIMI] Open-source lessons: LiteLLM pricing + — cost cross-check
- **UM** [#851](https://github.com/jaywedgeworth22/Usage-Monitor/issues/851): [KIMI] Ingest-time LiteLLM cost derivation, default-off flag (2026-07-29)
- **UM** [#855](https://github.com/jaywedgeworth22/Usage-Monitor/issues/855): Integrate Infisical project 'usage-monitor' scope & shared machine
- **UM** [#859](https://github.com/jaywedgeworth22/Usage-Monitor/issues/859): Infisical project usage-monitor prod populated (2026-07-30) — DONE. 76
- **UM** [#863](https://github.com/jaywedgeworth22/Usage-Monitor/issues/863): [KIMI] LLM burn windows — ccusage blocks generalized to all platforms
- **UM** [#868](https://github.com/jaywedgeworth22/Usage-Monitor/issues/868): iOS provider history time-range picker (parity with web 7/30/90/365d)
- **UM** [#872](https://github.com/jaywedgeworth22/Usage-Monitor/issues/872): [KIMI] FLAG: Oracle production deploy stalled since #858 Infisical merge

### Issues opened

- **ST** [#2328](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2328): [KIMI] Backtest-integrity §6 slice 3: qlib walk-forward window
- **ST** [#2329](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2329): [KIMI] Time-bounded (PIT) proposal evidence for the auto-tuner
- **ST** [#2336](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2336): Brokerage-model order-state hardening — PARTIALLY IMPLEMENTED
- **ST** [#2346](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2346): [2026-08-01] Repair PR #2344 (shared v2.4.1 bump) — landing. 's bump
- **UM** [#872](https://github.com/jaywedgeworth22/Usage-Monitor/issues/872): [KIMI] FLAG: Oracle production deploy stalled since #858 Infisical merge

## 2026-07-31

*36 PRs merged · 0 issues opened · 0 issues closed · 0 effort rows*

### Merged PRs

- **CT** [#1195](https://github.com/jaywedgeworth22/Congress.Trade/pull/1195): [kimi] prices: send bearer token to peer (App B) price reads _(by jaywedgeworth22)_
- **CT** [#1196](https://github.com/jaywedgeworth22/Congress.Trade/pull/1196): [kimi] prices: retry provider 429s; don't abort unmetered runs on 429 _(by jaywedgeworth22)_
- **CT** [#1197](https://github.com/jaywedgeworth22/Congress.Trade/pull/1197): [kimi] docs: rollout note — price pipeline restoration _(by jaywedgeworth22)_
- **CT** [#1198](https://github.com/jaywedgeworth22/Congress.Trade/pull/1198): fix(prices): point APP_B_IMPORT_URL at socratictrade.com (redirect strips bearer) _(by jaywedgeworth22)_
- **CT** [#1199](https://github.com/jaywedgeworth22/Congress.Trade/pull/1199): feat(ui): update site heading logo, eagle app icon, and remove live pill _(by jaywedgeworth22)_
- **CT** [#1200](https://github.com/jaywedgeworth22/Congress.Trade/pull/1200): Raise D1 row budget + daily R2 free-tier Pushover summary _(by jaywedgeworth22)_
- **CT** [#1201](https://github.com/jaywedgeworth22/Congress.Trade/pull/1201): feat(cron): staggered daily lane crons (fix 45s deadline starvation) _(by jaywedgeworth22)_
- **CT** [#1202](https://github.com/jaywedgeworth22/Congress.Trade/pull/1202): Effort log: 2026-07-31 closeout _(by jaywedgeworth22)_
- **CT** [#1203](https://github.com/jaywedgeworth22/Congress.Trade/pull/1203): fix(cron): invalid Deno.cron name crashes prod boot _(by jaywedgeworth22)_
- **CT** [#1204](https://github.com/jaywedgeworth22/Congress.Trade/pull/1204): docs(ops): cron-lane split rollout record _(by jaywedgeworth22)_
- **CT** [#1205](https://github.com/jaywedgeworth22/Congress.Trade/pull/1205): fix(ui): add ?v=2 cache busters for brand logo, icons, and webmanifest _(by jaywedgeworth22)_
- **CT** [#1206](https://github.com/jaywedgeworth22/Congress.Trade/pull/1206): fix(ui): inline % buys right of metric value, 100% white logo lettering with eagle gold aura in dark mode, and 18px toggle spacing on desktop _(by jaywedgeworth22)_
- **CT** [#1207](https://github.com/jaywedgeworth22/Congress.Trade/pull/1207): fix(auth,ui): resolve /auth/google/start redirect loop behind reverse proxy and add high quality star-badge eagle app icon _(by jaywedgeworth22)_
- **CT** [#1208](https://github.com/jaywedgeworth22/Congress.Trade/pull/1208): fix(auth): parse X-Forwarded-Host and Host headers in /auth/google/start to prevent infinite redirect loop behind reverse proxy _(by jaywedgeworth22)_
- **CT** [#1209](https://github.com/jaywedgeworth22/Congress.Trade/pull/1209): fix(auth): parse X-Forwarded-Host and Host headers in /auth/google/start to resolve proxy redirect loop _(by jaywedgeworth22)_
- **CT** [#1210](https://github.com/jaywedgeworth22/Congress.Trade/pull/1210): fix(deno): sanitize surrounding quotes from TURSO_DATABASE_URL to prevent LibsqlError _(by jaywedgeworth22)_
- **CT** [#1211](https://github.com/jaywedgeworth22/Congress.Trade/pull/1211): fix(deno): regex sanitize multiple surrounding quotes on TURSO_DATABASE_URL and TURSO_AUTH_TOKEN _(by jaywedgeworth22)_
- **CT** [#1212](https://github.com/jaywedgeworth22/Congress.Trade/pull/1212): perf(cron): time-sliced enrichment + hourly drain lane _(by jaywedgeworth22)_
- **CT** [#1213](https://github.com/jaywedgeworth22/Congress.Trade/pull/1213): docs(ops): enrichment-slicing rollout record _(by jaywedgeworth22)_
- **CT** [#1214](https://github.com/jaywedgeworth22/Congress.Trade/pull/1214): fix(cron): stringify lane result in log line _(by jaywedgeworth22)_
- **ST** [#2312](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2312): feat(ops): R2 free-tier usage monitor + unify LITESTREAM_S3_ → AWS_ secret names [KIMI] _(by jaywedgeworth22)_
- **ST** [#2313](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2313): fix(macro,regime): keyless VIX cascade + suppress Unknown-side regime flaps _(by jaywedgeworth22)_
- **ST** [#2314](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2314): [kimi] Token-gated EOD market-data read routes for congress.trade (cache-aside) _(by jaywedgeworth22)_
- **ST** [#2315](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2315): docs(r2): resolution addendum — replication verified, old keys deleted, monitor live _(by jaywedgeworth22)_
- **ST** [#2316](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2316): fix(ops): bind litestream IPC socket on writable DB volume _(by jaywedgeworth22)_
- **ST** [#2317](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2317): chore(ops): retire deleted Hetzner servers (ci-cpx32 + old prod box) _(by jaywedgeworth22)_
- **ST** [#2318](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2318): Expose portfolio fetch errors in UI to fix hidden fallback _(by jaywedgeworth22)_
- **ST** [#2319](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2319): feat(ops): daily R2 free-tier digest via notify (Pushover) [KIMI] _(by jaywedgeworth22)_
- **ST** [#2320](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2320): docs(rollout): notify channel server-env fix — SMS live, Pushover pending _(by jaywedgeworth22)_
- **ST** [#2321](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2321): feat(notify): per-user Pushover/Twilio credentials in user settings [KIMI] _(by jaywedgeworth22)_
- **ST** [#2322](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2322): docs(notify): per-user creds deployed, Twilio migrated to user settings _(by jaywedgeworth22)_
- **ST** [#2323](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2323): Expose portfolio fetch errors in UI to fix hidden fallback _(by jaywedgeworth22)_
- **ST** [#2324](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2324): Expose portfolio fetch errors in UI to fix hidden fallback _(by jaywedgeworth22)_
- **ST** [#2325](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2325): docs(rollout): Docker+containerd data-root migration to /data _(by jaywedgeworth22)_
- **fleet** [#3](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/3): feat(calendar): permanent fleet agent-activity ICS feed _(by jaywedgeworth22)_
- **fleet** [#4](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/4): chore(calendar): include Congress.Trade in ICS seed _(by jaywedgeworth22)_

## 2026-07-30

*31 PRs merged · 16 issues opened · 2 issues closed · 0 effort rows*

### Merged PRs

- **CT** [#1173](https://github.com/jaywedgeworth22/Congress.Trade/pull/1173): fix(sentry): add DEFAULT_SENTRY_DSN fallback to sentryOptions _(by jaywedgeworth22)_
- **CT** [#1174](https://github.com/jaywedgeworth22/Congress.Trade/pull/1174): docs: update AGENTS.md architecture to reflect Coolify deployment on Oracle host _(by jaywedgeworth22)_
- **CT** [#1175](https://github.com/jaywedgeworth22/Congress.Trade/pull/1175): chore(ci): remove obsolete deploy-deno.yml workflow and policy reference _(by jaywedgeworth22)_
- **CT** [#1180](https://github.com/jaywedgeworth22/Congress.Trade/pull/1180): fix(ingestion): exclude synthetic provider-missing placeholder rows from public feed and clear stale review queue items _(by jaywedgeworth22)_
- **CT** [#1181](https://github.com/jaywedgeworth22/Congress.Trade/pull/1181): fix(ui): resolve source document links for all trade rows in drawer _(by jaywedgeworth22)_
- **CT** [#1182](https://github.com/jaywedgeworth22/Congress.Trade/pull/1182): fix(container): default PORT=5000 in Dockerfile and main.ts to fix 502 Bad Gateway and enhance drawer source links _(by jaywedgeworth22)_
- **CT** [#1183](https://github.com/jaywedgeworth22/Congress.Trade/pull/1183): security(botDefense): reduce daily public row budget to 3,000 rows per IP _(by jaywedgeworth22)_
- **CT** [#1184](https://github.com/jaywedgeworth22/Congress.Trade/pull/1184): security(botDefense): lower max public offset to 2,000 and max page limit to 250 _(by jaywedgeworth22)_
- **CT** [#1185](https://github.com/jaywedgeworth22/Congress.Trade/pull/1185): chore: update deployment documentation and package.json scripts to reflect Coolify deployment _(by jaywedgeworth22)_
- **CT** [#1186](https://github.com/jaywedgeworth22/Congress.Trade/pull/1186): docs(ops): prod 502 incident closeout — Caddy stable-alias fix + findings _(by jaywedgeworth22)_
- **CT** [#1187](https://github.com/jaywedgeworth22/Congress.Trade/pull/1187): docs(ops): Turso→local SQLite cutover closeout _(by jaywedgeworth22)_
- **CT** [#1188](https://github.com/jaywedgeworth22/Congress.Trade/pull/1188): chore(deps): bump @google/genai from 2.13.0 to 2.14.0 in /app _(by dependabot[bot])_
- **CT** [#1189](https://github.com/jaywedgeworth22/Congress.Trade/pull/1189): chore(deps): bump @aws-sdk/client-s3 from 3.1097.0 to 3.1098.0 in /app _(by dependabot[bot])_
- **CT** [#1190](https://github.com/jaywedgeworth22/Congress.Trade/pull/1190): chore(deps): bump node-html-parser from 9.0.0 to 9.0.1 in /app _(by dependabot[bot])_
- **CT** [#1192](https://github.com/jaywedgeworth22/Congress.Trade/pull/1192): docs(ops): correct secret-resolution findings + R2 401 owner action _(by jaywedgeworth22)_
- **CT** [#1193](https://github.com/jaywedgeworth22/Congress.Trade/pull/1193): feat(export): price-needs for congressional S&P performance share _(by jaywedgeworth22)_
- **ST** [#2288](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2288): Expose portfolio fetch errors in UI to fix hidden fallback _(by jaywedgeworth22)_
- **ST** [#2289](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2289): docs(oss-lessons): record §5 zero-code finding + §8 implemented _(by jaywedgeworth22)_
- **ST** [#2294](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2294): feat(learning): rule significance testing — Jesse label-permutation baseline (oss-lessons §6 slice 1) _(by jaywedgeworth22)_
- **ST** [#2295](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2295): fix(ci): set NODE_OPTIONS=3072 on Playwright webServer to stop smoke OOM _(by jaywedgeworth22)_
- **ST** [#2296](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2296): docs(rollout): Oracle deploy-path repair — prod deploys restored _(by jaywedgeworth22)_
- **ST** [#2303](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2303): fix(ci): authenticate Playwright smoke via middleware local fallback _(by jaywedgeworth22)_
- **ST** [#2304](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2304): docs(rollout): auto-deploy restored end-to-end — webhook route+secret, ENOSPC, Caddy alias _(by jaywedgeworth22)_
- **ST** [#2305](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2305): feat(tuning): qlib walk-forward window report + in-sample disclosure on OOS gates (oss-lessons §6 slice 3) _(by jaywedgeworth22)_
- **ST** [#2310](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2310): feat(congress-share): deep-share App A price-needs for S&P performance _(by jaywedgeworth22)_
- **UM** [#858](https://github.com/jaywedgeworth22/Usage-Monitor/pull/858): feat(secrets): Infisical sole source of truth for Usage Monitor _(by jaywedgeworth22)_
- **UM** [#860](https://github.com/jaywedgeworth22/Usage-Monitor/pull/860): feat(analytics): LLM burn windows — ccusage 5h blocks generalized to all platforms _(by jaywedgeworth22)_
- **UM** [#862](https://github.com/jaywedgeworth22/Usage-Monitor/pull/862): docs: mark #860 merged in effort log _(by jaywedgeworth22)_
- **UM** [#864](https://github.com/jaywedgeworth22/Usage-Monitor/pull/864): feat(deploy): Infisical as sole source of truth for Oracle production runtime env _(by jaywedgeworth22)_
- **UM** [#865](https://github.com/jaywedgeworth22/Usage-Monitor/pull/865): feat(ios): provider history time-range picker (web parity) _(by jaywedgeworth22)_
- **UM** [#867](https://github.com/jaywedgeworth22/Usage-Monitor/pull/867): docs: mark iOS history range PR #865 as merged _(by jaywedgeworth22)_

### Issues closed

- **UM** [#861](https://github.com/jaywedgeworth22/Usage-Monitor/issues/861): [KIMI] LLM burn windows — ccusage blocks generalized to all platforms
- **UM** [#866](https://github.com/jaywedgeworth22/Usage-Monitor/issues/866): iOS provider history time-range picker (parity with web 7/30/90/365d)

### Issues opened

- **CT** [#1191](https://github.com/jaywedgeworth22/Congress.Trade/issues/1191): Uptime Alert: congress.trade health returned HTTP 502
- **ST** [#2290](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2290): [KIMI] OSS-lessons program: docs/oss-lessons.md + task brain
- **ST** [#2291](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2291): [KIMI] Generalized preview renderers for mutating operations
- **ST** [#2292](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2292): [KIMI] nofx-style consecutive-miss safety mode — In Progress
- **ST** [#2293](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2293): [Fleet] Shut down Oracle Actions runners; all repos GitHub-hosted CI
- **ST** [#2297](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2297): [KIMI] OSS-lessons program: docs/oss-lessons.md + task brain
- **ST** [#2298](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2298): [KIMI] Generalized preview renderers for mutating operations
- **ST** [#2301](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2301): [KIMI] nofx-style consecutive-miss safety mode
- **ST** [#2302](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2302): [KIMI] Generalized preview renderers for mutating operations
- **ST** [#2306](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2306): Backtest-integrity suite for the learning loop — PARTIALLY
- **ST** [#2307](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2307): [KIMI] Backtest-integrity §6 slice 1: rule significance testing
- **ST** [#2311](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2311): [2026-07-30] Share App A price-needs for congressional S&P performance
- **UM** [#861](https://github.com/jaywedgeworth22/Usage-Monitor/issues/861): [KIMI] LLM burn windows — ccusage blocks generalized to all platforms
- **UM** [#863](https://github.com/jaywedgeworth22/Usage-Monitor/issues/863): [KIMI] LLM burn windows — ccusage blocks generalized to all platforms
- **UM** [#866](https://github.com/jaywedgeworth22/Usage-Monitor/issues/866): iOS provider history time-range picker (parity with web 7/30/90/365d)
- **UM** [#868](https://github.com/jaywedgeworth22/Usage-Monitor/issues/868): iOS provider history time-range picker (parity with web 7/30/90/365d)

## 2026-07-29

*83 PRs merged · 13 issues opened · 9 issues closed · 0 effort rows*

### Merged PRs

- **CT** [#1115](https://github.com/jaywedgeworth22/Congress.Trade/pull/1115): feat: add sqlite-web for database monitoring _(by jaywedgeworth22)_
- **CT** [#1118](https://github.com/jaywedgeworth22/Congress.Trade/pull/1118): fix(docker): prepend sqlite_web to command _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1119](https://github.com/jaywedgeworth22/Congress.Trade/pull/1119): fix(docker): add allow-sys and custom arm64 sqlite-web _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1120](https://github.com/jaywedgeworth22/Congress.Trade/pull/1120): fix(docker): add unstable flags for KV/Cron in Deno _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1121](https://github.com/jaywedgeworth22/Congress.Trade/pull/1121): fix(ci): restore oracle-ci runner for deployment _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1122](https://github.com/jaywedgeworth22/Congress.Trade/pull/1122): fix(docker): connect containers to oracle_internal network for caddy _(by jaywedgeworth22)_
- **CT** [#1123](https://github.com/jaywedgeworth22/Congress.Trade/pull/1123): chore(deps): bump @aws-sdk/client-s3 from 3.1096.0 to 3.1097.0 in /app _(by dependabot[bot])_
- **CT** [#1124](https://github.com/jaywedgeworth22/Congress.Trade/pull/1124): docs: open-source lessons research note [KIMI] _(by jaywedgeworth22)_
- **CT** [#1125](https://github.com/jaywedgeworth22/Congress.Trade/pull/1125): docs: board closeout + standing merge directive [KIMI] _(by jaywedgeworth22)_
- **CT** [#1126](https://github.com/jaywedgeworth22/Congress.Trade/pull/1126): fix: review batch 1 — secrets, dark cron lanes, DLQ recovery, PDF 404, deploy profile [KIMI] _(by jaywedgeworth22)_
- **CT** [#1127](https://github.com/jaywedgeworth22/Congress.Trade/pull/1127): docs: rollout record for review fix batch 1 [KIMI] _(by jaywedgeworth22)_
- **CT** `Antigravity` [#1128](https://github.com/jaywedgeworth22/Congress.Trade/pull/1128): fix(ui,extraction): filter OCR junk dots and unparsed labels without LLM calls _(by jaywedgeworth22)_
- **CT** [#1129](https://github.com/jaywedgeworth22/Congress.Trade/pull/1129): feat(config): unconstrain default cost profile and daily call caps _(by jaywedgeworth22)_
- **CT** [#1130](https://github.com/jaywedgeworth22/Congress.Trade/pull/1130): feat: stored STOCK Act late-disclosure status + ?stockAct= feed filter [KIMI] _(by jaywedgeworth22)_
- **CT** [#1133](https://github.com/jaywedgeworth22/Congress.Trade/pull/1133): fix(brand): light cream app icon + transparent web logos _(by jaywedgeworth22)_
- **CT** [#1134](https://github.com/jaywedgeworth22/Congress.Trade/pull/1134): feat(ingestion): zero-config public residential proxy fallbacks for House live search _(by jaywedgeworth22)_
- **CT** [#1135](https://github.com/jaywedgeworth22/Congress.Trade/pull/1135): fix(ios): prevent All Time timeframe crash, display asset names, and fix trade sorting _(by jaywedgeworth22)_
- **CT** [#1136](https://github.com/jaywedgeworth22/Congress.Trade/pull/1136): feat: ?owner= first-class feed filter [KIMI] _(by jaywedgeworth22)_
- **CT** [#1137](https://github.com/jaywedgeworth22/Congress.Trade/pull/1137): feat: resolved Bioguide identity on filers + feed rows [KIMI] _(by jaywedgeworth22)_
- **CT** [#1138](https://github.com/jaywedgeworth22/Congress.Trade/pull/1138): docs: add Apache License 2.0 [KIMI] _(by jaywedgeworth22)_
- **CT** [#1139](https://github.com/jaywedgeworth22/Congress.Trade/pull/1139): feat: archive raw seed payloads to R2 before processing [KIMI] _(by jaywedgeworth22)_
- **CT** [#1140](https://github.com/jaywedgeworth22/Congress.Trade/pull/1140): docs: rollout record — history scrub + public/Apache [KIMI] _(by jaywedgeworth22)_
- **CT** [#1141](https://github.com/jaywedgeworth22/Congress.Trade/pull/1141): fix(extraction): strip dot-leaders and OCR artifacts from asset names _(by jaywedgeworth22)_
- **CT** [#1142](https://github.com/jaywedgeworth22/Congress.Trade/pull/1142): docs: open-source-lessons results + effort-board closeout [KIMI] _(by jaywedgeworth22)_
- **CT** [#1150](https://github.com/jaywedgeworth22/Congress.Trade/pull/1150): ci: GitHub-hosted only; Oracle Actions runners retired _(by jaywedgeworth22)_
- **CT** [#1152](https://github.com/jaywedgeworth22/Congress.Trade/pull/1152): feat(admin): add source health & error frequency timeline graphic with stats cards _(by jaywedgeworth22)_
- **CT** [#1153](https://github.com/jaywedgeworth22/Congress.Trade/pull/1153): feat(db): migration 0067 to clean OCR dot leader asset names in transactions and record cleaning audit notes _(by jaywedgeworth22)_
- **CT** [#1154](https://github.com/jaywedgeworth22/Congress.Trade/pull/1154): docs: update effort log for PR #1151 and #1153 _(by jaywedgeworth22)_
- **CT** [#1157](https://github.com/jaywedgeworth22/Congress.Trade/pull/1157): deploy: Coolify auto-deploy; retire Oracle SSH Actions path _(by jaywedgeworth22)_
- **CT** [#1159](https://github.com/jaywedgeworth22/Congress.Trade/pull/1159): feat(ui): add optional Notes column and trade drawer audit notes view _(by jaywedgeworth22)_
- **CT** [#1160](https://github.com/jaywedgeworth22/Congress.Trade/pull/1160): fix(latency): expand Quiver and Unusual Whales date field aliases _(by jaywedgeworth22)_
- **CT** [#1162](https://github.com/jaywedgeworth22/Congress.Trade/pull/1162): fix(latency): clean middle initials and normalize ticker dots to dashes in generateTradeHash _(by jaywedgeworth22)_
- **CT** [#1163](https://github.com/jaywedgeworth22/Congress.Trade/pull/1163): fix(latency): fuzzy match when transaction date is unparsed on provider side _(by jaywedgeworth22)_
- **CT** [#1164](https://github.com/jaywedgeworth22/Congress.Trade/pull/1164): feat(latency): support FMP_LATENCY_API_KEY and clamp FMP request limit to 25 _(by jaywedgeworth22)_
- **CT** [#1165](https://github.com/jaywedgeworth22/Congress.Trade/pull/1165): fix(latency): fix column references in backfillTradeLatencyCandidates SQL query _(by jaywedgeworth22)_
- **CT** [#1166](https://github.com/jaywedgeworth22/Congress.Trade/pull/1166): docs: replace Hetzner references with Oracle across agent policies and codebase docs _(by jaywedgeworth22)_
- **CT** [#1167](https://github.com/jaywedgeworth22/Congress.Trade/pull/1167): fix(ui): remove intro splash animations from website and iOS app _(by jaywedgeworth22)_
- **CT** [#1168](https://github.com/jaywedgeworth22/Congress.Trade/pull/1168): fix(auth): graceful handling and inline messaging for unconfigured Google OAuth _(by jaywedgeworth22)_
- **CT** [#1170](https://github.com/jaywedgeworth22/Congress.Trade/pull/1170): fix(prod): add Infisical bootstrap credentials to .prod.vars and multi-path fallback in main.ts _(by jaywedgeworth22)_
- **CT** [#1171](https://github.com/jaywedgeworth22/Congress.Trade/pull/1171): deploy: COOLIFY_AGENTS for Coolify API; keep stats token separate _(by jaywedgeworth22)_
- **CT** [#1172](https://github.com/jaywedgeworth22/Congress.Trade/pull/1172): fix(ci): route GitHub Actions to self-hosted Coolify runner for private repos and cloud runner for public repos _(by jaywedgeworth22)_
- **CT** [#1178](https://github.com/jaywedgeworth22/Congress.Trade/pull/1178): ci: finish Deno retirement — drop staging preview + stale Sentry watchlist [KIMI] _(by jaywedgeworth22)_
- **CT** [#1179](https://github.com/jaywedgeworth22/Congress.Trade/pull/1179): chore(config): sync updated Unusual Whales API key and global-api-keys.env lookup _(by jaywedgeworth22)_
- **ST** [#2253](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2253): feat(strategy): migrate to TradingGraph architecture _(by jaywedgeworth22)_
- **ST** [#2256](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2256): fix(risk): clamp daily notional cap to non-negative available spend and buying power _(by jaywedgeworth22)_
- **ST** [#2257](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2257): feat(strategy): enforce minimum account equity threshold for strategy runs _(by jaywedgeworth22)_
- **ST** [#2258](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2258): ci: pin setup-node to known good SHA _(by jaywedgeworth22)_
- **ST** [#2259](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2259): fix(ci): clean gitleaks temp files and fix db mock in challenger test _(by jaywedgeworth22)_
- **ST** [#2263](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2263): ci: remove concurrency bottleneck to allow parallel builds on self-hosted runners _(by jaywedgeworth22)_
- **ST** [#2265](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2265): fix(ui): prevent account switcher dropdown overflow and fix PWA touch backdrop on mobile _(by jaywedgeworth22)_
- **ST** [#2266](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2266): chore(license): add Apache 2.0 license and remove private flag _(by jaywedgeworth22)_
- **ST** [#2267](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2267): fix(ci): give Playwright Smoke webServer a test ENCRYPTION_KEY _(by jaywedgeworth22)_
- **ST** [#2268](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2268): fix(macro): keyless VIX cascade + hold-last-known regime on feed outage _(by jaywedgeworth22)_
- **ST** [#2269](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2269): fix(ci): raise Playwright Smoke NODE_OPTIONS to 3072 to match ci.yml _(by jaywedgeworth22)_
- **ST** [#2271](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2271): fix(ci): 30s request timeout for hung Effort Issues Sync + staged job backstop _(by jaywedgeworth22)_
- **ST** [#2272](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2272): feat(scheduler): task brain / cron journal + OSS lessons doc _(by jaywedgeworth22)_
- **ST** [#2273](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2273): docs,fix: System errors diagnostics and fixes (rate limits, staleness, retries) _(by jaywedgeworth22)_
- **ST** [#2274](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2274): fix(mobile): filter terminal orders in snapshot, add safe-area-inset-top for PWA _(by jaywedgeworth22)_
- **ST** [#2275](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2275): feat(risk): accuracy breaker (nofx-style consecutive-miss safety mode) _(by jaywedgeworth22)_
- **ST** [#2276](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2276): ci: retire self-hosted runners; GitHub-hosted ubuntu-latest only _(by jaywedgeworth22)_
- **ST** [#2285](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2285): fix(ops): Coolify stats token for metrics + Infisical secret-list guardrails _(by jaywedgeworth22)_
- **ST** [#2287](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2287): Expose portfolio fetch errors in UI to fix hidden $1000 fallback _(by jaywedgeworth22)_
- **UM** [#832](https://github.com/jaywedgeworth22/Usage-Monitor/pull/832): docs: update license to Apache 2.0 _(by jaywedgeworth22)_
- **UM** [#834](https://github.com/jaywedgeworth22/Usage-Monitor/pull/834): ci: migrate to hosted ubuntu-latest runners _(by jaywedgeworth22)_
- **UM** [#835](https://github.com/jaywedgeworth22/Usage-Monitor/pull/835): fix(ui): mobile/PWA quick wins from 2026-07-28 review _(by jaywedgeworth22)_
- **UM** [#836](https://github.com/jaywedgeworth22/Usage-Monitor/pull/836): ops/docs/hygiene: 2026-07-28 review O1/O5/O6/O7/O8/O9/O10 (+O14 export) _(by jaywedgeworth22)_
- **UM** [#837](https://github.com/jaywedgeworth22/Usage-Monitor/pull/837): feat(ingest): cross-app interop remediation X1–X9 (identity rate limits, per-event v2 rejections, typed 500s, versioned reads) _(by jaywedgeworth22)_
- **UM** [#838](https://github.com/jaywedgeworth22/Usage-Monitor/pull/838): perf(core): E1/E2a/E3/E4/E5/E6 efficiency fixes (2026-07-28 review §5) _(by jaywedgeworth22)_
- **UM** `Claude` [#839](https://github.com/jaywedgeworth22/Usage-Monitor/pull/839): feat(analytics): LiteLLM pricing snapshot + — cost cross-check _(by jaywedgeworth22)_
- **UM** [#841](https://github.com/jaywedgeworth22/Usage-Monitor/pull/841): feat(budget): spending-intelligence core — S2/S4/S6/S8/S9/S11/S13 + E3 partial _(by jaywedgeworth22)_
- **UM** [#842](https://github.com/jaywedgeworth22/Usage-Monitor/pull/842): docs: mark #839 merged in effort log _(by jaywedgeworth22)_
- **UM** [#843](https://github.com/jaywedgeworth22/Usage-Monitor/pull/843): fix(receipt-inbox): Workers-compatible lifecycle auditor fetch redirect _(by jaywedgeworth22)_
- **UM** [#845](https://github.com/jaywedgeworth22/Usage-Monitor/pull/845): feat(alerts): project budget/anomaly alerts, anomaly caps, cross-month baseline, per-code fatigue controls, subscription insights _(by jaywedgeworth22)_
- **UM** [#846](https://github.com/jaywedgeworth22/Usage-Monitor/pull/846): O4 self-Sentry error reporting + E7/O11 dead-dependency hygiene _(by jaywedgeworth22)_
- **UM** [#847](https://github.com/jaywedgeworth22/Usage-Monitor/pull/847): feat(ios): parity fixes I3/I5/I6/I7/I8/I9/I10/L5 from 2026-07-28 full-app review _(by jaywedgeworth22)_
- **UM** [#848](https://github.com/jaywedgeworth22/Usage-Monitor/pull/848): feat(ingest): default-off LiteLLM cost derivation for unpriced token events _(by jaywedgeworth22)_
- **UM** [#850](https://github.com/jaywedgeworth22/Usage-Monitor/pull/850): docs: mark #848 merged in effort log _(by jaywedgeworth22)_
- **UM** [#852](https://github.com/jaywedgeworth22/Usage-Monitor/pull/852): feat(ios): I2/I4 — session-backed project CRUD + provider-detail read depth _(by jaywedgeworth22)_
- **UM** [#853](https://github.com/jaywedgeworth22/Usage-Monitor/pull/853): refactor(ui): shared format/status-vocab/dialog primitives, projection + project-alert UI, export bearer wiring _(by jaywedgeworth22)_
- **UM** [#854](https://github.com/jaywedgeworth22/Usage-Monitor/pull/854): feat(infisical): integrate usage-monitor project scope and shared machine identity fallback _(by jaywedgeworth22)_
- **UM** [#857](https://github.com/jaywedgeworth22/Usage-Monitor/pull/857): docs: Infisical usage-monitor prod secret migration note _(by jaywedgeworth22)_
- **shared** [#254](https://github.com/jaywedgeworth22/congress-trading-shared/pull/254): docs: update license to Apache 2.0 _(by jaywedgeworth22)_
- **shared** [#255](https://github.com/jaywedgeworth22/congress-trading-shared/pull/255): ci: migrate to hosted ubuntu-latest runners _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1144](https://github.com/jaywedgeworth22/Congress.Trade/issues/1144): [2026-07-29] Fix iOS app crash on All Time selection, display asset names
- **CT** [#1145](https://github.com/jaywedgeworth22/Congress.Trade/issues/1145): [2026-07-28] Clean up OCR dot leaders and unparsed asset labels without LLM
- **CT** [#1146](https://github.com/jaywedgeworth22/Congress.Trade/issues/1146): [2026-07-29][KIMI] Open-source lessons research note — MERGED PR #1124
- **CT** [#1155](https://github.com/jaywedgeworth22/Congress.Trade/issues/1155): [2026-07-29] Migration 0067 database OCR dot leader cleaning & row audit
- **CT** [#1156](https://github.com/jaywedgeworth22/Congress.Trade/issues/1156): [2026-07-29] Web Dashboard Asset Name Cleaning & Sorting Tie-Breakers
- **ST** [#2260](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2260): Graph-based execution loop (strategy migration)
- **UM** [#797](https://github.com/jaywedgeworth22/Usage-Monitor/issues/797): owner-blocked: enable Cloudflare R2 for receipt inbox + Litestream restore path
- **UM** [#840](https://github.com/jaywedgeworth22/Usage-Monitor/issues/840): [KIMI] Open-source lessons: LiteLLM pricing + — cost cross-check
- **UM** [#849](https://github.com/jaywedgeworth22/Usage-Monitor/issues/849): [KIMI] Ingest-time LiteLLM cost derivation, default-off flag (2026-07-29)

### Issues opened

- **CT** [#1144](https://github.com/jaywedgeworth22/Congress.Trade/issues/1144): [2026-07-29] Fix iOS app crash on All Time selection, display asset names
- **CT** [#1145](https://github.com/jaywedgeworth22/Congress.Trade/issues/1145): [2026-07-28] Clean up OCR dot leaders and unparsed asset labels without LLM
- **CT** [#1146](https://github.com/jaywedgeworth22/Congress.Trade/issues/1146): [2026-07-29][KIMI] Open-source lessons research note — MERGED PR #1124
- **CT** [#1155](https://github.com/jaywedgeworth22/Congress.Trade/issues/1155): [2026-07-29] Migration 0067 database OCR dot leader cleaning & row audit
- **CT** [#1156](https://github.com/jaywedgeworth22/Congress.Trade/issues/1156): [2026-07-29] Web Dashboard Asset Name Cleaning & Sorting Tie-Breakers
- **ST** [#2260](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2260): Graph-based execution loop (strategy migration)
- **ST** [#2280](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2280): Backtest-integrity suite for the learning loop — PLANNED
- **UM** [#840](https://github.com/jaywedgeworth22/Usage-Monitor/issues/840): [KIMI] Open-source lessons: LiteLLM pricing + — cost cross-check
- **UM** [#844](https://github.com/jaywedgeworth22/Usage-Monitor/issues/844): [KIMI] Open-source lessons: LiteLLM pricing + — cost cross-check
- **UM** [#849](https://github.com/jaywedgeworth22/Usage-Monitor/issues/849): [KIMI] Ingest-time LiteLLM cost derivation, default-off flag (2026-07-29)
- **UM** [#851](https://github.com/jaywedgeworth22/Usage-Monitor/issues/851): [KIMI] Ingest-time LiteLLM cost derivation, default-off flag (2026-07-29)
- **UM** [#855](https://github.com/jaywedgeworth22/Usage-Monitor/issues/855): Integrate Infisical project 'usage-monitor' scope & shared machine
- **UM** [#859](https://github.com/jaywedgeworth22/Usage-Monitor/issues/859): Infisical project usage-monitor prod populated (2026-07-30) — DONE. 76
