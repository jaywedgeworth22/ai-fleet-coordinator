#!/usr/bin/env bash
# Contract tests for the agy-acp session/list stdio wrapper.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
RT="${ROOT}/agy-acp-runtime"
WRAP="${RT}/agy-acp-list-wrapper.cjs"
WRAP_SH="${RT}/agy-acp-list-wrapper.sh"
START="${RT}/start.sh"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

[[ -x "$WRAP" ]] || fail "agy-acp-list-wrapper.cjs must be executable"
[[ -x "$WRAP_SH" ]] || fail "agy-acp-list-wrapper.sh must be executable"
grep -q 'agy-acp-list-wrapper.cjs' "$WRAP_SH" || fail "shell entry must exec the node wrapper"
if grep -q 'agy-acp-list-wrapper' "$START"; then
  fail "start.sh must not spawn the list wrapper (pm2 :8765 hop stays turbo)"
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
HOME_FIX="$TMP/agy-home"
mkdir -p "$HOME_FIX/cache" \
  "$HOME_FIX/brain/sess-brain/.system_generated/logs" \
  "$HOME_FIX/conversations"

cat > "$HOME_FIX/cache/last_conversations.json" <<'JSON'
{
  "/Users/jay/apps/trading-antigravity": "sess-mapped",
  "/Users/jay/apps/dealdex-antigravity": "sess-brain"
}
JSON

cat > "$HOME_FIX/brain/sess-brain/.system_generated/logs/transcript.jsonl" <<'JSONL'
{"source":"USER_EXPLICIT","type":"USER_INPUT","content":"<USER_REQUEST>Fix the ticker chart</USER_REQUEST>","created_at":"2026-08-19T12:00:00.000Z"}
{"source":"MODEL","type":"PLANNER_RESPONSE","content":"ok","created_at":"2026-08-20T12:00:00.000Z"}
JSONL

printf 'sqlite' > "$HOME_FIX/conversations/sess-brain.db"
touch -t 202608201200 "$HOME_FIX/conversations/sess-brain.db"
printf 'sqlite' > "$HOME_FIX/conversations/sess-db.db"
touch -t 202608211200 "$HOME_FIX/conversations/sess-db.db"

AGY_ACP_HOME="$HOME_FIX" HOME="$TMP" WRAP_MODULE="$WRAP" node --input-type=commonjs -e '
const assert = require("assert");
const wrap = require(process.env.WRAP_MODULE);

const rewritten = wrap.rewriteInitializeResult({
  protocolVersion: 1,
  agentCapabilities: { loadSession: true },
});
assert.strictEqual(rewritten.agentCapabilities.loadSession, true);
assert.strictEqual(rewritten.agentCapabilities.sessionCapabilities.list, true);

const created = wrap.rewriteInitializeResult({ protocolVersion: 1 });
assert.strictEqual(created.agentCapabilities.sessionCapabilities.list, true);
assert.strictEqual(created.agentCapabilities.loadSession, undefined);

const failed = wrap.rewriteInitializeResult(undefined);
assert.strictEqual(failed, undefined);

const env = {
  AGY_ACP_HOME: process.env.AGY_ACP_HOME,
  HOME: process.env.HOME,
};
const listed = wrap.listAntigravitySessions({ env });
const ids = listed.map((s) => s.sessionId).sort();
assert.deepStrictEqual(ids, ["sess-brain", "sess-db", "sess-mapped"]);
const brain = listed.find((s) => s.sessionId === "sess-brain");
assert.strictEqual(brain.cwd, "/Users/jay/apps/dealdex-antigravity");
assert.strictEqual(brain.title, "Fix the ticker chart");
assert.ok(brain.updatedAt);

const mapped = listed.find((s) => s.sessionId === "sess-mapped");
assert.strictEqual(mapped.cwd, "/Users/jay/apps/trading-antigravity");
assert.strictEqual(mapped.title, "Untitled");

const filtered = wrap.listAntigravitySessions({
  env,
  cwd: "/Users/jay/apps/trading-antigravity",
});
assert.deepStrictEqual(filtered.map((s) => s.sessionId), ["sess-mapped"]);

const empty = wrap.listAntigravitySessions({
  env: { AGY_ACP_HOME: process.env.AGY_ACP_HOME + "-missing", HOME: process.env.HOME },
});
assert.deepStrictEqual(empty, []);

const orphanHome = process.env.AGY_ACP_HOME + "-orphan";
const fs = require("fs");
const path = require("path");
fs.mkdirSync(path.join(orphanHome, "conversations"), { recursive: true });
fs.writeFileSync(path.join(orphanHome, "conversations", "only-db.db"), "x");
const orphan = wrap.listAntigravitySessions({
  env: { AGY_ACP_HOME: orphanHome, HOME: process.env.HOME },
});
assert.deepStrictEqual(orphan, []);
'

MOCK="$TMP/mock-agy-acp.cjs"
cat > "$MOCK" <<'JS'
#!/usr/bin/env node
"use strict";
const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });
rl.on("line", (line) => {
  let msg;
  try {
    msg = JSON.parse(line);
  } catch {
    return;
  }
  if (msg.method === "initialize") {
    if (process.env.MOCK_INIT_FAIL === "1") {
      process.stdout.write(JSON.stringify({
        jsonrpc: "2.0",
        id: msg.id,
        error: { code: -32000, message: "child init failed" },
      }) + "\n");
      return;
    }
    process.stdout.write(JSON.stringify({
      jsonrpc: "2.0",
      id: msg.id,
      result: {
        protocolVersion: 1,
        agentCapabilities: { loadSession: true },
      },
    }) + "\n");
    return;
  }
  if (msg.method === "session/new") {
    process.stdout.write(JSON.stringify({
      jsonrpc: "2.0",
      id: msg.id,
      result: { sessionId: "child-new" },
    }) + "\n");
    return;
  }
  if (msg.id != null) {
    process.stdout.write(JSON.stringify({
      jsonrpc: "2.0",
      id: msg.id,
      result: { echoed: msg.method },
    }) + "\n");
  }
});
JS
chmod +x "$MOCK"

run_proxy() {
  local extra="${1:-}"
  # stdin closes after the here-doc so the wrapper exits with the child.
  env AGY_ACP_CHILD="$MOCK" AGY_ACP_HOME="$HOME_FIX" HOME="$TMP" $extra \
    node "$WRAP" <<'RPC'
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":1}}
{"jsonrpc":"2.0","id":2,"method":"session/list","params":{}}
{"jsonrpc":"2.0","id":3,"method":"sessions/list","params":{"cwd":"/Users/jay/apps/trading-antigravity"}}
{"jsonrpc":"2.0","id":4,"method":"session/new","params":{"cwd":"/tmp"}}
RPC
}

OUT="$(run_proxy)"
echo "$OUT" | grep -q '"loadSession":true' || fail "initialize rewrite must keep loadSession: $OUT"
echo "$OUT" | grep -q '"list":true' || fail "initialize rewrite must set list=true: $OUT"
echo "$OUT" | grep -q '"sessionId":"sess-brain"' || fail "session/list must include fixture brain id: $OUT"
echo "$OUT" | grep -q '"sessionId":"sess-mapped"' || fail "sessions/list filter must include mapped id: $OUT"
echo "$OUT" | grep -q '"sessionId":"child-new"' || fail "session/new must pass through: $OUT"

FAIL_OUT="$(run_proxy "MOCK_INIT_FAIL=1")"
echo "$FAIL_OUT" | grep -q '"message":"child init failed"' || fail "child initialize error must pass through: $FAIL_OUT"
if echo "$FAIL_OUT" | grep -q '"list":true'; then
  fail "failed initialize must not advertise list: $FAIL_OUT"
fi
if echo "$FAIL_OUT" | grep -q '"sessionId":"sess-brain"'; then
  fail "failed initialize must fail-close list to []: $FAIL_OUT"
fi
echo "$FAIL_OUT" | grep -F -q '"sessions":[]' || fail "failed initialize list must be []: $FAIL_OUT"

echo "ok"
