---
description: Review code for quality, patterns, and best practices
arguments:
  - name: target
    description: File, directory, or PR to review
    required: false
  - name: focus
    description: Focus area (quality, performance, security, all)
    required: false
    default: all
---

# Code Review Command

Perform thorough code review with actionable feedback.

## Review Categories

### 1. Code Quality

```typescript
// ❌ Bad: Magic numbers
if (user.loginAttempts > 5) { }

// ✅ Good: Named constants
const MAX_LOGIN_ATTEMPTS = 5
if (user.loginAttempts > MAX_LOGIN_ATTEMPTS) { }


// ❌ Bad: Deep nesting
if (user) {
  if (user.isActive) {
    if (user.hasPermission) {
      doSomething()
    }
  }
}

// ✅ Good: Early returns (guard clauses)
if (!user) return
if (!user.isActive) return
if (!user.hasPermission) return
doSomething()


// ❌ Bad: God function
function processOrder(order: Order) {
  // 200 lines of code doing everything
}

// ✅ Good: Single responsibility
function processOrder(order: Order) {
  validateOrder(order)
  calculateTotals(order)
  applyDiscounts(order)
  processPayment(order)
  sendConfirmation(order)
}
```

### 2. Naming Conventions

```typescript
// ❌ Bad: Unclear names
const d = new Date()
const u = getUser()
const x = items.filter(i => i.a > 0)

// ✅ Good: Descriptive names
const createdAt = new Date()
const currentUser = getUser()
const activeItems = items.filter(item => item.isActive)


// ❌ Bad: Inconsistent casing
const UserData = { firstName: 'John' }
const get_user_name = () => {}

// ✅ Good: Consistent conventions
const userData = { firstName: 'John' }  // camelCase for variables
const getUserName = () => {}             // camelCase for functions
interface UserData { }                   // PascalCase for types
const MAX_RETRIES = 3                    // UPPER_SNAKE for constants
```

### 3. Error Handling

```typescript
// ❌ Bad: Swallowing errors
try {
  await saveUser(user)
} catch (e) {
  // silently ignore
}

// ✅ Good: Proper error handling
try {
  await saveUser(user)
} catch (error) {
  logger.error('Failed to save user', { userId: user.id, error })
  throw new UserSaveError('Could not save user', { cause: error })
}


// ❌ Bad: Generic error
throw new Error('Something went wrong')

// ✅ Good: Specific, actionable error
throw new ValidationError('Email is required', {
  field: 'email',
  code: 'REQUIRED',
})
```

### 4. TypeScript Practices

```typescript
// ❌ Bad: Using any
function processData(data: any): any {
  return data.map((item: any) => item.value)
}

// ✅ Good: Proper typing
function processData<T extends { value: number }>(data: T[]): number[] {
  return data.map(item => item.value)
}


// ❌ Bad: Type assertion abuse
const user = response.data as User

// ✅ Good: Type guards or Zod validation
const user = userSchema.parse(response.data)


// ❌ Bad: Optional chaining overuse
const name = user?.profile?.settings?.displayName?.first ?? 'Unknown'

// ✅ Good: Proper null checks or required fields
interface User {
  profile: {
    displayName: string  // Required, not optional
  }
}
```

### 5. React Patterns

```typescript
// ❌ Bad: Prop drilling
<GrandParent user={user}>
  <Parent user={user}>
    <Child user={user}>
      <GrandChild user={user} />
    </Child>
  </Parent>
</GrandParent>

// ✅ Good: Context for global state
const UserContext = createContext<User | null>(null)
<UserProvider value={user}>
  <GrandChild /> {/* Uses useUser() hook */}
</UserProvider>


// ❌ Bad: Inline functions in render
<Button onClick={() => handleClick(id)} />

// ✅ Good: useCallback for stable references
const handleButtonClick = useCallback(() => {
  handleClick(id)
}, [id])
<Button onClick={handleButtonClick} />
```

## Review Output Format

```
📝 CODE REVIEW: src/components/UserProfile.tsx
═══════════════════════════════════════════════════════════════

SUMMARY
───────────────────────────────────────────────────────────────
Lines: 245 (⚠️ Consider splitting - target <200)
Complexity: Medium
Issues: 5 (1 high, 3 medium, 1 low)

🔴 HIGH PRIORITY
───────────────────────────────────────────────────────────────

[L45] Missing error handling in async operation
```typescript
// Current
const user = await fetchUser(id)
setUser(user)

// Suggested
try {
  const user = await fetchUser(id)
  setUser(user)
} catch (error) {
  setError(error)
  toast.error('Failed to load user')
}
```

🟠 MEDIUM PRIORITY
───────────────────────────────────────────────────────────────

[L23] Magic number should be a constant
```typescript
// Current
if (items.length > 10) { }

// Suggested
const MAX_VISIBLE_ITEMS = 10
if (items.length > MAX_VISIBLE_ITEMS) { }
```

[L67-89] Function does too many things
Consider extracting: validateForm, submitData, showNotification

[L120] Unused import
Remove: `import { unused } from '@/lib/utils'`

🟡 SUGGESTIONS
───────────────────────────────────────────────────────────────

[L5] Consider using named export for better tree-shaking
[L150] This component could benefit from React.memo

✅ WHAT'S GOOD
───────────────────────────────────────────────────────────────

• Clean component structure
• Good TypeScript types
• Proper use of hooks
• Accessible form inputs
```

