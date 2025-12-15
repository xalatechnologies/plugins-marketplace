---
description: React component development expertise
triggers:
  - creating react components
  - refactoring components
  - component performance
  - component testing
---

# React Component Skill

Expert React component development capabilities.

## Component Patterns

### Compound Components
```tsx
// Flexible API with shared state
const Tabs = ({ children, defaultValue }: TabsProps) => {
  const [value, setValue] = useState(defaultValue)
  return (
    <TabsContext.Provider value={{ value, setValue }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  )
}

const TabsList = ({ children }: { children: ReactNode }) => (
  <div className="tabs-list">{children}</div>
)

const TabsTrigger = ({ value, children }: TabsTriggerProps) => {
  const { value: selected, setValue } = useTabsContext()
  return (
    <button
      data-state={selected === value ? 'active' : 'inactive'}
      onClick={() => setValue(value)}
    >
      {children}
    </button>
  )
}

const TabsContent = ({ value, children }: TabsContentProps) => {
  const { value: selected } = useTabsContext()
  if (selected !== value) return null
  return <div>{children}</div>
}

// Attach sub-components
Tabs.List = TabsList
Tabs.Trigger = TabsTrigger
Tabs.Content = TabsContent
```

### Render Props
```tsx
interface DataFetcherProps<T> {
  url: string
  children: (state: { data: T | null; loading: boolean; error: Error | null }) => ReactNode
}

function DataFetcher<T>({ url, children }: DataFetcherProps<T>) {
  const state = useFetch<T>(url)
  return <>{children(state)}</>
}

// Usage
<DataFetcher url="/api/users">
  {({ data, loading, error }) => (
    loading ? <Spinner /> : <UserList users={data} />
  )}
</DataFetcher>
```

### Higher-Order Components
```tsx
function withAuth<P extends object>(Component: ComponentType<P>) {
  return function AuthenticatedComponent(props: P) {
    const { user, isLoading } = useAuth()
    
    if (isLoading) return <Spinner />
    if (!user) return <Navigate to="/login" />
    
    return <Component {...props} />
  }
}
```

### Polymorphic Components
```tsx
type PolymorphicProps<E extends ElementType> = {
  as?: E
} & ComponentPropsWithoutRef<E>

function Box<E extends ElementType = 'div'>({
  as,
  children,
  ...props
}: PolymorphicProps<E>) {
  const Component = as || 'div'
  return <Component {...props}>{children}</Component>
}

// Usage
<Box as="section" className="container">...</Box>
<Box as="article">...</Box>
<Box as={Link} to="/home">...</Box>
```

## Performance Patterns

### Avoid Re-renders
```tsx
// Split contexts
const UserContext = createContext<User | null>(null)
const UserActionsContext = createContext<UserActions | null>(null)

// Components only subscribe to what they need
function UserName() {
  const user = useContext(UserContext) // Only re-renders on user change
  return <span>{user?.name}</span>
}

function LogoutButton() {
  const actions = useContext(UserActionsContext) // Stable, no re-renders
  return <button onClick={actions?.logout}>Logout</button>
}
```

### Virtualization
```tsx
import { useVirtualizer } from '@tanstack/react-virtual'

function VirtualList({ items }: { items: Item[] }) {
  const parentRef = useRef<HTMLDivElement>(null)
  
  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
  })
  
  return (
    <div ref={parentRef} style={{ height: '400px', overflow: 'auto' }}>
      <div style={{ height: `${virtualizer.getTotalSize()}px`, position: 'relative' }}>
        {virtualizer.getVirtualItems().map(virtualRow => (
          <div
            key={virtualRow.index}
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: `${virtualRow.size}px`,
              transform: `translateY(${virtualRow.start}px)`,
            }}
          >
            {items[virtualRow.index].name}
          </div>
        ))}
      </div>
    </div>
  )
}
```

### Lazy Loading
```tsx
const HeavyComponent = lazy(() => import('./HeavyComponent'))

function App() {
  return (
    <Suspense fallback={<ComponentSkeleton />}>
      <HeavyComponent />
    </Suspense>
  )
}
```

## When to Use

Apply this skill when:
- Creating new components
- Refactoring existing components
- Fixing performance issues
- Implementing complex UI patterns
- Setting up component tests

