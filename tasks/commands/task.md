---
description: Create, update, or manage tasks in Xala PM
arguments:
  - name: action
    description: Action to perform (create, update, start, done, list, view)
    required: true
  - name: id
    description: Task ID (required for update, start, done, view)
    required: false
  - name: title
    description: Task title (for create)
    required: false
---

# Task Management Command

Manage tasks in Xala PM directly from Claude Code.

## Prerequisites

This command requires the Xala PM MCP server with these tools:
- `get_tasks` - List tasks
- `create_task` - Create new task
- `update_task` - Update existing task
- `log_activity` - Log activity

## Actions

### Create Task (`/task create`)

```
/task create title="Implement user authentication" role=backend priority=high phase_id=2
```

**Required fields:**
- `title` - Task title
- `role` - One of: blockchain, contract, backend, frontend, mobile-ios, mobile-android, devops

**Optional fields:**
- `priority` - low, medium, high, critical (default: medium)
- `phase_id` - Phase number (default: current phase)
- `description` - Detailed description
- `estimate` - Time estimate (e.g., "4h", "2d")

**Workflow:**
```
1. create_task(id="t{phase}-{n}", title="{title}", role="{role}", phase_id={phase}, priority="{priority}")
2. log_activity(type="task_update", title="Created task: {title}", entity_type="task", entity_id="{id}")
3. Confirm creation to user
```

### Update Task (`/task update`)

```
/task update t1-5 status=in_progress
/task update t1-5 priority=critical description="Updated requirements"
```

**Updatable fields:**
- `status` - backlog, in_progress, review, done
- `priority` - low, medium, high, critical
- `title` - New title
- `description` - New description
- `assignee` - Assignee ID

**Workflow:**
```
1. update_task(task_id="{id}", ...fields)
2. log_activity(type="task_update", title="Updated {id}: {changes}", entity_type="task", entity_id="{id}")
3. If status changed to done, check if phase progress needs update
```

### Start Task (`/task start`)

```
/task start t1-5
```

Shorthand for `/task update t1-5 status=in_progress`

**Workflow:**
```
1. update_task(task_id="{id}", status="in_progress")
2. log_activity(type="task_update", title="Started task {id}", entity_type="task", entity_id="{id}")
```

### Complete Task (`/task done`)

```
/task done t1-5
```

Shorthand for `/task update t1-5 status=done`

**Workflow:**
```
1. update_task(task_id="{id}", status="done")
2. log_activity(type="task_update", title="Completed task {id}", entity_type="task", entity_id="{id}")
3. Calculate new phase progress
4. update_phase(phase_id={n}, progress={new_percentage})
```

### List Tasks (`/task list`)

```
/task list
/task list status=in_progress
/task list role=backend phase_id=2
/task list assignee=me
```

**Filters:**
- `status` - Filter by status
- `role` - Filter by role
- `phase_id` - Filter by phase
- `assignee` - Filter by assignee ("me" for current user)
- `priority` - Filter by priority

**Output format:**
```
📋 TASKS

Phase 2: Core Infrastructure (75% complete)
─────────────────────────────────────────────

🔴 Critical
├── t2-1: [backend] Implement rate limiting     → in_progress
└── t2-3: [frontend] Fix auth redirect          → review

🟠 High  
├── t2-5: [backend] Add pagination              → backlog
└── t2-6: [frontend] Dashboard loading states   → in_progress

🟡 Medium
└── t2-8: [devops] Update CI pipeline           → done ✅

Summary: 2 in_progress, 1 review, 1 backlog, 1 done
```

### View Task (`/task view`)

```
/task view t1-5
```

**Output format:**
```
📌 TASK: t1-5
═══════════════════════════════════════════════════════════════

Title:       Implement OAuth authentication
Status:      in_progress
Priority:    high
Role:        backend
Phase:       2 - Core Infrastructure
Assignee:    @developer

Description:
Add OAuth support for Google and GitHub authentication.
Must integrate with existing session management.

Created:     2024-12-10
Updated:     2024-12-15

Related:
├── Blocks: t1-8 (Frontend auth UI)
└── Blocked by: t1-2 (Auth middleware) ✅
```

## Guidelines

1. **Always log activities** after task changes
2. **Update phase progress** when completing tasks
3. **Use consistent ID format** (t{phase}-{number})
4. **Validate status transitions** (can't go from done to backlog)
5. **Check for blockers** before starting tasks

