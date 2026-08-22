/*
 * agent-sync-push: Slack Socket Mode -> local push fan-out.
 *
 * Reads (env):
 *   SLACK_SYNC_WEBSOCKET  app-level xapp- token (connections:write) - REQUIRED
 *   SLACK_BOT_TOKEN       bot token with chat:write, used only by local /post
 *   AGENT_SYNC_POST_TOKEN shared bearer token for authenticated /post callers
 *   SLACK_CHANNEL_ID      channel to mirror (default C0BEZDJDNKV, #agent-sync)
 *   RELAY_PORT            local WS relay port (default 8787, loopback only)
 *   EVENTS_FILE           append-only JSONL (default /Users/jay/apps/agent-sync/events.jsonl)
 *
 * Outputs, per channel message:
 *   1. one JSON line appended to EVENTS_FILE:
 *      {ts, thread_ts, channel, user, bot_id, username, subtype, text}
 *   2. the same JSON as one text frame to every client of ws://127.0.0.1:RELAY_PORT
 *
 * Consumers filter for themselves (e.g. `tail -f events.jsonl | grep -v '\[MYTAG->'`).
 * Protocol notes: every events_api envelope is ACKed immediately by envelope_id;
 * `disconnect` frames (Slack-initiated refresh) trigger a clean reconnect via a fresh
 * apps.connections.open URL; exponential backoff on errors, capped at 60s.
 */
'use strict';

const fs = require('fs');
const http = require('http');
const path = require('path');
const { timingSafeEqual } = require('crypto');
const { WebSocketServer } = require('ws');

const APP_TOKEN = process.env.SLACK_SYNC_WEBSOCKET;
const BOT_TOKEN = process.env.SLACK_BOT_TOKEN;
const POST_TOKEN = process.env.AGENT_SYNC_POST_TOKEN;
const CHANNEL = process.env.SLACK_CHANNEL_ID || 'C0BEZDJDNKV';
const RELAY_PORT = parseInt(process.env.RELAY_PORT || '8787', 10);
const EVENTS_FILE = process.env.EVENTS_FILE || '/Users/jay/apps/agent-sync/events.jsonl';
const MAX_POST_BYTES = parseInt(process.env.AGENT_SYNC_POST_MAX_BYTES || '16384', 10);

if (!APP_TOKEN || !APP_TOKEN.startsWith('xapp-')) {
  console.error('FATAL: SLACK_SYNC_WEBSOCKET missing or not an xapp- app-level token');
  process.exit(1);
}

fs.mkdirSync(path.dirname(EVENTS_FILE), { recursive: true });

function json(res, status, body) {
  res.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
    'cache-control': 'no-store',
  });
  res.end(JSON.stringify(body));
}

function timingSafeStringEqual(a, b) {
  if (!a || !b) return false;
  const left = Buffer.from(a);
  const right = Buffer.from(b);
  return left.length === right.length && timingSafeEqual(left, right);
}

function bearerToken(req) {
  const auth = req.headers.authorization || '';
  if (typeof auth === 'string' && auth.toLowerCase().startsWith('bearer ')) {
    return auth.slice(7).trim();
  }
  const header = req.headers['x-agent-sync-post-token'];
  return Array.isArray(header) ? header[0] : (header || '').trim();
}

function websocketToken(req) {
  const fromHeader = bearerToken(req);
  if (fromHeader) return fromHeader;
  try {
    const url = new URL(req.url || '/', 'http://127.0.0.1');
    return (url.searchParams.get('token') || '').trim();
  } catch {
    return '';
  }
}

function authorizedSocket(req) {
  if (!POST_TOKEN) return false;
  return timingSafeStringEqual(websocketToken(req), POST_TOKEN);
}

function readJsonBody(req) {
  return new Promise((resolve, reject) => {
    let bytes = 0;
    let raw = '';
    let tooLarge = false;
    req.setEncoding('utf8');
    req.on('data', (chunk) => {
      if (tooLarge) return;
      bytes += Buffer.byteLength(chunk);
      if (bytes > MAX_POST_BYTES) {
        tooLarge = true;
        raw = '';
        return;
      }
      raw += chunk;
    });
    req.on('end', () => {
      if (tooLarge) {
        reject(Object.assign(new Error('request too large'), { status: 413 }));
        return;
      }
      try {
        resolve(raw ? JSON.parse(raw) : {});
      } catch {
        reject(Object.assign(new Error('invalid json'), { status: 400 }));
      }
    });
    req.on('error', reject);
  });
}

function cleanUsername(value) {
  if (typeof value !== 'string') return undefined;
  const name = value.trim().toUpperCase();
  return /^[A-Z][A-Z0-9_-]{1,20}$/.test(name) ? name : undefined;
}

async function postToSlack({ text, username }) {
  const resp = await fetch('https://slack.com/api/chat.postMessage', {
    method: 'POST',
    headers: {
      authorization: `Bearer ${BOT_TOKEN}`,
      'content-type': 'application/json; charset=utf-8',
    },
    body: JSON.stringify({
      channel: CHANNEL,
      text,
      ...(username ? { username } : {}),
      unfurl_links: false,
      unfurl_media: false,
    }),
  });
  const body = await resp.json().catch(() => ({}));
  if (!resp.ok || !body.ok) {
    throw new Error(body.error || `http_${resp.status}`);
  }
  return body;
}

async function handlePost(req, res) {
  if (!POST_TOKEN || !BOT_TOKEN) {
    json(res, 503, { ok: false, error: 'post endpoint is not configured' });
    return;
  }
  if (!timingSafeStringEqual(bearerToken(req), POST_TOKEN)) {
    json(res, 401, { ok: false, error: 'unauthorized' });
    return;
  }

  let body;
  try {
    body = await readJsonBody(req);
  } catch (err) {
    json(res, err.status || 400, { ok: false, error: err.message || 'invalid request' });
    return;
  }

  const text = typeof body.text === 'string' ? body.text.trim() : '';
  if (!text) {
    json(res, 400, { ok: false, error: 'text is required' });
    return;
  }

  try {
    const slack = await postToSlack({ text, username: cleanUsername(body.username) });
    json(res, 200, { ok: true, channel: slack.channel, ts: slack.ts });
  } catch (err) {
    console.error('post failed:', err.message);
    json(res, 502, { ok: false, error: 'slack post failed' });
  }
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url || '/', 'http://127.0.0.1');
  if (req.method === 'GET' && url.pathname === '/health') {
    json(res, 200, {
      ok: true,
      service: 'agent-sync-push',
      protocol: {
        websocket: 'ws-root',
        websocketPath: '/',
        websocketAuth: 'Bearer AGENT_SYNC_POST_TOKEN or ?token=',
        localEndpoint: `ws://127.0.0.1:${RELAY_PORT}`,
        publicEndpoint: 'wss://agent-sync.jays.services/',
        postPath: '/post',
        healthPath: '/health',
      },
      capabilities: {
        websocketFanout: true,
        authenticatedWebsocket: Boolean(POST_TOKEN),
        authenticatedPost: Boolean(POST_TOKEN && BOT_TOKEN),
        slackSocketMode: Boolean(APP_TOKEN),
      },
      clients: relay.clients.size,
    });
    return;
  }
  if (url.pathname === '/post') {
    if (req.method !== 'POST') {
      json(res, 405, { ok: false, error: 'method not allowed' });
      return;
    }
    void handlePost(req, res);
    return;
  }
  json(res, 404, { ok: false, error: 'not found' });
});

// --- local relay -----------------------------------------------------------
const relay = new WebSocketServer({
  noServer: true,
});
server.on('upgrade', (req, socket, head) => {
  if (!authorizedSocket(req)) {
    socket.write('HTTP/1.1 401 Unauthorized\r\nConnection: close\r\n\r\n');
    socket.destroy();
    return;
  }
  relay.handleUpgrade(req, socket, head, (ws) => {
    relay.emit('connection', ws, req);
  });
});
relay.on('connection', (c) => {
  console.log(`relay client connected (${relay.clients.size} total)`);
  c.on('error', () => {});
});

server.listen(RELAY_PORT, '127.0.0.1', () => {
  console.log(`relay listening ws://127.0.0.1:${RELAY_PORT}`);
  console.log(`post endpoint listening http://127.0.0.1:${RELAY_PORT}/post`);
});

function fanout(record) {
  const line = JSON.stringify(record);
  fs.appendFileSync(EVENTS_FILE, line + '\n');
  for (const client of relay.clients) {
    if (client.readyState === 1) client.send(line);
  }
}

// --- Slack Socket Mode client ----------------------------------------------
let backoffMs = 1000;

async function openSocketUrl() {
  const resp = await fetch('https://slack.com/api/apps.connections.open', {
    method: 'POST',
    headers: { Authorization: `Bearer ${APP_TOKEN}` },
  });
  const data = await resp.json();
  if (!data.ok) throw new Error(`apps.connections.open failed: ${data.error}`);
  return data.url;
}

function handleEnvelope(ws, raw) {
  let env;
  try { env = JSON.parse(raw); } catch { return; }

  if (env.type === 'hello') {
    console.log('slack: hello (connected)');
    backoffMs = 1000;
    return;
  }
  if (env.type === 'disconnect') {
    console.log(`slack: disconnect requested (${env.reason}); reconnecting`);
    ws.close();
    return;
  }
  if (env.envelope_id) ws.send(JSON.stringify({ envelope_id: env.envelope_id }));

  if (env.type !== 'events_api') { console.log(`envelope: ${env.type}`); return; }
  const ev = env.payload && env.payload.event;
  console.log(`event: ${ev && ev.type}/${(ev && ev.subtype) || '-'} ch=${ev && ev.channel}`);
  if (!ev || ev.type !== 'message' || ev.channel !== CHANNEL) return;
  // skip edits/deletes/joins; keep plain + bot_message (fleet posts via the shared bot)
  if (ev.subtype && ev.subtype !== 'bot_message' && ev.subtype !== 'thread_broadcast') return;

  fanout({
    ts: ev.ts,
    thread_ts: ev.thread_ts || null,
    channel: ev.channel,
    user: ev.user || null,
    bot_id: ev.bot_id || null,
    username: ev.username || null,
    subtype: ev.subtype || null,
    text: ev.text || '',
  });
}

async function run() {
  for (;;) {
    try {
      const url = await openSocketUrl();
      await new Promise((resolve) => {
        const ws = new WebSocket(url); // Node >=22 native client
        ws.onmessage = (m) => handleEnvelope(ws, typeof m.data === 'string' ? m.data : m.data.toString());
        ws.onerror = (e) => console.error('slack ws error:', e.message || e.type);
        ws.onclose = () => { console.log('slack ws closed'); resolve(); };
      });
    } catch (err) {
      console.error('connect failed:', err.message);
    }
    await new Promise((r) => setTimeout(r, backoffMs));
    backoffMs = Math.min(backoffMs * 2, 60000);
  }
}

run();
