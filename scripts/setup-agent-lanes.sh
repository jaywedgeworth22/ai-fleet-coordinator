#!/bin/bash
set -euo pipefail

# setup-agent-lanes.sh
# Creates separate git worktrees for different AI agents to work in parallel
# Usage: ./setup-agent-lanes.sh <base_path> (defaults to ~/apps)

BASE_PATH="${1:-$HOME/apps}"
REPO_NAME=$(basename "$(pwd)")
MAIN_BRANCH=$(git branch --show-current)

echo "Setting up agent lanes for $REPO_NAME in $BASE_PATH"
mkdir -p "$BASE_PATH"

AGENTS=("claude" "codex" "antigravity" "cursor" "grok" "monet")

for agent in "${AGENTS[@]}"; do
  LANE_PATH="$BASE_PATH/${REPO_NAME}-${agent}"
  BRANCH_NAME="agent/${agent}"
  
  if [ -d "$LANE_PATH" ]; then
    echo "Lane already exists: $LANE_PATH"
    continue
  fi

  echo "Creating lane for $agent at $LANE_PATH..."
  
  # Check if branch exists
  if git rev-parse --verify "$BRANCH_NAME" >/dev/null 2>&1; then
    git worktree add "$LANE_PATH" "$BRANCH_NAME"
  else
    git worktree add -b "$BRANCH_NAME" "$LANE_PATH" "$MAIN_BRANCH"
  fi
  
  echo "Lane $agent created."
done

echo "All agent lanes set up successfully!"
