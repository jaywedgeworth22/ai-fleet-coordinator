# Fleet Skills Catalog (Universal Multi-Platform Pack)

Updated **2026-08-23**: the installer **specializes identity per platform**.  `docs/fleet-skills/` stays the Monet / Claude.app upload pack.  `~/.cursor/skills` gets `[CURSOR]` / `cursor/`, `~/.gemini/skills` gets `[AG]`, `~/.codex/skills` gets `[CODEX]`, `~/.grok/skills` gets `[GROK]`.  `~/.claude/skills` is shared by Monet and Claude — pin `AGENT_SEAT` to `MONET` or `CLAUDE`.  Do not copy Monet `SKILL.md` files into another seat's folder unchanged.

These skills govern fleet operations across all apps (Socratic.Trade, Congress.Trade, Usage-Monitor, congress-trading-shared, DealDex, Personal-Site, TopSpin, ContactLogo, and ai-fleet-coordinator).

Having explicit fleet skills installed significantly improves agent compliance with procedures across all chats and tools, reinforcing the protocols defined in `AGENT-SYNC.md` and `AGENTS.md`.

---

## 📦 Complete Skills Catalog

| Skill | Purpose & Trigger |
| :--- | :--- |
| **`fleet-coordination`** | **Master Flagship Skill:** End-to-end multi-agent fleet operations (startup, triple-claim, secrets, sentence gap, Apple Notes, PR landing, closeout). |
| **`session-start`** | Systematic startup: poll Slack, check THE BOARD & live effort logs, worktree isolation in `~/apps/`, claim before editing. |
| **`board-ops`** | Operating THE BOARD CLI (`board stats`, `board list`, `board claim`, `board file`) and `mac.jays.services/board`. |
| **`secret-handoff`** | Strict secret safety: canonical handoff file `/Users/jay/.secrets/global-api-keys`, Infisical runtime source of truth, grep-trap ban, safe helpers. |
| **`sentence-gap`** | Visible double-space between sentences (`&nbsp; ` in Markdown chat, two literal spaces in source files). |
| **`owner-copy`** | Human-facing copy standards: two spaces, light theme default, Title Case headings, no agent names in ASC release notes. |
| **`apple-notes`** | Owner-facing review docs, plans, rollouts, and completion notes in the `Coding` folder (local on this Mac). |
| **`land-lane`** | App-specific verification gates, PR creation, auto-merge arming, and production deploy triggers. |
| **`unstick-pr`** | Diagnosing and unblocking stuck PRs (phantom vs real conflicts with 2-arg `git merge-tree`, bot review threads, flakes). |
| **`codex-triage`** | Triaging and resolving automated review bot comments (Codex, Bugbot, Copilot, human reviewers). |
| **`pickup-seat`** | Picking up capped or abandoned peer lanes safely with full attribution. |
| **`fleet-infra`** | Accessing the private infrastructure hub (`fleet-ops:ATTACK-MAP.md`) for host IPs, Tailscale mesh, Coolify UUIDs, and Infisical IDs without committing secrets. |
| **`deploy-verify`** | Post-merge verification across Coolify, Vercel, and public `/api/health` endpoints. |
| **`ios-ship`** | Native iOS Xcode build, version patch increments (`1.0.N`), and TestFlight release loop via Mac runner. |
| **`closeout`** | End-of-task closeout: effort board Deployed/Completed, GitHub Issue closed, Slack `#agent-sync` closeout, Apple Notes stamp. |

---

## 🚀 Installation & Import Guide

### 1. Local skill dirs (specialized per seat)
Folders with `SKILL.md`:
- **Cursor:** `~/.cursor/skills/` — identity `[CURSOR]`, branches `cursor/`
- **Antigravity (Gemini):** `~/.gemini/skills/` — identity `[AG]`, worktrees `*-antigravity`
- **Codex:** `~/.codex/skills/` — identity `[CODEX]`
- **Grok:** `~/.grok/skills/` — identity `[GROK]` (GROK-BUILD is a different pin)
- **Claude Code:** `~/.claude/skills/` — shared Monet + Claude; pin `AGENT_SEAT`

```bash
python3 /Users/jay/Code/ai-fleet-coordinator/scripts/install-fleet-skills.py
```

Never rsync the Monet pack into Cursor/Grok/Codex/AG without running that script.

### 2. Claude Desktop & Web App (UI Upload)
For web/cloud agent interfaces that support ZIP skill imports:
1. Open **Settings → Capabilities → Skills** (or claude.ai → Settings → Capabilities → Skills).
2. Click **Create / Upload skill**.
3. Select any `.zip` package from `/Users/jay/Code/ai-fleet-coordinator/docs/fleet-skills/<skill-name>.zip`.
4. Enable the imported skills.

---

## 🔒 Safety & Sanitization Guarantees

All skills in this directory are sanitized and safe for repository tracking:
- **No live API keys, tokens, or plaintext passwords.**
- **No insecure secret-dumping endpoints.**
- **Grep-trap compliance:** Instructions mandate names-only grep (`grep -oE '^[A-Z][A-Z0-9_]*'`) and direct single-variable extraction.
- **Runtime secrets:** Enforce Infisical as the sole source of truth for deployed application environments.
