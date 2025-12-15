---
description: Create or run E2E tests with Playwright
arguments:
  - name: action
    description: Action (create, run, debug)
    required: true
  - name: name
    description: Test name or feature to test
    required: false
---

# E2E Testing Command

Create and run end-to-end tests with Playwright.

## Create E2E Test (`/e2e create`)

```bash
/e2e create auth-flow
/e2e create dashboard-navigation
```

### Playwright Test Template

```typescript
// tests/e2e/auth.spec.ts
import { test, expect } from '@playwright/test'

test.describe('Authentication Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/')
  })

  test('should show login page for unauthenticated users', async ({ page }) => {
    await page.goto('/dashboard')
    
    // Should redirect to login
    await expect(page).toHaveURL('/auth/login')
    await expect(page.getByRole('heading', { name: 'Logg inn' })).toBeVisible()
  })

  test('should login with valid credentials', async ({ page }) => {
    await page.goto('/auth/login')
    
    // Fill login form
    await page.getByLabel('E-post').fill('test@example.com')
    await page.getByLabel('Passord').fill('password123')
    
    // Submit
    await page.getByRole('button', { name: 'Logg inn' }).click()
    
    // Should redirect to dashboard
    await expect(page).toHaveURL('/dashboard')
    await expect(page.getByText('Velkommen tilbake')).toBeVisible()
  })

  test('should show error for invalid credentials', async ({ page }) => {
    await page.goto('/auth/login')
    
    await page.getByLabel('E-post').fill('invalid@example.com')
    await page.getByLabel('Passord').fill('wrongpassword')
    await page.getByRole('button', { name: 'Logg inn' }).click()
    
    await expect(page.getByRole('alert')).toContainText('Ugyldig e-post eller passord')
  })

  test('should logout successfully', async ({ page }) => {
    // Login first (use helper)
    await loginAs(page, 'test@example.com', 'password123')
    
    // Logout
    await page.getByRole('button', { name: 'Profil' }).click()
    await page.getByRole('menuitem', { name: 'Logg ut' }).click()
    
    // Should be on login page
    await expect(page).toHaveURL('/auth/login')
  })
})

// Test helper
async function loginAs(page: Page, email: string, password: string) {
  await page.goto('/auth/login')
  await page.getByLabel('E-post').fill(email)
  await page.getByLabel('Passord').fill(password)
  await page.getByRole('button', { name: 'Logg inn' }).click()
  await expect(page).toHaveURL('/dashboard')
}
```

### Page Object Model Pattern

```typescript
// tests/e2e/pages/LoginPage.ts
import { Page, Locator } from '@playwright/test'

export class LoginPage {
  readonly page: Page
  readonly emailInput: Locator
  readonly passwordInput: Locator
  readonly submitButton: Locator
  readonly errorAlert: Locator

  constructor(page: Page) {
    this.page = page
    this.emailInput = page.getByLabel('E-post')
    this.passwordInput = page.getByLabel('Passord')
    this.submitButton = page.getByRole('button', { name: 'Logg inn' })
    this.errorAlert = page.getByRole('alert')
  }

  async goto() {
    await this.page.goto('/auth/login')
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email)
    await this.passwordInput.fill(password)
    await this.submitButton.click()
  }
}

// Usage in test
test('should login', async ({ page }) => {
  const loginPage = new LoginPage(page)
  await loginPage.goto()
  await loginPage.login('test@example.com', 'password123')
  await expect(page).toHaveURL('/dashboard')
})
```

## Run E2E Tests (`/e2e run`)

```bash
/e2e run                    # Run all E2E tests
/e2e run auth               # Run auth tests only
/e2e run --headed           # Run with browser visible
/e2e run --debug            # Run in debug mode
```

### Playwright Configuration

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
  ],

  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
})
```

## Visual Testing

```typescript
test('dashboard matches snapshot', async ({ page }) => {
  await loginAs(page, 'test@example.com', 'password123')
  await page.goto('/dashboard')
  
  // Wait for content to load
  await expect(page.getByRole('main')).toBeVisible()
  
  // Visual comparison
  await expect(page).toHaveScreenshot('dashboard.png', {
    maxDiffPixels: 100,
  })
})
```

## API Testing with Playwright

```typescript
test('API returns user data', async ({ request }) => {
  const response = await request.get('/api/v1/users/me', {
    headers: {
      Authorization: `Bearer ${authToken}`,
    },
  })
  
  expect(response.ok()).toBeTruthy()
  
  const user = await response.json()
  expect(user).toMatchObject({
    email: expect.any(String),
    name: expect.any(String),
  })
})
```

## Guidelines

1. **Use page object model** for reusable code
2. **Test user journeys** not implementation details
3. **Use role selectors** (getByRole) for accessibility
4. **Handle async** properly with expect assertions
5. **Isolate tests** - each test should be independent

