---
description: Performance testing expertise
triggers:
  - performance testing
  - load testing
  - benchmarking
  - lighthouse
---

# Performance Testing Skill

Expert performance testing capabilities.

## Lighthouse Automation

```typescript
// scripts/lighthouse.ts
import lighthouse from 'lighthouse'
import * as chromeLauncher from 'chrome-launcher'

async function runLighthouse(url: string) {
  const chrome = await chromeLauncher.launch({ chromeFlags: ['--headless'] })
  
  const result = await lighthouse(url, {
    port: chrome.port,
    onlyCategories: ['performance'],
  })
  
  await chrome.kill()
  
  return result.lhr
}

// In test
it('meets performance budget', async () => {
  const result = await runLighthouse('http://localhost:3000')
  
  expect(result.categories.performance.score).toBeGreaterThan(0.9)
  expect(result.audits['largest-contentful-paint'].numericValue).toBeLessThan(2500)
  expect(result.audits['cumulative-layout-shift'].numericValue).toBeLessThan(0.1)
})
```

## Load Testing with K6

```javascript
// Basic load test
import http from 'k6/http'
import { check } from 'k6'

export const options = {
  vus: 50,
  duration: '2m',
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
}

export default function () {
  const res = http.get('http://localhost:3000/api/users')
  check(res, {
    'status 200': (r) => r.status === 200,
    'fast response': (r) => r.timings.duration < 500,
  })
}
```

## Core Web Vitals

```typescript
// Measure in browser
interface WebVitals {
  LCP: number  // Largest Contentful Paint
  FID: number  // First Input Delay
  CLS: number  // Cumulative Layout Shift
}

async function measureWebVitals(page: Page): Promise<WebVitals> {
  return page.evaluate(() => {
    return new Promise((resolve) => {
      const vitals: Partial<WebVitals> = {}
      
      new PerformanceObserver((list) => {
        const entries = list.getEntries()
        const lastEntry = entries[entries.length - 1]
        vitals.LCP = lastEntry.startTime
      }).observe({ type: 'largest-contentful-paint', buffered: true })
      
      new PerformanceObserver((list) => {
        const entries = list.getEntries()
        vitals.FID = entries[0].processingStart - entries[0].startTime
      }).observe({ type: 'first-input', buffered: true })
      
      new PerformanceObserver((list) => {
        let cls = 0
        for (const entry of list.getEntries()) {
          if (!entry.hadRecentInput) {
            cls += entry.value
          }
        }
        vitals.CLS = cls
      }).observe({ type: 'layout-shift', buffered: true })
      
      setTimeout(() => resolve(vitals as WebVitals), 5000)
    })
  })
}
```

## Bundle Size Tracking

```typescript
// scripts/check-bundle-size.ts
import { statSync, readdirSync } from 'fs'
import { join } from 'path'

const BUDGET_KB = 300

function getDirectorySize(dir: string): number {
  let size = 0
  for (const file of readdirSync(dir, { withFileTypes: true })) {
    const path = join(dir, file.name)
    if (file.isDirectory()) {
      size += getDirectorySize(path)
    } else if (file.name.endsWith('.js')) {
      size += statSync(path).size
    }
  }
  return size
}

const bundleSize = getDirectorySize('.next/static')
const bundleSizeKB = bundleSize / 1024

if (bundleSizeKB > BUDGET_KB) {
  console.error(`Bundle size ${bundleSizeKB}KB exceeds budget ${BUDGET_KB}KB`)
  process.exit(1)
}
```

## Benchmarking Functions

```typescript
import { bench, describe } from 'vitest'

describe('Array operations', () => {
  const array = Array.from({ length: 10000 }, (_, i) => i)

  bench('forEach', () => {
    array.forEach(x => x * 2)
  })

  bench('map', () => {
    array.map(x => x * 2)
  })

  bench('for loop', () => {
    for (let i = 0; i < array.length; i++) {
      array[i] * 2
    }
  })
})
```

## When to Use

Apply when:
- Checking Lighthouse scores
- Running load tests
- Tracking bundle sizes
- Benchmarking code

