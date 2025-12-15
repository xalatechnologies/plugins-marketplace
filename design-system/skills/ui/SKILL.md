---
description: UI/UX design system expertise
triggers:
  - creating ui components
  - styling components
  - theming
  - accessibility
  - design tokens
---

# UI Design System Skill

Expert design system and UI development capabilities.

## Component Patterns

### Radix UI Primitives
```typescript
// Wrap Radix components with styles
import * as DialogPrimitive from '@radix-ui/react-dialog'

const Dialog = DialogPrimitive.Root
const DialogTrigger = DialogPrimitive.Trigger

const DialogContent = forwardRef<
  ElementRef<typeof DialogPrimitive.Content>,
  ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPrimitive.Portal>
    <DialogPrimitive.Overlay className="fixed inset-0 bg-black/50" />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        'fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2',
        'bg-background rounded-xl shadow-xl p-6',
        'w-full max-w-lg',
        className
      )}
      {...props}
    >
      {children}
    </DialogPrimitive.Content>
  </DialogPrimitive.Portal>
))
```

### Form Components
```typescript
// Input with label and error
interface InputProps extends ComponentPropsWithoutRef<'input'> {
  label?: string
  error?: string
  hint?: string
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, hint, id, className, ...props }, ref) => {
    const inputId = id || useId()
    const errorId = `${inputId}-error`
    const hintId = `${inputId}-hint`

    return (
      <div className="space-y-1.5">
        {label && (
          <label htmlFor={inputId} className="text-sm font-medium">
            {label}
          </label>
        )}
        <input
          ref={ref}
          id={inputId}
          aria-invalid={!!error}
          aria-describedby={error ? errorId : hint ? hintId : undefined}
          className={cn(
            'w-full rounded-lg border bg-background px-3 py-2',
            error ? 'border-error focus:ring-error' : 'border-input focus:ring-ring',
            className
          )}
          {...props}
        />
        {error && (
          <p id={errorId} className="text-sm text-error">
            {error}
          </p>
        )}
        {hint && !error && (
          <p id={hintId} className="text-sm text-muted-foreground">
            {hint}
          </p>
        )}
      </div>
    )
  }
)
```

## Animation Patterns

### CSS Transitions
```css
/* Smooth state transitions */
.button {
  transition: background-color 150ms ease, transform 100ms ease;
}

.button:hover {
  background-color: var(--color-primary-hover);
}

.button:active {
  transform: scale(0.98);
}
```

### Keyframe Animations
```css
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 200ms ease-out;
}
```

### Staggered Animations
```typescript
// Apply animation-delay for staggered reveals
{items.map((item, index) => (
  <div
    key={item.id}
    className="animate-fade-in"
    style={{ animationDelay: `${index * 50}ms` }}
  >
    {item.content}
  </div>
))}
```

## Responsive Design

### Mobile-First
```tsx
<div className="
  p-4          // Mobile: 16px
  md:p-6       // Tablet: 24px
  lg:p-8       // Desktop: 32px
  
  grid
  grid-cols-1  // Mobile: 1 column
  md:grid-cols-2  // Tablet: 2 columns
  lg:grid-cols-3  // Desktop: 3 columns
  gap-4
">
```

### Container Queries
```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}
```

## Accessibility Checklist

- [ ] Semantic HTML elements
- [ ] Proper heading hierarchy
- [ ] Focus visible states
- [ ] Keyboard navigation
- [ ] ARIA labels for icons
- [ ] Color contrast 4.5:1
- [ ] Reduced motion support
- [ ] Screen reader testing

## When to Use

Apply this skill when:
- Creating new UI components
- Implementing design tokens
- Adding animations
- Ensuring accessibility
- Building responsive layouts

