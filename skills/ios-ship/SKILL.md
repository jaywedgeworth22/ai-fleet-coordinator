---
name: ios-ship
description: Build, screenshot, and TestFlight-ship fleet iOS clients with bash xcodebuild/simctl — never Xcode MCP. Use for Socratic.Trade, Congress.Trade, Usage Monitor (client + local), or DealDex native UI, simulator QA, archives, or ASC listing copy.
---

# iOS agent loop (Universal)

Owner 2026-08-13: do **not** stand up, debug, or narrate Xcode MCP (`XcodeBuildMCP`, `xcrun mcpbridge`, `build_sim`).  `xcodebuild` and `xcrun simctl` via bash are pre-approved.  Run them.  Do not ask permission.

## Build / run / screenshot

Discover simulators — do not hardcode a device name:

```bash
xcrun simctl list devices available
```

XcodeGen apps (ST `ios/project.yml`, UM `ios/UsageMonitor/project.yml`, DealDex `native/ios/project.yml`): edit `project.yml`, then `xcodegen generate`.  CT iOS is **not** XcodeGen (`clients/ios/CongressTrade.xcodeproj`) — still do **not** hand-edit `.pbxproj`, xibs, storyboards, or entitlements; create the `.swift` file and report that it needs target membership.

Stable Xcode only: `/Applications/Xcode.app`, never `Xcode-beta`.

A user-visible client change is not done until a simulator screenshot exists (`xcrun simctl io booted screenshot …`).  `BUILD SUCCEEDED` is not visual QA.  Capture in **light** theme unless the owner asked for dark.

## Architecture defaults (unless the file already differs)

- `@Observable` + `@MainActor` on stores (never `ObservableObject`)
- `NavigationStack` + value-based `NavigationLink` (never `NavigationView` / destination-closure links)
- Light is the product default
- Two spaces between sentences in every human-readable string, including ASC fields
- iOS root screens: `.navigationBarTitleDisplayMode(.inline)`

## Apps (from `~/apps/ios-fleet/README.md`)

| Key | Display | Bundle | Scheme | Project |
|-----|---------|--------|--------|---------|
| `socratic` | Socratic.Trade | `trade.socratic.app` | `SocraticTrade` | `ios/Socratic Trade.xcodeproj` |
| `congress` | Congress.Trade | `trade.congress.ios` | `CongressTrade` | `clients/ios/CongressTrade.xcodeproj` |
| `usage` | Usage Client Monitor | `services.jays.usage.client.monitor` | `UsageMonitor` | `ios/UsageMonitor/UsageMonitor.xcodeproj` |
| `usage-local` | Usage Local Monitor | `services.jays.usage.local.monitor` | `LocalUsageMonitor` | same xcodeproj (free / no server) |
| `dealdex` | DealDex | `online.dealdex` (Android stays `me.grok.dealdex`) | `DealDex` | `native/ios/DealDex.xcodeproj` (XcodeGen `native/ios/project.yml`).  **No ASC app record yet — do not TestFlight until the owner creates SKU `dealdex`.** |

Per-app notes: `ios/CLAUDE.md`, `clients/ios/CLAUDE.md`, or `native/ios/CLAUDE.md`.

## Version + TestFlight notes

Patch increment `1.0.N` on **every** TestFlight upload.  Never reuse a version string.  Legacy `0.x.x` is banned.

Release notes **must not** contain agent names (`Monet`, `Claude`, `Grok`, …).

```text
[1.0.5] Usage-Monitor Update
Released: Mon, Aug 12, 2026 at 1:15 AM CT · PR #1065

What's New:
- Added live server status widget to Settings tab
- Fixed token expiration refresh handler
```

Two ASCII spaces between sentences in multi-sentence notes.  Timestamps America/Chicago, labeled `CT`.

ASC listing copy must match live product truth (CT covers House, Senate, **and** Executive Branch / OGE 278-T; Premium trial is **2 weeks** as of 2026-08-14, not a leftover 1-month).  See `owner-copy`.

## Ship

Signing last-mile: `scripts/ios-ship-testflight.sh` + `/Users/jay/apps/ios-fleet/README.md`.  Do not debug code-signing by guessing.  ASC `.p8` lives under `~/.secrets/` — `secret-handoff` before you touch it.

Mac Xcode ship runners are **not** the banned Mac PR-check runners.  Do not "fix CI" by turning on `trading-live-mac-ci`.

## Canon

- `/Users/jay/apps/AGENT-SYNC.md` § iOS agent build loop; App Versioning & TestFlight
- `/Users/jay/apps/ios-fleet/README.md`
- `/Users/jay/apps/FLEET-UI-COPY.md`
- Skills: `owner-copy`, `secret-handoff`, `apple-notes`
