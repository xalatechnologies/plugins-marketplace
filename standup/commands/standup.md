---
description: Generate a daily standup report based on your recent work
arguments:
  - name: period
    description: Time period to summarize (today, yesterday, week)
    required: false
    default: today
---

# Standup Command

Generate a formatted daily standup report based on your recent work.

## Data Sources

Gather information from:
1. **Git history**: Recent commits, branches, PRs
2. **Xala PM**: Task status changes, activity logs (if MCP available)
3. **Code changes**: Files modified, features implemented
4. **Session context**: What you've been working on

## Standup Format

Standard daily standup structure:

```
📅 DAILY STANDUP - [Date]
═══════════════════════════════════════════════════════════════

👤 [User Name]

───────────────────────────────────────────────────────────────

✅ YESTERDAY (What I completed)

• [Task/PR] - [Brief description]
  └── Related: t1-42, PR #123

• [Task/PR] - [Brief description]
  └── Related: t1-43

───────────────────────────────────────────────────────────────

🚧 TODAY (What I'm working on)

• [Task] - [Brief description]
  └── Target: [Expected completion]
  └── Status: [In progress / Starting]

• [Task] - [Brief description]
  └── Target: [Expected completion]

───────────────────────────────────────────────────────────────

🚫 BLOCKERS

• [Blocker 1] - [Who can help / What's needed]
• None ✅

───────────────────────────────────────────────────────────────

📊 METRICS

Tasks Completed: [X]
PRs Merged: [X]
Commits: [X]
Lines Changed: +[X] / -[X]

───────────────────────────────────────────────────────────────
```

## Smart Features

### Auto-Detection
- Parse git log for commits since last standup
- Check modified files for context
- Identify completed vs in-progress work

### Xala PM Integration
When MCP tools available:
- Pull tasks assigned to user
- Get recent activity logs
- Update standup in dashboard

### Team Context
If working in a team:
- Note dependencies on others' work
- Flag coordination needs
- Highlight shared blockers

## Output Variations

### Concise (for Slack/chat)
```
📅 Standup [Date]
✅ Completed OAuth implementation (t1-42)
🚧 Working on rate limiting (t1-45)
🚫 No blockers
```

### Detailed (for meetings)
[Full format above]

### JSON (for automation)
```json
{
  "date": "2024-12-15",
  "completed": [...],
  "today": [...],
  "blockers": []
}
```

## Guidelines

- Be specific but concise
- Link to task IDs and PRs when possible
- Highlight blockers prominently
- Include context for team members
- Suggest if there are coordination needs

