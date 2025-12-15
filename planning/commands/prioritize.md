---
description: Assign priority levels (P0-P3) to tasks for MVP vs Production focus
arguments:
  - name: task
    description: Task ID or description to prioritize
    required: false
  - name: bulk
    description: Prioritize all unprioritized tasks
    required: false
    default: false
---

# Prioritize Command

Assign P0/P1/P2/P3 priorities to tasks. Critical for MVP focus.

## Purpose

> **Not everything is equally important.** Priority levels help you focus.

This command helps you:
- Distinguish MVP-critical from nice-to-have
- Avoid scope creep
- Know what to work on next
- Ship faster by deferring correctly

## Usage

```bash
# Prioritize a specific task
/prioritize T-005

# Bulk prioritize all tasks
/prioritize --bulk

# Prioritize with explicit level
/prioritize T-005 --level P0
```

## Priority Levels

| Priority | Emoji | Name | For MVP? | When to Use |
|----------|-------|------|----------|-------------|
| **P0** | 🔴 | Critical | ✅ Yes | Blocks shipping |
| **P1** | 🟠 | Important | ✅ Yes | Core UX improvement |
| **P2** | 🟡 | Nice to Have | ❌ No | Polish, can defer |
| **P3** | ⚪ | Future | ❌ No | Ideas for later |

## Decision Framework

When prioritizing a task, ask these questions in order:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRIORITY DECISION TREE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Q1: Can the user complete their core journey without this?      │
│      ├─ NO  → 🔴 P0 (Critical)                                   │
│      └─ YES → Go to Q2                                           │
│                                                                   │
│  Q2: Does this significantly improve the core experience?        │
│      ├─ YES → 🟠 P1 (Important)                                  │
│      └─ NO  → Go to Q3                                           │
│                                                                   │
│  Q3: Is this polish, optimization, or edge case handling?        │
│      ├─ YES → 🟡 P2 (Nice to Have)                               │
│      └─ NO  → ⚪ P3 (Future)                                     │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Examples by Category

### P0 - Critical (Must ship with this)

| Task Type | Example |
|-----------|---------|
| Core functionality | User login/logout |
| Data integrity | Save user data |
| Security | Password hashing |
| Blocking bugs | App crashes on load |
| Legal requirements | Terms acceptance |

### P1 - Important (Should ship with this)

| Task Type | Example |
|-----------|---------|
| UX improvements | Loading indicators |
| Error handling | Friendly error messages |
| Quick wins | Form validation |
| Polish | Consistent button styles |

### P2 - Nice to Have (Ship after MVP)

| Task Type | Example |
|-----------|---------|
| Optimization | Image lazy loading |
| Additional features | Dark mode |
| Advanced options | Keyboard shortcuts |
| Analytics | Usage tracking |

### P3 - Future (Backlog for later)

| Task Type | Example |
|-----------|---------|
| Future integrations | Third-party apps |
| Nice ideas | AI-powered features |
| Scalability | Multi-tenant support |
| Platform expansion | Mobile app |

## Process

### Single Task Prioritization

When you run `/prioritize T-005`, I'll:

1. **Show task details**
2. **Ask the three questions**
3. **Recommend a priority**
4. **Update the task**

```markdown
## Task: T-005 - Dark mode support

### Priority Analysis

| Question | Answer | Implication |
|----------|--------|-------------|
| Can user complete core journey without? | ✅ Yes | Not P0 |
| Significantly improves core experience? | ❌ No | Not P1 |
| Is it polish/optimization? | ✅ Yes | P2 |

### Recommendation: 🟡 P2 (Nice to Have)

**Reason:** Dark mode is polish. Users can complete all core tasks with light mode. Defer to post-MVP.

**Action:** Mark as P2 and add to post-MVP backlog?
```

### Bulk Prioritization

When you run `/prioritize --bulk`, I'll:

1. **List all unprioritized tasks**
2. **Walk through each one**
3. **Group by recommended priority**
4. **Apply in batch**

```markdown
## Bulk Prioritization

Found 12 unprioritized tasks.

### Recommended Priorities

#### 🔴 P0 - Critical (3 tasks)
| Task | Reason |
|------|--------|
| T-001: User auth | Core functionality |
| T-003: Data save | Data integrity |
| T-007: Fix crash bug | Blocking |

#### 🟠 P1 - Important (4 tasks)
| Task | Reason |
|------|--------|
| T-002: Error messages | UX improvement |
| T-005: Form validation | Quick win |

#### 🟡 P2 - Nice to Have (3 tasks)
| Task | Reason |
|------|--------|
| T-008: Dark mode | Polish |
| T-010: Animations | Nice-to-have |

#### ⚪ P3 - Future (2 tasks)
| Task | Reason |
|------|--------|
| T-011: Mobile app | Future scope |
| T-012: AI features | Ideas |

### Apply these priorities? (y/n)
```

## Common Mistakes

### Over-Prioritizing (Making Everything P0)

```markdown
❌ Wrong: "Everything is critical!"
   Result: Nothing is actually prioritized

✅ Right: Be honest about what BLOCKS shipping
   Only 2-4 things should be P0
```

### Under-Prioritizing (Deferring Too Much)

```markdown
❌ Wrong: "We'll add error handling after MVP"
   Result: Users see ugly errors

✅ Right: Basic error handling is P1
   Users need friendly feedback
```

### Priority Creep (P2 → P1 → P0)

```markdown
❌ Wrong: "Actually, dark mode is really important..."
   Result: Scope creep, delayed shipping

✅ Right: Stick to your priorities unless:
   - New information changes the situation
   - Users explicitly request it
   - It becomes a blocker
```

## Integration

### With Focus Mode

```bash
# After prioritizing, focus on MVP
/focus mvp  # Shows P0 + P1 only
```

### With Task List

```bash
# View tasks by priority
/task list --priority P0
/task list --priority P1
```

### With Specs

```bash
# Specs include priority section
/spec new-feature  # Generates with priority matrix
```

## Best Practices

1. **Prioritize early** — Before starting work
2. **Be ruthless** — Only 2-4 P0 items
3. **Defer liberally** — P2/P3 is fine for most things
4. **Re-assess sparingly** — Don't re-prioritize constantly
5. **Ship P0/P1 first** — Always

## Remember

> "If everything is P0, nothing is P0."

Priorities help you:
- Know what to work on next
- Say "not yet" to good ideas
- Ship something real
- Stop feeling overwhelmed

---

*"Ruthless prioritization is kindness to your future self."*

