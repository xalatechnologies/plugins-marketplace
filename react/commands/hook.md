---
description: Create a custom React hook with proper typing and testing
arguments:
  - name: name
    description: Hook name (must start with 'use')
    required: true
  - name: type
    description: Hook type (state, async, subscription, form)
    required: false
    default: state
---

# Create Hook Command

Generate a custom React hook with proper structure and types.

## Hook Types

### State Hook (`type=state`)
```typescript
// src/hooks/useCounter.ts
import { useState, useCallback } from 'react'

interface UseCounterOptions {
  initialValue?: number
  min?: number
  max?: number
  step?: number
}

interface UseCounterReturn {
  count: number
  increment: () => void
  decrement: () => void
  reset: () => void
  set: (value: number) => void
}

export function useCounter(options: UseCounterOptions = {}): UseCounterReturn {
  const { initialValue = 0, min = -Infinity, max = Infinity, step = 1 } = options
  
  const [count, setCount] = useState(initialValue)
  
  const increment = useCallback(() => {
    setCount(prev => Math.min(prev + step, max))
  }, [step, max])
  
  const decrement = useCallback(() => {
    setCount(prev => Math.max(prev - step, min))
  }, [step, min])
  
  const reset = useCallback(() => {
    setCount(initialValue)
  }, [initialValue])
  
  const set = useCallback((value: number) => {
    setCount(Math.min(Math.max(value, min), max))
  }, [min, max])
  
  return { count, increment, decrement, reset, set }
}
```

### Async Hook (`type=async`)
```typescript
// src/hooks/useAsync.ts
import { useState, useCallback, useEffect } from 'react'

interface AsyncState<T> {
  data: T | null
  loading: boolean
  error: Error | null
}

interface UseAsyncReturn<T> extends AsyncState<T> {
  execute: () => Promise<void>
  reset: () => void
}

export function useAsync<T>(
  asyncFunction: () => Promise<T>,
  immediate = true
): UseAsyncReturn<T> {
  const [state, setState] = useState<AsyncState<T>>({
    data: null,
    loading: immediate,
    error: null,
  })

  const execute = useCallback(async () => {
    setState(prev => ({ ...prev, loading: true, error: null }))
    try {
      const data = await asyncFunction()
      setState({ data, loading: false, error: null })
    } catch (error) {
      setState({ data: null, loading: false, error: error as Error })
    }
  }, [asyncFunction])

  const reset = useCallback(() => {
    setState({ data: null, loading: false, error: null })
  }, [])

  useEffect(() => {
    if (immediate) {
      execute()
    }
  }, [execute, immediate])

  return { ...state, execute, reset }
}
```

### Subscription Hook (`type=subscription`)
```typescript
// src/hooks/useEventListener.ts
import { useEffect, useRef } from 'react'

type EventHandler<K extends keyof WindowEventMap> = (event: WindowEventMap[K]) => void

export function useEventListener<K extends keyof WindowEventMap>(
  eventName: K,
  handler: EventHandler<K>,
  element: Window | HTMLElement = window,
  options?: AddEventListenerOptions
): void {
  const savedHandler = useRef(handler)

  useEffect(() => {
    savedHandler.current = handler
  }, [handler])

  useEffect(() => {
    const listener = (event: Event) => {
      savedHandler.current(event as WindowEventMap[K])
    }

    element.addEventListener(eventName, listener, options)

    return () => {
      element.removeEventListener(eventName, listener, options)
    }
  }, [eventName, element, options])
}
```

### Form Hook (`type=form`)
```typescript
// src/hooks/useForm.ts
import { useState, useCallback, ChangeEvent, FormEvent } from 'react'
import { z } from 'zod'

interface UseFormOptions<T> {
  initialValues: T
  schema?: z.ZodSchema<T>
  onSubmit: (values: T) => void | Promise<void>
}

interface UseFormReturn<T> {
  values: T
  errors: Partial<Record<keyof T, string>>
  touched: Partial<Record<keyof T, boolean>>
  isSubmitting: boolean
  handleChange: (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void
  handleBlur: (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void
  handleSubmit: (e: FormEvent) => void
  setFieldValue: (name: keyof T, value: T[keyof T]) => void
  reset: () => void
}

export function useForm<T extends Record<string, any>>(
  options: UseFormOptions<T>
): UseFormReturn<T> {
  const { initialValues, schema, onSubmit } = options
  
  const [values, setValues] = useState<T>(initialValues)
  const [errors, setErrors] = useState<Partial<Record<keyof T, string>>>({})
  const [touched, setTouched] = useState<Partial<Record<keyof T, boolean>>>({})
  const [isSubmitting, setIsSubmitting] = useState(false)

  const validate = useCallback((values: T) => {
    if (!schema) return {}
    try {
      schema.parse(values)
      return {}
    } catch (e) {
      if (e instanceof z.ZodError) {
        return e.errors.reduce((acc, err) => {
          acc[err.path[0] as keyof T] = err.message
          return acc
        }, {} as Partial<Record<keyof T, string>>)
      }
      return {}
    }
  }, [schema])

  const handleChange = useCallback((e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setValues(prev => ({ ...prev, [name]: value }))
  }, [])

  const handleBlur = useCallback((e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name } = e.target
    setTouched(prev => ({ ...prev, [name]: true }))
    setErrors(validate(values))
  }, [values, validate])

  const handleSubmit = useCallback(async (e: FormEvent) => {
    e.preventDefault()
    const validationErrors = validate(values)
    setErrors(validationErrors)
    
    if (Object.keys(validationErrors).length === 0) {
      setIsSubmitting(true)
      try {
        await onSubmit(values)
      } finally {
        setIsSubmitting(false)
      }
    }
  }, [values, validate, onSubmit])

  const setFieldValue = useCallback((name: keyof T, value: T[keyof T]) => {
    setValues(prev => ({ ...prev, [name]: value }))
  }, [])

  const reset = useCallback(() => {
    setValues(initialValues)
    setErrors({})
    setTouched({})
  }, [initialValues])

  return {
    values,
    errors,
    touched,
    isSubmitting,
    handleChange,
    handleBlur,
    handleSubmit,
    setFieldValue,
    reset,
  }
}
```

## Guidelines

1. **Always type returns** with explicit interfaces
2. **Use useCallback** for stable function references
3. **Cleanup subscriptions** in useEffect return
4. **Document with JSDoc** and examples
5. **Include tests** for complex hooks

