---
description: Create a React context with provider and hook
arguments:
  - name: name
    description: Context name (e.g., Auth, Theme)
    required: true
---

# Create Context Command

Generate a React context with provider, hook, and proper typing.

## Context Template

```typescript
// src/contexts/AuthContext.tsx
import {
  createContext,
  useContext,
  useState,
  useCallback,
  useMemo,
  type ReactNode,
} from 'react'

// Types
interface User {
  id: string
  email: string
  name: string
  role: string
}

interface AuthContextValue {
  user: User | null
  isAuthenticated: boolean
  isLoading: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => Promise<void>
  refresh: () => Promise<void>
}

// Context
const AuthContext = createContext<AuthContextValue | undefined>(undefined)

// Provider props
interface AuthProviderProps {
  children: ReactNode
}

// Provider component
export function AuthProvider({ children }: AuthProviderProps) {
  const [user, setUser] = useState<User | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  const isAuthenticated = useMemo(() => user !== null, [user])

  const login = useCallback(async (email: string, password: string) => {
    setIsLoading(true)
    try {
      // Implement login logic
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        body: JSON.stringify({ email, password }),
      })
      const data = await response.json()
      setUser(data.user)
    } finally {
      setIsLoading(false)
    }
  }, [])

  const logout = useCallback(async () => {
    setIsLoading(true)
    try {
      await fetch('/api/auth/logout', { method: 'POST' })
      setUser(null)
    } finally {
      setIsLoading(false)
    }
  }, [])

  const refresh = useCallback(async () => {
    setIsLoading(true)
    try {
      const response = await fetch('/api/auth/me')
      if (response.ok) {
        const data = await response.json()
        setUser(data.user)
      } else {
        setUser(null)
      }
    } catch {
      setUser(null)
    } finally {
      setIsLoading(false)
    }
  }, [])

  // Memoize value to prevent unnecessary re-renders
  const value = useMemo<AuthContextValue>(
    () => ({
      user,
      isAuthenticated,
      isLoading,
      login,
      logout,
      refresh,
    }),
    [user, isAuthenticated, isLoading, login, logout, refresh]
  )

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

// Hook with error if used outside provider
export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext)
  
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  
  return context
}

// Optional: Hook that doesn't throw (for conditional usage)
export function useAuthOptional(): AuthContextValue | undefined {
  return useContext(AuthContext)
}
```

## With Reducer Pattern (for complex state)

```typescript
// src/contexts/CartContext.tsx
import {
  createContext,
  useContext,
  useReducer,
  useMemo,
  type ReactNode,
  type Dispatch,
} from 'react'

// Types
interface CartItem {
  id: string
  name: string
  price: number
  quantity: number
}

interface CartState {
  items: CartItem[]
  total: number
}

type CartAction =
  | { type: 'ADD_ITEM'; payload: CartItem }
  | { type: 'REMOVE_ITEM'; payload: string }
  | { type: 'UPDATE_QUANTITY'; payload: { id: string; quantity: number } }
  | { type: 'CLEAR' }

interface CartContextValue {
  state: CartState
  dispatch: Dispatch<CartAction>
  addItem: (item: Omit<CartItem, 'quantity'>) => void
  removeItem: (id: string) => void
  updateQuantity: (id: string, quantity: number) => void
  clear: () => void
}

// Reducer
function cartReducer(state: CartState, action: CartAction): CartState {
  switch (action.type) {
    case 'ADD_ITEM': {
      const existing = state.items.find(item => item.id === action.payload.id)
      if (existing) {
        return {
          ...state,
          items: state.items.map(item =>
            item.id === action.payload.id
              ? { ...item, quantity: item.quantity + 1 }
              : item
          ),
          total: state.total + action.payload.price,
        }
      }
      return {
        ...state,
        items: [...state.items, { ...action.payload, quantity: 1 }],
        total: state.total + action.payload.price,
      }
    }
    case 'REMOVE_ITEM': {
      const item = state.items.find(i => i.id === action.payload)
      return {
        ...state,
        items: state.items.filter(i => i.id !== action.payload),
        total: state.total - (item ? item.price * item.quantity : 0),
      }
    }
    case 'UPDATE_QUANTITY': {
      const item = state.items.find(i => i.id === action.payload.id)
      if (!item) return state
      const diff = action.payload.quantity - item.quantity
      return {
        ...state,
        items: state.items.map(i =>
          i.id === action.payload.id
            ? { ...i, quantity: action.payload.quantity }
            : i
        ),
        total: state.total + item.price * diff,
      }
    }
    case 'CLEAR':
      return { items: [], total: 0 }
    default:
      return state
  }
}

// Context
const CartContext = createContext<CartContextValue | undefined>(undefined)

// Provider
export function CartProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(cartReducer, { items: [], total: 0 })

  const value = useMemo<CartContextValue>(
    () => ({
      state,
      dispatch,
      addItem: (item) => dispatch({ type: 'ADD_ITEM', payload: { ...item, quantity: 1 } }),
      removeItem: (id) => dispatch({ type: 'REMOVE_ITEM', payload: id }),
      updateQuantity: (id, quantity) => dispatch({ type: 'UPDATE_QUANTITY', payload: { id, quantity } }),
      clear: () => dispatch({ type: 'CLEAR' }),
    }),
    [state]
  )

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>
}

// Hook
export function useCart(): CartContextValue {
  const context = useContext(CartContext)
  if (context === undefined) {
    throw new Error('useCart must be used within a CartProvider')
  }
  return context
}
```

## Guidelines

1. **Always memoize context value** to prevent re-renders
2. **Throw in hook** if used outside provider
3. **Use reducer** for complex state logic
4. **Type actions** with discriminated unions
5. **Export provider and hook** from same file

