---
description: Manage the task backlog - prioritize, groom, and organize tasks
arguments:
  - name: action
    description: Action (view, prioritize, groom, sprint)
    required: false
    default: view
---

# Backlog Management Command

Manage and organize the task backlog.

## Actions

### View Backlog (`/backlog` or `/backlog view`)

Display the current backlog organized by priority and phase.

```
📋 BACKLOG
═══════════════════════════════════════════════════════════════

🔴 CRITICAL (2 tasks)
──────────────────────────────────────────────────────────────
t2-1: [backend] Fix authentication bypass vulnerability
      Phase: 2 | Est: 4h | Created: 2 days ago
      
t2-3: [frontend] Resolve hydration errors blocking release  
      Phase: 2 | Est: 2h | Created: 1 day ago

🟠 HIGH (5 tasks)
──────────────────────────────────────────────────────────────
t2-5: [backend] Implement rate limiting for API
      Phase: 2 | Est: 8h | Created: 5 days ago

t3-1: [frontend] Build dashboard charts component
      Phase: 3 | Est: 12h | Created: 3 days ago
      
[... more tasks ...]

🟡 MEDIUM (12 tasks)
──────────────────────────────────────────────────────────────
[Collapsed - use /backlog view priority=medium to expand]

🟢 LOW (8 tasks)
──────────────────────────────────────────────────────────────
[Collapsed - use /backlog view priority=low to expand]

──────────────────────────────────────────────────────────────
SUMMARY
Total: 27 tasks | Critical: 2 | High: 5 | Medium: 12 | Low: 8
Estimated: 156 hours | Oldest: 14 days
```

### Prioritize (`/backlog prioritize`)

Interactively prioritize tasks based on impact and urgency.

```
/backlog prioritize
```

**Process:**
1. Analyze all backlog tasks
2. Consider:
   - Dependencies (what blocks what)
   - Business impact
   - Technical risk
   - Time in backlog
3. Suggest priority changes
4. Apply changes after confirmation

**Output:**
```
🎯 PRIORITY RECOMMENDATIONS
═══════════════════════════════════════════════════════════════

📈 Recommend INCREASING priority:

t3-5: [backend] Add database indexes for slow queries
Current: medium → Recommended: high
Reason: Blocking 3 other tasks, performance impact

t2-8: [security] Update vulnerable dependencies  
Current: low → Recommended: critical
Reason: Security vulnerability, compliance requirement

📉 Recommend DECREASING priority:

t3-2: [frontend] Add dark mode support
Current: high → Recommended: medium
Reason: Nice-to-have, no dependencies, can defer

──────────────────────────────────────────────────────────────
Apply these changes? (y/n)
```

### Groom (`/backlog groom`)

Review and clean up the backlog.

```
/backlog groom
```

**Checks for:**
- Stale tasks (no updates in 30+ days)
- Duplicate or similar tasks
- Tasks missing estimates
- Tasks missing descriptions
- Orphaned tasks (no phase assigned)
- Completed tasks still in backlog

**Output:**
```
🧹 BACKLOG GROOMING
═══════════════════════════════════════════════════════════════

⚠️ STALE TASKS (no activity 30+ days)
t1-12: [frontend] Refactor form components (45 days)
       → Archive? Still relevant?

t1-15: [backend] Add caching layer (38 days)
       → Archive? Still relevant?

📝 MISSING ESTIMATES
t2-7: [devops] Set up staging environment
t2-9: [backend] Implement webhooks
       → Add estimates?

🔄 POTENTIAL DUPLICATES
t2-5 and t3-8 both mention "rate limiting"
       → Merge or differentiate?

✅ COMPLETED BUT NOT CLOSED
t1-8: [frontend] Login page UI (marked done 5 days ago)
       → Close and archive?

──────────────────────────────────────────────────────────────
Actions to take:
1. Archive 2 stale tasks
2. Add estimates to 2 tasks
3. Review 1 potential duplicate
4. Close 1 completed task
```

### Sprint Planning (`/backlog sprint`)

Suggest tasks for the next sprint based on capacity.

```
/backlog sprint capacity=40h
```

**Process:**
1. Get available capacity (hours)
2. Select tasks by priority (critical first)
3. Check dependencies
4. Balance across roles
5. Suggest sprint contents

**Output:**
```
🏃 SPRINT PLANNING
═══════════════════════════════════════════════════════════════

Capacity: 40 hours
Sprint: Week of Dec 16-20

RECOMMENDED SPRINT
──────────────────────────────────────────────────────────────

🔴 Critical (must include)
├── t2-1: Fix auth bypass [4h] - backend
└── t2-3: Fix hydration errors [2h] - frontend
    Subtotal: 6h

🟠 High (should include)
├── t2-5: Rate limiting [8h] - backend
├── t3-1: Dashboard charts [12h] - frontend
└── t2-7: Staging env [6h] - devops
    Subtotal: 26h

🟡 Medium (stretch goals)
└── t2-8: Update dependencies [4h] - devops
    Subtotal: 4h

──────────────────────────────────────────────────────────────
TOTAL: 36h / 40h capacity (90% utilized)

Role Distribution:
├── Backend: 12h (30%)
├── Frontend: 14h (35%)
└── DevOps: 10h (25%)

Accept this sprint plan? (y/n)
```

## Guidelines

1. **Regular grooming** keeps backlog healthy
2. **Prioritize by value** not just urgency
3. **Consider dependencies** in sprint planning
4. **Leave buffer** for unexpected work (80-90% capacity)
5. **Balance roles** to avoid bottlenecks

