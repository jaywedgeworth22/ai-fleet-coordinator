# Jay's Daily Coding-Related Activities

_Generated 2026-08-29 20:57 CDT · timezone America/Chicago_

Sources: merged PRs, issues opened/closed, effort-board bullets (`docs/EFFORT-LOG.md`).
Agent names are stripped from titles; HTML site shows logos instead.

- **HTML:** https://jaywedgeworth22.github.io/ai-fleet-coordinator/
- **ICS (daily outline):** https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/daily-digest.ics
- **ICS (per-commit activity):** https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/agent-activity.ics

## 2026-08-29

*8 PRs merged · 0 issues opened · 0 issues closed · 232 effort rows*

### Merged PRs

- **CT** [#2251](https://github.com/jaywedgeworth22/Congress.Trade/pull/2251): chore(deps-dev): bump eslint from 10.9.0 to 10.9.1 in /app _(by dependabot[bot])_
- **CT** [#2254](https://github.com/jaywedgeworth22/Congress.Trade/pull/2254): chore(deps-dev): bump @typescript-eslint/parser from 8.67.0 to 8.68.0 in /app _(by dependabot[bot])_
- **CT** [#2255](https://github.com/jaywedgeworth22/Congress.Trade/pull/2255): chore(deps-dev): bump @types/node from 26.2.0 to 26.3.0 in /app _(by dependabot[bot])_
- **CL** [#24](https://github.com/jaywedgeworth22/ContactLogo/pull/24): fix: full-stack remediation of the 29-finding audit _(by jaywedgeworth22)_
- **PS** [#45](https://github.com/jaywedgeworth22/Personal-Site/pull/45): feat(branding): align project names, blurbs, and latest crisp app icons _(by jaywedgeworth22)_
- **ST** [#3124](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3124): fix(auth,ios): return the OAuth sheet to the app + survive equity-curve decode _(by jaywedgeworth22)_
- **ST** [#3125](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3125): docs: record #3124 merge + production deploy on the effort log _(by jaywedgeworth22)_
- **AFC** [#143](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/143): feat(fleet): align app names, normalize board aliases, and refresh activity assets _(by jaywedgeworth22)_

### Effort board

- **ST** `Claude` [ -> ] iOS OAuth return-to-app + workspace decode fixes — COMPLETED / Deployed to production 2026-08-29 (PR #3124, squash `f1d3a3e6f`, live `f1d3a3e6f`, board 0b58f822). Owner re-report after #3116/#3117. — root-caused both and committed to the lane but never pushed — picked up the unpushed commit, re-verified both causes against live prod, hardened, and l
- **ST** `Claude` Durable litestream remote-inventory cache (PR #2665 leftover) — IN PROGRESS. Issue #2694
- **ST** `Claude` Durable litestream remote-inventory cache (PR #2665 leftover) — IN PROGRESS. Issue #2694
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
- **ST** `Claude` PR #449 - Regime-enum adoption inside the risk gates ( risk lane). Merged to `main`
- **ST** `Claude` PR #374 - GitHub Issues mirror of the effort board , cross-app
- **ST** PR #350 - AI Review inheritance, model catalog, and text-box font controls
- **ST** PR #349 - Socratic admin/RAG/Pinecone/settings parity implementation
- **ST** PR #348 - Sell to Fund Buys title-case copy fix
- **ST** PR #347 - Console universe index exclusivity fix
- **ST** PR #346 - IRA wash-sale UI correction
- **ST** PR #345 - Run-state UX fix
- **ST** PR #344 - Socratic Trade Autonomy Desk implementation
- **ST** PR #340 - Socratic Trade rebrand
- **ST** `Antigravity` Fix mobile "Settings" crash inside Sheet — Fixed "Maximum call stack size exceeded" bug caused by a focus trap race condition when navigating to settings from the More sheet menu on mobile. PR pending
- **ST** `Antigravity` Harden HMAC Security & Persistent Idempotency for webhooks — moved back from Completed
- **ST** `Antigravity` Congress.Trade Improvements — Comprehensive improvements across UI, data sharing, and scraping. Worktree `~/apps/trading- `, branch `agent/antigravity`
- **ST** `Codex` Cloud Slack + effort-log readiness across all four apps
- **ST** `Cursor` ~~PR #808 — session: P0 checkRegimeFlip RMW fix + P1 backlog exhaustiveness ~~
- **ST** `Antigravity` ~~Admin connection health and backend-failure notification pass ~~
- **ST** `Cursor` `Claude` PR #856 - add — lane at port 4103, move — to 4104 (OWNER, S) — new row, IN PROGRESS
- **ST** `Claude` Shared-dep tokenless git-dependency switch — CLOSED, superseded by #444
- **ST** `Codex` global coordination + fleet monitoring setup
- **ST** `Claude` `claude/ci-hybrid-runner-verify`
- **ST** `Claude` `claude/drawdown-advisory-rescope` → PR #360, auto-merge armed
- **ST** `claude/w1-llm-fixes` — Bear schema confidenceScore fix (live bug); non-OpenAI reasoning-token headroom; cross-family Bear default + temperature; reward-abstention; stakes-scaled dissent trigger. STATUS: MERGED (PR #364)
- **ST** `Codex` `claude/w1-learning-loops` — Bear-veto counterfactuals + red-team efficacy scorecard; re-index decision memory on lifecycle changes; trading-day horizon arithmetic; + — second-pass review fixes (market-day horizon anchoring via new `market-calendar.marketDateOf`, kind-scoped veto audit queries + keyed efficacy joins, NULL-evidence backfill on `insertSkippedCounterfactualCandidate`). STA
- **ST** `claude/w1-rag-quickwins` — relevance floor + near-dup dedupe wired; provenance headers + stable chunk ids; content-hash dedup on + 128-bit; embedding-model version tag; rerank pool cap. STATUS: MERGED (PR #366)
- **ST** `Claude` `claude/w1-regime-data` — typed regime enum + numeric severity (new dependency-free `src/lib/market-regime.ts`); live ^VIX off the 24h macro cache; per-data-class TTLs + asOf on Alpaca snapshot. STATUS: MERGED (PR #368). NOTE (correction to the earlier row text): the crisis cap (policy.ts) and bear filter (strategy.ts) deliberately KEPT their substring checks per the swimlan
- **ST** `Claude` `claude/tokenless-git-dep`
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
- **CT** `Grok` 2026-08-05 — COMPLETED + DEPLOYED — Pricing $5/$50 + 30d trial, delivery edit, Apple IAP. PR #1345 `0733b3f8`. Live HTML: $5/mo · $50/yr · 1-month free trial. Coolify deploy finished. grant-premium jaywedgeworth22@gmail.com → trialing monthly thru 2026-09-04 + seeded user SSE delivery. ST system deliveries (socratic-trade-) left alone. iOS IAP still needs App Store Connect produ
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
- **CT** Web: delivery pause/resume/delete + filter editing (unassigned, M)
- **CT** Wave 4 go-live: configure auth + Stripe paywall services (unassigned, M) — board reservation
- **UM** `Codex` Infisical provider-credential auto-sync ( delegated implementation + security/runtime reviewers, owner-directed
- **UM** `Codex` Remaining-provider automatic enrichment implementation wave ( + provider teams
- **UM** `Antigravity` App-wide UI/UX Responsive and Accessibility Refinements — COMPLETED: Adding skeleton loaders, fixing table responsiveness on mobile, and semantic HTML fixes in ProviderCard. Merged implicitly into `main` via PR #66
- **UM** Bound generic usage-ingest request bodies before JSON decoding (unassigned, S) — MERGED PR #311 / DEPLOYED. OTLP ingest uses
- **UM** `Antigravity` Generic Service Cost Tracking & Project Schema Update — MERGED PR #66 / DEPLOYED. — COMPLETED: Decoupling API from Service in Provider, adding `Project` and `ProviderProjectAllocation` tables via Prisma to allow fractional cost attribution. (From architecture audit)
- **UM** `Claude` Fix /api/budget-status 401: exclude it from the dashboard-session middleware matcher — MERGED PR #58 / DEPLOYED
- **UM** `Antigravity` Resolve Agent Sync Relay noise and Anthropic must-keep-funded alerts — MERGED PR #113 / DEPLOYED. Updated `ensureAgentSyncProviderSeeded` to automatically disable the Agent Sync Relay provider on startup/poll, silencing the spurious missing_snapshot PagerDuty alerts. Also added a migration step in the same boot sequence to unflag `mustKeepFunded` for Anthropic since Anthropic does
- **UM** `Grok` Prod revision identity — LANDING. Deleted frozen Coolify `GIT_COMMIT_SHA`/`SOURCE_COMMIT` env; PR #1093 merged (prefer SOURCE_COMMIT); PR #1096 bakes SOURCE_COMMIT into image. Force rebuild after #1096 merges. Public may still show revision null until rebuild
- **UM** `Grok` Rename compose project oracle → usage-monitor — COMPLETED PR #1018 (`8f23199600fd`). Issue #1019 closed
- **UM** `Grok` iOS app icons clean orange + Local LOCAL stripe — COMPLETED PR #1009 (`750a28cede83`). Issue #1011 closed
- **UM** `Grok` R2 fleet ST/CT pushover-parity + iOS inline titles — COMPLETED PR #984 (`4be34c7e8815`). Issue #1006 closed
- **UM** `Grok` Fix auto-deploy race mid-build — COMPLETED PR #1001 (`61def229`). Issue #992 closed
- **UM** `Grok` Install replica-status probe + R2 kill reason — COMPLETED PR #989 (`098c9658c7b8`). Issue #990 closed
- **UM** `Grok` Issue/effort hygiene + replica age 3h — COMPLETED PR #976 (`6fc1def25ae8`). Issue #979 closed
- **UM** `Grok` Overview money UX — COMPLETED PR #949 (`146c9ca05b7b`). Issue #980 closed
- **UM** `Grok` iOS staleness banners + fetch coalescing + subscriptions read UI (P2, M) — PLANNED. Wire `BudgetStaleness`; single in-flight `BudgetStore` fetch; surface `APIClient.subscriptions()`
- **UM** `Grok` Producer retry-storm contract (ST/CT/OTLP wrappers) (P0, L, cross-repo) — PLANNED. Honor Retry-After; exponential backoff + circuit breaker; treat HTTP 202 as success regardless of `accepted`; never spin on `accepted: 0`. Cross-board rows on Socratic.Trade / Congress.Trade / shared as needed. Evidence: historical OOM→35rps overage
- **UM** `Grok` Dark-mode pass on Projects, Attention, Sentry, dashboard chrome (P1, S) — PLANNED. Complements residual dark-mode planned row
- **UM** `Grok` Cross-repo telemetry contract CI lock (P1, M) — PLANNED. Shared package vectors/enums vs `usage-telemetry.ts`; pin version. Cross: congress-trading-shared
- **UM** `Grok` Producer hard rules: always occurredAt ISO + explicit per-call idempotencyKey (P1, M, cross-repo) — PLANNED. Fix random-UUID when occurredAt missing; normalize ISO in basis only with coordinated bump
- **UM** `Grok` Optional verified-preferred cash mode for OpenRouter when coverage high (P2, L) — PLANNED. Audit layer today does not correct budgets
- **UM** Capture exact OpenAI, Mistral, and Google recurring subscription terms (unassigned, M). Current production has no local Subscription rows for these providers, and the integrated official usage/cost APIs do not expose the owner's consumer subscription purchase terms. Import an exact receipt or owner-supplied amount, currency, cadence, current-period start/end, renewal behavior, provider
- **UM** Implement OTLP logs ingestion (unassigned, L, deliberately deferred) — `/api/otlp/v1/logs`
- **CTS** Renamed remaining "Agentic Trading" references to "Socratic Trade" (PR #119)
- **CTS** Added Zod schemas for AmountBracket, Subscription, and SseMessage (PR #119)
- **CTS** Expanded client.ts and SseParser test coverage to 337 tests (PR #119)
- **CTS** Refined AmountBracketSchema to reject inverted bounds (PR #119)
- **CTS** Fixed TypeScript 6.0.3 and Zod v4 compatibility issues in tsup/schemas (PR #119)
- **CTS** Unified ticker normalizer regex & preferred/depositary helper functions (PR #97)
- **CTS** Relocated STOCK Act AmountBracket definitions & snapping/matching helpers (PR #97)
- **CTS** Aligned Zod schemas for ClientAsset and ClientTrade with production API outputs (PR #98)
- **CTS** Vitest CI test suite execution with strict code coverage minimum thresholds (PR #96)
- **CTS** Tokenless smoke-install verification job in CI (PR #96)
- **CTS** Corrected docs/RELEASE.md consumer notification list (PR #96)
- **CTS** CongressTradeClient + SUBSCRIPTIONS API path (PR #55)
- **CTS** balance/limit metricTypes (PR #56)
- **CTS** createCongressEvent helper and type dedup (PR #57)
- **CTS** Dependabot + weekly CI audit (PR #54)
- **CTS** (n/a for pre-1.3.0 — library package; "deployed" = version published/consumed by apps)
- **CTS** `Codex` Protect immutable release tags and enable repository-native security controls
- **CTS** `Claude` `Codex` autofix reusable workflow: migrate from Anthropic to DeepSeek
- **CTS** Make exact-pin drift checks tokenless, symmetric, and fail-closed (cross-app, P1/M)
- **CTS** `Antigravity` Split `TICKER_ALIASES` into rename-vs-acquisition classes — shared portion done in v1.3.0; consumer migration pending. ATVI→MSFT is
- **AR** `Antigravity` Web and iOS utility and power enhancements — · PR [#48](https://github.com/jaywedgeworth22/Autorotate/pull/48) (`ag/utility-power-enhancements`). Interactive .env importer & wizard, multi-select & batch actions, secret drift detection & live read-back inspector, dry-run simulator, workspace alert webhooks (Slack/Discord), QR pairing, Face ID biometrics, SwiftUI .env importer, QR scan
- **AR** `Grok` Merge — App Builder PWA with this monorepo — · merged as [#38](https://github.com/jaywedgeworth22/Autorotate/pull/38) (`900bd54`). Backups under `backups/`. Live web engine folds — rotators + parser + Mac agent
- **AR** `Cursor` `Grok` Apache-2.0 + Kimi dump backup + catalog fold-in — · PR [#42](https://github.com/jaywedgeworth22/Autorotate/pull/42) · branch `cursor/kimi-apache-merge`. Relicensed to Apache 2.0 (© Jay). Kimi dump at `backups/kimi-agent-autorotate/`. Secret Rotator nickname (`app/`) at `backups/secret-rotator/` (not a standalone app). — extra catalog folded into live web + AutorotateCore
- **AR** `Grok` `Antigravity` Owner: Developer portal App IDs for Autorotate — leftover after — #50 closed as duplicate of — #48. https://autorotate.codes. Do not reopen or merge #50. `com.jay.shellular` stays disabled
- **CL** `Grok` (none on Coolify/Cloudflare yet. Official product URL is https://contactlogo.com. — Publish at https://contact-logo.grok.me is legacy only.)
- **AFC** (n/a — machine-side infra is "deployed" when running under pm2/hooks; see Completed)
- **AFC** `Claude` Push pipeline RECEIVE path — BLOCKED on owner. Slack app Event Subscriptions not
- **AFC** `Codex` cloud Slack + effort-log readiness work (DONE-local, never pushed) — new row, IN PROGRESS
- **AFC** `Antigravity` Socratic.Trade PR #853 (effort-log mirror sync) still OPEN despite — 'DONE' claim — new row, IN
- **AFC** `Cursor` `Claude` Socratic.Trade PR #856 (port-lane docs: — 4103 / — 4104) still OPEN — new row, IN
- **AFC** `Antigravity` congress-trading-shared PRs #54/#55/#56 open despite — 'DONE' Slack claims — new row, IN
- **AFC** `Claude` `Antigravity` Congress.Trade PRs #181 (Sentry CI reporter, ) and #182 (dep pin, ) open — new row, IN
- **AFC** `Claude` Effort-issues sync rate-limit hardening propagated fleet-wide ( + owner-spawned
- **AFC** Enable Slack Event Subscriptions so the relay receive path goes live (OWNER, S) — toggle +

## 2026-08-28

*17 PRs merged · 9 issues opened · 4 issues closed · 2 effort rows*

### Merged PRs

- **AR** [#71](https://github.com/jaywedgeworth22/Autorotate/pull/71): chore(deps-dev): bump @babel/plugin-transform-modules-systemjs from 7.29.0 to 7.29.8 in /backups/secret-rotator/tree _(by dependabot[bot])_
- **AR** [#72](https://github.com/jaywedgeworth22/Autorotate/pull/72): chore(deps): bump lodash from 4.17.21 to 4.18.1 in /backups/secret-rotator/tree _(by dependabot[bot])_
- **AR** [#73](https://github.com/jaywedgeworth22/Autorotate/pull/73): chore(deps-dev): bump flatted from 3.3.3 to 3.4.4 in /backups/secret-rotator/tree _(by dependabot[bot])_
- **AR** `Claude` [#88](https://github.com/jaywedgeworth22/Autorotate/pull/88): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **AR** [#114](https://github.com/jaywedgeworth22/Autorotate/pull/114): feat(legal): add /privacy and /privacy-policy static pages for App Store review _(by jaywedgeworth22)_
- **CT** [#2257](https://github.com/jaywedgeworth22/Congress.Trade/pull/2257): feat(ingest): route scraping and probing via Tailscale residential proxy _(by jaywedgeworth22)_
- **CL** [#29](https://github.com/jaywedgeworth22/ContactLogo/pull/29): docs(branding): four logo concepts for ContactLogo _(by jaywedgeworth22)_
- **CL** `Claude` [#31](https://github.com/jaywedgeworth22/ContactLogo/pull/31): feat(branding): adopt — official logo 01-swap-square and 1024x1024 app icon _(by jaywedgeworth22)_
- **DD** [#209](https://github.com/jaywedgeworth22/DealDex/pull/209): docs: handoff — Android has never been compiled, and everything else still open _(by jaywedgeworth22)_
- **DD** [#211](https://github.com/jaywedgeworth22/DealDex/pull/211): Fix Datadog 503, PGlite WASM bundling, fixed iOS origin, and polished sign-in buttons _(by jaywedgeworth22)_
- **ST** [#3121](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3121): feat(qdrant): Pinecone-to-Qdrant copy script + rollout doc _(by jaywedgeworth22)_
- **ST** [#3122](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3122): Kalshi first-class account, real-time paper data, and universal shorting & options _(by jaywedgeworth22)_
- **ST** [#3123](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3123): Update EFFORT-LOG.md for Kalshi and options expansion completion _(by jaywedgeworth22)_
- **AFC** [#121](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/121): feat(handoff): cloud→Mac local-agent needs-mac queue _(by jaywedgeworth22)_
- **AFC** [#139](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/139): feat(backup): snapshot findings.db to Google Drive daily backup _(by jaywedgeworth22)_
- **AFC** [#142](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/142): Integrate CleanMyMac CLI into local housekeeping and disk janitor scripts _(by jaywedgeworth22)_
- **OPS** [#5](https://github.com/jaywedgeworth22/fleet-ops/pull/5): docs(inventory): correct ST Infisical id; add qdrant-st entry _(by jaywedgeworth22)_

### Issues closed

- **CL** [#30](https://github.com/jaywedgeworth22/ContactLogo/issues/30): Pickup PR #24 local compile + merge main
- **CL** [#34](https://github.com/jaywedgeworth22/ContactLogo/issues/34): Web: load a pasted logo URL via canvas so connect-src can drop `https:`
- **DD** [#210](https://github.com/jaywedgeworth22/DealDex/issues/210): 2026-08-28 — IN PROGRESS — Fix Datadog 503 / Vercel secrets, PGlite WASM packaging, iOS unmodifiable dealdex.net origin & polished sign-in buttons
- **AFC** [#141](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/141): Integrate CleanMyMac CLI into local housekeeping and disk janitor scripts

### Issues opened

- **CL** [#32](https://github.com/jaywedgeworth22/ContactLogo/issues/32): iOS: persist the background match queue before advertising it
- **CL** [#33](https://github.com/jaywedgeworth22/ContactLogo/issues/33): Native shells: surface retryable rows instead of showing them as "Not found"
- **CL** [#34](https://github.com/jaywedgeworth22/ContactLogo/issues/34): Web: load a pasted logo URL via canvas so connect-src can drop `https:`
- **CL** [#35](https://github.com/jaywedgeworth22/ContactLogo/issues/35): Web: virtualizer assumes every row is the height of the first one
- **CL** [#36](https://github.com/jaywedgeworth22/ContactLogo/issues/36): R8: an org-only brand-tail card resolves to the contact's email domain, not the tail's brand
- **CL** [#37](https://github.com/jaywedgeworth22/ContactLogo/issues/37): Simple Icons: 23 of 79 curated slugs 404, and 7 domains are left with no high-tier source
- **DD** [#210](https://github.com/jaywedgeworth22/DealDex/issues/210): 2026-08-28 — IN PROGRESS — Fix Datadog 503 / Vercel secrets, PGlite WASM packaging, iOS unmodifiable dealdex.net origin & polished sign-in buttons
- **DD** [#212](https://github.com/jaywedgeworth22/DealDex/issues/212): 2026-08-28 — IN PROGRESS — Fix Datadog 503 / Vercel secrets, PGlite WASM
- **AFC** [#141](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/141): Integrate CleanMyMac CLI into local housekeeping and disk janitor scripts

### Effort board

- **CT** `Antigravity` 2026-08-28 — IN PROGRESS (branch `antigravity/tailscale-residential-proxy`) — Tailscale residential proxy on Mac & server-directed scraping/probing. Deploying a lightweight HTTP/CONNECT proxy on Mac over Tailscale (`100.113.106.39:3128`), retiring local scout in favor of server-directed scraping & latency probes, and adding native proxied fetch in Deno with fail-soft fallback wh
- **DD** `Antigravity` 2026-08-28 — IN PROGRESS — Fix Datadog 503 / Vercel secrets, PGlite WASM packaging, iOS unmodifiable dealdex.net origin & polished Google/Apple/X sign-in buttons. Branch `ag/auth-buttons-and-fixed-url`. Configured missing production secrets on Vercel (`DD_API_KEY`, Better Auth, OAuth IDs), added `copy-pglite.mjs` for serverless function WASM assets, made iOS origin unmodifiable to

## 2026-08-27

*28 PRs merged · 25 issues opened · 17 issues closed · 10 effort rows*

### Merged PRs

- **CT** [#2238](https://github.com/jaywedgeworth22/Congress.Trade/pull/2238): docs(asc): verify prices + trial from the live API, add read-only ASC checks _(by jaywedgeworth22)_
- **CT** `Claude` [#2239](https://github.com/jaywedgeworth22/Congress.Trade/pull/2239): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **CT** [#2240](https://github.com/jaywedgeworth22/Congress.Trade/pull/2240): fix(backup): litestream B2 multipart part-size 10MB + concurrency 2 _(by jaywedgeworth22)_
- **CT** `Antigravity` [#2241](https://github.com/jaywedgeworth22/Congress.Trade/pull/2241): iOS UI polish: Trends KPIs, filter legibility, drawer titles & error fallback, avatars & logos, directory top gap, delivery cleanup _(by jaywedgeworth22)_
- **CT** [#2242](https://github.com/jaywedgeworth22/Congress.Trade/pull/2242): docs(effort-log): closeout iOS UI polish lane (PR #2241 merged) _(by jaywedgeworth22)_
- **CT** `Antigravity` [#2243](https://github.com/jaywedgeworth22/Congress.Trade/pull/2243): fix(ios-ship): restore 1.0.# (timestamp) build number format _(by jaywedgeworth22)_
- **CT** [#2244](https://github.com/jaywedgeworth22/Congress.Trade/pull/2244): docs(effort-log): closeout iOS timestamp build number restore (PR #2243 merged) _(by jaywedgeworth22)_
- **CT** [#2246](https://github.com/jaywedgeworth22/Congress.Trade/pull/2246): feat(observability): align Datadog APM tracing with Socratic.Trade standard _(by jaywedgeworth22)_
- **CT** [#2247](https://github.com/jaywedgeworth22/Congress.Trade/pull/2247): docs(effort-log): close out #2246 Datadog APM alignment _(by jaywedgeworth22)_
- **DD** [#183](https://github.com/jaywedgeworth22/DealDex/pull/183): Add Datadog logs, APM, and browser RUM on the existing US5 account _(by jaywedgeworth22)_
- **DD** [#201](https://github.com/jaywedgeworth22/DealDex/pull/201): fix(ios-ship): restore UTC CFBundleVersion _(by jaywedgeworth22)_
- **DD** [#203](https://github.com/jaywedgeworth22/DealDex/pull/203): Full-app review remediation: valuation, native privacy, sign-in, a real iOS card scanner, and the tests that keep them fixed _(by jaywedgeworth22)_
- **DD** [#205](https://github.com/jaywedgeworth22/DealDex/pull/205): docs: record the #203 ship — the Swift compiles, 1.0.59 is on TestFlight _(by jaywedgeworth22)_
- **ST** [#3116](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3116): fix(auth,ios): GET OAuth initiator for native web sign-in + legacy signin translation _(by jaywedgeworth22)_
- **ST** [#3117](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3117): fix(dashboard,ios): cut snapshot worst-case latency and retry first mobile load _(by jaywedgeworth22)_
- **ST** [#3118](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3118): docs: record #3116/#3117 merge + deploy on effort log _(by jaywedgeworth22)_
- **UM** [#1366](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1366): fix(ios-ship): restore UTC CFBundleVersion _(by jaywedgeworth22)_
- **UM** [#1368](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1368): fix(backup): litestream B2 multipart part-size 10MB + concurrency 2 _(by jaywedgeworth22)_
- **UM** [#1369](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1369): docs(backup): record B2 L0 corrupt-object heal + commit the heal script _(by jaywedgeworth22)_
- **AFC** [#130](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/130): docs(reviews): 2026-08-27 fleet ops review _(by jaywedgeworth22)_
- **AFC** [#131](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/131): docs(reviews): correct A1 — early Pinecone snap is a deliberate buffer _(by jaywedgeworth22)_
- **AFC** [#132](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/132): docs(reviews): correct A2 — PR B landed Aug 22 as squash #3041 _(by jaywedgeworth22)_
- **AFC** `Grok` [#133](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/133): feat(afl): let — Bot drive live — TUI sessions _(by jaywedgeworth22)_
- **AFC** `Grok` [#134](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/134): fix(afl): drive live — TUI via session/resume, not load _(by jaywedgeworth22)_
- **AFC** [#135](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/135): docs(reviews): rotation resolved; plain-language RAG key _(by jaywedgeworth22)_
- **AFC** [#136](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/136): fix(afl): live TUI prompt returns queued, does not wait the turn _(by jaywedgeworth22)_
- **AFC** `Grok` [#137](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/137): feat(afl): generic live — TUI drive for any local agent _(by jaywedgeworth22)_
- **AFC** [#138](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/138): feat(afl): TUI drive follow-ups plus cloud MCP hop _(by jaywedgeworth22)_

### Issues closed

- **AR** [#97](https://github.com/jaywedgeworth22/Autorotate/issues/97): Epic: full-field security & quality audit remediation (AR-01…AR-35)
- **AR** [#98](https://github.com/jaywedgeworth22/Autorotate/issues/98): 01 (Critical): web control center has no authentication
- **AR** [#99](https://github.com/jaywedgeworth22/Autorotate/issues/99): 02 (Critical): connector with no config mints a fake secret and writes it to live targets
- **AR** [#100](https://github.com/jaywedgeworth22/Autorotate/issues/100): 03 (Critical): demo mode defaulted ON (fail-open)
- **AR** [#101](https://github.com/jaywedgeworth22/Autorotate/issues/101): 04 (Critical): admin-credential encryption key falls back to a repo-published passphrase
- **AR** [#102](https://github.com/jaywedgeworth22/Autorotate/issues/102): 05 (Critical): Android rotation is fabricated; a 6h worker writes fake audit records
- **AR** [#103](https://github.com/jaywedgeworth22/Autorotate/issues/103): 33 (Critical): debug-signed release APK committed to the public repo
- **AR** [#104](https://github.com/jaywedgeworth22/Autorotate/issues/104): 06 (High): web engine commits a rotation with zero targets
- **AR** [#105](https://github.com/jaywedgeworth22/Autorotate/issues/105): 07 (High): audit chain races itself and cannot be repaired
- **AR** [#106](https://github.com/jaywedgeworth22/Autorotate/issues/106): 08 (High): Apple audit log is not hash-chained
- **AR** [#107](https://github.com/jaywedgeworth22/Autorotate/issues/107): 09 (High): unauthenticated SSRF; stored webhook URLs handed to any caller
- **AR** [#108](https://github.com/jaywedgeworth22/Autorotate/issues/108): 10 (High): AWS IAM connector discards the API response and returns an invented key
- **AR** [#109](https://github.com/jaywedgeworth22/Autorotate/issues/109): 11 (High): VERIFY proves delivery, never that the new credential works
- **AR** [#110](https://github.com/jaywedgeworth22/Autorotate/issues/110): 12 (High): macOS Keychain writes land in the legacy keychain
- **AR** [#111](https://github.com/jaywedgeworth22/Autorotate/issues/111): 13 (High): Android release builds were debug-signed and unminified
- **AR** [#112](https://github.com/jaywedgeworth22/Autorotate/issues/112): 14 (High): Android biometrics was a screen, not a lock
- **AR** [#113](https://github.com/jaywedgeworth22/Autorotate/issues/113): 15 (High): tests never ran in CI; the rotation pipeline had no test

### Issues opened

- **AR** [#97](https://github.com/jaywedgeworth22/Autorotate/issues/97): Epic: full-field security & quality audit remediation (AR-01…AR-35)
- **AR** [#98](https://github.com/jaywedgeworth22/Autorotate/issues/98): 01 (Critical): web control center has no authentication
- **AR** [#99](https://github.com/jaywedgeworth22/Autorotate/issues/99): 02 (Critical): connector with no config mints a fake secret and writes it to live targets
- **AR** [#100](https://github.com/jaywedgeworth22/Autorotate/issues/100): 03 (Critical): demo mode defaulted ON (fail-open)
- **AR** [#101](https://github.com/jaywedgeworth22/Autorotate/issues/101): 04 (Critical): admin-credential encryption key falls back to a repo-published passphrase
- **AR** [#102](https://github.com/jaywedgeworth22/Autorotate/issues/102): 05 (Critical): Android rotation is fabricated; a 6h worker writes fake audit records
- **AR** [#103](https://github.com/jaywedgeworth22/Autorotate/issues/103): 33 (Critical): debug-signed release APK committed to the public repo
- **AR** [#104](https://github.com/jaywedgeworth22/Autorotate/issues/104): 06 (High): web engine commits a rotation with zero targets
- **AR** [#105](https://github.com/jaywedgeworth22/Autorotate/issues/105): 07 (High): audit chain races itself and cannot be repaired
- **AR** [#106](https://github.com/jaywedgeworth22/Autorotate/issues/106): 08 (High): Apple audit log is not hash-chained
- **AR** [#107](https://github.com/jaywedgeworth22/Autorotate/issues/107): 09 (High): unauthenticated SSRF; stored webhook URLs handed to any caller
- **AR** [#108](https://github.com/jaywedgeworth22/Autorotate/issues/108): 10 (High): AWS IAM connector discards the API response and returns an invented key
- **AR** [#109](https://github.com/jaywedgeworth22/Autorotate/issues/109): 11 (High): VERIFY proves delivery, never that the new credential works
- **AR** [#110](https://github.com/jaywedgeworth22/Autorotate/issues/110): 12 (High): macOS Keychain writes land in the legacy keychain
- **AR** [#111](https://github.com/jaywedgeworth22/Autorotate/issues/111): 13 (High): Android release builds were debug-signed and unminified
- **AR** [#112](https://github.com/jaywedgeworth22/Autorotate/issues/112): 14 (High): Android biometrics was a screen, not a lock
- **AR** [#113](https://github.com/jaywedgeworth22/Autorotate/issues/113): 15 (High): tests never ran in CI; the rotation pipeline had no test
- **CT** [#2248](https://github.com/jaywedgeworth22/Congress.Trade/issues/2248): Options & Kalshi event contract account separation, distinct settings & exact pricing
- **CL** [#30](https://github.com/jaywedgeworth22/ContactLogo/issues/30): Pickup PR #24 local compile + merge main
- **DD** [#204](https://github.com/jaywedgeworth22/DealDex/issues/204): 2026-08-26 — IN PROGRESS — Full-app review remediation (branch
- **DD** [#206](https://github.com/jaywedgeworth22/DealDex/issues/206): 2026-08-26 — IN PROGRESS — Full-app review remediation (branch
- **DD** [#207](https://github.com/jaywedgeworth22/DealDex/issues/207): 2026-08-27 — DEPLOYER — IN PROGRESS — Datadog web logs + APM + RUM (#183
- **ST** [#3119](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3119): Migrate RAG vector embeddings & SEC chunk retrieval to Supabase Vector with hard spend caps
- **UM** [#1370](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1370): Add Backblaze B2 App Usage Breakdown chart to Web & iOS dashboard
- **OPS** [#4](https://github.com/jaywedgeworth22/fleet-ops/issues/4): BotFleet (OpenMausBot) iOS release binary upload to App Store Connect

### Effort board

- **CT** `Antigravity` 2026-08-27 — COMPLETED/DEPLOYED #2246 (`946866ea`) — Datadog APM tracing alignment with Socratic.Trade on us5.datadoghq.com (branch `antigravity/datadog-apm-parity`). Added DATADOG_API_KEY and DATADOG_APP_KEY aliases, default site fallback to us5.datadoghq.com, DD_AGENT_HOST / DD_TRACE_AGENT_URL support, npm:dd-trace Deno APM initialization, and HTTP / outbound fetch / queue APM spans. L
- **CT** `Antigravity` `Grok` 2026-08-27 — COMPLETED/MERGED #2243 (`ae79e816`) — Restore iOS build number format to 1.0.# (timestamp) (branch `antigravity/restore-ios-timestamp-build-number`). Reverted — bot's removal of timestamp in CFBundleVersion (`1.0.81 (1.0.81)` -> `1.0.# (YYYYMMDDHHMM)`). Marketing version stays 1.0.# (`CFBundleShortVersionString`) and UTC timestamp is restored for `CFBundleVersion` so App S
- **CT** `Antigravity` 2026-08-27 — COMPLETED/MERGED #2241 (`b5cb1fd9`) — iOS UI polish across Trends, Directory, Delivery, Filter controls, and Ticker/Politician sheets (branch `antigravity/ios-ui-polish-trends-directory-delivery`). Refined Trends Market Snapshot KPI grid to 3-per-row with responsive 2-per-row fallback (`ViewThatFits`), darkened filter dropdowns & symbols on Trends/Trades (`glyphGrey` = label
- **UM** `Claude` 2026-08-27 — COMPLETED (ops heal, docs PR) — Litestream B2 L0 corrupt-object heal. Post-#1368 the retry storm persisted: deterministic `close reader 14: file checksum mismatch` = corrupt L0 `26855`; every ~30-60s retry re-read 5,557 L0 objects (~1 GB) from B2 for ~2.2 days — the shared Backblaze daily-cap burn. Deleted 4,994 objects wholly below the newest L9 snapshot boundary `27bc
- **UM** `Claude` 2026-08-27 — IN PR — Litestream B2 multipart fix: part-size 10MB + concurrency 2 (branch `claude/litestream-b2-part-size`). L1 compaction against B2 was wedged in a retry storm (119 "compaction failed" checksum-mismatch multiparts in ~2h on 2026-08-27), burning the shared Backblaze daily transaction caps. Mirrors Socratic.Trade's proven 2026-08-07/22 fix. YAML-only. Rollout: `docs
- **DD** 2026-08-27 — DEPLOYER — IN PROGRESS — Datadog web logs + APM + RUM (#183 rebase). Branch `cursor/datadog-web-observability-4edf`. Infisical SOT. Vercel machine identity only. No extra-ship
- **DD** `Claude` 2026-08-26 — IN PROGRESS — Full-app review remediation (branch `claude/full-app-evaluation-893vtd`). Owner asked for a full evaluation of website, backend, iOS and Android, then for every finding to be fixed. Landed: valuation engine (circular matcher, grade never reaching the book, per-desk conflict detection, `decodeHtml` no-ops, HP-stat-as-condition on all three clients), n
- **CL** `Grok` `Claude` 2026-08-27 — IN PROGRESS — Pickup — PR #24 local compile (board 30af32b2, issue #30, worktree `~/apps/contactlogo — eval` @ `claude/full-app-evaluation-wwwwk1`). Native Swift/Android compiled for the first time. Golden corpus now runs in Swift, TypeScript, and Kotlin. `UIBackgroundModes=processing` is in the built iOS Info.plist. PR #24 still draft-to-ready; owner decis
- **AFC** `Grok` 2026-08-27 — IN PROGRESS — TUI drive follow-ups + cloud hop (`grok/tui-drive-cloudhop`). Board `56cc91fd`. Worktree `~/apps/fleet — cloudhop`. Install-on-merge, await-next-turn, pendingTool, self-guard, tracked seat-mcp launchers, cloud MCP hop `agents.jays.services`. Generic any-seat
- **AFC** `Grok` `Cursor` 2026-08-27 — IN PROGRESS — Bot drive for live — TUI sessions (`grok/tui-drive`). Board `d854b8b4`. Worktree `~/apps/fleet — drive`. leader-client `prompt`/`peek`, ` .py`, seat-mcp v1.1 `grok_sessions_list`/`grok_session_prompt`, skill `drive — tui` (GB + ). Handshake ok; list 30 sessions / 2 live. Did not inject a test prompt into the live TUI

## 2026-08-26

*65 PRs merged · 14 issues opened · 14 issues closed · 14 effort rows*

### Merged PRs

- **AR** [#63](https://github.com/jaywedgeworth22/Autorotate/pull/63): feat(branding): Autorotate.Codes branding, ASC export compliance & screenshot assets _(by jaywedgeworth22)_
- **AR** [#76](https://github.com/jaywedgeworth22/Autorotate/pull/76): docs(audit): full field audit of web, backend, Apple and Android surfaces _(by jaywedgeworth22)_
- **AR** [#83](https://github.com/jaywedgeworth22/Autorotate/pull/83): fix(build): untrack android/local.properties and canonicalize macOS bundle ID _(by jaywedgeworth22)_
- **AR** [#84](https://github.com/jaywedgeworth22/Autorotate/pull/84): perf(vercel): add Vite vercel config with asset caching and security headers _(by jaywedgeworth22)_
- **AR** [#86](https://github.com/jaywedgeworth22/Autorotate/pull/86): docs(audit): truthing Mac agent and SECURITY contact (AR-22, AR-23) _(by jaywedgeworth22)_
- **AR** [#87](https://github.com/jaywedgeworth22/Autorotate/pull/87): chore(repo): repo hygiene — untrack build artifacts, stop debug-signing Android releases _(by jaywedgeworth22)_
- **AR** [#89](https://github.com/jaywedgeworth22/Autorotate/pull/89): fix(web): AA contrast, mobile console layout, dead chrome, code splitting _(by jaywedgeworth22)_
- **AR** [#90](https://github.com/jaywedgeworth22/Autorotate/pull/90): fix(android): remove fabricated rotation, bind Keystore key to auth, fix QR pairing _(by jaywedgeworth22)_
- **AR** [#91](https://github.com/jaywedgeworth22/Autorotate/pull/91): fix(core): hash-chain the Apple audit log, unify fingerprint length, use the macOS data-protection keychain (AR-08, AR-12, AR-18) _(by jaywedgeworth22)_
- **AR** [#93](https://github.com/jaywedgeworth22/Autorotate/pull/93): fix(web): authentication, fail-closed rotation engine, serialized audit chain, SSRF guard, real alerts, CI tests (AR-01..AR-21) _(by jaywedgeworth22)_
- **AR** [#94](https://github.com/jaywedgeworth22/Autorotate/pull/94): feat(apple): surface audit-chain verification and fix sentence spacing _(by jaywedgeworth22)_
- **AR** [#95](https://github.com/jaywedgeworth22/Autorotate/pull/95): docs(audit): record remediation status _(by jaywedgeworth22)_
- **CT** [#2222](https://github.com/jaywedgeworth22/Congress.Trade/pull/2222): fix(ios): ASC 2.1(a) login responsiveness + 2.1(b) IAP purchase errors _(by jaywedgeworth22)_
- **CT** [#2223](https://github.com/jaywedgeworth22/Congress.Trade/pull/2223): feat(admin,ingest,prices): streamline admin auth, gov interval brackets, and 24h price snapshots _(by jaywedgeworth22)_
- **CT** [#2224](https://github.com/jaywedgeworth22/Congress.Trade/pull/2224): fix(ingest): preserve probe brackets on provider seed upgrades and send from scout _(by jaywedgeworth22)_
- **CT** [#2225](https://github.com/jaywedgeworth22/Congress.Trade/pull/2225): docs(asc): update App Store release checklist with live review status _(by jaywedgeworth22)_
- **CT** [#2226](https://github.com/jaywedgeworth22/Congress.Trade/pull/2226): fix(deno): guard unhandled rejections and unpdf extraction errors _(by jaywedgeworth22)_
- **CT** [#2227](https://github.com/jaywedgeworth22/Congress.Trade/pull/2227): fix(sentry): drop expected unpdf XRef noise (CONGRESS-TRADE-1C) _(by jaywedgeworth22)_
- **CT** [#2228](https://github.com/jaywedgeworth22/Congress.Trade/pull/2228): docs: provider-missing stub auto-close after #2221 _(by jaywedgeworth22)_
- **CT** [#2229](https://github.com/jaywedgeworth22/Congress.Trade/pull/2229): fix(ios): Color.secondary vs Color.red on sign-in notice _(by jaywedgeworth22)_
- **CT** [#2231](https://github.com/jaywedgeworth22/Congress.Trade/pull/2231): fix(extract): self-close NTR scans, EO.Pdf columns, Deleted rows _(by jaywedgeworth22)_
- **CT** [#2232](https://github.com/jaywedgeworth22/Congress.Trade/pull/2232): docs: update release checklist and notes for iOS v1.0.177 resubmission _(by jaywedgeworth22)_
- **CT** [#2233](https://github.com/jaywedgeworth22/Congress.Trade/pull/2233): fix(extract): close Deleted/NTR rows as verified_empty _(by jaywedgeworth22)_
- **CT** [#2236](https://github.com/jaywedgeworth22/Congress.Trade/pull/2236): fix(ios-ship): use 1.0.N for CFBundleVersion _(by jaywedgeworth22)_
- **CL** [#25](https://github.com/jaywedgeworth22/ContactLogo/pull/25): fix(pipeline-vcard): drop dead candidate images and preserve raw vCard properties _(by jaywedgeworth22)_
- **CL** [#26](https://github.com/jaywedgeworth22/ContactLogo/pull/26): fix(vcard): emit data URI photo syntax for vCard 4.0 export _(by jaywedgeworth22)_
- **CL** [#27](https://github.com/jaywedgeworth22/ContactLogo/pull/27): perf(vercel): add Vite vercel config with asset caching and security headers _(by jaywedgeworth22)_
- **CL** `Claude` [#28](https://github.com/jaywedgeworth22/ContactLogo/pull/28): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **DD** [#196](https://github.com/jaywedgeworth22/DealDex/pull/196): fix(auth-scan): resolve review comments on OAuth pairs, scan guard, and login redirect _(by jaywedgeworth22)_
- **DD** [#197](https://github.com/jaywedgeworth22/DealDex/pull/197): perf(vercel): add asset caching, security headers, and clean URLs _(by jaywedgeworth22)_
- **DD** [#199](https://github.com/jaywedgeworth22/DealDex/pull/199): fix(auth): reject off-origin login redirect after OAuth _(by jaywedgeworth22)_
- **DD** [#200](https://github.com/jaywedgeworth22/DealDex/pull/200): fix(ios-ship): use 1.0.N for CFBundleVersion _(by jaywedgeworth22)_
- **DD** `Claude` [#202](https://github.com/jaywedgeworth22/DealDex/pull/202): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **PS** [#35](https://github.com/jaywedgeworth22/Personal-Site/pull/35): fix(mirror): preserve landed project blurbs in daily site mirror _(by jaywedgeworth22)_
- **PS** [#36](https://github.com/jaywedgeworth22/Personal-Site/pull/36): fix(mirror): match replacement keys to actual mirrored blurbs _(by jaywedgeworth22)_
- **PS** [#38](https://github.com/jaywedgeworth22/Personal-Site/pull/38): fix(prod,branding): update DealDex logo, add CTS acronym, and fix Datadog production build _(by jaywedgeworth22)_
- **PS** [#40](https://github.com/jaywedgeworth22/Personal-Site/pull/40): feat(datadog): support PERSONALSITE_DD_ prefixed keys from Infisical _(by jaywedgeworth22)_
- **PS** [#42](https://github.com/jaywedgeworth22/Personal-Site/pull/42): perf(vercel): add ignoreCommand, asset caching, security headers, and clean URLs _(by jaywedgeworth22)_
- **PS** `Claude` [#44](https://github.com/jaywedgeworth22/Personal-Site/pull/44): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **ST** [#3105](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3105): fix(guardrails,stops): resolve reviewer feedback on capabilities, market hours, and short stop fallbacks _(by jaywedgeworth22)_
- **ST** [#3106](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3106): docs: record PR #3105 resolution in docs/EFFORT-LOG.md _(by jaywedgeworth22)_
- **ST** [#3107](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3107): UI Fixes, Litestream Budget, & iOS Authentication Fixes _(by jaywedgeworth22)_
- **ST** [#3108](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3108): Fix APNs contract for roic_status_advisory _(by cursor[bot])_
- **ST** [#3113](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3113): fix(ios,ci): consolidate review-debt leftovers for fleet publish _(by jaywedgeworth22)_
- **ST** [#3114](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3114): docs: close out review-debt leftovers PR #3113 _(by jaywedgeworth22)_
- **ST** `Claude` [#3115](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3115): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **UM** [#1356](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1356): docs: Coolify replica-status probe after #1354/#1355 _(by jaywedgeworth22)_
- **UM** [#1360](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1360): fix(adapters): resolve Namecheap adapter review comments _(by jaywedgeworth22)_
- **UM** [#1361](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1361): fix: resolve reviewer feedback across PRs #1352, #1354, #1356, #1357, #1358, #1360 _(by jaywedgeworth22)_
- **UM** [#1362](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1362): fix(ios): link ASC p8 before xcodebuild archive _(by jaywedgeworth22)_
- **UM** [#1363](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1363): feat(ios): add native iOS Settings-style long-press to copy _(by jaywedgeworth22)_
- **UM** [#1364](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1364): docs(effort-log): mark iOS long-press to copy PR #1363 completed _(by jaywedgeworth22)_
- **UM** [#1365](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1365): fix(ios-ship): use 1.0.N for CFBundleVersion _(by jaywedgeworth22)_
- **UM** `Claude` [#1367](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1367): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **AFC** [#122](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/122): fix(janitor): add simulator cache pruning and suffixed worktree dep reaping _(by jaywedgeworth22)_
- **AFC** [#123](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/123): fix(fleet): audit and resolve reviewer comments on acp bridges and maintenance _(by jaywedgeworth22)_
- **AFC** [#124](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/124): docs(effort): close out fleet reviewer comments audit and resolution _(by jaywedgeworth22)_
- **AFC** [#125](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/125): fix(mac): do not simctl shutdown all on the 4h cleanup tick _(by jaywedgeworth22)_
- **AFC** [#126](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/126): fix(acp): reset cancel flag per turn and track baseline messages by identity _(by jaywedgeworth22)_
- **AFC** `Antigravity` [#127](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/127): fix future digest dates _(by jaywedgeworth22)_
- **AFC** [#128](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/128): docs: add binding rules for solving root causes and not burying issues in prose _(by jaywedgeworth22)_
- **AFC** `Claude` [#129](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/129): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **CTS** `Codex` [#287](https://github.com/jaywedgeworth22/congress-trading-shared/pull/287): fix : clean up subshell auth file and fix history filter stdin _(by jaywedgeworth22)_
- **CTS** `Claude` [#288](https://github.com/jaywedgeworth22/congress-trading-shared/pull/288): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_
- **OPS** `Claude` [#3](https://github.com/jaywedgeworth22/fleet-ops/pull/3): feat(cloud): — Cloud setup script _(by jaywedgeworth22)_

### Issues closed

- **AR** [#77](https://github.com/jaywedgeworth22/Autorotate/issues/77): Inline navigation bar title display mode across iOS views — · COMPLETED
- **AR** [#78](https://github.com/jaywedgeworth22/Autorotate/issues/78): Rebrand (Autorotate.codes), Native Android Companion App & Apple
- **AR** [#79](https://github.com/jaywedgeworth22/Autorotate/issues/79): Web and iOS utility and power enhancements — · PR
- **AR** [#80](https://github.com/jaywedgeworth22/Autorotate/issues/80): Fleet onboarding — join ai-fleet-coordinator as app Autorotate (TS). KIMI
- **AR** [#81](https://github.com/jaywedgeworth22/Autorotate/issues/81): Merge — App Builder PWA with this monorepo — · merged as
- **AR** [#82](https://github.com/jaywedgeworth22/Autorotate/issues/82): Apache-2.0 + Kimi dump backup + catalog fold-in — · PR
- **AR** [#85](https://github.com/jaywedgeworth22/Autorotate/issues/85): 2026-08-26 — COMPLETED — Add Vercel free feature optimizations
- **CT** [#2230](https://github.com/jaywedgeworth22/Congress.Trade/issues/2230): Publisher: drain 3 terminal review-queue rows + self-close similar filings
- **CT** [#2234](https://github.com/jaywedgeworth22/Congress.Trade/issues/2234): 2026-08-26 — COMPLETED — Submit Congress.Trade iOS 1.0.177 with
- **CT** [#2235](https://github.com/jaywedgeworth22/Congress.Trade/issues/2235): 2026-08-26 — COMPLETED/MERGED (#2225 5bd14d30) — App Store
- **DD** [#198](https://github.com/jaywedgeworth22/DealDex/issues/198): 2026-08-26 — COMPLETED — Add Vercel free feature optimizations
- **PS** [#39](https://github.com/jaywedgeworth22/Personal-Site/issues/39): 2026-08-26 — COMPLETED — Update DealDex logo, add CTS acronym, and fix
- **PS** [#41](https://github.com/jaywedgeworth22/Personal-Site/issues/41): 2026-08-26 — COMPLETED — Add PERSONALSITEDD prefixed key support and sync
- **PS** [#43](https://github.com/jaywedgeworth22/Personal-Site/issues/43): 2026-08-26 — COMPLETED — Add Vercel free feature optimizations

### Issues opened

- **AR** [#77](https://github.com/jaywedgeworth22/Autorotate/issues/77): Inline navigation bar title display mode across iOS views — · COMPLETED
- **AR** [#78](https://github.com/jaywedgeworth22/Autorotate/issues/78): Rebrand (Autorotate.codes), Native Android Companion App & Apple
- **AR** [#79](https://github.com/jaywedgeworth22/Autorotate/issues/79): Web and iOS utility and power enhancements — · PR
- **AR** [#80](https://github.com/jaywedgeworth22/Autorotate/issues/80): Fleet onboarding — join ai-fleet-coordinator as app Autorotate (TS). KIMI
- **AR** [#81](https://github.com/jaywedgeworth22/Autorotate/issues/81): Merge — App Builder PWA with this monorepo — · merged as
- **AR** [#82](https://github.com/jaywedgeworth22/Autorotate/issues/82): Apache-2.0 + Kimi dump backup + catalog fold-in — · PR
- **AR** [#85](https://github.com/jaywedgeworth22/Autorotate/issues/85): 2026-08-26 — COMPLETED — Add Vercel free feature optimizations
- **CT** [#2230](https://github.com/jaywedgeworth22/Congress.Trade/issues/2230): Publisher: drain 3 terminal review-queue rows + self-close similar filings
- **CT** [#2234](https://github.com/jaywedgeworth22/Congress.Trade/issues/2234): 2026-08-26 — COMPLETED — Submit Congress.Trade iOS 1.0.177 with
- **CT** [#2235](https://github.com/jaywedgeworth22/Congress.Trade/issues/2235): 2026-08-26 — COMPLETED/MERGED (#2225 5bd14d30) — App Store
- **DD** [#198](https://github.com/jaywedgeworth22/DealDex/issues/198): 2026-08-26 — COMPLETED — Add Vercel free feature optimizations
- **PS** [#39](https://github.com/jaywedgeworth22/Personal-Site/issues/39): 2026-08-26 — COMPLETED — Update DealDex logo, add CTS acronym, and fix
- **PS** [#41](https://github.com/jaywedgeworth22/Personal-Site/issues/41): 2026-08-26 — COMPLETED — Add PERSONALSITEDD prefixed key support and sync
- **PS** [#43](https://github.com/jaywedgeworth22/Personal-Site/issues/43): 2026-08-26 — COMPLETED — Add Vercel free feature optimizations

### Effort board

- **CT** `Grok` 2026-08-26 — IN PR — Publisher drain of 3 terminal review-queue rows + self-close pipeline (issue #2230, board `3390fd23`, branch `grok/review-queue-terminal`, worktree `~/apps/congress — terminal`). Live: confirmed Cohen `H-2026-20035235` (2 official buys); rejected Hern `H-2026-20035196` as later official amendment of persisted `H-2026-20035134`; rejected Rogers `H-2026-911
- **CT** `Antigravity` 2026-08-26 — COMPLETED / IN PR (branch `antigravity/update-asc-release-checklist`) — Update App Store release checklist with live ASC review status and merged features. Updated CHECKLIST_FOR_ASC_PUBLIC_RELEASE.md to reflect the live ASC status as of Aug 26, 2026 (submission `b174dd86` state UNRESOLVED_ISSUES / version 1.0.81 REJECTED), documented Apple review feedback on Guidelines 2.1(a)
- **CT** `Antigravity` 2026-08-26 — COMPLETED (branch `antigravity/admin-auth-and-probe-intervals`) — Streamline Admin & Review Queue UI, Government Poll Interval Brackets, and 24h Price Snapshots. Verified session-based admin recognition without secondary login dialogs or browser token popups (`canUseAdmin()` unlocked via `ADMIN_EMAILS` session allowlist). Durably recorded previous check timestamp ($T
- **CT** `Antigravity` 2026-08-26 — COMPLETED — Submit Congress.Trade iOS 1.0.177 with Guideline 2.1(a) and 2.1(b) fixes. Built fresh Tahoe GM binary 202608262138 on GitHub-hosted macos-latest (run 33016281432), updated ASC version 1.0.177, attached build 29d9c081, attached 4 items (version + group 3a37da1c + monthly efbef974 + annual f85b493e), verified physical-device deletion video (COMPLETE)
- **CT** `Antigravity` 2026-08-26 — COMPLETED/MERGED (#2225 `5bd14d30`) — App Store release checklist update. Updated CHECKLIST_FOR_ASC_PUBLIC_RELEASE.md with August 26, 2026 live ASC state, rejected submission b174dd86 summary, and Guideline 2.1(a) / 2.1(b) resolution path
- **UM** `Antigravity` 2026-08-26 — COMPLETED/MERGED #1363 `5d2c580f` — Native iOS Settings-style long-press to copy (branch `ag/ios-long-press-copy`). Implemented system-wide native iOS Settings-style long-press to copy (`CopyableValueModifier`, `.copyableRow(label:value:)`, `.copyableValue(_:label:)`, and `CopyableLabeledContent`) across DesignSystem, Settings, Computers, Agents, Platforms, ServerSt
- **UM** `Antigravity` `Claude` 2026-08-26 — COMPLETED — Comprehensive PR review fixes & thread resolution (branch `antigravity/reviewer-feedback-fixes`). Resolved reviewer feedback across PRs #1352 / #1354 / #1356 / #1357 / #1358 / #1360: included retained rollups from `ExternalUsageEventDailyRollup` in All Time agent aggregations, preserved the — `service= -code` discriminator, reconciled 5h b
- **DD** `Antigravity` 2026-08-26 — COMPLETED — Add Vercel free feature optimizations (branch `antigravity/vercel-optimizations`). Updated `vercel.json` with immutable 1-year cache-control headers for static build assets (`/assets/(.)`), stale-while-revalidate caching for media/fonts/favicons, strict security headers (nosniff, sameorigin, referrer-policy, permissions-policy), clean URLs, and t
- **PS** `Antigravity` 2026-08-26 — COMPLETED — Add Vercel free feature optimizations (branch `antigravity/vercel-optimizations`). Updated `site/vercel.json` with `ignoreCommand` to skip redundant builds on non-site repo edits, immutable 1-year cache headers for build assets, media/font cache-control headers, strict security headers (nosniff, sameorigin, referrer-policy, permissions-policy), cl
- **PS** `Antigravity` 2026-08-26 — COMPLETED — Add PERSONALSITE_DD_ prefixed key support and sync all app Datadog secrets into Infisical shared workspace (branch ag/infisical-prefixed-keys). Wired PERSONALSITE_DD_ key fallbacks in fail-closed.ts and vite.config.ts. Synchronized Datadog secrets for Personal-Site, ContactLogo, DealDex, and Autorotate into shared-at-ct Infisical workspace
- **PS** `Antigravity` 2026-08-26 — COMPLETED — Update DealDex logo, add CTS acronym, and fix Datadog production deployment (branch ag/dealdex-logo-future-dates-prod-fix). Replaced DealDex app icon with official 1024px icon. Added CTS acronym fallback for Congress Trading Shared. Fixed assertDatadogKeysOrThrow to prevent aborting Vercel production build when DD_ are unset
- **AR** `Antigravity` 2026-08-26 — COMPLETED — Add Vercel free feature optimizations (branch `antigravity/vercel-optimizations`). Created `apps/web/vercel.json` with Vite framework preset, 1-year immutable cache headers for build assets (`/assets/(.)`), stale-while-revalidate headers for static media/fonts, strict security headers (nosniff, sameorigin, referrer-policy, permissions-policy), cl
- **CL** `Antigravity` 2026-08-26 — COMPLETED — Add Vercel free feature optimizations (branch `antigravity/vercel-optimizations`). Created `web/vercel.json` with Vite framework preset, 1-year immutable cache headers for build assets (`/assets/(.)`), stale-while-revalidate headers for static media/fonts, strict security headers (nosniff, sameorigin, referrer-policy, permissions-policy), clean U
- **AFC** `Antigravity` 2026-08-26 — DEPLOYED/MERGED #123 — Audit and resolve reviewer comments across past 2 weeks. Claimed Wed, Aug 26, 2026. Fixed mac-auto-cleanup worktree idle/clean checks and agent-sync runtime preservation (#122), dsh-acp watchdog timeout, session/load resume, supported mode restriction (#110, #111), cursor_acp_cloud_bridge authMethods and follow-up response wait (#75), and regis

## 2026-08-25

*25 PRs merged · 7 issues opened · 8 issues closed · 28 effort rows*

### Merged PRs

- **CT** [#2213](https://github.com/jaywedgeworth22/Congress.Trade/pull/2213): Mirror 2026-08-23 full-stack review onto effort log _(by jaywedgeworth22)_
- **CT** [#2215](https://github.com/jaywedgeworth22/Congress.Trade/pull/2215): chore(deps-dev): bump eslint from 10.8.1 to 10.9.0 in /app _(by dependabot[bot])_
- **CT** [#2216](https://github.com/jaywedgeworth22/Congress.Trade/pull/2216): chore(deps): bump @aws-sdk/client-s3 from 3.1115.0 to 3.1116.0 in /app _(by dependabot[bot])_
- **CT** [#2217](https://github.com/jaywedgeworth22/Congress.Trade/pull/2217): fix(ios): open filing alerts that only send camelCase keys _(by jaywedgeworth22)_
- **CT** [#2218](https://github.com/jaywedgeworth22/Congress.Trade/pull/2218): iOS disclaimer, push alerts, watchlist, and theme overhaul _(by jaywedgeworth22)_
- **CT** [#2219](https://github.com/jaywedgeworth22/Congress.Trade/pull/2219): Email-only admin UI + review_queue publisher webhook _(by jaywedgeworth22)_
- **CT** [#2220](https://github.com/jaywedgeworth22/Congress.Trade/pull/2220): docs: prod ADMIN_EMAILS session allowlist investigation (env-only) _(by jaywedgeworth22)_
- **CT** [#2221](https://github.com/jaywedgeworth22/Congress.Trade/pull/2221): Auto-reject provider-missing stubs when official filing is persisted _(by jaywedgeworth22)_
- **CL** [#19](https://github.com/jaywedgeworth22/ContactLogo/pull/19): feat(web): high-res logo sources, crop studio modal, drag-drop uploads & review-first safety _(by jaywedgeworth22)_
- **CL** [#20](https://github.com/jaywedgeworth22/ContactLogo/pull/20): docs(effort-log): mark high-res logos, drag-drop, and crop modal completed _(by jaywedgeworth22)_
- **CL** [#21](https://github.com/jaywedgeworth22/ContactLogo/pull/21): feat(web): delta vCard export, ticker logos, Brandfetch, Logo.dev & low-res filter _(by jaywedgeworth22)_
- **CL** [#22](https://github.com/jaywedgeworth22/ContactLogo/pull/22): fix(web): stop review livelock on tiny favicons _(by jaywedgeworth22)_
- **DD** [#190](https://github.com/jaywedgeworth22/DealDex/pull/190): Configure Google/Apple/X OAuth aliases and overhaul Web Scan UI _(by jaywedgeworth22)_
- **PS** [#33](https://github.com/jaywedgeworth22/Personal-Site/pull/33): feat(work): format project domains, add blue hyperlinks, and GitHub action buttons _(by jaywedgeworth22)_
- **ST** [#3103](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3103): chore(ios): commit generated AppUpdatePromptTests pbxproj _(by jaywedgeworth22)_
- **ST** [#3104](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3104): docs: close out #3103 leftover pbxproj after squash 64a06e78 _(by jaywedgeworth22)_
- **UM** [#1350](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1350): feat(ios): widget topics Mac, Alerts, Providers _(by jaywedgeworth22)_
- **UM** [#1351](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1351): fix(ios): add GlanceWidgets.swift to widget extension compile sources _(by jaywedgeworth22)_
- **UM** [#1354](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1354): fix(replica-probe): ltx -json levels 0-3/9, classify B2 timeouts, stop argv secret leak _(by jaywedgeworth22)_
- **UM** [#1355](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1355): fix(replica-probe): do not skip host fallback on cred-less heartbeat _(by jaywedgeworth22)_
- **UM** [#1357](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1357): fix(r2): bill GB-month so a 22 GiB August peak is not hidden as 2% _(by jaywedgeworth22)_
- **UM** [#1358](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1358): Namecheap adapter, app icon favicon, Twilio SMS gateway, Hetzner CX53/CAX41 watcher & compact density _(by jaywedgeworth22)_
- **UM** [#1359](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1359): fix(ios): resolve async autoclosure and double unwrap in swift tests _(by jaywedgeworth22)_
- **AFC** [#119](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/119): fix(ci): make git push non-fatal for branch rules and add all fleet repos _(by jaywedgeworth22)_
- **AFC** `Antigravity` [#120](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/120): Add thin ACP wrapper so Shellular can list — sessions _(by jaywedgeworth22)_

### Issues closed

- **AR** [#55](https://github.com/jaywedgeworth22/Autorotate/issues/55): Owner: Developer portal App IDs for Autorotate — leftover from . Git
- **DD** [#191](https://github.com/jaywedgeworth22/DealDex/issues/191): 2026-08-24 — COMPLETED/MERGED #167 (b6cad4d) — Switch iOS CI & Actions
- **DD** [#192](https://github.com/jaywedgeworth22/DealDex/issues/192): 2026-08-25 — COMPLETED — Configure Google/Apple/X OAuth from
- **DD** [#193](https://github.com/jaywedgeworth22/DealDex/issues/193): 2026-08-23 — COMPLETED/MERGED #163 — Settings appearance 3-way +
- **DD** [#194](https://github.com/jaywedgeworth22/DealDex/issues/194): 2026-08-23 — COMPLETED - OG share: drop TCGPlayer, DealDex.net
- **DD** [#195](https://github.com/jaywedgeworth22/DealDex/issues/195): 2026-08-23 — COMPLETED/MERGED #156 — OG share card. TCGPlayer dropped
- **PS** [#34](https://github.com/jaywedgeworth22/Personal-Site/issues/34): 2026-08-25 — COMPLETED — Project domains, hyperlinks, GitHub card buttons
- **UM** [#1346](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1346): [Uptime] Usage Monitor production is stale vs main

### Issues opened

- **CT** [#2214](https://github.com/jaywedgeworth22/Congress.Trade/issues/2214): 2026-08-23 — PLANNED — Live full-stack review children (no product
- **DD** [#191](https://github.com/jaywedgeworth22/DealDex/issues/191): 2026-08-24 — COMPLETED/MERGED #167 (b6cad4d) — Switch iOS CI & Actions
- **DD** [#192](https://github.com/jaywedgeworth22/DealDex/issues/192): 2026-08-25 — COMPLETED — Configure Google/Apple/X OAuth from
- **DD** [#193](https://github.com/jaywedgeworth22/DealDex/issues/193): 2026-08-23 — COMPLETED/MERGED #163 — Settings appearance 3-way +
- **DD** [#194](https://github.com/jaywedgeworth22/DealDex/issues/194): 2026-08-23 — COMPLETED - OG share: drop TCGPlayer, DealDex.net
- **DD** [#195](https://github.com/jaywedgeworth22/DealDex/issues/195): 2026-08-23 — COMPLETED/MERGED #156 — OG share card. TCGPlayer dropped
- **PS** [#34](https://github.com/jaywedgeworth22/Personal-Site/issues/34): 2026-08-25 — COMPLETED — Project domains, hyperlinks, GitHub card buttons

### Effort board

- **CT** `Cursor` 2026-08-26 — IN PR — Docs: provider-missing stub auto-close after #2221 (branch `cursor/docs-provider-missing-stub-close`). #2221 landed the live observation reject; July 22 rollout and B6 still described create-only / backlog. Added `docs/rollouts/2026-08-25-provider-missing-stub-close.md` (match order, persisted-only close, no historic sweep, operator SQL). Pointed July 22 follow
- **CT** `Cursor` 2026-08-25 — IN PR — iOS ASC 2.1(a)/(b): login responsiveness + IAP purchase errors (branch `cursor/ios-asc-login-iap-fixes-b12e`). Reviewer iPad Air 11-inch: Sign in with Apple looked hung (no progress/disable); Premium purchase errors used post-charge redeem copy before Apple charged. `SignInPanel` now shows Apple/Google busy state + inline notices; `PremiumPricing.purchaseFailure
- **CT** `Cursor` 2026-08-25 — IN PR — Prod session admin allowlist investigation (branch `cursor/admin-emails-env-investigation-7267`). Live `GET /auth/me` → `admin.allowed:false` for signed-in operator after #2219 removed token UI. Code path (`identity.ts` / `parseEmailAllowlist` / `isAdminSessionEmail`) correct. Infisical congress-trade prod key `ADMIN_EMAILS` present but stale (19-char value ≠
- **CT** `Cursor` 2026-08-25 — COMPLETED/MERGED #2219 — Email-only admin + review_queue publisher webhook (branch `cursor/email-admin-review-notify-b7ee`). Removed public Admin Sign-In / token UI from web (`dashboardHtml.ts`); admin gated on `ME.admin.allowed` (session email on `ADMIN_EMAILS` or persisted grant). `ADMIN_TOKEN` stays server-side only. Added fail-closed signed `REVIEW_QUEUE_PUBLISHER_
- **CT** `Cursor` 2026-08-25 — COMPLETED/MERGED #2221 — Auto-reject provider-missing stubs when official filing is persisted (branch `cursor/provider-missing-stub-close-77a0`). FMP latency can open `provider-missing-` review rows before Senate/House discovery lands; when `S-{uuid}` / `H — {id}` (or matching `source_url`) is already `persisted`, the stub now rejects as duplicate on the next provider o
- **CT** `Cursor` 2026-08-25 — IN PR #2212 — Copy pinned AppUpdatePrompt.swift into the Congress.Trade iOS target (branch `cursor/appupdateprompt-file-8688`). Stop inlining the type in `App.swift`. Real file copied from `scripts/ios-fleet/AppUpdatePrompt.swift`. `knownAppleIds` (stale `online.dealdex`) removed from Swift; live DealDex is `net.dealdex` appleId `6802474288` in `apps.json`. Pin kept
- **CT** `Cursor` 2026-08-25 — IN PR — ios-ship: drop `secrets.` from job/step `if` (DealDex #175 class, branch `cursor/ios-ship-secrets-if-0efe`). After #2207/#2209, `ios-ship` is a 0-job fail: GitHub rejects `if: && secrets.ASC_KEY_ID != ''` (`Unrecognized named-value: 'secrets'`). Keep the scheduled ship gate. Map existing team secrets into step env, check `ASC_KEY_ID` there, then run `ios-a
- **CT** `Cursor` 2026-08-25 — IN PR #2210 — Datadog logs + APM + public RUM on the existing account (branch `cursor/datadog-logs-apm-rum-3c8e`). Deno agentless HTTP intake for logs/APM; RUM via `%GA_SCRIPT%` on public HTML. Reuses fleet `DD_API_KEY` / `DD_APP_KEY` / `DD_SITE` plus RUM client-token aliases. Fail closed / no-op on missing or partial keys. No new Datadog plan, no session replay, no D
- **CT** `Cursor` 2026-08-25 — IN PR — iOS inbound trade/member/ticker links + Trends 5xx retry (audit F1/F4, branch `cursor/ios-deeplink-trends-retry-50f4`). `AppDeepLink` parses `https://congress.trade/?trade|member|ticker=` and `congresstrade://` equivalents; `onContinueUserActivity` for Universal Links; missing/unknown queries stay nil; inbound 404 uses the web not-found copy. Trends reuses the T
- **UM** `Antigravity` 2026-08-25 — COMPLETED/MERGED #1359 — Fix iOS Swift package test unwraps (branch `fix/ios-swift-test-unwraps`). Extracted `store.listProviders()` out of `XCTUnwrap` autoclosure and fixed optional Double literal comparisons in `LocalConnectAccountsTests.swift` and `OfflineCacheTests.swift`
- **UM** `Antigravity` 2026-08-25 — COMPLETED/MERGED #1358 — Namecheap adapter, App icon favicon, Twilio SMS gateway, Hetzner watcher & Global Compact Density (branch `ag/namecheap-favicon-hetzner-twilio`). Added Namecheap poll adapter (`src/lib/adapters/namecheap.ts`) and AI agent CLI (`scripts/namecheap.py`) for balance, auto-renew, and domain inventory. Replaced web favicon with multi-resolution R
- **UM** `Antigravity` 2026-08-25 — COMPLETED/MERGED #1357 — Mac Host telemetry parity & dedicated Agents tab (branch `ag/agents-tab-and-mac-parity`). Upgraded Mac watchdog to report dynamic Apple Silicon chip (`Apple M5`), accurate APFS data volume disk usage, Tailscale hostname formatting, grey Not Enabled badges without false alert flags, and full fleet PM2/launchd process monitoring. Added dedica
- **UM** `Cursor` 2026-08-25 — IN PR — Widget topics Mac, Alerts, Providers + dedicated Mac/Alerts tiles (branch `cursor/widget-mac-alerts-providers-ef6c`). Same `services.jays.usage.client.monitor.widget` bundle. Edit Widget lists Budget, LLM Quotas, Servers, Mac, Alerts, Providers. Mac is Computers heartbeat, not Servers → Host. Dedicated Mac (CPU/memory/disk) and Alerts (open list) tiles. Snaps
- **UM** `Cursor` 2026-08-25 — COMPLETED/MERGED #1349 `ebcc972` — Usage Monitor widget topics Budget / LLM Quotas / Servers + Large (branch `cursor/widget-topics-737e`). Existing `services.jays.usage.client.monitor.widget` only. Edit Widget picks topic. Snapshot cache extended for LLM + server tiles. Honest empty/stale. No new ASC app
- **UM** `Cursor` 2026-08-25 — COMPLETED/MERGED #1347 `258e790` — Pin AppUpdatePrompt.swift for both iOS targets (branch `cursor/appupdateprompt-pin-c60e`). One in-repo ios-fleet pin, copied into App + LocalApp. knownAppleIds off Swift (stale online.dealdex) into apps.json. Live DealDex is net.dealdex appleId 6802474288. No Swift package. testers.json untouched. No ` — force-ship`. LocalUsageMoni
- **UM** `Cursor` 2026-08-25 — COMPLETED/MERGED #1341 `d563c8b` — Datadog logs + APM + gated RUM (branch `cursor/datadog-logs-apm-rum-802c`). Existing US5 account only. No new Datadog spend. Fail closed without `DD_SERVICE`. RUM stays dark until the public pair is set. Sentry/PD stay. Do not promote Coolify until Infisical has `DD_SERVICE=usage-monitor` plus `DD_ENV`/`DD_SITE`/`DD_AGENT_HOST`/`DD
- **UM** `Grok` 2026-08-25 — COMPLETED/MERGED #1343 — Hosted ios-ship ASC import (branch `cursor/ios-hosted-asc-import-1a3f`). Run 32795404598 failed: macos-latest has no `~/.secrets/appstore-connect.env`. Import existing team secrets (ASC_KEY_ID / ASC_ISSUER_ID / ASC_KEY_P8 / IOS_DIST_P12_BASE64 / IOS_DIST_P12_PASSWORD) via `ios-appstore-gm-prepare.sh`, same path as ST #3089. Cache `~/.cache/ios-fl
- **DD** `Antigravity` 2026-08-25 — COMPLETED — Configure Google/Apple/X OAuth from secrets & polish Scan UI button layout. Branch `ag/auth-and-scan-ui-polish`, worktree `~/apps/dealdex- `
- **PS** `Antigravity` 2026-08-25 — COMPLETED — Project domains, hyperlinks, GitHub card buttons (branch ag/project-cards-and-domain-links). Formatted project domains (DealDex.net, Autorotate.Codes, Congress.Trade, SocraticTrade.com, ContactLogo.com, usage.jays.services). Rendered domains in project descriptions as un-underlined blue hyperlinks. Added right-arrow + GitHub action buttons to card header
- **PS** `Antigravity` 2026-08-25 — COMPLETED — Add Autorotate and ContactLogo portfolio work cards (branch ag/portfolio-autorotate-and-contactlogo). Updated site.ts and static/index.html with Autorotate (dynamic secret rotation, native macOS/iOS, ar.png) and ContactLogo. Personal-Site itself excluded from portfolio per owner spec
- **PS** `Cursor` 2026-08-25 — COMPLETED — Designer leftover UX (visitor blurbs + CL/Fleet icons). PR #22. Copy and icons only. Datadog #19 untouched. No deploy
- **PS** `Cursor` 2026-08-25 — COMPLETED — Datadog logs + APM + RUM. PR #19. Existing Datadog account. Fail closed if keys missing. Replay off. Sentry / PagerDuty unchanged
- **AR** `Antigravity` Inline navigation bar title display mode across iOS views — · COMPLETED 2026-08-25. Applied .navigationBarTitleDisplayMode(.inline) to all NavigationStack root and detail views so centered compact title stays pinned during scroll
- **CL** `Antigravity` 2026-08-25 — COMPLETED — Set inline navigation bar title display mode in ContactLogo iOS (branch ag/ios-inline-nav-titles). Set .navigationBarTitleDisplayMode(.inline) on root NavigationStack
- **CL** `Antigravity` 2026-08-25 — COMPLETED — High-res logo sources (Google 256px, Clearbit 512px), quality baseline filter, 404 error prevention, review-first safety refinement, direct card drag-drop upload, and interactive crop/zoom studio modal. Upgraded web candidate sources (Clearbit 512px, Google 256px, Preferred SVGs); prevented SimpleIcons 404 question mark SVGs via strict slug validation; kep
- **AFC** `Cursor` `Antigravity` `Grok` 2026-08-25 — IN PROGRESS — agy-acp session/list wrapper (`cursor/agy-acp-session-list-2365`). Thin NDJSON proxy so Shellular can list — sessions. Does not rewrite agy-acp. Does not change `start.sh` / `:8765`. Keepouts: agents.json, — acp, launchd
- **AFC** `Cursor` `Grok` 2026-08-25 — COMPLETED — Harden pm2 agy-acp fail-closed (`cursor/agy-acp-fail-closed-387d`, #117). Track turbo.sh; start.sh child is turbo; grace 300s; bind persist via `bind-loopback.cjs`. Keepouts: — acp, Shellular agents.json, session scanner
- **AFC** `Grok` `Cursor` 2026-08-20 — IN PROGRESS — 5-day Mac takeover (through 2026-08-25). Owner: this Mac — TUI takes the — queue. — Bot.app is — (`com.anysphere.sand`) and only launches — cloud agents; local chats already sit on ` `. No — cloud from this seat unless owner asks. Board `c8d325b9`. 2h babysit loop. PR conflicts/CI/comments across ST/CT

## 2026-08-24

*114 PRs merged · 29 issues opened · 17 issues closed · 6 effort rows*

### Merged PRs

- **AR** `Cursor` [#40](https://github.com/jaywedgeworth22/Autorotate/pull/40): docs(repo): document — Cloud dev-environment setup for apps/web _(by jaywedgeworth22)_
- **AR** [#58](https://github.com/jaywedgeworth22/Autorotate/pull/58): feat(release): cross-platform 3D icons, dry-run guard & release builds _(by jaywedgeworth22)_
- **AR** [#68](https://github.com/jaywedgeworth22/Autorotate/pull/68): chore(deps-dev): bump vite from 7.3.0 to 7.3.5 in /backups/secret-rotator/tree _(by dependabot[bot])_
- **AR** [#69](https://github.com/jaywedgeworth22/Autorotate/pull/69): chore(deps-dev): bump postcss from 8.5.6 to 8.5.26 in /backups/secret-rotator/tree _(by dependabot[bot])_
- **AR** [#70](https://github.com/jaywedgeworth22/Autorotate/pull/70): chore(deps-dev): bump js-yaml from 4.1.1 to 4.3.1 in /backups/secret-rotator/tree _(by dependabot[bot])_
- **CT** [#2157](https://github.com/jaywedgeworth22/Congress.Trade/pull/2157): By Sector ink, mobile logo nudge, and grey Directory sort/rows _(by jaywedgeworth22)_
- **CT** [#2169](https://github.com/jaywedgeworth22/Congress.Trade/pull/2169): fix(vision-worker): keep short tickers after Sell/Buy strip _(by jaywedgeworth22)_
- **CT** [#2179](https://github.com/jaywedgeworth22/Congress.Trade/pull/2179): Consume shared tickerLogoPolicy; keep CONFIG_KV jury _(by jaywedgeworth22)_
- **CT** [#2188](https://github.com/jaywedgeworth22/Congress.Trade/pull/2188): fix(ops): CT Pushover app token and Coolify disk hygiene alerts _(by jaywedgeworth22)_
- **CT** [#2189](https://github.com/jaywedgeworth22/Congress.Trade/pull/2189): feat(auth): add X (Twitter) OAuth 2.0 PKCE authentication _(by jaywedgeworth22)_
- **CT** [#2192](https://github.com/jaywedgeworth22/Congress.Trade/pull/2192): chore(deps): bump hono from 4.13.2 to 4.13.3 in /app in the cloudflare group _(by dependabot[bot])_
- **CT** [#2193](https://github.com/jaywedgeworth22/Congress.Trade/pull/2193): chore(deps-dev): bump vitest from 4.1.10 to 4.1.11 in /app in the testing group _(by dependabot[bot])_
- **CT** [#2194](https://github.com/jaywedgeworth22/Congress.Trade/pull/2194): chore(deps): bump @aws-sdk/client-s3 from 3.1112.0 to 3.1115.0 in /app _(by dependabot[bot])_
- **CT** [#2195](https://github.com/jaywedgeworth22/Congress.Trade/pull/2195): chore(deps): bump @google/genai from 2.17.1 to 2.18.0 in /app _(by dependabot[bot])_
- **CT** [#2196](https://github.com/jaywedgeworth22/Congress.Trade/pull/2196): chore(deps-dev): bump @vitest/coverage-v8 from 4.1.10 to 4.1.11 in /app _(by dependabot[bot])_
- **CT** [#2197](https://github.com/jaywedgeworth22/Congress.Trade/pull/2197): fix(uptime): resolve container restart loop and Infisical 401 login fallback _(by jaywedgeworth22)_
- **CT** [#2198](https://github.com/jaywedgeworth22/Congress.Trade/pull/2198): ci: switch iOS workflows and policy checks to GitHub-hosted cloud runners _(by jaywedgeworth22)_
- **CT** [#2202](https://github.com/jaywedgeworth22/Congress.Trade/pull/2202): chore: update VENDOR-PROVENANCE.md to v2.6.0 _(by jaywedgeworth22)_
- **CT** `Antigravity` [#2203](https://github.com/jaywedgeworth22/Congress.Trade/pull/2203): latency snapshots backfill _(by jaywedgeworth22)_
- **CT** [#2204](https://github.com/jaywedgeworth22/Congress.Trade/pull/2204): docs: update effort log for X auth and production stability fixes _(by jaywedgeworth22)_
- **CT** [#2205](https://github.com/jaywedgeworth22/Congress.Trade/pull/2205): chore(deps): bump pillow from 11.2.1 to 12.3.0 in /services/scan-cpu-worker _(by dependabot[bot])_
- **CT** `Cursor` [#2206](https://github.com/jaywedgeworth22/Congress.Trade/pull/2206): fix: — env ports must be objects _(by jaywedgeworth22)_
- **CT** [#2207](https://github.com/jaywedgeworth22/Congress.Trade/pull/2207): fix(ios): seed fleet version publish from remote before PUT _(by jaywedgeworth22)_
- **CT** [#2208](https://github.com/jaywedgeworth22/Congress.Trade/pull/2208): fix(ui): ordinary language for public Admin Sign-In _(by jaywedgeworth22)_
- **CT** [#2209](https://github.com/jaywedgeworth22/Congress.Trade/pull/2209): fix(ios): open trade/member/ticker links and retry Trends 5xx _(by jaywedgeworth22)_
- **CT** [#2210](https://github.com/jaywedgeworth22/Congress.Trade/pull/2210): feat(observability): fail-closed Datadog logs, APM, and public RUM _(by jaywedgeworth22)_
- **CT** [#2211](https://github.com/jaywedgeworth22/Congress.Trade/pull/2211): Do not use secrets in ios-ship if conditions _(by jaywedgeworth22)_
- **CT** [#2212](https://github.com/jaywedgeworth22/Congress.Trade/pull/2212): Copy pinned AppUpdatePrompt.swift into the iOS target _(by jaywedgeworth22)_
- **CL** [#11](https://github.com/jaywedgeworth22/ContactLogo/pull/11): Add CI and point copy at contactlogo.com _(by jaywedgeworth22)_
- **CL** [#13](https://github.com/jaywedgeworth22/ContactLogo/pull/13): Add Datadog logs, APM, and RUM on ContactLogo web _(by jaywedgeworth22)_
- **CL** [#14](https://github.com/jaywedgeworth22/ContactLogo/pull/14): Keep Datadog dark instead of blocking Coolify boot _(by jaywedgeworth22)_
- **CL** [#15](https://github.com/jaywedgeworth22/ContactLogo/pull/15): feat(ios): set inline navigation bar title display mode _(by jaywedgeworth22)_
- **CL** [#16](https://github.com/jaywedgeworth22/ContactLogo/pull/16): fix(android): do not overwrite employee photos on Apply _(by jaywedgeworth22)_
- **DD** [#138](https://github.com/jaywedgeworth22/DealDex/pull/138): Hold dealdex.online redirects until dealdex.net is live _(by jaywedgeworth22)_
- **DD** [#153](https://github.com/jaywedgeworth22/DealDex/pull/153): OG social card: logo-only centered wordmark _(by jaywedgeworth22)_
- **DD** [#167](https://github.com/jaywedgeworth22/DealDex/pull/167): ci(ios): switch iOS ship workflow to macos-latest cloud runner _(by jaywedgeworth22)_
- **DD** [#170](https://github.com/jaywedgeworth22/DealDex/pull/170): Vendor ios-fleet and restore Mac runner so ASC gets 1.0.N _(by jaywedgeworth22)_
- **DD** [#172](https://github.com/jaywedgeworth22/DealDex/pull/172): Put ios-ship back on GitHub-hosted macos-latest _(by jaywedgeworth22)_
- **DD** [#173](https://github.com/jaywedgeworth22/DealDex/pull/173): Stop DealDex ship from wiping the fleet iOS version manifest _(by jaywedgeworth22)_
- **DD** [#175](https://github.com/jaywedgeworth22/DealDex/pull/175): Do not use secrets in ios-ship if conditions _(by jaywedgeworth22)_
- **DD** [#176](https://github.com/jaywedgeworth22/DealDex/pull/176): Accept dealdex in vendored ship-testflight.sh case _(by jaywedgeworth22)_
- **DD** [#178](https://github.com/jaywedgeworth22/DealDex/pull/178): Add skippable Android Play and PWA update alerts _(by jaywedgeworth22)_
- **DD** [#180](https://github.com/jaywedgeworth22/DealDex/pull/180): Center iOS Scan empty-loading spinner _(by jaywedgeworth22)_
- **DD** [#182](https://github.com/jaywedgeworth22/DealDex/pull/182): Fix testers.json Comcast typo (johnwedgeworth) _(by jaywedgeworth22)_
- **DD** [#184](https://github.com/jaywedgeworth22/DealDex/pull/184): fix(observability): do not 503 production when RUM tokens are missing _(by jaywedgeworth22)_
- **DD** [#186](https://github.com/jaywedgeworth22/DealDex/pull/186): feat(ios): set inline navigation bar title display mode across iOS views _(by jaywedgeworth22)_
- **DD** [#188](https://github.com/jaywedgeworth22/DealDex/pull/188): Pin AppUpdatePrompt.swift and move Apple IDs off Swift _(by jaywedgeworth22)_
- **PS** [#16](https://github.com/jaywedgeworth22/Personal-Site/pull/16): Point project list at ContactLogo and contactlogo.com _(by jaywedgeworth22)_
- **PS** [#19](https://github.com/jaywedgeworth22/Personal-Site/pull/19): Add Datadog logs, APM, and RUM on the existing account _(by jaywedgeworth22)_
- **PS** [#22](https://github.com/jaywedgeworth22/Personal-Site/pull/22): Visitor work blurbs and ContactLogo / Fleet icons _(by jaywedgeworth22)_
- **PS** [#26](https://github.com/jaywedgeworth22/Personal-Site/pull/26): feat(portfolio): add Autorotate and ContactLogo work cards _(by jaywedgeworth22)_
- **ST** [#3049](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3049): fix(proposals): keep Approve clickable after Retry Red Team _(by jaywedgeworth22)_
- **ST** [#3052](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3052): fix(db): harden SQLite migrations with tableExists and columnExists guards _(by jaywedgeworth22)_
- **ST** [#3054](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3054): feat(branding): add offset candlestick ST vector SVG and sync icon assets _(by jaywedgeworth22)_
- **ST** [#3055](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3055): Walk shared tickerLogoPolicy on /api/logos/ticker _(by jaywedgeworth22)_
- **ST** [#3074](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3074): build(deps-dev): bump vitest from 4.1.10 to 4.1.11 in the testing group _(by dependabot[bot])_
- **ST** [#3075](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3075): build(deps): bump jose from 6.2.8 to 6.2.9 _(by dependabot[bot])_
- **ST** [#3076](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3076): build(deps): bump lucide-react from 1.31.0 to 1.33.0 _(by dependabot[bot])_
- **ST** [#3078](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3078): build(deps-dev): bump js-yaml from 5.2.1 to 5.3.0 _(by dependabot[bot])_
- **ST** [#3079](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3079): build(deps): bump actions/upload-artifact from 4.6.2 to 7.0.1 _(by dependabot[bot])_
- **ST** [#3080](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3080): build(deps): bump nanoid from 3.3.12 to 3.3.18 _(by dependabot[bot])_
- **ST** [#3081](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3081): build(deps): bump fast-uri from 3.1.3 to 3.1.6 _(by dependabot[bot])_
- **ST** [#3082](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3082): build(deps): bump undici from 7.28.0 to 7.29.0 _(by dependabot[bot])_
- **ST** [#3083](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3083): ci(ios): switch iOS build and ship workflows to macos-latest cloud runners _(by jaywedgeworth22)_
- **ST** [#3084](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3084): build(deps): bump brace-expansion _(by dependabot[bot])_
- **ST** [#3086](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3086): build(deps): bump @auth/core and next-auth _(by dependabot[bot])_
- **ST** [#3087](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3087): docs: Alpaca Paper approve fix deploy handoff (#3049) _(by jaywedgeworth22)_
- **ST** [#3088](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3088): docs: Paper approve close-out — live verify + TestFlight blocked _(by jaywedgeworth22)_
- **ST** [#3089](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3089): ci(ios): TestFlight from hosted macos-latest via in-repo fleet _(by jaywedgeworth22)_
- **ST** [#3090](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3090): fix(rag): keep hydrated 1A when MD&A also reserves a slot _(by jaywedgeworth22)_
- **ST** [#3093](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3093): fix(console): Discard universe draft, approve typed-confirm, Coach chips _(by jaywedgeworth22)_
- **ST** [#3094](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3094): feat: Datadog logs, APM, and RUM on the existing us5 account _(by jaywedgeworth22)_
- **ST** [#3096](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3096): docs: TestFlight 1.0.69 installable via hosted macos-latest _(by jaywedgeworth22)_
- **ST** [#3097](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3097): test(e2e): assert Scan via More on mobile smoke _(by jaywedgeworth22)_
- **ST** [#3100](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3100): test(e2e): dismiss ConsentGate before mobile More in smoke _(by jaywedgeworth22)_
- **ST** [#3101](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3101): docs: close out ConsentGate smoke after Playwright Smoke green _(by jaywedgeworth22)_
- **ST** [#3102](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3102): fix(ios): move AppUpdatePrompt Apple IDs off Swift _(by jaywedgeworth22)_
- **UM** [#1321](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1321): feat(receipts): Grok/DeepSeek classify fallback _(by jaywedgeworth22)_
- **UM** [#1323](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1323): fix(ios): budget editing affordances and Mac health auth _(by jaywedgeworth22)_
- **UM** [#1330](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1330): chore(deps): bump congress-trading-shared to v2.6.0 _(by jaywedgeworth22)_
- **UM** [#1331](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1331): ci(ios): switch iOS build and ship workflows to macos-latest cloud runners _(by jaywedgeworth22)_
- **UM** [#1332](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1332): feat(agents): add dedicated Agents tab with live quota matrix & runtime indicators _(by jaywedgeworth22)_
- **UM** [#1333](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1333): chore(deps): bump the npm-minor-and-patch group with 7 updates _(by dependabot[bot])_
- **UM** [#1335](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1335): feat(alerts): enrich Pushover alerts for usage spikes with details and sounds _(by jaywedgeworth22)_
- **UM** [#1336](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1336): fix(ios-local): connect restored accounts instead of a dead toggle _(by jaywedgeworth22)_
- **UM** [#1337](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1337): fix(r2): keep idle orphan buckets in GraphQL storage lookback _(by jaywedgeworth22)_
- **UM** [#1338](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1338): fix(r2): group month storage by bucket so idle orphans stay visible _(by jaywedgeworth22)_
- **UM** [#1339](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1339): fix(collectors): post fleet seats under their own producerIds _(by jaywedgeworth22)_
- **UM** [#1341](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1341): feat(observability): add Datadog APM, logs, and gated RUM _(by jaywedgeworth22)_
- **UM** [#1342](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1342): fix(observability): do not fail boot on RUM labels or a partial public pair _(by jaywedgeworth22)_
- **UM** [#1343](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1343): fix(ios): import existing ASC secrets on hosted ios-ship _(by jaywedgeworth22)_
- **UM** [#1345](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1345): docs: mark Datadog #1341 complete on the effort board _(by jaywedgeworth22)_
- **UM** [#1347](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1347): fix(ios): pin AppUpdatePrompt.swift for both targets _(by jaywedgeworth22)_
- **UM** [#1348](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1348): docs: mark AppUpdatePrompt pin #1347 complete on the effort board _(by jaywedgeworth22)_
- **UM** [#1349](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1349): feat(ios): Usage Monitor widget topics — Budget, LLM Quotas, Servers _(by jaywedgeworth22)_
- **AFC** `Cursor` [#75](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/75): Bridge Shellular — chats to Cloud Agents _(by jaywedgeworth22)_
- **AFC** [#83](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/83): fix(board): stop inbound sync from unclaiming GitHub issues _(by jaywedgeworth22)_
- **AFC** [#97](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/97): fix(mac): do not force-reap worktrees or wipe simulators _(by jaywedgeworth22)_
- **AFC** [#99](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/99): feat(backup): mirror fleet agent skills to Google Drive _(by jaywedgeworth22)_
- **AFC** [#103](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/103): feat(host): fleet-housekeep timer for disk, zombies, and failed units _(by jaywedgeworth22)_
- **AFC** [#110](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/110): fix(shellular): DeepSeek iOS thinking hang — auto-approve Harness tools _(by jaywedgeworth22)_
- **AFC** [#112](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/112): fix(host): stop housekeep false-warn on zero zombies _(by jaywedgeworth22)_
- **AFC** [#113](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/113): Per-seat fleet skills; drop local Mac iOS ship _(by jaywedgeworth22)_
- **AFC** [#114](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/114): fix(host): ignore cloud-init-hotplugd in housekeep _(by jaywedgeworth22)_
- **AFC** `Grok` [#115](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/115): self-id; FLEET is a — Bot wake only _(by jaywedgeworth22)_
- **AFC** [#116](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/116): feat(legend): add Autorotate, ContactLogo, jays.services and new agent logos _(by jaywedgeworth22)_
- **AFC** [#117](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/117): Harden pm2 agy-acp: turbo child, 300s grace, persist loopback _(by jaywedgeworth22)_
- **AFC** [#118](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/118): docs: add fleet DNS and registrar playbook _(by jaywedgeworth22)_
- **CTS** [#282](https://github.com/jaywedgeworth22/congress-trading-shared/pull/282): chore(deps): bump anthropics/claude-code-action from 1.0.193 to 1.0.199 _(by dependabot[bot])_
- **CTS** [#283](https://github.com/jaywedgeworth22/congress-trading-shared/pull/283): chore(deps-dev): bump vitest from 4.1.10 to 4.1.11 _(by dependabot[bot])_
- **CTS** [#284](https://github.com/jaywedgeworth22/congress-trading-shared/pull/284): chore(deps-dev): bump @vitest/coverage-v8 from 4.1.10 to 4.1.11 _(by dependabot[bot])_
- **CTS** [#285](https://github.com/jaywedgeworth22/congress-trading-shared/pull/285): chore(deps-dev): bump publint from 0.3.23 to 0.3.24 _(by dependabot[bot])_
- **OPS** [#1](https://github.com/jaywedgeworth22/fleet-ops/pull/1): feat(fleet): GitHub fleet audit tools and Datadog observability suite _(by jaywedgeworth22)_
- **OPS** [#2](https://github.com/jaywedgeworth22/fleet-ops/pull/2): docs(ops): land fleet-ops self-id as OPS, not FLEET _(by jaywedgeworth22)_

### Issues closed

- **AR** [#64](https://github.com/jaywedgeworth22/Autorotate/issues/64): Site & App Triage, Security Fixes, Cross-Platform Master 3D Icons, and
- **AR** [#65](https://github.com/jaywedgeworth22/Autorotate/issues/65): 2026-08-22 — COMPLETED - Autorotate Apple IDs codes.autorotate after
- **AR** [#66](https://github.com/jaywedgeworth22/Autorotate/issues/66): Apple IDs in git (codes.autorotate) — PR
- **DD** [#187](https://github.com/jaywedgeworth22/DealDex/issues/187): 2026-08-22 — PICKUP — Analytics already live; remaining
- **PS** [#18](https://github.com/jaywedgeworth22/Personal-Site/issues/18): 2026-08-22 — IN PROGRESS — Vercel Web Analytics
- **PS** [#20](https://github.com/jaywedgeworth22/Personal-Site/issues/20): 2026-08-25 — COMPLETED — Datadog logs + APM + RUM. PR #19. Existing
- **PS** [#21](https://github.com/jaywedgeworth22/Personal-Site/issues/21): 2026-08-22 — COMPLETED — Vercel Web Analytics. @vercel/analytics/react
- **PS** [#24](https://github.com/jaywedgeworth22/Personal-Site/issues/24): 2026-08-25 — COMPLETED — Designer leftover UX (visitor blurbs +
- **PS** [#27](https://github.com/jaywedgeworth22/Personal-Site/issues/27): 2026-08-22 — DEPLOYED - Enable Vercel Web Analytics on Personal-Site
- **PS** [#28](https://github.com/jaywedgeworth22/Personal-Site/issues/28): 2026-08-22 — DEPLOYED — Vercel Web Analytics (PR #17)
- **PS** [#29](https://github.com/jaywedgeworth22/Personal-Site/issues/29): 2026-08-22 — PICKUP — github-sync chat already DEPLOYED (Hobby
- **PS** [#30](https://github.com/jaywedgeworth22/Personal-Site/issues/30): 2026-08-22 — DEPLOYED - Personal-Site on personal Hobby Vercel +
- **PS** [#31](https://github.com/jaywedgeworth22/Personal-Site/issues/31): 2026-08-22 — DEPLOYED — Personal Hobby Vercel + backup handoff
- **PS** [#32](https://github.com/jaywedgeworth22/Personal-Site/issues/32): 2026-08-25 — COMPLETED — Add Autorotate and ContactLogo portfolio work
- **ST** [#2964](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2964): Migrations 2 and 14 use PRAGMA table_info as an existence check, which returns empty (not an error) for a missing table
- **UM** [#1329](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1329): [Uptime] Usage Monitor Hetzner origin readiness failure
- **UM** [#1344](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1344): 2026-08-25 — IN PR #1341 — Datadog logs + APM + RUM on

### Issues opened

- **AR** [#64](https://github.com/jaywedgeworth22/Autorotate/issues/64): Site & App Triage, Security Fixes, Cross-Platform Master 3D Icons, and
- **AR** [#65](https://github.com/jaywedgeworth22/Autorotate/issues/65): 2026-08-22 — COMPLETED - Autorotate Apple IDs codes.autorotate after
- **AR** [#66](https://github.com/jaywedgeworth22/Autorotate/issues/66): Apple IDs in git (codes.autorotate) — PR
- **AR** [#67](https://github.com/jaywedgeworth22/Autorotate/issues/67): Owner: Developer portal App IDs for Autorotate — leftover after — #50 closed
- **DD** [#168](https://github.com/jaywedgeworth22/DealDex/issues/168): 2026-08-24 — IN PROGRESS — Switch iOS CI & Actions workflows to
- **DD** [#169](https://github.com/jaywedgeworth22/DealDex/issues/169): 2026-08-22 — IN PROGRESS — OG logo-only social card. Centered DealDex
- **DD** [#171](https://github.com/jaywedgeworth22/DealDex/issues/171): 2026-08-24 — IN PROGRESS — Vendor ios-fleet + restore Mac runner so
- **DD** [#174](https://github.com/jaywedgeworth22/DealDex/issues/174): 2026-08-24 — IN PROGRESS — Put ios-ship back on GitHub-hosted
- **DD** [#177](https://github.com/jaywedgeworth22/DealDex/issues/177): 2026-08-25 — IN PROGRESS — Accept dealdex in vendored
- **DD** [#179](https://github.com/jaywedgeworth22/DealDex/issues/179): 2026-08-25 — IN PROGRESS — Android Play + PWA skippable update alerts
- **DD** [#181](https://github.com/jaywedgeworth22/DealDex/issues/181): 2026-08-25 — IN PROGRESS — Center iOS Scan empty-loading spinner +
- **DD** [#185](https://github.com/jaywedgeworth22/DealDex/issues/185): 2026-08-25 — IN PROGRESS — testers.json Comcast typo (johnwedeworth →
- **DD** [#187](https://github.com/jaywedgeworth22/DealDex/issues/187): 2026-08-22 — PICKUP — Analytics already live; remaining
- **DD** [#189](https://github.com/jaywedgeworth22/DealDex/issues/189): 2026-08-25 — IN PROGRESS — Pin AppUpdatePrompt.swift from in-repo
- **PS** [#20](https://github.com/jaywedgeworth22/Personal-Site/issues/20): 2026-08-25 — COMPLETED — Datadog logs + APM + RUM. PR #19. Existing
- **PS** [#21](https://github.com/jaywedgeworth22/Personal-Site/issues/21): 2026-08-22 — COMPLETED — Vercel Web Analytics. @vercel/analytics/react
- **PS** [#24](https://github.com/jaywedgeworth22/Personal-Site/issues/24): 2026-08-25 — COMPLETED — Designer leftover UX (visitor blurbs +
- **PS** [#27](https://github.com/jaywedgeworth22/Personal-Site/issues/27): 2026-08-22 — DEPLOYED - Enable Vercel Web Analytics on Personal-Site
- **PS** [#28](https://github.com/jaywedgeworth22/Personal-Site/issues/28): 2026-08-22 — DEPLOYED — Vercel Web Analytics (PR #17)
- **PS** [#29](https://github.com/jaywedgeworth22/Personal-Site/issues/29): 2026-08-22 — PICKUP — github-sync chat already DEPLOYED (Hobby
- **PS** [#30](https://github.com/jaywedgeworth22/Personal-Site/issues/30): 2026-08-22 — DEPLOYED - Personal-Site on personal Hobby Vercel +
- **PS** [#31](https://github.com/jaywedgeworth22/Personal-Site/issues/31): 2026-08-22 — DEPLOYED — Personal Hobby Vercel + backup handoff
- **PS** [#32](https://github.com/jaywedgeworth22/Personal-Site/issues/32): 2026-08-25 — COMPLETED — Add Autorotate and ContactLogo portfolio work
- **ST** [#3098](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3098): 2026-08-25 — PLANNED — Console honesty: Guardrails Discard, approve
- **ST** [#3099](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3099): 2026-08-25 — IN PROGRESS — Console honesty: Guardrails Discard
- **UM** [#1329](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1329): [Uptime] Usage Monitor Hetzner origin readiness failure
- **UM** [#1344](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1344): 2026-08-25 — IN PR #1341 — Datadog logs + APM + RUM on
- **UM** [#1346](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1346): [Uptime] Usage Monitor production is stale vs main
- **CTS** [#286](https://github.com/jaywedgeworth22/congress-trading-shared/issues/286): tickerLogoPolicy A/B/C/D seed (v2.6.0)

### Effort board

- **CT** `Cursor` 2026-08-24 — PR OPEN #2208 — Public Admin Sign-In copy: no ADMIN_TOKEN / bearer / localStorage / Authorization jargon (branch `cursor/admin-signin-copy-7460`). Visitors and Premium users saw env-var names in the Admin Sign-In dialog and Admin Access help. Copy-only in `dashboardHtml.ts`; token save/clear/auth unchanged. Gates: typecheck clean; 293 files / 3726 tests. Live congress
- **CT** `Antigravity` 2026-08-24 — COMPLETED/DEPLOYED (`f41fc75d`) — X (Twitter) OAuth 2.0 PKCE auth integration + DOCKER-USER network timeout resolution & Infisical circular telemetry fix. Added X PKCE login, email linking, and privacy/terms URLs. Fixed Hetzner host DOCKER-USER iptables DROP trap (missing interface scoping), resolved Docker MTU mismatch, fixed Infisical circular telemetry deadlock (P
- **CT** `Antigravity` 2026-08-24 — IN PROGRESS — Switch iOS CI & Actions workflows to GitHub-hosted cloud macOS runners (branch `antigravity/cloud-ios-actions-runners`). Update ios-build.yml and related workflows to use standard GitHub-hosted runners (free for public repos), drop self-hosted Mac runner dependency, remove obsolete backup files, and update runner docs
- **CT** `Antigravity` 2026-08-24 — COMPLETED / PR OPEN — Latency Snapshots Pre-Publish and Sweeping Backfill. Prioritize `provider_first_seen_at` for latency offsets. Add `-30m`, `-15m`, and `+12h` snapshots to `latencyPriceSnapshots.ts`. Verified locally (tsc/vitest). PR #2203
- **UM** `Antigravity` 2026-08-24 — IN PROGRESS — Switch iOS CI & Actions workflows to GitHub-hosted cloud macOS runners (branch `antigravity/cloud-ios-actions-runners`). Update ios-build.yml and ios-ship.yml to runs-on macos-latest (free unlimited minutes on public repo), and update Xcode assertion
- **DD** `Antigravity` 2026-08-24 — COMPLETED/MERGED #167 (`b6cad4d`) — Switch iOS CI & Actions workflows to GitHub-hosted cloud macOS runners (branch `antigravity/cloud-ios-actions-runners`). Updated ios-ship.yml to runs-on macos-latest (free unlimited minutes on public repo), and updated Xcode version assertion. Full cloud CI suite green. Live SHA `b6cad4d`

## 2026-08-23

*31 PRs merged · 26 issues opened · 4 issues closed · 8 effort rows*

### Merged PRs

- **AR** [#61](https://github.com/jaywedgeworth22/Autorotate/pull/61): docs(agents): update Autorotate branding, acronym AR, and integration path _(by jaywedgeworth22)_
- **CT** [#2190](https://github.com/jaywedgeworth22/Congress.Trade/pull/2190): chore(ios-fleet): update Autorotate branding and bundle ID codes.autorotate _(by jaywedgeworth22)_
- **CT** [#2191](https://github.com/jaywedgeworth22/Congress.Trade/pull/2191): docs: record bot protection and origin lock _(by jaywedgeworth22)_
- **DD** [#156](https://github.com/jaywedgeworth22/DealDex/pull/156): Enlarge OG share card for DealDex.net _(by jaywedgeworth22)_
- **DD** [#158](https://github.com/jaywedgeworth22/DealDex/pull/158): Center OG share card and DealDex.net host _(by jaywedgeworth22)_
- **DD** [#160](https://github.com/jaywedgeworth22/DealDex/pull/160): Rewrite OG subtitle and re-render share card _(by jaywedgeworth22)_
- **DD** [#161](https://github.com/jaywedgeworth22/DealDex/pull/161): Remove DealDex.net from site headings _(by jaywedgeworth22)_
- **DD** [#162](https://github.com/jaywedgeworth22/DealDex/pull/162): Hamburger menu for site chrome; drop App Mark picker _(by jaywedgeworth22)_
- **DD** [#163](https://github.com/jaywedgeworth22/DealDex/pull/163): Native Google, Apple, and X sign-in; appearance in Settings _(by jaywedgeworth22)_
- **DD** [#165](https://github.com/jaywedgeworth22/DealDex/pull/165): Align DealDex iOS versions with fleet 1.0.N regimen _(by jaywedgeworth22)_
- **ST** [#3068](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3068): docs: 2026-08-23 full-stack ST review filing (#3056–#3067) _(by jaywedgeworth22)_
- **ST** [#3069](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3069): fix(r2): proactively sweep stale .r2snap temp files and clean journals in finally block _(by jaywedgeworth22)_
- **ST** [#3070](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3070): feat(auth): add X (Twitter) OAuth 2.0 login provider _(by jaywedgeworth22)_
- **ST** [#3071](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3071): fix(ui, risk): toggle touch styling, account extended hours hints & active short management _(by jaywedgeworth22)_
- **ST** [#3072](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3072): docs(effort-log): mark active short management as completed and deployed _(by jaywedgeworth22)_
- **UM** [#1322](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1322): fix(r2): account-wide GraphQL storage for UM alerts and fleet digest _(by jaywedgeworth22)_
- **UM** [#1324](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1324): Fix iOS bottom scroll clearance across all tabs and More sheet _(by jaywedgeworth22)_
- **UM** [#1325](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1325): docs(effort-log): mark iOS bottom scroll clearance completed in #1324 _(by jaywedgeworth22)_
- **UM** [#1326](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1326): feat(collectors): unified fleet quota & shadow API cost collectors _(by jaywedgeworth22)_
- **UM** [#1327](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1327): Fix GET /api/health/mac dual-auth to support dashboard session cookies _(by jaywedgeworth22)_
- **UM** [#1328](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1328): docs(effort-log): mark health/mac session auth fix completed in #1327 _(by jaywedgeworth22)_
- **AFC** [#101](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/101): Specialize fleet skills per agent seat _(by jaywedgeworth22)_
- **AFC** [#102](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/102): Fix fx skill YAML quotes and install FX fleet pack _(by jaywedgeworth22)_
- **AFC** [#104](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/104): docs(infra): update Hetzner Tailscale MagicDNS to server.boa-roygbiv.ts.net _(by jaywedgeworth22)_
- **AFC** [#105](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/105): docs(infra): record server.boa-roygbiv.ts.net in fleet-infra skill _(by jaywedgeworth22)_
- **AFC** [#106](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/106): fix(skills): specialize seat identity per platform and render universal root skills _(by jaywedgeworth22)_
- **AFC** [#107](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/107): docs(mac): document agy-acp-turbo wrapper for Shellular _(by jaywedgeworth22)_
- **AFC** [#108](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/108): fix(shellular): set unknown-clients policy to always-allow _(by jaywedgeworth22)_
- **AFC** [#109](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/109): docs(fleet): document canonical app acronyms matrix and update Autorotate (AR) _(by jaywedgeworth22)_
- **AFC** [#111](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/111): docs(effort): update canonical Autorotate board path to AUTOROTATE-EFFORT-LOG.md _(by jaywedgeworth22)_
- **CTS** [#281](https://github.com/jaywedgeworth22/congress-trading-shared/pull/281): Add tickerLogoPolicy A/B/C/D source order (v2.6.0) _(by jaywedgeworth22)_

### Issues closed

- **AR** [#23](https://github.com/jaywedgeworth22/Autorotate/issues/23): Dependabot triage after #16 — · actions + radix PRs #1–15 still open;
- **AR** [#37](https://github.com/jaywedgeworth22/Autorotate/issues/37): iOS first-launch update prompt (fleet) — · branch
- **AR** [#39](https://github.com/jaywedgeworth22/Autorotate/issues/39): Merge — App Builder PWA with this monorepo — · branch
- **AR** [#46](https://github.com/jaywedgeworth22/Autorotate/issues/46): Dependabot leftover radix/react PRs — · after #16. Remaining npm PRs

### Issues opened

- **AR** [#59](https://github.com/jaywedgeworth22/Autorotate/issues/59): Full internal rename TopSpin → Autorotate
- **CT** [#2180](https://github.com/jaywedgeworth22/Congress.Trade/issues/2180): P0: GET /api/transactions?order=desc is ingest — not trade date (2024 Khanna is page 1)
- **CT** [#2181](https://github.com/jaywedgeworth22/Congress.Trade/issues/2181): P0: Latency probes still silent — Quiver 278h, Unusual Whales 241h (health degraded)
- **CT** [#2182](https://github.com/jaywedgeworth22/Congress.Trade/issues/2182): P1: 80 ingestion outbox items stuck in dead letter
- **CT** [#2183](https://github.com/jaywedgeworth22/Congress.Trade/issues/2183): P1: Sentry CONGRESS-TRADE-1B Deno cron tick still exceeds 45s (246 events / 2d)
- **CT** [#2184](https://github.com/jaywedgeworth22/Congress.Trade/issues/2184): P1: Only 34% of trades resolve to a ticker (analytics.summary resolvedTickerPct)
- **CT** [#2185](https://github.com/jaywedgeworth22/Congress.Trade/issues/2185): P2: Sign-in password field is not inside a form (browser warning)
- **CT** [#2186](https://github.com/jaywedgeworth22/Congress.Trade/issues/2186): P2: Primary tabs expose duplicate accessible names (Trends Trends)
- **CT** [#2187](https://github.com/jaywedgeworth22/Congress.Trade/issues/2187): P2: GET /api/stream returns 400 (SSE live path)
- **DD** [#157](https://github.com/jaywedgeworth22/DealDex/issues/157): 2026-08-23 — IN PROGRESS — Enlarge OG share card; drop TCGPlayer;
- **DD** [#159](https://github.com/jaywedgeworth22/DealDex/issues/159): 2026-08-23 — IN PROGRESS — Center OG heading/subtitle; DealDex.net +
- **DD** [#164](https://github.com/jaywedgeworth22/DealDex/issues/164): 2026-08-23 — IN PROGRESS — Settings appearance 3-way + native
- **DD** [#166](https://github.com/jaywedgeworth22/DealDex/issues/166): 2026-08-23 — IN PROGRESS — iOS version regimen (1.0.N + UTC build, not
- **ST** [#3056](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3056): [P0] Alpaca write path sends stop_market; Alpaca requires stop
- **ST** [#3057](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3057): [P0] SEC ingest misclassifies embed 400s as budget exceeded and requeues them
- **ST** [#3058](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3058): [P0] MCP place timeout always REST-falls-back and can double-submit
- **ST** [#3059](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3059): [P1] Dashboard recent fills take the oldest 500
- **ST** [#3060](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3060): [P1] Incremental SEC refresh counts skipped+error as success
- **ST** [#3061](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3061): [P1] iOS Dictionary(uniqueKeysWithValues:) traps on duplicate command ids
- **ST** [#3062](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3062): [P1] Web 401 never routes to login; desk freezes on last-good data
- **ST** [#3063](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3063): [P1] Prod tradingLiveness degraded; oldest completed run ~3d
- **ST** [#3064](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3064): [P1] Any client_order_id counts as app-placed (owner GTC cancel-replace risk)
- **ST** [#3065](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3065): [P1] Query embed failure returns null; retrieval looks like empty corpus
- **ST** [#3066](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3066): [P2] iOS TestFlight ship CI, Playwright smoke, deploy freshness failing on main
- **ST** [#3067](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3067): [P2] Session close prints stamped Delayed Quote
- **ST** [#3073](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3073): Options portfolio allocation and ranking architecture

### Effort board

- **CT** `Cursor` 2026-08-23 — IN PROGRESS — Consume shared tickerLogoPolicy (CTS v2.6.0 vendor). KV jury stays here. Branch `cursor/ticker-logo-policy`. Rollout: `docs/rollouts/2026-08-23-ticker-logo-policy.md`. Keepouts: extract/halt, Infisical, #1959
- **UM** `Antigravity` 2026-08-23 — COMPLETED/MERGED #1327 `c22863f2` — Fix GET /api/health/mac session auth for Computers tab (branch `fix/health-mac-session-auth`). Added dashboard session cookie check to GET /api/health/mac so signed-in Full Access dashboard sessions can load Mac health stats without requiring a separate USAGE_READ_TOKEN. Unit tests added
- **UM** `Antigravity` 2026-08-23 — COMPLETED/MERGED #1324 `6df4fbf3` — iOS bottom scroll clearance across all tabs & More sheet (branch `ag/ios-bottom-scroll-clearance`). Fixed `safeAreaInset` on `RootView` capsule bar, propagated `tabBarScrollClearance` (96pt safeAreaPadding + scrollContent contentMargins) across child `ScrollView`/`List`/`Form` views, added bottom margin to `MoreSheet`, and ensured
- **DD** `Cursor` `Grok` 2026-08-23 — COMPLETED/MERGED #163 — Settings appearance 3-way + Google/Apple/X auth. Squash on main. — broker and email/password removed. Needs Vercel `GOOGLE_CLIENT_ID`/`GOOGLE_CLIENT_SECRET` (and Apple/X if used) plus OAuth callback URLs
- **DD** `Cursor` 2026-08-23 — COMPLETED - OG share: drop TCGPlayer, DealDex.net, enlarge title. PR #156: enlarged OG card, eBay·Mercari, dealdex.net, cache-bust share-20260823. <! — wb-agent-report:9844c760d93b4f229185fabd07eb5867 — >
- **AFC** `Cursor` 2026-08-23 — IN PROGRESS — Shellular iOS DeepSeek thinking hang (`cursor/shellular-deepseek-thinking-fix-e0b0`). Harness `approval: ask` blocked phone clients; `dsh-acp` now auto-approves via `DSH_PERMISSION_MODE=danger-full-access`
- **AFC** `Cursor` 2026-08-23 — IN PROGRESS — fx skill discovery (`cursor/fx-skills-yaml`). Fold quoted SKILL.md descriptions (`malformed_quote`), install FX seat to `~/.fx/skills`, raise fx `skill_catalog_bytes`. Worktree `~/apps/fleet — fx-skills`
- **AFC** `Claude` `Cursor` `Antigravity` `Codex` `Grok` 2026-08-23 — IN PROGRESS — Per-seat fleet skill identity (`cursor/fleet-skill-seat-identity`). Specialize platform skill installs so do not inherit ` `

## 2026-08-22

*59 PRs merged · 27 issues opened · 17 issues closed · 40 effort rows*

### Merged PRs

- **AR** [#47](https://github.com/jaywedgeworth22/Autorotate/pull/47): fix(web): do not overwrite live secrets when sending a canary _(by jaywedgeworth22)_
- **AR** [#48](https://github.com/jaywedgeworth22/Autorotate/pull/48): feat: Autorotate rebrand (Autorotate.codes), Android companion app, Apple specs & power enhancements _(by jaywedgeworth22)_
- **AR** [#51](https://github.com/jaywedgeworth22/Autorotate/pull/51): fix(security): sanitize Drive backup references and add private infra hub instructions _(by jaywedgeworth22)_
- **AR** [#57](https://github.com/jaywedgeworth22/Autorotate/pull/57): feat(branding): add master 3D silver key app icon & squircle policy _(by jaywedgeworth22)_
- **CT** [#2171](https://github.com/jaywedgeworth22/Congress.Trade/pull/2171): fix(security): sanitize origin IPs, Coolify UUIDs, and Infisical IDs; remove root scratch scripts _(by jaywedgeworth22)_
- **CT** [#2172](https://github.com/jaywedgeworth22/Congress.Trade/pull/2172): feat(fullstack): web polish, backend tuning, ST market data integration, and iOS full parity _(by jaywedgeworth22)_
- **CT** [#2175](https://github.com/jaywedgeworth22/Congress.Trade/pull/2175): docs(ios): Tahoe GM App Store 1.0.81 resubmit _(by jaywedgeworth22)_
- **CT** [#2176](https://github.com/jaywedgeworth22/Congress.Trade/pull/2176): fix(ios): pin disclaimer under title and auto-hide on cold start _(by jaywedgeworth22)_
- **CT** [#2177](https://github.com/jaywedgeworth22/Congress.Trade/pull/2177): fix(security): sanitize historical host IP in EFFORT-LOG.md _(by jaywedgeworth22)_
- **CT** [#2178](https://github.com/jaywedgeworth22/Congress.Trade/pull/2178): fix(ui,ops): remove sub-month timeframes, render ticker analytics, and isolate systemd units _(by jaywedgeworth22)_
- **CL** [#10](https://github.com/jaywedgeworth22/ContactLogo/pull/10): Configure Xcode project (iOS & macOS), build native Android app, and align ContactLogo.com _(by jaywedgeworth22)_
- **DD** [#128](https://github.com/jaywedgeworth22/DealDex/pull/128): Add Vercel Web Analytics to DealDex _(by jaywedgeworth22)_
- **DD** [#130](https://github.com/jaywedgeworth22/DealDex/pull/130): Use owner DD PNG as AppIcon and isolated DD as favicon _(by jaywedgeworth22)_
- **DD** [#132](https://github.com/jaywedgeworth22/DealDex/pull/132): Scan over eBay/Mercari; Android/PWA isolated DD _(by jaywedgeworth22)_
- **DD** [#134](https://github.com/jaywedgeworth22/DealDex/pull/134): Scan box: centered filters, SCAN 2.5x, Hide Proxies _(by jaywedgeworth22)_
- **DD** [#136](https://github.com/jaywedgeworth22/DealDex/pull/136): Point DealDex at dealdex.net _(by jaywedgeworth22)_
- **DD** [#139](https://github.com/jaywedgeworth22/DealDex/pull/139): Switch iOS bundle to net.dealdex, set iOS 17.0 target, sync official brand icons, and update domain _(by jaywedgeworth22)_
- **DD** [#145](https://github.com/jaywedgeworth22/DealDex/pull/145): Mount Vercel Speed Insights on the TanStack root _(by jaywedgeworth22)_
- **DD** [#147](https://github.com/jaywedgeworth22/DealDex/pull/147): Add App Store Connect profile icon asset and verify builds under net.dealdex _(by jaywedgeworth22)_
- **DD** [#154](https://github.com/jaywedgeworth22/DealDex/pull/154): Publish native apps with website scan scoring _(by jaywedgeworth22)_
- **PS** [#11](https://github.com/jaywedgeworth22/Personal-Site/pull/11): ci(backup): update repo backup workflow for full fleet _(by jaywedgeworth22)_
- **PS** [#12](https://github.com/jaywedgeworth22/Personal-Site/pull/12): Personal Hobby Vercel + retire broken GitHub backup Action _(by jaywedgeworth22)_
- **PS** [#14](https://github.com/jaywedgeworth22/Personal-Site/pull/14): Close out personal Vercel backup handoff board row _(by jaywedgeworth22)_
- **PS** [#17](https://github.com/jaywedgeworth22/Personal-Site/pull/17): feat(ps): Vercel Web Analytics for TanStack Start _(by jaywedgeworth22)_
- **ST** [#3041](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3041): Cascade last-resort + RAG Green/Red hydrate _(by jaywedgeworth22)_
- **ST** [#3042](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3042): fix(security): sanitize origin IPs, Coolify UUIDs, and host environment paths _(by jaywedgeworth22)_
- **ST** [#3043](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3043): Fix test DB isolation and SVG sparkline gradient IDs _(by jaywedgeworth22)_
- **ST** [#3045](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3045): fix(security): sanitize retired host IPs, app UUIDs, and deploy scripts _(by jaywedgeworth22)_
- **ST** [#3046](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3046): Full system fixes & native iOS website parity upgrades _(by jaywedgeworth22)_
- **ST** [#3048](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3048): fix(market): CT peer intraday uses stored operator Robinhood token _(by jaywedgeworth22)_
- **ST** [#3051](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3051): Ship owner candlestick ST favicon, ASC listing, and Android master _(by jaywedgeworth22)_
- **ST** [#3053](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3053): fix(console): blur-commit operations knobs and prevent empty fallback writes _(by jaywedgeworth22)_
- **UM** [#1310](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1310): feat(receipts): show inbox mail, file expenses, Apple Calendar ICS _(by jaywedgeworth22)_
- **UM** [#1311](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1311): fix(receipts): do not auto-file inbox mail as actual cash _(by jaywedgeworth22)_
- **UM** [#1312](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1312): Fleet projects, Manually only labels, local workspace copy _(by jaywedgeworth22)_
- **UM** [#1313](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1313): fix(workspace): merge import must not overwrite live plans _(by jaywedgeworth22)_
- **UM** [#1314](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1314): fix(security): sanitize origin IPs, Coolify UUIDs, and Infisical IDs _(by jaywedgeworth22)_
- **UM** [#1315](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1315): fix(security): sanitize hardcoded Infisical project IDs, mock test fixtures, and scripts _(by jaywedgeworth22)_
- **UM** `Codex` `Grok` [#1316](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1316): API-equivalent cost for — and — Build seats _(by jaywedgeworth22)_
- **UM** `Codex` [#1317](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1317): Skip — token_count replays that do not advance totals _(by jaywedgeworth22)_
- **UM** [#1318](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1318): Add Copilot CLI API-equivalent cost and restore Infisical project bake _(by jaywedgeworth22)_
- **UM** [#1319](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1319): fix(collectors): subtract Copilot cache writes from inclusive input _(by jaywedgeworth22)_
- **UM** `Codex` [#1320](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1320): fix(collectors): keep — sessionKey stable across archive _(by jaywedgeworth22)_
- **AFC** [#80](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/80): KIMI unclaim leftover work; claims must show the claim date _(by jaywedgeworth22)_
- **AFC** [#81](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/81): Redirect board.jays.services to THE BOARD _(by jaywedgeworth22)_
- **AFC** [#82](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/82): fix(board): stop writeback loop; make two-way sync idempotent _(by jaywedgeworth22)_
- **AFC** [#84](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/84): feat(skills): add master fleet-coordination skill and universal multi-platform catalog _(by jaywedgeworth22)_
- **AFC** [#85](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/85): fix(security): sanitize origin IPs, Coolify UUIDs, and Infisical IDs in docs and skills _(by jaywedgeworth22)_
- **AFC** [#86](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/86): Update AGENT-SYNC Apple Notes standards with line-height and aesthetics protocols _(by jaywedgeworth22)_
- **AFC** [#88](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/88): docs(notes): clarify Coding folder is intentionally local and non-iCloud _(by jaywedgeworth22)_
- **AFC** [#89](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/89): feat(backup): add automated fleet Google Drive backup script _(by jaywedgeworth22)_
- **AFC** [#90](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/90): Janitor covers all apps; Kimi and nested worktree reap _(by jaywedgeworth22)_
- **AFC** [#91](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/91): feat(protocol): add living handoff report and substitute agent closeout protocol _(by jaywedgeworth22)_
- **AFC** [#92](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/92): feat(skills): add fleet-infra skill and update TEMPLATE-AGENTS loud notices _(by jaywedgeworth22)_
- **AFC** [#93](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/93): fix(mac): janitor must idle-check; do not substring-match kimi _(by jaywedgeworth22)_
- **AFC** [#94](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/94): Coordinator owns Drive + GitHub source backups _(by jaywedgeworth22)_
- **AFC** [#95](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/95): feat(skills): add mac-cleanup skill, script, and launchd plist _(by jaywedgeworth22)_
- **AFC** [#98](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/98): Require Central Time whenever telling the owner a time _(by jaywedgeworth22)_
- **AFC** [#100](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/100): docs(policy): full-bleed square app icon standard (no pre-baked squircles) _(by jaywedgeworth22)_

### Issues closed

- **AR** [#52](https://github.com/jaywedgeworth22/Autorotate/issues/52): Rebrand (Autorotate.codes), Native Android Companion App & Apple
- **AR** [#53](https://github.com/jaywedgeworth22/Autorotate/issues/53): Web and iOS utility and power enhancements — · PR
- **AR** [#54](https://github.com/jaywedgeworth22/Autorotate/issues/54): Merge — App Builder PWA with this monorepo — · merged as
- **DD** [#140](https://github.com/jaywedgeworth22/DealDex/issues/140): 2026-08-22 — DEPLOYED — Vercel Web Analytics (#128 squash 148780af)
- **DD** [#141](https://github.com/jaywedgeworth22/DealDex/issues/141): 2026-08-22 — COMPLETED - Point DealDex production at dealdex.net. Landed
- **DD** [#142](https://github.com/jaywedgeworth22/DealDex/issues/142): 2026-08-22 — COMPLETED - Android + PWA use isolated DD. Merged #132
- **DD** [#143](https://github.com/jaywedgeworth22/DealDex/issues/143): 2026-08-22 — COMPLETED - Tighter DD AppIcon on ST grid. Merged #130
- **DD** [#144](https://github.com/jaywedgeworth22/DealDex/issues/144): 2026-08-22 — COMPLETED — DealDex.net domain, net.dealdex bundle
- **DD** [#148](https://github.com/jaywedgeworth22/DealDex/issues/148): 2026-08-22 — PICKUP — Analytics already live; remaining
- **DD** [#149](https://github.com/jaywedgeworth22/DealDex/issues/149): 2026-08-22 — DEPLOYED — Vercel Web Analytics (#128 squash 148780af)
- **DD** [#150](https://github.com/jaywedgeworth22/DealDex/issues/150): 2026-08-21 — DEPLOYED — #118 / #117 scan layout + subtitle
- **DD** [#151](https://github.com/jaywedgeworth22/DealDex/issues/151): 2026-08-22 — COMPLETED - Point DealDex production at dealdex.net. Landed
- **DD** [#152](https://github.com/jaywedgeworth22/DealDex/issues/152): 2026-08-22 — COMPLETED — Build app under net.dealdex bundle
- **PS** [#13](https://github.com/jaywedgeworth22/Personal-Site/issues/13): 2026-08-22 — IN PROGRESS — Personal Hobby Vercel + fleet Drive backup
- **PS** [#15](https://github.com/jaywedgeworth22/Personal-Site/issues/15): 2026-08-22 — DEPLOYED — Personal Hobby Vercel + backup handoff. GitHub
- **ST** [#2958](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2958): Admin > Operations knobs PATCH on every keystroke and write each knob's default on an emptied field
- **ST** [#3047](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3047): Hetzner server migration: prod box 91.98.44.8 (4GB fsn1) ->

### Issues opened

- **AR** [#52](https://github.com/jaywedgeworth22/Autorotate/issues/52): Rebrand (Autorotate.codes), Native Android Companion App & Apple
- **AR** [#53](https://github.com/jaywedgeworth22/Autorotate/issues/53): Web and iOS utility and power enhancements — · PR
- **AR** [#54](https://github.com/jaywedgeworth22/Autorotate/issues/54): Merge — App Builder PWA with this monorepo — · merged as
- **AR** [#55](https://github.com/jaywedgeworth22/Autorotate/issues/55): Owner: Developer portal App IDs for Autorotate — leftover from . Git
- **AR** [#56](https://github.com/jaywedgeworth22/Autorotate/issues/56): Dependabot leftover radix/react PRs — · after #16. Remaining npm PRs
- **CT** [#2174](https://github.com/jaywedgeworth22/Congress.Trade/issues/2174): 2026-08-21 — KIMI — PLANNED — [P2] Deploy hygiene: delete .bak/debug workflows
- **DD** [#129](https://github.com/jaywedgeworth22/DealDex/issues/129): 2026-08-22 — IN PROGRESS — Vercel Web Analytics. Branch
- **DD** [#131](https://github.com/jaywedgeworth22/DealDex/issues/131): 2026-08-22 — IN PROGRESS — Owner DD AppIcon + isolated favicon. Branch
- **DD** [#133](https://github.com/jaywedgeworth22/DealDex/issues/133): 2026-08-22 — IN PROGRESS — Android + PWA isolated DD. Branch
- **DD** [#135](https://github.com/jaywedgeworth22/DealDex/issues/135): 2026-08-22 — IN PROGRESS — Scan box contrast + SCAN label. Branch
- **DD** [#137](https://github.com/jaywedgeworth22/DealDex/issues/137): 2026-08-22 — IN PROGRESS — Public host dealdex.net. Branch
- **DD** [#140](https://github.com/jaywedgeworth22/DealDex/issues/140): 2026-08-22 — DEPLOYED — Vercel Web Analytics (#128 squash 148780af)
- **DD** [#141](https://github.com/jaywedgeworth22/DealDex/issues/141): 2026-08-22 — COMPLETED - Point DealDex production at dealdex.net. Landed
- **DD** [#142](https://github.com/jaywedgeworth22/DealDex/issues/142): 2026-08-22 — COMPLETED - Android + PWA use isolated DD. Merged #132
- **DD** [#143](https://github.com/jaywedgeworth22/DealDex/issues/143): 2026-08-22 — COMPLETED - Tighter DD AppIcon on ST grid. Merged #130
- **DD** [#144](https://github.com/jaywedgeworth22/DealDex/issues/144): 2026-08-22 — COMPLETED — DealDex.net domain, net.dealdex bundle
- **DD** [#146](https://github.com/jaywedgeworth22/DealDex/issues/146): 2026-08-22 — IN PROGRESS — Vercel Speed Insights
- **DD** [#148](https://github.com/jaywedgeworth22/DealDex/issues/148): 2026-08-22 — PICKUP — Analytics already live; remaining
- **DD** [#149](https://github.com/jaywedgeworth22/DealDex/issues/149): 2026-08-22 — DEPLOYED — Vercel Web Analytics (#128 squash 148780af)
- **DD** [#150](https://github.com/jaywedgeworth22/DealDex/issues/150): 2026-08-21 — DEPLOYED — #118 / #117 scan layout + subtitle
- **DD** [#151](https://github.com/jaywedgeworth22/DealDex/issues/151): 2026-08-22 — COMPLETED - Point DealDex production at dealdex.net. Landed
- **DD** [#152](https://github.com/jaywedgeworth22/DealDex/issues/152): 2026-08-22 — COMPLETED — Build app under net.dealdex bundle
- **DD** [#155](https://github.com/jaywedgeworth22/DealDex/issues/155): 2026-08-22 — IN PROGRESS — Publish native Android + iOS with website
- **PS** [#13](https://github.com/jaywedgeworth22/Personal-Site/issues/13): 2026-08-22 — IN PROGRESS — Personal Hobby Vercel + fleet Drive backup
- **PS** [#15](https://github.com/jaywedgeworth22/Personal-Site/issues/15): 2026-08-22 — DEPLOYED — Personal Hobby Vercel + backup handoff. GitHub
- **PS** [#18](https://github.com/jaywedgeworth22/Personal-Site/issues/18): 2026-08-22 — IN PROGRESS — Vercel Web Analytics
- **ST** [#3047](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3047): Hetzner server migration: prod box 91.98.44.8 (4GB fsn1) ->

### Effort board

- **CT** `Antigravity` 2026-08-22 — IN PROGRESS #2178 — Remove sub-month timeframes, render ticker analytics, iPad Trends 2-col, and fix Launchpad pseudo-apps root cause (branch `antigravity/sub-month-timeframe-and-launchpad-fix`). Web/iOS: removed 1d and 7d from Trades & Trends filter dropdowns (min window = 1 Month / 30d). iOS: render TickerAnalytics (Buy Pressure meter, top buyers/sellers with avatars, bac
- **CT** `Antigravity` 2026-08-22 — COMPLETED/DEPLOYED #2172 (`828b0149`) — Full-stack audit fixes, backend I/O cache & ST market data integration, web polish, iOS core parity (branch `antigravity/full-stack-fixes-and-ios-parity`). Backend: cached buildEnvironmentValues at isolate boot, global error/rejection handlers, SQLite pragmas (busy_timeout, synchronous NORMAL, cache_size, mmap_size), hardened ST peer c
- **CT** `Grok` 2026-08-22 — IN PROGRESS — iOS disclaimer under title, cold-start 3s slide (board `08b3f53c`, branch `grok/ios-disclaimer-header`, worktree `~/apps/congress — header`). ⓘ is always in the nav bar but the banner lived in the ScrollView, so a tap while scrolled looked broken. Banner now sits in `FeedDisclaimerHeader` under the wordmark above filters; filters slide with it;
- **CT** `Grok` 2026-08-22 — COMPLETED — Submit Congress.Trade iOS 1.0.81 from Tahoe GM with physical-device deletion recording (board `56cefc26`, branch `grok/asc-1-0-resubmit`). Owner "has issues" was Invalid Binary: Mac-built `202608202100` on macOS 27.0 beta (`26A5416b`) flips WAITING_FOR_REVIEW → INVALID_BINARY in ~45s. First API pass also missed IAPs (`subscription` is not a reviewSubmissionIte
- **CT** `Grok` 2026-08-22 — IN PROGRESS — iOS filter bar in the opaque light header, tight under the title, sticky on scroll (board `06ddcb30`, branch `grok/filter-header-sticky`, worktree `~/apps/congress — header`). Owner screenshots: pills sat on the cool grey page with a gap under the wordmark; `ultraThinMaterial` + 92% `panel` read as a blue wash and swam on scroll. `FeedStickyBar` is
- **CT** `Grok` 2026-08-22 — IN PR — Trust github-actions[bot] on same-repo gitleaks (branch `grok/gitleaks-trust-actions-bot`). Auto-update-from-main runs as that bot; security.yml refused it so required gitleaks went red and auto-merge sat forever (#1966 class). Scan still runs. Forks still refused
- **CT** `Grok` `Cursor` 2026-08-22 — IN PR — Unstick #2159 hide-retracted filing detail (branch `grok/unstick-2159`). Merged origin/main (kept PIPELINE_TX_SOURCES_SQL from #2161 era). Unique leftover is a SQLite filing-detail test that unpublished rows stay off GET /filings. Comment-only rest/admin wording. Lands the test — opened; does not steal extract
- **CT** `Cursor` 2026-08-22 — IN PROGRESS — iOS Account / tab footer matches website (disclaimer above links) (branch `cursor/settings-disclaimer-above-links-ecb2`). Account settings popup had Privacy/Terms then the disclaimer. Website `.site-footer` is the reverse. Shared `SiteFooterStack` now used by Account, leftover Settings, and `AppLegalFooter` on every tab. Keepouts: extract, #1959, Infisic
- **CT** `Cursor` 2026-08-22 — COMPLETED/MERGED #2156 (`51c29c47`) — Trends #/$ toggles, KPI center, collapsing drawer headers (branch `cursor/trends-kpi-center-toggles-ecb2`). `#`/`$` 14px/700 black; Buys vs Sells matched. KPI extras inside `.v`. Drawer tickers `var( — text)`. Company/politician heroes sticky-shrink; trade fades compact title. Keepouts held
- **CT** `Cursor` 2026-08-22 — IN PROGRESS — Trends toggles + drawer collapsing header (branch `cursor/trends-kpi-center-toggles-ecb2`, PR #2156). `#`/`$` match and black; KPI figures center under pinned headings. Drawer tickers are `var( — text)`, not accent blue. Company/politician heroes sticky-shrink (logo/avatar + name) into the ✕ row on scroll; trade fades its topbar summary in only after the h
- **CT** `Cursor` 2026-08-22 — IN PROGRESS — Sector amounts + By Sector title + mobile logo + Directory sort/rows ink (branch `cursor/sector-flow-logo-nudge-ecb2`). Web flow-row $ matches sector-name `var( — text)`. Web heading is By Sector (large figure is total volume); iOS stays Net Flow by Sector. Mobile web brand logo shifts 1ch off the left edge. Directory Sort + Rows menus use `glyphGrey` + M
- **CT** `Cursor` 2026-08-22 — COMPLETED/MERGED #2156 (`51c29c47`) — Trends #/$ toggles, KPI center, collapsing drawer headers (branch `cursor/trends-kpi-center-toggles-ecb2`). `#`/`$` 14px/700 black; Buys vs Sells matched. KPI extras inside `.v`. Drawer tickers `var( — text)`. Company/politician heroes sticky-shrink; trade fades compact title. Gates: 288 files / 3685 tests; CI typecheck+test + git
- **CT** `Grok` 2026-08-22 — IN PROGRESS — iOS filter chrome grey + push settings none/filings/watchlist (board `e235bb0e` `655eccbf`; also `0c5398a5` `c6f8f389` `4ec359a1` `e60c71cd`; #1046 slice; branch `grok/filter-chrome-push-settings`, worktree `~/apps/congress — push`). Filter chevrons/glyphs/3 Months/info/hamburger/exchange arrows one semi-dark grey; no system blue except selected-opt
- **UM** `Grok` 2026-08-22 — IN PROGRESS — Copilot CLI API-equivalent + Infisical project bake (branch `grok/api-equivalent-more`, worktree `~/apps/usage — equivalent-more`, board `75e48fd4`). Copilot CLI `session.shutdown` modelMetrics tokens × list price, estimated never cash. Restore `INFISICAL_UM_PROJECT_ID` bake so #1316 can deploy (Coolify rolled back: Infisical `projectId=undefined` aft
- **UM** `Grok` `Codex` 2026-08-22 — COMPLETED/MERGED #1316 `5e15b38b` — API-equivalent cost for — + — Build (board `8cff91d9`). Not deployed: Coolify rolled back to #1314 because #1315 dropped the Infisical project UUID fallback. Follow-up `grok/api-equivalent-more`
- **UM** `Grok` 2026-08-22 — IN PROGRESS — Fleet projects, Manually only labels, stale refetch, local copy (branch `grok/fleet-projects-manual`, worktree `~/apps/usage — projects`, board `1a5de7b6`). Seed ST/CT/UM/DealDex/Personal-Site/Autorotate/ContactLogo/Fleet. Non-poll providers never look fetchable. Old pollable snapshots refetch. Secret-free workspace export/import for Local UM. Re
- **UM** `Grok` 2026-08-22 — IN PROGRESS — Receipt inbox subjects, April expenses, Apple Calendar ICS, — classify (branch `grok/receipt-bills`, worktree `~/apps/usage — bills`). Dashboard shows bounded receipt subject/amount. Owner-expense `usage` kind plus due dates. Unlisted `/api/bills.ics`. Worker rules+Grok/DeepSeek can POST expenses. FMP/Massive no next due. Domain renewals ar
- **DD** `Cursor` `Grok` 2026-08-22 — PICKUP — Analytics already live; remaining Autorotate (`autorotate.codes`, GitHub Autorotate) + DealDex.net copy is — Auto. — is no longer owner. Board comment on DealDex #129
- **DD** `Grok` 2026-08-22 — DEPLOYED — Vercel Web Analytics (#128 squash `148780af`). Canonical check is https://dealdex.net (was documented on dealdex.online). Privacy discloses cookie-less page views. Board `e65921a0`
- **DD** `Cursor` 2026-08-23 — COMPLETED/MERGED #156 — OG share card. TCGPlayer dropped. Footer eBay · Mercari + dealdex.net. Wordmark ~400px tall, 48px subtitle. Cache-bust `og.jpg?v=share-20260823`. Squash `1e9a017`. PR #154. TestFlight `net.dealdex` 1.0.2 (202608230250) internal testers READY_FOR_BETA_TESTING. Sideload APK on `/install` after Vercel Production. Landed DealDex #136
- **DD** `Grok` 2026-08-22 — COMPLETED - Android + PWA use isolated DD. Merged #132. Scan over eBay/Mercari; Android/PWA isolated DD. <! — wb-agent-report:2d4aff5cad2847eb807cfd03e41f999a — >
- **DD** `Grok` 2026-08-22 — COMPLETED - Tighter DD AppIcon on ST grid. Merged #130. AppIcon is the owner 1024 PNG resized. Favicon is the isolated transparent DD. <! — wb-agent-report:3b2d4b881f214f88abc49a658626b6ee — >
- **DD** `Antigravity` 2026-08-22 — COMPLETED — Build app under net.dealdex bundle, dealdex.net domain, sync iOS/Android/Favicon/ASC icons. Branch `ag/bundle-net-and-builds`, worktree `~/apps/dealdex- `
- **DD** `Antigravity` 2026-08-22 — COMPLETED — DealDex.net domain, net.dealdex bundle ID, iOS 17 + Xcode 26 doc format + icons + dev team link, and Android build. Branch `ag/net-domain-and-ios-setup`, worktree `~/apps/dealdex- `
- **PS** `Cursor` 2026-08-22 — DEPLOYED - Enable Vercel Web Analytics on Personal-Site. PR #17 on production. insights/script.js + insights/view 200 on personal-site-jayw.vercel.app. <! — wb-agent-report:365732267fe143c589160c3f6bb59cf4 — >
- **PS** `Cursor` 2026-08-22 — DEPLOYED — Vercel Web Analytics (PR #17). `@vercel/analytics/react` in TanStack Start root. Production `https://personal-site-jayw.vercel.app/` loaded `/_vercel/insights/script.js` and POSTed `/_vercel/insights/view` HTTP 200. Board `36573226`
- **PS** `Cursor` `Grok` 2026-08-22 — PICKUP — github-sync chat already DEPLOYED (Hobby Vercel + Drive #94). — Auto owns remaining apex/domain cutover if asked. — is no longer owner
- **PS** `Grok` 2026-08-22 — DEPLOYED - Personal-Site on personal Hobby Vercel + GitHub/Drive backup. Personal Vercel Hobby project personal-site READY at https://personal-site-jayw.vercel.app/ (About copy + Doximity view URL). PRs #12 #14. Apex jays.services still Cloudflare A 64.239.109.1 until domain cutover. Drive backups: coordinator #94. <! — wb-agent-report:3a5fa02ce0ad416bba6801da1ae0f5
- **PS** `Grok` 2026-08-22 — DEPLOYED — Personal Hobby Vercel + backup handoff. Production `https://personal-site-jayw.vercel.app/` HTTP 200 (About copy + Doximity view URL). Apex still Cloudflare A `64.239.109.1`. PRs #12 #14. Board `3a5fa02c`
- **PS** `Cursor` 2026-08-22 — COMPLETED — Vercel Web Analytics. `@vercel/analytics/react` in `site/src/routes/__root.tsx`. PR #17
- **AR** `Antigravity` Site & App Triage, Security Fixes, Cross-Platform Master 3D Icons, and iOS/Android Release Builds — · COMPLETED 2026-08-22. Merged PR #47 (canary secret isolation) and added dry-run live rotate guard (`shouldMintProviderCredential`). Generated and linked full-bleed 3D silver key master app icon assets across Web (favicon, apple-touch-icon, app-icon), Apple (iOS/macOS 1024x1024 asse
- **AR** `Cursor` `Antigravity` `Grok` 2026-08-22 — COMPLETED - Autorotate Apple IDs codes.autorotate after autorotate.codes. Apple IDs live in — #48. Closed duplicate — #50. Portal App IDs still owner. dealdex.net HTTP 200. <! — wb-agent-report:56b8070663e7402b946796c1d86dea80 — >
- **AR** `Grok` `Antigravity` `Cursor` Apple IDs in git (`codes.autorotate`) — PR [#50](https://github.com/jaywedgeworth22/TopSpin/pull/50) closed as duplicate of — [#48](https://github.com/jaywedgeworth22/TopSpin/pull/48) which already sets `codes.autorotate` / `codes.autorotate.macos`. — 2026-08-22: do not merge both. Owner still creates those App IDs in the Developer portal before TestFlight
- **AR** `Antigravity` Rebrand (`Autorotate.codes`), Native Android Companion App & Apple Build Verification — · COMPLETED 2026-08-22. Rebranded monorepo across Web (`Autorotate.codes`), Apple apps (`codes.autorotate`, `codes.autorotate.macos`, `codes.autorotate.shared`), and added native Android companion app (`android/` with Kotlin + Jetpack Compose Material 3, Biometrics, QR scanner, .env pa
- **CL** `Antigravity` 2026-08-22 — COMPLETED — Xcode project (iOS & macOS), ContactLogo.com domain alignment, Android app build. Xcode project generation with iOS 17+ min deployment, document format 26 compatibility, bundle IDs `com.contactlogo` and `com.contactlogo.macos`, display name `ContactLogo`, category `utilities`, Dev Team `CC8UTF7ATG`, verified on iOS simulator with screenshot, domain aligned
- **CL** `Cursor` 2026-08-22 — IN PROGRESS — Domain + CI leftovers (uncommitted). Official host `contactlogo.com`. Added `.github/workflows/ci.yml` (web Node job + macOS `swift test`) and `AGENTS.md`. Did not run `onboard-new-app.sh` (must be from a fleet worktree, not `~/Code`). Cloudflare jay account has no `contactlogo.com` zone; no DNS invented. Personal-Site project list now points at C
- **AFC** `Grok` 2026-08-22 — IN PROGRESS — Harden THE BOARD two-way sync (`mac-collab-writeback`). Board `c76c7feb`. Worktree `~/apps/fleet — writeback` @ `grok/board-writeback`. Stopped the looping first-run job; surgical md; applied-status bootstrap; REST Issues; no `~/Code` git
- **AFC** `Grok` 2026-08-22 — IN PROGRESS — Harden THE BOARD two-way sync (`mac-collab-writeback`). Board `c76c7feb`. Worktree `~/apps/fleet — writeback` @ `grok/board-writeback`. Stopped the looping first-run job; surgical md; applied-status bootstrap; REST Issues; no `~/Code` git
- **AFC** `Grok` 2026-08-22 — DEPLOYED — Redirect board.jays.services to mac.jays.services/board. Cloudflare proxied `AAAA 100::` + Single Redirect 302 (query string preserved). Verified `Location: https://mac.jays.services/board`. Board `b89c8330`. Branch `grok/board-redirect`
- **AFC** `Grok` 2026-08-22 — IN PROGRESS — KIMI unclaim leftover work; claims must show the claim date. Claimed Sat, Aug 22, 2026. Board `f8126c1e`. Worktree `~/apps/fleet — clear` @ `grok/kimi-unclaim-claim-dates`. KIMI must have nothing In Progress or Planned. Slack/board ` — where` carry `claimed: <date>`

## 2026-08-21

*170 PRs merged · 45 issues opened · 19 issues closed · 41 effort rows*

### Merged PRs

- **AR** [#1](https://github.com/jaywedgeworth22/Autorotate/pull/1): chore(deps): bump @radix-ui/react-separator from 1.1.8 to 1.1.15 in /apps/web _(by dependabot[bot])_
- **AR** [#2](https://github.com/jaywedgeworth22/Autorotate/pull/2): chore(deps): bump @radix-ui/react-dropdown-menu from 2.1.16 to 2.1.24 in /apps/web _(by dependabot[bot])_
- **AR** [#3](https://github.com/jaywedgeworth22/Autorotate/pull/3): chore(deps): bump github/codeql-action from 3 to 4 _(by dependabot[bot])_
- **AR** [#4](https://github.com/jaywedgeworth22/Autorotate/pull/4): chore(deps): bump gitleaks/gitleaks-action from 2 to 3 _(by dependabot[bot])_
- **AR** [#5](https://github.com/jaywedgeworth22/Autorotate/pull/5): chore(deps): bump softprops/action-gh-release from 2 to 3 _(by dependabot[bot])_
- **AR** [#6](https://github.com/jaywedgeworth22/Autorotate/pull/6): chore(deps): bump actions/checkout from 4 to 7 _(by dependabot[bot])_
- **AR** [#7](https://github.com/jaywedgeworth22/Autorotate/pull/7): chore(deps): bump actions/setup-node from 4 to 7 _(by dependabot[bot])_
- **AR** [#8](https://github.com/jaywedgeworth22/Autorotate/pull/8): chore(deps): bump @radix-ui/react-slider from 1.3.6 to 1.4.7 in /apps/web _(by dependabot[bot])_
- **AR** [#9](https://github.com/jaywedgeworth22/Autorotate/pull/9): chore(deps): bump @radix-ui/react-hover-card from 1.1.15 to 1.1.23 in /apps/web _(by dependabot[bot])_
- **AR** [#10](https://github.com/jaywedgeworth22/Autorotate/pull/10): chore(deps): bump @radix-ui/react-checkbox from 1.3.3 to 1.3.11 in /apps/web _(by dependabot[bot])_
- **AR** [#11](https://github.com/jaywedgeworth22/Autorotate/pull/11): chore(deps): bump @radix-ui/react-progress from 1.1.8 to 1.1.16 in /apps/web _(by dependabot[bot])_
- **AR** [#12](https://github.com/jaywedgeworth22/Autorotate/pull/12): chore(deps-dev): bump eslint-plugin-react-refresh from 0.4.26 to 0.5.4 in /apps/web _(by dependabot[bot])_
- **AR** [#13](https://github.com/jaywedgeworth22/Autorotate/pull/13): chore(deps): bump react and @types/react in /apps/web _(by dependabot[bot])_
- **AR** [#14](https://github.com/jaywedgeworth22/Autorotate/pull/14): chore(deps): bump @radix-ui/react-switch from 1.2.6 to 1.3.7 in /apps/web _(by dependabot[bot])_
- **AR** [#15](https://github.com/jaywedgeworth22/Autorotate/pull/15): chore(deps): bump @radix-ui/react-toggle from 1.1.10 to 1.1.18 in /apps/web _(by dependabot[bot])_
- **AR** [#16](https://github.com/jaywedgeworth22/Autorotate/pull/16): chore(repo): fleet onboarding — TopSpin joins ai-fleet-coordinator (TS) _(by jaywedgeworth22)_
- **AR** [#17](https://github.com/jaywedgeworth22/Autorotate/pull/17): fix(core): do not rotate or commit when no target can receive the new value _(by jaywedgeworth22)_
- **AR** [#21](https://github.com/jaywedgeworth22/Autorotate/pull/21): docs(repo): close out fleet onboard effort-board row _(by jaywedgeworth22)_
- **AR** [#25](https://github.com/jaywedgeworth22/Autorotate/pull/25): chore(deps): bump actions/setup-python from 5 to 7 _(by dependabot[bot])_
- **AR** [#26](https://github.com/jaywedgeworth22/Autorotate/pull/26): chore(deps): bump @radix-ui/react-menubar from 1.1.16 to 1.1.24 in /apps/web _(by dependabot[bot])_
- **AR** [#27](https://github.com/jaywedgeworth22/Autorotate/pull/27): chore(deps-dev): bump autoprefixer from 10.4.23 to 10.5.4 in /apps/web _(by dependabot[bot])_
- **AR** [#28](https://github.com/jaywedgeworth22/Autorotate/pull/28): chore(deps-dev): bump eslint-plugin-react-hooks from 7.0.1 to 7.1.1 in /apps/web _(by dependabot[bot])_
- **AR** [#29](https://github.com/jaywedgeworth22/Autorotate/pull/29): chore(deps): bump @hono/node-server from 1.19.17 to 2.1.1 in /apps/web _(by dependabot[bot])_
- **AR** [#30](https://github.com/jaywedgeworth22/Autorotate/pull/30): chore(deps-dev): bump postcss from 8.5.6 to 8.5.26 in /apps/web _(by dependabot[bot])_
- **AR** [#31](https://github.com/jaywedgeworth22/Autorotate/pull/31): chore(deps): bump @radix-ui/react-aspect-ratio from 1.1.8 to 1.1.15 in /apps/web _(by dependabot[bot])_
- **AR** [#33](https://github.com/jaywedgeworth22/Autorotate/pull/33): chore(deps): bump @radix-ui/react-context-menu from 2.2.16 to 2.3.7 in /apps/web _(by dependabot[bot])_
- **AR** [#34](https://github.com/jaywedgeworth22/Autorotate/pull/34): chore(deps-dev): bump esbuild from 0.27.2 to 0.28.2 in /apps/web _(by dependabot[bot])_
- **AR** [#36](https://github.com/jaywedgeworth22/Autorotate/pull/36): feat(ios): prompt to update on first launch _(by jaywedgeworth22)_
- **AR** `Grok` [#38](https://github.com/jaywedgeworth22/Autorotate/pull/38): feat: merge — App Builder PWA with GitHub TopSpin _(by jaywedgeworth22)_
- **AR** [#41](https://github.com/jaywedgeworth22/Autorotate/pull/41): fix(web): verify Infisical against the same name PUSH wrote _(by jaywedgeworth22)_
- **AR** [#42](https://github.com/jaywedgeworth22/Autorotate/pull/42): Apache-2.0 relicensing, Kimi dump backup, extra catalog _(by jaywedgeworth22)_
- **CT** [#1959](https://github.com/jaywedgeworth22/Congress.Trade/pull/1959): Add fail-soft OpenRouter OCR path for executive scanned_pdf (#1575) _(by jaywedgeworth22)_
- **CT** [#1965](https://github.com/jaywedgeworth22/Congress.Trade/pull/1965): Directory photos, owner, committees, and horizon labels _(by jaywedgeworth22)_
- **CT** [#1966](https://github.com/jaywedgeworth22/Congress.Trade/pull/1966): Count backfilled CT trades in latency coverage (#1523, #1462) _(by jaywedgeworth22)_
- **CT** [#1967](https://github.com/jaywedgeworth22/Congress.Trade/pull/1967): Fix deep-link aliases, quiet anonymous loads, and primary-only feed _(by jaywedgeworth22)_
- **CT** [#1973](https://github.com/jaywedgeworth22/Congress.Trade/pull/1973): docs(audit): web / iOS parity matrix (2026-08-17) _(by jaywedgeworth22)_
- **CT** [#1976](https://github.com/jaywedgeworth22/Congress.Trade/pull/1976): Read-only House/Senate/OGE ingestion integrity audit _(by jaywedgeworth22)_
- **CT** [#1981](https://github.com/jaywedgeworth22/Congress.Trade/pull/1981): docs(audit): Stripe + StoreKit purchases end-to-end (report-only) _(by jaywedgeworth22)_
- **CT** [#2014](https://github.com/jaywedgeworth22/Congress.Trade/pull/2014): Close politician photo party rings all the way around _(by jaywedgeworth22)_
- **CT** [#2015](https://github.com/jaywedgeworth22/Congress.Trade/pull/2015): Stop claiming we discovered a trade before it happened _(by jaywedgeworth22)_
- **CT** [#2040](https://github.com/jaywedgeworth22/Congress.Trade/pull/2040): docs: retire Deno Deploy and Turso as current-shape _(by jaywedgeworth22)_
- **CT** [#2042](https://github.com/jaywedgeworth22/Congress.Trade/pull/2042): Wire real Sentry for Coolify Deno-in-Docker _(by jaywedgeworth22)_
- **CT** [#2064](https://github.com/jaywedgeworth22/Congress.Trade/pull/2064): fix: CT follow-ups from ST audit #2802 (CI, provenance, Massive last-resort) _(by jaywedgeworth22)_
- **CT** [#2072](https://github.com/jaywedgeworth22/Congress.Trade/pull/2072): fix(web-a11y): restore table semantics, real radio group, honest card labels _(by jaywedgeworth22)_
- **CT** [#2082](https://github.com/jaywedgeworth22/Congress.Trade/pull/2082): Pushover alert on new Premium activation with live totals _(by jaywedgeworth22)_
- **CT** [#2089](https://github.com/jaywedgeworth22/Congress.Trade/pull/2089): effort-log: fleet setup-audit findings (KIMI, 2026-08-21) _(by jaywedgeworth22)_
- **CT** [#2110](https://github.com/jaywedgeworth22/Congress.Trade/pull/2110): fix(extract): stop deterministic drain re-flagging future_tx_date hard-fails _(by jaywedgeworth22)_
- **CT** [#2112](https://github.com/jaywedgeworth22/Congress.Trade/pull/2112): fix(extract): do not drop the first ownerless House PTR row as chrome _(by jaywedgeworth22)_
- **CT** [#2117](https://github.com/jaywedgeworth22/Congress.Trade/pull/2117): ci: drop pull_request_target auto-merge; same-repo guard; no GH_PAT _(by jaywedgeworth22)_
- **CT** [#2118](https://github.com/jaywedgeworth22/Congress.Trade/pull/2118): docs: redact public credential inventory; point at private attack map _(by jaywedgeworth22)_
- **CT** [#2119](https://github.com/jaywedgeworth22/Congress.Trade/pull/2119): chore(deps): bump @aws-sdk/client-s3 from 3.1111.0 to 3.1112.0 in /app _(by dependabot[bot])_
- **CT** [#2120](https://github.com/jaywedgeworth22/Congress.Trade/pull/2120): fix(ios): Premium belongs to the account, never auto-linked from a device _(by jaywedgeworth22)_
- **CT** [#2121](https://github.com/jaywedgeworth22/Congress.Trade/pull/2121): fix(legal): add no-warranty / no-guarantee language to Terms of Service _(by jaywedgeworth22)_
- **CT** [#2122](https://github.com/jaywedgeworth22/Congress.Trade/pull/2122): fix(theme): delete the Sepia theme (web + iOS) _(by jaywedgeworth22)_
- **CT** [#2123](https://github.com/jaywedgeworth22/Congress.Trade/pull/2123): fix(ios): semantic icon colors instead of accent blue _(by jaywedgeworth22)_
- **CT** [#2124](https://github.com/jaywedgeworth22/Congress.Trade/pull/2124): fix(ios-tests): stop chamber-filter test racing refreshTrends()'s latency call _(by jaywedgeworth22)_
- **CT** [#2125](https://github.com/jaywedgeworth22/Congress.Trade/pull/2125): fix(ios): do not silent-link an Apple purchase onto a Stripe Premium session _(by jaywedgeworth22)_
- **CT** [#2126](https://github.com/jaywedgeworth22/Congress.Trade/pull/2126): fix(ios-tests): isolate MockURLProtocol.handler across CongressTradeTests _(by jaywedgeworth22)_
- **CT** [#2133](https://github.com/jaywedgeworth22/Congress.Trade/pull/2133): feat(ios): prompt to update on first launch _(by jaywedgeworth22)_
- **CT** [#2134](https://github.com/jaywedgeworth22/Congress.Trade/pull/2134): OpenRouter Flash stays on latest; skip mistral-ocr on vision models _(by jaywedgeworth22)_
- **CT** `Grok` [#2140](https://github.com/jaywedgeworth22/Congress.Trade/pull/2140): Cascade cheap Qwen VL after a missed — CLI PTR solo pass _(by jaywedgeworth22)_
- **CT** [#2141](https://github.com/jaywedgeworth22/Congress.Trade/pull/2141): fix(vision-worker): do not publish a truncated Qwen cascade hit _(by jaywedgeworth22)_
- **CT** `Grok` [#2142](https://github.com/jaywedgeworth22/Congress.Trade/pull/2142): fix(vision-worker): do not publish a truncated local — CLI pass _(by jaywedgeworth22)_
- **CT** `Grok` [#2143](https://github.com/jaywedgeworth22/Congress.Trade/pull/2143): fix(extract): stop local-vision re-OCR loop and auto-publish clean — rows _(by jaywedgeworth22)_
- **CT** `Grok` [#2144](https://github.com/jaywedgeworth22/Congress.Trade/pull/2144): fix(extract): do not auto-publish an all-no-amount local — extract _(by jaywedgeworth22)_
- **CT** `Grok` [#2146](https://github.com/jaywedgeworth22/Congress.Trade/pull/2146): fix(vision-worker): rotate sideways House PTR scans upright before _(by jaywedgeworth22)_
- **CT** [#2147](https://github.com/jaywedgeworth22/Congress.Trade/pull/2147): fix(vision-worker): do not guess 270 when upright-rotate OCR is silent _(by jaywedgeworth22)_
- **CT** [#2148](https://github.com/jaywedgeworth22/Congress.Trade/pull/2148): fix(vision-worker): attach upright pages to PDF-native cascade _(by jaywedgeworth22)_
- **CT** `Grok` [#2149](https://github.com/jaywedgeworth22/Congress.Trade/pull/2149): fix(vision-worker): skip truncated — CLI on long Khanna PTRs _(by jaywedgeworth22)_
- **CT** [#2150](https://github.com/jaywedgeworth22/Congress.Trade/pull/2150): fix(vision-worker): do not publish a partial PDF-native chunk packet _(by jaywedgeworth22)_
- **CT** [#2151](https://github.com/jaywedgeworth22/Congress.Trade/pull/2151): fix(extract): do not park a filing for one blank row or Clerk filed_date _(by jaywedgeworth22)_
- **CT** [#2152](https://github.com/jaywedgeworth22/Congress.Trade/pull/2152): Send SENATE_RELAY_SECRET on Mac relay POST routes _(by jaywedgeworth22)_
- **CT** [#2153](https://github.com/jaywedgeworth22/Congress.Trade/pull/2153): fix(extract): truncated review payload must not block a complete vision read _(by jaywedgeworth22)_
- **CT** [#2154](https://github.com/jaywedgeworth22/Congress.Trade/pull/2154): fix(extract): compare persistable dated rows when guarding vision overwrite _(by jaywedgeworth22)_
- **CT** [#2155](https://github.com/jaywedgeworth22/Congress.Trade/pull/2155): Grey filter chrome and filing/watchlist push settings _(by jaywedgeworth22)_
- **CT** [#2156](https://github.com/jaywedgeworth22/Congress.Trade/pull/2156): Match Trends #/$ toggles, center KPIs, and collapse drawer headers _(by jaywedgeworth22)_
- **CT** [#2158](https://github.com/jaywedgeworth22/Congress.Trade/pull/2158): iOS Account footer: disclaimer above Privacy/Terms like the website _(by jaywedgeworth22)_
- **CT** [#2160](https://github.com/jaywedgeworth22/Congress.Trade/pull/2160): fix(extract): retire leftover primary when a complete vision set publishes _(by jaywedgeworth22)_
- **CT** [#2161](https://github.com/jaywedgeworth22/Congress.Trade/pull/2161): fix(delivery): unknown filing GET must 404, not 500 _(by jaywedgeworth22)_
- **CT** [#2162](https://github.com/jaywedgeworth22/Congress.Trade/pull/2162): fix(extract): compare dated rows when superseding a resolved confirm _(by jaywedgeworth22)_
- **CT** [#2163](https://github.com/jaywedgeworth22/Congress.Trade/pull/2163): fix(delivery): keep retracted rows off filing detail (#2159 unstick) _(by jaywedgeworth22)_
- **CT** [#2164](https://github.com/jaywedgeworth22/Congress.Trade/pull/2164): ci: let github-actions[bot] run same-repo gitleaks _(by jaywedgeworth22)_
- **CT** `Grok` [#2165](https://github.com/jaywedgeworth22/Congress.Trade/pull/2165): fix(vision-worker): stop same-PTR re-OCR and isolate — CLI _(by jaywedgeworth22)_
- **CT** [#2170](https://github.com/jaywedgeworth22/Congress.Trade/pull/2170): fix(ios): pin filter pills in the opaque light header _(by jaywedgeworth22)_
- **CT** [#2173](https://github.com/jaywedgeworth22/Congress.Trade/pull/2173): Sit web filter pills in the white header and keep them sticky _(by jaywedgeworth22)_
- **CL** [#3](https://github.com/jaywedgeworth22/ContactLogo/pull/3): effort-log: bootstrap + P0 history purge recorded (KIMI, 2026-08-21) _(by jaywedgeworth22)_
- **CL** [#5](https://github.com/jaywedgeworth22/ContactLogo/pull/5): Retire BadgeBook and Crest names — GitHub slug is ContactLogo _(by jaywedgeworth22)_
- **CL** [#6](https://github.com/jaywedgeworth22/ContactLogo/pull/6): Fix URL format in README site link _(by jaywedgeworth22)_
- **CL** [#7](https://github.com/jaywedgeworth22/ContactLogo/pull/7): folder, backups, and merge _(by jaywedgeworth22)_
- **CL** [#8](https://github.com/jaywedgeworth22/ContactLogo/pull/8): Web Google Contacts 2-way sync, canvas studio, iOS swipe triage & simulator, macOS shortcuts _(by jaywedgeworth22)_
- **CL** [#9](https://github.com/jaywedgeworth22/ContactLogo/pull/9): Update docs/EFFORT-LOG.md _(by jaywedgeworth22)_
- **DD** [#113](https://github.com/jaywedgeworth22/DealDex/pull/113): Transparent DD favicon and ST-grid iOS AppIcon _(by jaywedgeworth22)_
- **DD** [#115](https://github.com/jaywedgeworth22/DealDex/pull/115): Effort log: close DD favicon + ST-grid AppIcon _(by jaywedgeworth22)_
- **DD** [#118](https://github.com/jaywedgeworth22/DealDex/pull/118): Compact scan box, larger OG wordmark, new subtitle _(by jaywedgeworth22)_
- **DD** [#120](https://github.com/jaywedgeworth22/DealDex/pull/120): docs: close #117 / #118 on the effort board _(by jaywedgeworth22)_
- **DD** [#122](https://github.com/jaywedgeworth22/DealDex/pull/122): feat(ios): prompt to update on first launch _(by jaywedgeworth22)_
- **DD** [#124](https://github.com/jaywedgeworth22/DealDex/pull/124): Cross-Platform Power Features, Card Dossier, Evaluator, and Saved Ledger _(by jaywedgeworth22)_
- **ST** [#2797](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2797): fix(coord): tolerate slow/flappy Congress.Trade and Usage-Monitor lanes (#2550) _(by jaywedgeworth22)_
- **ST** [#2801](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2801): Retire leftover installable PWA; keep website and iOS _(by jaywedgeworth22)_
- **ST** [#2941](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2941): fix(coord): vendor-era pin check, durable call-volume, congress-read label _(by jaywedgeworth22)_
- **ST** [#2969](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2969): fix(llm): meter the provider's billed cost instead of a hand-maintained price table _(by jaywedgeworth22)_
- **ST** [#2971](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2971): fix(copy): make the two-space sentence rule actually render on the web _(by jaywedgeworth22)_
- **ST** [#2987](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2987): iOS/Mac: width-aware tab bar (>4 tabs on iPad and wide Mac) + iPad Air 11" layout pass _(by jaywedgeworth22)_
- **ST** [#2990](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2990): docs(handoff): DEEPSEEK review handoff note — instructions for fleet agents _(by jaywedgeworth22)_
- **ST** [#2991](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2991): ci: npm ci, SHA-pin gh, Dependabot Actions, pin-check on forks _(by jaywedgeworth22)_
- **ST** [#2992](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2992): docs(handoff): close out #2987 and write down what is still unfinished _(by jaywedgeworth22)_
- **ST** [#2994](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2994): build(deps): bump actions/cache from 4 to 6 _(by dependabot[bot])_
- **ST** [#2995](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2995): build(deps): bump actions/checkout from 4 to 7 _(by dependabot[bot])_
- **ST** [#2996](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2996): build(deps): bump actions/setup-python from 5 to 7 _(by dependabot[bot])_
- **ST** [#2997](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2997): build(deps): bump the observability group with 2 updates _(by dependabot[bot])_
- **ST** [#2998](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2998): build(deps-dev): bump eslint-config-next from 16.3.0 to 16.3.1 _(by dependabot[bot])_
- **ST** [#2999](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2999): build(deps): bump @xyflow/react from 12.11.2 to 12.11.3 _(by dependabot[bot])_
- **ST** [#3000](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3000): build(deps): bump better-sqlite3 from 13.0.2 to 13.0.3 _(by dependabot[bot])_
- **ST** [#3001](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3001): build(deps): bump lightweight-charts from 5.2.0 to 5.2.1 _(by dependabot[bot])_
- **ST** [#3002](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3002): fix(login): hero wordmark, equal-size provider buttons, expanded legal copy _(by jaywedgeworth22)_
- **ST** [#3003](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3003): Align the LLM catalog to display / OpenRouter / native slugs _(by jaywedgeworth22)_
- **ST** [#3005](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3005): fix(copy): web adopts iOS's Title Case, because iOS was the compliant side _(by jaywedgeworth22)_
- **ST** [#3006](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3006): Mark LLM catalog effort as merged (#3003) _(by jaywedgeworth22)_
- **ST** [#3007](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3007): Commit numeric settings on blur instead of silently losing them _(by jaywedgeworth22)_
- **ST** [#3008](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3008): Unfreeze the login wordmark, and two defects only the Mac showed _(by jaywedgeworth22)_
- **ST** [#3009](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3009): Native weekly value and momentum screens _(by jaywedgeworth22)_
- **ST** [#3010](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3010): fix(deploy): stop a top-level await from failing every image build _(by jaywedgeworth22)_
- **ST** [#3011](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3011): fix(deploy): fail the RTH drain when Coolify cannot be nudged _(by jaywedgeworth22)_
- **ST** [#3012](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3012): feat(ios): prompt to update on first launch _(by jaywedgeworth22)_
- **ST** [#3013](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3013): fix(strategy): abort abandoned gather so Roth/Paper runs can finish _(by jaywedgeworth22)_
- **ST** [#3014](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3014): fix(ci): setup-node 4→7 without breaking pin-check queue-safety _(by jaywedgeworth22)_
- **ST** [#3015](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3015): fix(llm): send OpenRouter family-latest aliases with the required ~ _(by jaywedgeworth22)_
- **ST** [#3018](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3018): fix(strategy): abort keyed Finnhub wave on gather timeout _(by jaywedgeworth22)_
- **ST** [#3019](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3019): fix(ios): full-card scan tap and honest last/next run _(by jaywedgeworth22)_
- **ST** `Claude` [#3022](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3022): docs(effort): close out the two — rows that landed today _(by jaywedgeworth22)_
- **ST** [#3023](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3023): ci(ios): unhang xcodebuild pipe and run XCTests _(by jaywedgeworth22)_
- **ST** [#3025](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3025): docs: record ios-build success after #3023 (232 XCTests, hang gone) _(by jaywedgeworth22)_
- **ST** [#3026](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3026): docs(handoff): quiescent-cutover deploy design, to replace the daytime ban _(by jaywedgeworth22)_
- **ST** [#3027](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3027): Rename WrappingHStackTests.swift to LayoutMathTests.swift _(by jaywedgeworth22)_
- **ST** [#3028](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3028): iOS: wide-window chrome, Admin tab, gear/bell, console-return fence _(by jaywedgeworth22)_
- **ST** [#3030](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3030): Unify website Google, GitHub, and Apple sign-in buttons _(by jaywedgeworth22)_
- **ST** [#3031](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3031): Redesign Activity: Alerts Center first, Strategy Runs, Order Fills, Audit Log _(by jaywedgeworth22)_
- **ST** [#3032](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3032): fix(rag): stop paging Starter 2M Pinecone write units on a Standard trial _(by jaywedgeworth22)_
- **ST** [#3034](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3034): docs: mark Activity layout #3031 completed on main _(by jaywedgeworth22)_
- **ST** [#3035](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3035): fix(quotes): do not stop the cascade on last-session close _(by jaywedgeworth22)_
- **ST** [#3036](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3036): docs: mark iOS wide-layout #3028 completed on main _(by jaywedgeworth22)_
- **ST** [#3037](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3037): Honor 5M Pinecone WU until Aug 27, then snap to free-tier _(by jaywedgeworth22)_
- **ST** [#3038](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3038): fix(rag): do not park ingest on numberless monthly-WU 429s during the 5M week _(by jaywedgeworth22)_
- **ST** [#3039](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3039): docs: mark Pinecone snap + RAG panel #3037 completed _(by jaywedgeworth22)_
- **ST** [#3040](https://github.com/jaywedgeworth22/Socratic.Trade/pull/3040): Fix Sentry Noise and CI Failures _(by jaywedgeworth22)_
- **UM** [#1303](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1303): fix(ios): keep last tab rows above the glass bar; calm Jay Old R2 _(by jaywedgeworth22)_
- **UM** [#1305](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1305): feat(ios): prompt to update on first launch _(by jaywedgeworth22)_
- **UM** [#1307](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1307): Stop inventing unpaid August subscription cash _(by jaywedgeworth22)_
- **UM** [#1309](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1309): Keep receipt-backed subscription charges on pause or delete _(by jaywedgeworth22)_
- **AFC** [#58](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/58): fix(watch): do not resurrect a poisoned dump.pm2 _(by jaywedgeworth22)_
- **AFC** [#59](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/59): Apple Notes: space sections and bullets _(by jaywedgeworth22)_
- **AFC** [#60](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/60): Apple Notes: &nbsp; after periods in HTML _(by jaywedgeworth22)_
- **AFC** [#61](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/61): docs(mac): fleet recovery lessons from the 2026-08-21 degradation _(by jaywedgeworth22)_
- **AFC** [#62](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/62): docs(mac): agent worktrees belong in ~/apps, not ~/Code _(by jaywedgeworth22)_
- **AFC** [#63](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/63): docs(sync): port #agent-sync skim filter into the versioned poller _(by jaywedgeworth22)_
- **AFC** [#64](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/64): docs(effort-log): record the 2026-08-21 shellular + pm2 + MCP root-cause _(by jaywedgeworth22)_
- **AFC** [#65](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/65): docs(processes): add pm2 orphan-holds-port recovery runbook _(by jaywedgeworth22)_
- **AFC** [#66](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/66): Automate Mac watch and Hetzner ST/UM health recover _(by jaywedgeworth22)_
- **AFC** [#67](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/67): fix(ops): do not bounce ST when a nested health dependency is down _(by jaywedgeworth22)_
- **AFC** [#68](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/68): docs(handoff): pick-up note for all 10 open Mac sessions _(by jaywedgeworth22)_
- **AFC** `Claude` [#69](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/69): docs(effort-log): — completed row for the open-sessions handoff note _(by jaywedgeworth22)_
- **AFC** [#70](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/70): feat(fleet-skills): land the sentence-gap skill and its cross-references _(by jaywedgeworth22)_
- **AFC** `Claude` [#71](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/71): docs: correct this session's seat attribution to _(by jaywedgeworth22)_
- **AFC** [#72](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/72): fix(ops): do not Coolify-restart ST after a successful docker bounce _(by jaywedgeworth22)_
- **AFC** [#73](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/73): docs(mac): record that vision-worker's worker.py is a hand-copied deploy _(by jaywedgeworth22)_
- **AFC** `Grok` [#74](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/74): fix(mac): stop — restart-storm when TUI holds the socket _(by jaywedgeworth22)_
- **AFC** [#76](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/76): Stop serving Mac secrets over HTTP and bind agy-acp to loopback _(by jaywedgeworth22)_
- **AFC** [#77](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/77): docs: autonomous iOS Debug console vs TestFlight _(by jaywedgeworth22)_
- **AFC** [#78](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/78): fix(security): sanitize host IPs, UUIDs, and untrack live env files _(by jaywedgeworth22)_
- **AFC** [#79](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/79): docs(sync): mark KIMI as retired/unavailable long-term _(by jaywedgeworth22)_

### Issues closed

- **AR** [#18](https://github.com/jaywedgeworth22/Autorotate/issues/18): Fleet onboarding — join ai-fleet-coordinator as app TopSpin (TS)
- **AR** [#19](https://github.com/jaywedgeworth22/Autorotate/issues/19): Xcode 26 first build of both app schemes (TopSpinCore is compiler-verified
- **AR** [#20](https://github.com/jaywedgeworth22/Autorotate/issues/20): Owner dashboard items: branch protection on main (require PR + checks web
- **AR** [#22](https://github.com/jaywedgeworth22/Autorotate/issues/22): Fleet onboarding — join ai-fleet-coordinator as app TopSpin (TS). KIMI
- **AR** [#43](https://github.com/jaywedgeworth22/Autorotate/issues/43): iOS first-launch update prompt (fleet) — · COMPLETED/MERGED #36 squash
- **AR** [#44](https://github.com/jaywedgeworth22/Autorotate/issues/44): Merge — App Builder PWA with this monorepo — · merged as
- **AR** [#45](https://github.com/jaywedgeworth22/Autorotate/issues/45): Apache-2.0 + Kimi dump backup + catalog fold-in — · PR
- **CT** [#1462](https://github.com/jaywedgeworth22/Congress.Trade/issues/1462): Cross-app: vendored congress-trading-shared is v2.0.0; shared repo is at v2.5.1 — audit drift
- **CT** [#1523](https://github.com/jaywedgeworth22/Congress.Trade/issues/1523): Latency comparison undercounts cross-source matches — methodology redesign (owner request 2026-08-08)
- **CT** [#1575](https://github.com/jaywedgeworth22/Congress.Trade/issues/1575): scanned_pdf corpus needs vision/OCR extraction — deliberately out of scope for the deterministic autonomy fix
- **CT** [#2039](https://github.com/jaywedgeworth22/Congress.Trade/issues/2039): ENGINEERINGQUALITY-01: Wire real Sentry for Deno production
- **DD** [#112](https://github.com/jaywedgeworth22/DealDex/issues/112): Transparent DD favicon + ST-grid iOS AppIcon
- **DD** [#116](https://github.com/jaywedgeworth22/DealDex/issues/116): 2026-08-21 — COMPLETED/MERGED #113 / #112 — Transparent DD favicon +
- **DD** [#117](https://github.com/jaywedgeworth22/DealDex/issues/117): Scan layout, OG wordmark size, and new subtitle
- **DD** [#121](https://github.com/jaywedgeworth22/DealDex/issues/121): 2026-08-21 — DEPLOYED — #118 / #117 scan layout + subtitle
- **DD** [#125](https://github.com/jaywedgeworth22/DealDex/issues/125): 2026-08-20 — COMPLETED — PR babysit rebase #85 + #93. Lane
- **DD** [#126](https://github.com/jaywedgeworth22/DealDex/issues/126): 2026-08-21 — COMPLETED — Multi-platform power enhancements (Web
- **DD** [#127](https://github.com/jaywedgeworth22/DealDex/issues/127): 2026-08-21 — iOS first-launch update prompt (fleet) — COMPLETED/MERGED
- **ST** [#2550](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2550): P1 coordination: congress.trade + usage-monitor lanes degraded from prod's view (11s CT response, 6.9s UM latency, SSE flaps) — widen backoff, verify consumers tolerate it

### Issues opened

- **AR** [#18](https://github.com/jaywedgeworth22/Autorotate/issues/18): Fleet onboarding — join ai-fleet-coordinator as app TopSpin (TS)
- **AR** [#19](https://github.com/jaywedgeworth22/Autorotate/issues/19): Xcode 26 first build of both app schemes (TopSpinCore is compiler-verified
- **AR** [#20](https://github.com/jaywedgeworth22/Autorotate/issues/20): Owner dashboard items: branch protection on main (require PR + checks web
- **AR** [#22](https://github.com/jaywedgeworth22/Autorotate/issues/22): Fleet onboarding — join ai-fleet-coordinator as app TopSpin (TS). KIMI
- **AR** [#23](https://github.com/jaywedgeworth22/Autorotate/issues/23): Dependabot triage after #16 — · actions + radix PRs #1–15 still open;
- **AR** [#24](https://github.com/jaywedgeworth22/Autorotate/issues/24): Owner dashboard items: branch protection on main (require PR + checks web
- **AR** [#37](https://github.com/jaywedgeworth22/Autorotate/issues/37): iOS first-launch update prompt (fleet) — · branch
- **AR** [#39](https://github.com/jaywedgeworth22/Autorotate/issues/39): Merge — App Builder PWA with this monorepo — · branch
- **AR** [#43](https://github.com/jaywedgeworth22/Autorotate/issues/43): iOS first-launch update prompt (fleet) — · COMPLETED/MERGED #36 squash
- **AR** [#44](https://github.com/jaywedgeworth22/Autorotate/issues/44): Merge — App Builder PWA with this monorepo — · merged as
- **AR** [#45](https://github.com/jaywedgeworth22/Autorotate/issues/45): Apache-2.0 + Kimi dump backup + catalog fold-in — · PR
- **AR** [#46](https://github.com/jaywedgeworth22/Autorotate/issues/46): Dependabot leftover radix/react PRs — · after #16. Remaining npm PRs
- **CT** [#2127](https://github.com/jaywedgeworth22/Congress.Trade/issues/2127): 2026-08-17 — IN PROGRESS — #1460 expansion leftovers + #1429 product
- **CT** [#2128](https://github.com/jaywedgeworth22/Congress.Trade/issues/2128): 2026-08-17 — IN PR #1965 — #1460 expansion leftovers + #1429 Delivery
- **CT** [#2129](https://github.com/jaywedgeworth22/Congress.Trade/issues/2129): 2026-08-17 — IN PROGRESS — UX polish: deep-link ids, quiet anonymous
- **CT** [#2130](https://github.com/jaywedgeworth22/Congress.Trade/issues/2130): 2026-08-17 — IN PR #1967 — UX polish: deep-link ids, quiet anonymous
- **CT** [#2131](https://github.com/jaywedgeworth22/Congress.Trade/issues/2131): 2026-08-17 — IN PROGRESS — #1523 latency corpus match + #1462
- **CT** [#2132](https://github.com/jaywedgeworth22/Congress.Trade/issues/2132): 2026-08-17 — IN PR #1966 — #1523 latency corpus match + #1462
- **CT** [#2135](https://github.com/jaywedgeworth22/Congress.Trade/issues/2135): 2026-08-17 — IN PR #1973 — Read-only web/iOS parity + UX audit (branch
- **CT** [#2136](https://github.com/jaywedgeworth22/Congress.Trade/issues/2136): 2026-08-17 — IN PR #1976 — Read-only ingestion integrity audit (branch
- **CT** [#2137](https://github.com/jaywedgeworth22/Congress.Trade/issues/2137): 2026-08-17 4:15pm CT — IN PROGRESS — #1575 scannedpdf vision/OCR path
- **CT** [#2138](https://github.com/jaywedgeworth22/Congress.Trade/issues/2138): 2026-08-21 — iOS first-launch update prompt (fleet) — IN PROGRESS
- **CT** [#2139](https://github.com/jaywedgeworth22/Congress.Trade/issues/2139): 2026-08-21 — iOS first-launch update prompt (fleet) — IN PR #2133
- **CT** [#2166](https://github.com/jaywedgeworth22/Congress.Trade/issues/2166): 2026-08-21 — KIMI — PLANNED — [P0] Verify the 34-secret history scrub +
- **CT** [#2167](https://github.com/jaywedgeworth22/Congress.Trade/issues/2167): 2026-08-21 — KIMI — PLANNED — [P1] Add same-repo fork guard to
- **CT** [#2168](https://github.com/jaywedgeworth22/Congress.Trade/issues/2168): 2026-08-21 — KIMI — PLANNED — [P1] Rollback path + auto-migrations + drop 131MB
- **DD** [#114](https://github.com/jaywedgeworth22/DealDex/issues/114): 2026-08-20 — IN PROGRESS #112 — Transparent DD favicon + ST-grid
- **DD** [#116](https://github.com/jaywedgeworth22/DealDex/issues/116): 2026-08-21 — COMPLETED/MERGED #113 / #112 — Transparent DD favicon +
- **DD** [#117](https://github.com/jaywedgeworth22/DealDex/issues/117): Scan layout, OG wordmark size, and new subtitle
- **DD** [#119](https://github.com/jaywedgeworth22/DealDex/issues/119): 2026-08-21 — IN PROGRESS — Scan layout + OG wordmark + subtitle
- **DD** [#121](https://github.com/jaywedgeworth22/DealDex/issues/121): 2026-08-21 — DEPLOYED — #118 / #117 scan layout + subtitle
- **DD** [#123](https://github.com/jaywedgeworth22/DealDex/issues/123): 2026-08-21 — iOS first-launch update prompt (fleet) — IN PROGRESS
- **DD** [#125](https://github.com/jaywedgeworth22/DealDex/issues/125): 2026-08-20 — COMPLETED — PR babysit rebase #85 + #93. Lane
- **DD** [#126](https://github.com/jaywedgeworth22/DealDex/issues/126): 2026-08-21 — COMPLETED — Multi-platform power enhancements (Web
- **DD** [#127](https://github.com/jaywedgeworth22/DealDex/issues/127): 2026-08-21 — iOS first-launch update prompt (fleet) — COMPLETED/MERGED
- **ST** [#3016](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3016): iOS first-launch update prompt (fleet) — IN PR #3012
- **ST** [#3017](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3017): Land leftover open PRs — IN PROGRESS 2026-08-21. #3013
- **ST** [#3020](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3020): Land leftover open PRs — IN PROGRESS 2026-08-21. #2941
- **ST** [#3021](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3021): setup-node 4→7 + pin-check test — IN PROGRESS
- **ST** [#3024](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3024): Land leftover open PRs — IN PROGRESS 2026-08-21. #3008
- **ST** [#3029](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3029): Land leftover open PRs — IN PROGRESS 2026-08-21. #2990
- **ST** [#3033](https://github.com/jaywedgeworth22/Socratic.Trade/issues/3033): Land leftover open PRs — IN PROGRESS 2026-08-21
- **UM** [#1304](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1304): 2026-08-21 — IN PR #1303 — Client+Local last rows hide under the glass
- **UM** [#1306](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1306): 2026-08-21 — iOS first-launch update prompt (fleet) — IN PROGRESS
- **UM** [#1308](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1308): 2026-08-21 — IN PR #1307 — Ledger email corrections (branch

### Effort board

- **CT** `Grok` 2026-08-21 — IN PROGRESS — Vision-worker loop overhaul (board `72852a1e`, branch `grok/vision-loop-overhaul`, worktree `~/apps/congress — loop`). 443 — chats / ~20 PDFs today (Rogers 17x189, McCaul 93x134). Isolate — p from AGENTS.md/MCP/xhigh; noRows stamps local_vision_submitted; pending excludes that stamp on classified/error too; never clear_attempts after a finis
- **CT** `Grok` 2026-08-21 — IN PROGRESS — Web filter chips in the white header, sticky on scroll (board `ee0a55b3`, branch `grok/filter-sticky-white`, worktree `~/apps/congress — sticky`). Owner screenshots: on the website pills sat on the cool-grey page too far under CONGRESS TRADE, and on scroll pinned on the header/content divider. main padding-top 0 + opaque white sticky strip; no over
- **CT** `Grok` `Gemini` 2026-08-21 — IN PROGRESS — Drain follow-up: retire overlapping primary+local_mac on the same PTR (board `d66b1f6d`, branch `grok/supersede-prior-sources`, worktree `~/apps/congress — supersede`). Khanna `H-2025-8221264` filing detail still 570 = 209 truncated confirm + 361 — chunk (190 cross-source twins). persistNormalizedPublish will deprecate other pipeline sources when loc
- **CT** `Grok` 2026-08-21 — IN PROGRESS — Drain remaining review-queue items + autonomy fixes (board `e9458ef2`, branch `grok/review-drain-probes`, worktree `~/apps/congress — drain`). Owner: empty the queue, fix stall, H/S/E probes within minutes. Confirmed Khanna `H-2025-8221264` 209 live (dropped one blank SAP line). Code: local vision ignores a sibling missing_tx_date; future_tx_date
- **CT** `Cursor` 2026-08-21 — IN PROGRESS — Auth scout.jays.services POST /fetch-ptr and /fetch-doc (board `d6453d72`, branch `cursor/senate-relay-auth`, worktree `~/apps/congress — relay-auth`). Bearer `SENATE_RELAY_SECRET` on Mac origin + CT caller. Infisical CT prod + Coolify env written. Mac origin does not require the secret until this lands (`SENATE_RELAY_REQUIRE=0`) so production Senate i
- **CT** `Grok` `Gemini` 2026-08-21 — IN PROGRESS — Khanna attached-schedule auto-publish: skip — CLI when pages>12, chunk — PDF (board `642b4524`, branch `grok/khanna-attached-pages`, worktree `~/apps/congress — pages`). Nine Ro Khanna PTRs (15–34p cover+schedules) sat in review because MAX_PAGES=12 truncated the CLI and a single — shot hit 32k tokens (`H-2025-8221264` 210 rows, no_amou
- **CT** `Grok` 2026-08-21 — IN PROGRESS — Upright-rotate sideways House PTR scans before — CLI (board `c9d9766b`, branch `grok/vision-upright-rotate`, worktree `~/apps/congress — rotate`). Portrait pdftoppm of landscape PTR grids burned the — CLI turn budget. Worker now scores 90 vs 270 CW and defaults to 270. Live pm2 copy restarted. Same-session drain: McCaul H-2024-8220320 219
- **CT** `Grok` 2026-08-21 — IN PROGRESS — Local vision auto-publish + stop re-OCR loop (board `c9d9766b`, branch `grok/queue-autopublish`, worktree `~/apps/congress — autopublish`). Worker looped Rogers `H-2025-9115689` (17) and McCaul `H-2025-8221302` (93) because pending?worker=local reclaimed needs_review after ingest returned published=false. parseAmountRange treated Fund 4 / BDS 2016 a
- **CT** `Cursor` 2026-08-21 — IN PROGRESS — Finish all open CT PRs + deploy to production (owner-directed). Live already `cd6079f` = prior main. MERGED #1973 (`10c838a0`) web/iOS parity audit. Rematched remaining drafts onto main after concurrent #2134 (`e52f2c06`). Still open: #2133 iOS update prompt, #2042 Sentry, #2040 Coolify-shape docs, #2015 discovered-stamp, #2014 party rings, #1986 extract
- **CT** `Cursor` 2026-08-21 — iOS first-launch update prompt (fleet) — COMPLETED/MERGED #2133 squash `79f25b8f` (branch `cursor/ios-update-prompt-9992`, worktree `~/apps/congress — ios-update`). On first open, ask to update when a newer version exists. TestFlight opens TestFlight; App Store opens the App Store. Manifest `jaywedgeworth22/ios-app-versions`. Prompt inlined in `App.swift` because
- **CT** `Cursor` `Gemini` 2026-08-21 — IN PR #2134 — OpenRouter Flash stays on latest; native-vision for Flash-latest + DeepSeek vision-exp (branch `cursor/deepseek-v4-flash-eval-ecb2`). Follow-up to the vision-exp eval: owner asked if — 3.7 Flash 75% off meant pinning 3.7, and whether ` -flash-latest` already is 3.7. Live OR: `~google/gemini-flash-latest` prices as 3.7 ($0.375/$1.875, Vertex disco
- **CT** `Cursor` 2026-08-21 — EVAL #2134 — DeepSeek V4 Flash Vision Exp + Atlas vs OpenRouter (branch `cursor/deepseek-v4-flash-eval-ecb2`). Owner asked whether to add `deepseek/deepseek-v4-flash-vision-exp` to the CT cascade, whether ST Green/Red should use it, and whether atlascloud.ai saves money vs OpenRouter. Live OR catalog (420): vision-exp is same-day experimental, `text`+`image` only (no `f
- **CT** `Cursor` `Claude` 2026-08-21 — COMPLETED/MERGED #2126 — Harden MockURLProtocol.handler races in CongressTradeTests (branch `cursor/harden-mock-urlprotocol-070d`). 's chamber-filter `/feed` guards in #2124 (`55572400`) were left untouched. Remaining last-request captures (`testTimeRangeAllOmitsFromParameter`, pager tests, `testSetSearchUsesMemberNameNotMember`, feed call-count sites) now require
- **CT** `Cursor` 2026-08-21 — iOS first-launch update prompt (fleet) — IN PROGRESS (branch `cursor/ios-update-prompt-9992`, worktree `~/apps/congress — ios-update`). On first open, ask to update when a newer version exists. TestFlight opens TestFlight; App Store opens the App Store. Manifest `jaywedgeworth22/ios-app-versions`. Prompt inlined in `App.swift` because pbxproj edits are hook
- **CT** `Cursor` 2026-08-21 — iOS first-launch update prompt (fleet) — IN PR #2133 (branch `cursor/ios-update-prompt-9992`, worktree `~/apps/congress — ios-update`). On first open, ask to update when a newer version exists. TestFlight opens TestFlight; App Store opens the App Store. Manifest `jaywedgeworth22/ios-app-versions`. Prompt inlined in `App.swift` because pbxproj edits are hook
- **UM** `Cursor` 2026-08-21 — IN PR #1307 — Ledger email corrections (branch `cursor/ledger-email-corrections-c163`). Live voids applied: Massive/FMP/Anthropic/Kimi August seed cash is now $0. Those four rows are `considering`. Namecheap `$1.18` ingested from Gmail order `#211025634`. iCloud still unread (no IMAP). Keepout: iOS TestFlight/update-prompt lanes
- **UM** `Cursor` 2026-08-21 — iOS first-launch update prompt (fleet) — IN PROGRESS (branch `cursor/ios-update-prompt-9992`, worktree `~/apps/usage — ios-update`). Client + Local. TestFlight opens TestFlight; App Store opens the App Store. Manifest `jaywedgeworth22/ios-app-versions`
- **UM** `Cursor` 2026-08-21 — IN PR #1303 — Client+Local last rows hide under the glass tab bar; Jay Old R2 looks degraded (branch `cursor/settings-about-footer-visible-db38`). Shell-wide 72pt scroll clearance on every Client tab and Local `TabView`. iOS now treats `r2_not_enabled` / Jay Old leftovers as neutral, not Unavailable. Keepout: RootView, DesignSystem clearance, LocalRootView, Platf
- **UM** 2026-08-21 — KIMI — PLANNED — [P1] Restore deploy gating on the Coolify path. Board item d0f5f1db. The retired Oracle pipeline (deploy-production.sh) hard-gated on signed commits + merged-PR provenance + exact-SHA green checks + validated rollback; the current Coolify/Hetzner path has no in-repo gate — production-deploy-verify.yml is explicitly observer-only ('never mutates production'
- **UM** 2026-08-21 — KIMI — PLANNED — [P2] Consolidate 3 generations of deploy/backup docs; delete retired Garage compose; per-project Infisical identities. Board item bba9984a. DEPLOY.md header says Hetzner/Coolify while invariant #4 still describes the Oracle timer as the live gate; backups span Garage+B2+R2 docs. deploy/coolify/garage.compose.yaml (GARAGE_ALLOW_WORLD_READABLE_SECRETS=true
- **DD** `Cursor` 2026-08-21 — DEPLOYED — #118 / #117 scan layout + subtitle. https://dealdex.net homepage HTML includes Identify Best-Priced Pokémon Card Listings. `og.jpg?v=subtitle-20260821` is the new 92437-byte JPEG (Vercel 200). Squash `5474ef1`
- **DD** `Cursor` 2026-08-21 — COMPLETED/MERGED #113 / #112 — Transparent DD favicon + ST-grid AppIcon. Safari PNG/ICO interlocking DD. Header `img` outline removed. iOS/Android launcher is DD on the ST tiled field (no candlesticks). PR #113 squash `493e88a`
- **DD** `Antigravity` 2026-08-21 — COMPLETED — Multi-platform power enhancements (Web, iOS, Android). Branch `ag/power-enhancements`, worktree `~/apps/dealdex- `. Grading arbitrage & net flip calculators, repack filter, native iOS & Android Card Dossier, Evaluator, and Saved Ledger parity
- **DD** `Cursor` 2026-08-21 — iOS first-launch update prompt (fleet) — COMPLETED/MERGED #122 squash `3b18d9a` (branch `cursor/ios-update-prompt-9992`, worktree `~/apps/dealdex — ios-update`). TestFlight opens TestFlight; App Store opens the App Store. Manifest `jaywedgeworth22/ios-app-versions`. Verify + Vercel green
- **AR** `Cursor` iOS first-launch update prompt (fleet) — · COMPLETED/MERGED #36 squash `994cc73` 2026-08-21. On first open, ask to update when a newer version exists. TestFlight opens TestFlight; App Store opens the App Store. Manifest: `jaywedgeworth22/ios-app-versions`. Silent until an ASC/TestFlight record exists. Same prompt landing in ST / CT / UM / DealDex
- **AR** `Cursor` Fleet onboarding — join ai-fleet-coordinator as app `Autorotate` (TS). KIMI bootstrap + — closeout 2026-08-21. App PR [#16](https://github.com/jaywedgeworth22/Autorotate/pull/16) merged (`c1f12a5`). Coordinator PR [#57](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/57) already merged. Local + CI: iOS/macOS BUILD SUCCEEDED, AutorotateCore 22/22, web `npm ci` + che
- **CL** `Cursor` 2026-08-21 — COMPLETED — Local folder `~/Code/ContactLogo` + GitHub `jaywedgeworth22/ContactLogo` + — project name ContactLogo. `mv` of `/Users/jay/Code/BadgeBook` (git history, uncommitted merge, `backups/`, `vendor/crest/` intact). GitHub already renamed (0 forks, old BadgeBook slug redirects). Origin set to `https://github.com/jaywedgeworth22/ContactLogo.git`. Curso
- **CL** `Cursor` 2026-08-21 — COMPLETED — Preserve Crest+BadgeBook merge into the live app. Uncommitted kit/web/PWA/Google-import/iOS review work committed with backups. `vendor/crest/` subtree kept. Best ideas stay in ContactLogoKit + `web/`
- **CL** 2026-08-21 — KIMI — COMPLETED — [P0] PRIVACY INCIDENT: purged `.badgebook/` from git history. Board item 3b9ca6cf. Removed scan dumps, match results, review HTML, and UUID-keyed candidate PNGs from all commits via `git filter-repo` + force-push. `.gitignore` now covers `.badgebook/`, `.contactlogo/`, scan artifacts, and AddressBook exports. Issue #4 closed. Residual: GitHub may cac
- **CL** `Antigravity` 2026-08-21 — COMPLETED — Web, iOS, macOS, Android PWA enhancements & power features. Two-way Google Contacts write sync (`updateGoogleContactPhoto` with write scope), in-browser safe-ring canvas studio (`padAndSquareImage`), instant search & smart filter bar with live circle-mask toggle, iOS swipe triage & live simulator sheet (incoming call / iMessage), macOS keyboard shortcuts (
- **CL** 2026-08-21 — KIMI — PLANNED — [P1] Onboard ContactLogo to the fleet. Board item 3b9ca6cf. Still absent from fleet-apps.json and the digest. CI workflow now exists locally (see In Progress); dependabot and seat worktrees still missing. `jaywedgeworth22/crest` is archived (2026-08-21); `vendor/crest` remains a subtree path, not a second product
- **AFC** `Grok` Unstick merge+deploy across apps — IN PROGRESS 2026-08-21 (board 8b7665ce). Merged FLEET #67, CT #2089, CT #1966. ST prod 39 commits behind: RTH latch is correct; evening drain was silent-green. Drain fix in `grok/rth-drain-nudge`. UM/CTS/DD/PS had no open PRs; UM live sha matches main. Remaining ST #3008/#2941 real conflicts, #2990 gitleaks dummy key, #2993 dependabot verif
- **AFC** `Cursor` 2026-08-21 — COMPLETED/DEPLOYED — Mac share hardening. Coordinator #76 merged. CT #2152 merged and live (`build.sha` `f80afd47`). ACP loopback+WAF. Collab no secrets HTTP. Agent-sync WS gated. Slack token out of LaunchAgent. mcp.json launchers. Board 8-char prefixes. Daily findings.db snapshot. Mac `SENATE_RELAY_REQUIRE=1`: public `/fetch-ptr` 401, authed 200, `/health` 200. Pro
- **AFC** `Cursor` 2026-08-21 — COMPLETED (evaluation) — Mac share vs hosted MCP + security review. Owner asked whether a Mac-hosted MCP would beat the current HTTP/`board` share, plus a vuln/best-practice/custom-opt pass. Verdict: do not tunnel an MCP; keep HTTPS + `board` CLI. Live P0s: public `acp.jays.services` (agy-acp :8765, 426), `MAC_COLLAB_TOKEN` serves `global-api-keys` (111 names)
- **AFC** `Grok` 2026-08-21 — COMPLETED — Automate Mac + Hetzner recovery. Watch: dump-safe jlist-timeout, HTTP /health bounce, Shellular ioreg. Host: fleet-health-recover@socratic-app and @usage-monitor active; verify Pushover. Merged #66. Board `21c68868`
- **AFC** `Grok` 2026-08-21 — COMPLETED — Apple Notes HTML sentence gap (`&nbsp; `). Owner: double space after period in HTML too. Notes.app collapses ASCII doubles. Helper converts leftover `. ` to `&nbsp; `. Merged coordinator #60
- **AFC** `Grok` 2026-08-21 — COMPLETED — Apple Notes section spacing. Owner: space sections apart. Helper MD converter dropped blanks; now emits `<div><br></div>` between sections and bullets. Skills + AGENT-SYNC. Live `~/apps/apple-notes-coding.sh`. Incident note rewritten ` — html`. Merged coordinator #59
- **AFC** `Cursor` `Grok` 2026-08-21 — COMPLETED (Mac-local) — sessionStart hook + watch dump-incomplete fallback. Confirmed 14 pm2 online 02:29. Hook `~/.cursor/hooks.json` sessionStart fail-open 8s. Rule `~/.cursor/rules/mac-local-processes.mdc`. — owns the RCA row below
- **AFC** `Grok` 2026-08-21 — COMPLETED — iOS Debug-install vs TestFlight (autonomous device logs). Helper `~/apps/ios-fleet/ios-debug.sh`. Policy in AGENT-SYNC § iOS agent build loop. Merged coordinator #77. Board `cbc1edeb`
- **AFC** `Claude` 2026-08-21 — COMPLETED — Handoff note covering all 10 open, unarchived Mac sessions. Board item `311e1ab5`. Merged #68 → `docs/handoffs/2026-08-21-open-sessions-handoff.md`. Every claim re-verified against live state rather than trusting the transcripts, and the drift is recorded: pm2 at 11/14 not 14/14, `xcode-health` +116 restarts since an agent offered to clear its orphan
- **AFC** `Claude` 2026-08-21 — COMPLETED — Shellular down, `pm2 status` empty, XcodeBuildMCP timing out: root-caused as two separate problems. Board item `2dc5da58`. Shellular was NOT a duplicate install and NOT launchd — it crash-looped on `/bin/sh: ioreg: command not found` because pm2 replays the env cached at an app's FIRST start, and that cached PATH had no `/usr/sbin`, while `pm2-ecosyst

## 2026-08-20

*113 PRs merged · 99 issues opened · 59 issues closed · 29 effort rows*

### Merged PRs

- **CT** [#1978](https://github.com/jaywedgeworth22/Congress.Trade/pull/1978): Audit analytics accuracy (report-only) _(by jaywedgeworth22)_
- **CT** [#1979](https://github.com/jaywedgeworth22/Congress.Trade/pull/1979): Blind-spots audit: strategy, ethics, legal, tests, observability _(by jaywedgeworth22)_
- **CT** [#2011](https://github.com/jaywedgeworth22/Congress.Trade/pull/2011): Classify OpenRouter replies so garbage/Unauthorized skip one doc _(by jaywedgeworth22)_
- **CT** [#2036](https://github.com/jaywedgeworth22/Congress.Trade/pull/2036): IOSENGINEERING-14: iOS compile + XCTest must fail CI _(by jaywedgeworth22)_
- **CT** [#2061](https://github.com/jaywedgeworth22/Congress.Trade/pull/2061): fix: scout.jays.services GET / matches mac.jays.services _(by jaywedgeworth22)_
- **CT** [#2075](https://github.com/jaywedgeworth22/Congress.Trade/pull/2075): feat(seo): open render paths, add sitemap, real entity links, per-view titles _(by jaywedgeworth22)_
- **CT** [#2076](https://github.com/jaywedgeworth22/Congress.Trade/pull/2076): Serve the AASA manifest — web half of iOS Universal Links _(by jaywedgeworth22)_
- **CT** [#2077](https://github.com/jaywedgeworth22/Congress.Trade/pull/2077): feat(web): dismissible App Store banner, dark until IOS_APP_STORE_ID is set _(by jaywedgeworth22)_
- **CT** [#2078](https://github.com/jaywedgeworth22/Congress.Trade/pull/2078): docs: production is Coolify, not a Cloudflare Worker _(by jaywedgeworth22)_
- **CT** [#2079](https://github.com/jaywedgeworth22/Congress.Trade/pull/2079): docs: cite Coolify/Deno proof on README + DEPLOY _(by jaywedgeworth22)_
- **CT** [#2080](https://github.com/jaywedgeworth22/Congress.Trade/pull/2080): feat(latency): bracket competitor publish time with probe-run history _(by jaywedgeworth22)_
- **CT** [#2081](https://github.com/jaywedgeworth22/Congress.Trade/pull/2081): fix(web-mobile): restore centered tab labels, shrink six-tab dock, avatar hamburger _(by jaywedgeworth22)_
- **CT** [#2083](https://github.com/jaywedgeworth22/Congress.Trade/pull/2083): fix(admin): gate Admin/Review Queue on real admin status, add admin grant/revoke _(by jaywedgeworth22)_
- **CT** [#2086](https://github.com/jaywedgeworth22/Congress.Trade/pull/2086): fix(latency): repair price-snapshot pipeline (live/backfill split, +15m, no FMP) _(by jaywedgeworth22)_
- **CT** [#2087](https://github.com/jaywedgeworth22/Congress.Trade/pull/2087): fix(iap): remove forced registration from Apple purchase (Guideline 5.1.1(v)) _(by jaywedgeworth22)_
- **CT** [#2088](https://github.com/jaywedgeworth22/Congress.Trade/pull/2088): fix(iap): do not resurrect a refunded Apple subscription on redeem _(by jaywedgeworth22)_
- **CT** [#2090](https://github.com/jaywedgeworth22/Congress.Trade/pull/2090): fix(iap): keep claimed Apple owner across racing anonymous redeem _(by jaywedgeworth22)_
- **CT** [#2092](https://github.com/jaywedgeworth22/Congress.Trade/pull/2092): fix(iap): tombstone Apple REFUND/REVOKE that arrives before first redeem _(by jaywedgeworth22)_
- **CT** [#2093](https://github.com/jaywedgeworth22/Congress.Trade/pull/2093): fix(iap): grant legacy /billing/apple/confirm through the Apple ledger _(by jaywedgeworth22)_
- **CT** [#2094](https://github.com/jaywedgeworth22/Congress.Trade/pull/2094): fix(ios): iPad Air layout fixes — full-width sheets, Assets grid, Delivery width, executive titles _(by jaywedgeworth22)_
- **CT** [#2096](https://github.com/jaywedgeworth22/Congress.Trade/pull/2096): fix(iap): accept Apple-signed Sandbox purchases by default _(by jaywedgeworth22)_
- **CT** [#2098](https://github.com/jaywedgeworth22/Congress.Trade/pull/2098): fix(iap): do not let a stale DID_RENEW resurrect a refunded Apple row _(by jaywedgeworth22)_
- **CT** [#2099](https://github.com/jaywedgeworth22/Congress.Trade/pull/2099): fix(iap): keep refunded Apple rows revoked across stale ASSN retries _(by jaywedgeworth22)_
- **CT** [#2100](https://github.com/jaywedgeworth22/Congress.Trade/pull/2100): fix(iap): do not let DID_CHANGE_RENEWAL_STATUS brick a paid resubscribe _(by jaywedgeworth22)_
- **CT** [#2102](https://github.com/jaywedgeworth22/Congress.Trade/pull/2102): fix(extract): lift 200-tx cap and publish on type-code plurality (#2101) _(by jaywedgeworth22)_
- **CT** [#2103](https://github.com/jaywedgeworth22/Congress.Trade/pull/2103): fix(ui): Light vs Sepia palettes, Trends layout, combined disclaimer _(by jaywedgeworth22)_
- **CT** [#2104](https://github.com/jaywedgeworth22/Congress.Trade/pull/2104): fix(extract): do not publish truncated review payloads from drain _(by jaywedgeworth22)_
- **CT** [#2107](https://github.com/jaywedgeworth22/Congress.Trade/pull/2107): fix(extract): reclaim review queue autonomously — worker selection, scanned drain guard, ?worker=local reclaim _(by jaywedgeworth22)_
- **CT** [#2108](https://github.com/jaywedgeworth22/Congress.Trade/pull/2108): fix(extract): do not let local vision shrink a stored review extract _(by jaywedgeworth22)_
- **CT** [#2109](https://github.com/jaywedgeworth22/Congress.Trade/pull/2109): fix(extract): split glued House PTR rows so typed filings auto-publish _(by jaywedgeworth22)_
- **CT** [#2111](https://github.com/jaywedgeworth22/Congress.Trade/pull/2111): fix(extract): do not inherit House PTR owner onto later blank rows _(by jaywedgeworth22)_
- **CT** [#2114](https://github.com/jaywedgeworth22/Congress.Trade/pull/2114): fix(extract): do not skip truncated OpenRouter JSON as garbage _(by jaywedgeworth22)_
- **CT** [#2116](https://github.com/jaywedgeworth22/Congress.Trade/pull/2116): docs: CHECKLIST_FOR_ASC_PUBLIC_RELEASE — what agents do, what the owner does _(by jaywedgeworth22)_
- **CL** [#1](https://github.com/jaywedgeworth22/ContactLogo/pull/1): one product from Crest + BadgeBook _(by jaywedgeworth22)_
- **CL** [#2](https://github.com/jaywedgeworth22/ContactLogo/pull/2): GitHub About, homepage, and visitor docs _(by jaywedgeworth22)_
- **DD** [#85](https://github.com/jaywedgeworth22/DealDex/pull/85): ci(ios): add TestFlight ship workflow for native/ios _(by jaywedgeworth22)_
- **DD** [#93](https://github.com/jaywedgeworth22/DealDex/pull/93): docs: effort-log pointer for ST audit #2802 follow-ups _(by jaywedgeworth22)_
- **DD** [#96](https://github.com/jaywedgeworth22/DealDex/pull/96): docs: match README and About to how DealDex ships _(by jaywedgeworth22)_
- **DD** [#101](https://github.com/jaywedgeworth22/DealDex/pull/101): effort-log: fleet setup-audit findings (KIMI, 2026-08-21) _(by jaywedgeworth22)_
- **DD** [#103](https://github.com/jaywedgeworth22/DealDex/pull/103): feat(ios): official chips, 3D title, unsigned scan, Google OAuth _(by jaywedgeworth22)_
- **DD** [#105](https://github.com/jaywedgeworth22/DealDex/pull/105): docs: close iOS desk + 3D title on the effort board _(by jaywedgeworth22)_
- **PS** [#9](https://github.com/jaywedgeworth22/Personal-Site/pull/9): docs: refresh public work list hosting copy _(by jaywedgeworth22)_
- **ST** [#2785](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2785): feat(brand): crop offset candlestick ST website favicon _(by jaywedgeworth22)_
- **ST** [#2792](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2792): Keep FilingAPI; skip missing/401 keys (#2778) _(by jaywedgeworth22)_
- **ST** [#2793](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2793): feat(ui): console/admin entry for curl-only diagnostics (#2563) _(by jaywedgeworth22)_
- **ST** [#2794](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2794): fix(ios): #2560 release-readiness leftovers — privacy manifest + console handoffs _(by jaywedgeworth22)_
- **ST** [#2795](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2795): fix(a11y): console chip AA, stacked Escape, tooltip/columns/meter _(by jaywedgeworth22)_
- **ST** [#2803](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2803): RAG audit P0 follow-ups: parsed-text SEC, chat asOf, production eval path _(by jaywedgeworth22)_
- **ST** [#2804](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2804): docs: web / mobile-web / iOS parity audit (2026-08-17) _(by jaywedgeworth22)_
- **ST** [#2805](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2805): docs(audit): brokers + data-cascade reliability report (2026-08-17) _(by jaywedgeworth22)_
- **ST** [#2806](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2806): docs: 2026-08-17 security and reliability audit (report-only) _(by jaywedgeworth22)_
- **ST** [#2807](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2807): docs(audit): 2026-08-17 architecture and backend report _(by jaywedgeworth22)_
- **ST** [#2808](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2808): docs(audit): trading-outcomes validation review (2026-08-17) _(by jaywedgeworth22)_
- **ST** [#2816](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2816): fix(ops): page health JSON flags, require OPS token, cap R2 retain at 1 _(by jaywedgeworth22)_
- **ST** [#2817](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2817): Latch Coolify RTH unless HOTFIX=1; record live watch_paths (do not re-apply) _(by jaywedgeworth22)_
- **ST** [#2828](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2828): fix(console): shrink Safari tab-bar chrome gap and paint it white _(by jaywedgeworth22)_
- **ST** [#2841](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2841): Notification history on website and iOS _(by jaywedgeworth22)_
- **ST** [#2842](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2842): fix(tax): wire existing IRA Ignore/Block and min-loss _(by jaywedgeworth22)_
- **ST** [#2854](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2854): fix(gather): no Pinecone inventory + 502/429 fail-open during Manual Run once _(by jaywedgeworth22)_
- **ST** [#2860](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2860): fix(ci): do not skip verify for build-imported docs/benchmarks _(by jaywedgeworth22)_
- **ST** [#2861](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2861): fix(green): make Bull strict schema valid (required ⊇ properties) _(by jaywedgeworth22)_
- **ST** [#2862](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2862): fix(approve): report placement outcome, not command resolve _(by jaywedgeworth22)_
- **ST** [#2863](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2863): fix(ios): clear session snapshot, show edit errors, decode nested stop-loss _(by jaywedgeworth22)_
- **ST** [#2873](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2873): fix(mobile): chrome budget and 44px touch targets _(by jaywedgeworth22)_
- **ST** [#2878](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2878): fix(pnl): stop zeroing Day P&L and minting phantom short deposits _(by jaywedgeworth22)_
- **ST** [#2883](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2883): fix(auth): fail closed when AUTH_SECRET is missing in live _(by jaywedgeworth22)_
- **ST** [#2884](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2884): fix(console): keep server DB out of the client bundle _(by jaywedgeworth22)_
- **ST** [#2885](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2885): fix(fts): indexed mirror idempotency and yield during strategy runs _(by jaywedgeworth22)_
- **ST** [#2886](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2886): fix(broker): deadlines on quotes/place/cancel and scoped order history _(by jaywedgeworth22)_
- **ST** [#2944](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2944): test(contract): pin GET /api/policy to the Swift FullPolicy decoder _(by jaywedgeworth22)_
- **ST** [#2945](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2945): docs: fix stale Coolify / PWA / preview hosting copy _(by jaywedgeworth22)_
- **ST** [#2946](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2946): fix(prompt): put the trust boundary at the sink, contain untrusted directives _(by jaywedgeworth22)_
- **ST** [#2947](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2947): fix(broker): keep Tradier order paging past 5 pages _(by jaywedgeworth22)_
- **ST** [#2949](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2949): fix(orders): tombstone owner-cancelled stops when lookup misses _(by jaywedgeworth22)_
- **ST** [#2950](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2950): fix(perf): make every performance number state its basis and window _(by jaywedgeworth22)_
- **ST** [#2951](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2951): fix(fts): do not delete a reused FTS rowid from a stale index _(by jaywedgeworth22)_
- **ST** [#2952](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2952): fix(broker): keep Tradier live pending_cancel stops in default order list _(by jaywedgeworth22)_
- **ST** [#2953](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2953): feat(market): serve CT real-time quotes and intraday bars without FMP _(by jaywedgeworth22)_
- **ST** [#2954](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2954): test(ios): make the Swift test target compile and fix three stale assertions _(by jaywedgeworth22)_
- **ST** [#2955](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2955): fix(pnl): read the whole fill ledger and grade the whole round trip _(by jaywedgeworth22)_
- **ST** [#2956](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2956): docs(ops): record that the B2 restore is proven, unblocking the historic R2 prune _(by jaywedgeworth22)_
- **ST** [#2957](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2957): fix(auth): let peer token reach #2953 quotes/intraday routes _(by jaywedgeworth22)_
- **ST** [#2959](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2959): fix(market): return 502 when #2953 intraday providers fail _(by jaywedgeworth22)_
- **ST** [#2960](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2960): fix(broker): do not retry Alpaca createOrder after a dropped socket _(by jaywedgeworth22)_
- **ST** [#2962](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2962): fix(orders): tombstone owner-cancelled stops when cancel times out _(by jaywedgeworth22)_
- **ST** [#2963](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2963): fix(broker): include terminal orders on Alpaca MCP list _(by jaywedgeworth22)_
- **ST** [#2965](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2965): fix(console): commit numeric fields on blur and stop writing a fallback when cleared _(by jaywedgeworth22)_
- **ST** [#2966](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2966): fix(auth): gate the operator page tree, attribute knob writes, split the admin transcript _(by jaywedgeworth22)_
- **ST** [#2968](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2968): fix(run): do not adopt a frozen-but-live Manual Run worker _(by jaywedgeworth22)_
- **ST** [#2973](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2973): fix(broker): cancel what you time out, and stop launching duplicates on live orders _(by jaywedgeworth22)_
- **ST** [#2974](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2974): fix(ios): resolve iOS/web parity divergence by divergence, not by syncing one way _(by jaywedgeworth22)_
- **ST** [#2975](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2975): effort-log: fleet setup-audit findings (KIMI, 2026-08-21) _(by jaywedgeworth22)_
- **ST** [#2982](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2982): docs(review): DEEPSEEK full-stack review — desktop web, mobile web, iOS (zero-code) _(by jaywedgeworth22)_
- **ST** [#2983](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2983): docs(effort): DEEPSEEK review row COMPLETED/MERGED #2982 _(by jaywedgeworth22)_
- **ST** [#2984](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2984): docs(review): DEEPSEEK review track reports — backend, desktop web, iOS, mobile web _(by jaywedgeworth22)_
- **UM** `Grok` [#1233](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1233): docs(effort): board hygiene — close stale In Progress _(by jaywedgeworth22)_
- **UM** [#1234](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1234): docs: provider-connectors accuracy audit (2026-08-17) _(by jaywedgeworth22)_
- **UM** [#1237](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1237): docs: web / iOS parity audit (2026-08-17) _(by jaywedgeworth22)_
- **UM** [#1238](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1238): docs: outcomes and projections audit (2026-08-17) _(by jaywedgeworth22)_
- **UM** [#1239](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1239): docs: 2026-08-17 backend durability audit (report only) _(by jaywedgeworth22)_
- **UM** [#1240](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1240): docs: 2026-08-17 purchase-path scan (UM + DealDex) _(by jaywedgeworth22)_
- **UM** [#1242](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1242): Say Deno Deploy is retired; Coolify hosts Congress.Trade _(by jaywedgeworth22)_
- **UM** [#1247](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1247): docs: align GitHub About and current docs with Hetzner production _(by jaywedgeworth22)_
- **UM** [#1292](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1292): effort-log: fleet setup-audit findings (KIMI, 2026-08-21) _(by jaywedgeworth22)_
- **AFC** [#44](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/44): docs: STATUS pointer for ST audit #2802 follow-ups _(by jaywedgeworth22)_
- **AFC** [#45](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/45): docs: match README and About to the live fleet _(by jaywedgeworth22)_
- **AFC** [#46](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/46): effort-log: bootstrap fleet-infra board + setup-audit findings (KIMI, 2026-08-21) _(by jaywedgeworth22)_
- **AFC** `Claude` [#52](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/52): docs: — fleet-skills pack (current policy, all apps) _(by jaywedgeworth22)_
- **AFC** `Claude` [#53](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/53): docs: tighten — fleet-skills land/deploy facts _(by jaywedgeworth22)_
- **AFC** [#54](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/54): Add fleet-coordination skill (meta protocol for THE BOARD, triple claim, Slack, effort logs, Notes, consistency) _(by jaywedgeworth22)_
- **AFC** [#55](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/55): chore(seats): onboard DEEPSEEK fleet seat _(by jaywedgeworth22)_
- **AFC** [#56](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/56): docs(processes): record mac-collab orphan-port self-heal and sync overlap _(by jaywedgeworth22)_
- **AFC** [#57](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/57): feat(fleet): onboard TopSpin (TS) as fleet app _(by jaywedgeworth22)_

### Issues closed

- **CT** [#2095](https://github.com/jaywedgeworth22/Congress.Trade/issues/2095): Mac/TestFlight IAP: Apple confirmed purchase, production rejects Sandbox JWS
- **CT** [#2097](https://github.com/jaywedgeworth22/Congress.Trade/issues/2097): Light vs sepia as full theme options; Trends layout; combined disclaimer
- **CT** [#2101](https://github.com/jaywedgeworth22/Congress.Trade/issues/2101): Lift 200-tx publish cap; plurality + House type-code ticker demotion so multi-model filings auto-publish
- **CT** [#2106](https://github.com/jaywedgeworth22/Congress.Trade/issues/2106): Review-queue remaining clusters: glued PTR rows, due-date as tx date, form-chrome wipe
- **CL** [#4](https://github.com/jaywedgeworth22/ContactLogo/issues/4): [P0] Privacy incident: .badgebook/ purged from git history
- **DD** [#97](https://github.com/jaywedgeworth22/DealDex/issues/97): 2026-08-20 — COMPLETED/MERGED #94 — Apache License 2.0 at repo root
- **DD** [#98](https://github.com/jaywedgeworth22/DealDex/issues/98): 2026-08-19 — COMPLETED/MERGED #87 — Official DD AppIcon + TestFlight
- **DD** [#99](https://github.com/jaywedgeworth22/DealDex/issues/99): 2026-08-19 — COMPLETED/MERGED #86 — Official DealDex wordmark (in-app
- **DD** [#102](https://github.com/jaywedgeworth22/DealDex/issues/102): iOS desk + 3D title wordmark (Xcode 26.3, official chips, unsigned scan, Google)
- **DD** [#106](https://github.com/jaywedgeworth22/DealDex/issues/106): 2026-08-20 — COMPLETED/MERGED #103 — iOS desk + 3D title wordmark
- **PS** [#10](https://github.com/jaywedgeworth22/Personal-Site/issues/10): 2026-08-20 — COMPLETED — Public work list copy matches current apps
- **ST** [#2560](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2560): P1: iOS release-readiness batch — Close-only/Wind-down controls missing, no APNs despite alert copy promising it, ITSAppUsesNonExemptEncryption/privacy manifest absent, no web-console deep links
- **ST** [#2561](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2561): P1/P2: console accessibility batch — light-theme chip contrast fails AA, Sheet Escape closes stacked surfaces, tooltip/columns-popover/meter gaps
- **ST** [#2563](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2563): P3: curl-only server capabilities with no UI entry — tuning-dry-run, learning-ledger, backtest-ic, audit query
- **ST** [#2731](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2731): Website favicon: cropped offset candlestick ST, transparent
- **UM** [#953](https://github.com/jaywedgeworth22/Usage-Monitor/issues/953): [OWNER ACTION REQUIRED] P0 deleted-live-SQLite recovery (2026-08-01) — ACTIVE
- **UM** [#981](https://github.com/jaywedgeworth22/Usage-Monitor/issues/981): Receipt inbox Worker + Email Routing (post-R2 bucket)
- **UM** [#1241](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1241): Docs: Deno Deploy is retired; Coolify is the Congress.Trade host
- **UM** [#1251](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1251): 2026-08-17 — SHIPPED TestFlight — UM Client + Local 1.0.1 via Xcode.app
- **UM** [#1252](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1252): 2026-08-14 — DEPLOYED — Add all four Cloudflare accounts as UM
- **UM** [#1253](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1253): [2026-08-12] Local key/config propagation bundle — MERGED PR #1145
- **UM** [#1254](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1254): [2026-08-12] — quota collector finished against the real CLI
- **UM** [#1255](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1255): [2026-08-13] R2 kill-switch cleared + auto-resume made durable +
- **UM** [#1256](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1256): [2026-08-12] R2 free-tier kill-switch: it is pinned in config, not held
- **UM** [#1257](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1257): [2026-08-12] Infisical card false alarm: probe bug + one stale secret
- **UM** [#1258](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1258): [2026-08-11] iOS Swift test suite green + one real product bug — MERGED
- **UM** [#1259](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1259): [2026-08-11] Platforms tab (all-platform infra status) + iOS full web
- **UM** [#1260](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1260): 2026-08-17 — BOARD HYGIENE — verified-merged In Progress rows (first
- **UM** [#1261](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1261): 2026-08-14 — COMPLETED/MERGED #1198 — iOS More sheet opens at ~50%
- **UM** [#1262](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1262): 2026-08-14 — COMPLETED/MERGED #1180 — Backup restore-proof + honest
- **UM** [#1263](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1263): 2026-08-13 3:37pm CT — IN PROGRESS — CI and iOS ship never ran on
- **UM** [#1264](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1264): 2026-08-12 — IN PR (#1160) / OPS DONE — UM Platforms CF/R2
- **UM** [#1265](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1265): [2026-08-12] PagerDuty alert correctness: false Twilio discrepancies +
- **UM** [#1266](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1266): App Store submit Client+Local — WAITINGFORREVIEW
- **UM** [#1267](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1267): Prod revision identity — LANDING. Deleted frozen Coolify
- **UM** [#1268](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1268): GHPAT + iOS ship + land #1167 — IN PROGRESS 2026-08-13
- **UM** [#1269](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1269): Coolify B2 replica heartbeat — COMPLETED/DEPLOYED
- **UM** [#1270](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1270): ST OOM + Coolify/ST ops visibility — COMPLETED/DEPLOYED
- **UM** [#1271](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1271): Default light theme — COMPLETED/DEPLOYED 2026-08-11 PR
- **UM** [#1272](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1272): OpenRouter credit probe + UptimeRobot
- **UM** [#1273](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1273): Mobile nav brand always visible — COMPLETED/DEPLOYED 2026-08-09 PR #1063
- **UM** [#1274](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1274): Hetzner deploy observer + Coolify SOURCECOMMIT — COMPLETED/DEPLOYED
- **UM** [#1275](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1275): [2026-08-07] Local catalog connect wave 2 — COMPLETED PR #1049
- **UM** [#1276](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1276): [2026-08-07] Litestream primary → Backblaze B2 — COMPLETED/DEPLOYED
- **UM** [#1277](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1277): [2026-08-07] Local iOS ↔ web parity wave 1 — COMPLETED PR #1047
- **UM** [#1278](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1278): [2026-08-07] Backblaze B2 provider web + iOS Local — COMPLETED PR #1033
- **UM** [#1279](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1279): [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger
- **UM** [#1280](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1280): Rename compose project oracle → usage-monitor — COMPLETED PR #1018
- **UM** [#1281](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1281): iOS app icons clean orange + Local LOCAL stripe — COMPLETED PR #1009
- **UM** [#1282](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1282): R2 fleet ST/CT pushover-parity + iOS inline titles — COMPLETED PR #984
- **UM** [#1283](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1283): Fix auto-deploy race mid-build — COMPLETED PR #1001 (61def229). Issue
- **UM** [#1284](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1284): Install replica-status probe + R2 kill reason — COMPLETED PR #989
- **UM** [#1285](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1285): Issue/effort hygiene + replica age 3h — COMPLETED PR #976
- **UM** [#1286](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1286): Overview money UX — COMPLETED PR #949 (146c9ca05b7b). Issue #980 closed
- **UM** [#1287](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1287): iOS Client Monitor backup layers + host usage — DEPLOYED
- **UM** [#1295](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1295): [Uptime] Usage Monitor production is stale vs main
- **UM** [#1296](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1296): 2026-08-17 — IN PROGRESS — Read-only provider-connectors accuracy audit
- **UM** [#1298](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1298): 2026-08-17 — IN PR — Read-only web/iOS parity audit (branch
- **CTS** [#280](https://github.com/jaywedgeworth22/congress-trading-shared/issues/280): Retire leftover Deno Deploy current-shape in

### Issues opened

- **CT** [#2084](https://github.com/jaywedgeworth22/Congress.Trade/issues/2084): 2026-08-17 — IN PR — Read-only blind-spots audit (branch
- **CT** [#2085](https://github.com/jaywedgeworth22/Congress.Trade/issues/2085): 2026-08-17 — IN PR #1979 — Read-only blind-spots audit (branch
- **CT** [#2095](https://github.com/jaywedgeworth22/Congress.Trade/issues/2095): Mac/TestFlight IAP: Apple confirmed purchase, production rejects Sandbox JWS
- **CT** [#2097](https://github.com/jaywedgeworth22/Congress.Trade/issues/2097): Light vs sepia as full theme options; Trends layout; combined disclaimer
- **CT** [#2101](https://github.com/jaywedgeworth22/Congress.Trade/issues/2101): Lift 200-tx publish cap; plurality + House type-code ticker demotion so multi-model filings auto-publish
- **CT** [#2106](https://github.com/jaywedgeworth22/Congress.Trade/issues/2106): Review-queue remaining clusters: glued PTR rows, due-date as tx date, form-chrome wipe
- **CT** [#2115](https://github.com/jaywedgeworth22/Congress.Trade/issues/2115): 2026-08-19 — IN PROGRESS — OpenRouter reply-routing: no halt latch on
- **CL** [#4](https://github.com/jaywedgeworth22/ContactLogo/issues/4): [P0] Privacy incident: .badgebook/ purged from git history
- **DD** [#97](https://github.com/jaywedgeworth22/DealDex/issues/97): 2026-08-20 — COMPLETED/MERGED #94 — Apache License 2.0 at repo root
- **DD** [#98](https://github.com/jaywedgeworth22/DealDex/issues/98): 2026-08-19 — COMPLETED/MERGED #87 — Official DD AppIcon + TestFlight
- **DD** [#99](https://github.com/jaywedgeworth22/DealDex/issues/99): 2026-08-19 — COMPLETED/MERGED #86 — Official DealDex wordmark (in-app
- **DD** [#100](https://github.com/jaywedgeworth22/DealDex/issues/100): 2026-08-20 — IN PR #96 — Shipping docs + GitHub About. Branch
- **DD** [#102](https://github.com/jaywedgeworth22/DealDex/issues/102): iOS desk + 3D title wordmark (Xcode 26.3, official chips, unsigned scan, Google)
- **DD** [#104](https://github.com/jaywedgeworth22/DealDex/issues/104): 2026-08-20 — IN PROGRESS — iOS desk + 3D title wordmark. Lane
- **DD** [#106](https://github.com/jaywedgeworth22/DealDex/issues/106): 2026-08-20 — COMPLETED/MERGED #103 — iOS desk + 3D title wordmark
- **DD** [#107](https://github.com/jaywedgeworth22/DealDex/issues/107): 2026-08-21 — KIMI — PLANNED — [P1] Refresh stale package-lock.json, return CI
- **DD** [#108](https://github.com/jaywedgeworth22/DealDex/issues/108): 2026-08-21 — KIMI — PLANNED — [P2] Mobile CI + move DB migrations out of the
- **DD** [#109](https://github.com/jaywedgeworth22/DealDex/issues/109): 2026-08-20 — POINTER — Cross-app coordination follow-ups (audit
- **DD** [#110](https://github.com/jaywedgeworth22/DealDex/issues/110): 2026-08-20 — rebase #85 onto main. Docs-union of STATUS/PLAN/effort log
- **DD** [#111](https://github.com/jaywedgeworth22/DealDex/issues/111): 2026-08-19 — IN PR #85 — iOS TestFlight ship workflow. Branch
- **DD** [#112](https://github.com/jaywedgeworth22/DealDex/issues/112): Transparent DD favicon + ST-grid iOS AppIcon
- **PS** [#10](https://github.com/jaywedgeworth22/Personal-Site/issues/10): 2026-08-20 — COMPLETED — Public work list copy matches current apps
- **ST** [#2958](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2958): Admin > Operations knobs PATCH on every keystroke and write each knob's default on an emptied field
- **ST** [#2961](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2961): Strategy runs can hang forever: RAG retrieval on the run path has no deadline and the embedding fetch passes signal: undefined
- **ST** [#2964](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2964): Migrations 2 and 14 use PRAGMA table_info as an existence check, which returns empty (not an error) for a missing table
- **ST** [#2967](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2967): P0: multi-second to 60s event-loop freezes during market hours, and nothing alerts when runs stop completing
- **ST** [#2970](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2970): Abandoned Alpaca reads still leak sockets: the SDK's axios instance is unreachable from our interceptors
- **ST** [#2972](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2972): FilingAPI optional key, degrade gracefully — IN
- **ST** [#2976](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2976): 2026-08-21 — KIMI — PLANNED — [P0] Human/CODEOWNERS review gate for
- **ST** [#2977](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2977): 2026-08-21 — KIMI — PLANNED — [P1] — hardening + remove committed
- **ST** [#2978](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2978): 2026-08-21 — KIMI — PLANNED — [P2] Fail-closed broker-token encryption
- **ST** [#2979](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2979): Console a11y batch — IN PROGRESS 2026-08-17 (branch
- **ST** [#2980](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2980): Console a11y batch — IN PR #2795 2026-08-17 (branch
- **ST** [#2981](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2981): 2026-08-15 — IN PR #2785 2026-08-17 — Website favicon: cropped offset
- **ST** [#2985](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2985): P3 curl-only diagnostics UI entry — IN PROGRESS
- **ST** [#2986](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2986): P3 curl-only diagnostics UI entry — IN PR #2793
- **ST** [#2988](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2988): iOS release-readiness leftovers (#2560) — IN PROGRESS
- **ST** [#2989](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2989): iOS release-readiness leftovers (#2560) — IN PR #2794
- **UM** [#1248](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1248): 2026-08-20 — IN PR #1247 — GitHub About + production docs (branch
- **UM** [#1249](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1249): 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control
- **UM** [#1250](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1250): 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control
- **UM** [#1251](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1251): 2026-08-17 — SHIPPED TestFlight — UM Client + Local 1.0.1 via Xcode.app
- **UM** [#1252](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1252): 2026-08-14 — DEPLOYED — Add all four Cloudflare accounts as UM
- **UM** [#1253](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1253): [2026-08-12] Local key/config propagation bundle — MERGED PR #1145
- **UM** [#1254](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1254): [2026-08-12] — quota collector finished against the real CLI
- **UM** [#1255](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1255): [2026-08-13] R2 kill-switch cleared + auto-resume made durable +
- **UM** [#1256](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1256): [2026-08-12] R2 free-tier kill-switch: it is pinned in config, not held
- **UM** [#1257](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1257): [2026-08-12] Infisical card false alarm: probe bug + one stale secret
- **UM** [#1258](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1258): [2026-08-11] iOS Swift test suite green + one real product bug — MERGED
- **UM** [#1259](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1259): [2026-08-11] Platforms tab (all-platform infra status) + iOS full web
- **UM** [#1260](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1260): 2026-08-17 — BOARD HYGIENE — verified-merged In Progress rows (first
- **UM** [#1261](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1261): 2026-08-14 — COMPLETED/MERGED #1198 — iOS More sheet opens at ~50%
- **UM** [#1262](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1262): 2026-08-14 — COMPLETED/MERGED #1180 — Backup restore-proof + honest
- **UM** [#1263](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1263): 2026-08-13 3:37pm CT — IN PROGRESS — CI and iOS ship never ran on
- **UM** [#1264](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1264): 2026-08-12 — IN PR (#1160) / OPS DONE — UM Platforms CF/R2
- **UM** [#1265](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1265): [2026-08-12] PagerDuty alert correctness: false Twilio discrepancies +
- **UM** [#1266](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1266): App Store submit Client+Local — WAITINGFORREVIEW
- **UM** [#1267](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1267): Prod revision identity — LANDING. Deleted frozen Coolify
- **UM** [#1268](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1268): GHPAT + iOS ship + land #1167 — IN PROGRESS 2026-08-13
- **UM** [#1269](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1269): Coolify B2 replica heartbeat — COMPLETED/DEPLOYED
- **UM** [#1270](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1270): ST OOM + Coolify/ST ops visibility — COMPLETED/DEPLOYED
- **UM** [#1271](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1271): Default light theme — COMPLETED/DEPLOYED 2026-08-11 PR
- **UM** [#1272](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1272): OpenRouter credit probe + UptimeRobot
- **UM** [#1273](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1273): Mobile nav brand always visible — COMPLETED/DEPLOYED 2026-08-09 PR #1063
- **UM** [#1274](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1274): Hetzner deploy observer + Coolify SOURCECOMMIT — COMPLETED/DEPLOYED
- **UM** [#1275](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1275): [2026-08-07] Local catalog connect wave 2 — COMPLETED PR #1049
- **UM** [#1276](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1276): [2026-08-07] Litestream primary → Backblaze B2 — COMPLETED/DEPLOYED
- **UM** [#1277](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1277): [2026-08-07] Local iOS ↔ web parity wave 1 — COMPLETED PR #1047
- **UM** [#1278](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1278): [2026-08-07] Backblaze B2 provider web + iOS Local — COMPLETED PR #1033
- **UM** [#1279](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1279): [2026-08-06] R2 subject Pushover identity + sent-from + fleet stagger
- **UM** [#1280](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1280): Rename compose project oracle → usage-monitor — COMPLETED PR #1018
- **UM** [#1281](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1281): iOS app icons clean orange + Local LOCAL stripe — COMPLETED PR #1009
- **UM** [#1282](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1282): R2 fleet ST/CT pushover-parity + iOS inline titles — COMPLETED PR #984
- **UM** [#1283](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1283): Fix auto-deploy race mid-build — COMPLETED PR #1001 (61def229). Issue
- **UM** [#1284](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1284): Install replica-status probe + R2 kill reason — COMPLETED PR #989
- **UM** [#1285](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1285): Issue/effort hygiene + replica age 3h — COMPLETED PR #976
- **UM** [#1286](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1286): Overview money UX — COMPLETED PR #949 (146c9ca05b7b). Issue #980 closed
- **UM** [#1287](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1287): iOS Client Monitor backup layers + host usage — DEPLOYED
- **UM** [#1288](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1288): [OWNER] ~/.secrets/umkeys-pass (chmod 600) before a real AirDrop
- **UM** [#1289](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1289): 2026-08-20 — IN PROGRESS — Deno Deploy copy says retired; Coolify is
- **UM** [#1290](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1290): 2026-08-20 — IN PR #1242 — Deno Deploy copy says retired; Coolify is
- **UM** [#1291](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1291): 2026-08-17 — IN PR — Outcomes/projections audit (branch
- **UM** [#1293](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1293): 2026-08-21 — KIMI — PLANNED — [P1] Restore deploy gating on the Coolify path
- **UM** [#1294](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1294): 2026-08-21 — KIMI — PLANNED — [P2] Consolidate 3 generations of deploy/backup
- **UM** [#1295](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1295): [Uptime] Usage Monitor production is stale vs main
- **UM** [#1296](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1296): 2026-08-17 — IN PROGRESS — Read-only provider-connectors accuracy audit
- **UM** [#1297](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1297): 2026-08-17 — IN PR #1234 — Read-only provider-connectors accuracy audit
- **UM** [#1298](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1298): 2026-08-17 — IN PR — Read-only web/iOS parity audit (branch
- **UM** [#1299](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1299): 2026-08-17 — COMPLETED/MERGED #1234 ed996adf — Read-only
- **UM** [#1300](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1300): 2026-08-17 — IN PR #1239 — Read-only backend durability audit (branch
- **UM** [#1301](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1301): 2026-08-17 — COMPLETED/MERGED #1237 dc109fdc — Read-only
- **UM** [#1302](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1302): 2026-08-17 — COMPLETED/MERGED #1234 — Read-only provider-connectors
- **AFC** [#47](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/47): [P0] MAC_COLLAB_TOKEN is root-of-everything — replace with per-seat scoped tokens
- **AFC** [#48](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/48): [P0] Board server + findings.db (3,703 rows) are unversioned, Mac-only, no automated backup
- **AFC** [#49](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/49): [P1] Coordination hub flapped 502 during audit and is neither watched nor monitored
- **AFC** [#50](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/50): [P1] 'Mac runners PERMANENTLY BANNED' policy contradicted by 3 always-on Mac runners the watchdog bootstraps
- **AFC** [#51](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/51): [P1] Triple-claim not atomic; mirrored statuses overwritten; deploys de-conflicted by a ~10-min Slack window
- **CTS** [#279](https://github.com/jaywedgeworth22/congress-trading-shared/issues/279): Cross-app coordination follow-ups
- **CTS** [#280](https://github.com/jaywedgeworth22/congress-trading-shared/issues/280): Retire leftover Deno Deploy current-shape in

### Effort board

- **CT** `Cursor` 2026-08-20 — IN PR #2042 — ENGINEERINGQUALITY-01 real Sentry for Deno-in-Docker / Coolify (issue #2039, branch `cursor/deno-sentry-f7d6`). `#sentry` binds `@sentry/deno` (runtime SDK, not Deno Deploy). No deployctl / Deploy APIs. Boot inits from Infisical/Coolify `SENTRY_DSN`; missing DSN or `init` throw is fail-soft. Release = Coolify `CT_BUILD_SHA` / `SOURCE_COMMIT` via `readBui
- **CT** `Cursor` 2026-08-20 — IN PR #2040 — Retire Deno Deploy / Turso as current-shape (issue #2035, branch `cursor/coolify-shape-not-deploy-ce04`). Docs + operator comments only. Live path is Coolify Deno-in-Docker on Hetzner, SQLite + Litestream, Infisical, paid cron ` `. Dated 2026-07 rollouts stay past tense. Gates: `deno check` clean; 259 files / 3191 tests. Keepouts: `app/src/deno
- **CT** `Claude` 2026-08-21 — IN PR #2122 — Delete the Sepia theme, web + iOS (branch `claude/remove-sepia-theme`). Owner ruling: Sepia was "too dark of a color that doesn't look like old fashioned paper but just looks ugly," and only Trades/Trends were ever properly themed for it — "just delete the option." No retuned palette, no flag. Light and Dark (and System) remain; Light stays the product de
- **CT** `Claude` `Codex` 2026-08-20 — IN PR #2082 — Premium activation alerts + — review round (branch `claude/premium-signup-alerts`). Pushover on first Premium activation from either billing path, once per subscription. Migration 0093 (renumbered twice by collisions with `admin_allowlist` and `apple_subscriptions_nullable_user`). EIGHT — findings resolved, several real correctness bugs not style
- **CT** `Grok` `Claude` 2026-08-20 — IN PR #2082 — Rebased Pushover premium-activation alerts onto origin/main (no merge). Was DIRTY/CONFLICTING vs `4a7951aa` (#2088 refund-resurrect + #2086 + #2087). Mechanical only: kept — notify/isNew slice; kept main `redeemAppleTransactionForUser`, refund-resurrect guard, and nullable `user_id`; effort-log UNION ( 0090-collision row kept); renumbered `premium
- **CT** `Cursor` 2026-08-20 — IN PROGRESS — Harden shared-dep auto-merge: same-repo guard, drop pull_request_target, no GH_PAT (branch `cursor/harden-shared-dep-automerge`). Kimi finding plus Jay ruling: package is public/vendored so deploy does not need a PAT. Fork PRs could skip required typecheck (skipped = satisfied). Workflows now `pull_request` + same-repo + read-only; required Linux CI runs
- **CT** `Grok` 2026-08-20 — IN PROGRESS — Review-queue remaining clusters: glued PTR rows, due-date as tx date, form-chrome wipe (#2106, board `efdb8a9f`, branch `grok/review-queue-clusters`, worktree `~/apps/congress — clusters`). 73 held House items. Seven typed `text_pdf`s park because later self-owned rows glue into the first rawText (AMZN on a PA muni). Parser splits on `[TYPE] P/S/E
- **CT** 2026-08-20 — DEEPSEEK — IN PR — Review-queue autonomy: worker selection fix, scanned reclaim via ?worker=local, deterministic-drain scanned_pdf guard, Coolify disk-full deploy rescue (branch `deepseek/review-queue-autonomy`, board CONGRESS-TRADE-EFFORT-LOG.md). Prod was 10 commits behind main — Coolify host disk 97% full killed 6 queued deploys (Postgres disk-full), Docker build cache pinned
- **CT** `Grok` 2026-08-20 — IN PR — Filings: lift 200-tx cap, plurality consensus, House type-code ticker demotion (#2101, board `22db6199`, branch `grok/filings-review-autopublish`, worktree `~/apps/congress — review`). Live queue was 114 held. Models succeeded on the same trades but GS/ST/CS leaked into ticker; vision conf capped at 0.6; 200-row gate truncated McCaul 219. Confirm-drain
- **CT** `Claude` 2026-08-20 — IN PR — Latency price snapshots: record-then-backfill, FMP removed (branch `claude/latency-snapshot-repair`). Pipeline recorded 7 prices out of 2955 (2937 `missed_window`, 11 `fmp_quote_http_402`). Two root causes: (A) rows scheduled RETROSPECTIVELY from matched candidates so `due_at` was always past and the 3-min staleness guard correctly refused — cron was fine, t
- **CT** `Grok` 2026-08-20 — IN PR #1979 — Rebased report-only blind-spots audit onto current main (docs-union only). Findings file unchanged. Effort-log unique #1979 rows kept. No product code. No merge
- **CT** `Grok` 2026-08-20 — IN PR #1978 — Rebased report-only analytics accuracy audit onto current main (docs-union only). Findings file unchanged. Effort-log unique #1978 row kept. No product code. No merge
- **CT** `Grok` 2026-08-20 — IN PR #1967 — Rebased deep-link aliases / quiet anonymous loads / primary-only feed onto current main. Kept `nav.tabs a` from main (tabs are links, not buttons). Added case-insensitive `resolveViewId` plus `directory→people`. Effort-log unique #1967 rows kept. No merge
- **CT** `Grok` 2026-08-20 — IN PR #2036 — Rebased IOSENGINEERING-14 onto current main and unblocked unsigned XCTest CI. Kept Linux jobs on `ubuntu-latest` (no oracle-ci restore). POST-body tests now read `requestBody()`; pager test matches the default 50-row page. Device compile + XCTest use isolated DerivedData. No TestFlight. No merge
- **UM** `Cursor` 2026-08-20 — IN PR #1247 — GitHub About + production docs (branch `cursor/github-about-docs-a3f2`). Docs/metadata only. Set About homepage to `https://usage.jays.services`; drop invented "30+" provider count from the public description. Align README/AGENTS/current runbooks with Hetzner NBG1 / Coolify production. Cloudflare is the TLS proxy, not the host
- **UM** `Cursor` 2026-08-20 — IN PROGRESS — Deno Deploy copy says retired; Coolify is the CT host (branch `cursor/deno-deploy-retired-docs-e16e`, issue #1241). Provider already `lifecycle: "retired"`. Adapter kept. Help notes, catalog, research, and iOS help no longer read as a live host
- **UM** `Cursor` 2026-08-20 — IN PR #1242 — Deno Deploy copy says retired; Coolify is the CT host (branch `cursor/deno-deploy-retired-docs-e16e`, issue #1241). Provider already `lifecycle: "retired"`. Adapter kept. Help notes, catalog, research, and iOS help no longer read as a live host
- **CTS** `Cursor` Cross-app coordination follow-ups (2026-08-20). Pointer only. Socratic.Trade audit #2802 follow-ups are in ST PR #2941, Congress.Trade #2064, Usage-Monitor #1245. Pins still CTS v2.5.2. Pin-check is fail-closed but not a required merge check. DealDex stays protocol-only / Vercel. Branch `cursor/cross-app-coordination-followups`
- **DD** `Grok` 2026-08-20 — COMPLETED/MERGED #103 — iOS desk + 3D title wordmark. Official olive eBay/Mercari source chips (website SVG sizes + even-odd holes). Jay's glossy DealDex title on header/login/OG/iOS/Android. Isolated DD stored; live AppIcon not swapped. Unsigned `POST /api/native/scan`, Google `dealdex://`, iOS 18 / Xcode 26.3. Production heading cache-busted `?v=3d-20260820`
- **DD** `Grok` 2026-08-20 — COMPLETED — PR babysit rebase #85 + #93. Lane `~/apps/dealdex — prfix`. Force-with-lease onto current main. #85 `59e9782` and #93 `748c7d4` are MERGEABLE/CLEAN, verify green. Did not merge. No TestFlight upload. Keep runner `[self-hosted, macOS, ARM64, xcode26]`, path `native/ios/`, app key `dealdex`
- **PS** `Cursor` `Grok` 2026-08-20 — COMPLETED — Public work list copy matches current apps. Socratic Trade uses Coolify / socratictrade.com wording from that README. Congress.Trade names congress.trade. DealDex and ContactLogo cards added. This site still deploys — to Vercel behind Cloudflare. Docs: STATUS, rollout `2026-08-20-work-list-copy`, README, this board
- **AFC** `Grok` 2026-08-21 — IN PROGRESS — Mac total service collapse RCA + restore. Last healthy 22:29 CT 2026-08-20. pm2 RPC wedge → 4/hour watch backoff → overnight crash-loops (`ERR_STREAM_DESTROYED`) → dsh session started only vision-worker → `pm2 kill` dumped that one-job list over `~/.pm2/dump.pm2` at 01:40/01:59 → crash reboot 01:58 and 02:04 (wtmp `crash`, shutdown_stall, JetsamEvent lar
- **AFC** `Grok` 2026-08-20 — IN PROGRESS — Coolify disk hygiene pager (host install + CT `grok/disk-hygiene-alert`). 14h at 93–99% with syslog-only ALERT. Wire Pushover from `/etc/congress-health-recover.env`, trim backups/scratch, 15-min timer
- **AFC** `Grok` 2026-08-20 — IN PROGRESS — Unstick and merge all open fleet PRs to production. Owner: resolve conflicts, review comments, merge to production across ST/CT/UM/CTS/DD/PS/FLEET. Inventory: ST 13 CONFLICTING; CT 8 MERGEABLE/BLOCKED + 11 CONFLICTING (9 draft); UM 4 CLEAN (1 draft); DD 1 CLEAN + 2 CONFLICTING; FLEET 2 CLEAN; CTS/PS none. Board `8b7665ce`. Worktrees per-repo ` — u
- **AFC** `Grok` `Claude` 2026-08-20 — COMPLETED — Install Desktop fleet-skills into — (`~/.grok/skills`). Owner: update — with the skills on Desktop now. Adapted — pack (12 SKILL.md) to — identity (` `, `grok/`, `~/apps/<prefix>- `) and installed user-scoped copies. ` inspect — json`: all 12 `source.type=user`. Slash `/session-start` `/board-ops` `/closeout` `/secret-handoff` `
- **AFC** `Grok` `Claude` 2026-08-20 — COMPLETED — Refresh — Desktop fleet-skills pack. Owner: update `~/Desktop/fleet-skills` for the — .app library. Jul 13 copies were ST-only and stale. Rewrote 5 skills + added session-start, board-ops, closeout, secret-handoff, apple-notes, ios-ship, owner-copy. Git copy merged ai-fleet-coordinator PR #52. Board `f78464cb`. Remaining: owner upload on
- **AFC** `Grok` 2026-08-20 — COMPLETED — mac-collab + xcode-health errored (orphans held 8792/8791). pm2 both errored `Address already in use`. 1:09am CT orphans (pids 53430/53461) held the ports; `/health` empty-reply/timeout. Killed orphans, `pm2 reset` + restart, `pm2 save`. Local + public `/health` 200 (`mac.jays.services`, `xcode.jays.services`). Board `fb192d16`
- **AFC** `Cursor` 2026-08-20 — KIMI / 2026-08-21 — COMPLETED — Onboard Autorotate as fleet app (TS). GitHub repo public (`jaywedgeworth22/Autorotate`). Coordinator PR #57 merged. App PR #16 merged (`c1f12a5`) after — fixed web `npm ci` (lockfile hosts were npmmirror + msh.team). Local iOS/macOS first builds succeeded; Effort Issues Sync run 32458648310 success; `~/Code/Autorotate` ff to mer
- **AFC** `Grok` 2026-08-20 — COMPLETED — Fleet GitHub PR inventory for production. Owner asked for every PR that should go to production. Seven scouts (ST/CT/UM/CTS/DD/PS/FLEET). Real gap is already-merged, not-live: ST 9 PRs (prod `e0a4959a` vs main `0a7ffa74`; Coolify silent freeze, do not hand-trigger) and CT 10 PRs (prod `6ebb15eb` vs main `4b9694d10714`; Coolify stuck after IAP/extract bu

## 2026-08-19

*58 PRs merged · 87 issues opened · 13 issues closed · 1 effort rows*

### Merged PRs

- **CT** [#1964](https://github.com/jaywedgeworth22/Congress.Trade/pull/1964): Keep a live backend during Coolify compose swaps (#1537) _(by jaywedgeworth22)_
- **CT** [#2022](https://github.com/jaywedgeworth22/Congress.Trade/pull/2022): docs(review): full-app expert panel review — 24 lenses, 467 verified findings _(by jaywedgeworth22)_
- **CT** [#2024](https://github.com/jaywedgeworth22/Congress.Trade/pull/2024): Poll OGE executive index every 15 minutes _(by jaywedgeworth22)_
- **CT** [#2026](https://github.com/jaywedgeworth22/Congress.Trade/pull/2026): OGE adaptive probe schedule; server-first fetch (Senate Mac-first) _(by jaywedgeworth22)_
- **CT** [#2028](https://github.com/jaywedgeworth22/Congress.Trade/pull/2028): Fix APNs fan-out filers join so push can send _(by jaywedgeworth22)_
- **CT** `Claude` [#2030](https://github.com/jaywedgeworth22/Congress.Trade/pull/2030): P0: webhook, politician 404, delivery secret, Apple refund, Filing PDF _(by jaywedgeworth22)_
- **CT** [#2037](https://github.com/jaywedgeworth22/Congress.Trade/pull/2037): Dedupe trades, stop fabricating competitor brackets, stock-only $ KPIs _(by jaywedgeworth22)_
- **CT** [#2038](https://github.com/jaywedgeworth22/Congress.Trade/pull/2038): Skip Coolify rebuilds on docs-only main merges (#2033) _(by jaywedgeworth22)_
- **CT** [#2041](https://github.com/jaywedgeworth22/Congress.Trade/pull/2041): In-app account deletion (LEGALCOMPLIANCE-01, Guideline 5.1.1(v)) _(by jaywedgeworth22)_
- **CT** [#2043](https://github.com/jaywedgeworth22/Congress.Trade/pull/2043): Mark DATACORRECTNESS #2037 completed/merged in the effort log _(by jaywedgeworth22)_
- **CT** [#2044](https://github.com/jaywedgeworth22/Congress.Trade/pull/2044): docs: strengthen two-spaces rule to cover chat replies and internal prose _(by jaywedgeworth22)_
- **CT** [#2045](https://github.com/jaywedgeworth22/Congress.Trade/pull/2045): docs: correct two-spaces guidance to use literal &nbsp; entity, not raw NBSP _(by jaywedgeworth22)_
- **CT** [#2046](https://github.com/jaywedgeworth22/Congress.Trade/pull/2046): docs: add Planned effort-log rows for the 2026-08-19 full-app review _(by jaywedgeworth22)_
- **CT** [#2065](https://github.com/jaywedgeworth22/Congress.Trade/pull/2065): Show FinancialModelingPrep.com and hide dead latency lanes _(by jaywedgeworth22)_
- **CT** [#2066](https://github.com/jaywedgeworth22/Congress.Trade/pull/2066): fix: take twin-dedupe off unbounded feed COUNT (#2062) _(by jaywedgeworth22)_
- **CT** [#2068](https://github.com/jaywedgeworth22/Congress.Trade/pull/2068): fix(legal): government non-affiliation disclaimer + accurate filing scope _(by jaywedgeworth22)_
- **CT** [#2069](https://github.com/jaywedgeworth22/Congress.Trade/pull/2069): fix: apply twin-dedupe after cheap first-page LIMIT (#2062) _(by jaywedgeworth22)_
- **CT** [#2070](https://github.com/jaywedgeworth22/Congress.Trade/pull/2070): fix(web): self-host Inter so the body font finally loads (QABUGHUNT-01/WEBPERF-01) _(by jaywedgeworth22)_
- **CT** [#2073](https://github.com/jaywedgeworth22/Congress.Trade/pull/2073): fix(web): keep connecting banner out of the header-to-filter gap _(by jaywedgeworth22)_
- **CT** [#2074](https://github.com/jaywedgeworth22/Congress.Trade/pull/2074): ci: pin Linux GitHub Actions to ubuntu-latest _(by jaywedgeworth22)_
- **DD** [#92](https://github.com/jaywedgeworth22/DealDex/pull/92): docs: strengthen two-spaces rule to cover chat replies and internal prose _(by jaywedgeworth22)_
- **DD** [#94](https://github.com/jaywedgeworth22/DealDex/pull/94): Add Apache License 2.0 at repo root _(by jaywedgeworth22)_
- **ST** [#2796](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2796): fix(ops): alert silent deploy freezes + isolate CT OCR load (#2545) _(by jaywedgeworth22)_
- **ST** [#2798](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2798): fix(ops): mute retired FilingAPI leftover 401s and live-boot connection pages _(by jaywedgeworth22)_
- **ST** [#2813](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2813): fix(roic): resume Individual archive from cache and artifacts _(by jaywedgeworth22)_
- **ST** [#2814](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2814): fix(ios): drop leaked coordinator notes from user-visible copy _(by jaywedgeworth22)_
- **ST** [#2818](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2818): Stamp delayed fallback on approval cards; keep trading _(by jaywedgeworth22)_
- **ST** [#2834](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2834): fix(llm+scan): Green 400 failover and Nasdaq screener so cascade runs _(by jaywedgeworth22)_
- **ST** [#2857](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2857): iOS Guardrails names + fold #2849 Desk subtitle _(by jaywedgeworth22)_
- **ST** [#2858](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2858): docs(review): 2026-08-18 full-app expert-panel review — desktop web + mobile web + iOS _(by jaywedgeworth22)_
- **ST** [#2859](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2859): docs(review): Part II — adversarial re-verify, gap coverage, deduped fix plan _(by jaywedgeworth22)_
- **ST** [#2864](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2864): docs(review): commit the audit board + machine-readable work items _(by jaywedgeworth22)_
- **ST** [#2865](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2865): fix(alerts): evaluate user-scoped quotes, do not fail silent _(by jaywedgeworth22)_
- **ST** [#2872](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2872): fix(home): real proposal ids, honest tones, keyboard rows _(by jaywedgeworth22)_
- **ST** [#2874](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2874): fix(coach): fail-closed tool inputs and abort in-flight turns _(by jaywedgeworth22)_
- **ST** [#2876](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2876): fix(accounts): do not copy Autopilot or reactivate a draining account _(by jaywedgeworth22)_
- **ST** [#2877](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2877): fix(alerts): 60s same-alert delivery lock (cluster alert-repeat-lock) _(by jaywedgeworth22)_
- **ST** [#2879](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2879): fix(market): session-aware cache TTL, not calendar-day freeze _(by jaywedgeworth22)_
- **ST** [#2881](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2881): docs(review): record the four owner decisions from the full-app review _(by jaywedgeworth22)_
- **ST** [#2882](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2882): fix(orders): do not auto-replace orders we do not own _(by jaywedgeworth22)_
- **ST** [#2887](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2887): fix(copy): guardrail claims match advisory engine _(by jaywedgeworth22)_
- **ST** [#2888](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2888): fix(run): scope Red Team, retry and learned directives to the run's account _(by jaywedgeworth22)_
- **ST** [#2889](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2889): fix(console): wire dead tax/webhook/preset controls _(by jaywedgeworth22)_
- **ST** [#2890](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2890): docs: strengthen two-spaces rule to cover chat replies and internal prose _(by jaywedgeworth22)_
- **ST** [#2892](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2892): fix(console): show per-account truth instead of the active account's data _(by jaywedgeworth22)_
- **ST** [#2893](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2893): docs: state HOW to emit the two-space gap so it is visible _(by jaywedgeworth22)_
- **ST** [#2894](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2894): docs: add Planned effort-log rows for the 2026-08-19 full-app review _(by jaywedgeworth22)_
- **ST** [#2940](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2940): Set the Pinecone Standard trial calendar to 7 days from Aug 19 _(by jaywedgeworth22)_
- **ST** [#2942](https://github.com/jaywedgeworth22/Socratic.Trade/pull/2942): fix(console): honor push deep links and close P1/P2 parity gaps _(by jaywedgeworth22)_
- **UM** [#1235](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1235): docs: 2026-08-17 security and privacy audit _(by jaywedgeworth22)_
- **UM** [#1236](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1236): docs: 2026-08-17 blind-spots audit (report only) _(by jaywedgeworth22)_
- **UM** [#1243](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1243): docs: strengthen two-spaces rule to cover chat replies and internal prose _(by jaywedgeworth22)_
- **UM** [#1244](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1244): fix(deps): resolve npm audit high — deepmerge-ts stack exhaustion via prisma _(by jaywedgeworth22)_
- **UM** [#1245](https://github.com/jaywedgeworth22/Usage-Monitor/pull/1245): Cross-app coordination follow-ups (pin check + CT health) _(by jaywedgeworth22)_
- **CTS** `Cursor` [#275](https://github.com/jaywedgeworth22/congress-trading-shared/pull/275): docs: Congress.Trade host is Coolify, not Deno Deploy _(by jaywedgeworth22)_
- **CTS** [#276](https://github.com/jaywedgeworth22/congress-trading-shared/pull/276): docs: strengthen two-spaces rule to cover chat replies and internal prose _(by jaywedgeworth22)_
- **CTS** [#277](https://github.com/jaywedgeworth22/congress-trading-shared/pull/277): docs: correct two-spaces guidance to use literal &nbsp; entity, not raw NBSP _(by jaywedgeworth22)_
- **CTS** [#278](https://github.com/jaywedgeworth22/congress-trading-shared/pull/278): docs: effort-log pointer for ST audit #2802 follow-ups _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1537](https://github.com/jaywedgeworth22/Congress.Trade/issues/1537): Deploy: brief 'no available server' downtime on every Coolify container swap
- **CT** [#1574](https://github.com/jaywedgeworth22/Congress.Trade/issues/1574): One-time backfill: reconcile 547 filings rows desynced from resolved review_queue state
- **CT** [#1994](https://github.com/jaywedgeworth22/Congress.Trade/issues/1994): 2026-08-18 — IN PR #1993 — #1991 iOS Admin + Review Queue (branch
- **CT** [#2005](https://github.com/jaywedgeworth22/Congress.Trade/issues/2005): 2026-08-18 — IN PROGRESS — No public extract card; Admin nav badges;
- **CT** [#2023](https://github.com/jaywedgeworth22/Congress.Trade/issues/2023): OGE executive poll interval: 15 minutes (keep 10m failure backoff)
- **CT** [#2025](https://github.com/jaywedgeworth22/Congress.Trade/issues/2025): OGE executive on House/Senate adaptive probe schedule
- **CT** [#2033](https://github.com/jaywedgeworth22/Congress.Trade/issues/2033): OPSRELIABILITY-01: every main merge 502s congress.trade for ~60s (docs-only included)
- **CT** [#2034](https://github.com/jaywedgeworth22/Congress.Trade/issues/2034): In-app account deletion (LEGALCOMPLIANCE-01, Guideline 5.1.1(v))
- **CT** [#2062](https://github.com/jaywedgeworth22/Congress.Trade/issues/2062): PR 2037 twin-dedupe hangs /api/transactions and Trends (COUNT NOT EXISTS)
- **CT** [#2071](https://github.com/jaywedgeworth22/Congress.Trade/issues/2071): Connecting banner sits between header and filter row
- **ST** [#2545](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2545): P0: Deploy pipeline froze all day 2026-08-06 — SSH exec stream dies mid-build under shared-box load; add freshness alert + isolate CT OCR load
- **ST** [#2833](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2833): Live prod triage 2026-08-18
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
- **CT** [#2062](https://github.com/jaywedgeworth22/Congress.Trade/issues/2062): PR 2037 twin-dedupe hangs /api/transactions and Trends (COUNT NOT EXISTS)
- **CT** [#2063](https://github.com/jaywedgeworth22/Congress.Trade/issues/2063): 2026-08-20 — IN PR #1964 — #1537 Coolify compose swap drops every
- **CT** [#2067](https://github.com/jaywedgeworth22/Congress.Trade/issues/2067): 2026-08-20 — IN PR #2065 — Latency comparison display
- **CT** [#2071](https://github.com/jaywedgeworth22/Congress.Trade/issues/2071): Connecting banner sits between header and filter row
- **DD** [#95](https://github.com/jaywedgeworth22/DealDex/issues/95): 2026-08-20 — IN PR #94 — Apache License 2.0 at repo root. Branch
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
- **ST** [#2943](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2943): 2026-08-19 — IN PROGRESS — Review clusters not covered by any other seat (16 + 4 owner decisions)
- **UM** [#1241](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1241): Docs: Deno Deploy is retired; Coolify is the Congress.Trade host
- **UM** [#1246](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1246): 2026-08-17 — IN PR #1235 — Read-only security/privacy audit (branch
- **AFC** [#43](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/43): mac.jays.services collab read (LIVE)

### Effort board

- **AFC** `Cursor` 2026-08-19 — LIVE — mac.jays.services collab tunnel. pm2 `mac-collab` on `127.0.0.1:8792`. Same named tunnel (ingress v8) + proxied CNAME. Public `/health`. Token-gated `/files` + `/files/<name>` (allowlist only). Token `~/.secrets/mac-collab.env` (`MAC_COLLAB_TOKEN`, never print). xcode + scout `/health` still 200. Do not mint TryCloudflare. Do not change `SENATE_RELAY_URL`

## 2026-08-18

*42 PRs merged · 27 issues opened · 76 issues closed · 3 effort rows*

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
- **DD** [#82](https://github.com/jaywedgeworth22/DealDex/pull/82): ios: switch bundle identifier to online.dealdex _(by jaywedgeworth22)_
- **DD** [#86](https://github.com/jaywedgeworth22/DealDex/pull/86): Official DealDex wordmark for in-app and web (icon is a follow-up) _(by jaywedgeworth22)_
- **DD** [#87](https://github.com/jaywedgeworth22/DealDex/pull/87): Official DealDex DD AppIcon and TestFlight reject fixes _(by jaywedgeworth22)_
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
- **AFC** `Grok` [#41](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/41): docs: Shellular — ACP argv and — :12419 _(by jaywedgeworth22)_
- **AFC** `Grok` [#42](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/42): docs: shared — for local chat control _(by jaywedgeworth22)_

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
- **DD** [#88](https://github.com/jaywedgeworth22/DealDex/issues/88): 2026-08-18 — COMPLETED/MERGED #82 — iOS bundle ID online.dealdex. Team
- **DD** [#90](https://github.com/jaywedgeworth22/DealDex/issues/90): 2026-08-19 — COMPLETED/MERGED #86 — Official DealDex wordmark (in-app
- **ST** [#2752](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2752): Review UX: fast approve, live vs proposed price, Retry Red Team, clearer agent controls
- **ST** [#2836](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2836): 2026-08-16 — COMPLETED via #2757 — Review UX: fast approve, live vs
- **ST** [#2837](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2837): Prefer Pushover over Resend — COMPLETED via #2698
- **ST** [#2838](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2838): Durable litestream remote-inventory cache — COMPLETED
- **ST** [#2839](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2839): 2026-08-17 — CANCELLED — FilingAPI Plus checkout. Owner later kept the
- **ST** [#2843](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2843): rag-embed DeepInfra batch-window 400 — IN PROGRESS
- **ST** [#2846](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2846): rag-embed DeepInfra batch-window 400
- **CTS** [#248](https://github.com/jaywedgeworth22/congress-trading-shared/issues/248): ISO 8601 UTC date/time formatting contract
- **CTS** [#265](https://github.com/jaywedgeworth22/congress-trading-shared/issues/265): Effort-sync transport-level retry — IN PR
- **CTS** [#273](https://github.com/jaywedgeworth22/congress-trading-shared/issues/273): 2026-08-17 — BOARD HYGIENE — ISO 8601 already shipped as v2.3.0

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
- **DD** [#83](https://github.com/jaywedgeworth22/DealDex/issues/83): 2026-08-18 — IN PROGRESS — iOS bundle ID online.dealdex (PR #82)
- **DD** [#84](https://github.com/jaywedgeworth22/DealDex/issues/84): 2026-08-14 — PLANNED — TestFlight + App Store + Play upload. Blocked on
- **DD** [#88](https://github.com/jaywedgeworth22/DealDex/issues/88): 2026-08-18 — COMPLETED/MERGED #82 — iOS bundle ID online.dealdex. Team
- **DD** [#89](https://github.com/jaywedgeworth22/DealDex/issues/89): 2026-08-19 — IN PROGRESS — Official DealDex wordmark (in-app / web
- **DD** [#90](https://github.com/jaywedgeworth22/DealDex/issues/90): 2026-08-19 — COMPLETED/MERGED #86 — Official DealDex wordmark (in-app
- **DD** [#91](https://github.com/jaywedgeworth22/DealDex/issues/91): 2026-08-19 — IN PR — Official DD AppIcon + TestFlight rejects. Branch
- **ST** [#2833](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2833): Live prod triage 2026-08-18
- **ST** [#2835](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2835): 2026-08-15 — IN PROGRESS — Website favicon: cropped offset candlestick
- **ST** [#2836](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2836): 2026-08-16 — COMPLETED via #2757 — Review UX: fast approve, live vs
- **ST** [#2837](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2837): Prefer Pushover over Resend — COMPLETED via #2698
- **ST** [#2838](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2838): Durable litestream remote-inventory cache — COMPLETED
- **ST** [#2839](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2839): 2026-08-17 — CANCELLED — FilingAPI Plus checkout. Owner later kept the
- **ST** [#2843](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2843): rag-embed DeepInfra batch-window 400 — IN PROGRESS
- **ST** [#2846](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2846): rag-embed DeepInfra batch-window 400
- **CTS** [#273](https://github.com/jaywedgeworth22/congress-trading-shared/issues/273): 2026-08-17 — BOARD HYGIENE — ISO 8601 already shipped as v2.3.0
- **CTS** [#274](https://github.com/jaywedgeworth22/congress-trading-shared/issues/274): 2026-08-17 — BOARD HYGIENE — July 2026 cross-app leftovers parked

### Effort board

- **AFC** `Grok` 2026-08-18 — COMPLETED/LIVE — Max local — chat control. pm2 ` ` on `~/.grok/leader.sock` (` — always-approve`, ` — no-exit-on-disconnect`). Shellular spawn ` agent — always-approve — leader stdio`. `[cli] use_leader = true` for new TUI. `leader-client.py list` saw 30 sessions including this chat. — stays ` — no-leader serve` on `:12419` (` — leader serve` does
- **AFC** `Grok` 2026-08-18 — COMPLETED/LIVE — Restore Shellular — ACP (`ACP connection closed`). Wrong argv ` agent stdio — always-approve` (flag belongs on `agent`). Fixed `~/.shellular/agents.json` to `~/.grok/bin/grok agent — always-approve stdio`. Homebrew node restored (`merve` 1.2.2_2 + node 26.7.0). — on `:12419` only. Phone client reconnected 4:21pm
- **AFC** `Grok` 2026-08-20 — COMPLETED — Coolify host disk reclaim (fleet-hetzner-nbg1). Owner: free disk space swiftly. Overnight hygiene had used=97% / 4.5G free; this turn started at 97G used / 67%. Deleted completed 2026-08-18 ST restore drills (`/data/scratch/socratic-restore-20260818`, `/data/backups/restore-proof/socratic-restore-scratch-20260817`, ~10G), extra ST snapshot beyond KEEP_C

## 2026-08-17

*53 PRs merged · 76 issues opened · 101 issues closed · 16 effort rows*

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
- **DD** `Grok` [#76](https://github.com/jaywedgeworth22/DealDex/pull/76): docs(effort): board hygiene — close stale In Progress _(by jaywedgeworth22)_
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
- **AFC** `Grok` [#40](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/40): docs: effort-board hygiene note _(by jaywedgeworth22)_
- **CTS** [#271](https://github.com/jaywedgeworth22/congress-trading-shared/pull/271): chore(deps): bump anthropics/claude-code-action from 1.0.187 to 1.0.193 _(by dependabot[bot])_
- **CTS** `Grok` [#272](https://github.com/jaywedgeworth22/congress-trading-shared/pull/272): docs(effort): board hygiene — close stale In Progress _(by jaywedgeworth22)_

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
- **DD** [#77](https://github.com/jaywedgeworth22/DealDex/issues/77): 2026-08-15 — COMPLETED/MERGED #71 — Vercel + GitHub +
- **DD** [#78](https://github.com/jaywedgeworth22/DealDex/issues/78): 2026-08-17 — COMPLETED — Effort-board hygiene. Live In Progress already
- **DD** [#79](https://github.com/jaywedgeworth22/DealDex/issues/79): 2026-08-16 — IN PR — Rename Apple Note pointer to ⭐️ Background Jobs
- **DD** [#80](https://github.com/jaywedgeworth22/DealDex/issues/80): 2026-08-15 — COMPLETED/MERGED #61 — Point DealDex AGENTS.md at Mac
- **DD** [#81](https://github.com/jaywedgeworth22/DealDex/issues/81): Fast-forward local main after Mac-storage prune — COMPLETED
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
- **DD** [#77](https://github.com/jaywedgeworth22/DealDex/issues/77): 2026-08-15 — COMPLETED/MERGED #71 — Vercel + GitHub +
- **DD** [#78](https://github.com/jaywedgeworth22/DealDex/issues/78): 2026-08-17 — COMPLETED — Effort-board hygiene. Live In Progress already
- **DD** [#79](https://github.com/jaywedgeworth22/DealDex/issues/79): 2026-08-16 — IN PR — Rename Apple Note pointer to ⭐️ Background Jobs
- **DD** [#80](https://github.com/jaywedgeworth22/DealDex/issues/80): 2026-08-15 — COMPLETED/MERGED #61 — Point DealDex AGENTS.md at Mac
- **DD** [#81](https://github.com/jaywedgeworth22/DealDex/issues/81): Fast-forward local main after Mac-storage prune — COMPLETED
- **ST** [#2770](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2770): Fix Green Team OpenRouter slugs and stop paging lease-lost as Pinecone/rerank outages
- **ST** [#2773](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2773): 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control
- **ST** [#2774](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2774): 2026-08-16 — IN PROGRESS — Review UX: fast approve, live vs proposed
- **ST** [#2775](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2775): 2026-08-15 — IN PROGRESS — Website favicon: cropped offset candlestick
- **ST** [#2776](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2776): Fix ST Litestream wedge and prefer Pushover over Resend
- **ST** [#2777](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2777): Durable litestream remote-inventory cache (PR #2665
- **ST** [#2778](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2778): [OWNER] FilingAPI Plus checkout. Stored FILINGAPI key is still
- **ST** [#2779](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2779): 2026-08-17 — BOARD HYGIENE — moved the following verified-merged rows
- **ST** [#2780](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2780): Litestream L2/L3 + FilingAPI + ROIC earnings universe
- **ST** [#2781](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2781): 2026-08-14 — COMPLETED (docs in UM #1180) — Backup restore-proof (no ST
- **ST** [#2782](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2782): iOS full desk (Coach, Scan, Guardrails, Results, Data
- **ST** [#2783](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2783): Quote sheet Key Stats + fill/position card tap — YIELDED
- **ST** [#2786](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2786): Green-Team empty/malformed failover +
- **ST** [#2789](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2789): Retire FilingAPI.dev — use ROIC.ai only — IN PROGRESS
- **ST** [#2790](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2790): [OWNER] FilingAPI Plus checkout. SUPERSEDED 2026-08-17

### Effort board

- **UM** `Cursor` 2026-08-17 — IN PR #1235 — Read-only security/privacy audit (branch `cursor/security-privacy-audit-f36a`). Report-only: `docs/audits/2026-08-17-security-privacy.md`. Scope: secrets, token storage, account isolation, logs, receipt email, billing privacy, authz, deps, backups, R2, alert webhooks, recovery. No secret values. No implementation. Keepout: outcomes/projections aud
- **UM** `Grok` 2026-08-17 — IN PR — Outcomes/projections audit (branch `cursor/outcomes-projections-audit-4269`). Read-only report at `docs/audits/2026-08-17-outcomes-projections.md`. Not taking implementation. Disjoint from providers-accuracy `cursor/providers-accuracy-audit-9579`
- **UM** `Cursor` 2026-08-17 — IN PR #1239 — Read-only backend durability audit (branch `cursor/backend-durability-audit-c46b`). Report-only: `docs/audits/2026-08-17-backend-durability.md`. Accounts for #1180 restore-proof, #1223 R2 weekly-only, #1226/#1228 ST Litestream visibility, 2026-08-16 `/tmp` 503, #1144 kill-switch, #1131 PD. Keepout: parallel UM audits #1233–#1238. No product-code ed
- **UM** `Grok` `Cursor` 2026-08-17 — COMPLETED/MERGED #1237 `dc109fdc` — Read-only web/iOS parity audit (branch `cursor/web-ios-parity-audit-fc87`). Desktop + mobile web vs Client + Local. Report `docs/audits/2026-08-17-web-ios-parity.md`. No product code. Top gap: web hero uses global budget; Client hero sums provider budgets. Mac Health route is bearer-only. TestFlight still 1.0.0 REJECT
- **UM** `Grok` 2026-08-17 — COMPLETED/MERGED #1234 `ed996adf` — Read-only provider-connectors accuracy audit (branch `cursor/providers-accuracy-audit-9579`). Report-only: `docs/audits/2026-08-17-providers-accuracy.md`. All poll adapters + identity, balances, credits, usage, costs, invoices/receipts, pagination, currencies, units, rate limits, stale/fallback, projections, discrepancy alerts. N
- **UM** `Grok` 2026-08-17 — COMPLETED/MERGED #1234 — Read-only provider-connectors accuracy audit (branch `cursor/providers-accuracy-audit-9579`). Report-only: `docs/audits/2026-08-17-providers-accuracy.md`. All poll adapters + identity, balances, credits, usage, costs, invoices/receipts, pagination, currencies, units, rate limits, stale/fallback, projections, discrepancy alerts. Not taking i
- **UM** `Grok` 2026-08-17 — IN PR #1234 — Read-only provider-connectors accuracy audit (branch `cursor/providers-accuracy-audit-9579`). Report-only: `docs/audits/2026-08-17-providers-accuracy.md`. All poll adapters + identity, balances, credits, usage, costs, invoices/receipts, pagination, currencies, units, rate limits, stale/fallback, projections, discrepancy alerts. Not taking implementati
- **UM** `Grok` 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control board. Zero open PRs on 2026-08-17. #1206/#1204/#1198/#1180/#1165/#1185/#1218 already merged. First lines of those rows preserved under Completed. Invalid Binary stays Planned (owner: rebuild on stable macOS). Historical-archive heading renamed so #953 is not re-opened as In Progress
- **UM** `Grok` 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control board. Mirror PR #1233 still open (verify failed on `npm audit` high / prisma deepmerge-ts; main CI is green). Rebase + rerun
- **UM** `Grok` 2026-08-17 — SHIPPED TestFlight — UM Client + Local 1.0.1 via Xcode.app on this Mac. Owner: use normal Xcode here. Client `1.0.1 (202608172057)` upload succeeded 16:08Z and again 18:56Z. Local upload succeeded 19:01Z. `DEVELOPER_DIR=/Applications/Xcode.app` (26.6). ASC list API was 500 at start; ship used ` — version 1.0.1`. App Store review attach still needs a VALID processing s
- **UM** `Grok` 2026-08-17 — BOARD HYGIENE — verified-merged In Progress rows (first lines unchanged)
- **CTS** `Grok` 2026-08-17 — BOARD HYGIENE — ISO 8601 already shipped as v2.3.0 (Deployed). First line preserved
- **DD** `Grok` 2026-08-17 — COMPLETED — Effort-board hygiene. Live In Progress already empty; landing this board as the repo mirror so stale GitHub `state:in-progress` issues close
- **AFC** `Grok` 2026-08-17 — IN PROGRESS — Rebuild UM Client + Local with Xcode.app on this Mac. Owner: agents use normal `/Applications/Xcode.app` here (`xcodebuild` / `simctl`). Not parked on “beta host”
- **AFC** `Grok` 2026-08-17 — IN PROGRESS — Effort-board hygiene + this-session control board. Hygiene PRs armed
- **AFC** `Grok` 2026-08-17 — BOARD HYGIENE — folded the duplicate lower In Progress (July 2026 audit leftovers + already-COMPLETED onboard rows). First lines unchanged

## 2026-08-16

*42 PRs merged · 7 issues opened · 6 issues closed · 6 effort rows*

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
- **AFC** `Grok` [#37](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/37): Move Mac always-on jobs to pm2 and add a down-watch _(by jaywedgeworth22)_
- **AFC** `Grok` [#38](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/38): mac-process-watch restarts always-on Mac jobs _(by jaywedgeworth22)_
- **AFC** `Grok` [#39](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/39): Keep scheduled Mac jobs able to fire _(by jaywedgeworth22)_

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

- **DD** `Grok` 2026-08-16 — IN PR — Rename Apple Note pointer to `⭐️ Background Jobs Master List` (branch `grok/note-title`, worktree `~/apps/dealdex — title`). AGENTS.md only
- **AFC** `Grok` 2026-08-16 — IN PROGRESS — FDA for Xcode Python.app + iOS 26.5 platform + TestFlight ships. iOS 26.5 runtime installed (`23F77`). CT 1.0.17 archive running (stuck at provisioning/keychain — needs owner Allow/Touch ID if a dialog is up). SIP blocked TCC.db write; launchd iMessage still needs FDA toggle in System Settings. Listener is up from this session
- **AFC** `Grok` 2026-08-16 — IN PROGRESS — FDA for Xcode Python.app + iOS 26.5 platform + TestFlight ships. iOS 26.5 runtime installed (`23F77`). CT 1.0.17 archive running (stuck at provisioning/keychain — needs owner Allow/Touch ID if a dialog is up). SIP blocked TCC.db write; launchd iMessage still needs FDA toggle in System Settings. Listener is up from this session
- **AFC** `Grok` 2026-08-16 — COMPLETED/LIVE — Scheduled jobs operational when triggered. Cleared stale janitor (Aug 11) + shepherd (Jul 14) locks; both steal >2h leftovers. Watch keeps timers loaded (no idle kickstart; never ios-ship-now / com.PM2). Hetzner cron retargeted to live `<HETZNER_SERVER_ID>` / `nbg1-dc3`. Coordinator PR #39 merged
- **AFC** `Grok` 2026-08-16 — COMPLETED/LIVE — mac-process-watch restarts always-on jobs. Live `~/apps/mac-process-watch.sh` (launchd already runs it). pm2 resurrect / ecosystem start + launchd kickstart/bootstrap. 4/hour backoff. Verified: stopped `code-main-keeper`, watch brought it back. Coordinator PR #38 (`grok/mac-watch-restart`). Note `[FLEET, ] mac-process-watch restarts always
- **AFC** `Grok` 2026-08-16 — COMPLETED — Note retitled `⭐️ Background Jobs Master List`; restarted intended always-on pm2 jobs. Pointers: coordinator #33/#34, ST #2739, UM #1224, DealDex #74, CT #1886. scout needed stdin=/dev/null. com.PM2 plist now Homebrew pm2

## 2026-08-15

*37 PRs merged · 15 issues opened · 9 issues closed · 11 effort rows*

### Merged PRs

- **CT** `Grok` [#1876](https://github.com/jaywedgeworth22/Congress.Trade/pull/1876): docs: point agents at Mac background-jobs master list _(by jaywedgeworth22)_
- **CT** [#1877](https://github.com/jaywedgeworth22/Congress.Trade/pull/1877): Record submitting iOS 1.0 for App Review _(by jaywedgeworth22)_
- **CT** [#1878](https://github.com/jaywedgeworth22/Congress.Trade/pull/1878): Add PrivacyInfo and a Tahoe GM App Store ship _(by jaywedgeworth22)_
- **CT** [#1879](https://github.com/jaywedgeworth22/Congress.Trade/pull/1879): Record the Tahoe GM App Store resubmit _(by jaywedgeworth22)_
- **CT** [#1881](https://github.com/jaywedgeworth22/Congress.Trade/pull/1881): fix(ios): parse tab footer links and sign latency lead/lag _(by jaywedgeworth22)_
- **CT** [#1882](https://github.com/jaywedgeworth22/Congress.Trade/pull/1882): Keep only the newest weekly R2 archive _(by jaywedgeworth22)_
- **CT** [#1884](https://github.com/jaywedgeworth22/Congress.Trade/pull/1884): fix(ui): Trends order, ticker #/$, Directory pager, Khanna dates _(by jaywedgeworth22)_
- **DD** `Grok` [#61](https://github.com/jaywedgeworth22/DealDex/pull/61): docs: point agents at Mac background-jobs master list _(by jaywedgeworth22)_
- **DD** [#63](https://github.com/jaywedgeworth22/DealDex/pull/63): Record local main fast-forward on the effort board _(by jaywedgeworth22)_
- **DD** [#65](https://github.com/jaywedgeworth22/DealDex/pull/65): share image, shared scan cache, app marks _(by jaywedgeworth22)_
- **DD** [#67](https://github.com/jaywedgeworth22/DealDex/pull/67): Paint the eBay and Mercari filter chips white _(by jaywedgeworth22)_
- **DD** `Grok` [#71](https://github.com/jaywedgeworth22/DealDex/pull/71): Vercel + GitHub for dealdex.online _(by jaywedgeworth22)_
- **DD** [#74](https://github.com/jaywedgeworth22/DealDex/pull/74): docs: point AGENTS at ⭐️ Background Jobs Master List _(by jaywedgeworth22)_
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
- **AFC** `Grok` [#31](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/31): docs: Mac background-jobs master list (always-on vs on-demand) _(by jaywedgeworth22)_
- **AFC** [#32](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/32): docs(agents): forbid grepping secrets files for KEY=value lines _(by jaywedgeworth22)_
- **AFC** [#33](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/33): docs: point fleet instructions at ⭐️ Background Jobs Master List _(by jaywedgeworth22)_
- **AFC** `Grok` [#34](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/34): docs: refresh Mac process list after always-on restart _(by jaywedgeworth22)_
- **AFC** `Grok` [#35](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/35): docs: launchd helper inventory (vision/xcode/imessage/pm2) _(by jaywedgeworth22)_
- **AFC** `Grok` [#36](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/36): docs: Mac process list after launchd diagnose _(by jaywedgeworth22)_
- **CTS** [#269](https://github.com/jaywedgeworth22/congress-trading-shared/pull/269): Record local main fast-forward on the effort board _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1880](https://github.com/jaywedgeworth22/Congress.Trade/issues/1880): iOS tab footer links + latency lead/lag signs
- **CT** [#1883](https://github.com/jaywedgeworth22/Congress.Trade/issues/1883): Trends layout, Directory pager, Khanna recent-trade dates
- **DD** [#62](https://github.com/jaywedgeworth22/DealDex/issues/62): 2026-08-15 — IN PR — Point DealDex AGENTS.md at Mac background-jobs
- **DD** [#64](https://github.com/jaywedgeworth22/DealDex/issues/64): Fast-forward local main after Mac-storage prune — COMPLETED
- **DD** [#68](https://github.com/jaywedgeworth22/DealDex/issues/68): 2026-08-15 — COMPLETED — DealDex OG + shared scan cache + app
- **DD** [#72](https://github.com/jaywedgeworth22/DealDex/issues/72): 2026-08-15 — COMPLETED — White filter-row marks (PR #67)
- **DD** [#75](https://github.com/jaywedgeworth22/DealDex/issues/75): 2026-08-16 — IN PR — Rename Apple Note pointer to ⭐️ Background Jobs
- **UM** [#1139](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1139): [FLEET] R2 archive creds live-check — PARTIAL 2026-08-12. UM first weekly
- **CTS** [#270](https://github.com/jaywedgeworth22/congress-trading-shared/issues/270): Fast-forward local main after Mac-storage prune

### Issues opened

- **CT** [#1880](https://github.com/jaywedgeworth22/Congress.Trade/issues/1880): iOS tab footer links + latency lead/lag signs
- **CT** [#1883](https://github.com/jaywedgeworth22/Congress.Trade/issues/1883): Trends layout, Directory pager, Khanna recent-trade dates
- **DD** [#62](https://github.com/jaywedgeworth22/DealDex/issues/62): 2026-08-15 — IN PR — Point DealDex AGENTS.md at Mac background-jobs
- **DD** [#64](https://github.com/jaywedgeworth22/DealDex/issues/64): Fast-forward local main after Mac-storage prune — COMPLETED
- **DD** [#66](https://github.com/jaywedgeworth22/DealDex/issues/66): 2026-08-15 — IN PROGRESS — DealDex OG + shared scan cache + app
- **DD** [#68](https://github.com/jaywedgeworth22/DealDex/issues/68): 2026-08-15 — COMPLETED — DealDex OG + shared scan cache + app
- **DD** [#69](https://github.com/jaywedgeworth22/DealDex/issues/69): 2026-08-15 — IN PROGRESS — White filter-row marks. eBay/Mercari
- **DD** [#72](https://github.com/jaywedgeworth22/DealDex/issues/72): 2026-08-15 — COMPLETED — White filter-row marks (PR #67)
- **DD** [#73](https://github.com/jaywedgeworth22/DealDex/issues/73): 2026-08-15 — IN PROGRESS — Vercel + GitHub + dealdex.online
- **DD** [#75](https://github.com/jaywedgeworth22/DealDex/issues/75): 2026-08-16 — IN PR — Rename Apple Note pointer to ⭐️ Background Jobs
- **ST** [#2731](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2731): Website favicon: cropped offset candlestick ST, transparent
- **ST** [#2735](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2735): 13F + ARK + Form 4 as live idea sources
- **ST** [#2738](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2738): Litestream L2/L3 + FilingAPI 401 + ROIC universe transcripts
- **UM** [#1222](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1222): [FLEET] R2 archive creds live-check — COMPLETED 2026-08-15. UM weekly
- **CTS** [#270](https://github.com/jaywedgeworth22/congress-trading-shared/issues/270): Fast-forward local main after Mac-storage prune

### Effort board

- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1180 — Backup restore-proof + honest gatesOverallOk (branch `grok/backup-restore-proof`). UM/CT B2 restore PASS; ST latest B2 was non-contiguous (later L1 suffix work). `gatesOverallOk` honest. CT weekly 401 later fixed 2026-08-15 with an account-write token. Receipt: `docs/rollouts/2026-08-14-backup-restore-proof.md`
- **UM** `Grok` [FLEET] R2 archive creds live-check — COMPLETED 2026-08-15. UM weekly still ok. ST historic LIST + Aug 9 cold snapshot remain; leftover R2 LTX pruned. CT weekly 401 fixed with a new account-write token in Infisical + host rclone `[r2]`; live key `weekly/congress-trade-20260815T211942Z.db`
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1180 — Backup restore-proof + honest gatesOverallOk (branch `grok/backup-restore-proof`). UM/CT B2 restore PASS. ST latest was non-contiguous (later L1 suffix work). `gatesOverallOk` honest. CT weekly 401 later fixed 2026-08-15. Receipt: `docs/rollouts/2026-08-14-backup-restore-proof.md`
- **CTS** `Grok` Fast-forward local main after Mac-storage prune — COMPLETED 2026-08-15. Discarded stale In-Progress row for already-merged #260/#262. `git pull — ff-only` `c1f6787` → `88c72b3`. 0 open PRs
- **DD** `Grok` 2026-08-15 — COMPLETED/MERGED #71 — Vercel + GitHub + dealdex.online. Live host is dealdex.online. Re-link on — Vercel if `main` is not auto-building
- **DD** `Grok` 2026-08-15 — COMPLETED/MERGED #61 — Point DealDex AGENTS.md at Mac background-jobs master list. Canonical `~/apps/MAC-LOCAL-PROCESSES.md` + pinned Note
- **DD** `Grok` Fast-forward local main after Mac-storage prune — COMPLETED 2026-08-15. Discarded local Xcode pbxproj dirt (shopping category / LD_RUNPATH rewrite). `git pull — ff-only` `58fcc12` → `6a686c1`. 0 open PRs
- **AFC** `Grok` 2026-08-15 11:51pm CT — COMPLETED — launchd always-on + on-demand helper pass (not pm2). vision-worker pid 40656 healthy (stale last-exit -15 / energy inefficient). xcode-health :8791 + xcode.jays.services 200. imessage — launchd FDA-blocked (disabled; Aqua orphan 81696 listening). com.PM2 plist already `/opt/homebrew/bin/pm2 resurrect`; bootstrapped LaunchOnlyOnce. ios-s
- **AFC** `Grok` `Codex` `Gemini` `Cursor` `Claude` Ban grepping secrets files for KEY=value lines — COMPLETED 2026-08-15. Coordinator #32 merged (`c6d304d`). Live `~/apps/AGENT-SYNC.md` § Handoff-file grep trap + .md / .md / fleet-standards + secret-safety skill. Names only: `grep -oE`. ST AGENTS.md landing separately on `grok/secret-file-grep-ban`
- **AFC** `Grok` `Cursor` 2026-08-15 — COMPLETED — Master list of Mac background jobs + Apple Note. Live `~/apps/MAC-LOCAL-PROCESSES.md` (second-pass helpers + vendor rows). Note `[FLEET, ] Mac background jobs master list` refreshed. Binding copied into AGENT-SYNC, TEMPLATE-AGENTS, ONBOARDING-NEW-AGENT, ~/.claude / ~/.codex / ~/.gemini / ~/. fleet-standards, plus CT #1876 / ST #2730
- **AFC** `Grok` `Claude` Finish — Mac-storage prune of leftover worktrees — COMPLETED 2026-08-15. — had already removed 45 ST trees (~50 GB) then hit weekly cap. This session inventoried ST/CT/UM/fleet/DealDex/Personal/CTS by GitHub PR state (not merge-base — squash-merge rewrites SHAs). Preserved remaining real diffs under `~/apps/_preserved-patches/`. Removed ~150 disposable worktrees (m

## 2026-08-14

*71 PRs merged · 33 issues opened · 22 issues closed · 27 effort rows*

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
- **DD** [#40](https://github.com/jaywedgeworth22/DealDex/pull/40): docs: AGENTS start-here table + stronger economics _(by jaywedgeworth22)_
- **DD** `Grok` [#41](https://github.com/jaywedgeworth22/DealDex/pull/41): Register the — Build Mac lane as a standing seat _(by jaywedgeworth22)_
- **DD** [#47](https://github.com/jaywedgeworth22/DealDex/pull/47): Link the Vercel dealdex project to GitHub main _(by jaywedgeworth22)_
- **DD** [#50](https://github.com/jaywedgeworth22/DealDex/pull/50): Build native Android and iOS apps _(by jaywedgeworth22)_
- **DD** [#54](https://github.com/jaywedgeworth22/DealDex/pull/54): Close native-build effort row after PR #50 _(by jaywedgeworth22)_
- **DD** [#56](https://github.com/jaywedgeworth22/DealDex/pull/56): Prepare DealDex for TestFlight, App Store, and Play _(by jaywedgeworth22)_
- **DD** [#58](https://github.com/jaywedgeworth22/DealDex/pull/58): Park store upload as Planned after PR #56 _(by jaywedgeworth22)_
- **PS** [#1](https://github.com/jaywedgeworth22/Personal-Site/pull/1): Join the fleet and fix About copy plus social-redirect docs _(by jaywedgeworth22)_
- **PS** [#4](https://github.com/jaywedgeworth22/Personal-Site/pull/4): Close out the fleet-onboard board row _(by jaywedgeworth22)_
- **PS** [#6](https://github.com/jaywedgeworth22/Personal-Site/pull/6): Point Doximity short link at the public view profile _(by jaywedgeworth22)_
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
- **AFC** [#25](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/25): docs: onboard links + subagent/economics wording _(by jaywedgeworth22)_
- **AFC** `Grok` [#26](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/26): Register — as a standing fleet seat _(by jaywedgeworth22)_
- **AFC** `Grok` [#27](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/27): Add — to the Agent Seat table _(by jaywedgeworth22)_
- **AFC** [#28](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/28): Register Personal-Site (PS) in the fleet registries _(by jaywedgeworth22)_
- **AFC** `Grok` [#29](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/29): Inventory Mac local processes and require agents to list them _(by jaywedgeworth22)_
- **AFC** `Grok` [#30](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/30): docs: two spaces after every sentence, including App Store review notes _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1716](https://github.com/jaywedgeworth22/Congress.Trade/issues/1716): 2026-08-11 1:05pm CT — COMPLETED — Outage post-mortem closed out
- **CT** [#1717](https://github.com/jaywedgeworth22/Congress.Trade/issues/1717): 2026-08-11 ~12:56pm CT — IN PROGRESS — App review top-to-bottom &
- **CT** [#1866](https://github.com/jaywedgeworth22/Congress.Trade/issues/1866): Verify ASC Premium intro offer is 2 weeks ( leftover from #1835)
- **DD** [#43](https://github.com/jaywedgeworth22/DealDex/issues/43): 2026-08-14 — COMPLETED — Onboarding links + subagent/economics wording
- **DD** [#44](https://github.com/jaywedgeworth22/DealDex/issues/44): 2026-08-13 — COMPLETED — White toggle wordmarks (PR #37)
- **DD** [#45](https://github.com/jaywedgeworth22/DealDex/issues/45): 2026-08-13 — COMPLETED — iOS agent build-loop policy (PR #18)
- **DD** [#48](https://github.com/jaywedgeworth22/DealDex/issues/48): 2026-08-14 — COMPLETED — Register — Build as a standing fleet
- **DD** [#51](https://github.com/jaywedgeworth22/DealDex/issues/51): 2026-08-14 — DEPLOYED — Vercel project dealdex (PR #47). Linked to
- **DD** [#52](https://github.com/jaywedgeworth22/DealDex/issues/52): 2026-08-14 — COMPLETED — Register — Build as a standing fleet
- **DD** [#55](https://github.com/jaywedgeworth22/DealDex/issues/55): 2026-08-14 — COMPLETED — Compile native iOS + Android apps (PR #50)
- **DD** [#59](https://github.com/jaywedgeworth22/DealDex/issues/59): 2026-08-14 — COMPLETED — Store-submit prep (PR #56). Privacy page
- **PS** [#2](https://github.com/jaywedgeworth22/Personal-Site/issues/2): 2026-08-14 — DEPLOYED — Social short-link URL redirects on
- **PS** [#3](https://github.com/jaywedgeworth22/Personal-Site/issues/3): 2026-08-14 — IN PROGRESS — Onboard Personal-Site as a fleet app + About
- **PS** [#5](https://github.com/jaywedgeworth22/Personal-Site/issues/5): 2026-08-14 — COMPLETED — Onboard Personal-Site as a fleet app + About
- **PS** [#7](https://github.com/jaywedgeworth22/Personal-Site/issues/7): 2026-08-14 — DEPLOYED — doximity.jaywedgeworth.com → public view
- **PS** [#8](https://github.com/jaywedgeworth22/Personal-Site/issues/8): 2026-08-14 — DEPLOYED — Social short-link URL redirects on
- **UM** [#1188](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1188): 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch
- **UM** [#1193](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1193): Finish cf-token-map.sh for Cloudflare token/account map
- **UM** [#1197](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1197): iOS More sheet opens at half height
- **UM** [#1199](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1199): 2026-08-14 — IN PR #1198 — iOS More sheet opens at ~50% (branch
- **UM** [#1205](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1205): 2026-08-14 — IN PROGRESS — R2 card: GB / 10 GB Free Tier + colored bar
- **UM** [#1207](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1207): 2026-08-14 — IN PROGRESS — R2 card layout + UM/Old usage read (branch

### Issues opened

- **CT** [#1861](https://github.com/jaywedgeworth22/Congress.Trade/issues/1861): 2026-08-14 — IN PROGRESS — iOS Trades sort grouping + search-slot status
- **CT** [#1866](https://github.com/jaywedgeworth22/Congress.Trade/issues/1866): Verify ASC Premium intro offer is 2 weeks ( leftover from #1835)
- **DD** [#42](https://github.com/jaywedgeworth22/DealDex/issues/42): 2026-08-14 — IN PROGRESS — Onboarding links + subagent/economics wording
- **DD** [#43](https://github.com/jaywedgeworth22/DealDex/issues/43): 2026-08-14 — COMPLETED — Onboarding links + subagent/economics wording
- **DD** [#44](https://github.com/jaywedgeworth22/DealDex/issues/44): 2026-08-13 — COMPLETED — White toggle wordmarks (PR #37)
- **DD** [#45](https://github.com/jaywedgeworth22/DealDex/issues/45): 2026-08-13 — COMPLETED — iOS agent build-loop policy (PR #18)
- **DD** [#46](https://github.com/jaywedgeworth22/DealDex/issues/46): 2026-08-14 — IN PROGRESS — Register — Build as a standing fleet
- **DD** [#48](https://github.com/jaywedgeworth22/DealDex/issues/48): 2026-08-14 — COMPLETED — Register — Build as a standing fleet
- **DD** [#49](https://github.com/jaywedgeworth22/DealDex/issues/49): 2026-08-14 — IN PROGRESS — Link Vercel project dealdex to GitHub
- **DD** [#51](https://github.com/jaywedgeworth22/DealDex/issues/51): 2026-08-14 — DEPLOYED — Vercel project dealdex (PR #47). Linked to
- **DD** [#52](https://github.com/jaywedgeworth22/DealDex/issues/52): 2026-08-14 — COMPLETED — Register — Build as a standing fleet
- **DD** [#53](https://github.com/jaywedgeworth22/DealDex/issues/53): 2026-08-14 — IN PROGRESS — Compile native iOS + Android apps (PR
- **DD** [#55](https://github.com/jaywedgeworth22/DealDex/issues/55): 2026-08-14 — COMPLETED — Compile native iOS + Android apps (PR #50)
- **DD** [#57](https://github.com/jaywedgeworth22/DealDex/issues/57): 2026-08-14 — IN PROGRESS — Submit DealDex to TestFlight / App Store and
- **DD** [#59](https://github.com/jaywedgeworth22/DealDex/issues/59): 2026-08-14 — COMPLETED — Store-submit prep (PR #56). Privacy page
- **DD** [#60](https://github.com/jaywedgeworth22/DealDex/issues/60): 2026-08-14 — PLANNED — TestFlight + App Store + Play upload. Blocked on
- **PS** [#2](https://github.com/jaywedgeworth22/Personal-Site/issues/2): 2026-08-14 — DEPLOYED — Social short-link URL redirects on
- **PS** [#3](https://github.com/jaywedgeworth22/Personal-Site/issues/3): 2026-08-14 — IN PROGRESS — Onboard Personal-Site as a fleet app + About
- **PS** [#5](https://github.com/jaywedgeworth22/Personal-Site/issues/5): 2026-08-14 — COMPLETED — Onboard Personal-Site as a fleet app + About
- **PS** [#7](https://github.com/jaywedgeworth22/Personal-Site/issues/7): 2026-08-14 — DEPLOYED — doximity.jaywedgeworth.com → public view
- **PS** [#8](https://github.com/jaywedgeworth22/Personal-Site/issues/8): 2026-08-14 — DEPLOYED — Social short-link URL redirects on
- **ST** [#2724](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2724): Collapse model versions onto family identity for Results / benchmarks / history
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

- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1206 `8c1d6dd0` — R2 card layout + UM/Old usage read (branch `grok/r2-bar-layout-and-um-read`). Bar as wide as the GB / 10 GB line, more row gap, vertically center labels. UM+Jay Old failed because month-long GraphQL storage dumps (337–416 KiB) overflowed the 256 KiB probe cap; shrink to 24h latest-per-bucket + 1 MiB trusted GraphQL cap. #1204 alr
- **UM** `Grok` `Claude` 2026-08-14 — COMPLETED — Pickup — chat “Usage monitor multi-platform section”. Platforms tab (#1099) and key/config bundle (#1145) already merged. Import Keys is already on Local TestFlight (last ship `1ac20f23` contains `9870d0ad`). Leftover R2 UM/Old false-unavailable + bar layout landed as #1206. Owner still needs `~/.secrets/umkeys-pass` (chmod 600) before a real AirDr
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1204 — R2 card: GB / 10 GB Free Tier + colored bar (branch `grok/r2-usage-bar`). Drop “% of free tier” text. Show used / 10 GB Free Tier and a fill bar (green / amber / red by closeness to 10 GB)
- **UM** `Grok` 2026-08-14 — IN PROGRESS — Point UM AGENTS.md at Mac process list (branch `grok/mac-local-processes`). One table row. Canonical list is `~/apps/MAC-LOCAL-PROCESSES.md`
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1198 `2ac7b9d4` — iOS More sheet opens at ~50% (branch `grok/ios-more-sheet-height`). Fitted custom detent, cap 88%. All 7 destinations on screen. Closed #1197
- **UM** `Grok` 2026-08-14 — DEPLOYED — Add all four Cloudflare accounts as UM providers. #1185 + oneshot #1187 live as `d674904`. Four ON rows: `cloudflare-usage-jays` …d1b7, `-socratic` …2e79, `-congress` …1ae9, `-jay-old` …8c73. Seed logged `created=4`; later ticks do not force `isActive`. UJS token is distinct `CLOUDFLARE_JAY_` (restored in Infisical; was overwritten with fleet). ST to
- **UM** `Grok` 2026-08-14 — IN PROGRESS — Apex iCloud MX + receipts Worker catch-all (branch `grok/apex-icloud-receipts-routing`). Owner: `@jays.services` → iCloud; `receipts.jays.services` → receipt-inbox Worker. Live DNS already cut over (apex `mx01`/`mx02.mail.icloud.com`, SPF `include:icloud.com`; receipts CF MX unchanged; catch-all now Worker). Docs PR #1182 (auto-merge). Do not repai
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1206 `8c1d6dd0` — R2 card layout + UM/Old usage read (branch `grok/r2-bar-layout-and-um-read`). Bar as wide as the GB / 10 GB line, more row gap, vertically center labels. UM+Jay Old failed because month-long GraphQL storage dumps (337–416 KiB) overflowed the 256 KiB probe cap; shrink to 24h latest-per-bucket + 1 MiB trusted GraphQL cap. #1204 al
- **UM** `Grok` `Claude` 2026-08-14 — COMPLETED — Pickup — chat “Usage monitor multi-platform section”. Platforms tab (#1099) and key/config bundle (#1145) already merged. Import Keys is already on Local TestFlight (last ship `1ac20f23` contains `9870d0ad`). Leftover R2 UM/Old false-unavailable + bar layout landed as #1206. Owner still needs `~/.secrets/umkeys-pass` (chmod 600) before a real AirD
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1204 — R2 card: GB / 10 GB Free Tier + colored bar (branch `grok/r2-usage-bar`). Drop “% of free tier” text. Show used / 10 GB Free Tier and a fill bar (green / amber / red by closeness to 10 GB)
- **UM** `Grok` 2026-08-14 — IN PROGRESS — Point UM AGENTS.md at Mac process list (branch `grok/mac-local-processes`). One table row. Canonical list is `~/apps/MAC-LOCAL-PROCESSES.md`
- **UM** `Grok` 2026-08-14 — COMPLETED/MERGED #1198 — iOS More sheet opens at ~50% (branch `grok/ios-more-sheet-height`). Fitted custom detent, cap 88%. All 7 destinations on screen. Closed #1197
- **DD** `Grok` 2026-08-14 — DEPLOYED — Vercel project dealdex (PR #47). Linked to GitHub `main`. Production READY: https://dealdex-git-main-jaywedgeworth22s-projects.vercel.app/ (HTTP 200, DealDex scan page). No custom domain
- **DD** `Grok` 2026-08-14 — COMPLETED — Store-submit prep (PR #56). Privacy page, listing copy, ship wrapper, export-compliance plist. ASC CREATE forbidden for App Manager key. Archive hung on Xcode 26 `clang -v`
- **DD** `Grok` 2026-08-14 — COMPLETED — Compile native iOS + Android apps (PR #50). Gradle 8.7 wrapper + XcodeGen spec. Debug APK in `public/DealDex.apk`. iOS launched on iPhone 17 Pro sim
- **DD** `Grok` 2026-08-14 — COMPLETED — Register — Build as a standing fleet seat (DealDex PR #41, fleet PR #26). Mac lane `~/apps/dealdex — build`. `fleet-apps.json` has — BUILD. AGENT-SYNC seat table still for Mac — (keepout this turn)
- **DD** `Grok` 2026-08-14 — COMPLETED — Onboarding links + subagent/economics wording (PR #40). AGENTS.md start-here table + stronger Delegation stanza. Docs only
- **DD** `Grok` 2026-08-14 — PLANNED — TestFlight + App Store + Play upload. Blocked on owner: ASC app record (SKU `dealdex`, Account Holder create) and Google Play Console credentials. Bundle ID `me.grok.dealdex` is registered. Prep landed in PR #56
- **PS** `Grok` 2026-08-14 — DEPLOYED — doximity.jaywedgeworth.com → public view profile. 301 to `https://www.doximity.com/profiles/3cb95815-2fd1-4985-94e5-3d6f932283bf/view`. `/cv/jaywedgeworth` opened edit mode. Verified live 301 after Cloudflare rule + cache purge
- **PS** `Grok` 2026-08-14 — DEPLOYED — Social short-link URL redirects on jaywedgeworth.com. Cloudflare Single Redirects (301) + dummy proxied `AAAA 100::`. doximity → view profile (see row above); facebook/fb → Facebook; instagram/ig → Instagram; x → X; linkedin → LinkedIn `/in/JayWedgeworth`
- **PS** `Grok` 2026-08-14 — COMPLETED — Onboard Personal-Site as a fleet app + About copy "included" (PR #1). AGENTS, board, static CI, effort-issues-sync. Snapshot uses "Earlier work included". Live Vercel project is not on the fleet MCP team, so production HTML is unchanged
- **AFC** `Grok` 2026-08-14 — COMPLETED — Onboard Personal-Site as a fleet app (PS). Personal-Site PR #1 + coordinator PR #28 merged. Social short-link 301s live. Live Vercel project is not on the fleet MCP team
- **AFC** `Grok` 2026-08-14 — COMPLETED — Onboarding links + subagent/economics wording. Fleet #25 + DealDex #40 merged. ST #2711 / CT #1859 / UM #1190 auto-merge armed. Live AGENT-SYNC + QUICKSTART + seat globals already updated
- **AFC** `Grok` 2026-08-14 — COMPLETED — Register — Build as a standing fleet seat (PR #26). Tag ` `, Notes name ` Build`, suffix ` `, prefix ` -build/`. DealDex PR #41 closed the app-side docs. AGENT-SYNC seat table still open for Mac
- **AFC** `Grok` 2026-08-14 — COMPLETED — Two spaces after every sentence, including App Store review notes (live `~/apps/AGENT-SYNC.md` + `FLEET-UI-COPY.md`; coordinator PR `grok/two-spaces-rule`). Owner: applies everywhere forever. CT App Store listing also rewritten (2-week trial, Executive Branch)
- **AFC** `Claude` `Grok` 2026-08-14 — COMPLETED — Master list of Mac local processes (`~/apps/MAC-LOCAL-PROCESSES.md`). LaunchAgents / cron / login items inventoried. Binding: every agent must add a row when they add a surviving process. `AGENT-SYNC.md` § Mac local processes. — remote-control is KeepAlive
- **AFC** `Grok` 2026-08-14 — COMPLETED — iOS fleet auto-ship 1h (`DEFAULT_MIN_INTERVAL_SEC=3600`). Runtime updated; ship-all includes usage-local. CT #1869 merged; UM #1195 merged; ST #2716 pin auto-merging

## 2026-08-13

*86 PRs merged · 43 issues opened · 25 issues closed · 16 effort rows*

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
- **DD** [#1](https://github.com/jaywedgeworth22/DealDex/pull/1): Join DealDex to the fleet: AGENTS, effort board, and CI _(by jaywedgeworth22)_
- **DD** [#3](https://github.com/jaywedgeworth22/DealDex/pull/3): Use npm install in CI until the lockfile is refreshed _(by jaywedgeworth22)_
- **DD** [#6](https://github.com/jaywedgeworth22/DealDex/pull/6): Remove the broken Auto Update PRs workflow _(by jaywedgeworth22)_
- **DD** [#9](https://github.com/jaywedgeworth22/DealDex/pull/9): chore(gitignore): protect Apple private keys with .p8 rule _(by jaywedgeworth22)_
- **DD** [#10](https://github.com/jaywedgeworth22/DealDex/pull/10): Show eBay and Mercari logos; document the ship path _(by jaywedgeworth22)_
- **DD** `Grok` [#12](https://github.com/jaywedgeworth22/DealDex/pull/12): Add — Build as a fleet seat _(by jaywedgeworth22)_
- **DD** `Grok` [#15](https://github.com/jaywedgeworth22/DealDex/pull/15): Sign this seat — BUILD, not _(by jaywedgeworth22)_
- **DD** `Claude` [#18](https://github.com/jaywedgeworth22/DealDex/pull/18): docs: iOS .md + xcodebuild-without-MCP rule _(by jaywedgeworth22)_
- **DD** [#20](https://github.com/jaywedgeworth22/DealDex/pull/20): Use official eBay and Mercari wordmarks _(by jaywedgeworth22)_
- **DD** [#22](https://github.com/jaywedgeworth22/DealDex/pull/22): Lock marketplace marks and remember scan history _(by jaywedgeworth22)_
- **DD** [#26](https://github.com/jaywedgeworth22/DealDex/pull/26): Widen raggy copy and restyle the guest line _(by jaywedgeworth22)_
- **DD** [#29](https://github.com/jaywedgeworth22/DealDex/pull/29): Let copy use the same width as the cards _(by jaywedgeworth22)_
- **DD** [#31](https://github.com/jaywedgeworth22/DealDex/pull/31): Put marketplace marks in chips and add phone Settings _(by jaywedgeworth22)_
- **DD** [#34](https://github.com/jaywedgeworth22/DealDex/pull/34): Straighten the JustTCG J _(by jaywedgeworth22)_
- **DD** [#37](https://github.com/jaywedgeworth22/DealDex/pull/37): Paint toggle wordmarks solid white _(by jaywedgeworth22)_
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
- **AFC** [#23](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/23): Add DealDex to the fleet and write app/agent onboard playbooks _(by jaywedgeworth22)_
- **AFC** [#24](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/24): docs: iOS agent build-loop policy (no Xcode MCP) _(by jaywedgeworth22)_

### Issues closed

- **DD** [#2](https://github.com/jaywedgeworth22/DealDex/issues/2): 2026-08-13 — IN PROGRESS — Fleet onboard: link ~/Code/DealDex to
- **DD** [#4](https://github.com/jaywedgeworth22/DealDex/issues/4): 2026-08-13 — COMPLETED — Fleet onboard merged (PR #1). ~/Code/DealDex is
- **DD** [#5](https://github.com/jaywedgeworth22/DealDex/issues/5): 2026-08-13 — IN PROGRESS — CI: npm ci fails on Node 22 lock drift
- **DD** [#7](https://github.com/jaywedgeworth22/DealDex/issues/7): 2026-08-13 — COMPLETED — Drop broken Auto Update PRs workflow
- **DD** [#8](https://github.com/jaywedgeworth22/DealDex/issues/8): 2026-08-13 — COMPLETED — CI uses npm install (PR #3). Main CI verify is
- **DD** [#11](https://github.com/jaywedgeworth22/DealDex/issues/11): 2026-08-13 — IN PROGRESS — Marketplace logos + ship path. eBay/Mercari
- **DD** [#13](https://github.com/jaywedgeworth22/DealDex/issues/13): 2026-08-13 — Build — COMPLETED — Join fleet as named seat. Seat table +
- **DD** [#14](https://github.com/jaywedgeworth22/DealDex/issues/14): 2026-08-13 — COMPLETED — Marketplace logos + ship path (PR #10)
- **DD** [#16](https://github.com/jaywedgeworth22/DealDex/issues/16): 2026-08-13 — COMPLETED — Join fleet as named seat. Seat table +
- **DD** [#17](https://github.com/jaywedgeworth22/DealDex/issues/17): 2026-08-13 — COMPLETED — Marketplace logos + ship path (PR #10)
- **DD** [#21](https://github.com/jaywedgeworth22/DealDex/issues/21): 2026-08-13 — IN PROGRESS — Official eBay + Mercari wordmarks. Swap
- **DD** [#23](https://github.com/jaywedgeworth22/DealDex/issues/23): 2026-08-13 — COMPLETED — Official eBay + Mercari wordmarks (PR
- **DD** [#24](https://github.com/jaywedgeworth22/DealDex/issues/24): 2026-08-13 — IN PROGRESS — Scan desk: lock logos, card frame
- **DD** [#27](https://github.com/jaywedgeworth22/DealDex/issues/27): 2026-08-13 — COMPLETED — Scan desk polish (PR #22). Locked
- **DD** [#28](https://github.com/jaywedgeworth22/DealDex/issues/28): 2026-08-13 — IN PROGRESS — Copy wrap + guest line. Stop skinny
- **DD** [#32](https://github.com/jaywedgeworth22/DealDex/issues/32): 2026-08-13 — COMPLETED — One page measure (PR #29). Copy and cards
- **DD** [#35](https://github.com/jaywedgeworth22/DealDex/issues/35): 2026-08-13 — COMPLETED — Chip toggles + phone Settings (PR #31)
- **DD** [#38](https://github.com/jaywedgeworth22/DealDex/issues/38): 2026-08-13 — COMPLETED — Straighten the JustTCG J (PR #34). Desk
- **UM** [#1170](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1170): Alert emails need (sent by Usage Monitor) footer
- **UM** [#1172](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1172): Prefer Pushover over Resend for alert delivery
- **UM** [#1176](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1176): GHPAT + iOS ship + land #1167 — IN PROGRESS 2026-08-13
- **UM** [#1183](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1183): 2026-08-14 — IN PROGRESS — Apex iCloud MX + receipts Worker catch-all
- **UM** [#1186](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1186): 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch
- **CTS** [#267](https://github.com/jaywedgeworth22/congress-trading-shared/issues/267): Land open PR queue — COMPLETED 2026-08-12
- **CTS** [#268](https://github.com/jaywedgeworth22/congress-trading-shared/issues/268): Cloud protocol bootstrap — COMPLETED

### Issues opened

- **CT** [#1826](https://github.com/jaywedgeworth22/Congress.Trade/issues/1826): 2026-08-12 — COMPLETED/MERGED (#1821 f204c688) — Fleet deploy-guard
- **CT** [#1827](https://github.com/jaywedgeworth22/Congress.Trade/issues/1827): 2026-08-12 — COMPLETED/MERGED (#1820 7634fe61) — Land remaining open PRs
- **CT** [#1828](https://github.com/jaywedgeworth22/Congress.Trade/issues/1828): 2026-08-12 12:25pm CT — COMPLETED/MERGED via #1820 (7634fe61;
- **CT** [#1829](https://github.com/jaywedgeworth22/Congress.Trade/issues/1829): 2026-08-12 — COMPLETED/MERGED (#1796 4e6371d8; closeout PR #1798
- **CT** [#1830](https://github.com/jaywedgeworth22/Congress.Trade/issues/1830): 2026-08-12 1:25pm CT — IN PR — Effort Issues Sync: the transport retry
- **CT** [#1831](https://github.com/jaywedgeworth22/Congress.Trade/issues/1831): 2026-08-12 — IN PROGRESS — iOS Directory/Trades/Trends chrome: Name sort
- **CT** [#1838](https://github.com/jaywedgeworth22/Congress.Trade/issues/1838): 2026-08-13 3:37pm CT — IN PROGRESS — CI and iOS ship never ran on
- **DD** [#2](https://github.com/jaywedgeworth22/DealDex/issues/2): 2026-08-13 — IN PROGRESS — Fleet onboard: link ~/Code/DealDex to
- **DD** [#4](https://github.com/jaywedgeworth22/DealDex/issues/4): 2026-08-13 — COMPLETED — Fleet onboard merged (PR #1). ~/Code/DealDex is
- **DD** [#5](https://github.com/jaywedgeworth22/DealDex/issues/5): 2026-08-13 — IN PROGRESS — CI: npm ci fails on Node 22 lock drift
- **DD** [#7](https://github.com/jaywedgeworth22/DealDex/issues/7): 2026-08-13 — COMPLETED — Drop broken Auto Update PRs workflow
- **DD** [#8](https://github.com/jaywedgeworth22/DealDex/issues/8): 2026-08-13 — COMPLETED — CI uses npm install (PR #3). Main CI verify is
- **DD** [#11](https://github.com/jaywedgeworth22/DealDex/issues/11): 2026-08-13 — IN PROGRESS — Marketplace logos + ship path. eBay/Mercari
- **DD** [#13](https://github.com/jaywedgeworth22/DealDex/issues/13): 2026-08-13 — Build — COMPLETED — Join fleet as named seat. Seat table +
- **DD** [#14](https://github.com/jaywedgeworth22/DealDex/issues/14): 2026-08-13 — COMPLETED — Marketplace logos + ship path (PR #10)
- **DD** [#16](https://github.com/jaywedgeworth22/DealDex/issues/16): 2026-08-13 — COMPLETED — Join fleet as named seat. Seat table +
- **DD** [#17](https://github.com/jaywedgeworth22/DealDex/issues/17): 2026-08-13 — COMPLETED — Marketplace logos + ship path (PR #10)
- **DD** [#19](https://github.com/jaywedgeworth22/DealDex/issues/19): 2026-08-13 — IN PROGRESS — iOS agent build-loop policy (branch
- **DD** [#21](https://github.com/jaywedgeworth22/DealDex/issues/21): 2026-08-13 — IN PROGRESS — Official eBay + Mercari wordmarks. Swap
- **DD** [#23](https://github.com/jaywedgeworth22/DealDex/issues/23): 2026-08-13 — COMPLETED — Official eBay + Mercari wordmarks (PR
- **DD** [#24](https://github.com/jaywedgeworth22/DealDex/issues/24): 2026-08-13 — IN PROGRESS — Scan desk: lock logos, card frame
- **DD** [#27](https://github.com/jaywedgeworth22/DealDex/issues/27): 2026-08-13 — COMPLETED — Scan desk polish (PR #22). Locked
- **DD** [#28](https://github.com/jaywedgeworth22/DealDex/issues/28): 2026-08-13 — IN PROGRESS — Copy wrap + guest line. Stop skinny
- **DD** [#30](https://github.com/jaywedgeworth22/DealDex/issues/30): 2026-08-13 — IN PROGRESS — One page measure. Copy and cards share
- **DD** [#32](https://github.com/jaywedgeworth22/DealDex/issues/32): 2026-08-13 — COMPLETED — One page measure (PR #29). Copy and cards
- **DD** [#33](https://github.com/jaywedgeworth22/DealDex/issues/33): 2026-08-13 — IN PROGRESS — Chip toggles + phone Settings
- **DD** [#35](https://github.com/jaywedgeworth22/DealDex/issues/35): 2026-08-13 — COMPLETED — Chip toggles + phone Settings (PR #31)
- **DD** [#36](https://github.com/jaywedgeworth22/DealDex/issues/36): 2026-08-13 — IN PROGRESS — Straighten the JustTCG J. Desk names
- **DD** [#38](https://github.com/jaywedgeworth22/DealDex/issues/38): 2026-08-13 — COMPLETED — Straighten the JustTCG J (PR #34). Desk
- **DD** [#39](https://github.com/jaywedgeworth22/DealDex/issues/39): 2026-08-13 — IN PROGRESS — White toggle wordmarks. Scan/alert
- **ST** [#2686](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2686): On-demand quote sheet drops fundamentals; fill/position cards only tap the logo
- **ST** [#2694](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2694): Durable litestream remote-inventory cache (PR #2665's
- **ST** [#2697](https://github.com/jaywedgeworth22/Socratic.Trade/issues/2697): Fix ST Litestream wedge and prefer Pushover over Resend
- **UM** [#1166](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1166): CI and iOS ship never ran on bot-merged PRs — IN
- **UM** [#1170](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1170): Alert emails need (sent by Usage Monitor) footer
- **UM** [#1172](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1172): Prefer Pushover over Resend for alert delivery
- **UM** [#1176](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1176): GHPAT + iOS ship + land #1167 — IN PROGRESS 2026-08-13
- **UM** [#1181](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1181): 2026-08-14 — IN PROGRESS — Backup restore-proof + honest gatesOverallOk
- **UM** [#1183](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1183): 2026-08-14 — IN PROGRESS — Apex iCloud MX + receipts Worker catch-all
- **UM** [#1186](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1186): 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch
- **UM** [#1188](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1188): 2026-08-14 — IN PROGRESS — Four Cloudflare provider rows (branch
- **CTS** [#267](https://github.com/jaywedgeworth22/congress-trading-shared/issues/267): Land open PR queue — COMPLETED 2026-08-12
- **CTS** [#268](https://github.com/jaywedgeworth22/congress-trading-shared/issues/268): Cloud protocol bootstrap — COMPLETED

### Effort board

- **UM** `Claude` CI and iOS ship never ran on bot-merged PRs — IN PROGRESS 2026-08-13 3:37pm CT (branch `monet/ci-ship-trigger-bot-merge`). A PR merged by `github-actions[bot]` lands on `main` and dispatches ZERO workflow runs: GitHub raises no workflow events for actions taken with `GITHUB_TOKEN`, and `auto-merge-prs.yml` arms auto-merge with exactly that token. PR #1145 (bot-me
- **UM** `Claude` 2026-08-13 3:37pm CT — IN PROGRESS — CI and iOS ship never ran on bot-merged PRs (branch `monet/ci-ship-trigger-bot-merge`). A PR merged by `github-actions[bot]` lands on `main` and dispatches ZERO workflow runs (GitHub raises no workflow events for `GITHUB_TOKEN` actions; `auto-merge-prs.yml` arms with that token). PR #1145 (bot, touches `ios/`) produced no `ios-ship` run; #1
- **UM** `Grok` GH_PAT + iOS ship + land #1167 — IN PROGRESS 2026-08-13 (branch `grok/um-ios-ship-ghpat`, isolation worktree). Set repo secret `GH_PAT` on UM/ST/CT from `GITHUB_ADMIN_PAT` (names only). Land #1167 backup-row copy. Expand `ios-ship.yml` iOS-touching paths. Mark #953 Oracle deleted-inode HISTORICAL. No TestFlight upload: host is macOS 27.0 beta (`26A5406e`); Xco
- **DD** `Grok` 2026-08-13 — COMPLETED — White toggle wordmarks (PR #37). Scan/alert source chips use solid white eBay/Mercari letters. Listing-row marks stay full color
- **DD** `Grok` 2026-08-13 — COMPLETED — Straighten the JustTCG J (PR #34). Desk names use Plex. Fraunces WONK=0
- **DD** `Grok` 2026-08-13 — COMPLETED — Official eBay + Mercari wordmarks (PR #20). Owner-supplied blue MERCARI mark replaces the red character. eBay four-color wordmark kept. Native Scan matches
- **DD** `Grok` 2026-08-13 — COMPLETED — Join fleet as named seat. Seat table + ` -build/` prefix. Preview lane is `/workspace`. Same PR/CI/merge loop as every other seat
- **DD** `Grok` 2026-08-13 — COMPLETED — Marketplace logos + ship path (PR #10). eBay/Mercari marks on scan, alerts, native. CONTRIBUTING documents GitHub `main` + one-time Vercel/Coolify import
- **DD** `Grok` `Claude` 2026-08-13 — COMPLETED — iOS agent build-loop policy (PR #18). `native/ios/CLAUDE.md` + AGENTS + — pbxproj hook. xcodebuild via bash is pre-approved
- **DD** `Grok` 2026-08-13 — COMPLETED — Drop broken Auto Update PRs workflow. `chinthakagodawita/autoupdate@v1.22.0` does not exist; it failed every main push. Revisit with the Usage-Monitor `gh pr update-branch` pattern if DealDex grows stacked PRs
- **DD** `Grok` 2026-08-13 — COMPLETED — CI uses npm install (PR #3). Main CI verify is green (lint/typecheck/test/build)
- **DD** `Grok` 2026-08-13 — COMPLETED — Fleet onboard merged (PR #1). `~/Code/DealDex` is `jaywedgeworth22/DealDex`. AGENTS.md, effort board, Slack `repo: DealDex` / `DD`
- **AFC** `Grok` 2026-08-21 — COMPLETED — lock-held restart storm. `ms` showed pm2 — `errored` (355 restarts). This TUI holds `~/.grok/leader.sock`. Watch skip was a no-op: LaunchAgent PATH omitted `/usr/sbin` and `lsof` lives only there. Stopped the job. Watch + plist PATH + `leader.sh` exit 75. Landed coordinator #74. ios-ship-now is the 2026-08-13 login leftover
- **AFC** `Grok` 2026-08-13 — COMPLETED — iOS agent build-loop policy (no Xcode MCP; bash xcodebuild pre-approved). Fleet #24 merged. DD #18 + UM #1178 merged. ST #2705 + CT #1850 auto-merge armed. Live `~/apps/AGENT-SYNC.md` already has the section
- **AFC** `Claude` `Grok` `Codex` `Cursor` `Gemini` 2026-08-13 9:00pm CT — COMPLETED — Attach XcodeBuildMCP to every agent platform. Added `npx -y xcodebuildmcp@latest mcp` (Sentry disabled, absolute `/opt/homebrew/bin/npx`) to , — CLI, , , , Copilot, official — Desktop, and Parall desktop configs. Clients must restart to load tools
- **AFC** `Grok` 2026-08-13 — COMPLETED — Onboard DealDex as a fleet app + write new-app/new-agent onboarding. `~/Code/DealDex` cloned to `jaywedgeworth22/DealDex`. DealDex PRs #1 + #3. Coordinator PR #23 (`docs/ONBOARDING-NEW-APP.md`, `docs/ONBOARDING-NEW-AGENT.md`, `fleet-apps.json`, digest/calendar/acronyms)

## 2026-08-12

*110 PRs merged · 28 issues opened · 37 issues closed · 15 effort rows*

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
- **AFC** [#19](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/19): feat(fleet): mobile push alerts, Needs Owner banners, and rich Slack cards _(by jaywedgeworth22)_
- **AFC** [#20](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/20): docs(fleet): TestFlight 1.0.N versioning policy, Central Time release notes, and mobile feedback instructions _(by jaywedgeworth22)_
- **AFC** [#21](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/21): docs(fleet): prohibit agent names in TestFlight release notes & format PR #s on Apple Notes timestamp row _(by jaywedgeworth22)_
- **CTS** `Codex` [#260](https://github.com/jaywedgeworth22/congress-trading-shared/pull/260): chore: standardize — Cloud coordination setup _(by jaywedgeworth22)_
- **CTS** [#262](https://github.com/jaywedgeworth22/congress-trading-shared/pull/262): chore(deps): bump anthropics/claude-code-action from 1.0.183 to 1.0.187 _(by dependabot[bot])_
- **CTS** [#264](https://github.com/jaywedgeworth22/congress-trading-shared/pull/264): fix(effort-sync): retry transport failures so one dropped response body cannot kill the run _(by jaywedgeworth22)_
- **CTS** [#266](https://github.com/jaywedgeworth22/congress-trading-shared/pull/266): docs(effort): close the landed #262/#260 PR queue _(by jaywedgeworth22)_

### Issues closed

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
- **AFC** [#22](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/22): Mac runner: Xcode 26 CI runners for CT/ST/UM + xcode.jays.services health endpoint

### Issues opened

- **CT** [#1804](https://github.com/jaywedgeworth22/Congress.Trade/issues/1804): 2026-08-12 12:22pm CT — IN PR — Effort Issues Sync: retry transient
- **CT** [#1805](https://github.com/jaywedgeworth22/Congress.Trade/issues/1805): 2026-08-12 ~8:20pm CT — COMPLETED — Open-issues resolve batch: dead
- **CT** [#1806](https://github.com/jaywedgeworth22/Congress.Trade/issues/1806): 2026-08-12 ~6:40pm CT — COMPLETED/APPLIED — iOS version naming is now
- **CT** [#1807](https://github.com/jaywedgeworth22/Congress.Trade/issues/1807): 2026-08-12 4:45am CT — MERGED (#1782, deployed via auto-merge)
- **CT** [#1808](https://github.com/jaywedgeworth22/Congress.Trade/issues/1808): 2026-08-12 2:05am CT — IN PR — Member photos: licence check widened
- **CT** [#1809](https://github.com/jaywedgeworth22/Congress.Trade/issues/1809): 2026-08-11 ~12:35pm CT — COMPLETED/DEPLOYED — Full — chat closeout +
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
- **AFC** [#22](https://github.com/jaywedgeworth22/ai-fleet-coordinator/issues/22): Mac runner: Xcode 26 CI runners for CT/ST/UM + xcode.jays.services health endpoint
- **CTS** [#265](https://github.com/jaywedgeworth22/congress-trading-shared/issues/265): Effort-sync transport-level retry — IN PR

### Effort board

- **UM** `Claude` [2026-08-12] PagerDuty alert correctness: false Twilio discrepancies + two permanent-strand paths — MERGED PR #1131 2026-08-12 (auto-deploys). PD #64/#70 were `usage_reconciliation_discrepancy` on two Twilio rows because the reconciler compared the real bill against ZERO pushed telemetry (delta = 100% of the bill; no tolerance short of 1.0 absorbs it) — `reportedEventCount === 0`
- **UM** `Claude` Effort-sync transport-level retry — IN PR 2026-08-12 (branch `claude/effort-sync-transport-retry`). `http_request` in `scripts/sync-effort-issues.py` caught only `urllib.error.HTTPError`, so transport failures escaped the function, never reached the rate-limit retry in `GitHubClient._request`, and killed the whole run (production: `IncompleteRead(714456 bytes read
- **UM** `Claude` [2026-08-12] Local key/config propagation bundle — MERGED PR #1145 (`9870d0ad`); Stripe legacy-payouts probe fix MERGED PR #1143. Keys travel Mac → encrypted .umkeys file → phone Keychain, never through a server API. Generator `scripts/local-keys-bundle.mjs` (list/build/verify, AES-256-GCM + PBKDF2 600k, value-blind, atomic 0600 writes, TOCTOU-safe fd-based passphrase read); pho
- **UM** `Claude` `Antigravity` [2026-08-12] — quota collector finished against the real CLI + launchd job live — MERGED PR #1100 (`469fc598`) + #1136 (`8ea014a4`). Picked up a cloud session's handoff (`docs/rollouts/2026-08-12 — local-agent-handoff.md`) that could not reach `agy`, Infisical, the host or Xcode. The guessed parser was wrong in two data-losing ways. Real `agy -p "/usag
- **UM** `Claude` [2026-08-12] R2 free-tier kill-switch: it is pinned in config, not held by usage — CHECKED (superseded by the 2026-08-13 row above). The persisted flag `/data/r2-disabled-70pct.flag` is absent; the switch is engaged purely through Coolify env vars `LITESTREAM_EMERGENCY_DISABLE=true` + `R2_WRITES_DISABLED=true`, set in both production and preview scopes. That answers th
- **UM** `Claude` [2026-08-12] Infisical card false alarm: probe bug + one stale secret — MERGED PR #1111 (`dd7883ef`) + value-blind sync run. Owner was right that Infisical worked; the probe was wrong twice. Verified live with hash-only comparisons: all four stored CLIENT_IDs match, and of the four stored CLIENT_SECRETs only Socratic Trade's was dead (401) — CT/Shared/Automation authenticate (id
- **UM** `Grok` 2026-08-12 — IN PR (#1160) / OPS DONE — UM Platforms CF/R2 false-degraded + PD #73/#74. Infisical fleet token copied into CT/ST/JAY/R2_USAGE. PD spend spikes resolved (expected ST SEC ingest). Sentry CONGRESS-TRADE-1 ignored (retired Worker cron)
- **UM** `Grok` Land open PR queue to production — MERGED 2026-08-12, deploy queued. Open UM count 0. #1094 hygiene `0c6329b4`, #1113 Anthropic/Kimi $200/mo + B2 Litestream tail probe `17831d32`, #1152 ESLint 9.39.5 + eslint-config-next 16.3.0 flat config `ff0364ee` (superseded Dependabot #1070/#1071). Coolify webhook deploys queued to main HEAD `ff0364ee`
- **UM** `Grok` [FLEET] R2 archive creds live-check — PARTIAL 2026-08-12. UM first weekly archive verified (`weekly/prod-2026-08-12T23-57-10Z.db.gz`, `/api/ready` weeklyArchive.ok); Coolify cron `0 4 0`. ST `AWS_R2_HISTORIC_`/`R2_ARCHIVE_` LIST 200, cold-snapshots/app-2026-08-09.db present. CT `R2_ARCHIVE_` is the revoked shared CLOUDFLARE_R2 key (401) and congress-trade is exited:unhealth
- **UM** `Claude` [2026-08-12] PagerDuty alert correctness: false Twilio discrepancies + two permanent-strand paths — MERGED PR #1131 2026-08-12 (auto-deploys). PD #64/#70 were `usage_reconciliation_discrepancy` on two Twilio rows because the reconciler compared the real bill against ZERO pushed telemetry (delta = 100% of the bill; no tolerance short of 1.0 absorbs it) — `reportedEventCount === 0
- **UM** `Grok` iOS R2 Historic false-green + Client ops timeouts + 0.1.0 version — MERGED PR #1124 2026-08-12 (`418b2f3c`, issue #1123). Historic R2 no longer reports ok when the weekly archive is missing/stale; iOS shows Lagging instead of a green "weekly freeze". Client ops GETs use 60s; server overlaps/parallelizes the Coolify+R2+B2 fan-out and serves stale operations on refre
- **CTS** `Grok` `Claude` `Codex` Land open PR queue — COMPLETED 2026-08-12. Squash-merged #262 (`976e73e`, — code-action 1.0.183→1.0.187) after update-branch; prior verify fail was the pre-existing nanoid audit, already fixed on main (3.3.18). Squash-merged #260 (`ebe1f95`, — Cloud coordination) after update-branch + review fixes (`d5d923d`: Slack `ok:true` check, `[Congress-Tra
- **CTS** `Codex` `Grok` Cloud protocol bootstrap — COMPLETED 2026-08-12 — land. PR #260 merged as `ebe1f95`. Repo-local `.codex/setup.sh` / `.codex/maintenance.sh`, `scripts/codex-coordination.sh`, and Apple Notes cloud handoff. Review threads resolved before merge
- **AFC** `Grok` 2026-08-12 — IN PROGRESS — Mac Xcode runner does not update the phone. Runners were online but only unsigned-compile (`ios-build.yml`; ST PR #2648 not on main). TestFlight shipping was ad-hoc. ST latest builds stuck `MISSING_EXPORT_COMPLIANCE` (patched live to IN_BETA_TESTING). Adding `ios-ship.yml` on the Mac runners + ship-script compliance auto-declare + ST min iOS 17. Worktre
- **AFC** `Claude` `Grok` 2026-08-12 — COMPLETED — Mac disk: pruned 8.3GB ( sessions >7d, npm npx/cache, Xcode DerivedData, 3 finished worktrees). Data volume 90%→88% (42→50GB free). Left live: last-7-day — sessions (2.8GB), worktrees (~6GB), CoreSimulator (4.4GB, needed for iOS), Mac iOS runners (1.6GB, live). Added 7-day session prune + npx wipe to `~/apps/mac-auto-cleanup.sh`

## 2026-08-11

*89 PRs merged · 19 issues opened · 4 issues closed · 12 effort rows*

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
- **AFC** [#18](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/18): docs(fleet): Apple Notes pin/unpin shortcut instructions & universal fleet processes _(by jaywedgeworth22)_
- **CTS** [#261](https://github.com/jaywedgeworth22/congress-trading-shared/pull/261): chore(deps-dev): bump publint from 0.3.22 to 0.3.23 _(by dependabot[bot])_
- **CTS** [#263](https://github.com/jaywedgeworth22/congress-trading-shared/pull/263): feat(release): 2.5.2 — TxType B/S/E coercion, sub-$1k bracket tier, TransactionsQueryInput export _(by jaywedgeworth22)_

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
- **UM** `Claude` [2026-08-11] iOS Swift test suite green + one real product bug — MERGED PR #1101 (`78f13bf7`) + #1102 (`5597afe9`). `UsageMonitorKitTests` had not compiled for some time and nothing in CI runs Swift tests, so the breakage was invisible — the app builds fine. The fix was sitting UNCOMMITTED in the `grok/mac-tf-xcode-app-ship` worktree; landed it. Repairing the target exposed 22
- **UM** `Claude` [2026-08-11] Platforms tab (all-platform infra status) + iOS full web parity — MERGED PR #1099 / squash `bdf68941`. New `/platforms` web section + iOS Platforms tab over a registry of 23 credential-gated probes across 8 categories (hosting, edge, storage, observability, developer, messaging, payments, secrets); unconfigured platforms render a calm "not configured" card naming the
- **UM** `Grok` App Store submit Client+Local — WAITING_FOR_REVIEW 2026-08-11. Builds Client `202608110228` + Local `202608110240` attached; listing/screenshots/privacy/content rights pushed; both review submissions submitted (~17:37Z). May still flip INVALID_BINARY if Apple rejects beta-host binaries (macOS 27 / min iOS 26). Monitor ASC
- **UM** `Grok` [2026-08-11] Effort hygiene closeout — COMPLETED. Closed stale in-progress GitHub mirrors whose PRs were already on main: issues #1086 #1085 #1084 #1083 #1082 #1067 #1064 #1054 #1052 #1050 #1048 #1034 #1031 #1019 #1011 #1006 #1003 #992 #990 #980 #979 (state_reason=completed, each cites merge PR/sha). Left open: Invalid Binary (board-only residual), #953 P0 SQLite, #981 receipt-inb
- **UM** `Grok` ST OOM + Coolify/ST ops visibility — COMPLETED/DEPLOYED 2026-08-11 PR #1077 (`e94bcf6464b3`). Full ST health + Coolify fleet Operations card; host OOM/backup ops. Issues #1084 + duplicate OOM rows closed out of In Progress
- **UM** `Grok` Default light theme — COMPLETED/DEPLOYED 2026-08-11 PR #1078 (`3d04f45ccfde`) + two-spaces #1079. Web+iOS light default. Issue #1083 closed
- **UM** `Grok` [2026-08-11] Fleet backups + host prevention indicators LANDED (#1080/#1081). Local iOS 202608110223 uploaded (ITS encryption+app group); 1.0.0 PREPARE_FOR_SUBMISSION with new build. Prod UM restarted for HCLOUD_TOKEN; Host Stats live. — COMPLETED
- **UM** `Grok` iOS Client Monitor backup layers + host usage — DEPLOYED 2026-08-11 2:29am CT. Prod `/api/ready` backupLayers local/B2/R2 OK; Infisical HCLOUD_TOKEN + COOLIFY_SERVER_STATS wired; `/api/server-metrics` live (cx43 ~26% CPU, UM self healthy). TestFlight 1.0.0 (202608110228) uploaded for `services.jays.usage.client.monitor`. PR #1075
- **UM** `Grok` Local Invalid Binary fix (App Groups profiles + PrivacyInfo + re-ship) — OPEN 2026-08-11. Portal profiles regenerated (groups fixed); PrivacyInfo shipped; TF VALID. App Store review still Invalid Binary — host is macOS 27 beta (`BuildMachineOSBuild=26A5353q`); owner must rebuild on stable macOS/Xcode Cloud. Rollout note in repo. (PR #1090 closed unmerged; invest
- **AFC** `Antigravity` Apple Notes Pin/Unpin shortcut & fleet processes documentation — COMPLETE 2026-08-11. PR created/merged. Detailed System Settings App Shortcut (⌘⌥P) & headless macOS Shortcuts (Pin Coding Note) instructions; universal fleet coordination processes (Slack sync, 3-way claim/closeout, branch/PR/auto-merge, model economics, secrets, outages, context continuity);

## 2026-08-10

*85 PRs merged · 33 issues opened · 7 issues closed · 5 effort rows*

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
- **AFC** [#17](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/17): style(digest): legend 2-col table layout + Created spacing _(by jaywedgeworth22)_

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

- **UM** `Grok` Coolify B2 replica heartbeat — COMPLETED/DEPLOYED 2026-08-10 PR #1072 (`71e7607e592a`). Live B2 fine; in-container heartbeat + Coolify probe; `replicaOk=true`. Issue #1086 closed
- **UM** `Grok` OpenRouter credit probe + UptimeRobot — COMPLETED/DEPLOYED 2026-08-10 PR #1066 (`9ce94e707df8`). `GET /api/openrouter-credits`. Issue #1067 closed
- **UM** `Grok` ASC store listing + screenshots + App Store prep (Client + Local) — COMPLETED 2026-08-10 2:10pm CT. PR #1073 merged. ASC en-US copy/categories/age/review/builds + 20 screenshots COMPLETE. Public /privacy+/support shipped. Submit for Review still owner gate
- **AFC** `Grok` `Claude` 2026-08-10 2:03am CT — DEPLOYED — Box disk hygiene + health-recover hardening ( handoff). Added `scripts/ops/box-disk-hygiene.{sh,service,timer}` (30min: df + SQLite/WAL sizes + docker system df; light prune when ok; builder+image prune-af at ≥80% used or <15G free; aggressive system prune at ≥90%/<8G; skips during Coolify builds; no volume prune by default). Installed+enabl
- **AFC** `Grok` digest legend 2-col layout + Created spacing — COMPLETE 2026-08-10. PR #17. Hidden 2-col legend (Repos/Agents | chips); extra margin after Created lede. Live on activity.jays.services after Pages

## 2026-08-09

*29 PRs merged · 11 issues opened · 3 issues closed · 4 effort rows*

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
- **AFC** `Grok` [#15](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/15): docs(fleet): Apple Notes [APP, Agent] + timestamp standard _(by jaywedgeworth22)_
- **AFC** [#16](https://github.com/jaywedgeworth22/ai-fleet-coordinator/pull/16): style(digest): polish activity site UI _(by jaywedgeworth22)_

### Issues closed

- **CT** [#1609](https://github.com/jaywedgeworth22/Congress.Trade/issues/1609): 2026-08-09T22:55Z — COMPLETED — Senate 5-year historical backfill
- **CT** [#1612](https://github.com/jaywedgeworth22/Congress.Trade/issues/1612): 2026-08-10T02:30Z — IN PROGRESS (pipeline draining) — 5-year/3-branch
- **CT** [#1614](https://github.com/jaywedgeworth22/Congress.Trade/issues/1614): 2026-08-09 — IN PR (auto-merge intended) — Owner web/iOS UX punchlist

### Issues opened

- **CT** [#1591](https://github.com/jaywedgeworth22/Congress.Trade/issues/1591): 2026-08-09 — DEPLOYED — Lane 2: deterministic-only stuck-filing
- **CT** [#1598](https://github.com/jaywedgeworth22/Congress.Trade/issues/1598): 2026-08-09 — IN PR (auto-merge enabled) — Icon/tooltip color fixes
- **CT** [#1601](https://github.com/jaywedgeworth22/Congress.Trade/issues/1601): 2026-08-09T22:21Z — IN PROGRESS — Social OG share image light refresh
- **CT** [#1604](https://github.com/jaywedgeworth22/Congress.Trade/issues/1604): Senate ingestion relay depends on an ephemeral tunnel + one agent's Mac staying on
- **CT** [#1609](https://github.com/jaywedgeworth22/Congress.Trade/issues/1609): 2026-08-09T22:55Z — COMPLETED — Senate 5-year historical backfill
- **CT** [#1612](https://github.com/jaywedgeworth22/Congress.Trade/issues/1612): 2026-08-10T02:30Z — IN PROGRESS (pipeline draining) — 5-year/3-branch
- **CT** [#1614](https://github.com/jaywedgeworth22/Congress.Trade/issues/1614): 2026-08-09 — IN PR (auto-merge intended) — Owner web/iOS UX punchlist
- **CT** [#1616](https://github.com/jaywedgeworth22/Congress.Trade/issues/1616): 2026-08-09 — COMPLETED/MERGED (#1613) — Owner web/iOS UX punchlist
- **CT** [#1618](https://github.com/jaywedgeworth22/Congress.Trade/issues/1618): 2026-08-09 9:30pm CT — IN PROGRESS (pipeline draining)
- **CT** [#1619](https://github.com/jaywedgeworth22/Congress.Trade/issues/1619): 2026-08-09 5:55pm CT — COMPLETED — Senate 5-year historical backfill
- **UM** [#1064](https://github.com/jaywedgeworth22/Usage-Monitor/issues/1064): Mobile nav brand label always visible ("Usage Monitor") — IN PR #1063

### Effort board

- **UM** `Grok` Mobile nav brand always visible — COMPLETED/DEPLOYED 2026-08-09 PR #1063 (`0351c5466848`). Issue #1064 closed
- **AFC** `Grok` activity.jays.services digest UI polish (legend/icons/title/dates) — COMPLETE 2026-08-09. PR #16 merged. Icon-only ST/CT/UM apps, agent under repo, ICS - daily/per commit, long-form dates, Created subheading, title Jay's Daily Log, legend spacing. Live after Pages refresh / activity.jays.services
- **AFC** `Grok` Short-link DNS redirects (activity/github/x/fb/ig) — COMPLETE 2026-08-09. Cloudflare Single Redirects + proxied AAAA `100::` on `jays.services` + `jaywedgeworth.com`: activity→fleet digest, github→github.com/jaywedgeworth22, x/fb/ig→JayWedgeworth socials
- **AFC** `Grok` sync updated policies (Infisical/Coolify secrets, Apple Notes close-out, FLEET-UI-COPY) — COMPLETE 2026-08-09. Landed on main `6a33f30`. AGENT-SYNC: Infisical sole-source + Coolify token split + Infisical CLI forbid; EFFORT-LOG-PROTOCOL Apple Notes close-out parity; TEMPLATE-AGENTS + README pointers; vendored FLEET-UI-COPY.md

## 2026-08-08

*56 PRs merged · 26 issues opened · 6 issues closed · 0 effort rows*

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

- **CT** [#1526](https://github.com/jaywedgeworth22/Congress.Trade/issues/1526): 2026-08-08T14:49Z — IN PR (auto-merge enabled) — iOS entity
- **CT** [#1527](https://github.com/jaywedgeworth22/Congress.Trade/issues/1527): 2026-08-08 — PR OPEN (auto-merge queued) — Server-side asset
- **CT** [#1530](https://github.com/jaywedgeworth22/Congress.Trade/issues/1530): 2026-08-08 — IN PR — Members directory dedupe + perf (#1452, #1454)
- **CT** [#1534](https://github.com/jaywedgeworth22/Congress.Trade/issues/1534): 2026-08-08T16:29Z — IN PR (auto-merge enabled) — Design convergence
- **CT** [#1536](https://github.com/jaywedgeworth22/Congress.Trade/issues/1536): 2026-08-08 — COMPLETED — Owner UX work-order wave + review-issue fixes
- **CT** [#1556](https://github.com/jaywedgeworth22/Congress.Trade/issues/1556): 2026-08-09 — MERGED (162163b2) — Apple backend: Sign in with Apple +

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
- **CT** [#1552](https://github.com/jaywedgeworth22/Congress.Trade/issues/1552): 2026-08-09 — IN PR (auto-merge enabled) — Web owner follow-up batch #2
- **CT** [#1556](https://github.com/jaywedgeworth22/Congress.Trade/issues/1556): 2026-08-09 — MERGED (162163b2) — Apple backend: Sign in with Apple +
- **CT** [#1559](https://github.com/jaywedgeworth22/Congress.Trade/issues/1559): 2026-08-09 — IN PR (auto-merge enabled) — iOS Sign in with Apple +
- **CT** [#1563](https://github.com/jaywedgeworth22/Congress.Trade/issues/1563): 2026-08-09 — IN PR (auto-merge enabled) — SECURITY: Apple JWS x5c full
- **CT** [#1567](https://github.com/jaywedgeworth22/Congress.Trade/issues/1567): 2026-08-09 — IN PR (auto-merge enabled) — Trades-tab count accuracy (3
- **CT** [#1571](https://github.com/jaywedgeworth22/Congress.Trade/issues/1571): 2026-08-09T03:57Z — IN PROGRESS — Hi-res brand lockup + white-letter
- **CT** [#1574](https://github.com/jaywedgeworth22/Congress.Trade/issues/1574): One-time backfill: reconcile 547 filings rows desynced from resolved review_queue state
- **CT** [#1575](https://github.com/jaywedgeworth22/Congress.Trade/issues/1575): scanned_pdf corpus needs vision/OCR extraction — deliberately out of scope for the deterministic autonomy fix
- **CT** [#1576](https://github.com/jaywedgeworth22/Congress.Trade/issues/1576): Data hygiene: delete manual test-probe row S — should-not-exist-zzzz from prod filings
- **CT** [#1577](https://github.com/jaywedgeworth22/Congress.Trade/issues/1577): Check whether the House bulk FD ZIP fetch is degraded (186 persisted rows stuck filed_date-NULL past catch-up window)
- **CT** [#1578](https://github.com/jaywedgeworth22/Congress.Trade/issues/1578): 2026-08-09 — IN PR (auto-merge enabled) — Review-queue false "all done"
- **CT** [#1580](https://github.com/jaywedgeworth22/Congress.Trade/issues/1580): 2026-08-09 — IN PR (auto-merge enabled) — Ingestion pipeline autonomy
- **CT** [#1587](https://github.com/jaywedgeworth22/Congress.Trade/issues/1587): 2026-08-09T04:33Z — COMPLETED/DEPLOYED — Trades pager + autonomous
