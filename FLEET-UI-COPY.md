# Fleet UI copy conventions (owner, 2026-08-07)

Binding for **Socratic.Trade**, **Congress.Trade**, **Usage Monitor**, **DealDex**, **Personal-Site**, and **Autorotate (formerly TopSpin)** — web + iOS.



## Theme default = light (owner ruling 2026-08-10 — ALL apps, ALL agents)

Owner: default UI theme is **light**. Agents keep inventing dark-first or
"system" defaults that land on dark because the Mac is dark — stop that.

- **Default for first visit / no stored preference:** always **light**.
- **Do not** boot into dark from `prefers-color-scheme` unless the user has
  explicitly chosen **System** (or Dark).
- Dark remains an **optional** user choice via Light | Dark | System (or
  equivalent) — never the product default.
- **Screenshots / ASC / marketing / design previews:** capture in **light**
  mode unless the owner explicitly asks for dark. Existing ASC packs that
  are already light do not need a redo for this rule alone.
- Applies to Socratic.Trade, Congress.Trade, Usage Monitor, DealDex, Personal-Site, and Autorotate (formerly TopSpin) (web + iOS).
- Do not "make it look cool" with dark chrome by default. Light is correct.

## Proper nouns

- **Congress** and **Congressional** always take a capital **C** (U.S. proper nouns) in product copy, App Store text, and UI.
- Brand: **Congress.Trade**. Display URLs may use `https://Congress.Trade` (hostnames are case-insensitive; DNS/cert still resolve).
- Brand: **DealDex**. Do not reintroduce retired product names in user-facing copy.
- Keep technical identifiers lowercase: `trade.congress.ios`, `congress.trade` event names, email local-parts as configured.
## Headings / titles / buttons
Use **Title Case** (capitalize main words):
- Examples: `Agent Controls`, `Run Once`, `Win Rate`, `Needs Attention`,
  `Pending Proposals`, `Review 2 Proposals`, `Current Policy`,
  `Connected Accounts`, `Delete Account`, `Price Alerts`, `Last Run`,
  `Backend Remains Authoritative`, `Portfolio Brief`, `User Info`.

## Values / answers / secondary status (right side of labeled rows, subtitles that are data)
Use **sentence case or lowercase** — not Title Case:
- Examples: `not reported`, `ask-first`, `intraday`, `not scheduled`,
  `every 60 min`, `open holdings`, `none waiting`,
  `account return minus SPY…` (lowercase leading **a**).

## Special cases
- **Latency vs other providers (CT, 2026-08-16):** never print `+` or `−` on
  lead/lag.  Positive seconds means we published first.  Say **earlier**
  (green) or **later** (red), plus the magnitude (`13.0h earlier`,
  `5.7h later`).  Later is always red.  Earlier is always green.
- `vs SPY` — leave as-is (exception to value casing).
- `Use` buttons — short; leave as `Use`.
- Prefer **not** saying “Live” for account reality. All connected accounts are real money.
  Paper only: `Alpaca (paper)` with lowercase **p**. No “Live” dots/pills next to account rows.
- Market session banner (when shown): stream glyph + **`Market Closed`** / **`Market Open`**
  (not bare `Closed` alone if redundant with a Markets card).

## Times and dates (owner 2026-08-09, amended 2026-08-12, strengthened 2026-08-22)
- **Product UI renders in the VIEWER's device timezone** — iOS, browser, desktop.  A user in
  another zone reading their own trade times in Central would be the bug, not the fix.
- **Two deliberate exceptions, both about accounting honesty, not localization:**
  - Console surfaces that pin a **market-day boundary** stay `America/Chicago`
    (`app/console/lib/format.ts`), because they must agree with the day boundary the P&L
    accounting itself uses (`startOfDayInTimeZone`, `src/lib/db-execution.ts`).  A "today"
    that means a different day than the numbers under it is wrong.
  - **Market-session times** are the market's, not the viewer's: say `9:30 AM ET`, labeled.
- **Always label the zone** when a time could be read in more than one (`2:41 PM CT`,
  `9:30 AM ET`).  Relative times (`3m ago`) need no label.
- Owner-facing agent writing (chat, boards, rollouts, Slack, Notes, release notes) is
  **Central Time, labeled**.  Never UTC-only when telling the owner a time.  UTC may follow
  in parentheses after the Central stamp.  `00:00 UTC` is 7:00 PM CT the previous calendar
  day in CDT (6:00 PM CT in CST).  That is a coordination rule, not a UI one.  See
  `/Users/jay/apps/AGENT-SYNC.md` § Timestamps: Central Time.

## Money
- Compact suffixes **lowercase**: `$99.8k`, `$1.2m`, `$3.4b`.
- Home / hero equity (and places with room): **full** currency `$99,812.34`, not compact.

## iOS navigation titles
Always `.navigationBarTitleDisplayMode(.inline)` (small, centered) on root tab screens —
**not** large left-aligned titles that collapse only after scroll.

## Congress.Trade — no asset-class dropdown (owner 2026-08-14)

Do **not** add an All Assets / Public Equities, Funds, & ETFs / Stocks and ETF
dropdown on web or iOS.  It is worthless, unused, and a waste of space.
Never reintroduce it.  The server `assetClass=` param may stay for API clients;
the public UI must not grow a control for it.

## Congress.Trade — store listing and corpus accuracy (owner 2026-08-14)

The product corpus is **House, Senate, and Executive Branch** (OGE 278-T), not
Congress alone.  App Store description, promotional text, keywords, review
notes, IAP review notes, OG/RSS, and in-app blurbs must say so.  Do not write
“Congressional trades” or “House and Senate” as if that were the whole feed
(fixed 2026-08-13 in-app; App Store listing caught 2026-08-14).

Premium trial copy must match the live App Store introductory offer:
**2 weeks** (`FREE_TRIAL` / `TWO_WEEKS` on `trade.congress.premium.monthly`
and `.annual`).  Never ship leftover “1-month” / “1 month” trial text.

## Ticker logos
Show company logos next to ticker symbols wherever symbols appear (positions, orders,
watchlist, fills, proposals, scan tables). Fall back to monogram; never leave a blank hole.
Same open icon source as ST: `ticker-logos` / app logo proxy.

## What is NOT in scope
- Code identifiers, API enums, log lines, internal “live stream” engineering labels
  (SSE, live snapshot) unless user-facing product chrome.

## Two spaces between sentences (owner rule 2026-08-08, strengthened 2026-08-10 and 2026-08-14 — ALL agents, ALL contexts)

Owner: **two spaces between sentences everywhere, including App Store
submission fields.**  Not optional.  Not “web only.”  Not “UI only.”
**Every single agent, every app, every surface, forever.**

**Strengthened again 2026-08-19 (owner, in-conversation):** "For any and all paragraphs in
any context, always use 2 spaces to separate a period from the beginning of a new sentence."
This closes the last loophole -- the rule is NOT limited to product/user-facing copy.  It
covers every paragraph an agent writes anywhere: **chat replies to the owner**, PR titles and
bodies, commit messages, Slack posts to #agent-sync, Apple Notes, effort-board rows, rollout
notes, review reports and design docs.  If it is prose, it gets two spaces.  (Single space
remains correct after a non-terminal abbreviation -- "e.g.", "v1.2.3".  In HTML preserve the
gap with NBSP+space or SENTENCE_GAP, since raw double spaces collapse.  In Markdown, note that
two spaces at the END of a line is a hard line break -- a different thing; this rule is about
the gap BETWEEN sentences.)

**HOW to emit it so it's actually visible (verified 2026-08-19, Socratic.Trade
PR #2893):** intent is not enough, the gap has to survive the renderer.  In a
**chat reply** (Claude Code terminal/desktop transcript, any agent chat UI), type
the literal HTML entity text `&nbsp;` right after the period, then a normal space
— `Sentence one.&nbsp; Sentence two.` — the markdown renderer expands the entity
into a visibly wider gap.  Tested and confirmed NOT to work in chat: two literal
spaces (collapsed by GitHub-flavored markdown); a raw U+00A0 character typed
directly (normalized away in the transcript view even though copy-paste out of it
can look right).  In a **file** (read as source, never through that renderer),
literal two ASCII spaces stays correct — do not switch file content to NBSP or
`&nbsp;`.  **Exception: Apple Notes `--html` and any other HTML a renderer
will show.**  Notes.app is an HTML renderer, so write
`Sentence one.&nbsp; Sentence two.`  Two ASCII spaces in a `<p>` collapse.

**Rendering trap -- SOLVED 2026-08-19, owner-verified.  How to actually emit the gap:**

- **Agent chat replies** (Claude Code terminal / desktop transcript): use the HTML entity
  `&nbsp;` immediately after the period, then a normal space --
  `Sentence one.&nbsp; Sentence two.`  The markdown renderer expands the entity, so the double
  gap is VISIBLE to the owner.
- **Files** -- repo markdown/text, commit messages, PR titles and bodies, Slack posts,
  effort-board rows, code comments: two LITERAL spaces.  These are read as source; an
  entity would appear as literal text.
- **HTML that a renderer will show** (Apple Notes `--html`, in-app HTML/JSX/SwiftUI):
  `Sentence one.&nbsp; Sentence two.`  Notes.app is an HTML renderer — two ASCII
  spaces in a `<p>` collapse to one.  The notes helper converts leftover ASCII
  doubles after `.`/`!`/`?` into `&nbsp; `.

**What does NOT work, all tested in front of the owner:** two literal spaces in chat (GFM
collapses the run when rendering); a raw U+00A0 character in chat (normalized away in the view,
even though copy-paste showed two spaces -- do not be fooled by copy-paste); app settings (none
exist -- `outputStyle` changes tone only, `--output-format` is headless `claude -p` only,
`axScreenReader` only drops borders); patching the client (the CLI is a ~277MB compiled Mach-O
binary, the desktop app is a signed native bundle -- patching breaks code signing and is wiped by
auto-update; do not attempt).

**Process lesson that cost four rounds of owner correction:** when an instruction appears not to
take effect, diagnose the RENDERING/transport layer between you and the reader -- and ask what
they actually see on screen -- before restating a promise to comply.  Repeating "fixed" on output
the reader cannot see reads as ignoring them.

Caught live 2026-08-14: Congress.Trade App Store **review notes** still said
“1-month free trial” with single spaces after periods, while the description
already said 2 weeks.  Agents had treated review notes as exempt.  They are
not.

**Where it applies (non-exhaustive — if a human reads it, use two spaces):**
- In-app UI strings (web, PWA, iOS native, widgets)
- **App Store Connect — all of it:** description, promotional text, What’s New,
  **App Review notes**, **subscription / IAP review notes**, subscription
  localization descriptions, support/marketing blurbs
- Push / email / Slack-to-owner product copy / help / privacy / terms prose
- Apple Notes completion notes, rollouts meant for the owner, README user prose
- Marketing, screenshot captions, TestFlight “What to Test”

**How:**
- Between sentences in a paragraph: `end.  Start` (two ASCII spaces after `.` `!` `?`)
- HTML/JSX/SwiftUI that collapses spaces: use NBSP+space
  (`&nbsp; ` / `{"\u00A0 "}` / `\u00A0 `) or a shared helper (ST: `SENTENCE_GAP`)
- Prefer ONE paragraph for short related sentences over stacked one-liners when
  the owner asked for density (see Socratic proposals empty-state, 2026-08-08)
- Do not insert spaces after brand periods (`Congress.Trade`), URLs, emails, or `U.S.`

**Does NOT apply:** code identifiers, commit messages (normal spacing is fine
for git), log lines, API enums, pure bullet lists of fragments with no
sentence terminator.

**Agent failure mode:** shipping App Store description, review notes, or UI
paragraphs with single spaces after periods, or stale trial/corpus copy.
Fix on sight.  Protocol: `/Users/jay/apps/AGENT-SYNC.md` § Two spaces.

## Run-once glyph = emoji bolt (owner preference 2026-08-08, Socratic.Trade)
The Run-once affordance uses the colored emoji ⚡ (U+26A1), not a line-icon Zap —
owner: the emoji "reads better than the one on the site." Keep Start/Resume on the
Play glyph (two "go" line-icons side-by-side read as competing primaries). When copy
references the control inline, use the ⚡ emoji there too.
