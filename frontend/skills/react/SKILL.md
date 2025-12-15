---
description: React development expertise - patterns, hooks, performance optimization
triggers:
  - creating react components
  - fixing react bugs
  - optimizing react performance
  - working with react hooks
---

# React Development Skill

Expert React development capabilities for components, hooks, and optimization.

## Core Patterns

### Custom Hooks
Create hooks for reusable logic:
```tsx
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value)
  
  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay)
    return () => clearTimeout(timer)
  }, [value, delay])
  
  return debouncedValue
}
```

### Compound Components
For complex UI patterns:
```tsx
const Tabs = ({ children, defaultValue }) => {
  const [value, setValue] = useState(defaultValue)
  return (
    <TabsContext.Provider value={{ value, setValue }}>
      {children}
    </TabsContext.Provider>
  )
}
Tabs.List = TabsList
Tabs.Trigger = TabsTrigger
Tabs.Content = TabsContent
```

### Render Props / Children as Function
For flexible rendering:
```tsx
<DataFetcher url="/api/users">
  {({ data, loading, error }) => (
    loading ? <Spinner /> : <UserList users={data} />
  )}
</DataFetcher>
```

## Performance Patterns

### Memoization
```tsx
// Memoize expensive calculations
const sortedItems = useMemo(() => 
  items.sort((a, b) => a.name.localeCompare(b.name)),
  [items]
)

// Memoize callbacks passed to children
const handleClick = useCallback((id: string) => {
  setSelected(id)
}, [])

// Memoize components that receive object/array props
const MemoizedChild = memo(ChildComponent)
```

### Code Splitting
```tsx
// Lazy load heavy components
const HeavyEditor = lazy(() => import('./HeavyEditor'))

// With Suspense boundary
<Suspense fallback={<EditorSkeleton />}>
  <HeavyEditor />
</Suspense>
```

### Virtualization
For large lists:
```tsx
import { useVirtualizer } from '@tanstack/react-virtual'

const rowVirtualizer = useVirtualizer({
  count: items.length,
  getScrollElement: () => parentRef.current,
  estimateSize: () => 50,
})
```

## Common Fixes

### Dependency Arrays
```tsx
// ❌ Missing dependency
useEffect(() => {
  fetchData(userId)
}, []) // userId missing

// ✅ Complete dependencies
useEffect(() => {
  fetchData(userId)
}, [userId])
```

### State Updates
```tsx
// ❌ Stale closure
const handleClick = () => {
  setCount(count + 1) // Uses stale count
}

// ✅ Functional update
const handleClick = () => {
  setCount(prev => prev + 1)
}
```

### Cleanup
```tsx
useEffect(() => {
  const subscription = subscribe()
  return () => subscription.unsubscribe() // Always cleanup
}, [])
```

## When to Use

Apply this skill when:
- Creating new React components
- Debugging React-specific issues
- Optimizing render performance
- Implementing complex UI patterns
- Managing component state

