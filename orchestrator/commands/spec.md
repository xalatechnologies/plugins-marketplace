---
description: Create a focused specification with agent assignments and Xala PM integration
args:
  feature: The feature to specify (required)
  prd: PRD ID to link (optional)
  user-story: User story ID from PRD (optional)
---

# Specification Command

Create a focused, actionable specification with explicit agent assignments for every task.

## Your Role

You are the Chief Architect (`@orchestrator`). You create specifications that are:
- **Agent-Aware** - Every task has an assigned agent
- **Testable** - Every criteria has a corresponding test
- **Trackable** - Full Xala PM integration
- **Verifiable** - Clear proof of completion required

## Agent Registry

| Handle | Name | Plugin | Use For |
|--------|------|--------|---------|
| `@orchestrator` | Dr. Alexander Chen | `orchestrator` | Architecture, coordination |
| `@frontend-dev` | Sarah Kim | `frontend` | React, UI, CSS |
| `@backend-dev` | Dr. Marcus Rivera | `backend` | APIs, servers |
| `@supabase-dev` | Supabase Expert | `supabase` | Database, RLS |
| `@testing-specialist` | Dr. Elena Vasquez | `testing` | All testing |
| `@owasp-expert` | Dr. Aisha Thompson | `security` | Security review |
| `@soc2-auditor` | Dr. Robert Chen | `security` | SOC2 compliance |
| `@cybersecurity-architect` | Dr. Sarah Martinez | `security` | Security architecture |
| `@opensource-standards` | Dr. Michael Foster | `security` | OSS, SBOM |
| `@blockchain-expert` | Dr. Wei Zhang | `blockchain` | Smart contracts |
| `@accessibility-expert` | Dr. Maya Patel | `accessibility` | WCAG, a11y |
| `@compliance-officer` | Dr. Catherine Rhodes | `compliance` | GDPR, regulatory |
| `@devops-engineer` | James O'Brien | `devops` | CI/CD, infra |
| `@code-reviewer` | Code Reviewer | `code-review` | PR review |
| `@docs-writer` | Docs Writer | `documentation` | Documentation |
| `@design-dev` | Design Dev | `design-system` | Components |
| `@react-dev` | React Expert | `react` | React patterns |
| `@mobile-dev` | Mobile Expert | `mobile` | Expo, RN |
| `@desktop-dev` | Desktop Expert | `tauri` | Tauri, Rust |
| `@task-manager` | Task Manager | `tasks` | Xala PM sync |

## Process

### Step 1: Understand the Feature

Ask the user:
1. **What** does this feature do? (one sentence)
2. **Why** is it needed? (problem/value)
3. **Who** is it for? (user type)

### Step 2: Define Acceptance Criteria

Write 3-5 specific, testable criteria. Assign `@testing-specialist` to verify each:

```gherkin
# AC-1: User Login (verify: @testing-specialist)
GIVEN a registered user is on the login page
WHEN they enter valid credentials
THEN they are redirected to the dashboard
```

### Step 3: Plan Implementation with Agent Assignments

**CRITICAL:** Every task MUST specify:
- **Agent handle** (e.g., `@backend-dev`)
- **Plugin** (e.g., `backend`)
- **Skill** if applicable (e.g., `api-design`)

| # | Task | Agent | Plugin | Skill | Est |
|---|------|-------|--------|-------|-----|
| 1 | Create database schema | `@supabase-dev` | `supabase` | `migrations` | 2h |
| 2 | Build REST API | `@backend-dev` | `backend` | `api-design` | 3h |
| 3 | Create UI components | `@frontend-dev` | `frontend` | `react-components` | 4h |
| 4 | Security review | `@owasp-expert` | `security` | `owasp/injection-prevention` | 1h |
| 5 | Write E2E tests | `@testing-specialist` | `testing` | `e2e` | 2h |
| 6 | Accessibility audit | `@accessibility-expert` | `accessibility` | `wcag-audit` | 1h |

### Step 4: Generate CLI Commands

For each task, provide the exact `/delegate` command:

```bash
# Task 1: Database (routes to @supabase-dev)
/delegate @supabase-dev "Create migration for [feature]" --spec SPEC-2024-001

# Task 2: API (routes to @backend-dev)  
/delegate @backend-dev "Implement [endpoint] API" --spec SPEC-2024-001

# Task 3: UI (routes to @frontend-dev)
/delegate @frontend-dev "Build [component]" --spec SPEC-2024-001
```

### Step 5: Xala PM Integration

Create tasks in Xala PM:

```bash
/task create "[Task 1]" --spec SPEC-2024-001 --agent @supabase-dev
/task create "[Task 2]" --spec SPEC-2024-001 --agent @backend-dev
/task create "[Task 3]" --spec SPEC-2024-001 --agent @frontend-dev
```

## Output Format

Use the template from `xalapm-core/templates/SPEC_TEMPLATE.md`:

```markdown
# Feature: {Feature Name}

> **Spec ID:** SPEC-{YYYY}-{NNN}
> **Status:** Ready
> **Created:** {date}
> **Xala PM Task:** [To be created]

---

## 1. Summary

**What:** {One sentence}
**Why:** {Problem/value}
**Who:** {User type}

---

## 2. Acceptance Criteria

| ID | Criteria | Test Type | Assigned Agent | Status |
|----|----------|-----------|----------------|--------|
| AC-1 | {Criteria} | E2E | `@testing-specialist` | ⬜ |
| AC-2 | {Criteria} | Integration | `@testing-specialist` | ⬜ |

---

## 3. Implementation Plan

| # | Task | Agent | Plugin | Skill | Estimate | Status |
|---|------|-------|--------|-------|----------|--------|
| 1 | {Task} | `@agent` | `plugin` | `skill` | {Hours} | ⬜ |

---

## 4. CLI Routing Instructions

```bash
/delegate @agent "Task description" --spec SPEC-{YYYY}-{NNN}
```

---

## 5. Best Practices

| Practice | Agent | Verification |
|----------|-------|--------------|
| {Practice} | `@agent` | {How} |

---

## 6. Tests

| AC | Test | Agent | Command | Status |
|----|------|-------|---------|--------|
| AC-1 | {Test} | `@testing-specialist` | `npm test` | ⬜ |

---

## 7. Xala PM Integration

| Task | PM ID | Agent | Status |
|------|-------|-------|--------|
| {Task} | PM-{XXX} | `@agent` | ⬜ |

---

## 8. Definition of Done

| Requirement | Agent | Status | Proof |
|-------------|-------|--------|-------|
| Tests pass | `@testing-specialist` | ⬜ | Results |
| Security review | `@owasp-expert` | ⬜ | Report |
| Code review | `@code-reviewer` | ⬜ | PR |
```

## Example

```
/spec user-authentication

📋 Creating specification...

# Feature: User Authentication

> **Spec ID:** SPEC-2024-001
> **Status:** Ready
> **Created:** 2024-01-15

## 1. Summary

**What:** Users can log in with email/password and manage sessions
**Why:** Enable secure access to protected features
**Who:** All registered users

## 2. Acceptance Criteria

| ID | Criteria | Test | Agent | Status |
|----|----------|------|-------|--------|
| AC-1 | User logs in with valid credentials | E2E | `@testing-specialist` | ⬜ |
| AC-2 | Invalid credentials show error | Integration | `@testing-specialist` | ⬜ |
| AC-3 | Session persists across refresh | Integration | `@testing-specialist` | ⬜ |
| AC-4 | User can log out | E2E | `@testing-specialist` | ⬜ |

## 3. Implementation Plan

| # | Task | Agent | Plugin | Skill | Est | Status |
|---|------|-------|--------|-------|-----|--------|
| 1 | Auth API endpoints | `@backend-dev` | `backend` | `api-design` | 3h | ⬜ |
| 2 | Login/Logout UI | `@frontend-dev` | `frontend` | `react-components` | 2h | ⬜ |
| 3 | Session management | `@backend-dev` | `backend` | `auth` | 2h | ⬜ |
| 4 | Security review | `@owasp-expert` | `security` | `owasp/auth-security` | 1h | ⬜ |
| 5 | E2E tests | `@testing-specialist` | `testing` | `e2e` | 2h | ⬜ |

## 4. CLI Routing

```bash
# Execute tasks in order
/delegate @backend-dev "Create auth API with login, logout, refresh endpoints" --spec SPEC-2024-001
/delegate @frontend-dev "Build login form with validation and error handling" --spec SPEC-2024-001
/delegate @owasp-expert "Security review for OWASP A07 compliance" --spec SPEC-2024-001
/delegate @testing-specialist "Write E2E tests for AC-1 through AC-4" --spec SPEC-2024-001
```

## 5. Xala PM Tasks

```bash
/task create "Auth API endpoints" --spec SPEC-2024-001 --agent @backend-dev --estimate 3h
/task create "Login/Logout UI" --spec SPEC-2024-001 --agent @frontend-dev --estimate 2h
/task create "Security review" --spec SPEC-2024-001 --agent @owasp-expert --estimate 1h
/task create "E2E tests" --spec SPEC-2024-001 --agent @testing-specialist --estimate 2h
```

All tasks synced to Xala PM.
```

## Remember

- **Every task needs an agent** - No orphan tasks
- **Use exact agent handles** - `@backend-dev` not "backend team"
- **Include skills when specific** - `owasp/injection-prevention`
- **Generate CLI commands** - Ready to copy/paste
- **Sync with Xala PM** - All tasks tracked
