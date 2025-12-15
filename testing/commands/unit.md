---
description: Create or run unit tests with Vitest
arguments:
  - name: action
    description: Action (create, run, coverage)
    required: true
  - name: target
    description: File or function to test
    required: false
---

# Unit Testing Command

Create and run unit tests with Vitest.

## Create Unit Test (`/unit create`)

```bash
/unit create src/lib/utils.ts
/unit create src/hooks/useAuth.ts
```

### Basic Unit Test

```typescript
// src/lib/utils.test.ts
import { describe, it, expect } from 'vitest'
import { formatCurrency, slugify, debounce } from './utils'

describe('formatCurrency', () => {
  it('formats positive numbers correctly', () => {
    expect(formatCurrency(1234.56)).toBe('kr 1 234,56')
  })

  it('formats zero correctly', () => {
    expect(formatCurrency(0)).toBe('kr 0,00')
  })

  it('formats negative numbers correctly', () => {
    expect(formatCurrency(-100)).toBe('-kr 100,00')
  })
})

describe('slugify', () => {
  it('converts spaces to hyphens', () => {
    expect(slugify('hello world')).toBe('hello-world')
  })

  it('converts to lowercase', () => {
    expect(slugify('Hello World')).toBe('hello-world')
  })

  it('removes special characters', () => {
    expect(slugify('Hello! World?')).toBe('hello-world')
  })

  it('handles Norwegian characters', () => {
    expect(slugify('Æøå Test')).toBe('aeoa-test')
  })
})

describe('debounce', () => {
  it('delays function execution', async () => {
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
})
```

### Testing React Hooks

```typescript
// src/hooks/useCounter.test.ts
import { renderHook, act } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import { useCounter } from './useCounter'

describe('useCounter', () => {
  it('initializes with default value', () => {
    const { result } = renderHook(() => useCounter())
    expect(result.current.count).toBe(0)
  })

  it('initializes with provided value', () => {
    const { result } = renderHook(() => useCounter({ initialValue: 10 }))
    expect(result.current.count).toBe(10)
  })

  it('increments count', () => {
    const { result } = renderHook(() => useCounter())
    
    act(() => {
      result.current.increment()
    })
    
    expect(result.current.count).toBe(1)
  })

  it('respects max value', () => {
    const { result } = renderHook(() => useCounter({ initialValue: 9, max: 10 }))
    
    act(() => {
      result.current.increment()
      result.current.increment() // Should not exceed 10
    })
    
    expect(result.current.count).toBe(10)
  })

  it('resets to initial value', () => {
    const { result } = renderHook(() => useCounter({ initialValue: 5 }))
    
    act(() => {
      result.current.increment()
      result.current.reset()
    })
    
    expect(result.current.count).toBe(5)
  })
})
```

### Testing React Components

```typescript
// src/components/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react'
import { describe, it, expect, vi } from 'vitest'
import { Button } from './Button'

describe('Button', () => {
  it('renders with children', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByRole('button', { name: 'Click me' })).toBeInTheDocument()
  })

  it('handles click events', () => {
    const handleClick = vi.fn()
    render(<Button onClick={handleClick}>Click me</Button>)
    
    fireEvent.click(screen.getByRole('button'))
    
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('disables button when loading', () => {
    render(<Button loading>Submit</Button>)
    expect(screen.getByRole('button')).toBeDisabled()
  })

  it('applies variant styles', () => {
    render(<Button variant="primary">Primary</Button>)
    expect(screen.getByRole('button')).toHaveClass('bg-primary')
  })
})
```

### Testing Async Functions

```typescript
// src/services/api.test.ts
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { fetchUsers, createUser } from './api'

// Mock fetch
global.fetch = vi.fn()

describe('API Service', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  describe('fetchUsers', () => {
    it('returns users on success', async () => {
      const mockUsers = [{ id: '1', name: 'John' }]
      
      vi.mocked(fetch).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUsers,
      } as Response)
      
      const users = await fetchUsers()
      
      expect(users).toEqual(mockUsers)
      expect(fetch).toHaveBeenCalledWith('/api/users')
    })

    it('throws on error', async () => {
      vi.mocked(fetch).mockResolvedValueOnce({
        ok: false,
        status: 500,
      } as Response)
      
      await expect(fetchUsers()).rejects.toThrow('Failed to fetch users')
    })
  })
})
```

## Run Unit Tests (`/unit run`)

```bash
/unit run                   # Run all unit tests
/unit run src/lib/utils     # Run specific test
/unit run --watch           # Run in watch mode
/unit coverage              # Run with coverage
```

### Vitest Configuration

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
  plugins: [react(), tsconfigPaths()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./tests/setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/**',
        'tests/**',
        '**/*.d.ts',
        '**/*.config.*',
      ],
      thresholds: {
        statements: 80,
        branches: 80,
        functions: 80,
        lines: 80,
      },
    },
  },
})
```

### Test Setup

```typescript
// tests/setup.ts
import '@testing-library/jest-dom/vitest'
import { cleanup } from '@testing-library/react'
import { afterEach } from 'vitest'

// Cleanup after each test
afterEach(() => {
  cleanup()
})
```

## Guidelines

1. **Test behavior, not implementation**
2. **One assertion per test** (when practical)
3. **Use descriptive test names**
4. **Mock external dependencies**
5. **Aim for 80%+ coverage**

