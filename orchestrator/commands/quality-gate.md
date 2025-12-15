---
description: Verify feature meets all quality standards before release
args:
  spec: Spec ID to verify (required)
  full: Run full audit including manual checks (default: false)
---

# Quality Gate Command

Verify a feature meets ALL quality standards with zero compromise. This is the final gate before release.

## Quality Pillars

| Pillar | Agent | Verification |
|--------|-------|--------------|
| Code Quality | `@code-reviewer` | Lint, types, coverage |
| Performance | `@frontend-dev`, `@backend-dev` | Lighthouse, load tests |
| Security | `@owasp-expert` | OWASP scan, dependency audit |
| Compliance | `@soc2-auditor`, `@compliance-officer` | Audit checks |
| UX | `@frontend-dev` | Interaction review |
| UI | `@design-dev` | Design system compliance |
| Accessibility | `@accessibility-expert` | WCAG AA audit |
| Documentation | `@docs-writer` | JSDoc coverage |
| Tests | `@testing-specialist` | TDD verification |
| Maintainability | `@code-reviewer` | Architecture review |

## Process

### Step 1: Automated Checks

```bash
# Code Quality
npm run lint                    # Zero errors
npm run typecheck               # Zero errors
npm run test -- --coverage      # ≥80% coverage

# Security
npm audit --audit-level=high    # Zero high/critical
/security-scan --scope all      # OWASP compliant

# Performance
npm run test:perf               # Meets thresholds
lighthouse --performance ≥90

# Accessibility
npm run test:a11y               # WCAG AA pass
axe-core scan                   # Zero violations
```

### Step 2: Agent Reviews

Each agent verifies their domain:

```bash
/delegate @owasp-expert "Security review for SPEC-{id}"
/delegate @accessibility-expert "Accessibility audit for SPEC-{id}"
/delegate @code-reviewer "Code quality review for SPEC-{id}"
/delegate @testing-specialist "Test coverage verification for SPEC-{id}"
/delegate @docs-writer "Documentation coverage for SPEC-{id}"
```

### Step 3: Quality Report

Generate comprehensive report with pass/fail for each pillar.

## Output Format

```markdown
## 🎯 Quality Gate Report

**Spec:** SPEC-2024-001 - User Authentication
**Date:** 2024-01-15
**Result:** ✅ PASSED / ❌ FAILED

---

### 📊 Summary

| Pillar | Status | Score | Agent |
|--------|--------|-------|-------|
| Code Quality | ✅ | 95% | @code-reviewer |
| Performance | ✅ | 92 | @frontend-dev |
| Security | ✅ | A | @owasp-expert |
| Compliance | ✅ | 100% | @soc2-auditor |
| UX | ✅ | Pass | @frontend-dev |
| UI | ✅ | Pass | @design-dev |
| Accessibility | ✅ | AA | @accessibility-expert |
| Documentation | ✅ | 88% | @docs-writer |
| Tests | ✅ | 85% | @testing-specialist |
| Maintainability | ✅ | A | @code-reviewer |

**Overall:** 10/10 pillars passed ✅

---

### 1️⃣ Code Quality

**Agent:** @code-reviewer
**Status:** ✅ PASSED

| Check | Result |
|-------|--------|
| ESLint | 0 errors, 0 warnings |
| TypeScript | 0 errors |
| Test Coverage | 85% (threshold: 80%) |
| Complexity | Max 8 (threshold: 10) |
| Duplication | 2.1% (threshold: 3%) |

---

### 2️⃣ Performance

**Agent:** @frontend-dev, @backend-dev
**Status:** ✅ PASSED

#### Frontend (Lighthouse)
| Metric | Score | Target |
|--------|-------|--------|
| Performance | 92 | ≥90 |
| LCP | 1.8s | ≤2.5s |
| FID | 45ms | ≤100ms |
| CLS | 0.05 | ≤0.1 |

#### Backend
| Metric | Result | Target |
|--------|--------|--------|
| API Response (p95) | 145ms | ≤200ms |
| Throughput | 1,250 req/s | ≥1,000 |
| Error Rate | 0.02% | ≤0.1% |

---

### 3️⃣ Security

**Agent:** @owasp-expert
**Status:** ✅ PASSED

| OWASP | Check | Result |
|-------|-------|--------|
| A01 | Access Control | ✅ Pass |
| A02 | Cryptography | ✅ Pass |
| A03 | Injection | ✅ Pass |
| A04 | Insecure Design | ✅ Pass |
| A05 | Security Config | ✅ Pass |
| A06 | Components | ✅ Pass |
| A07 | Authentication | ✅ Pass |
| A08 | Integrity | ✅ Pass |
| A09 | Logging | ✅ Pass |
| A10 | SSRF | ✅ Pass |

**Dependency Audit:** 0 high/critical vulnerabilities

---

### 4️⃣ Compliance

**Agent:** @soc2-auditor
**Status:** ✅ PASSED

| Control | Status |
|---------|--------|
| CC6.1 Access Control | ✅ |
| CC6.6 Encryption | ✅ |
| CC7.2 Monitoring | ✅ |
| CC8.1 Change Management | ✅ |

---

### 5️⃣ Accessibility

**Agent:** @accessibility-expert
**Status:** ✅ PASSED (WCAG 2.1 AA)

| Category | Violations |
|----------|------------|
| Perceivable | 0 |
| Operable | 0 |
| Understandable | 0 |
| Robust | 0 |

**Manual Checks:**
- [x] Keyboard navigation tested
- [x] Screen reader tested (VoiceOver)
- [x] Color contrast verified

---

### 6️⃣ Documentation

**Agent:** @docs-writer
**Status:** ✅ PASSED

| Type | Coverage | Target |
|------|----------|--------|
| Public Functions | 92% | ≥80% |
| Public Types | 88% | ≥80% |
| Components | 100% | 100% |
| API Endpoints | 100% | 100% |

---

### 7️⃣ Tests

**Agent:** @testing-specialist
**Status:** ✅ PASSED

| Type | Count | Passing |
|------|-------|---------|
| Unit | 45 | 45 |
| Integration | 12 | 12 |
| E2E | 8 | 8 |

**Coverage:** 85% (statements), 82% (branches)

---

### Sign-off Required

| Role | Agent | Status |
|------|-------|--------|
| Tech Lead | @orchestrator | ⬜ Pending |
| Security | @owasp-expert | ⬜ Pending |
| QA | @testing-specialist | ⬜ Pending |
| Accessibility | @accessibility-expert | ⬜ Pending |
```

## Failure Handling

If any pillar fails:

1. **Block release** until resolved
2. **Generate remediation tasks** assigned to appropriate agents
3. **Re-run quality gate** after fixes

```markdown
### ❌ FAILED: Accessibility

**Issues Found:**
1. Missing alt text on 3 images
2. Color contrast ratio 3.8:1 (required: 4.5:1)
3. Missing form labels on 2 inputs

**Remediation Tasks Created:**
- PM-12345: Fix alt text (@frontend-dev)
- PM-12346: Fix color contrast (@design-dev)
- PM-12347: Add form labels (@frontend-dev)

**Action Required:** Fix issues and re-run `/quality-gate SPEC-2024-001`
```

## Integration with CI/CD

```yaml
# .github/workflows/quality-gate.yml
name: Quality Gate

on:
  pull_request:
    types: [opened, synchronize]
    branches: [main]

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Code Quality
        run: |
          npm run lint
          npm run typecheck
          npm run test -- --coverage

      - name: Security Scan
        run: |
          npm audit --audit-level=high
          npx snyk test

      - name: Accessibility
        run: npm run test:a11y

      - name: Performance
        run: npm run test:perf

      - name: Documentation
        run: npm run docs:coverage
```

## Remember

- **Zero compromise** on any pillar
- **All agents must approve** in their domain
- **Automated + manual** checks required
- **Block release** until all gates pass
- **Document exceptions** (if any, must be approved by Tech Lead)

