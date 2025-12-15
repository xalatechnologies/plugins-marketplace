#!/bin/bash
# Xala PM Activity Logger
# Logs file changes for activity tracking

# Read input from stdin
INPUT=$(cat)

# Extract tool info
TOOL_NAME=$(echo "$INPUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('tool_name', ''))" 2>/dev/null || echo "")
FILE_PATH=$(echo "$INPUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))" 2>/dev/null || echo "")

# Log to activity file if exists
ACTIVITY_LOG="${CLAUDE_PROJECT_DIR:-.}/.claude/activity.log"
if [ -n "$FILE_PATH" ]; then
  mkdir -p "$(dirname "$ACTIVITY_LOG")" 2>/dev/null
  echo "$(date -Iseconds) | $TOOL_NAME | $FILE_PATH" >> "$ACTIVITY_LOG" 2>/dev/null
fi

# Exit 0 to allow tool to proceed
exit 0

