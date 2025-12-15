---
description: SOLID principles, clean architecture, and manageable code - Priority #1
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
alwaysApply: true
---

# SOLID Principles & Clean Code - Priority #1

> **This skill is ALWAYS applied.** Every piece of code must be small, reusable, properly structured, and follow SOLID principles.

## The Golden Rules

```
┌─────────────────────────────────────────────────────────────────┐
│                    CODE QUALITY PYRAMID                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                     ▲ ELEGANT                                   │
│                    ╱ ╲ Beautiful, idiomatic                     │
│                   ╱───╲                                         │
│                  ╱TESTABLE╲ Easy to test in isolation           │
│                 ╱──────────╲                                    │
│                ╱ REUSABLE   ╲ Components used across codebase   │
│               ╱──────────────╲                                  │
│              ╱   MANAGEABLE   ╲ Small files, small functions    │
│             ╱──────────────────╲                                │
│            ╱      S.O.L.I.D.     ╲ Principles always followed   │
│           ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔                              │
│                  FOUNDATION                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## S - Single Responsibility Principle

> **A module should have one, and only one, reason to change.**

### ❌ Violation: God Class

```typescript
// ❌ BAD: UserService does EVERYTHING
class UserService {
  async createUser(data: UserData) { /* 50 lines */ }
  async validateEmail(email: string) { /* 20 lines */ }
  async hashPassword(password: string) { /* 15 lines */ }
  async sendWelcomeEmail(user: User) { /* 30 lines */ }
  async generateAvatar(user: User) { /* 25 lines */ }
  async logActivity(user: User, action: string) { /* 20 lines */ }
  async updateProfile(id: string, data: Partial<User>) { /* 40 lines */ }
  async deleteUser(id: string) { /* 30 lines */ }
  async exportUserData(id: string) { /* 50 lines */ }
  // ... 500+ lines total
}
```

### ✅ Correct: Focused Services

```typescript
// ✅ GOOD: Each service has ONE responsibility

// User CRUD operations only
class UserRepository {
  async create(data: CreateUserDto): Promise<User> { /* 20 lines */ }
  async findById(id: string): Promise<User | null> { /* 10 lines */ }
  async update(id: string, data: UpdateUserDto): Promise<User> { /* 15 lines */ }
  async delete(id: string): Promise<void> { /* 10 lines */ }
}

// Validation only
class UserValidationService {
  validateEmail(email: string): ValidationResult { /* 15 lines */ }
  validatePassword(password: string): ValidationResult { /* 15 lines */ }
  validateProfile(data: ProfileData): ValidationResult { /* 20 lines */ }
}

// Password operations only
class PasswordService {
  async hash(password: string): Promise<string> { /* 10 lines */ }
  async verify(password: string, hash: string): Promise<boolean> { /* 10 lines */ }
}

// Email operations only
class EmailService {
  async sendWelcome(user: User): Promise<void> { /* 20 lines */ }
  async sendPasswordReset(user: User, token: string): Promise<void> { /* 20 lines */ }
}

// Orchestrates user creation
class UserRegistrationUseCase {
  constructor(
    private readonly userRepo: UserRepository,
    private readonly validation: UserValidationService,
    private readonly password: PasswordService,
    private readonly email: EmailService,
  ) {}

  async execute(data: RegisterUserDto): Promise<Result<User>> {
    // Orchestration logic - 30 lines max
  }
}
```

### Size Limits

| Element | Max Lines | Action if Exceeded |
|---------|-----------|-------------------|
| Function | 30 | Extract helper functions |
| Class | 200 | Split into focused classes |
| File | 300 | Split into modules |

---

## O - Open/Closed Principle

> **Open for extension, closed for modification.**

### ❌ Violation: Switch/If Chains

```typescript
// ❌ BAD: Must modify this function for every new payment type
function processPayment(type: string, amount: number) {
  if (type === 'credit') {
    // Credit card logic
  } else if (type === 'debit') {
    // Debit card logic
  } else if (type === 'paypal') {
    // PayPal logic
  } else if (type === 'crypto') {
    // Crypto logic - had to MODIFY existing code!
  }
  // Every new type = modification
}
```

### ✅ Correct: Strategy Pattern

```typescript
// ✅ GOOD: Extend without modifying

// Abstract interface
interface PaymentProcessor {
  readonly type: string;
  process(amount: number): Promise<PaymentResult>;
  validate(data: PaymentData): ValidationResult;
}

// Concrete implementations - can add new ones without changing existing
class CreditCardProcessor implements PaymentProcessor {
  readonly type = 'credit';
  async process(amount: number) { /* implementation */ }
  validate(data: PaymentData) { /* implementation */ }
}

class PayPalProcessor implements PaymentProcessor {
  readonly type = 'paypal';
  async process(amount: number) { /* implementation */ }
  validate(data: PaymentData) { /* implementation */ }
}

// New payment type = NEW file, no modifications
class CryptoProcessor implements PaymentProcessor {
  readonly type = 'crypto';
  async process(amount: number) { /* implementation */ }
  validate(data: PaymentData) { /* implementation */ }
}

// Registry - also closed for modification
class PaymentProcessorRegistry {
  private processors = new Map<string, PaymentProcessor>();

  register(processor: PaymentProcessor) {
    this.processors.set(processor.type, processor);
  }

  get(type: string): PaymentProcessor | undefined {
    return this.processors.get(type);
  }
}
```

---

## L - Liskov Substitution Principle

> **Subtypes must be substitutable for their base types.**

### ❌ Violation: Broken Hierarchy

```typescript
// ❌ BAD: Square breaks Rectangle contract
class Rectangle {
  constructor(protected width: number, protected height: number) {}

  setWidth(width: number) { this.width = width; }
  setHeight(height: number) { this.height = height; }
  getArea() { return this.width * this.height; }
}

class Square extends Rectangle {
  setWidth(width: number) {
    this.width = width;
    this.height = width; // Breaks expectation!
  }
  setHeight(height: number) {
    this.height = height;
    this.width = height; // Breaks expectation!
  }
}

// Code expecting Rectangle behavior BREAKS
function resize(rect: Rectangle) {
  rect.setWidth(10);
  rect.setHeight(5);
  // Expected: area = 50
  // With Square: area = 25 (broken!)
}
```

### ✅ Correct: Proper Abstraction

```typescript
// ✅ GOOD: Separate abstractions
interface Shape {
  getArea(): number;
}

class Rectangle implements Shape {
  constructor(private width: number, private height: number) {}
  getArea() { return this.width * this.height; }
}

class Square implements Shape {
  constructor(private side: number) {}
  getArea() { return this.side * this.side; }
}

// Both work correctly as Shape
function printArea(shape: Shape) {
  console.log(`Area: ${shape.getArea()}`);
}
```

---

## I - Interface Segregation Principle

> **Clients should not depend on interfaces they don't use.**

### ❌ Violation: Fat Interface

```typescript
// ❌ BAD: Massive interface forces unnecessary implementation
interface UserService {
  createUser(data: UserData): Promise<User>;
  updateUser(id: string, data: Partial<User>): Promise<User>;
  deleteUser(id: string): Promise<void>;
  findUser(id: string): Promise<User>;
  listUsers(filters: Filters): Promise<User[]>;
  sendEmail(userId: string, template: string): Promise<void>;
  resetPassword(userId: string): Promise<void>;
  generateReport(userId: string): Promise<Report>;
  exportData(userId: string): Promise<Buffer>;
  importData(userId: string, data: Buffer): Promise<void>;
}

// Read-only component forced to implement write methods
class UserDisplayWidget implements UserService {
  findUser(id: string) { /* needs this */ }
  listUsers(filters: Filters) { /* needs this */ }
  
  // Forced to implement these even though never used!
  createUser() { throw new Error('Not implemented'); }
  updateUser() { throw new Error('Not implemented'); }
  deleteUser() { throw new Error('Not implemented'); }
  // ... more unused methods
}
```

### ✅ Correct: Focused Interfaces

```typescript
// ✅ GOOD: Small, focused interfaces

interface UserReader {
  findById(id: string): Promise<User | null>;
  findMany(filters: Filters): Promise<User[]>;
}

interface UserWriter {
  create(data: CreateUserDto): Promise<User>;
  update(id: string, data: UpdateUserDto): Promise<User>;
  delete(id: string): Promise<void>;
}

interface UserNotifier {
  sendEmail(userId: string, template: string): Promise<void>;
  sendPush(userId: string, message: string): Promise<void>;
}

interface UserExporter {
  exportData(userId: string): Promise<Buffer>;
  generateReport(userId: string): Promise<Report>;
}

// Components only depend on what they need
class UserDisplayWidget {
  constructor(private readonly reader: UserReader) {} // Only needs reading
}

class UserAdminPanel {
  constructor(
    private readonly reader: UserReader,
    private readonly writer: UserWriter, // Needs read + write
  ) {}
}
```

### Interface Size Limits

| Metric | Maximum | Why |
|--------|---------|-----|
| Methods per interface | 5 | Focused responsibility |
| Parameters per method | 4 | Use options object for more |

---

## D - Dependency Inversion Principle

> **Depend on abstractions, not concretions.**

### ❌ Violation: Concrete Dependencies

```typescript
// ❌ BAD: Directly depends on concrete implementations
class OrderService {
  private db = new PostgresDatabase(); // Concrete!
  private email = new SendGridEmailer(); // Concrete!
  private logger = new WinstonLogger(); // Concrete!

  async createOrder(data: OrderData) {
    await this.db.insert('orders', data);
    await this.email.send(data.userEmail, 'Order Confirmation');
    this.logger.info('Order created');
  }
}

// Can't test without real database, email service, etc.
// Can't swap implementations without changing this class
```

### ✅ Correct: Dependency Injection

```typescript
// ✅ GOOD: Depend on abstractions, inject dependencies

// Abstractions
interface Database {
  insert<T>(table: string, data: T): Promise<void>;
  query<T>(sql: string, params: unknown[]): Promise<T[]>;
}

interface Emailer {
  send(to: string, template: string, data?: object): Promise<void>;
}

interface Logger {
  info(message: string, context?: object): void;
  error(message: string, error?: Error): void;
}

// Service depends on abstractions
class OrderService {
  constructor(
    private readonly db: Database,
    private readonly email: Emailer,
    private readonly logger: Logger,
  ) {}

  async createOrder(data: OrderData): Promise<Result<Order>> {
    try {
      await this.db.insert('orders', data);
      await this.email.send(data.userEmail, 'order-confirmation', data);
      this.logger.info('Order created', { orderId: data.id });
      return ok(data);
    } catch (error) {
      this.logger.error('Failed to create order', error);
      return err('ORDER_CREATION_FAILED');
    }
  }
}

// Easy to test with mocks
const mockDb: Database = { insert: vi.fn(), query: vi.fn() };
const mockEmail: Emailer = { send: vi.fn() };
const mockLogger: Logger = { info: vi.fn(), error: vi.fn() };

const service = new OrderService(mockDb, mockEmail, mockLogger);
```

---

## Reusable Component Patterns

### Extract Common Logic

```typescript
// ❌ BAD: Duplicated logic
function validateUserEmail(email: string) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!regex.test(email)) throw new Error('Invalid email');
}

function validateContactEmail(email: string) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Duplicated!
  if (!regex.test(email)) throw new Error('Invalid email');
}

// ✅ GOOD: Shared utility
// utils/validation.ts
export function isValidEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export function validateEmail(email: string): Result<string> {
  return isValidEmail(email) 
    ? ok(email) 
    : err('Invalid email format');
}

// Used everywhere
import { validateEmail } from '@/utils/validation';
```

### Composable Components

```tsx
// ❌ BAD: Monolithic component
function UserCard({ user }: { user: User }) {
  return (
    <div className="card">
      <img src={user.avatar} className="w-16 h-16 rounded-full" />
      <div className="ml-4">
        <h3 className="font-bold">{user.name}</h3>
        <p className="text-gray-500">{user.email}</p>
        <span className="inline-flex items-center px-2 py-1 rounded-full text-xs bg-green-100 text-green-800">
          {user.role}
        </span>
      </div>
      <button onClick={() => editUser(user.id)}>Edit</button>
      <button onClick={() => deleteUser(user.id)}>Delete</button>
    </div>
  );
}

// ✅ GOOD: Composed from reusable parts
// components/Avatar.tsx (reusable)
function Avatar({ src, size = 'md' }: AvatarProps) {
  const sizes = { sm: 'w-8 h-8', md: 'w-12 h-12', lg: 'w-16 h-16' };
  return <img src={src} className={`${sizes[size]} rounded-full`} />;
}

// components/Badge.tsx (reusable)
function Badge({ children, variant = 'default' }: BadgeProps) {
  const variants = {
    default: 'bg-gray-100 text-gray-800',
    success: 'bg-green-100 text-green-800',
    warning: 'bg-yellow-100 text-yellow-800',
  };
  return (
    <span className={`inline-flex px-2 py-1 rounded-full text-xs ${variants[variant]}`}>
      {children}
    </span>
  );
}

// components/Card.tsx (reusable)
function Card({ children, className }: CardProps) {
  return (
    <div className={cn("bg-white rounded-lg shadow p-4", className)}>
      {children}
    </div>
  );
}

// Composed component
function UserCard({ user, onEdit, onDelete }: UserCardProps) {
  return (
    <Card className="flex items-center gap-4">
      <Avatar src={user.avatar} size="lg" />
      <div className="flex-1">
        <h3 className="font-bold">{user.name}</h3>
        <p className="text-sm text-muted">{user.email}</p>
        <Badge variant="success">{user.role}</Badge>
      </div>
      <ButtonGroup>
        <Button onClick={() => onEdit(user.id)} variant="ghost">Edit</Button>
        <Button onClick={() => onDelete(user.id)} variant="danger">Delete</Button>
      </ButtonGroup>
    </Card>
  );
}
```

---

## File Structure

```
src/
├── components/           # UI components (max 200 lines each)
│   ├── Button/
│   │   ├── Button.tsx      # Main component
│   │   ├── Button.test.tsx # Tests
│   │   ├── variants.ts     # Button variants
│   │   └── index.ts        # Public exports
│   └── ...
├── hooks/                # Custom hooks (max 50 lines each)
├── services/             # Business logic (one responsibility each)
│   ├── user/
│   │   ├── UserRepository.ts
│   │   ├── UserValidation.ts
│   │   └── index.ts
│   └── ...
├── utils/                # Pure utilities (max 30 lines per function)
├── types/                # Type definitions
└── lib/                  # External integrations
```

---

## Checklist (Apply to Every File)

### Size Checks
- [ ] No function > 30 lines
- [ ] No class > 200 lines
- [ ] No file > 300 lines
- [ ] No function > 4 parameters
- [ ] No nesting > 3 levels

### SOLID Checks
- [ ] **S**: Does this have only ONE reason to change?
- [ ] **O**: Can I extend without modifying?
- [ ] **L**: Are subtypes substitutable?
- [ ] **I**: Are interfaces focused (≤5 methods)?
- [ ] **D**: Am I depending on abstractions?

### Reusability Checks
- [ ] Is there similar code elsewhere? → Extract
- [ ] Can this be used in other contexts? → Generalize
- [ ] Am I copying code? → Create shared utility
- [ ] Is this component doing too much? → Compose

---

*"The best code is small, focused, and boring. Complexity is the enemy."*

