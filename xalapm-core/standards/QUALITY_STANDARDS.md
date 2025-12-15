# Quality Standards - Zero Compromise

> **Philosophy:** We build software like the best in the industry. Every feature, every line of code, every interaction must meet these standards. No exceptions.

---

## Quality Tiers: MVP to Production

> **Anti-Overwhelm Strategy:** Not everything needs to be perfect on day one. Use quality tiers to focus on what matters NOW and defer what can wait.

### Why Quality Tiers?

| Problem | Solution |
|---------|----------|
| Overwhelmed by standards | Start with MVP tier, upgrade later |
| Never shipping | Focus on "good enough to ship" first |
| Perfectionism paralysis | Clear definition of "done" for each tier |
| Scope creep | P0/P1 for MVP, P2/P3 for later |

### Tier 1: MVP (Minimum Viable Product)

**Goal:** Ship something that works, get feedback fast.

| Category | MVP Requirement | Full Requirement |
|----------|-----------------|------------------|
| **Code Quality** | ✅ Lint + TypeCheck pass | ✅ Full metrics |
| **Tests** | ✅ Happy path only (≥50%) | ✅ ≥80% coverage |
| **Security** | ✅ Basic (A01-A03) | ✅ Full OWASP |
| **Performance** | ✅ Functional | ✅ Optimized |
| **Accessibility** | ⚡ Basic labels | ✅ WCAG AA |
| **Documentation** | ⚡ README only | ✅ Full JSDoc |
| **Compliance** | ⚡ Defer | ✅ Full audit |

**Legend:** ✅ Required | ⚡ Minimal/Deferred

#### MVP Quality Gate

```bash
# MVP requires ONLY these checks to pass:
mvp_gates:
  - lint: "npm run lint"           # Zero errors
  - typecheck: "tsc --noEmit"      # Zero errors  
  - test: "npm test"               # Core paths pass
  - build: "npm run build"         # Successful
  - security_basic: "npm audit --audit-level=critical"  # No critical
```

#### MVP Definition of Done

- [ ] Core feature works end-to-end
- [ ] No critical bugs or security issues
- [ ] Can be deployed and tested by users
- [ ] Happy path tests pass
- [ ] Basic error handling in place

### Tier 2: Production-Ready

**Goal:** Enterprise-grade quality for long-term sustainability.

| Category | Requirement | Verification |
|----------|-------------|--------------|
| **Code Quality** | All metrics pass | SonarQube |
| **Tests** | ≥80% coverage | Jest/Vitest |
| **Security** | Full OWASP Top 10 | Security scan |
| **Performance** | All targets met | Lighthouse, load tests |
| **Accessibility** | WCAG 2.1 AA | Axe audit |
| **Documentation** | Full JSDoc + API docs | TypeDoc |
| **Compliance** | SOC2, GDPR as needed | Audits |

#### Production Quality Gate

```bash
# Production requires ALL checks (see full quality gates below)
production_gates:
  - all_mvp_gates
  - coverage: "≥80%"
  - security_full: "OWASP scan pass"
  - accessibility: "WCAG AA pass"
  - performance: "All targets met"
  - documentation: "≥80% coverage"
```

### Tier Progression Strategy

```
┌─────────────────────────────────────────────────────────────────┐
│                    QUALITY TIER PROGRESSION                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Week 1-2         Week 3-4         Week 5+          Ongoing     │
│  ┌─────────┐      ┌─────────┐      ┌─────────┐      ┌────────┐  │
│  │  MVP    │  ──► │ SHIP IT │  ──► │ HARDEN  │  ──► │ POLISH │  │
│  │ Tier 1  │      │ Get     │      │ Tier 2  │      │ Iterate│  │
│  └─────────┘      │ Feedback│      └─────────┘      └────────┘  │
│       │           └─────────┘           │                        │
│       ▼                                 ▼                        │
│   Focus on:                        Add:                          │
│   - Core features                  - Full test coverage          │
│   - Happy paths                    - Security hardening          │
│   - Basic quality                  - Accessibility audit         │
│                                    - Documentation               │
│                                    - Performance tuning          │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### When to Use Each Tier

| Scenario | Tier | Rationale |
|----------|------|-----------|
| New feature, testing hypothesis | MVP | Get feedback before investing |
| Internal tool | MVP | Lower risk, iterate faster |
| Customer-facing v1 | MVP → Production | Ship, then harden |
| Enterprise/regulated | Production | Compliance required |
| Security-critical | Production | No shortcuts on security |

---

## Task Priority Levels

> Use priority levels to focus on what matters for MVP.

| Priority | Name | For MVP? | Description |
|----------|------|----------|-------------|
| **P0** | Critical | ✅ Yes | Blocks shipping, core functionality |
| **P1** | Important | ✅ Yes | Significantly improves core UX |
| **P2** | Nice to Have | ❌ No | Polish, optimization, can defer |
| **P3** | Future | ❌ No | Ideas for later, backlog |

### Priority Decision Matrix

```
                    High Impact
                         │
            ┌────────────┼────────────┐
            │     P0     │     P1     │
    High    │  Critical  │  Important │
    Effort  │  (Do now)  │  (Do now)  │
            ├────────────┼────────────┤
            │     P1     │     P2     │
    Low     │  Important │  Nice to   │
    Effort  │  (Quick    │   Have     │
            │   wins)    │  (Defer)   │
            └────────────┼────────────┘
                         │
                    Low Impact
```

### How to Prioritize

1. **P0 - Critical Path**
   - User cannot complete core journey without it
   - Blocks other P0/P1 work
   - Security or data integrity issue
   - Example: Login, checkout, save data

2. **P1 - Important**
   - Significantly improves user experience
   - Enables key use cases
   - Low effort, high impact (quick wins)
   - Example: Error messages, loading states

3. **P2 - Nice to Have**
   - Polish and refinements
   - Performance optimization (unless critical)
   - Additional features beyond core
   - Example: Animations, advanced filters

4. **P3 - Future**
   - Ideas for future sprints
   - Nice to have someday
   - Not in current scope
   - Example: Integrations, advanced analytics

---

## PRIORITY #1: SOLID Principles & Clean Architecture

> **This is non-negotiable.** Every piece of code must follow SOLID principles, be reusable, properly structured, and small/manageable.

### SOLID Principles (Mandatory)

| Principle | Rule | Enforcement |
|-----------|------|-------------|
| **S**ingle Responsibility | One reason to change per module | Max 200 lines/file, max 30 lines/function |
| **O**pen/Closed | Open for extension, closed for modification | Use interfaces, composition |
| **L**iskov Substitution | Subtypes must be substitutable | Type safety, proper inheritance |
| **I**nterface Segregation | Small, focused interfaces | Max 5 methods per interface |
| **D**ependency Inversion | Depend on abstractions, not concretions | Dependency injection, IoC |

### Code Size Limits (Strictly Enforced)

| Element | Maximum | Why |
|---------|---------|-----|
| **Function/Method** | 30 lines | Single responsibility, testable |
| **Class/Component** | 200 lines | Focused, manageable |
| **File** | 300 lines | Easy to navigate |
| **Parameters** | 4 max | Use options object for more |
| **Nesting Depth** | 3 levels | Extract to functions |
| **Cyclomatic Complexity** | 10 max | Simple, testable logic |

### Reusability Requirements

- **Extract common logic** into shared utilities
- **Create reusable components** instead of copy-paste
- **Use composition** over inheritance
- **Build for extensibility** from the start
- **DRY (Don't Repeat Yourself)** - max 2 occurrences before extraction

---

## CRITICAL: Professional Communication Standards

> **No AI-generated tone. No emojis in code. Human-written, professional documentation.**

### Strictly Prohibited

| ❌ NEVER Use | Why |
|-------------|-----|
| Emojis in code, comments, or commits | Unprofessional, clutters code |
| "Built with ❤️" or "Made with love" | AI slop, unprofessional |
| "Happy coding!" or similar | AI tone, not professional |
| Overly enthusiastic language | Sounds artificial |
| "Let's dive in!" or "Let's get started!" | AI-generated filler |
| Excessive exclamation marks | Unprofessional |
| "Awesome", "Amazing", "Fantastic" | AI superlatives |
| "I hope this helps!" | AI tone |

### Professional Standards

| ✅ DO | Example |
|------|---------|
| **Concise, factual comments** | `// Validates user input before processing` |
| **Descriptive commit messages** | `fix: resolve null pointer in auth service` |
| **Technical documentation** | `This function returns a Result type containing...` |
| **Neutral, professional tone** | `The module handles user authentication.` |
| **Conventional Commits format** | `feat:`, `fix:`, `docs:`, `refactor:` |

### Commit Message Format

```bash
# ✅ CORRECT - Professional, descriptive
feat(auth): add JWT refresh token rotation
fix(api): handle race condition in concurrent requests
docs(readme): update installation instructions
refactor(utils): extract validation logic to shared module

# ❌ WRONG - AI tone, emojis, unprofessional
✨ Add awesome new feature!
🐛 Fix bug (hope this works!)
📝 Update docs - made with love ❤️
🚀 Ship it!
```

### Code Comments

```typescript
// ✅ CORRECT - Professional, factual
/**
 * Validates email format and checks domain against blocklist.
 * @param email - User email address
 * @returns Validation result with error details if invalid
 */
function validateEmail(email: string): ValidationResult {
  // Check format before expensive domain lookup
  if (!isValidFormat(email)) {
    return { valid: false, error: 'Invalid email format' };
  }
  // ...
}

// ❌ WRONG - AI tone, emojis, unprofessional
/**
 * 🎉 This awesome function validates emails!
 * Let's make sure those emails are valid! 💪
 * Happy validating! 🚀
 */
function validateEmail(email: string) {
  // Let's check the format first! ✨
  // ...
}
```

### Documentation Style

```markdown
# ✅ CORRECT - Technical, professional

## Authentication Module

This module handles user authentication using JWT tokens with refresh 
token rotation. Sessions expire after 24 hours of inactivity.

### Configuration

Set the following environment variables:
- `JWT_SECRET` - Secret key for token signing (min 32 chars)
- `TOKEN_EXPIRY` - Token lifetime in seconds (default: 86400)

# ❌ WRONG - AI tone, unprofessional

## 🔐 Authentication Module 

Welcome! 👋 This awesome module handles authentication! 🎉

We've built this with love ❤️ to make your life easier! 
Let's dive in and explore the amazing features! 🚀

Happy authenticating! 💪
```

### README Files

```markdown
# ✅ CORRECT
## Installation

Install dependencies:
\`\`\`bash
npm install
\`\`\`

## Usage

Import and initialize the client:
\`\`\`typescript
import { Client } from '@org/package';
const client = new Client({ apiKey: process.env.API_KEY });
\`\`\`

# ❌ WRONG
## 🚀 Installation

Let's get you set up! It's super easy! 🎉
\`\`\`bash
npm install  # This is where the magic happens! ✨
\`\`\`

## 💡 Usage

Now for the fun part! 🎊
```

---

## 🎯 Core Principles

### The 11 Pillars of Excellence

| # | Pillar | Standard | Verification |
|---|--------|----------|--------------|
| **1** | **🏗️ SOLID & Clean Code** | Small, reusable, properly structured | Code review, metrics |
| 2 | **Quality** | Zero defects in production | Automated testing, code review |
| 3 | **Performance** | Sub-second response times | Load testing, profiling |
| 4 | **Security** | OWASP Top 10 compliant | Security scans, pen testing |
| 5 | **Compliance** | SOC2, GDPR, WCAG AA | Audits, automated checks |
| 6 | **UX** | Intuitive, delightful interactions | User testing, analytics |
| 7 | **UI** | Sophisticated, aesthetic, rich | Design reviews, brand alignment |
| 8 | **Accessibility** | Universal access for all abilities | WCAG audits, screen reader tests |
| 9 | **Documentation** | Self-documenting code + JSDoc | Doc coverage checks |
| 10 | **TDD** | Tests first, then implementation | Coverage thresholds |
| 11 | **Maintainability** | Clean, modular, scalable | Code reviews, metrics |

---

## 1. Quality Standards

### Code Quality Metrics

| Metric | Threshold | Tool |
|--------|-----------|------|
| Test Coverage | ≥ 80% | Jest, Vitest |
| Cyclomatic Complexity | ≤ 10 | ESLint |
| Duplication | ≤ 3% | SonarQube |
| Technical Debt Ratio | ≤ 5% | SonarQube |
| Code Smells | 0 blockers/critical | SonarQube |

### Quality Gates

```yaml
# Every PR must pass:
quality_gates:
  - lint: "npm run lint" # Zero errors
  - typecheck: "tsc --noEmit" # Zero errors
  - test: "npm test" # All pass, ≥80% coverage
  - build: "npm run build" # Successful
  - security: "npm audit --audit-level=high" # Zero high/critical
  - a11y: "npm run test:a11y" # WCAG AA compliance
```

### Code Review Standards

Every PR requires:
- [ ] 2 approvals minimum
- [ ] All automated checks pass
- [ ] Security review (for sensitive changes)
- [ ] Accessibility review (for UI changes)
- [ ] Performance review (for critical paths)

---

## 2. Performance Standards

### Frontend Performance

| Metric | Target | Measurement |
|--------|--------|-------------|
| Largest Contentful Paint (LCP) | ≤ 2.5s | Lighthouse |
| First Input Delay (FID) | ≤ 100ms | Lighthouse |
| Cumulative Layout Shift (CLS) | ≤ 0.1 | Lighthouse |
| Time to Interactive (TTI) | ≤ 3.8s | Lighthouse |
| Lighthouse Performance Score | ≥ 90 | Lighthouse |
| Bundle Size (gzipped) | ≤ 200KB initial | Webpack analyzer |

### Backend Performance

| Metric | Target | Measurement |
|--------|--------|-------------|
| API Response Time (p95) | ≤ 200ms | APM |
| Database Query Time | ≤ 50ms | Query profiling |
| Throughput | ≥ 1000 req/s | Load testing |
| Error Rate | ≤ 0.1% | Monitoring |
| Memory Usage | ≤ 512MB base | Metrics |

### Performance Checklist

```typescript
// ✅ DO: Optimize for performance
const users = await db.user.findMany({
  select: { id: true, name: true }, // Only needed fields
  take: 20, // Pagination
});

// ❌ DON'T: Unoptimized queries
const users = await db.user.findMany(); // All fields, no limit
```

---

## 3. Security Standards

### OWASP Compliance Matrix

| OWASP | Requirement | Implementation | Agent |
|-------|-------------|----------------|-------|
| A01 | Access Control | RBAC, deny by default | `@owasp-expert` |
| A02 | Cryptography | AES-256, TLS 1.3, bcrypt | `@cybersecurity-architect` |
| A03 | Injection | Parameterized queries | `@owasp-expert` |
| A04 | Secure Design | Threat modeling | `@cybersecurity-architect` |
| A05 | Configuration | Hardened defaults | `@devops-engineer` |
| A06 | Components | SBOM, dependency scanning | `@opensource-standards` |
| A07 | Authentication | MFA, secure sessions | `@owasp-expert` |
| A08 | Integrity | Signed artifacts, SRI | `@devops-engineer` |
| A09 | Logging | Centralized, 90+ days | `@soc2-auditor` |
| A10 | SSRF | URL validation | `@owasp-expert` |

### Security Checklist

- [ ] All inputs validated server-side
- [ ] All outputs encoded properly
- [ ] Parameterized queries everywhere
- [ ] Secrets in vault (never in code)
- [ ] Security headers configured
- [ ] Rate limiting implemented
- [ ] MFA available for users
- [ ] Audit logging enabled
- [ ] Dependencies scanned weekly
- [ ] Penetration testing annually

---

## 4. Compliance Standards

### Regulatory Matrix

| Regulation | Requirements | Agent | Verification |
|------------|--------------|-------|--------------|
| **GDPR** | Data privacy, consent, DPA | `@compliance-officer` | Privacy audit |
| **SOC2** | Trust Service Criteria | `@soc2-auditor` | Type II audit |
| **WCAG 2.1** | Level AA accessibility | `@accessibility-expert` | Axe audit |
| **PCI-DSS** | Payment security | `@soc2-auditor` | Compliance scan |
| **HIPAA** | Health data protection | `@compliance-officer` | Security review |

### SOC2 Trust Service Criteria

| Criteria | Implementation |
|----------|----------------|
| **Security** | Access controls, encryption, monitoring |
| **Availability** | 99.9% SLA, DR plan, backups |
| **Processing Integrity** | Validation, error handling, reconciliation |
| **Confidentiality** | Data classification, encryption, access logs |
| **Privacy** | Consent, retention, subject rights |

---

## 5. UX Standards

### Interaction Design Principles

| Principle | Standard | Verification |
|-----------|----------|--------------|
| **Discoverability** | Features findable in ≤3 clicks | User testing |
| **Feedback** | All actions have visible response | UI review |
| **Consistency** | Same patterns throughout | Design audit |
| **Error Prevention** | Confirm destructive actions | UX review |
| **Recovery** | Undo available, clear errors | Functional testing |
| **Efficiency** | Common tasks optimized | Time-on-task metrics |

### UX Checklist

- [ ] Clear visual hierarchy
- [ ] Consistent navigation patterns
- [ ] Immediate feedback on actions
- [ ] Helpful error messages (not technical jargon)
- [ ] Progress indicators for long operations
- [ ] Keyboard shortcuts for power users
- [ ] Responsive to all screen sizes
- [ ] Touch-friendly on mobile
- [ ] Loading states that don't block
- [ ] Empty states that guide users

---

## 6. UI/Design Standards

### Visual Design System

| Element | Standard | Implementation |
|---------|----------|----------------|
| **Typography** | Clear hierarchy, readable | Design tokens |
| **Color** | Accessible contrast, brand-aligned | CSS variables |
| **Spacing** | Consistent rhythm | 4px/8px grid |
| **Motion** | Purposeful, not distracting | CSS transitions |
| **Icons** | Consistent style, meaningful | Icon system |
| **Components** | Reusable, documented | Component library |

### Design Quality Checklist

- [ ] Follows design system tokens
- [ ] Color contrast ≥ 4.5:1 (text), ≥ 3:1 (UI)
- [ ] Typography scale consistent
- [ ] Spacing follows grid system
- [ ] Icons are meaningful and labeled
- [ ] Animations enhance, not distract
- [ ] Dark/light mode support
- [ ] Brand guidelines followed
- [ ] Mobile-first responsive
- [ ] Print styles (if applicable)

### Rich UI Requirements

```typescript
// ✅ Sophisticated UI patterns
- Micro-interactions on hover/focus
- Smooth transitions (150-300ms)
- Skeleton loading states
- Progressive disclosure
- Contextual help tooltips
- Inline validation feedback
- Smart defaults
- Personalization options
```

---

## 7. Accessibility Standards

### WCAG 2.1 AA Requirements

| Category | Requirement | Implementation |
|----------|-------------|----------------|
| **Perceivable** | Text alternatives, captions | Alt text, transcripts |
| **Operable** | Keyboard accessible, timing | Tab order, skip links |
| **Understandable** | Readable, predictable | Plain language, consistency |
| **Robust** | Compatible with AT | Semantic HTML, ARIA |

### Accessibility Checklist

- [ ] All images have alt text
- [ ] Videos have captions
- [ ] Color is not sole indicator
- [ ] Contrast ratios meet standards
- [ ] Keyboard navigation complete
- [ ] Focus indicators visible
- [ ] Screen reader compatible
- [ ] ARIA labels where needed
- [ ] Form labels explicit
- [ ] Error messages announced

### Testing Requirements

```bash
# Automated testing
npm run test:a11y # Axe-core
npx lighthouse --accessibility

# Manual testing
- [ ] Keyboard-only navigation test
- [ ] Screen reader test (NVDA/VoiceOver)
- [ ] Zoom to 200% test
- [ ] High contrast mode test
```

---

## 8. Documentation Standards

### Code Documentation

| Type | Requirement | Tool |
|------|-------------|------|
| **JSDoc** | All exported functions | TypeDoc |
| **README** | Every package/module | Markdown |
| **API Docs** | All endpoints documented | OpenAPI |
| **Architecture** | System design documented | Diagrams |
| **Changelog** | All changes logged | Conventional Commits |

### JSDoc Requirements

```typescript
/**
 * Authenticates a user with email and password.
 *
 * @param email - The user's email address
 * @param password - The user's password (will be hashed)
 * @returns The authenticated user with session token
 * @throws {AuthError} When credentials are invalid
 * @throws {RateLimitError} When too many attempts
 *
 * @example
 * ```typescript
 * const user = await authenticate('user@example.com', 'password123');
 * console.log(user.token);
 * ```
 *
 * @see {@link logout} for ending sessions
 * @since 1.0.0
 */
async function authenticate(email: string, password: string): Promise<User> {
  // implementation
}
```

### Documentation Coverage

| Type | Minimum | Verification |
|------|---------|--------------|
| Public API | 100% | TypeDoc coverage |
| Internal functions | 80% | JSDoc linting |
| Components | 100% | Storybook stories |
| API endpoints | 100% | OpenAPI spec |

---

## 9. Test-Driven Development Standards

### TDD Process

```
1. 🔴 RED: Write failing test first
2. 🟢 GREEN: Write minimum code to pass
3. 🔵 REFACTOR: Improve while tests pass
```

### Test Coverage Requirements

| Type | Coverage | Location |
|------|----------|----------|
| Unit Tests | ≥ 80% | `__tests__/*.test.ts` |
| Integration Tests | Critical paths | `__tests__/*.integration.ts` |
| E2E Tests | Happy paths | `e2e/*.spec.ts` |
| Visual Tests | UI components | Storybook/Chromatic |
| Performance Tests | Critical endpoints | k6/Artillery |

### Test Quality Standards

```typescript
// ✅ Good Test: Descriptive, focused, independent
describe('UserAuthenticationService', () => {
  describe('authenticate', () => {
    it('should return user with valid token when credentials are correct', async () => {
      // Arrange
      const validEmail = 'user@example.com';
      const validPassword = 'SecurePass123!';
      await createTestUser(validEmail, validPassword);

      // Act
      const result = await authService.authenticate(validEmail, validPassword);

      // Assert
      expect(result.user.email).toBe(validEmail);
      expect(result.token).toMatch(/^eyJ/); // JWT format
      expect(result.expiresAt).toBeInstanceOf(Date);
    });

    it('should throw AuthError when password is incorrect', async () => {
      // Arrange
      await createTestUser('user@example.com', 'CorrectPassword');

      // Act & Assert
      await expect(
        authService.authenticate('user@example.com', 'WrongPassword')
      ).rejects.toThrow(AuthError);
    });
  });
});

// ❌ Bad Test: Vague, tests implementation
it('should work', () => {
  expect(service.authenticate()).toBeTruthy();
});
```

---

## 🔟 Maintainability Standards

### Code Architecture

| Principle | Implementation |
|-----------|----------------|
| **Single Responsibility** | One reason to change per module |
| **Open/Closed** | Extend, don't modify |
| **Liskov Substitution** | Subtypes substitutable |
| **Interface Segregation** | Small, focused interfaces |
| **Dependency Inversion** | Depend on abstractions |

### File Organization

```
src/
├── components/          # React components
│   ├── Button/
│   │   ├── Button.tsx
│   │   ├── Button.test.tsx
│   │   ├── Button.stories.tsx
│   │   └── index.ts
├── hooks/               # Custom React hooks
├── services/            # Business logic
├── utils/               # Pure utilities
├── types/               # TypeScript types
└── __tests__/           # Integration tests
```

### Code Metrics

| Metric | Maximum | Tool |
|--------|---------|------|
| File size | 300 lines | ESLint |
| Function size | 30 lines | ESLint |
| Parameters | 4 | ESLint |
| Nesting depth | 3 | ESLint |
| Cognitive complexity | 15 | SonarQube |

---

## 10. Quality Gates Matrix

### PR Merge Requirements

| Gate | Requirement | Blocking |
|------|-------------|----------|
| Build | Successful | ✅ Yes |
| Lint | Zero errors | ✅ Yes |
| TypeScript | Zero errors | ✅ Yes |
| Unit Tests | All pass | ✅ Yes |
| Coverage | ≥ 80% | ✅ Yes |
| Security Scan | No high/critical | ✅ Yes |
| Accessibility | WCAG AA pass | ✅ Yes |
| Performance | No regression | ✅ Yes |
| Code Review | 2 approvals | ✅ Yes |
| Documentation | JSDoc complete | ⚠️ Warning |

### Release Requirements

| Gate | Requirement | Agent |
|------|-------------|-------|
| All PRs merged | ✅ | `@orchestrator` |
| Integration tests | ✅ | `@testing-specialist` |
| E2E tests | ✅ | `@testing-specialist` |
| Security audit | ✅ | `@owasp-expert` |
| Accessibility audit | ✅ | `@accessibility-expert` |
| Performance baseline | ✅ | `@backend-dev` |
| Documentation updated | ✅ | `@docs-writer` |
| Changelog updated | ✅ | `@docs-writer` |

---

## 11. Enforcement

### Automated Enforcement

```json
// package.json
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx",
    "typecheck": "tsc --noEmit",
    "test": "vitest run --coverage",
    "test:a11y": "jest-axe",
    "test:e2e": "playwright test",
    "test:perf": "k6 run load-test.js",
    "security": "npm audit --audit-level=high",
    "docs": "typedoc --entryPoints src/index.ts"
  }
}
```

### CI/CD Pipeline

```yaml
# .github/workflows/quality.yml
name: Quality Gates

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: TypeCheck
        run: npm run typecheck
      
      - name: Test with Coverage
        run: npm run test -- --coverage
      
      - name: Security Scan
        run: npm audit --audit-level=high
      
      - name: Accessibility Test
        run: npm run test:a11y
      
      - name: Build
        run: npm run build
      
      - name: Performance Test
        run: npm run test:perf
```

---

---

## 📊 Completion Tracking

> Track progress toward shipping, not just task completion.

### Completion Dashboard

```
📊 Project Completion Status

MVP Progress: ████████░░ 80%
├─ Core Features:    ████████████ 100% ✅
├─ Basic Tests:      █████████░░░  90% ✅  
├─ Security (Basic): ███████░░░░░  75% ⚠️
└─ Build & Deploy:   ██████░░░░░░  60% ⚠️

Production Progress: ████░░░░░░ 40%
├─ Quality Gates:    ██████░░░░░░  60%
├─ Test Coverage:    ████░░░░░░░░  45%
├─ Documentation:    ███░░░░░░░░░  35%
└─ Compliance:       ███░░░░░░░░░  30%

🎯 Next Steps to MVP:
1. [ ] Complete security review (P0)
2. [ ] Fix remaining critical bugs (P0)
3. [ ] Deploy to staging (P0)
```

### Progress Metrics

| Metric | MVP Target | Production Target |
|--------|------------|-------------------|
| Core Features Complete | 100% | 100% |
| P0 Tasks Done | 100% | 100% |
| P1 Tasks Done | 80% | 100% |
| Test Coverage | 50% | 80% |
| Critical Bugs | 0 | 0 |
| High Bugs | ≤3 | 0 |
| Security Issues | 0 critical | 0 high/critical |

### Definition of "Done" by Tier

#### MVP Done = Shippable

```markdown
## MVP Finish Line ✓

- [x] All P0 tasks complete
- [x] All P1 tasks complete (or explicitly deferred)
- [x] Core user journey works end-to-end
- [x] No critical/high bugs
- [x] Basic security checks pass
- [x] Can deploy to production
- [x] Team has tested internally
```

#### Production Done = Sustainable

```markdown
## Production Finish Line ✓

- [x] All MVP requirements
- [x] ≥80% test coverage
- [x] All quality gates pass
- [x] WCAG AA accessible
- [x] Documentation complete
- [x] Security audit passed
- [x] Performance targets met
- [x] Monitoring & alerting set up
```

---

## 🧘 Anti-Overwhelm Guidelines

> Finishing beats perfecting. Ship, then iterate.

### The 80/20 Rule for Shipping

| Focus 80% effort on... | Spend 20% on... |
|------------------------|-----------------|
| Core user journey | Edge cases |
| Happy path | Error states |
| P0/P1 features | P2/P3 nice-to-haves |
| Working code | Perfect code |
| Shipping | Polishing |

### When You Feel Overwhelmed

1. **Stop and assess**
   ```bash
   /completion-status  # See where you really are
   ```

2. **Focus on MVP only**
   ```bash
   /focus mvp          # Hide P2/P3 tasks
   ```

3. **Identify blockers**
   - What is the ONE thing blocking MVP?
   - Do that thing first

4. **Ship something**
   - A working MVP > Perfect vaporware
   - Get feedback early
   - Iterate based on real usage

### Red Flags You're Over-Engineering

| Red Flag | What to Do |
|----------|------------|
| Spending days on "architecture" | Ship first, refactor later |
| Building features nobody asked for | Check your P0/P1 list |
| Endless refactoring | If it works, ship it |
| Waiting for "one more thing" | That's scope creep |
| Paralyzed by quality standards | Use MVP tier |

### The Shipping Mindset

```
┌─────────────────────────────────────────────────────────────────┐
│                     THE SHIPPING MINDSET                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│   ❌ Wrong: "I need to finish everything before I can ship"      │
│                                                                   │
│   ✅ Right: "What's the smallest thing I can ship today?"        │
│                                                                   │
│   ❌ Wrong: "This needs to be perfect"                           │
│                                                                   │
│   ✅ Right: "This needs to be good enough to get feedback"       │
│                                                                   │
│   ❌ Wrong: "Let me add one more feature..."                     │
│                                                                   │
│   ✅ Right: "That's P2, I'll add it after MVP ships"             │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Daily Check-in

Before starting work each day:

1. **What tier am I targeting?** (MVP or Production)
2. **What P0/P1 task moves me closest to done?**
3. **What can I defer to post-MVP?**
4. **What's my finish line for today?**

---

*"We don't ship until every standard is met. Quality is not negotiable."*

*...but we're smart about WHICH standards apply at each stage.*

*"Done is better than perfect. Ship the MVP, then harden."*

