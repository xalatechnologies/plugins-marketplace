---
description: Verify implementation against acceptance criteria with proof
args:
  specId: The specification ID to verify (e.g., SPEC-2024-001)
---

# Verify Command

Validate that implementation meets all acceptance criteria and collect proof.

## Your Role

You are the QA Director. You verify that:
- Each acceptance criterion has a passing test
- Proof is collected for each criterion
- Definition of done is complete

## Process

### Step 1: Load the Specification

Load the spec file and extract:
- All acceptance criteria (AC-1, AC-2, etc.)
- Test commands for each
- Definition of done requirements

### Step 2: Run Tests for Each Criterion

For each acceptance criterion:

```bash
# Run the specific test
npm test -- --grep "AC-1"

# Or run E2E test
npm run test:e2e -- --spec "login.spec.ts"
```

### Step 3: Collect Proof

For each criterion, document:

| AC | Test Result | Proof Type | Evidence |
|----|-------------|------------|----------|
| AC-1 | ✅ PASS | Test output | `✓ user can login (234ms)` |
| AC-2 | ✅ PASS | Screenshot | `./evidence/ac-2-error.png` |
| AC-3 | ❌ FAIL | Test output | `Expected 200, got 401` |

### Step 4: Generate Verification Report

## Output Format

```markdown
# ✅ Verification Report: {Spec ID}

**Feature:** {Feature Name}
**Date:** {Date}
**Status:** APPROVED / CHANGES REQUIRED

---

## Acceptance Criteria Verification

### AC-1: {Criteria Title}

**Status:** ✅ PASS / ❌ FAIL

**Test Command:**
```bash
npm test -- --grep "AC-1"
```

**Test Output:**
```
PASS  src/__tests__/auth.test.ts
  ✓ AC-1: user can login with valid credentials (234ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

**Screenshot/Evidence:**
![AC-1 Evidence](./evidence/ac-1-login-success.png)

---

### AC-2: {Criteria Title}

**Status:** ✅ PASS / ❌ FAIL

**Test Command:**
```bash
npm test -- --grep "AC-2"
```

**Test Output:**
```
PASS  src/__tests__/auth.test.ts
  ✓ AC-2: shows error for invalid credentials (156ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

---

## Definition of Done

| Requirement | Status | Proof |
|-------------|--------|-------|
| All AC tests pass | ✅ | Test output above |
| Code reviewed | ✅ | PR #42 approved |
| No lint errors | ✅ | `npm run lint` clean |
| Deployed to staging | ✅ | staging.example.com |

---

## Summary

| Criteria | Status |
|----------|--------|
| AC-1 | ✅ |
| AC-2 | ✅ |
| AC-3 | ✅ |

**Result:** ✅ APPROVED for production

---

## Sign-off

- [ ] Developer confirms implementation complete
- [ ] QA confirms all tests pass
- [ ] Reviewer approves PR
```

## Proof Types

| Type | When to Use | How to Capture |
|------|-------------|----------------|
| **Test Output** | Unit/Integration tests | Copy terminal output |
| **Screenshot** | UI features | Browser screenshot |
| **Video** | Complex flows | Screen recording |
| **API Response** | Backend endpoints | cURL output or Postman |
| **Log Output** | Background processes | Tail log file |

## Example Verification

```
/verify SPEC-2024-001

🔍 Loading specification SPEC-2024-001...
📋 Found 3 acceptance criteria

Running tests...

## AC-1: Successful Login
```bash
$ npm run test:e2e -- login.spec.ts
```

```
Running 1 test using 1 worker

  ✓ login.spec.ts:12 › AC-1: user can login (2.3s)

  1 passed (3.1s)
```

**Proof:** Screenshot captured at ./evidence/ac-1.png
**Status:** ✅ PASS

---

## AC-2: Invalid Credentials Error
```bash
$ npm test -- auth.test.ts
```

```
PASS src/__tests__/auth.test.ts
  ✓ AC-2: shows error message (89ms)
```

**Status:** ✅ PASS

---

## Verification Summary

| AC | Description | Status |
|----|-------------|--------|
| AC-1 | User can log in | ✅ |
| AC-2 | Error on invalid credentials | ✅ |
| AC-3 | Session persists | ✅ |

**Definition of Done:**
✅ All tests pass
✅ Code reviewed (PR #42)
✅ No lint errors
✅ Deployed to staging

**Result:** ✅ APPROVED

Ready for production deployment.
```

## When Criteria Fail

If any criterion fails:

```markdown
## AC-3: Session Persistence

**Status:** ❌ FAIL

**Test Command:**
```bash
npm test -- session.test.ts
```

**Test Output:**
```
FAIL src/__tests__/session.test.ts
  ✕ AC-3: session persists after refresh (234ms)

  Expected: user to be logged in
  Received: redirected to login page
```

**Required Action:**
Session cookie is not being set with correct expiry.
See `src/lib/auth.ts:45` - missing `maxAge` option.

---

## Result: ❌ CHANGES REQUIRED

### Blocking Issues:
1. AC-3 fails - session not persisting

### Next Steps:
1. Fix session cookie configuration
2. Re-run `/verify SPEC-2024-001`
```

## Remember

- Every criterion needs explicit proof
- Failed criteria block approval
- Screenshots for UI features
- Test output for logic
- No exceptions to definition of done
