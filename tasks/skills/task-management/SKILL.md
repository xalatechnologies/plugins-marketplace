---
description: Task management expertise - creating, updating, and tracking tasks automatically
triggers:
  - starting work on a feature
  - completing work
  - discussing tasks or backlog
  - creating new functionality
  - fixing bugs
---

# Task Management Skill

Autonomous task management capabilities for keeping Xala PM in sync.

## Auto-Detection Triggers

### Detect Task Start
When you see patterns like:
- "I'm going to work on..."
- "Let me implement..."
- "Starting on the..."
- "I'll fix this..."
- User opens files related to a task

**Action:** Check if related task exists and offer to update status.

### Detect Task Completion
When you see patterns like:
- "Done!"
- "That should fix it"
- "Implemented the..."
- "Finished the..."
- Successful test/build after changes

**Action:** Offer to mark task as done and update phase progress.

### Detect New Work
When you see patterns like:
- "We also need to..."
- "I noticed we should..."
- "Can you add..."
- Work that isn't in any existing task

**Action:** Offer to create a new task for this work.

## Intelligent Task Matching

When user mentions work, match to existing tasks:

```typescript
// Matching logic
function matchWorkToTask(work: string, tasks: Task[]): Task | null {
  // 1. Exact task ID mention
  const idMatch = work.match(/t\d+-\d+/)
  if (idMatch) return findTask(idMatch[0])
  
  // 2. Keyword matching
  const keywords = extractKeywords(work)
  const matches = tasks.filter(t => 
    keywords.some(k => t.title.toLowerCase().includes(k))
  )
  
  // 3. File path matching
  if (workingOnFile) {
    const fileMatches = tasks.filter(t =>
      t.related_files?.includes(workingOnFile)
    )
    if (fileMatches.length === 1) return fileMatches[0]
  }
  
  return matches.length === 1 ? matches[0] : null
}
```

## Task Suggestions

### When to Suggest Task Creation

- Bug fix that wasn't planned
- Refactoring discovered during work
- Documentation that needs updating
- Test coverage gaps
- Technical debt identified

**Example:**
```
💡 I noticed you're fixing a bug in the auth flow that wasn't planned.
   Would you like me to create a task for this?

   Suggested:
   - Title: Fix OAuth token refresh race condition
   - Role: backend
   - Priority: high
   - Phase: 2

   Create this task? (y/n)
```

### When to Suggest Status Updates

- Work in progress on backlog task
- Pull request merged
- Tests passing after fix
- User says "done" or similar

**Example:**
```
✅ It looks like you've completed the OAuth implementation.
   Should I update t2-5 to "done"?
   
   This will also update Phase 2 progress from 45% to 52%.
   
   Update task? (y/n)
```

## Phase Progress Calculation

```typescript
function calculatePhaseProgress(phaseId: number): number {
  const phaseTasks = await getTasks({ phase_id: phaseId })
  const completed = phaseTasks.filter(t => t.status === 'done').length
  const total = phaseTasks.length
  
  return Math.round((completed / total) * 100)
}
```

## Dependency Tracking

### Detect Blockers
Check for blocked tasks when:
- Starting a task with dependencies
- Completing a task that blocks others

**Example:**
```
⚠️ Task t2-8 depends on t2-5 which is still in progress.
   You may be blocked until t2-5 is complete.
   
   View t2-5 status? (y/n)
```

### Notify Unblocked
When completing a task:

```
🔓 Completing t2-5 will unblock these tasks:
   - t2-8: Implement user notifications
   - t2-9: Add email templates
   
   Should I update their status to ready?
```

## Activity Logging

Always log significant events:

```typescript
// Task started
log_activity({
  type: "task_update",
  title: `Started: ${task.title}`,
  entity_type: "task",
  entity_id: task.id
})

// Task completed
log_activity({
  type: "task_update", 
  title: `Completed: ${task.title}`,
  entity_type: "task",
  entity_id: task.id
})

// Task created
log_activity({
  type: "task_update",
  title: `Created: ${task.title}`,
  entity_type: "task", 
  entity_id: task.id
})
```

## When to Use

Apply this skill automatically when:
- User discusses work to be done
- Code changes are being made
- User mentions tasks or backlog
- Work is completed
- New features/fixes are requested

