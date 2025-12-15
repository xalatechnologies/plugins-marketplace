---
description: Create a new React component with proper structure, types, and tests
arguments:
  - name: name
    description: Component name (PascalCase)
    required: true
  - name: type
    description: Component type (ui, feature, layout, page)
    required: false
    default: ui
  - name: style
    description: Styling approach (tailwind, css-modules, styled)
    required: false
    default: tailwind
---

# Create Component Command

Generate a new React component following project conventions.

## Component Structure

Based on type argument:

### UI Components (`type=ui`)
Simple, reusable UI primitives:
```
src/components/ui/
└── ComponentName/
    ├── index.ts           # Re-exports
    ├── ComponentName.tsx  # Main component
    └── ComponentName.test.tsx # Tests (if testing enabled)
```

### Feature Components (`type=feature`)
Complex components with business logic:
```
src/components/features/
└── ComponentName/
    ├── index.ts
    ├── ComponentName.tsx
    ├── ComponentName.hooks.ts   # Custom hooks
    ├── ComponentName.types.ts   # Types
    └── ComponentName.test.tsx
```

### Layout Components (`type=layout`)
Page layouts and structural components:
```
src/components/layout/
└── ComponentName/
    ├── index.ts
    ├── ComponentName.tsx
    └── ComponentName.test.tsx
```

### Page Components (`type=page`)
Route-level page components:
```
src/app/[route]/
└── page.tsx  # or route.tsx for Remix
```

## Component Template

```tsx
import { forwardRef, type ComponentPropsWithoutRef } from 'react'
import { cn } from '@/lib/utils'

export interface {Name}Props extends ComponentPropsWithoutRef<'div'> {
  /** Component-specific props */
  variant?: 'default' | 'primary' | 'secondary'
}

/**
 * {Name} component
 * 
 * @example
 * <{Name} variant="primary">Content</{Name}>
 */
export const {Name} = forwardRef<HTMLDivElement, {Name}Props>(
  ({ className, variant = 'default', children, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn(
          // Base styles
          'relative',
          // Variant styles
          {
            'bg-white': variant === 'default',
            'bg-primary text-primary-foreground': variant === 'primary',
            'bg-secondary text-secondary-foreground': variant === 'secondary',
          },
          className
        )}
        {...props}
      >
        {children}
      </div>
    )
  }
)
{Name}.displayName = '{Name}'
```

## Guidelines

1. **Use forwardRef** for components that render DOM elements
2. **Extend native props** using `ComponentPropsWithoutRef<'element'>`
3. **Use cn()** for conditional class merging
4. **Document with JSDoc** including examples
5. **Keep under 150 lines** - extract hooks/utils if larger
6. **Accessibility**: Include aria attributes, keyboard handlers
7. **Responsive**: Use Tailwind breakpoint prefixes

## Accessibility Checklist

- [ ] Semantic HTML elements
- [ ] Proper heading hierarchy
- [ ] Focus visible states
- [ ] Keyboard navigation
- [ ] ARIA labels for icons/buttons
- [ ] Color contrast (4.5:1 minimum)
- [ ] Reduced motion support

