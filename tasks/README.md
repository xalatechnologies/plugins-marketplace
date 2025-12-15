# Tasks Agent Plugin

Comprehensive task management agent for Xala PM - create, update, track, and sync tasks automatically.

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/task create` | Create a new task |
| `/task update <id>` | Update task details |
| `/task start <id>` | Start working on a task |
| `/task done <id>` | Mark task as complete |
| `/task list` | List tasks with filters |
| `/task view <id>` | View task details |
| `/backlog` | View and manage backlog |
| `/backlog prioritize` | Re-prioritize tasks |
| `/backlog groom` | Clean up the backlog |
| `/backlog sprint` | Plan next sprint |
| `/generate-tasks` | Auto-generate tasks from code/PRD |

### Agent

Specialized task manager agent with expertise in:
- Task lifecycle management
- Priority and effort estimation
- Dependency tracking
- Sprint planning
- Progress tracking

### Skills

- **Task Management Skill**: Autonomous task detection and updates

### Hooks

- Check in-progress tasks on session start
- Show context when task IDs mentioned
- Suggest updates when code changes
- Prompt completion when work is done

### MCP Integration

Integrates with Xala PM MCP server:
- `get_tasks` - List and filter tasks
- `create_task` - Create new tasks
- `update_task` - Update task status/details
- `log_activity` - Log all activities
- `get_phases` / `update_phase` - Track phase progress

## Usage Examples

### Create a Task
```bash
/task create title="Implement rate limiting" role=backend priority=high phase_id=2
```

### Start Working
```bash
/task start t2-5
# or just mention you're starting work, and the agent will offer to update
```

### Complete a Task
```bash
/task done t2-5
# Automatically updates phase progress
```

### View Backlog
```bash
/backlog
/backlog prioritize
/backlog sprint capacity=40h
```

### Generate Tasks from Code
```bash
/generate-tasks code focus=security
/generate-tasks diff branch=feature/auth
```

## Automatic Behaviors

The Tasks Agent will automatically:

1. **Detect work context** - Match your work to existing tasks
2. **Suggest status updates** - When you start or finish work
3. **Create missing tasks** - When you work on untracked items
4. **Update phase progress** - When tasks are completed
5. **Log all activities** - Keep a complete audit trail
6. **Warn about blockers** - When dependencies aren't met

## Installation

```bash
/plugin install tasks@xalapm-marketplace
```

## Mandatory Workflow

When working with Xala PM, the agent enforces:

```
Starting work:
1. update_task status="in_progress"
2. log_activity

Completing work:
1. update_task status="done"
2. log_activity
3. update_phase progress
```

This ensures Xala PM is always in sync with actual work!

