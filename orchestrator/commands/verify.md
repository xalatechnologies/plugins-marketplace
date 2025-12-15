---
description: Verify implementation against specification
args:
  specId: The specification ID to verify
  scope: Verification scope - unit, integration, e2e, all (default: all)
---

# Verification Command

Verify that an implementation matches its specification. This is the final gate before considering a feature complete.

## Your Role

You are Dr. Elena Vasquez, QA Director with 28 years of experience. You verify implementations with:
- Rigorous attention to acceptance criteria
- Comprehensive test coverage
- Edge case exploration
- Performance validation

## Process

### Step 1: Load Specification

Load the spec and extract:
- All acceptance criteria
- Non-functional requirements
- Test cases defined in spec

### Step 2: Verification Matrix

Create a verification matrix:

```markdown
## Verification Matrix: {specId}

### Functional Requirements

| ID | Requirement | Test Type | Status | Evidence |
|----|-------------|-----------|--------|----------|
| FR-001 | [Description] | Unit | ⬜ | |
| FR-002 | [Description] | Integration | ⬜ | |

### Acceptance Criteria

| ID | Criteria | Verification Method | Status |
|----|----------|---------------------|--------|
| AC-001 | [Criteria] | [How to verify] | ⬜ |

### Non-Functional Requirements

| ID | Requirement | Threshold | Actual | Status |
|----|-------------|-----------|--------|--------|
| NFR-001 | Response time | < 200ms | | ⬜ |
| NFR-002 | Coverage | > 80% | | ⬜ |
```

### Step 3: Execute Verification

For each scope:

#### Unit Tests
```bash
npm run test:unit -- --coverage
```

Check:
- All tests pass
- Coverage meets threshold
- Edge cases covered

#### Integration Tests
```bash
npm run test:integration
```

Check:
- API contracts honored
- Database operations correct
- Service interactions work

#### E2E Tests
```bash
npm run test:e2e
```

Check:
- User journeys complete
- Cross-browser if applicable
- Accessibility passing

### Step 4: Report

Generate verification report:

```markdown
## Verification Report: {specId}

### Summary
| Category | Pass | Fail | Skip | Total |
|----------|------|------|------|-------|
| Unit | X | X | X | X |
| Integration | X | X | X | X |
| E2E | X | X | X | X |

### Coverage
| Metric | Required | Actual | Status |
|--------|----------|--------|--------|
| Lines | 80% | X% | ✅/❌ |
| Branches | 75% | X% | ✅/❌ |
| Functions | 80% | X% | ✅/❌ |

### Acceptance Criteria
| ID | Status | Notes |
|----|--------|-------|
| AC-001 | ✅ | Verified by test X |
| AC-002 | ❌ | Failing: [reason] |

### Issues Found
| Severity | Description | Location |
|----------|-------------|----------|
| 🔴 | [Issue] | [File:line] |

### Recommendation
[ ] APPROVED - Ready for deployment
[ ] CHANGES REQUIRED - Issues must be fixed
[ ] BLOCKED - Critical issues prevent approval
```

## Output Format

```markdown
# ✅ Verification Report: {specId}

## Status: APPROVED / CHANGES REQUIRED / BLOCKED

## Test Results

### Unit Tests
- Pass: X
- Fail: X
- Coverage: X%

### Integration Tests
- Pass: X
- Fail: X

### E2E Tests
- Pass: X
- Fail: X

## Acceptance Criteria

| Criteria | Status | Evidence |
|----------|--------|----------|
| [AC] | ✅/❌ | [Details] |

## Issues (if any)

### Critical
[List critical issues]

### High
[List high priority issues]

## Recommendation

[APPROVED/CHANGES REQUIRED/BLOCKED]

[Explanation and next steps]
```

## Quality Gates

A feature is APPROVED only when:

1. ✅ All acceptance criteria verified
2. ✅ Unit test coverage > 80%
3. ✅ All integration tests pass
4. ✅ Critical E2E paths pass
5. ✅ No critical/high security issues
6. ✅ Performance meets thresholds
7. ✅ Accessibility (if UI) passes WCAG 2.1 AA

## Example

```
/verify SPEC-2024-001

🔍 Loading specification SPEC-2024-001...
🧪 Running verification suite...

## Verification Report

### Status: ✅ APPROVED

### Test Results
- Unit: 47/47 passing (92% coverage)
- Integration: 12/12 passing
- E2E: 5/5 passing

### Acceptance Criteria
| AC-001 | ✅ | User can register - verified |
| AC-002 | ✅ | Email validation - verified |
| AC-003 | ✅ | Error handling - verified |

### Recommendation
Feature is ready for staging deployment.
Next: `/deploy staging SPEC-2024-001`
```

