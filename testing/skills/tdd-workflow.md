---
description: Test-Driven Development workflow and patterns
globs: ["**/*.test.ts", "**/*.test.tsx", "**/*.spec.ts"]
---

# TDD Workflow Skill

> Write tests first, then implementation. Every feature is proven by tests.

## TDD Cycle

```
┌─────────────────────────────────────────────────────────────┐
│                    THE TDD CYCLE                             │
│                                                              │
│         ┌──────────────────────────────────────────┐        │
│         │                                          │        │
│         ▼                                          │        │
│    ┌─────────┐    Write failing    ┌─────────┐    │        │
│    │  🔴 RED │ ─────────────────▶ │ 🟢 GREEN│    │        │
│    │  Test   │                     │   Code  │    │        │
│    └─────────┘                     └────┬────┘    │        │
│         ▲                               │         │        │
│         │         ┌─────────┐           │         │        │
│         └─────────│🔵REFACTOR│◀──────────┘         │        │
│                   │  Clean  │                      │        │
│                   └─────────┘                      │        │
│                        │                           │        │
│                        └───────────────────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

## Test Structure

### AAA Pattern (Arrange, Act, Assert)

```typescript
describe('UserService', () => {
  describe('createUser', () => {
    it('should create a new user with hashed password', async () => {
      // ====== ARRANGE ======
      // Set up test data and mocks
      const userData = {
        email: 'test@example.com',
        password: 'SecurePass123!',
        name: 'Test User',
      };
      
      const mockHashedPassword = 'hashed_password_123';
      vi.spyOn(passwordService, 'hash').mockResolvedValue(mockHashedPassword);
      
      // ====== ACT ======
      // Execute the function under test
      const result = await userService.createUser(userData);
      
      // ====== ASSERT ======
      // Verify the expected outcome
      expect(result.user).toMatchObject({
        email: userData.email,
        name: userData.name,
      });
      expect(result.user.passwordHash).toBe(mockHashedPassword);
      expect(result.user.id).toBeDefined();
      expect(passwordService.hash).toHaveBeenCalledWith(userData.password);
    });
  });
});
```

### BDD Style (Given, When, Then)

```typescript
describe('Feature: User Authentication', () => {
  describe('Scenario: Successful login', () => {
    it('Given a registered user, When they login with correct credentials, Then they receive a valid session', async () => {
      // GIVEN
      const user = await createTestUser({
        email: 'user@example.com',
        password: 'ValidPass123!',
      });

      // WHEN
      const result = await authService.login({
        email: 'user@example.com',
        password: 'ValidPass123!',
      });

      // THEN
      expect(result.success).toBe(true);
      expect(result.session.userId).toBe(user.id);
      expect(result.session.token).toMatch(/^[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+$/);
      expect(result.session.expiresAt).toBeInstanceOf(Date);
    });
  });

  describe('Scenario: Failed login', () => {
    it('Given a registered user, When they login with wrong password, Then they receive an error', async () => {
      // GIVEN
      await createTestUser({
        email: 'user@example.com',
        password: 'CorrectPass123!',
      });

      // WHEN & THEN
      await expect(
        authService.login({
          email: 'user@example.com',
          password: 'WrongPassword!',
        })
      ).rejects.toThrow(AuthenticationError);
    });
  });
});
```

## Test Types

### Unit Tests

```typescript
// Testing a pure function
describe('calculateDiscount', () => {
  it('should apply 10% discount for orders over $100', () => {
    expect(calculateDiscount(150)).toBe(15);
  });

  it('should apply 20% discount for orders over $500', () => {
    expect(calculateDiscount(600)).toBe(120);
  });

  it('should not apply discount for orders under $100', () => {
    expect(calculateDiscount(50)).toBe(0);
  });

  it('should handle edge case of exactly $100', () => {
    expect(calculateDiscount(100)).toBe(10);
  });
});
```

### Integration Tests

```typescript
describe('OrderService Integration', () => {
  let db: Database;
  let orderService: OrderService;

  beforeAll(async () => {
    db = await setupTestDatabase();
    orderService = new OrderService(db);
  });

  afterAll(async () => {
    await db.close();
  });

  beforeEach(async () => {
    await db.clear();
  });

  it('should create order and update inventory', async () => {
    // Arrange
    const product = await db.product.create({
      data: { name: 'Widget', stock: 10, price: 25 },
    });
    const user = await db.user.create({
      data: { email: 'buyer@example.com' },
    });

    // Act
    const order = await orderService.createOrder({
      userId: user.id,
      items: [{ productId: product.id, quantity: 3 }],
    });

    // Assert
    expect(order.total).toBe(75);
    expect(order.status).toBe('pending');

    const updatedProduct = await db.product.findUnique({
      where: { id: product.id },
    });
    expect(updatedProduct?.stock).toBe(7);
  });
});
```

### E2E Tests

```typescript
import { test, expect } from '@playwright/test';

test.describe('User Registration Flow', () => {
  test('should allow new user to register and login', async ({ page }) => {
    // Navigate to registration
    await page.goto('/register');
    
    // Fill registration form
    await page.fill('[data-testid="email-input"]', 'newuser@example.com');
    await page.fill('[data-testid="password-input"]', 'SecurePass123!');
    await page.fill('[data-testid="confirm-password-input"]', 'SecurePass123!');
    await page.fill('[data-testid="name-input"]', 'New User');
    
    // Submit form
    await page.click('[data-testid="register-button"]');
    
    // Verify redirect to dashboard
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('[data-testid="welcome-message"]'))
      .toContainText('Welcome, New User');
    
    // Verify user can logout and login again
    await page.click('[data-testid="logout-button"]');
    await expect(page).toHaveURL('/login');
    
    await page.fill('[data-testid="email-input"]', 'newuser@example.com');
    await page.fill('[data-testid="password-input"]', 'SecurePass123!');
    await page.click('[data-testid="login-button"]');
    
    await expect(page).toHaveURL('/dashboard');
  });
});
```

## Test Coverage

### Coverage Requirements

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      thresholds: {
        global: {
          statements: 80,
          branches: 80,
          functions: 80,
          lines: 80,
        },
      },
      include: ['src/**/*.{ts,tsx}'],
      exclude: [
        'src/**/*.test.{ts,tsx}',
        'src/**/*.d.ts',
        'src/types/**',
      ],
    },
  },
});
```

### What to Test

| Priority | Test Type | What to Test |
|----------|-----------|--------------|
| **P0** | Unit | Core business logic |
| **P0** | Unit | Validation functions |
| **P0** | Unit | Security-related code |
| **P1** | Integration | API endpoints |
| **P1** | Integration | Database operations |
| **P1** | Integration | External service calls |
| **P2** | E2E | Critical user flows |
| **P2** | E2E | Authentication flows |
| **P3** | Visual | UI component snapshots |
| **P3** | Performance | Load testing |

## Test Utilities

### Test Factories

```typescript
// factories/user.factory.ts
import { faker } from '@faker-js/faker';

export function createUserData(overrides: Partial<UserInput> = {}): UserInput {
  return {
    email: faker.internet.email(),
    password: faker.internet.password({ length: 12 }),
    name: faker.person.fullName(),
    ...overrides,
  };
}

export async function createTestUser(
  overrides: Partial<UserInput> = {},
  db: Database = getTestDb()
): Promise<User> {
  const userData = createUserData(overrides);
  return db.user.create({ data: userData });
}
```

### Custom Matchers

```typescript
// test/matchers.ts
expect.extend({
  toBeValidJWT(received: string) {
    const jwtPattern = /^[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+$/;
    const pass = jwtPattern.test(received);
    
    return {
      message: () =>
        `expected ${received} ${pass ? 'not ' : ''}to be a valid JWT`,
      pass,
    };
  },

  toHaveStatus(received: Response, expected: number) {
    const pass = received.status === expected;
    return {
      message: () =>
        `expected response to have status ${expected} but got ${received.status}`,
      pass,
    };
  },
});

// Usage
expect(token).toBeValidJWT();
expect(response).toHaveStatus(201);
```

### Test Helpers

```typescript
// test/helpers.ts
export function mockCurrentDate(date: Date) {
  const originalNow = Date.now;
  beforeAll(() => {
    vi.setSystemTime(date);
  });
  afterAll(() => {
    vi.setSystemTime(originalNow());
  });
}

export async function expectToReject<T extends Error>(
  promise: Promise<unknown>,
  errorType: new (...args: any[]) => T,
  message?: string
): Promise<T> {
  try {
    await promise;
    throw new Error('Expected promise to reject');
  } catch (error) {
    expect(error).toBeInstanceOf(errorType);
    if (message) {
      expect((error as Error).message).toContain(message);
    }
    return error as T;
  }
}
```

## Anti-Patterns to Avoid

### ❌ Testing Implementation Details

```typescript
// ❌ BAD: Tests internal state
it('should set isLoading to true', () => {
  userService.fetchUser('123');
  expect(userService._isLoading).toBe(true); // Don't test private state
});

// ✅ GOOD: Tests behavior
it('should show loading indicator while fetching', async () => {
  const { getByRole, queryByRole } = render(<UserProfile userId="123" />);
  
  expect(getByRole('progressbar')).toBeInTheDocument();
  
  await waitFor(() => {
    expect(queryByRole('progressbar')).not.toBeInTheDocument();
  });
});
```

### ❌ Flaky Tests

```typescript
// ❌ BAD: Race condition
it('should update after delay', async () => {
  component.startUpdate();
  await new Promise(r => setTimeout(r, 100)); // Arbitrary wait
  expect(component.value).toBe('updated');
});

// ✅ GOOD: Explicit waiting
it('should update after delay', async () => {
  component.startUpdate();
  await waitFor(() => {
    expect(component.value).toBe('updated');
  });
});
```

### ❌ Testing Mocks Instead of Code

```typescript
// ❌ BAD: Just testing the mock
it('should call the service', async () => {
  const mockService = vi.fn().mockResolvedValue({ data: 'test' });
  await mockService();
  expect(mockService).toHaveBeenCalled();
});

// ✅ GOOD: Testing actual behavior
it('should return user data from service', async () => {
  vi.spyOn(userApi, 'getUser').mockResolvedValue({ id: '1', name: 'Test' });
  
  const result = await userService.getUserProfile('1');
  
  expect(result.name).toBe('Test');
  expect(userApi.getUser).toHaveBeenCalledWith('1');
});
```

## Checklist

- [ ] Tests written BEFORE implementation
- [ ] Tests are independent (no shared state)
- [ ] Tests are deterministic (no flakiness)
- [ ] Test names describe behavior
- [ ] AAA/GWT pattern followed
- [ ] Edge cases covered
- [ ] Error cases tested
- [ ] Mocks used sparingly
- [ ] Test data factories used
- [ ] Coverage ≥ 80%

