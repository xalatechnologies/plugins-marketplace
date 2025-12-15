---
description: E2E testing expertise with Playwright
triggers:
  - writing e2e tests
  - testing user flows
  - browser testing
  - playwright
---

# E2E Testing Skill

Expert Playwright end-to-end testing capabilities.

## Quick Patterns

### Page Navigation

```typescript
// Navigate and wait for load
await page.goto('/dashboard')
await page.waitForLoadState('networkidle')

// Wait for specific element
await page.goto('/dashboard')
await expect(page.getByRole('main')).toBeVisible()
```

### Element Selection (Accessibility-First)

```typescript
// ✅ Preferred: Role-based selectors
await page.getByRole('button', { name: 'Submit' }).click()
await page.getByRole('textbox', { name: 'Email' }).fill('test@test.com')
await page.getByRole('link', { name: 'Dashboard' }).click()
await page.getByRole('heading', { level: 1 }).toHaveText('Welcome')

// ✅ Good: Label/placeholder text
await page.getByLabel('Password').fill('secret')
await page.getByPlaceholder('Search...').fill('query')
await page.getByText('Click me').click()

// ⚠️ Last resort: Test IDs
await page.getByTestId('submit-button').click()

// ❌ Avoid: CSS selectors
await page.locator('.btn-primary').click() // Fragile
```

### Assertions

```typescript
// Visibility
await expect(page.getByRole('alert')).toBeVisible()
await expect(page.getByRole('dialog')).toBeHidden()

// Text content
await expect(page.getByRole('heading')).toHaveText('Dashboard')
await expect(page.getByRole('alert')).toContainText('Success')

// Attributes
await expect(page.getByRole('button')).toBeEnabled()
await expect(page.getByRole('button')).toBeDisabled()
await expect(page.getByRole('checkbox')).toBeChecked()

// URL
await expect(page).toHaveURL('/dashboard')
await expect(page).toHaveURL(/\/dashboard\/\d+/)

// Count
await expect(page.getByRole('listitem')).toHaveCount(5)
```

### Form Interaction

```typescript
// Fill form
await page.getByLabel('Email').fill('test@example.com')
await page.getByLabel('Password').fill('password123')
await page.getByRole('button', { name: 'Submit' }).click()

// Select dropdown
await page.getByLabel('Country').selectOption('norway')

// Checkbox
await page.getByLabel('Accept terms').check()
await page.getByLabel('Newsletter').uncheck()

// Radio
await page.getByLabel('Credit card').check()
```

### Waiting

```typescript
// Wait for element
await page.waitForSelector('[data-loaded="true"]')

// Wait for navigation
await Promise.all([
  page.waitForNavigation(),
  page.getByRole('link').click()
])

// Wait for network
await page.waitForResponse('/api/users')

// Wait for timeout (last resort)
await page.waitForTimeout(1000)
```

### Authentication Fixture

```typescript
// tests/fixtures.ts
import { test as base } from '@playwright/test'

type Fixtures = {
  authenticatedPage: Page
}

export const test = base.extend<Fixtures>({
  authenticatedPage: async ({ page }, use) => {
    await page.goto('/auth/login')
    await page.getByLabel('Email').fill(process.env.TEST_EMAIL!)
    await page.getByLabel('Password').fill(process.env.TEST_PASSWORD!)
    await page.getByRole('button', { name: 'Login' }).click()
    await expect(page).toHaveURL('/dashboard')
    await use(page)
  },
})

// Usage
test('authenticated user can view profile', async ({ authenticatedPage }) => {
  await authenticatedPage.goto('/profile')
  await expect(authenticatedPage.getByRole('heading')).toHaveText('Profile')
})
```

### Page Object Model

```typescript
// pages/DashboardPage.ts
export class DashboardPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/dashboard')
  }

  get heading() {
    return this.page.getByRole('heading', { level: 1 })
  }

  get createButton() {
    return this.page.getByRole('button', { name: 'Create New' })
  }

  async createItem(name: string) {
    await this.createButton.click()
    await this.page.getByLabel('Name').fill(name)
    await this.page.getByRole('button', { name: 'Save' }).click()
  }
}
```

## When to Use

Apply when:
- Creating E2E tests
- Testing user journeys
- Debugging flaky tests
- Setting up test fixtures

