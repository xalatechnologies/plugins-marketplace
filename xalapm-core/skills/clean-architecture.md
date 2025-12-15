---
description: Clean architecture, proper structure, and modular design patterns
globs: ["**/*.ts", "**/*.tsx"]
alwaysApply: true
---

# Clean Architecture & Project Structure

> **Keep code small, organized, and easy to navigate.**

## Architecture Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                       PRESENTATION                               │
│  Components, Pages, Hooks, Controllers                          │
│  └── Depends on: Application                                    │
├─────────────────────────────────────────────────────────────────┤
│                       APPLICATION                                │
│  Use Cases, Services, DTOs, Mappers                             │
│  └── Depends on: Domain                                         │
├─────────────────────────────────────────────────────────────────┤
│                         DOMAIN                                   │
│  Entities, Value Objects, Interfaces, Business Rules            │
│  └── Depends on: Nothing (pure)                                 │
├─────────────────────────────────────────────────────────────────┤
│                      INFRASTRUCTURE                              │
│  Database, APIs, External Services, Frameworks                  │
│  └── Implements: Domain Interfaces                              │
└─────────────────────────────────────────────────────────────────┘

                    DEPENDENCY RULE:
            Dependencies point INWARD only
```

## Project Structure

### Feature-Based Organization (Recommended)

```
src/
├── features/                    # Feature modules
│   ├── auth/                    # Authentication feature
│   │   ├── components/          # UI components
│   │   │   ├── LoginForm.tsx
│   │   │   ├── SignupForm.tsx
│   │   │   └── index.ts
│   │   ├── hooks/               # Feature-specific hooks
│   │   │   ├── useAuth.ts
│   │   │   └── useSession.ts
│   │   ├── services/            # Business logic
│   │   │   ├── AuthService.ts
│   │   │   └── TokenService.ts
│   │   ├── types/               # Types for this feature
│   │   │   └── auth.types.ts
│   │   ├── utils/               # Feature utilities
│   │   │   └── validation.ts
│   │   └── index.ts             # Public exports only
│   │
│   ├── users/                   # Users feature
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── index.ts
│   │
│   └── orders/                  # Orders feature
│       └── ...
│
├── shared/                      # Shared across features
│   ├── components/              # Reusable UI components
│   │   ├── Button/
│   │   ├── Input/
│   │   ├── Card/
│   │   └── index.ts
│   ├── hooks/                   # Shared hooks
│   │   ├── useDebounce.ts
│   │   ├── useLocalStorage.ts
│   │   └── index.ts
│   ├── utils/                   # Pure utilities
│   │   ├── format.ts
│   │   ├── validation.ts
│   │   └── index.ts
│   └── types/                   # Shared types
│       └── common.types.ts
│
├── lib/                         # External integrations
│   ├── api/                     # API client
│   ├── database/                # Database client
│   └── analytics/               # Analytics
│
└── app/                         # App entry & routing
    ├── routes/
    ├── layout.tsx
    └── providers.tsx
```

### File Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Components | PascalCase | `UserCard.tsx` |
| Hooks | camelCase, `use` prefix | `useAuth.ts` |
| Services | PascalCase, `Service` suffix | `AuthService.ts` |
| Utilities | camelCase | `formatDate.ts` |
| Types | camelCase, `.types.ts` suffix | `user.types.ts` |
| Tests | Same name, `.test.ts` suffix | `UserCard.test.tsx` |
| Constants | UPPER_SNAKE_CASE | `API_ENDPOINTS.ts` |

---

## Module Boundaries

### Public API (index.ts)

Each feature exposes ONLY its public API:

```typescript
// features/auth/index.ts
// ✅ Only export what other features need

// Components
export { LoginForm } from './components/LoginForm';
export { SignupForm } from './components/SignupForm';

// Hooks
export { useAuth } from './hooks/useAuth';
export { useSession } from './hooks/useSession';

// Types (only public ones)
export type { User, Session } from './types/auth.types';

// ❌ Don't export internal implementation details
// export { TokenService } from './services/TokenService'; // Internal!
// export { validatePassword } from './utils/validation';  // Internal!
```

### Import Rules

```typescript
// ✅ GOOD: Import from feature's public API
import { useAuth, LoginForm } from '@/features/auth';
import { Button, Card } from '@/shared/components';

// ❌ BAD: Deep imports into feature internals
import { useAuth } from '@/features/auth/hooks/useAuth';
import { TokenService } from '@/features/auth/services/TokenService';
```

---

## Component Patterns

### Small, Focused Components

```tsx
// ❌ BAD: 300+ line component doing everything
function UserDashboard() {
  // 50 lines of state
  // 100 lines of effects
  // 150 lines of JSX
}

// ✅ GOOD: Composed from small components

// Container (logic) - 30 lines max
function UserDashboardContainer() {
  const { user, stats, isLoading } = useUserDashboard();
  
  if (isLoading) return <DashboardSkeleton />;
  if (!user) return <NotFound />;
  
  return <UserDashboard user={user} stats={stats} />;
}

// Presentational (UI) - 50 lines max
function UserDashboard({ user, stats }: UserDashboardProps) {
  return (
    <div className="space-y-6">
      <UserHeader user={user} />
      <StatsGrid stats={stats} />
      <RecentActivity userId={user.id} />
    </div>
  );
}

// Subcomponents - 30 lines max each
function UserHeader({ user }: { user: User }) { /* ... */ }
function StatsGrid({ stats }: { stats: Stats }) { /* ... */ }
function RecentActivity({ userId }: { userId: string }) { /* ... */ }
```

### Extract Logic to Hooks

```tsx
// ❌ BAD: Component full of logic
function SearchResults() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const debouncedQuery = useDebounce(query, 300);

  useEffect(() => {
    if (!debouncedQuery) {
      setResults([]);
      return;
    }
    
    setIsLoading(true);
    searchAPI(debouncedQuery)
      .then(setResults)
      .catch(setError)
      .finally(() => setIsLoading(false));
  }, [debouncedQuery]);

  // ... more logic
  // ... JSX
}

// ✅ GOOD: Logic extracted to hook
// hooks/useSearch.ts - 25 lines
function useSearch(initialQuery = '') {
  const [query, setQuery] = useState(initialQuery);
  const debouncedQuery = useDebounce(query, 300);
  
  const { data: results, isLoading, error } = useQuery({
    queryKey: ['search', debouncedQuery],
    queryFn: () => searchAPI(debouncedQuery),
    enabled: !!debouncedQuery,
  });

  return { query, setQuery, results, isLoading, error };
}

// Component is now simple - 20 lines
function SearchResults() {
  const { query, setQuery, results, isLoading, error } = useSearch();
  
  return (
    <div>
      <SearchInput value={query} onChange={setQuery} />
      <ResultsList results={results} isLoading={isLoading} error={error} />
    </div>
  );
}
```

---

## Service Patterns

### One Service, One Responsibility

```typescript
// ✅ Each service does ONE thing

// UserRepository - CRUD operations only
class UserRepository {
  async findById(id: string): Promise<User | null> { /* 10 lines */ }
  async findByEmail(email: string): Promise<User | null> { /* 10 lines */ }
  async create(data: CreateUserDto): Promise<User> { /* 15 lines */ }
  async update(id: string, data: UpdateUserDto): Promise<User> { /* 15 lines */ }
  async delete(id: string): Promise<void> { /* 10 lines */ }
}

// PasswordService - Password operations only
class PasswordService {
  async hash(password: string): Promise<string> { /* 10 lines */ }
  async verify(password: string, hash: string): Promise<boolean> { /* 10 lines */ }
  generateResetToken(): string { /* 5 lines */ }
}

// EmailService - Email operations only
class EmailService {
  async send(to: string, template: string, data: object): Promise<void> { /* 20 lines */ }
}

// Use Case - Orchestrates services
class RegisterUserUseCase {
  constructor(
    private readonly users: UserRepository,
    private readonly password: PasswordService,
    private readonly email: EmailService,
  ) {}

  async execute(data: RegisterDto): Promise<Result<User>> {
    // Orchestration - 30 lines max
    const hashedPassword = await this.password.hash(data.password);
    const user = await this.users.create({ ...data, password: hashedPassword });
    await this.email.send(user.email, 'welcome', { name: user.name });
    return ok(user);
  }
}
```

---

## Utility Patterns

### Pure, Single-Purpose Functions

```typescript
// ✅ Each utility does ONE thing, max 30 lines

// utils/format.ts
export function formatCurrency(amount: number, currency = 'USD'): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency,
  }).format(amount);
}

export function formatDate(date: Date, format = 'short'): string {
  const options: Intl.DateTimeFormatOptions = 
    format === 'short' 
      ? { month: 'short', day: 'numeric' }
      : { year: 'numeric', month: 'long', day: 'numeric' };
  return new Intl.DateTimeFormat('en-US', options).format(date);
}

export function formatRelativeTime(date: Date): string {
  const rtf = new Intl.RelativeTimeFormat('en', { numeric: 'auto' });
  const diff = Date.now() - date.getTime();
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  
  if (days === 0) return 'today';
  if (days === 1) return 'yesterday';
  if (days < 7) return rtf.format(-days, 'day');
  if (days < 30) return rtf.format(-Math.floor(days / 7), 'week');
  return rtf.format(-Math.floor(days / 30), 'month');
}
```

### Composable Utilities

```typescript
// utils/validation.ts
// Build complex validation from simple parts

// Primitives - 5 lines each
export const isNotEmpty = (s: string) => s.trim().length > 0;
export const isEmail = (s: string) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s);
export const minLength = (n: number) => (s: string) => s.length >= n;
export const maxLength = (n: number) => (s: string) => s.length <= n;
export const matches = (re: RegExp) => (s: string) => re.test(s);

// Composers - 10 lines each
export const combine = (...validators: Array<(s: string) => boolean>) =>
  (s: string) => validators.every(v => v(s));

export const validateWith = <T>(
  value: T,
  validators: Array<(v: T) => string | null>
): string[] => validators.map(v => v(value)).filter(Boolean) as string[];

// Usage
const isValidPassword = combine(
  minLength(8),
  maxLength(100),
  matches(/[A-Z]/),   // uppercase
  matches(/[a-z]/),   // lowercase
  matches(/[0-9]/),   // number
);
```

---

## When to Split

### File Too Long?

```
> 300 lines → Split into modules

// Before: UserService.ts (500 lines)

// After:
// UserRepository.ts (80 lines)
// UserValidation.ts (60 lines)
// PasswordService.ts (40 lines)
// UserService.ts (100 lines) - orchestrates the above
```

### Function Too Long?

```
> 30 lines → Extract helper functions

// Before: processOrder() - 80 lines

// After:
// validateOrder() - 15 lines
// calculateTotals() - 20 lines
// reserveInventory() - 15 lines
// processPayment() - 15 lines
// processOrder() - 20 lines (calls the above)
```

### Component Too Long?

```
> 200 lines → Split into components

// Before: UserProfile.tsx (400 lines)

// After:
// UserHeader.tsx (50 lines)
// UserStats.tsx (40 lines)
// UserActivity.tsx (60 lines)
// UserSettings.tsx (80 lines)
// UserProfile.tsx (50 lines) - composes the above
```

---

## Checklist

### Structure
- [ ] Feature-based organization
- [ ] Public API via index.ts
- [ ] No deep imports into features
- [ ] Clear layer separation

### Size
- [ ] Functions ≤ 30 lines
- [ ] Classes ≤ 200 lines
- [ ] Files ≤ 300 lines
- [ ] Components ≤ 200 lines

### Modularity
- [ ] One responsibility per module
- [ ] Dependencies injected
- [ ] Pure utilities extracted
- [ ] Logic in hooks (React)

---

*"Good architecture is invisible. Bad architecture is painful."*

