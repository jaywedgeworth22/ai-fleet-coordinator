---
name: dns-and-registrars
description: Fleet DNS and registrar playbook.  Cloudflare is DNS for every fleet domain; registrar and Cloudflare account are separate.  New DNS-only zones go on Usage.Jays.Services.  Use when adding a domain, linking a host, choosing a Cloudflare account, or touching nameservers.  Do not buy domains, mint accounts, or enable paid Cloudflare products without Jay.
---

# Fleet DNS and Registrars (ALL AGENTS)

> **This install is for `MONET`.** Slack `[MONET]`.  Notes `Monet`.  Branches `monet/`.  Worktrees `~/apps/<app>-monet`.  Do not inherit another seat's tag from another seat's upload pack.


Cloudflare is the DNS manager for every fleet domain.  Registrar and Cloudflare account are separate.

**Canonical:** `docs/DNS-AND-REGISTRARS.md` in `ai-fleet-coordinator`.

Do not change DNS, buy domains, mint Cloudflare accounts, install products, or spend without Jay.

## Default for a new DNS-only zone

App hosted on Vercel, Coolify, or elsewhere, with no Workers / R2 / WAF / other Cloudflare products: put the zone on **Usage.Jays.Services** (login `mail@jays.services`).  That account already holds Usage-Monitor plus DNS-only zones `jaywedgeworth.com` and `jays.services`.

If an app later needs extra Cloudflare services, create a dedicated Cloudflare account for that app and migrate its zone(s) there.  Do not pile product services onto Usage.

## Cloudflare accounts

| Account | Login | Holds | Do not |
|---------|-------|-------|--------|
| Usage.Jays.Services | `mail@jays.services` | Usage-Monitor + DNS-only zones + new DNS-only apps | Put ST/CT product services here |
| SocraticTrade.com | `socratic.trade@jays.services` | ST registrar for SocraticTrade.com and Socratic.Trade, ST DNS, ST R2 weekly backups | Move unrelated new zones here |
| Congress.Trade | `congress.trade@jays.services` | CT DNS, CT R2 weekly backups | Move unrelated new zones here |
| old | unused Gmail login (do not print it) | unused | Create or move anything here.  Leave it. |

## Registrars

| Registrar | Use for |
|-----------|---------|
| Namecheap | Default for most domains.  `NAMECHEAP_API_KEY` lives in global API keys (do not print or commit it). |
| UnstoppableDomains | `jays.services` only |
| Cloudflare registrar | SocraticTrade.com and Socratic.Trade only (the ST Cloudflare account) |

After registration, point nameservers at Cloudflare and manage records in the correct Cloudflare account.  Do not leave a live product on Namecheap parking / URL Forward.

## Linking a domain

1. Confirm host + required records.
2. Confirm the zone is on the right Cloudflare account (Usage unless the app already has a dedicated account).
3. Change DNS at Cloudflare unless nameservers are still at the registrar (then move NS first).

Do not mint Cloudflare accounts, buy domains, or enable paid Cloudflare products without Jay.  Env/secrets stay with Meteorologist.
