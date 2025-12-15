# Task: [Task Title]

> **Task ID:** PM-{XXXXX}
> **Spec:** [SPEC-{YYYY}-{NNN}](link)
> **Status:** Open | In Progress | Review | Done
> **Created:** {date}

---

## Assignment

| Field | Value |
|-------|-------|
| **Assigned Agent** | `@agent-handle` |
| **Agent Name** | [Agent Name] |
| **Plugin** | `plugin-name` |
| **Skills** | `skill-1`, `skill-2` |

### CLI Invocation

```bash
# Start this task
/delegate @agent-handle "[Task Title]" --task PM-{XXXXX}

# Or directly invoke
/task start PM-{XXXXX}
```

---

## Context

### From Spec
- **Spec ID:** SPEC-{YYYY}-{NNN}
- **Acceptance Criteria:** AC-1, AC-2
- **Related Tasks:** PM-{prev}, PM-{next}

### Requirements

[Detailed requirements for this specific task]

### Dependencies

- [ ] PM-{dep1}: [Dependency description]
- [ ] PM-{dep2}: [Dependency description]

---

## Agent Instructions

> These instructions are provided to the assigned agent.

### Objective

[Clear, one-sentence objective]

### Scope

**In Scope:**
- [Item 1]
- [Item 2]

**Out of Scope:**
- [Item 1]
- [Item 2]

### Standards to Follow

| Standard | Source | Verification |
|----------|--------|--------------|
| [Standard 1] | `xalapm-core/standards/` | [How to verify] |
| [Standard 2] | Agent guidelines | [How to verify] |

### DO ✅

- [Specific instruction 1]
- [Specific instruction 2]
- [Specific instruction 3]

### DON'T ❌

- [Anti-pattern 1]
- [Anti-pattern 2]
- [Anti-pattern 3]

---

## Deliverables

| # | Deliverable | Type | Status |
|---|-------------|------|--------|
| 1 | [Deliverable 1] | Code | ⬜ |
| 2 | [Deliverable 2] | Test | ⬜ |
| 3 | [Deliverable 3] | Docs | ⬜ |

---

## Verification

### Automated Checks

| Check | Command | Expected |
|-------|---------|----------|
| Tests pass | `npm test` | All green |
| Lint clean | `npm run lint` | No errors |
| Type check | `tsc --noEmit` | No errors |
| Security scan | `/security-scan` | No critical |

### Manual Verification

- [ ] Code review by `@code-reviewer`
- [ ] Security review by `@owasp-expert` (if applicable)
- [ ] Accessibility check by `@accessibility-expert` (if UI)

---

## Time Tracking

| Activity | Date | Hours | Note |
|----------|------|-------|------|
| Started | | | |
| [Activity] | | | |
| Completed | | | |
| **Total** | | | |

**Estimate:** {X}h
**Actual:** {Y}h

---

## Completion

### Proof of Done

- [ ] All deliverables complete
- [ ] All automated checks pass
- [ ] Manual verification complete
- [ ] PR submitted and approved
- [ ] Synced to Xala PM

### PR/Commit Reference

- PR: #[number]
- Commits: [hash1], [hash2]

### Notes

[Any notes for review or future reference]

---

## Xala PM Sync

```bash
# Complete this task
/task complete PM-{XXXXX} --proof "PR #XX merged, all tests passing"

# View in Xala PM
# https://xala.pm/tasks/PM-{XXXXX}
```

