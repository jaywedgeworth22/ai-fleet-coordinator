# fleet-recall-service

Hetzner-side HTTP front for the fleet-agents corpus, so cloud seats and phones reach fleet
recall even while the Mac is asleep.  It runs on the Coolify box next to Qdrant and TEI and
imports `scripts/fleet_rag/recall_api.py` unchanged, so the semantics are exactly those of the
`recall` CLI, the stdio `fleet-recall-mcp.py`, and the seat-mcp tools.

Public URL (once deployed): **https://recall.jays.services** — Cloudflare Access + bearer.
`agents.jays.services` stays up as the Mac-side hop that also carries the seat tools; this
service is the one that does not depend on the Mac.

## Endpoints

| Method | Path | Auth | What |
|---|---|---|---|
| GET | `/health` | none | `{ok, name, version, fleet_rag, collection, points, backend_ok, mcp, recall}` — `points` is the live count, cached 30 s; `ok` is the process, `backend_ok` is Qdrant |
| GET | `/recall/stats` | bearer | `recall_stats()` |
| POST | `/recall/search` | bearer | `recall_search(**body)` — `query` required; `limit`, `category`, `app`, `source`, `seat`, `since_days` |
| POST | `/recall/contribute` | bearer | `recall_contribute(**body)` — `text`, `category`, **`seat` required**; `app`, `title`, `url` |
| POST | `/mcp` | bearer | streamable-HTTP JSON-RPC: `initialize` (sets `MCP-Session-Id`), `notifications/*` (202), `ping`, `tools/list`, `tools/call`, `server/discover` — same framing as seat-mcp, so a client can swap the URL |

Auth is `Authorization: Bearer <RECALL_API_TOKEN>` on everything except `/health`, compared in
constant time; anything else answers 401 with `WWW-Authenticate: Bearer`.  REST errors are
`{"ok": false, "error": ...}` — 400 for caller mistakes, 502 (exception class only) when Qdrant
or TEI fails.  MCP tool errors come back as `isError: true` results so the model sees them;
unknown tools / methods are JSON-RPC errors (-32602 / -32601).  `seat` is required on
`recall_contribute` and the process's own `AGENT_SEAT` is never used for a remote caller.

Configuration is **environment only** — the container never reads `~/.secrets`:

| Variable | Required | Notes |
|---|---|---|
| `RECALL_API_TOKEN` | yes | bearer for every non-health route; the process refuses to start without it |
| `QDRANT_URL` | yes | `http://100.69.77.26:6333` from a container on the box (see *Network*) |
| `QDRANT_API_KEY` | yes | write key, used only by `recall_contribute` |
| `QDRANT_READONLY_API_KEY` | no | used for every read when present |
| `QDRANT_FLEET_COLLECTION` | yes | `fleet-agents` |
| `TEI_URL` | yes | `http://100.69.77.26:8081` |
| `TEI_API_KEY` | yes | |
| `TEI_EMBED_MODEL` | no | informational |
| `PORT` / `HOST` | no | default `8080` / `0.0.0.0` |
| `RECALL_REF` | no | git ref the bootstrap fetches (default `main`) |
| `RECALL_FAKE` | no | `1` serves the in-process fake corpus (tests, smoke) |

Logs go to stdout as `time method path status`; no bodies, headers, query strings, or tokens.

## Files

- `server.py` — the service (stdlib only, `ThreadingHTTPServer`)
- `bootstrap.sh` — fetch the public repo tarball with `urllib`, extract `scripts/fleet_rag` and
  `scripts/fleet-recall-service` into `/app`, `exec` the server.  Honors `RECALL_REF`,
  `RECALL_APP_DIR`, `RECALL_TARBALL` (reused when present), `RECALL_TARBALL_URL`,
  `RECALL_BOOTSTRAP_ONLY=1`
- `compose.example.yaml` — the Coolify resource: stock `python:3.12-slim`, a `python -c` command
  that downloads the tarball, extracts `bootstrap.sh`, and execs it; healthcheck on `/health`;
  1 CPU / 1 GiB; `restart: unless-stopped`; `expose: 8080` with no host binding
- `Dockerfile` — COPY-based image for anyone who prefers a build (`docker build -f
  scripts/fleet-recall-service/Dockerfile scripts`), non-root uid 10001, same healthcheck
- Tests: `scripts/fleet_rag/tests/test_service.py` (`cd scripts && python3 -m unittest
  fleet_rag.tests.test_service -v`)

## Run it locally

```bash
cd scripts
RECALL_API_TOKEN=dev RECALL_FAKE=1 HOST=127.0.0.1 PORT=8080 python3 fleet-recall-service/server.py
curl -s http://127.0.0.1:8080/health
```

Against the live backend, export the `QDRANT_*` / `TEI_*` names from Infisical shared/prod
into the environment first (never paste them into a file), then drop `RECALL_FAKE`.

## Network (checked 2026-09-02 from the box)

From a `python:3.12-slim` container on the `coolify` docker network:

| Target | Result |
|---|---|
| `http://100.69.77.26:6333/healthz` (host Tailscale address, Qdrant) | **200** |
| `http://100.69.77.26:8081/health` (host Tailscale address, TEI) | **200** |
| `http://10.0.1.1:6333/healthz` (docker0 gateway) | connection refused |
| `http://host.docker.internal:6333/healthz` | no such host |
| `qdrant` / `tei` container DNS names | not on the `coolify` network (each Coolify service has its own network `ookh0qml…` / `cday9viy…`) |

So the compose file defaults `QDRANT_URL` and `TEI_URL` to the Tailscale address, the same
values every Mac client already uses.  If the host ever loses Tailscale, the fallback is to
attach `recall-api` to the two service networks and use the `qdrant` / `tei` aliases.

## Deploy on Coolify (orchestrator applies; nothing here is automated)

Targets: project `l11qegr5vie93o7dqlfjgd6n`, environment `production`, server
`jxzqcs3h6g1wiipnnblhismp` (the Hetzner box, public `167.233.254.55` /
`2a01:4f8:1c1b:e6a5::1`), FQDN `https://recall.jays.services`.

1. **Coolify resource.**  Project → production → *New Resource* → *Docker Compose* (empty) on
   server `jxzqcs3h6g1wiipnnblhismp`.  Paste `compose.example.yaml`.  Name it `recall-api`.
   Leave *Connect to predefined network* on (the default) so Traefik can reach it.
2. **Environment variables** (the compose `${…}` references appear in the resource's
   *Environment Variables* tab).  From Infisical shared/prod (project
   `18f563a3-9c88-454c-96eb-28fc9678f3ba`) set `QDRANT_API_KEY`, `QDRANT_READONLY_API_KEY`,
   `TEI_API_KEY`; keep the defaults for `QDRANT_URL`, `TEI_URL`, `QDRANT_FLEET_COLLECTION`,
   `TEI_EMBED_MODEL`, `RECALL_REF=main`.  `SERVICE_PASSWORD_RECALLTOKEN` is generated by Coolify
   — copy its value into Infisical shared/prod as **`RECALL_API_TOKEN`** so Infisical stays the
   canonical home and the Mac seats can read it from there.  Use the Coolify UI or the MCP
   `bulk_env_update` tool; never put a value in a tracked file.
3. **Domain.**  On the `recall-api` service set the domain to `https://recall.jays.services`
   (port 8080).  Traefik issues the Let's Encrypt certificate once DNS resolves.
4. **Cloudflare DNS** (zone `jays.services`, account *Usage.Jays.Services*): `A recall →
   167.233.254.55`, proxied; optionally `AAAA recall → 2a01:4f8:1c1b:e6a5::1`, proxied.  The
   zone is already *Full (strict)*, which is what the other Coolify-hosted names use.
5. **Cloudflare Access** (org `silent-frost-37e0.cloudflareaccess.com`), mirroring
   `agents.jays.services` (app `1e1a5fc4-0f7d-44ac-bb0d-5fa6d5d73ddf`):
   - self-hosted app `recall.jays.services`, session 24 h;
   - policy *Allow* emails `mail@jays.services`, `jaywedgeworth22@gmail.com` (One-time PIN
     IdP `76030d10-ec5b-46ff-ba9d-a4412cd755ce`);
   - policy *Service Auth* with the existing service token
     `215fc9ae-4a1d-4b0e-8ec3-9bd0c49ee1fd` (so every cloud client keeps the same
     `CF-Access-Client-Id` / `CF-Access-Client-Secret` pair it already has for agents);
   - a second app `recall.jays.services/health` with a *Bypass everyone* policy so the Coolify
     healthcheck, UptimeRobot, and `recall doctor` can read health without a token (mirrors
     bypass app `99c0aacc-9e84-49b4-89b0-51bdb4b6bf36`).
6. **Deploy** and watch the log: `compose: fetching …` → `bootstrap: extracted N files` →
   `listening on 0.0.0.0:8080`.  The first start downloads a ~4 MB tarball; `start_period` is
   120 s.  `docker logs` never shows a token.
7. **Verify** from anywhere: `/health` must be public and report `backend_ok: true` with the
   live point count (38,7xx); `/recall/stats` must be 401 without headers and 200 with them.
8. **Record it**: fleet-ops `ATTACK-MAP.md` (host row), the Coolify resource UUID in
   `docs/RAG-FLEET-INFRA.md` *Health rows*, and an UptimeRobot monitor on
   `https://recall.jays.services/health`.

**Updating**: the container fetches `RECALL_REF` on every start, so *Restart* in Coolify picks
up the latest `main`.  Pin `RECALL_REF` to a tag or sha for a frozen deploy.

**Until this lane lands on `main`** the tarball does not contain `scripts/fleet-recall-service`
and the bootstrap exits with `server.py missing after extract`; deploy after the merge, or set
`RECALL_REF` to the merged branch name.

## Clients

Every request needs the bearer plus the two Cloudflare Access service-token headers (the
service token gets you through Access; the bearer gets you into the service).  Values come from
the environment / a secret store, never from a file in a repo.

### curl (REST)

```bash
curl -sS https://recall.jays.services/health

curl -sS https://recall.jays.services/recall/stats \
  -H "Authorization: Bearer $RECALL_API_TOKEN" \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET"

curl -sS https://recall.jays.services/recall/search \
  -H "Authorization: Bearer $RECALL_API_TOKEN" \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"query":"handoff file grep trap","limit":3,"app":"fleet"}'

curl -sS https://recall.jays.services/recall/contribute \
  -H "Authorization: Bearer $RECALL_API_TOKEN" \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"text":"<one reusable paragraph, 40..4000 chars>","category":"lesson","app":"fleet","seat":"CURSOR","url":"https://github.com/..."}'
```

### MCP (remote, streamable HTTP) — Claude Code Cloud, Cursor cloud, Codex cloud

Claude Code (`claude mcp add`, or the JSON below in `~/.claude.json` / the cloud seat's MCP
config):

```bash
claude mcp add --transport http fleet-recall https://recall.jays.services/mcp \
  --header "Authorization: Bearer ${RECALL_API_TOKEN}" \
  --header "CF-Access-Client-Id: ${CF_ACCESS_CLIENT_ID}" \
  --header "CF-Access-Client-Secret: ${CF_ACCESS_CLIENT_SECRET}"
```

```json
{
  "mcpServers": {
    "fleet-recall": {
      "type": "http",
      "url": "https://recall.jays.services/mcp",
      "headers": {
        "Authorization": "Bearer ${RECALL_API_TOKEN}",
        "CF-Access-Client-Id": "${CF_ACCESS_CLIENT_ID}",
        "CF-Access-Client-Secret": "${CF_ACCESS_CLIENT_SECRET}"
      }
    }
  }
}
```

Cursor (`~/.cursor/mcp.json`, same shape without `"type"`):

```json
{
  "mcpServers": {
    "fleet-recall": {
      "url": "https://recall.jays.services/mcp",
      "headers": {
        "Authorization": "Bearer ${RECALL_API_TOKEN}",
        "CF-Access-Client-Id": "${CF_ACCESS_CLIENT_ID}",
        "CF-Access-Client-Secret": "${CF_ACCESS_CLIENT_SECRET}"
      }
    }
  }
}
```

Codex (`~/.codex/config.toml`; `env_http_headers` names the environment variables that hold
the header values, so `RECALL_AUTH_HEADER` must contain `Bearer <token>`):

```toml
[mcp_servers.fleet-recall]
url = "https://recall.jays.services/mcp"
env_http_headers = { "Authorization" = "RECALL_AUTH_HEADER", "CF-Access-Client-Id" = "CF_ACCESS_CLIENT_ID", "CF-Access-Client-Secret" = "CF_ACCESS_CLIENT_SECRET" }
```

The tracked example is `scripts/seat-mcp/mcp.example.json` (entry `fleet-recall`).  Tools:
`recall_search`, `recall_stats`, `recall_contribute` (pass `seat`).

## Tests

```bash
cd scripts && python3 -m unittest fleet_rag.tests.test_service -v   # 25 tests, no network
cd scripts && python3 -m unittest fleet_rag.tests                     # whole suite
```

The tests bind `127.0.0.1:0`, install `recall_api`'s fake backend, and cover: `/health` without
auth (and with the backend down), 401 without / with a wrong token and 200 with the right one,
every REST route, argument validation, the seat requirement, the 502 class-only path, the MCP
subset (`initialize` + `MCP-Session-Id`, notifications → 202, `ping`, `tools/list`,
`tools/call`, `server/discover`, framing errors, protocol-version and `Mcp-Method` checks), and
the real entry point (refuses without `RECALL_API_TOKEN`; `RECALL_FAKE=1` serves; the log never
contains the token).
