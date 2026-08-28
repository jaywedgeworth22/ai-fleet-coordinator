#!/bin/sh
# Local seat-mcp stdio launcher for Grok TUI / Cursor / any local agent.
# Token stays in ~/.secrets/seat-mcp.env.  Never in mcp.json or config.toml.
set -e
exec /usr/bin/python3 /Users/jay/apps/mcp-servers/seat-mcp-stdio-proxy.py
