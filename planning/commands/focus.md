---
description: Focus on MVP or Production scope - filter out distractions
arguments:
  - name: tier
    description: Focus tier (mvp, production, or all)
    required: true
  - name: show-deferred
    description: Show deferred items with strikethrough
    required: false
    default: false
---

# Focus Command

Enter focus mode to filter out distractions and see only what matters NOW.

## Purpose

> **When everything is a priority, nothing is.**

This command helps you:
- Hide P2/P3 tasks when focusing on MVP
- Reduce cognitive load
- See only actionable items
- Avoid getting distracted by "nice-to-haves"

## Usage

```bash
# Focus on MVP only (P0/P1 tasks)
/focus mvp

# Focus on Production tier (all quality gates)
/focus production

# Show everything (exit focus mode)
/focus all

# Show what's deferred
/focus mvp --show-deferred
```

## What Each Mode Shows

### MVP Focus Mode

```markdown
🎯 FOCUS MODE: MVP

Showing: P0 (Critical) + P1 (Important) tasks only
Hidden: P2 (Nice to Have) + P3 (Future)

## Active Tasks (MVP Scope)

### P0 - Critical (Must complete to ship)

| ID | Task | Status | Agent |
|----|------|--------|-------|
| T-001 | User authentication | 🔄 In Progress | @backend-dev |
| T-002 | Dashboard UI | ⬜ Pending | @frontend-dev |
| T-003 | Data persistence | ⬜ Pending | @supabase-dev |

### P1 - Important (Should complete for MVP)

| ID | Task | Status | Agent |
|----|------|--------|-------|
| T-004 | Error handling | ⬜ Pending | @backend-dev |
| T-005 | Loading states | ⬜ Pending | @frontend-dev |

---

📊 MVP Progress: 1/5 tasks complete (20%)

🎯 Next Action: Complete T-001 (User authentication)

---

💡 Hidden: 8 P2/P3 tasks (run `/focus all` to see)
```

### Production Focus Mode

```markdown
🏆 FOCUS MODE: Production

Showing: All tasks + quality gates
Quality Tier: Production (all 11 pillars required)

## Quality Gates Status

| Pillar | Status | Score |
|--------|--------|-------|
| Code Quality | ✅ | 95% |
| Tests | ⚠️ | 72% (need 80%) |
| Security | ✅ | A |
| Performance | ⚠️ | 85 (need 90) |
| Accessibility | ❌ | Not audited |
| Documentation | ⚠️ | 60% |

## Remaining Work

### To Pass Quality Gates

1. [ ] Increase test coverage to 80%
2. [ ] Run accessibility audit
3. [ ] Improve Lighthouse score
4. [ ] Complete documentation

### P2/P3 Tasks (Now Visible)

| ID | Task | Priority | Agent |
|----|------|----------|-------|
| T-010 | Animation polish | P2 | @frontend-dev |
| T-011 | Performance tuning | P2 | @backend-dev |
```

### Show All Mode

```markdown
📋 FOCUS MODE: All

Showing: All tasks, all priorities
Quality Tier: Full visibility

## All Tasks by Priority

### P0 - Critical
[P0 tasks...]

### P1 - Important  
[P1 tasks...]

### P2 - Nice to Have
[P2 tasks...]

### P3 - Future
[P3 tasks...]
```

## Focus Mode Benefits

| Benefit | How |
|---------|-----|
| **Reduced overwhelm** | See only what matters now |
| **Clear next action** | P0 tasks are always visible |
| **Progress clarity** | Track MVP vs Production separately |
| **Scope discipline** | P2/P3 items are hidden, not deleted |

## Integration

### With Finish Line

```bash
# Define what MVP means
/finish-line mvp

# Then focus on it
/focus mvp
```

### With Completion Status

```bash
# See progress toward focused tier
/focus mvp
/completion-status mvp
```

### With Task List

```bash
# Focus mode filters task list
/focus mvp
/backlog  # Shows only P0/P1 tasks
```

## Focus Mode Rules

### MVP Mode Filters

| Shows | Hides |
|-------|-------|
| P0 Critical tasks | P2 Nice-to-have tasks |
| P1 Important tasks | P3 Future tasks |
| MVP quality gates | Production-only gates |
| Blocking issues | Polish items |

### What Gets Deferred

When in MVP focus:
- Performance optimization (unless critical)
- Full accessibility audit (basic labels still required)
- Complete documentation (README only)
- Full test coverage (happy path only)
- Compliance audits (unless regulated)

## Output Format

```markdown
🎯 Focus Mode Activated: [TIER]

## Visible Scope

| Category | Showing | Hidden |
|----------|---------|--------|
| Tasks | [N] P0/P1 | [N] P2/P3 |
| Quality Gates | [N] MVP gates | [N] Production gates |

## Current Sprint

[Filtered task list based on focus tier]

## Quick Stats

- MVP Progress: [X]%
- Blockers: [N]
- Next Action: [Task]

---

To exit focus mode: `/focus all`
To see deferred items: `/focus mvp --show-deferred`
```

## Best Practices

1. **Start every session in MVP focus** until you ship
2. **Review P2/P3 weekly** to ensure nothing critical was mis-prioritized
3. **Promote tasks** if they become blockers (P2 → P1)
4. **Celebrate MVP** before switching to Production focus

## Remember

> "Focus is about saying no to the hundred other good ideas."
> — Steve Jobs

MVP focus means:
- ❌ Not ignoring quality
- ❌ Not skipping tests
- ✅ Doing the minimum to validate
- ✅ Getting feedback faster
- ✅ Shipping something real

---

*"Focus on finishing, not on having the most tasks."*

