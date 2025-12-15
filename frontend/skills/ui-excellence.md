---
description: Create sophisticated, aesthetic, and rich user interfaces
globs: ["**/*.tsx", "**/*.jsx", "**/*.css", "**/*.scss"]
---

# UI Excellence Skill

> Build interfaces that are sophisticated, aesthetic, rich, and delightful.

## Design Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│                    UI EXCELLENCE PYRAMID                         │
├─────────────────────────────────────────────────────────────────┤
│                        ▲ DELIGHT                                │
│                       ╱ ╲ Micro-interactions                    │
│                      ╱───╲ Animations                           │
│                     ╱ UX  ╲ Intuitive flows                     │
│                    ╱───────╲ Clear feedback                     │
│                   ╱ AESTHETIC╲ Typography, color, space         │
│                  ╱───────────╲ Visual hierarchy                 │
│                 ╱ ACCESSIBLE  ╲ WCAG AA, keyboard, screen reader│
│                ╱───────────────╲                                │
│               ╱   FUNCTIONAL    ╲ Works correctly, performant   │
│              ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔                               │
└─────────────────────────────────────────────────────────────────┘
```

## Typography Standards

### Font Scale (Perfect Fourth - 1.333)

```css
:root {
  /* Font Families */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-display: 'Cal Sans', 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;

  /* Type Scale */
  --text-xs: 0.75rem;     /* 12px */
  --text-sm: 0.875rem;    /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg: 1.125rem;    /* 18px */
  --text-xl: 1.333rem;    /* 21px */
  --text-2xl: 1.777rem;   /* 28px */
  --text-3xl: 2.369rem;   /* 38px */
  --text-4xl: 3.157rem;   /* 51px */
  --text-5xl: 4.209rem;   /* 67px */

  /* Line Heights */
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.75;

  /* Letter Spacing */
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
}
```

### Typography Best Practices

```tsx
// ✅ DO: Rich typography hierarchy
<article className="prose prose-lg">
  <h1 className="font-display text-4xl tracking-tight font-bold">
    Article Title
  </h1>
  <p className="text-xl text-gray-600 leading-relaxed">
    Lead paragraph with larger, more readable text.
  </p>
  <h2 className="font-display text-2xl mt-12 mb-4">
    Section Heading
  </h2>
  <p className="text-base leading-relaxed">
    Body text with comfortable reading experience.
  </p>
</article>

// ❌ DON'T: Flat, boring typography
<div>
  <div className="text-lg font-bold">Title</div>
  <div>Some text here</div>
</div>
```

## Color System

### Semantic Color Tokens

```css
:root {
  /* Brand */
  --color-primary: oklch(65% 0.25 250);
  --color-primary-hover: oklch(60% 0.28 250);
  --color-secondary: oklch(70% 0.15 180);

  /* Semantic */
  --color-success: oklch(70% 0.2 145);
  --color-warning: oklch(80% 0.2 85);
  --color-error: oklch(60% 0.25 25);
  --color-info: oklch(65% 0.2 250);

  /* Neutral */
  --color-background: oklch(99% 0.005 250);
  --color-surface: oklch(100% 0 0);
  --color-surface-elevated: oklch(100% 0 0);
  --color-border: oklch(90% 0.01 250);
  --color-text: oklch(20% 0.02 250);
  --color-text-secondary: oklch(45% 0.02 250);
  --color-text-muted: oklch(60% 0.01 250);
}

/* Dark mode */
[data-theme="dark"] {
  --color-background: oklch(15% 0.02 250);
  --color-surface: oklch(20% 0.02 250);
  --color-surface-elevated: oklch(25% 0.02 250);
  --color-border: oklch(30% 0.02 250);
  --color-text: oklch(95% 0.01 250);
  --color-text-secondary: oklch(75% 0.01 250);
  --color-text-muted: oklch(55% 0.01 250);
}
```

### Color Contrast (WCAG AA)

```tsx
// ✅ DO: Ensure 4.5:1 contrast for text
<p className="text-gray-700 bg-white">Readable text</p>      // ✓ 8.5:1
<p className="text-gray-500 bg-white">Secondary text</p>     // ✓ 4.6:1

// ❌ DON'T: Low contrast
<p className="text-gray-400 bg-white">Hard to read</p>       // ✗ 2.9:1
```

## Spacing System

### 8px Grid

```css
:root {
  --space-0: 0;
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */
}
```

### Spacing Best Practices

```tsx
// ✅ DO: Consistent spacing rhythm
<div className="p-6 space-y-4">
  <h2 className="text-2xl">Card Title</h2>
  <p className="text-gray-600">Card description with proper spacing.</p>
  <div className="flex gap-3 pt-4">
    <Button>Primary</Button>
    <Button variant="secondary">Secondary</Button>
  </div>
</div>

// ❌ DON'T: Arbitrary spacing
<div style={{ padding: '17px' }}>
  <h2 style={{ marginBottom: '7px' }}>Inconsistent</h2>
</div>
```

## Motion & Animation

### Transition Standards

```css
:root {
  /* Durations */
  --duration-instant: 50ms;
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --duration-slow: 350ms;
  --duration-slower: 500ms;

  /* Easings */
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### Micro-Interactions

```tsx
// ✅ DO: Delightful micro-interactions
<button
  className={cn(
    "relative px-4 py-2 rounded-lg",
    "bg-primary text-white font-medium",
    "transition-all duration-150 ease-out",
    "hover:bg-primary-hover hover:shadow-lg hover:-translate-y-0.5",
    "active:translate-y-0 active:shadow-md",
    "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary/50",
    "disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0"
  )}
>
  {children}
</button>

// Loading state with smooth transition
<button disabled={isLoading}>
  <span className={cn(
    "transition-opacity duration-150",
    isLoading ? "opacity-0" : "opacity-100"
  )}>
    Submit
  </span>
  {isLoading && (
    <div className="absolute inset-0 flex items-center justify-center">
      <Spinner className="animate-spin" />
    </div>
  )}
</button>
```

### Page Transitions

```tsx
// ✅ Smooth page load animations
const pageVariants = {
  initial: { opacity: 0, y: 20 },
  enter: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -20 },
};

<motion.main
  initial="initial"
  animate="enter"
  exit="exit"
  variants={pageVariants}
  transition={{ duration: 0.3, ease: "easeOut" }}
>
  {children}
</motion.main>
```

## Component Patterns

### Card Component (Rich UI)

```tsx
export function Card({ 
  title, 
  description, 
  image, 
  tags, 
  actions 
}: CardProps) {
  return (
    <article
      className={cn(
        "group relative overflow-hidden rounded-2xl",
        "bg-surface border border-border",
        "transition-all duration-300 ease-out",
        "hover:border-primary/20 hover:shadow-xl hover:shadow-primary/5",
        "hover:-translate-y-1"
      )}
    >
      {/* Image with overlay */}
      {image && (
        <div className="relative aspect-video overflow-hidden">
          <img
            src={image}
            alt=""
            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent" />
        </div>
      )}

      {/* Content */}
      <div className="p-6 space-y-4">
        {/* Tags */}
        {tags && (
          <div className="flex flex-wrap gap-2">
            {tags.map((tag) => (
              <span
                key={tag}
                className="px-2 py-1 text-xs font-medium rounded-full bg-primary/10 text-primary"
              >
                {tag}
              </span>
            ))}
          </div>
        )}

        {/* Title & Description */}
        <div className="space-y-2">
          <h3 className="text-xl font-display font-semibold tracking-tight text-text group-hover:text-primary transition-colors">
            {title}
          </h3>
          <p className="text-text-secondary leading-relaxed line-clamp-2">
            {description}
          </p>
        </div>

        {/* Actions */}
        {actions && (
          <div className="flex items-center gap-3 pt-4 border-t border-border">
            {actions}
          </div>
        )}
      </div>

      {/* Hover indicator */}
      <div
        className={cn(
          "absolute bottom-0 left-0 right-0 h-1",
          "bg-gradient-to-r from-primary to-secondary",
          "transform origin-left scale-x-0",
          "transition-transform duration-300 ease-out",
          "group-hover:scale-x-100"
        )}
      />
    </article>
  );
}
```

### Form Inputs (Interactive UX)

```tsx
export function Input({ 
  label, 
  error, 
  hint, 
  icon,
  ...props 
}: InputProps) {
  const [isFocused, setIsFocused] = useState(false);
  const [hasValue, setHasValue] = useState(Boolean(props.value));

  return (
    <div className="relative">
      {/* Floating Label */}
      <label
        className={cn(
          "absolute left-3 transition-all duration-200 pointer-events-none",
          "text-text-muted",
          (isFocused || hasValue)
            ? "top-2 text-xs text-primary"
            : "top-1/2 -translate-y-1/2 text-base"
        )}
      >
        {label}
      </label>

      {/* Input */}
      <input
        {...props}
        className={cn(
          "w-full pt-6 pb-2 px-3 rounded-lg",
          "bg-surface border-2 transition-all duration-200",
          "text-text placeholder-transparent",
          "focus:outline-none",
          error
            ? "border-error focus:border-error focus:ring-4 focus:ring-error/10"
            : "border-border focus:border-primary focus:ring-4 focus:ring-primary/10",
          icon && "pr-10"
        )}
        onFocus={(e) => {
          setIsFocused(true);
          props.onFocus?.(e);
        }}
        onBlur={(e) => {
          setIsFocused(false);
          setHasValue(Boolean(e.target.value));
          props.onBlur?.(e);
        }}
      />

      {/* Icon */}
      {icon && (
        <div className="absolute right-3 top-1/2 -translate-y-1/2 text-text-muted">
          {icon}
        </div>
      )}

      {/* Error/Hint */}
      <div className="mt-1.5 min-h-[20px]">
        {error && (
          <p className="text-sm text-error flex items-center gap-1">
            <AlertCircle className="w-4 h-4" />
            {error}
          </p>
        )}
        {!error && hint && (
          <p className="text-sm text-text-muted">{hint}</p>
        )}
      </div>
    </div>
  );
}
```

## Rich UI Patterns

### Skeleton Loading

```tsx
function Skeleton({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "animate-pulse rounded-lg bg-gradient-to-r",
        "from-gray-200 via-gray-100 to-gray-200",
        "bg-[length:200%_100%]",
        className
      )}
    />
  );
}

// Usage
function CardSkeleton() {
  return (
    <div className="p-6 space-y-4 border rounded-2xl">
      <Skeleton className="h-48 w-full" />
      <Skeleton className="h-4 w-3/4" />
      <Skeleton className="h-4 w-1/2" />
      <div className="flex gap-2">
        <Skeleton className="h-6 w-16 rounded-full" />
        <Skeleton className="h-6 w-16 rounded-full" />
      </div>
    </div>
  );
}
```

### Toast Notifications

```tsx
function Toast({ type, title, message, onDismiss }: ToastProps) {
  const icons = {
    success: <CheckCircle className="w-5 h-5 text-success" />,
    error: <XCircle className="w-5 h-5 text-error" />,
    warning: <AlertTriangle className="w-5 h-5 text-warning" />,
    info: <Info className="w-5 h-5 text-info" />,
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 50, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, y: 20, scale: 0.95 }}
      className={cn(
        "flex items-start gap-3 p-4 rounded-xl shadow-lg",
        "bg-surface border border-border",
        "max-w-sm w-full"
      )}
    >
      {icons[type]}
      <div className="flex-1 min-w-0">
        <p className="font-medium text-text">{title}</p>
        {message && (
          <p className="mt-1 text-sm text-text-secondary">{message}</p>
        )}
      </div>
      <button
        onClick={onDismiss}
        className="text-text-muted hover:text-text transition-colors"
      >
        <X className="w-4 h-4" />
      </button>
    </motion.div>
  );
}
```

## Quality Checklist

- [ ] Typography uses consistent scale
- [ ] Colors follow semantic system
- [ ] Spacing follows 8px grid
- [ ] All interactive elements have hover/focus states
- [ ] Loading states implemented
- [ ] Error states designed
- [ ] Empty states guide users
- [ ] Animations are purposeful (not excessive)
- [ ] Dark mode supported
- [ ] Responsive on all breakpoints
- [ ] Touch targets ≥ 44px on mobile
- [ ] Contrast ratios meet WCAG AA

