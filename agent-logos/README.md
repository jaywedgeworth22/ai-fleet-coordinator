# Agent seat logos (fleet daily digest HTML)

Used by `scripts/build-fleet-daily-digest.py` → copied into `site/agent-logos/`
on each build. The HTML page shows these chips **instead of** printing seat
names like `[GROK]` / `[CODEX]` / `[CLAUDE]`.

| File | Seat |
|------|------|
| `grok.svg` | Grok — the **Grok** mark (`Grok-icon.svg` from `~/Code/Icons - Logos`).  NOT the xAI mark; owner-corrected 2026-08-20. |
| `grok-bot.png` | Grok Bot — its own product mark (owner-supplied `Grok-Bot.png`).  Grok Bot is a separate cloud seat from Grok. |
| `xai.svg` | The xAI company mark, kept under an honest name.  Not used for any seat chip. |
| `codex.svg` | Codex (OpenAI mark) |
| `claude.svg` | Claude (Anthropic mark) |
| `cursor.png` | Cursor — the real Cursor app icon (owner-supplied `cursor.png`), not a generic pointer glyph. |
| `ag.svg` / `gemini.svg` | Antigravity / Gemini |
| `monet.svg` | Monet |
| `owner.svg` / `owner.png` | Jay signature (asset kept for future use) |
| `app-st.png` / `app-ct.png` / `app-um.png` / `app-dd.png` | Product app icons (ST, CT, UM, DealDex) |

Most vendor marks came from `Socratic.Trade/public/model-logos/`; Grok, Grok Bot,
and Cursor are owner-supplied from `~/Code/Icons - Logos/`.

**Mixed extensions are expected.** Grok Bot and Cursor ship as PNG, the rest are
SVG, so never assume `<slug>.svg` — resolve the extension (see `logo_file()` in
`scripts/build-fleet-daily-digest.py` and `load_agent_logos()` in
`~/apps/mac-collab/mac-collab-server.py`).

**Owner / Jay:** the orange signature is stored as `owner.svg` (PNG embedded) and
`owner.png`, but the daily digest does **not** show an Owner chip. Rows that say
`OWNER ACTION` stay plain text — that label is “needs human follow-up”, not a
coding seat like Grok/Codex/Claude.
