# Xala PM Development Standards

> The definitive guide to how we build software. These standards train AI agents to produce code that matches our team's quality and patterns.

---

## 🎯 Philosophy

### Core Principles

1. **Spec-First Development** - Never code without a specification
2. **Verification-Driven** - Every feature has acceptance criteria before implementation
3. **Incremental Delivery** - Small, focused changes that can be reviewed and tested
4. **Expert-Level Quality** - Code that a 30-year veteran would be proud of

### The Quality Bar

We build software as if:
- A security auditor will review every line
- A new developer needs to understand it in 5 minutes
- It will run for 10 years without maintenance
- It will handle 100x the expected load

---

## 📐 Architecture Standards

### Layered Architecture

```
┌─────────────────────────────────────────────┐
│                   UI Layer                   │
│  (React components, styling, interactions)  │
├─────────────────────────────────────────────┤
│               Application Layer              │
│  (Use cases, business logic, orchestration) │
├─────────────────────────────────────────────┤
│                 Domain Layer                 │
│  (Entities, value objects, domain services) │
├─────────────────────────────────────────────┤
│             Infrastructure Layer             │
│  (Database, APIs, external services)        │
└─────────────────────────────────────────────┘
```

### Dependency Rules

- UI → Application → Domain ← Infrastructure
- Domain has ZERO external dependencies
- Infrastructure implements interfaces defined in Domain

---

## 🏗️ Code Standards

### TypeScript

```typescript
// ✅ CORRECT: Explicit types, descriptive names, single responsibility
interface CreateUserInput {
  email: string;
  displayName: string;
  role: UserRole;
}

async function createUser(input: CreateUserInput): Promise<Result<User, UserError>> {
  const validated = validateUserInput(input);
  if (validated.isErr()) {
    return err(validated.error);
  }
  
  const user = User.create(validated.value);
  await userRepository.save(user);
  
  return ok(user);
}

// ❌ WRONG: any types, unclear names, mixed concerns
async function doStuff(data: any) {
  // validation mixed with persistence mixed with business logic
}
```

### React Components

```typescript
// ✅ CORRECT: Typed props, accessibility, composition
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'danger';
  size: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
}

export function Button({ 
  variant, 
  size, 
  isLoading, 
  disabled, 
  children, 
  onClick 
}: ButtonProps) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }))}
      disabled={disabled || isLoading}
      onClick={onClick}
      aria-busy={isLoading}
    >
      {isLoading ? <Spinner aria-hidden /> : null}
      {children}
    </button>
  );
}
```

### Error Handling

```typescript
// Use Result types, not exceptions for expected errors
type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

// Define error types explicitly
type UserError = 
  | { type: 'validation'; field: string; message: string }
  | { type: 'duplicate_email'; email: string }
  | { type: 'not_found'; id: string };
```

---

## 🧪 Testing Standards

### Test Pyramid

```
         ╱╲
        ╱  ╲  E2E (5%)
       ╱────╲  Critical user journeys only
      ╱      ╲
     ╱────────╲  Integration (20%)
    ╱          ╲  API contracts, DB queries
   ╱────────────╲
  ╱              ╲  Unit (75%)
 ╱────────────────╲  Pure functions, components
```

### Test Structure

```typescript
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with valid input', async () => {
      // Arrange
      const input = createValidUserInput();
      
      // Act
      const result = await userService.createUser(input);
      
      // Assert
      expect(result.ok).toBe(true);
      expect(result.value.email).toBe(input.email);
    });

    it('should reject duplicate email', async () => {
      // Arrange
      const existingUser = await createTestUser();
      const input = { ...createValidUserInput(), email: existingUser.email };
      
      // Act
      const result = await userService.createUser(input);
      
      // Assert
      expect(result.ok).toBe(false);
      expect(result.error.type).toBe('duplicate_email');
    });
  });
});
```

---

## 📝 Documentation Standards

### Code Comments

```typescript
// ❌ WRONG: Explaining what the code does
// Loop through users and filter active ones
const activeUsers = users.filter(u => u.isActive);

// ✅ CORRECT: Explaining WHY or business context
// Active users are those who logged in within the last 30 days
// per the user retention policy defined in PRD-2024-001
const activeUsers = users.filter(u => u.isActive);
```

### API Documentation

Every API endpoint must have:
1. Description of purpose
2. Request/response schemas with examples
3. Error codes and meanings
4. Rate limits and quotas
5. Authentication requirements

---

## 🔐 Security Standards

### Never Commit

- API keys, tokens, passwords
- Private keys, certificates
- Database connection strings
- Customer data

### Always Validate

- All user input (client AND server)
- File uploads (type, size, content)
- URL parameters and query strings
- Request headers where used

### Security Token Regulations

For security tokens (ERC-3643, etc.):
- ❌ NO DEX/CEX integration
- ❌ NO public trading
- ❌ NO liquidity pools
- ✅ KYC required for all transfers
- ✅ Whitelist required for holders
- ✅ Pause mechanism required
- ✅ Regulatory compliance verified

---

## 📋 Commit Standards

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests
- `docs`: Documentation only
- `chore`: Maintenance tasks

### Examples

```
feat(auth): add OAuth2 login with Google

- Implement OAuth2 flow
- Add user profile sync
- Update session management

Closes #123
```

---

## 🚀 Deployment Standards

### Pre-Deployment Checklist

- [ ] All tests pass
- [ ] No linting errors
- [ ] Security scan clean
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] Migration tested on staging
- [ ] Rollback plan documented

### Environment Parity

Development, staging, and production must be identical except for:
- Data content
- Scale
- Secrets

---

*Last updated: 2024*
*Maintained by: Xala PM Engineering*

