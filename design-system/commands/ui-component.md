---
description: Create a design system UI component with variants, theming, and accessibility
arguments:
  - name: name
    description: Component name (PascalCase)
    required: true
  - name: base
    description: Base element or Radix primitive to extend
    required: false
    default: div
---

# Create UI Component Command

Generate a design system UI component with proper structure.

## Component Structure

```
packages/ui/src/
└── ComponentName/
    ├── index.ts              # Re-exports
    ├── ComponentName.tsx     # Main component
    ├── ComponentName.styles.ts # Variant styles (cva)
    └── ComponentName.stories.tsx # Storybook stories
```

## Component Template

```typescript
// packages/ui/src/Button/Button.tsx
import { forwardRef, type ComponentPropsWithoutRef } from 'react'
import { Slot } from '@radix-ui/react-slot'
import { cn } from '../utils'
import { buttonVariants, type ButtonVariants } from './Button.styles'

export interface ButtonProps
  extends ComponentPropsWithoutRef<'button'>,
    ButtonVariants {
  /**
   * If true, the component will render as a Slot (pass through to child)
   */
  asChild?: boolean
  /**
   * If true, shows a loading spinner and disables the button
   */
  loading?: boolean
}

/**
 * Primary action button component
 *
 * @example
 * <Button variant="primary" size="lg">
 *   Click me
 * </Button>
 *
 * @example
 * <Button asChild>
 *   <a href="/link">Link Button</a>
 * </Button>
 */
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      className,
      variant,
      size,
      asChild = false,
      loading = false,
      disabled,
      children,
      ...props
    },
    ref
  ) => {
    const Comp = asChild ? Slot : 'button'

    return (
      <Comp
        ref={ref}
        className={cn(buttonVariants({ variant, size }), className)}
        disabled={disabled || loading}
        aria-disabled={disabled || loading}
        {...props}
      >
        {loading ? (
          <>
            <span className="loading-spinner" aria-hidden="true" />
            <span className="sr-only">Loading...</span>
            {children}
          </>
        ) : (
          children
        )}
      </Comp>
    )
  }
)
Button.displayName = 'Button'
```

## Styles with CVA (Class Variance Authority)

```typescript
// packages/ui/src/Button/Button.styles.ts
import { cva, type VariantProps } from 'class-variance-authority'

export const buttonVariants = cva(
  // Base styles
  [
    'inline-flex items-center justify-center gap-2',
    'font-medium',
    'transition-colors duration-150',
    'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2',
    'disabled:pointer-events-none disabled:opacity-50',
    'select-none',
  ],
  {
    variants: {
      variant: {
        primary: [
          'bg-primary text-primary-foreground',
          'hover:bg-primary/90',
          'focus-visible:ring-primary',
        ],
        secondary: [
          'bg-secondary text-secondary-foreground',
          'hover:bg-secondary/80',
          'focus-visible:ring-secondary',
        ],
        outline: [
          'border border-input bg-transparent',
          'hover:bg-accent hover:text-accent-foreground',
          'focus-visible:ring-ring',
        ],
        ghost: [
          'bg-transparent',
          'hover:bg-accent hover:text-accent-foreground',
        ],
        destructive: [
          'bg-destructive text-destructive-foreground',
          'hover:bg-destructive/90',
          'focus-visible:ring-destructive',
        ],
        link: [
          'text-primary underline-offset-4',
          'hover:underline',
        ],
      },
      size: {
        sm: 'h-8 px-3 text-xs rounded-md',
        md: 'h-10 px-4 text-sm rounded-lg',
        lg: 'h-12 px-6 text-base rounded-lg',
        icon: 'h-10 w-10 rounded-lg',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

export type ButtonVariants = VariantProps<typeof buttonVariants>
```

## Storybook Stories

```typescript
// packages/ui/src/Button/Button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react'
import { Button } from './Button'

const meta = {
  title: 'Components/Button',
  component: Button,
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'outline', 'ghost', 'destructive', 'link'],
    },
    size: {
      control: 'select',
      options: ['sm', 'md', 'lg', 'icon'],
    },
  },
} satisfies Meta<typeof Button>

export default meta
type Story = StoryObj<typeof meta>

export const Primary: Story = {
  args: {
    children: 'Primary Button',
    variant: 'primary',
  },
}

export const Secondary: Story = {
  args: {
    children: 'Secondary Button',
    variant: 'secondary',
  },
}

export const Outline: Story = {
  args: {
    children: 'Outline Button',
    variant: 'outline',
  },
}

export const Loading: Story = {
  args: {
    children: 'Loading Button',
    loading: true,
  },
}

export const AllVariants: Story = {
  render: () => (
    <div className="flex flex-wrap gap-4">
      <Button variant="primary">Primary</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="outline">Outline</Button>
      <Button variant="ghost">Ghost</Button>
      <Button variant="destructive">Destructive</Button>
      <Button variant="link">Link</Button>
    </div>
  ),
}
```

## Guidelines

1. **Use CVA** for variant styles
2. **Support asChild** with Radix Slot
3. **Include loading state** where appropriate
4. **Add aria attributes** for accessibility
5. **Export types** for consumers
6. **Write Storybook stories** for documentation
7. **Support dark mode** via CSS variables

