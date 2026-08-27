"""Bearer token for the local MCP HTTP listener.

Never print the token.  Compare with hmac.compare_digest.
"""

from __future__ import annotations

import hmac
import os
import secrets
from pathlib import Path

from .config import SECRETS_FILE


def ensure_token_file() -> Path:
    """Create ~/.secrets/seat-mcp.env with a random token if missing."""
    SECRETS_FILE.parent.mkdir(mode=0o700, exist_ok=True)
    if not SECRETS_FILE.is_file():
        token = secrets.token_urlsafe(32)
        SECRETS_FILE.write_text("SEAT_MCP_TOKEN=" + token + "\n", encoding="utf-8")
    os.chmod(SECRETS_FILE, 0o600)
    return SECRETS_FILE


def load_token() -> str:
    """Read SEAT_MCP_TOKEN.  Empty file is a hard fail."""
    ensure_token_file()
    token = ""
    for raw in SECRETS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("SEAT_MCP_TOKEN="):
            token = line.split("=", 1)[1].strip().strip("'").strip('"')
            break
    if not token:
        raise RuntimeError("SEAT_MCP_TOKEN empty in %s" % SECRETS_FILE)
    return token


def bearer_ok(header: str, token: str) -> bool:
    """True when Authorization is Bearer <token>."""
    if not header or not token:
        return False
    parts = header.split(None, 1)
    if len(parts) != 2:
        return False
    scheme, got = parts
    if scheme.lower() != "bearer":
        return False
    got = got.strip()
    if len(got) != len(token):
        # Keep compare_digest from throwing on length mismatch.
        hmac.compare_digest(token, token)
        return False
    return hmac.compare_digest(got, token)


ACCESS_HEADERS = (
    "Cf-Access-Jwt-Assertion",
    "Cf-Access-Authenticated-User-Email",
)

ALLOWED_PUBLIC_ORIGINS = (
    "https://agents.jays.services",
)


def access_authenticated(headers) -> bool:
    """True when Cloudflare Access already gated this hop.

    Direct loopback clients do not send these.  Named-tunnel requests from
    Grok Bot / Cursor cloud do, after Access accepts the service token.
    """
    if headers is None:
        return False
    getter = headers.get if hasattr(headers, "get") else lambda k, d="": (headers or {}).get(k, d)
    for name in ACCESS_HEADERS:
        val = getter(name) or getter(name.lower())
        if val:
            return True
    return False


def origin_ok(origin: str, access_ok: bool = False) -> bool:
    """Allow missing Origin and local / editor origins.  Reject the rest.

    DNS-rebinding guard for streamable HTTP.  Loopback bind is the other half.
    Cloudflare Access-authenticated hops (Grok Bot via agents.jays.services)
    skip the browser-origin check — Access + Bearer still required.
    """
    if access_ok:
        return True
    if not origin:
        return True
    origin = origin.strip()
    if origin.lower() == "null":
        return True
    allowed_prefixes = (
        "http://127.0.0.1",
        "https://127.0.0.1",
        "http://localhost",
        "https://localhost",
        "app://",
        "vscode-file://",
        "vscode://",
        "cursor://",
    )
    if origin.startswith(allowed_prefixes):
        return True
    return origin.rstrip("/") in ALLOWED_PUBLIC_ORIGINS
