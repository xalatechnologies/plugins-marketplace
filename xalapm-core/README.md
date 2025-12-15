# Xala PM Core Integration

Core integration layer that enables all agents to synchronize with Xala PM.

## Purpose

This plugin provides the shared integration protocol that ALL other plugins use to:
- Update task status automatically
- Log activities to the project feed
- Sync analysis results with project data
- Create tasks from findings
- Notify team members

## Integration Protocol

### Every Agent MUST

1. **Check project context** at session start
2. **Mark tasks in_progress** when starting work
3. **Mark tasks done** when completing work
4. **Log activities** for significant actions
5. **Create tasks** from analysis findings

### Activity Types

| Type | When to Use |
|------|-------------|
| `task_update` | Task status changes |
| `code_change` | Files created/modified |
| `review` | Code review completed |
| `deployment` | Build/deploy actions |
| `analysis` | Codebase analysis |
| `compliance` | Compliance checks |

## Available MCP Tools

### Task Management
```bash
get_tasks status="in_progress"
create_task id="t1-fe-001" title="..." role="frontend"
update_task task_id="t1-fe-001" status="done"
```

### Activity Logging
```bash
log_activity type="task_update" title="Completed login component" entity_type="task" entity_id="t1-fe-001"
```

### Phase Management
```bash
update_phase phase_id=1 progress=75
```

### Notifications
```bash
notify_team type="success" title="Sprint complete" recipients=["pm"]
```

## Hooks

| Hook | Trigger | Action |
|------|---------|--------|
| `session_start` | New session | Load project context |
| `task_started` | Work begins | Mark in_progress |
| `task_completed` | Work ends | Mark done + log |
| `code_created` | New files | Log activity |
| `analysis_complete` | Analysis done | Create tasks |

## Usage

This plugin is automatically loaded (priority: 999, required: true).
All other plugins inherit its hooks and tools.

## For Plugin Developers

When creating a new plugin, ensure it:

1. **Imports xalapm-core** as a dependency
2. **Uses the MCP tools** for all project updates
3. **Follows the activity logging format**
4. **Triggers appropriate hooks**

Example hook in your plugin:
```json
{
  "event": "after_component_create",
  "action": "xalapm_sync",
  "description": "Sync with Xala PM after creating component"
}
```

