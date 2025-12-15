---
description: Run performance tests and benchmarks
arguments:
  - name: action
    description: Action (lighthouse, load, benchmark, profile)
    required: true
  - name: target
    description: URL or function to test
    required: false
---

# Performance Testing Command

Run performance tests, load tests, and benchmarks.

## Lighthouse Performance Audit (`/performance lighthouse`)

```bash
/performance lighthouse url=http://localhost:3000
/performance lighthouse url=/dashboard
```

### Lighthouse Configuration

```javascript
// lighthouse.config.js
module.exports = {
  extends: 'lighthouse:default',
  settings: {
    onlyCategories: ['performance', 'accessibility', 'best-practices', 'seo'],
    formFactor: 'desktop',
    throttling: {
      rttMs: 40,
      throughputKbps: 10240,
      cpuSlowdownMultiplier: 1,
    },
    screenEmulation: {
      mobile: false,
      width: 1920,
      height: 1080,
    },
  },
}
```

### Performance Budgets

```json
// budget.json
[
  {
    "path": "/*",
    "timings": [
      { "metric": "first-contentful-paint", "budget": 1500 },
      { "metric": "largest-contentful-paint", "budget": 2500 },
      { "metric": "cumulative-layout-shift", "budget": 0.1 },
      { "metric": "total-blocking-time", "budget": 300 }
    ],
    "resourceSizes": [
      { "resourceType": "script", "budget": 300 },
      { "resourceType": "total", "budget": 500 }
    ]
  }
]
```

## Load Testing (`/performance load`)

```bash
/performance load url=http://localhost:3000/api/users
/performance load scenario=checkout
```

### K6 Load Test

```javascript
// tests/load/api-load.js
import http from 'k6/http'
import { check, sleep } from 'k6'
import { Rate } from 'k6/metrics'

const errorRate = new Rate('errors')

export const options = {
  stages: [
    { duration: '30s', target: 10 },   // Ramp up to 10 users
    { duration: '1m', target: 50 },    // Ramp up to 50 users
    { duration: '2m', target: 50 },    // Stay at 50 users
    { duration: '30s', target: 0 },    // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% of requests under 500ms
    errors: ['rate<0.1'],               // Error rate under 10%
  },
}

export default function () {
  const res = http.get('http://localhost:3000/api/users')
  
  const success = check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  })
  
  errorRate.add(!success)
  
  sleep(1)
}
```

### Scenario-Based Load Test

```javascript
// tests/load/checkout-scenario.js
import http from 'k6/http'
import { check, group, sleep } from 'k6'

const BASE_URL = 'http://localhost:3000'

export const options = {
  vus: 20,
  duration: '5m',
}

export default function () {
  group('Browse Products', () => {
    const res = http.get(`${BASE_URL}/api/products`)
    check(res, { 'products loaded': (r) => r.status === 200 })
    sleep(2)
  })

  group('View Product', () => {
    const res = http.get(`${BASE_URL}/api/products/1`)
    check(res, { 'product loaded': (r) => r.status === 200 })
    sleep(1)
  })

  group('Add to Cart', () => {
    const res = http.post(`${BASE_URL}/api/cart`, JSON.stringify({
      productId: 1,
      quantity: 1,
    }), { headers: { 'Content-Type': 'application/json' } })
    check(res, { 'added to cart': (r) => r.status === 201 })
    sleep(1)
  })

  group('Checkout', () => {
    const res = http.post(`${BASE_URL}/api/checkout`, JSON.stringify({
      paymentMethod: 'card',
    }), { headers: { 'Content-Type': 'application/json' } })
    check(res, { 'checkout successful': (r) => r.status === 200 })
  })
}
```

## Benchmarking (`/performance benchmark`)

```bash
/performance benchmark fn=hashPassword
/performance benchmark file=src/lib/crypto.ts
```

### Vitest Benchmarks

```typescript
// src/lib/crypto.bench.ts
import { bench, describe } from 'vitest'
import { hashPassword, verifyPassword } from './crypto'

describe('Password hashing', () => {
  bench('hashPassword', async () => {
    await hashPassword('testPassword123')
  })

  bench('verifyPassword', async () => {
    const hash = await hashPassword('testPassword123')
    await verifyPassword('testPassword123', hash)
  })
})

describe('String operations', () => {
  const longString = 'a'.repeat(10000)

  bench('String concatenation', () => {
    let result = ''
    for (let i = 0; i < 100; i++) {
      result += 'test'
    }
  })

  bench('Array join', () => {
    const parts = []
    for (let i = 0; i < 100; i++) {
      parts.push('test')
    }
    parts.join('')
  })
})
```

## Profiling (`/performance profile`)

```bash
/performance profile url=http://localhost:3000/dashboard
```

### React Profiling

```typescript
// Enable React Profiler
import { Profiler } from 'react'

function onRenderCallback(
  id: string,
  phase: 'mount' | 'update',
  actualDuration: number,
  baseDuration: number,
  startTime: number,
  commitTime: number
) {
  console.log({
    id,
    phase,
    actualDuration,
    baseDuration,
    startTime,
    commitTime,
  })
}

function App() {
  return (
    <Profiler id="Dashboard" onRender={onRenderCallback}>
      <Dashboard />
    </Profiler>
  )
}
```

## Performance Report Format

```
📊 PERFORMANCE REPORT
═══════════════════════════════════════════════════════════════

URL: http://localhost:3000/dashboard
Date: 2024-12-15

LIGHTHOUSE SCORES
───────────────────────────────────────────────────────────────
Performance:    92 🟢
Accessibility:  98 🟢
Best Practices: 95 🟢
SEO:            100 🟢

CORE WEB VITALS
───────────────────────────────────────────────────────────────
LCP (Largest Contentful Paint):     1.8s  🟢 (< 2.5s)
FID (First Input Delay):            45ms  🟢 (< 100ms)
CLS (Cumulative Layout Shift):      0.05  🟢 (< 0.1)

PERFORMANCE METRICS
───────────────────────────────────────────────────────────────
First Contentful Paint:     0.9s
Time to Interactive:        2.1s
Speed Index:                1.5s
Total Blocking Time:        150ms

OPPORTUNITIES
───────────────────────────────────────────────────────────────
⚠️ Reduce unused JavaScript (save 120kb)
⚠️ Serve images in next-gen formats (save 45kb)
⚠️ Eliminate render-blocking resources (save 0.5s)
```

## Guidelines

1. **Set performance budgets** and enforce in CI
2. **Test under realistic conditions** (network, CPU)
3. **Profile before optimizing** - measure first
4. **Focus on Core Web Vitals** for user experience
5. **Run load tests regularly** to catch regressions

