#!/bin/bash
# Xala PM Session Start Hook
# Loads project context at session start

# Read input from stdin
INPUT=$(cat)

# Extract session info
SESSION_ID=$(echo "$INPUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('session_id', 'unknown'))" 2>/dev/null || echo "unknown")
CWD=$(echo "$INPUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('cwd', '.'))" 2>/dev/null || echo ".")

# Output context for Claude (stdout is added to context for SessionStart)
cat << EOF
📋 Xala PM Integration Active
- Session: ${SESSION_ID:0:8}...
- Project: $(basename "$CWD")

Available Xala PM tools: get_tasks, create_task, update_task, log_activity, get_phases
Use these to sync work with the project management system.
EOF

exit 0

