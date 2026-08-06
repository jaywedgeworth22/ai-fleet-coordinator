# Agent seat logos (fleet daily digest HTML)

Used by `scripts/build-fleet-daily-digest.py` → copied into `site/agent-logos/`
on each build. The HTML page shows these chips **instead of** printing seat
names like `[GROK]` / `[CODEX]` / `[CLAUDE]`.

| File | Seat |
|------|------|
| `grok.svg` | Grok (xAI mark from Socratic.Trade model-logos) |
| `codex.svg` | Codex (OpenAI mark) |
| `claude.svg` | Claude (Anthropic mark) |
| `cursor.svg` | Cursor |
| `ag.svg` / `gemini.svg` | Antigravity / Gemini |
| `monet.svg` | Monet |
| `owner.svg` / `owner.png` | Jay signature (asset kept for future use) |

LLM vendor marks reused from `Socratic.Trade/public/model-logos/`.

**Owner / Jay:** the orange signature is stored as `owner.svg` (PNG embedded) and
`owner.png`, but the daily digest does **not** show an Owner chip. Rows that say
`OWNER ACTION` stay plain text — that label is “needs human follow-up”, not a
coding seat like Grok/Codex/Claude.
