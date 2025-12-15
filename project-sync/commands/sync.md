---
description: Sync your current work with Xala PM - update task status, log activities, track progress
---

# Sync Command

Synchronize your development work with Xala PM dashboard.

## Prerequisites

This command requires the Xala PM MCP tools to be available. Check that you have access to:
- `get_tasks`
- `update_task`
- `log_activity`
- `get_phases`
- `update_phase`

## Sync Process

### 1. Identify Current Work
- Check git status for changed files
- Review recent commits
- Identify which tasks these relate to

### 2. Update Task Status
For each affected task:
- If work started → set status to `in_progress`
- If work completed → set status to `done`
- If blocked → add blocker note

### 3. Log Activities
Create activity log entries for:
- Tasks started
- Tasks completed
- Significant progress
- Blockers encountered

### 4. Update Phase Progress
If tasks completed, recalculate phase progress:
- Count completed tasks in phase
- Update phase progress percentage

## Usage Patterns

### Starting Work
```
User: /sync start t1-42
Agent: 
1. update_task(task_id="t1-42", status="in_progress")
2. log_activity(type="task_update", title="Started t1-42: [task title]")
```

### Completing Work
```
User: /sync done t1-42
Agent:
1. update_task(task_id="t1-42", status="done")
2. log_activity(type="task_update", title="Completed t1-42: [task title]")
3. update_phase(phase_id=N, progress=X%)
```

### Auto-Sync
```
User: /sync
Agent:
1. Check git diff to identify what was worked on
2. Match changes to tasks in the project
3. Update all relevant task statuses
4. Log all activities
5. Update phase progress
```

## Output Format

```
🔄 XALA PM SYNC
═══════════════════════════════════════════════════════════════

📊 Changes Detected:
- Modified: 5 files
- Related Tasks: t1-42, t1-43

✅ Synced:
- t1-42: "Implement OAuth" → status: done
- t1-43: "Add rate limiting" → status: in_progress

📝 Activities Logged:
- Completed OAuth implementation
- Started rate limiting work

📈 Phase Progress Updated:
- Phase 3: 75% → 82%

✅ Sync complete!
```

## Guidelines

- Always confirm before making changes
- Show what will be updated before syncing
- Handle errors gracefully (network issues, etc.)
- Provide clear feedback on what was synced

