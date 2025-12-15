# Xala PM Integration Protocol

All agents MUST follow this protocol to keep Xala PM synchronized.

## Core Principle

> Every action that changes project state MUST be reflected in Xala PM.

## Integration Rules

### Rule 1: Task Lifecycle

When starting ANY task:
```
1. FIRST: update_task task_id="<id>" status="in_progress"
2. THEN: log_activity type="task_update" title="Started <task>" entity_type="task" entity_id="<id>"
3. FINALLY: Begin the actual work
```

When completing ANY task:
```
1. FIRST: Finish the actual work
2. THEN: update_task task_id="<id>" status="done"
3. THEN: log_activity type="task_update" title="Completed <task>" entity_type="task" entity_id="<id>"
4. FINALLY: update_phase phase_id=<n> progress=<new_percentage> (if applicable)
```

### Rule 2: Activity Logging

Every significant action MUST be logged:

```typescript
interface ActivityLog {
  type: 'task_update' | 'code_change' | 'review' | 'deployment' | 'analysis' | 'compliance'
  title: string           // Human-readable description
  description?: string    // Optional details
  entity_type: 'task' | 'project' | 'phase' | 'repository'
  entity_id: string       // ID of the affected entity
  metadata?: {
    agent: string         // Which agent performed the action
    changes?: object      // What was changed
    artifacts?: string[]  // Created files, URLs, etc.
  }
}
```

### Rule 3: Project Context

Before any work, agents MUST:
1. Check current project context from Xala PM
2. Verify they're working on the correct project
3. Load relevant project metadata (PRD, phases, tasks)

### Rule 4: Cross-Agent Communication

When work affects multiple domains:
```
1. Primary agent completes work
2. Primary agent logs activity with cross-references
3. Primary agent notifies relevant agents via activity log
4. Orchestrator can trigger follow-up agent actions
```

## MCP Tools Reference

All agents have access to these Xala PM tools:

### Task Management
| Tool | Description |
|------|-------------|
| `get_tasks` | List tasks (filter by status, role, phase) |
| `get_task` | Get single task details |
| `create_task` | Create new task |
| `update_task` | Update task status, assignee, etc. |
| `delete_task` | Delete a task |

### Phase Management
| Tool | Description |
|------|-------------|
| `get_phases` | List all project phases |
| `update_phase` | Update phase progress/status |

### Activity Logging
| Tool | Description |
|------|-------------|
| `log_activity` | Log an activity to the feed |
| `get_activity` | Get recent activity |

### Project Management
| Tool | Description |
|------|-------------|
| `get_dashboard_stats` | Get project statistics |
| `get_repositories` | List connected repositories |
| `update_repository` | Update repository info |

### Compliance
| Tool | Description |
|------|-------------|
| `get_compliance` | Get compliance status |
| `update_compliance` | Update compliance check |

## Agent-Specific Protocols

### Frontend Agent
When completing UI work:
```
log_activity(
  type="code_change",
  title="Created {component} component",
  entity_type="task",
  entity_id="{task_id}",
  metadata={
    agent: "frontend",
    artifacts: ["src/components/{Component}.tsx"],
    changes: { files_created: 1, lines_added: X }
  }
)
```

### Backend Agent
When completing API work:
```
log_activity(
  type="code_change",
  title="Implemented {endpoint} endpoint",
  entity_type="task",
  entity_id="{task_id}",
  metadata={
    agent: "backend",
    artifacts: ["src/routes/{route}.ts"],
    changes: { endpoints_added: 1 }
  }
)
```

### Testing Agent
When completing tests:
```
log_activity(
  type="code_change",
  title="Added tests for {feature}",
  entity_type="task",
  entity_id="{task_id}",
  metadata={
    agent: "testing",
    artifacts: ["tests/{feature}.test.ts"],
    changes: { tests_added: X, coverage: Y }
  }
)
```

### Code Review Agent
When completing review:
```
log_activity(
  type="review",
  title="Reviewed PR #{pr_number}",
  entity_type="task",
  entity_id="{task_id}",
  metadata={
    agent: "code-review",
    changes: { 
      issues_found: X,
      blocking: Y,
      approved: boolean
    }
  }
)
```

### Repo Analysis Agent
When completing analysis:
```
log_activity(
  type="analysis",
  title="Analyzed repository {repo_name}",
  entity_type="project",
  entity_id="{project_id}",
  metadata={
    agent: "repo-analysis",
    changes: {
      files_analyzed: X,
      issues_found: Y,
      tasks_created: Z
    }
  }
)
// Also create tasks for findings
for each finding:
  create_task(...)
```

### Compliance Agent
When completing audit:
```
log_activity(
  type="compliance",
  title="Completed {type} compliance audit",
  entity_type="project",
  entity_id="{project_id}",
  metadata={
    agent: "accessibility" | "compliance",
    changes: {
      checks_passed: X,
      checks_failed: Y,
      score: Z
    }
  }
)
update_compliance(...)
```

## Project Document Sync

When creating or updating project documents:

### PRD Creation/Update
```
1. Generate PRD content
2. Save to docs/PRD.md
3. Update project in database:
   update_project(
     project_id="{id}",
     prd_content="{content}",
     prd_updated_at=now()
   )
4. Log activity:
   log_activity(
     type="analysis",
     title="Updated PRD for {project_name}",
     entity_type="project",
     entity_id="{project_id}"
   )
```

### Phase Updates from Analysis
```
1. Analyze project structure
2. Infer phases and deliverables
3. Update phases:
   for each phase:
     update_phase(phase_id, { deliverables, progress })
4. Log activity with summary
```

## Notifications

Agents should trigger notifications for:
- Task completed → notify PM / team
- Blocking issue found → notify assignee
- Compliance violation → notify compliance officer
- Deployment ready → notify DevOps

```typescript
// Notification trigger (via activity log)
log_activity(
  type="task_update",
  title="🔴 BLOCKING: Security vulnerability in auth",
  entity_type="task",
  entity_id="{task_id}",
  metadata={
    priority: "critical",
    notify: ["pm", "security-lead"],
    action_required: true
  }
)
```

