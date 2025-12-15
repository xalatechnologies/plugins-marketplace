---
description: Detect security, quality, compliance, and performance issues in the codebase
arguments:
  - name: category
    description: Issue category to focus on (all, security, quality, compliance, performance)
    required: false
    default: all
  - name: severity
    description: Minimum severity to report (critical, high, medium, low)
    required: false
    default: low
---

# Pitfalls Detection Command

Scan the codebase for common issues and anti-patterns.

## Detection Categories

### 🔴 Security Issues

**Critical:**
- Hardcoded secrets: `password|secret|key|token\s*[:=]\s*['"][^'"]+['"]`
- SQL injection: Raw SQL with string interpolation
- Exposed API keys in client code
- Missing authentication on sensitive routes

**High:**
- CSRF vulnerabilities (forms without tokens)
- XSS vulnerabilities (unescaped user input)
- Insecure dependencies (check npm audit, snyk)
- Missing rate limiting on auth endpoints

**Medium:**
- Weak password requirements
- Session without expiry
- Debug mode enabled
- Verbose error messages exposing internals

### 🟡 Quality Issues

**High:**
- Files over 300 lines (violates engineering standards)
- Functions with cyclomatic complexity > 10
- Deeply nested code (> 4 levels)
- Missing error handling on async operations

**Medium:**
- TODO/FIXME comments older than 30 days
- Dead code (unused functions, imports)
- Inconsistent naming conventions
- Missing TypeScript strict mode

**Low:**
- Missing JSDoc comments on public APIs
- Magic numbers without constants
- Inconsistent formatting
- Long parameter lists (> 4 params)

### ⚖️ Compliance Issues (Xala PM Specific)

**Critical:**
- Security token public trading enabled
- KYC bypass patterns
- Missing audit logging on mutations
- Direct FIAT handling

**High:**
- Missing whitelist verification
- No pause mechanism for security tokens
- Incomplete audit trail
- Missing compliance rules validation

### ⚡ Performance Issues

**High:**
- N+1 query patterns (await inside map/forEach)
- Missing pagination on list endpoints
- Large bundle sizes (> 500KB)
- Synchronous file operations

**Medium:**
- Missing memoization on expensive computations
- Unoptimized images
- Missing lazy loading
- Excessive re-renders (React)

## Output Format

```
⚠️ PITFALLS DETECTED
═══════════════════════════════════════════════════════════════

🔴 CRITICAL ([count])

┌─────────────────────────────────────────────────────────────┐
│ [ID]: [Title]                                               │
├─────────────────────────────────────────────────────────────┤
│ Location: [file:line]                                       │
│ Code:     [relevant code snippet]                           │
│                                                             │
│ Impact:   [What could go wrong]                             │
│ Fix:      [How to fix it]                                   │
│ Effort:   [trivial/small/medium/large]                      │
│ Auto-fix: [Yes/No]                                          │
└─────────────────────────────────────────────────────────────┘

🟠 HIGH ([count])
[Similar format...]

🟡 MEDIUM ([count])
[Similar format...]

🔵 LOW ([count])
[Summarized list...]

───────────────────────────────────────────────────────────────
SUMMARY BY CATEGORY

Security:        [bar] [count] issues
Quality:         [bar] [count] issues
Compliance:      [bar] [count] issues
Performance:     [bar] [count] issues

ESTIMATED FIX TIME: [hours]
AUTO-FIXABLE: [percentage]%
```

## Guidelines

- Always provide specific file paths and line numbers
- Include code snippets that demonstrate the issue
- Suggest concrete fixes, not vague recommendations
- Prioritize by impact, not just severity
- Group related issues together
- Identify patterns (e.g., "same issue in 15 files")

