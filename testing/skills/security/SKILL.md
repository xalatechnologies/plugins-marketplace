---
description: Security testing expertise
triggers:
  - security testing
  - penetration testing
  - vulnerability scanning
  - dependency audit
---

# Security Testing Skill

Expert security testing capabilities.

## Dependency Scanning

```bash
# npm audit
npm audit --audit-level=moderate

# Fix vulnerabilities
npm audit fix

# Snyk
npx snyk test
npx snyk monitor
```

## Security Headers Check

```typescript
it('has required security headers', async ({ request }) => {
  const response = await request.get('/')
  const headers = response.headers()
  
  // Required headers
  expect(headers['x-frame-options']).toBe('DENY')
  expect(headers['x-content-type-options']).toBe('nosniff')
  expect(headers['x-xss-protection']).toBe('1; mode=block')
  expect(headers['strict-transport-security']).toContain('max-age=')
  expect(headers['content-security-policy']).toBeDefined()
  
  // Should NOT expose
  expect(headers['server']).toBeUndefined()
  expect(headers['x-powered-by']).toBeUndefined()
})
```

## Common Vulnerability Tests

```typescript
describe('Security Tests', () => {
  test('prevents SQL injection', async ({ request }) => {
    const response = await request.get('/api/users', {
      params: { id: "1' OR '1'='1" }
    })
    expect(response.status()).toBe(400)
  })

  test('prevents XSS', async ({ page }) => {
    await page.goto('/search?q=<script>alert(1)</script>')
    const alerts = []
    page.on('dialog', d => alerts.push(d))
    await page.waitForTimeout(1000)
    expect(alerts).toHaveLength(0)
  })

  test('prevents path traversal', async ({ request }) => {
    const response = await request.get('/api/files', {
      params: { path: '../../../etc/passwd' }
    })
    expect(response.status()).toBe(400)
  })

  test('rate limits login attempts', async ({ request }) => {
    for (let i = 0; i < 10; i++) {
      await request.post('/api/auth/login', {
        data: { email: 'test@test.com', password: 'wrong' }
      })
    }
    
    const response = await request.post('/api/auth/login', {
      data: { email: 'test@test.com', password: 'wrong' }
    })
    expect(response.status()).toBe(429)
  })
})
```

## OWASP Top 10 Checklist

```typescript
// A01: Broken Access Control
test('requires authentication for protected routes', async ({ request }) => {
  const response = await request.get('/api/admin/users')
  expect(response.status()).toBe(401)
})

// A02: Cryptographic Failures
test('uses HTTPS', async ({ page }) => {
  await page.goto('/')
  expect(page.url()).toMatch(/^https:/)
})

// A03: Injection
test('validates input', async ({ request }) => {
  const response = await request.post('/api/users', {
    data: { email: 'not-an-email' }
  })
  expect(response.status()).toBe(400)
})

// A05: Security Misconfiguration
test('no debug mode in production', async ({ request }) => {
  const response = await request.get('/api/debug')
  expect(response.status()).toBe(404)
})
```

## CSP Validation

```typescript
function validateCSP(csp: string): string[] {
  const issues = []
  
  if (csp.includes("'unsafe-inline'")) {
    issues.push("CSP allows unsafe-inline scripts")
  }
  if (csp.includes("'unsafe-eval'")) {
    issues.push("CSP allows unsafe-eval")
  }
  if (csp.includes('*')) {
    issues.push("CSP has wildcard source")
  }
  if (!csp.includes('upgrade-insecure-requests')) {
    issues.push("CSP missing upgrade-insecure-requests")
  }
  
  return issues
}
```

## When to Use

Apply when:
- Auditing dependencies
- Testing for vulnerabilities
- Checking security headers
- Validating input handling

