---
description: Run security and penetration tests
arguments:
  - name: action
    description: Action (scan, pentest, dependency, sast)
    required: true
  - name: target
    description: URL or file to test
    required: false
---

# Security Testing Command

Run security scans, penetration tests, and vulnerability assessments.

## Dependency Scan (`/security dependency`)

```bash
/security dependency
/security dependency --fix
```

### npm audit

```bash
# Check for vulnerabilities
npm audit

# Fix automatically
npm audit fix

# Full report as JSON
npm audit --json
```

### Snyk Integration

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  snyk:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high
```

## Static Analysis (SAST) (`/security sast`)

```bash
/security sast
/security sast path=src/
```

### Semgrep Rules

```yaml
# .semgrep.yml
rules:
  - id: hardcoded-secret
    patterns:
      - pattern-either:
          - pattern: $X = "...$SECRET..."
          - pattern: password = "..."
          - pattern: apiKey = "..."
    message: Hardcoded secret detected
    severity: ERROR

  - id: sql-injection
    patterns:
      - pattern: |
          $QUERY = `... ${$USER_INPUT} ...`
          $DB.query($QUERY)
    message: Potential SQL injection
    severity: ERROR

  - id: xss-vulnerability
    patterns:
      - pattern: dangerouslySetInnerHTML={{ __html: $USER_INPUT }}
    message: Potential XSS vulnerability
    severity: WARNING
```

## Penetration Testing (`/security pentest`)

```bash
/security pentest url=http://localhost:3000
```

### OWASP ZAP Scan

```yaml
# zap-config.yaml
env:
  contexts:
    - name: "Application"
      urls:
        - "http://localhost:3000"
      authentication:
        method: "form"
        parameters:
          loginUrl: "http://localhost:3000/auth/login"
          loginRequestData: "email={%username%}&password={%password%}"
          
jobs:
  - type: spider
    parameters:
      maxDuration: 5
      
  - type: activeScan
    parameters:
      maxRuleDurationInMins: 10
      
  - type: report
    parameters:
      template: "risk-confidence-html"
      reportFile: "zap-report.html"
```

### Common Penetration Tests

```typescript
// tests/security/pentest.spec.ts
import { test, expect } from '@playwright/test'

test.describe('Security Tests', () => {
  
  test('should not expose sensitive headers', async ({ request }) => {
    const response = await request.get('/')
    
    // Check security headers
    expect(response.headers()['x-frame-options']).toBe('DENY')
    expect(response.headers()['x-content-type-options']).toBe('nosniff')
    expect(response.headers()['strict-transport-security']).toBeDefined()
    
    // Should not expose server info
    expect(response.headers()['server']).toBeUndefined()
    expect(response.headers()['x-powered-by']).toBeUndefined()
  })

  test('should prevent SQL injection', async ({ request }) => {
    const response = await request.get('/api/users', {
      params: { id: "1'; DROP TABLE users; --" }
    })
    
    // Should not error in a way that exposes SQL
    expect(response.status()).toBe(400) // Bad request, not 500
    const body = await response.text()
    expect(body).not.toContain('SQL')
    expect(body).not.toContain('syntax')
  })

  test('should prevent XSS', async ({ page }) => {
    await page.goto('/search?q=<script>alert(1)</script>')
    
    // Check that script is escaped, not executed
    const content = await page.content()
    expect(content).not.toContain('<script>alert(1)</script>')
    expect(content).toContain('&lt;script&gt;')
  })

  test('should enforce CSRF protection', async ({ request }) => {
    const response = await request.post('/api/users', {
      data: { name: 'Test' },
      // Missing CSRF token
    })
    
    expect(response.status()).toBe(403)
  })

  test('should rate limit login attempts', async ({ request }) => {
    // Attempt many failed logins
    for (let i = 0; i < 10; i++) {
      await request.post('/api/auth/login', {
        data: { email: 'test@test.com', password: 'wrong' }
      })
    }
    
    // 11th attempt should be rate limited
    const response = await request.post('/api/auth/login', {
      data: { email: 'test@test.com', password: 'wrong' }
    })
    
    expect(response.status()).toBe(429)
  })

  test('should not expose stack traces in production', async ({ request }) => {
    const response = await request.get('/api/error-endpoint')
    
    expect(response.status()).toBe(500)
    const body = await response.json()
    
    expect(body.stack).toBeUndefined()
    expect(body.error).not.toContain('/home/')
    expect(body.error).not.toContain('at ')
  })
})
```

## Vulnerability Report Format

```
🔒 SECURITY SCAN REPORT
═══════════════════════════════════════════════════════════════

Target: http://localhost:3000
Date: 2024-12-15
Scanner: OWASP ZAP + Semgrep + npm audit

SUMMARY
───────────────────────────────────────────────────────────────
🔴 Critical:  0
🟠 High:      2
🟡 Medium:    5
🟢 Low:       8

HIGH SEVERITY
───────────────────────────────────────────────────────────────

[SEC-001] Missing Content-Security-Policy Header
Risk: Cross-Site Scripting (XSS)
Location: All responses
Fix: Add CSP header with strict policy

[SEC-002] Outdated Dependency: lodash@4.17.20
Risk: Prototype Pollution (CVE-2021-23337)
Location: package.json
Fix: npm update lodash

MEDIUM SEVERITY
───────────────────────────────────────────────────────────────

[SEC-003] Missing Rate Limiting on /api/contact
[SEC-004] Session cookie missing SameSite attribute
[SEC-005] CORS allows any origin in development

RECOMMENDATIONS
───────────────────────────────────────────────────────────────

1. Implement Content-Security-Policy header
2. Update all dependencies with known vulnerabilities
3. Add rate limiting to all public endpoints
4. Configure CORS properly for production
5. Enable HTTP-only and Secure flags on all cookies
```

## Guidelines

1. **Run in CI/CD** - Security scans on every PR
2. **Fix critical/high immediately**
3. **Regular penetration tests** - At least quarterly
4. **Keep dependencies updated** - Automated updates
5. **Security headers** - CSP, HSTS, X-Frame-Options

