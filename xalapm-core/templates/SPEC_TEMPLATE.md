# Feature: [Feature Name]

> **Spec ID:** SPEC-{YYYY}-{NNN}
> **Status:** Draft | Ready | In Progress | Done
> **Created:** {date}

---

## 1. Summary

**What:** [One sentence describing the feature]

**Why:** [The problem it solves or value it provides]

**Who:** [Target user/persona]

---

## 2. Acceptance Criteria

| ID | Criteria | Test Type | Status |
|----|----------|-----------|--------|
| AC-1 | [User can...] | [Unit/Integration/E2E] | ⬜ |
| AC-2 | [System should...] | [Unit/Integration/E2E] | ⬜ |
| AC-3 | [When X, then Y...] | [Unit/Integration/E2E] | ⬜ |

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

### Tasks

| # | Task | Owner | Estimate | Status |
|---|------|-------|----------|--------|
| 1 | [Task description] | [Agent] | [Hours] | ⬜ |
| 2 | [Task description] | [Agent] | [Hours] | ⬜ |
| 3 | [Task description] | [Agent] | [Hours] | ⬜ |

### Dependencies

- [ ] [Dependency 1]
- [ ] [Dependency 2]

---

## 4. Best Practices

### Must Follow

- [ ] TypeScript strict mode enabled
- [ ] No `any` types
- [ ] Error handling with Result types
- [ ] Input validation on all endpoints
- [ ] Accessibility (WCAG 2.1 AA) if UI

### Code Patterns

```typescript
// Example of expected code pattern
```

---

## 5. Tests

### Test Plan

| AC | Test | File | Status |
|----|------|------|--------|
| AC-1 | [Test description] | `__tests__/feature.test.ts` | ⬜ |
| AC-2 | [Test description] | `__tests__/feature.test.ts` | ⬜ |
| AC-3 | [Test description] | `__tests__/feature.e2e.ts` | ⬜ |

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

## 6. Definition of Done

### Checklist

| # | Requirement | Status | Proof |
|---|-------------|--------|-------|
| 1 | All acceptance criteria pass | ⬜ | Test results |
| 2 | Code reviewed and approved | ⬜ | PR link |
| 3 | Tests written and passing | ⬜ | CI badge |
| 4 | No linting errors | ⬜ | Lint output |
| 5 | Documentation updated | ⬜ | Doc link |

### Proof of Completion

#### AC-1: [Criteria Title]
- **Test:** `npm test -- --grep "AC-1"`
- **Result:** ✅ PASS / ❌ FAIL
- **Screenshot/Evidence:**
  
  ```
  [Test output or screenshot path]
  ```

#### AC-2: [Criteria Title]
- **Test:** `npm test -- --grep "AC-2"`
- **Result:** ✅ PASS / ❌ FAIL
- **Screenshot/Evidence:**

  ```
  [Test output or screenshot path]
  ```

---

## 7. Sign-off

| Role | Name | Date | Approved |
|------|------|------|----------|
| Developer | | | ⬜ |
| Reviewer | | | ⬜ |
| QA | | | ⬜ |
