# Ship Captain Skill - Anti-Overwhelm Strategies

> Your toolkit for finishing projects and reaching production.

## Purpose

This skill helps you:
- Overcome analysis paralysis
- Focus on what matters for MVP
- Avoid scope creep
- Ship products instead of restarting

## Core Principles

### 1. Define the Finish Line First

Before writing any code:

```markdown
## My MVP Finish Line

The ONE thing a user must be able to do:
[Write it here]

When this works end-to-end, MVP is done:
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
```

### 2. Use Quality Tiers

| Tier | When | Quality Level |
|------|------|---------------|
| **MVP** | First launch | Good enough to get feedback |
| **Production** | After MVP ships | Enterprise-grade |

Don't try to hit Production quality before shipping MVP.

### 3. Priority-Based Task Management

| Priority | Action |
|----------|--------|
| P0 | Do now, blocks shipping |
| P1 | Do now, improves core UX |
| P2 | Defer to post-MVP |
| P3 | Backlog for future |

### 4. Daily Focus Ritual

```bash
# Every morning:
/completion-status   # Where am I?
/focus mvp          # What should I see?
# Then: Pick ONE P0 task and finish it
```

## When You Feel Overwhelmed

### Step 1: Stop and Breathe

Overwhelm is a signal, not a failure. It means you need to refocus.

### Step 2: Check Reality

```bash
/completion-status
```

Often you're further along than you think.

### Step 3: Identify the ONE Blocker

Ask: "What is the ONE thing that, if done, makes everything else easier?"

That's your next task. Ignore everything else.

### Step 4: Make It Smaller

If the blocker feels too big:
- Break it into 30-minute chunks
- Ask: "What's the smallest step I can take?"
- Do that step. Then the next.

### Step 5: Ship Ugly

Perfect is the enemy of done:
- Working > Pretty
- Shipped > Planned
- Feedback > Assumptions

## Common Anti-Patterns

### Pattern 1: The Endless Planner

```
❌ "I need to plan everything before I start"
✅ "I need to define MVP and start building"
```

**Fix:** Set a planning limit (2 hours max), then start coding.

### Pattern 2: The Feature Hoarder

```
❌ "Let me just add one more feature..."
✅ "That's P2. Adding it to post-MVP backlog."
```

**Fix:** Every new idea gets a priority. P2/P3 = after MVP.

### Pattern 3: The Perfectionist

```
❌ "This needs to be perfect before I show anyone"
✅ "This needs to work well enough to get feedback"
```

**Fix:** Use MVP quality tier. Ship, then polish.

### Pattern 4: The Restarter

```
❌ "This is getting complicated. Let me start over with a better architecture..."
✅ "Let me ship what I have and improve it iteratively"
```

**Fix:** Restarts are almost never faster. Push through.

### Pattern 5: The Comparison Trap

```
❌ "Product X has all these features. Mine needs them too."
✅ "What does MY user need to accomplish their goal?"
```

**Fix:** Focus on YOUR MVP, not competitors' mature products.

## Tactical Advice

### For Starting a New Project

1. `/finish-line mvp` — Define done
2. `/breakdown [feature]` — Create tasks
3. `/prioritize --bulk` — Assign P0/P1/P2/P3
4. `/focus mvp` — Hide distractions
5. Start the first P0 task

### For Getting Unstuck

1. `/completion-status` — See progress
2. Identify the ONE blocker
3. Break it into 30-min chunks
4. Do the first chunk
5. Celebrate small wins

### For Avoiding Scope Creep

1. Every new idea → `/prioritize [idea]`
2. If P2/P3 → "Great idea for v2!"
3. If P0/P1 → Add to current sprint
4. Review priorities weekly

### For Shipping

1. All P0 tasks done?
2. All P1 tasks done (or explicitly deferred)?
3. MVP quality gates pass?
4. If yes → **SHIP IT**

## Mantras

When you need a mindset shift:

| Situation | Mantra |
|-----------|--------|
| Overwhelmed | "What's the ONE thing?" |
| Perfectionist | "Done is better than perfect" |
| Scope creep | "That's a P2" |
| Wanting to restart | "Ship first, refactor later" |
| Comparing to others | "My MVP, my rules" |
| Stuck | "What's the smallest step?" |

## Success Metrics

You're using this skill well when:

| Metric | Target |
|--------|--------|
| MVP ships | Within 4 weeks of starting |
| P2/P3 items deferred | 50%+ of total tasks |
| Daily P0/P1 focus | 80%+ of work time |
| Restart frequency | Zero |
| Shipped vs started ratio | 100% |

## Integration with Other Skills

| Situation | Use |
|-----------|-----|
| Need task breakdown | `/breakdown` |
| Need time estimates | `/estimate` |
| Need to check quality | `/quality-gate --tier mvp` |
| Need to delegate | `/delegate @agent "task"` |

---

*"The ship that reaches port beats the ship still being designed."*

