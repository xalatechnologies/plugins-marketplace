---
description: Create, update, and manage tasks with Xala PM integration
args:
  action: create | update | complete | log | list | assign
  id: Task ID (for update/complete/log/assign)
  title: Task title (for create)
  spec: Spec ID to link (optional)
  agent: Agent to assign (optional)
  status: Task status (optional)
  hours: Hours to log (for log action)
  note: Note or description
---

# Task Command

Manage development tasks with full Xala PM integration.

## Actions

### Create Task

```bash
/task create "Implement user authentication API" --spec SPEC-2024-001 --agent @backend-dev

# Output:
✅ Task Created
- ID: PM-12345
- Title: Implement user authentication API
- Spec: SPEC-2024-001
- Assigned: @backend-dev (Dr. Marcus Rivera)
- Status: Open
- Synced to Xala PM: https://xala.pm/tasks/PM-12345
```

### Update Task

```bash
/task update PM-12345 --status in_progress

# Output:
✅ Task Updated
- ID: PM-12345
- Status: in_progress
- Updated: 2024-01-15 10:30
- Synced to Xala PM
```

### Assign Task

```bash
/task assign PM-12345 --agent @frontend-dev

# Output:
✅ Task Assigned
- ID: PM-12345
- Previous: @backend-dev
- New: @frontend-dev (Sarah Kim)
- Synced to Xala PM
```

### Log Work

```bash
/task log PM-12345 --hours 2 --note "Completed API endpoint implementation"

# Output:
✅ Work Logged
- ID: PM-12345
- Hours: 2
- Total: 6h / 8h estimated
- Note: Completed API endpoint implementation
- Synced to Xala PM
```

### Complete Task

```bash
/task complete PM-12345 --proof "All tests passing, PR #45 merged"

# Output:
✅ Task Completed
- ID: PM-12345
- Title: Implement user authentication API
- Time: 8h logged
- Proof: All tests passing, PR #45 merged
- Synced to Xala PM
```

### List Tasks

```bash
/task list --spec SPEC-2024-001

# Output:
📋 Tasks for SPEC-2024-001

| ID | Title | Agent | Status | Progress |
|----|-------|-------|--------|----------|
| PM-12345 | Auth API | @backend-dev | ✅ Done | 8h/8h |
| PM-12346 | Login UI | @frontend-dev | 🔄 In Progress | 3h/4h |
| PM-12347 | E2E Tests | @testing-specialist | ⬜ Open | 0h/2h |

/task list --agent @backend-dev

# Output:
📋 Tasks for @backend-dev

| ID | Title | Spec | Status |
|----|-------|------|--------|
| PM-12345 | Auth API | SPEC-2024-001 | ✅ Done |
| PM-12350 | Payment API | SPEC-2024-002 | 🔄 In Progress |
```

## Agent-Aware Task Creation

When creating tasks from a spec, specify the responsible agent:

```bash
# From spec, create all tasks with agents
/task create-from-spec SPEC-2024-001

# Output:
📋 Creating tasks from SPEC-2024-001...

✅ Created 5 tasks:

| PM ID | Task | Agent | Estimate |
|-------|------|-------|----------|
| PM-12345 | Create login API | @backend-dev | 2h |
| PM-12346 | Build login form | @frontend-dev | 2h |
| PM-12347 | Security review | @owasp-expert | 1h |
| PM-12348 | Write E2E tests | @testing-specialist | 2h |
| PM-12349 | Accessibility audit | @accessibility-expert | 1h |

All synced to Xala PM.
```

## Xala PM Sync

All task operations sync automatically:

```typescript
// On task create
await xalaPM.tasks.create({
  title: 'Implement user authentication API',
  specId: 'SPEC-2024-001',
  assignee: '@backend-dev',
  estimatedHours: 8,
});

// On status update
await xalaPM.tasks.update(taskId, {
  status: 'in_progress',
  updatedBy: '@backend-dev',
  updatedAt: new Date(),
});

// On completion
await xalaPM.tasks.complete(taskId, {
  proof: 'All tests passing, PR #45 merged',
  actualHours: 8,
  completedBy: '@backend-dev',
  completedAt: new Date(),
});
```

## Task States

| Status | Icon | Description |
|--------|------|-------------|
| `open` | ⬜ | Not started |
| `in_progress` | 🔄 | Currently being worked on |
| `blocked` | 🚫 | Waiting on dependency |
| `review` | 👀 | Ready for review |
| `done` | ✅ | Completed |
| `cancelled` | ❌ | Cancelled |

## Integration with /delegate

When using `/delegate`, a task is automatically created:

```bash
/delegate @backend-dev "Implement user API" --spec SPEC-2024-001

# Automatically creates:
# - Task PM-12345 assigned to @backend-dev
# - Linked to SPEC-2024-001
# - Status: in_progress
# - Start time logged
```
