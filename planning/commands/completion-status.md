---
description: Track overall project completion toward MVP or Production
arguments:
  - name: tier
    description: Which tier to check (mvp, production, or both)
    required: false
    default: both
  - name: detailed
    description: Show detailed breakdown
    required: false
    default: false
---

# Completion Status Command

See exactly how close you are to shipping. Track progress, not just tasks.

## Purpose

> **Problem:** "I have 47 tasks done but no idea when I'll ship."

This command helps you:
- See overall completion percentage
- Identify what's blocking MVP
- Track progress toward production
- Know your next most impactful action

## Usage

```bash
# Check both MVP and Production progress
/completion-status

# Check MVP progress only
/completion-status mvp

# Get detailed breakdown
/completion-status --detailed

# Check specific feature/spec
/completion-status --spec SPEC-2024-001
```

## Output Format

### Summary View (Default)

```markdown
# 📊 Completion Status

**Project:** [Project Name]
**Last Updated:** [Timestamp]
**Current Focus:** MVP

---

## 🚀 MVP Progress

```
████████░░░░░░░░░░░░ 40%
```

| Category | Progress | Status |
|----------|----------|--------|
| Core Features | ████████████░░ 85% | ⚠️ Almost |
| P0 Tasks | ██████████░░░░ 70% | ⚠️ In Progress |
| P1 Tasks | ██████░░░░░░░░ 45% | 🔄 Active |
| Basic Quality | ████████████░░ 90% | ✅ Good |
| Blockers | 2 items | ❌ Action Needed |

### 🚧 Blockers (Fix These First!)

1. **T-005: Payment integration** — P0, blocks checkout
   - Owner: @backend-dev
   - Blocked by: Waiting for Stripe keys
   
2. **T-008: User session bug** — P0, critical bug
   - Owner: @backend-dev
   - Action: Fix session expiry logic

### ✅ Recently Completed

- T-003: User authentication ✅
- T-004: Dashboard UI ✅
- T-007: Database schema ✅

### 🎯 Next Actions (Priority Order)

1. [ ] Unblock T-005 (get Stripe keys)
2. [ ] Fix T-008 (session bug)
3. [ ] Complete T-006 (error handling)

---

## 🏆 Production Progress

```
████░░░░░░░░░░░░░░░░ 20%
```

| Category | Progress | Status |
|----------|----------|--------|
| MVP Complete | ░░░░░░░░░░░░░░ 0% | ⬜ Pending MVP |
| Test Coverage | ████░░░░░░░░░░ 32% | ⚠️ Need 80% |
| Quality Gates | ██░░░░░░░░░░░░ 15% | ⚠️ 2/10 pass |
| Documentation | ██░░░░░░░░░░░░ 20% | ⚠️ README only |

> ℹ️ Production progress will accelerate after MVP ships.

---

## 📈 Velocity

| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Tasks Completed | 5 | 3 | 📈 +67% |
| P0 Tasks Done | 2 | 1 | 📈 |
| Blockers Resolved | 1 | 2 | 📉 |

**Estimated MVP Ship Date:** [Date] (based on current velocity)

---

💡 **Tip:** Run `/focus mvp` to hide P2/P3 distractions.
```

### Detailed View (--detailed)

```markdown
# 📊 Completion Status (Detailed)

## MVP Breakdown

### Core Features (85% complete)

| Feature | Status | Remaining Work |
|---------|--------|----------------|
| User Auth | ✅ 100% | — |
| Dashboard | ✅ 100% | — |
| Data Entry | 🔄 80% | Form validation |
| Reports | ⚠️ 60% | Export feature |
| Settings | ⬜ 0% | Not started |

### Tasks by Priority

#### P0 - Critical (70% complete)

| ID | Task | Status | Owner | Blocking? |
|----|------|--------|-------|-----------|
| T-001 | Auth API | ✅ Done | @backend-dev | No |
| T-002 | Login UI | ✅ Done | @frontend-dev | No |
| T-003 | Session mgmt | ✅ Done | @backend-dev | No |
| T-005 | Payment | ❌ Blocked | @backend-dev | **YES** |
| T-008 | Session bug | 🔄 Active | @backend-dev | **YES** |

#### P1 - Important (45% complete)

| ID | Task | Status | Owner |
|----|------|--------|-------|
| T-006 | Error handling | ⬜ Pending | @backend-dev |
| T-007 | Loading states | 🔄 Active | @frontend-dev |
| T-009 | Form validation | ⬜ Pending | @frontend-dev |

### Quality Gates (MVP Tier)

| Gate | Status | Details |
|------|--------|---------|
| Lint | ✅ Pass | 0 errors |
| TypeCheck | ✅ Pass | 0 errors |
| Build | ✅ Pass | Successful |
| Tests | ⚠️ Partial | 52% coverage (need 50% MVP) |
| Security | ⚠️ Partial | 1 medium issue |

### Deferred to Post-MVP

| Item | Priority | Why Deferred |
|------|----------|--------------|
| Animations | P2 | Polish |
| Dark mode | P2 | Nice-to-have |
| Analytics | P3 | Future |
| API docs | P2 | After MVP |

---

## Production Breakdown

### Quality Gates (Production Tier)

| Gate | Required | Current | Status |
|------|----------|---------|--------|
| Test Coverage | 80% | 52% | ❌ |
| Lint | 0 errors | 0 | ✅ |
| TypeCheck | 0 errors | 0 | ✅ |
| Security Scan | A | B | ⚠️ |
| Accessibility | AA | Not run | ❌ |
| Performance | 90 | Not run | ❌ |
| Documentation | 80% | 20% | ❌ |

### Work Remaining for Production

| Category | Tasks | Estimated Hours |
|----------|-------|-----------------|
| Test Coverage | 12 tests | 8h |
| Security Fixes | 3 issues | 4h |
| Accessibility | 1 audit + fixes | 6h |
| Documentation | 15 functions | 4h |
| Performance | 5 optimizations | 6h |
| **Total** | — | **28h** |
```

## Metrics Tracked

### MVP Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| P0 Completion | Critical tasks done | 100% |
| P1 Completion | Important tasks done | 80% |
| Core Features | Main functionality works | 100% |
| Blockers | Issues blocking progress | 0 |
| Basic Quality | Lint, types, build | Pass |

### Production Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| All MVP Metrics | Must pass first | ✅ |
| Test Coverage | Statement coverage | ≥80% |
| Quality Gates | All 10 pillars | Pass |
| Documentation | JSDoc coverage | ≥80% |
| Security | OWASP compliance | A |
| Accessibility | WCAG level | AA |
| Performance | Lighthouse score | ≥90 |

## Integration

### With Xala PM

```bash
# Sync completion status to Xala PM
/completion-status --sync

# Update project dashboard
```

### With Focus Mode

```bash
# Focus on tier with lowest completion
/completion-status mvp
/focus mvp  # Focus on what's needed
```

### With Finish Line

```bash
# Compare status to finish line
/finish-line status
/completion-status
```

## Calculation Method

### MVP Completion %

```
MVP % = (P0_done/P0_total × 50%) + (P1_done/P1_total × 30%) + (quality_gates × 20%)

Where:
- P0 tasks are weighted 50% (most critical)
- P1 tasks are weighted 30% (important)
- Quality gates are weighted 20% (must pass)
```

### Production Completion %

```
Production % = (MVP_complete × 40%) + (quality_gates × 40%) + (extras × 20%)

Where:
- MVP completion is prerequisite (40%)
- All quality gates must pass (40%)
- Extras: docs, monitoring, polish (20%)
```

## Best Practices

1. **Check daily** — Start each day with `/completion-status`
2. **Fix blockers first** — They have outsized impact
3. **Celebrate milestones** — 50%, 80%, 100% are worth noting
4. **Update status** — Keep task statuses current

## Remember

> "You can't manage what you can't measure."

Completion status tells you:
- Where you ARE (not where you hoped to be)
- What's ACTUALLY blocking you
- When you'll REALISTICALLY ship
- What to work on NEXT

---

*"Progress is measured by shipped features, not busy tasks."*

