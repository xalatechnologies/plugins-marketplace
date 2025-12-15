---
description: Define what "done" means for MVP and Production tiers
arguments:
  - name: tier
    description: Quality tier (mvp or production)
    required: false
    default: mvp
  - name: project
    description: Project name or ID
    required: false
---

# Finish Line Command

Define clear, achievable finish lines for your project. Stop the endless "one more thing" cycle.

## Purpose

> **The #1 reason projects don't ship:** No clear definition of "done."

This command helps you:
- Define exactly what MVP means for YOUR project
- Create a checklist you can actually complete
- Avoid scope creep and perfectionism
- Know when you're DONE

## Usage

```bash
# Define MVP finish line (recommended first)
/finish-line mvp

# Define production finish line
/finish-line production

# Check current finish line status
/finish-line status
```

## Process

### Step 1: Define Core User Journey

Ask the user:
1. **Who** is the primary user?
2. **What** is the ONE thing they must be able to do?
3. **What** makes this feature "working"?

### Step 2: List MVP Requirements

Generate a focused checklist:

```markdown
## 🎯 MVP Finish Line: [Project/Feature Name]

> **Ship Date Target:** [Date]
> **Tier:** MVP
> **Status:** In Progress | Ready to Ship | Shipped

### Core Requirements (P0)

- [ ] [Core feature 1] — User can [action]
- [ ] [Core feature 2] — System [behavior]
- [ ] [Core feature 3] — Data [persistence/validation]

### Basic Quality (P0)

- [ ] Lint passes (`npm run lint`)
- [ ] TypeCheck passes (`tsc --noEmit`)
- [ ] Build succeeds (`npm run build`)
- [ ] No critical security issues
- [ ] Core happy path works

### Deferred to Post-MVP (P2/P3)

| Feature | Priority | Reason for Deferral |
|---------|----------|---------------------|
| [Feature A] | P2 | Nice-to-have, not core |
| [Feature B] | P3 | Future enhancement |
| [Optimization C] | P2 | Works fine for now |

### Definition of "Ship Ready"

- [ ] Can deploy to production
- [ ] Core user journey works
- [ ] No critical bugs
- [ ] Team has tested internally
- [ ] Stakeholder has approved MVP scope
```

### Step 3: Production Finish Line (if requested)

```markdown
## 🏆 Production Finish Line: [Project/Feature Name]

> **Target Date:** [Date]
> **Tier:** Production
> **Prerequisite:** MVP shipped ✅

### All MVP Requirements

- [x] MVP Finish Line complete

### Quality Gates

- [ ] Test coverage ≥80%
- [ ] All quality gates pass (`/quality-gate SPEC-XXX`)
- [ ] Security audit complete
- [ ] Accessibility audit (WCAG AA)
- [ ] Documentation complete

### Performance

- [ ] Lighthouse score ≥90
- [ ] API response time p95 ≤200ms
- [ ] No N+1 queries
- [ ] Caching implemented

### Operational Readiness

- [ ] Monitoring set up
- [ ] Alerting configured
- [ ] Runbook documented
- [ ] Rollback plan tested
- [ ] Error tracking enabled
```

## Output Format

```markdown
# 🎯 Finish Line Defined

## MVP Finish Line

**Project:** [Name]
**Target Ship Date:** [Date]
**Total Checkboxes:** [N]
**Current Progress:** [X/N] ([%])

### Checklist

[Generated checklist based on conversation]

### Next Actions

1. [ ] First P0 task to complete
2. [ ] Second P0 task to complete
3. [ ] Third P0 task to complete

### Deferred Items

| Item | Priority | Ship After MVP |
|------|----------|----------------|
| [Item] | P2 | Yes |

---

💡 **Tip:** Run `/completion-status` daily to track progress toward this finish line.
```

## Integration

### With Xala PM

```bash
# Create finish line as a milestone
/task create "MVP Finish Line" --type milestone --spec SPEC-XXX

# Link P0 tasks to milestone
/task update [task-id] --milestone "MVP Finish Line"
```

### With Focus Mode

```bash
# After defining finish line, enter focus mode
/focus mvp

# Only shows tasks that contribute to MVP finish line
```

## Anti-Overwhelm Tips

1. **Start small** — 5-7 checklist items for MVP
2. **Be ruthless** — If it's not P0, defer it
3. **Ship ugly** — A working MVP beats a beautiful spec
4. **Celebrate** — Mark the finish line as DONE when you ship

## Remember

> "A finished MVP in users' hands is worth more than a perfect product in your head."

- MVP is not "minimum quality" — it's "minimum scope"
- You can always add more AFTER shipping
- Feedback from real users > your assumptions
- Shipping builds momentum

---

*"Define the finish line, run toward it, cross it. Then set a new one."*

