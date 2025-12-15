# Planning Plugin - Ship Captain

> **Mission:** Help you finish projects and reach production. No more endless restarts.

Anti-overwhelm tools for developers who start many projects but struggle to ship.

## The Problem This Solves

```
❌ The AI Era Trap:
   Start project → Add features → Feel overwhelmed → Restart → Repeat

✅ The Ship Captain Way:
   Define finish line → Focus on MVP → Ship it → Iterate → Celebrate
```

## Philosophy

> "A shipped MVP teaches you more than a perfect spec ever could."
> — Captain Maya Torres, Ship Captain

- **Done > Perfect** — Ship, then iterate
- **Focus > Features** — Fewer things, done well
- **Momentum > Planning** — Movement creates clarity
- **Small wins > Big bangs** — Celebrate progress daily

## Commands

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/finish-line` | Define what "done" means for MVP | Start of any project |
| `/focus mvp` | Show only P0/P1 tasks | When feeling overwhelmed |
| `/focus production` | Show all tasks + quality gates | After MVP ships |
| `/completion-status` | Track progress toward shipping | Daily check-in |
| `/breakdown` | Break features into small tasks | Planning phase |
| `/estimate` | Estimate task effort | Sprint planning |

## Quick Start

### 1. Define Your Finish Line

```bash
/finish-line mvp
```

Answer: "What's the ONE thing a user must be able to do?"

### 2. Focus on MVP

```bash
/focus mvp
```

Hides P2/P3 distractions. Shows only critical path.

### 3. Check Progress Daily

```bash
/completion-status
```

See how close you are to shipping. Identify blockers.

### 4. Ship It!

When MVP Finish Line is 100% → Deploy → Celebrate 🎉

## Priority System

| Priority | Label | MVP? | What It Means |
|----------|-------|------|---------------|
| **P0** | 🔴 Critical | ✅ | Blocks shipping |
| **P1** | 🟠 Important | ✅ | Core UX improvement |
| **P2** | 🟡 Nice to Have | ❌ | Polish, defer to post-MVP |
| **P3** | ⚪ Future | ❌ | Ideas for later |

### Priority Decision Guide

```
Is this feature required for core user journey?
├─ YES → P0 (Critical)
└─ NO → Does it significantly improve UX?
        ├─ YES → P1 (Important)
        └─ NO → Is it just polish/optimization?
                ├─ YES → P2 (Nice to Have)
                └─ NO → P3 (Future)
```

## Quality Tiers

Instead of trying to meet ALL quality standards immediately, use tiers:

### Tier 1: MVP (Ship Fast)

| Required | Optional |
|----------|----------|
| ✅ Lint + TypeCheck | ⚡ Full test coverage |
| ✅ Happy path tests | ⚡ Complete docs |
| ✅ Basic security | ⚡ Accessibility audit |
| ✅ Build passes | ⚡ Performance tuning |

### Tier 2: Production (Ship Right)

| Required | Why |
|----------|-----|
| ✅ All MVP requirements | Foundation |
| ✅ 80% test coverage | Confidence |
| ✅ Full security audit | Protection |
| ✅ WCAG AA accessible | Inclusivity |
| ✅ Complete documentation | Maintenance |

## The Ship Captain Agent

Captain Maya Torres is your anti-overwhelm expert:

- 25 years shipping products
- 92% ship rate on projects she touches
- Specializes in getting stuck teams across the finish line

### When You're Stuck

```
User: "I have so many things to do, I don't know where to start."

Captain Torres: Let's define your finish line. What's the ONE thing 
a user must be able to do in your MVP? We'll build backward from there.
```

### When Scope Creeps

```
User: "I want to add dark mode before we launch."

Captain Torres: Dark mode is P2. Mark it for post-MVP. What P0 items 
are still open? Let's focus on those first.
```

## Workflows

### Starting a New Project

```bash
# 1. Define what "done" means
/finish-line mvp

# 2. Break down into tasks
/breakdown "User authentication feature"

# 3. Focus on MVP
/focus mvp

# 4. Start working on P0 tasks
```

### Daily Routine

```bash
# Morning: Check status
/completion-status

# Identify: What's the ONE blocker to fix today?

# Work on: P0 tasks only

# Evening: Update task status
/task done [task-id]
```

### When Overwhelmed

```bash
# 1. See reality
/completion-status

# 2. Hide distractions  
/focus mvp

# 3. Pick ONE thing
# What P0 task moves you closest to done?

# 4. Do that one thing
```

## Integration

### With Specs

```bash
/spec user-auth  # Creates spec with priority levels
```

### With Tasks

```bash
/task list --priority P0  # Show only critical tasks
```

### With Quality Gates

```bash
/quality-gate SPEC-001 --tier mvp  # MVP-tier checks only
```

## Anti-Patterns to Avoid

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Try to meet all quality standards immediately | Use MVP tier first |
| Add "one more feature" before shipping | Mark it P2, ship without |
| Work on P2/P3 when P0s are pending | `/focus mvp` |
| Plan for months without shipping | Define finish line, hit it |
| Restart when overwhelmed | Check completion status, refocus |

## The Shipping Mindset

```
┌─────────────────────────────────────────────────────────────────┐
│                     THE SHIPPING MINDSET                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│   ❌ Wrong: "I need to finish everything before I can ship"      │
│   ✅ Right: "What's the smallest thing I can ship today?"        │
│                                                                   │
│   ❌ Wrong: "This needs to be perfect"                           │
│   ✅ Right: "This needs to be good enough to get feedback"       │
│                                                                   │
│   ❌ Wrong: "Let me add one more feature..."                     │
│   ✅ Right: "That's P2, I'll add it after MVP ships"             │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Installation

```bash
/plugin install planning@xalapm-marketplace
```

## Success Metrics

| Metric | Target |
|--------|--------|
| Ship rate | 100% of started projects |
| Time to MVP | ≤4 weeks |
| Scope discipline | 50%+ deferred to post-MVP |
| Team morale | Energized, not burned out |

---

*"The best time to ship was yesterday. The second best time is today."*
— Captain Maya Torres

