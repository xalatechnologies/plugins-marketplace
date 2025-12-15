---
description: Unit testing expertise with Vitest
triggers:
  - writing unit tests
  - testing functions
  - testing hooks
  - testing components
---

# Unit Testing Skill

Expert Vitest unit testing capabilities.

## Quick Patterns

### Basic Tests

```typescript
import { describe, it, expect, vi } from 'vitest'

describe('myFunction', () => {
  it('returns expected value', () => {
    expect(myFunction('input')).toBe('output')
  })

  it('throws on invalid input', () => {
    expect(() => myFunction(null)).toThrow('Invalid input')
  })
})
```

### Mocking

```typescript
// Mock function
const mockFn = vi.fn()
mockFn.mockReturnValue('result')
mockFn.mockResolvedValue('async result')
mockFn.mockRejectedValue(new Error('failed'))

// Mock module
vi.mock('./api', () => ({
  fetchData: vi.fn().mockResolvedValue({ data: [] })
}))

// Mock implementation
vi.mocked(fetchData).mockImplementation(async (id) => {
  return { id, name: 'Test' }
})

// Spy on existing function
const spy = vi.spyOn(console, 'log')
expect(spy).toHaveBeenCalledWith('message')
```

### Async Testing

```typescript
it('handles async operations', async () => {
  const result = await asyncFunction()
  expect(result).toBe('expected')
})

it('rejects with error', async () => {
  await expect(failingAsync()).rejects.toThrow('Error')
})
```

### Timer Mocking

```typescript
it('debounces calls', async () => {
  vi.useFakeTimers()
  
  const fn = vi.fn()
  const debounced = debounce(fn, 100)
  
  debounced()
  debounced()
  debounced()
  
  expect(fn).not.toHaveBeenCalled()
  
  await vi.advanceTimersByTime(100)
  
  expect(fn).toHaveBeenCalledTimes(1)
  
  vi.useRealTimers()
})
```

### React Component Testing

```typescript
import { render, screen, fireEvent } from '@testing-library/react'

it('renders correctly', () => {
  render(<Button>Click me</Button>)
  expect(screen.getByRole('button', { name: 'Click me' })).toBeInTheDocument()
})

it('calls onClick when clicked', () => {
  const handleClick = vi.fn()
  render(<Button onClick={handleClick}>Click</Button>)
  
  fireEvent.click(screen.getByRole('button'))
  
  expect(handleClick).toHaveBeenCalledTimes(1)
})
```

### React Hook Testing

```typescript
import { renderHook, act } from '@testing-library/react'

it('updates state', () => {
  const { result } = renderHook(() => useCounter())
  
  expect(result.current.count).toBe(0)
  
  act(() => {
    result.current.increment()
  })
  
  expect(result.current.count).toBe(1)
})
```

### Snapshot Testing

```typescript
it('matches snapshot', () => {
  const { container } = render(<Component />)
  expect(container).toMatchSnapshot()
})

// Inline snapshot
it('matches inline snapshot', () => {
  expect(formatDate(new Date('2024-01-01'))).toMatchInlineSnapshot(`"Jan 1, 2024"`)
})
```

## Test Patterns

### Arrange-Act-Assert

```typescript
it('calculates total correctly', () => {
  // Arrange
  const items = [
    { price: 10, quantity: 2 },
    { price: 5, quantity: 3 },
  ]
  
  // Act
  const total = calculateTotal(items)
  
  // Assert
  expect(total).toBe(35)
})
```

### Table-Driven Tests

```typescript
it.each([
  ['hello', 'HELLO'],
  ['world', 'WORLD'],
  ['', ''],
])('toUpperCase(%s) returns %s', (input, expected) => {
  expect(toUpperCase(input)).toBe(expected)
})
```

### Setup/Teardown

```typescript
describe('Database tests', () => {
  beforeAll(async () => {
    await db.connect()
  })

  afterAll(async () => {
    await db.disconnect()
  })

  beforeEach(async () => {
    await db.clear()
  })

  it('inserts record', async () => {
    await db.insert({ name: 'Test' })
    expect(await db.count()).toBe(1)
  })
})
```

## When to Use

Apply when:
- Testing pure functions
- Testing React components
- Testing custom hooks
- Mocking dependencies

