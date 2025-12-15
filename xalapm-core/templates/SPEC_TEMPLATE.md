# Feature: [Feature Name]

> **Spec ID:** SPEC-{YYYY}-{NNN}
> **Status:** Draft | Ready | In Progress | Done
> **Created:** {date}
> **Xala PM Task:** [Link to Xala PM task or "To be created"]

---

## 1. Summary

**What:** [One sentence describing the feature]

**Why:** [The problem it solves or value it provides]

**Who:** [Target user/persona]

---

## 2. Acceptance Criteria

| ID | Criteria | Test Type | Assigned Agent | Status |
|----|----------|-----------|----------------|--------|
| AC-1 | [User can...] | [E2E] | `@testing-specialist` | ⬜ |
| AC-2 | [System should...] | [Integration] | `@testing-specialist` | ⬜ |
| AC-3 | [When X, then Y...] | [Unit] | `@testing-specialist` | ⬜ |

### Acceptance Criteria Details

#### AC-1: [Title]
```gherkin
GIVEN [precondition]
WHEN [action]
THEN [expected result]
```

#### AC-2: [Title]
```gherkin
GIVEN [precondition]
WHEN [action]
THEN [expected result]
```

---

## 3. Implementation Plan

### Task Assignment

> **IMPORTANT:** Each task MUST specify the responsible agent/skill. The CLI will route to the exact agent.

| # | Task | Agent | Plugin | Skill | Estimate | Status |
|---|------|-------|--------|-------|----------|--------|
| 1 | Design database schema | `@supabase-dev` | `supabase` | `migrations` | 2h | ⬜ |
| 2 | Create API endpoints | `@backend-dev` | `backend` | `api-design` | 3h | ⬜ |
| 3 | Build UI components | `@frontend-dev` | `frontend` | `react-components` | 4h | ⬜ |
| 4 | Security review | `@owasp-expert` | `security` | `owasp/injection-prevention` | 1h | ⬜ |
| 5 | Write E2E tests | `@testing-specialist` | `testing` | `e2e-testing` | 2h | ⬜ |
| 6 | Accessibility audit | `@accessibility-expert` | `accessibility` | `wcag-audit` | 1h | ⬜ |

### Agent Reference

| Agent Handle | Name | Plugin | Specialty |
|--------------|------|--------|-----------|
| `@orchestrator` | Dr. Alexander Chen | `orchestrator` | Coordination, architecture |
| `@frontend-dev` | Sarah Kim | `frontend` | React, UI, accessibility |
| `@backend-dev` | Dr. Marcus Rivera | `backend` | APIs, databases, security |
| `@supabase-dev` | Supabase Expert | `supabase` | Postgres, RLS, migrations |
| `@testing-specialist` | Dr. Elena Vasquez | `testing` | E2E, unit, integration |
| `@owasp-expert` | Dr. Aisha Thompson | `security` | OWASP Top 10, ASVS |
| `@soc2-auditor` | Dr. Robert Chen | `security` | SOC2 compliance |
| `@cybersecurity-architect` | Dr. Sarah Martinez | `security` | NIST, CIS, Zero Trust |
| `@blockchain-expert` | Dr. Wei Zhang | `blockchain` | Smart contracts, security |
| `@accessibility-expert` | Dr. Maya Patel | `accessibility` | WCAG, Universal Design |
| `@compliance-officer` | Dr. Catherine Rhodes | `compliance` | GDPR, regulatory |
| `@devops-engineer` | James O'Brien | `devops` | CI/CD, infrastructure |
| `@code-reviewer` | Code Review Agent | `code-review` | PR review, quality |
| `@docs-writer` | Documentation Agent | `documentation` | API docs, README |
| `@design-dev` | Design System Agent | `design-system` | Components, tokens |
| `@react-dev` | React Expert | `react` | Hooks, state, patterns |
| `@mobile-dev` | Mobile Expert | `mobile` | Expo, React Native |
| `@desktop-dev` | Desktop Expert | `tauri` | Tauri, Rust, IPC |
| `@task-manager` | Task Manager Agent | `tasks` | Task CRUD, tracking |

### Dependencies

- [ ] [Dependency 1]
- [ ] [Dependency 2]

---

## 4. CLI Routing Instructions

> These instructions tell the CLI/coding agent exactly how to execute each task.

### Task Execution Commands

```bash
# Task 1: Database Schema (routes to @supabase-dev)
/delegate @supabase-dev "Create migration for [feature] with schema: [details]"

# Task 2: API Endpoints (routes to @backend-dev)
/delegate @backend-dev "Implement [endpoint] API following spec AC-1, AC-2"

# Task 3: UI Components (routes to @frontend-dev)
/delegate @frontend-dev "Build [component] with accessibility per AC-3"

# Task 4: Security Review (routes to @owasp-expert)
/delegate @owasp-expert "Review code for OWASP Top 10 vulnerabilities"

# Task 5: E2E Tests (routes to @testing-specialist)
/delegate @testing-specialist "Write E2E tests for AC-1, AC-2, AC-3"

# Task 6: Accessibility (routes to @accessibility-expert)
/delegate @accessibility-expert "Audit UI for WCAG 2.1 AA compliance"
```

### Skill Invocation

```bash
# Use specific skill for focused action
/skill security/owasp/injection-prevention  # SQL injection check
/skill security/owasp/auth-security         # Auth review
/skill testing/e2e                          # E2E test generation
/skill accessibility/wcag-audit             # Accessibility check
```

---

## 5. Best Practices

### Required Standards (by Agent)

| Practice | Responsible Agent | Verification |
|----------|-------------------|--------------|
| TypeScript strict mode | `@frontend-dev`, `@backend-dev` | `tsc --noEmit` |
| No `any` types | `@code-reviewer` | ESLint rule |
| Input validation | `@owasp-expert` | Security scan |
| Error handling | `@backend-dev` | Code review |
| WCAG 2.1 AA | `@accessibility-expert` | Axe audit |
| Test coverage > 80% | `@testing-specialist` | Coverage report |

### Code Patterns

```typescript
// Example of expected code pattern
```

---

## 6. Tests

### Test Plan (by Agent)

| AC | Test | Agent | Command | Status |
|----|------|-------|---------|--------|
| AC-1 | [Test description] | `@testing-specialist` | `npm test -- --grep "AC-1"` | ⬜ |
| AC-2 | [Test description] | `@testing-specialist` | `npm run test:e2e` | ⬜ |
| AC-3 | [Test description] | `@testing-specialist` | `npm run test:integration` | ⬜ |

### Security Tests

| Check | Agent | Skill | Command |
|-------|-------|-------|---------|
| OWASP Scan | `@owasp-expert` | `owasp/injection-prevention` | `/security-scan --scope owasp` |
| Dependency Audit | `@opensource-standards` | `sbom` | `npm audit` |

### Test Code

```typescript
describe('Feature: [Name]', () => {
  describe('AC-1: [Criteria]', () => {
    it('should [expected behavior]', async () => {
      // Arrange
      // Act
      // Assert
    });
  });
});
```

---

## 7. Xala PM Integration

> **All actions sync with Xala PM for tracking and visibility.**

### Task Sync

| Spec Task | Xala PM Task ID | Status Sync |
|-----------|-----------------|-------------|
| Task 1: Database schema | PM-{XXX} | Auto-sync via `@task-manager` |
| Task 2: API endpoints | PM-{XXX} | Auto-sync via `@task-manager` |
| Task 3: UI components | PM-{XXX} | Auto-sync via `@task-manager` |

### Commands for Xala PM

```bash
# Create task in Xala PM
/task create "[Task name]" --spec SPEC-{YYYY}-{NNN} --assign @backend-dev

# Update task status
/task update PM-{XXX} --status in_progress

# Log work
/task log PM-{XXX} --hours 2 --note "Completed API endpoint"

# Complete task
/task complete PM-{XXX} --proof "Test results attached"
```

### Activity Logging

All agent actions are logged to Xala PM:
- Task started/completed timestamps
- Agent assignments
- Test results
- Code review approvals

---

## 8. Definition of Done

### Checklist

| # | Requirement | Agent | Status | Proof |
|---|-------------|-------|--------|-------|
| 1 | All acceptance criteria pass | `@testing-specialist` | ⬜ | Test results |
| 2 | Code reviewed and approved | `@code-reviewer` | ⬜ | PR link |
| 3 | Security scan passed | `@owasp-expert` | ⬜ | Scan report |
| 4 | Accessibility audit passed | `@accessibility-expert` | ⬜ | Axe report |
| 5 | Documentation updated | `@docs-writer` | ⬜ | Doc link |
| 6 | Deployed to staging | `@devops-engineer` | ⬜ | URL |
| 7 | Xala PM tasks completed | `@task-manager` | ⬜ | PM links |

### Proof of Completion

#### AC-1: [Criteria Title]
- **Test Agent:** `@testing-specialist`
- **Command:** `npm test -- --grep "AC-1"`
- **Result:** ✅ PASS / ❌ FAIL
- **Evidence:**
  
  ```
  [Test output or screenshot path]
  ```

#### AC-2: [Criteria Title]
- **Test Agent:** `@testing-specialist`
- **Command:** `npm run test:e2e`
- **Result:** ✅ PASS / ❌ FAIL
- **Evidence:**

  ```
  [Test output or screenshot path]
  ```

---

## 9. Sign-off

| Role | Agent | Name | Date | Approved |
|------|-------|------|------|----------|
| Architecture | `@orchestrator` | Dr. Alexander Chen | | ⬜ |
| Development | `@backend-dev` / `@frontend-dev` | | | ⬜ |
| Security | `@owasp-expert` | Dr. Aisha Thompson | | ⬜ |
| QA | `@testing-specialist` | Dr. Elena Vasquez | | ⬜ |
| Accessibility | `@accessibility-expert` | Dr. Maya Patel | | ⬜ |
