---
description: Create sophisticated, aesthetic, and rich user interfaces with Web3 standards
globs: ["**/*.tsx", "**/*.jsx", "**/*.css", "**/*.scss"]
alwaysApply: true
---

# UI Excellence Skill - Web3 Standards

> Build interfaces that are sophisticated, aesthetic, rich, animated, eye-catching, and resilient.

## Design Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│                    UI EXCELLENCE PYRAMID                         │
├─────────────────────────────────────────────────────────────────┤
│                        ▲ WEB3 DELIGHT                           │
│                       ╱ ╲ Glassmorphism, Gradients              │
│                      ╱───╲ Fluid animations, Particles          │
│                     ╱ UX  ╲ Wallet-aware, Transaction states    │
│                    ╱───────╲ Optimistic updates, Clear feedback │
│                   ╱ AESTHETIC╲ Neon accents, Dark-first         │
│                  ╱───────────╲ Typography, Color, Depth         │
│                 ╱ ACCESSIBLE  ╲ WCAG AA, Keyboard, Motion-safe  │
│                ╱───────────────╲                                │
│               ╱   RESILIENT     ╲ Offline-ready, Error recovery │
│              ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Web3 Design Standards

### Visual Signature

| Element | Web3 Standard | Implementation |
|---------|---------------|----------------|
| **Theme** | Dark-first with light option | `prefers-color-scheme: dark` as default |
| **Backgrounds** | Gradient meshes, animated | CSS gradients, Three.js, particles |
| **Glass** | Glassmorphism cards | `backdrop-filter: blur()` |
| **Accents** | Neon, vibrant gradients | Glow effects, color transitions |
| **Depth** | Layered, floating elements | Shadows, transforms, parallax |
| **Motion** | Fluid, continuous | Spring physics, GSAP, Framer Motion |

### Color System (Web3)

```css
:root {
  /* Web3 Primary Palette */
  --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --gradient-secondary: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --gradient-success: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
  --gradient-warning: linear-gradient(135deg, #f2994a 0%, #f2c94c 100%);
  --gradient-error: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
  
  /* Neon Accents */
  --neon-blue: #00d4ff;
  --neon-purple: #bf00ff;
  --neon-pink: #ff0080;
  --neon-green: #00ff88;
  --neon-orange: #ff6b00;
  
  /* Glow Effects */
  --glow-blue: 0 0 20px rgba(0, 212, 255, 0.5);
  --glow-purple: 0 0 20px rgba(191, 0, 255, 0.5);
  --glow-pink: 0 0 20px rgba(255, 0, 128, 0.5);
  
  /* Dark Theme (Default) */
  --bg-primary: #0a0a0f;
  --bg-secondary: #12121a;
  --bg-elevated: #1a1a25;
  --bg-glass: rgba(255, 255, 255, 0.05);
  
  /* Text on Dark */
  --text-primary: #ffffff;
  --text-secondary: rgba(255, 255, 255, 0.7);
  --text-muted: rgba(255, 255, 255, 0.4);
  
  /* Borders */
  --border-subtle: rgba(255, 255, 255, 0.1);
  --border-accent: rgba(255, 255, 255, 0.2);
}
```

### Glassmorphism Components

```tsx
// ✅ Web3 Glass Card
function GlassCard({ children, className, glow = false }: GlassCardProps) {
  return (
    <div
      className={cn(
        // Glass effect
        "relative overflow-hidden rounded-2xl",
        "bg-white/5 backdrop-blur-xl",
        "border border-white/10",
        
        // Subtle inner glow
        "before:absolute before:inset-0",
        "before:bg-gradient-to-br before:from-white/10 before:to-transparent",
        "before:pointer-events-none",
        
        // Hover state
        "transition-all duration-300",
        "hover:bg-white/10 hover:border-white/20",
        "hover:shadow-2xl hover:shadow-primary/10",
        "hover:-translate-y-1",
        
        // Optional glow
        glow && "shadow-lg shadow-primary/20",
        
        className
      )}
    >
      {children}
    </div>
  );
}

// ✅ Gradient Border Card
function GradientBorderCard({ children }: { children: React.ReactNode }) {
  return (
    <div className="relative p-[1px] rounded-2xl bg-gradient-to-r from-purple-500 via-pink-500 to-orange-500">
      <div className="bg-bg-secondary rounded-2xl p-6">
        {children}
      </div>
    </div>
  );
}
```

### Animated Backgrounds

```tsx
// ✅ Gradient Mesh Background
function GradientMeshBackground() {
  return (
    <div className="fixed inset-0 -z-10 overflow-hidden">
      {/* Animated gradient orbs */}
      <div
        className={cn(
          "absolute -top-40 -right-40 w-80 h-80 rounded-full",
          "bg-purple-500/30 blur-[100px]",
          "animate-blob"
        )}
      />
      <div
        className={cn(
          "absolute -bottom-40 -left-40 w-80 h-80 rounded-full",
          "bg-pink-500/30 blur-[100px]",
          "animate-blob animation-delay-2000"
        )}
      />
      <div
        className={cn(
          "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2",
          "w-80 h-80 rounded-full",
          "bg-blue-500/30 blur-[100px]",
          "animate-blob animation-delay-4000"
        )}
      />
      
      {/* Noise overlay for texture */}
      <div className="absolute inset-0 bg-noise opacity-20" />
      
      {/* Grid pattern */}
      <div
        className="absolute inset-0 opacity-20"
        style={{
          backgroundImage: `linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
                           linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px)`,
          backgroundSize: '50px 50px',
        }}
      />
    </div>
  );
}

// CSS for blob animation
const blobKeyframes = `
@keyframes blob {
  0%, 100% { transform: translate(0, 0) scale(1); }
  25% { transform: translate(20px, -30px) scale(1.1); }
  50% { transform: translate(-20px, 20px) scale(0.9); }
  75% { transform: translate(30px, 10px) scale(1.05); }
}

.animate-blob {
  animation: blob 15s ease-in-out infinite;
}

.animation-delay-2000 {
  animation-delay: 2s;
}

.animation-delay-4000 {
  animation-delay: 4s;
}
`;
```

### Web3 Button Styles

```tsx
// ✅ Gradient Button with Glow
function GradientButton({ 
  children, 
  variant = 'primary',
  size = 'md',
  loading = false,
  ...props 
}: GradientButtonProps) {
  const variants = {
    primary: 'from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500',
    secondary: 'from-blue-600 to-cyan-600 hover:from-blue-500 hover:to-cyan-500',
    success: 'from-green-600 to-emerald-600 hover:from-green-500 hover:to-emerald-500',
  };
  
  const sizes = {
    sm: 'px-4 py-2 text-sm',
    md: 'px-6 py-3 text-base',
    lg: 'px-8 py-4 text-lg',
  };

  return (
    <button
      className={cn(
        // Base
        "relative group font-semibold rounded-xl",
        "transition-all duration-300",
        sizes[size],
        
        // Gradient background
        `bg-gradient-to-r ${variants[variant]}`,
        
        // Glow effect on hover
        "hover:shadow-lg hover:shadow-purple-500/25",
        "hover:-translate-y-0.5",
        
        // Active state
        "active:translate-y-0 active:shadow-md",
        
        // Disabled
        "disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0",
        
        // Focus
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-purple-500/50"
      )}
      disabled={loading}
      {...props}
    >
      {/* Shine effect */}
      <span
        className={cn(
          "absolute inset-0 rounded-xl overflow-hidden",
          "before:absolute before:inset-0",
          "before:bg-gradient-to-r before:from-transparent before:via-white/20 before:to-transparent",
          "before:-translate-x-full group-hover:before:translate-x-full",
          "before:transition-transform before:duration-700"
        )}
      />
      
      {/* Content */}
      <span className="relative flex items-center justify-center gap-2">
        {loading && <Spinner className="w-4 h-4 animate-spin" />}
        {children}
      </span>
    </button>
  );
}

// ✅ Outline Button with Gradient Border
function OutlineButton({ children, ...props }: ButtonProps) {
  return (
    <button
      className={cn(
        "relative px-6 py-3 rounded-xl font-semibold",
        "bg-transparent text-white",
        "transition-all duration-300",
        
        // Gradient border
        "before:absolute before:inset-0 before:rounded-xl before:p-[1px]",
        "before:bg-gradient-to-r before:from-purple-500 before:to-pink-500",
        "before:-z-10",
        
        // Inner background
        "after:absolute after:inset-[1px] after:rounded-[11px]",
        "after:bg-bg-primary after:-z-10",
        
        // Hover
        "hover:after:bg-purple-500/10",
        "hover:shadow-lg hover:shadow-purple-500/20"
      )}
      {...props}
    >
      {children}
    </button>
  );
}
```

### Transaction State UI

```tsx
// ✅ Web3 Transaction States
function TransactionStatus({ status, hash }: TransactionStatusProps) {
  const states = {
    pending: {
      icon: <Spinner className="animate-spin" />,
      text: 'Transaction Pending...',
      color: 'text-yellow-400',
      bg: 'bg-yellow-500/10',
    },
    confirming: {
      icon: <Spinner className="animate-spin" />,
      text: 'Confirming on chain...',
      color: 'text-blue-400',
      bg: 'bg-blue-500/10',
    },
    success: {
      icon: <CheckCircle className="text-green-400" />,
      text: 'Transaction Confirmed',
      color: 'text-green-400',
      bg: 'bg-green-500/10',
    },
    failed: {
      icon: <XCircle className="text-red-400" />,
      text: 'Transaction Failed',
      color: 'text-red-400',
      bg: 'bg-red-500/10',
    },
  };

  const state = states[status];

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={cn(
        "flex items-center gap-3 px-4 py-3 rounded-xl",
        state.bg,
        "border border-white/10"
      )}
    >
      <span className="w-5 h-5">{state.icon}</span>
      <div className="flex-1">
        <p className={cn("font-medium", state.color)}>{state.text}</p>
        {hash && (
          <a
            href={`https://etherscan.io/tx/${hash}`}
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm text-muted hover:text-white transition-colors"
          >
            View on Explorer →
          </a>
        )}
      </div>
    </motion.div>
  );
}
```

### Wallet Connect Button

```tsx
// ✅ Web3 Connect Wallet Button
function ConnectWalletButton() {
  const { address, isConnected, connect, disconnect } = useWallet();
  const [isHovered, setIsHovered] = useState(false);

  if (isConnected) {
    return (
      <button
        onClick={disconnect}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
        className={cn(
          "flex items-center gap-2 px-4 py-2 rounded-xl",
          "bg-white/5 border border-white/10",
          "hover:bg-red-500/10 hover:border-red-500/50",
          "transition-all duration-300"
        )}
      >
        <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
        <span className="font-mono text-sm">
          {isHovered ? 'Disconnect' : `${address?.slice(0, 6)}...${address?.slice(-4)}`}
        </span>
      </button>
    );
  }

  return (
    <GradientButton onClick={connect}>
      <Wallet className="w-4 h-4" />
      Connect Wallet
    </GradientButton>
  );
}
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

---

## 🎬 Web3 Animation Patterns

### Spring Physics

```tsx
// ✅ Use spring physics for natural motion
import { motion, useSpring, useTransform } from 'framer-motion';

function AnimatedCounter({ value }: { value: number }) {
  const spring = useSpring(value, {
    stiffness: 100,
    damping: 20,
    mass: 1,
  });
  
  const display = useTransform(spring, (v) => 
    v.toLocaleString('en-US', { maximumFractionDigits: 0 })
  );

  return (
    <motion.span className="font-mono text-4xl font-bold">
      {display}
    </motion.span>
  );
}

// ✅ Stagger children animations
function StaggeredList({ items }: { items: Item[] }) {
  return (
    <motion.ul
      initial="hidden"
      animate="visible"
      variants={{
        visible: {
          transition: { staggerChildren: 0.05 }
        }
      }}
    >
      {items.map((item) => (
        <motion.li
          key={item.id}
          variants={{
            hidden: { opacity: 0, x: -20 },
            visible: { opacity: 1, x: 0 }
          }}
          transition={{ type: 'spring', stiffness: 300, damping: 24 }}
        >
          {item.content}
        </motion.li>
      ))}
    </motion.ul>
  );
}
```

### Hover Interactions

```tsx
// ✅ 3D Card Tilt Effect
function TiltCard({ children }: { children: React.ReactNode }) {
  const [rotateX, setRotateX] = useState(0);
  const [rotateY, setRotateY] = useState(0);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    
    setRotateX((y - centerY) / 10);
    setRotateY((centerX - x) / 10);
  };

  return (
    <motion.div
      className="relative perspective-1000"
      onMouseMove={handleMouseMove}
      onMouseLeave={() => { setRotateX(0); setRotateY(0); }}
      style={{
        transform: `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`,
        transformStyle: 'preserve-3d',
      }}
      transition={{ type: 'spring', stiffness: 400, damping: 30 }}
    >
      {children}
      
      {/* Shine effect */}
      <div
        className="absolute inset-0 pointer-events-none rounded-2xl"
        style={{
          background: `radial-gradient(
            circle at ${50 + rotateY * 2}% ${50 - rotateX * 2}%,
            rgba(255,255,255,0.15) 0%,
            transparent 60%
          )`,
        }}
      />
    </motion.div>
  );
}
```

### Particle Effects

```tsx
// ✅ Floating Particles Background
function ParticlesBackground() {
  const particles = useMemo(() => 
    Array.from({ length: 50 }, (_, i) => ({
      id: i,
      x: Math.random() * 100,
      y: Math.random() * 100,
      size: Math.random() * 4 + 1,
      duration: Math.random() * 20 + 10,
      delay: Math.random() * 5,
    })),
    []
  );

  return (
    <div className="fixed inset-0 -z-10 overflow-hidden pointer-events-none">
      {particles.map((p) => (
        <motion.div
          key={p.id}
          className="absolute rounded-full bg-white/20"
          style={{
            left: `${p.x}%`,
            top: `${p.y}%`,
            width: p.size,
            height: p.size,
          }}
          animate={{
            y: [0, -30, 0],
            opacity: [0.2, 0.8, 0.2],
          }}
          transition={{
            duration: p.duration,
            repeat: Infinity,
            delay: p.delay,
            ease: 'easeInOut',
          }}
        />
      ))}
    </div>
  );
}
```

### Loading States (Web3)

```tsx
// ✅ Shimmer Loading
function ShimmerSkeleton({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "relative overflow-hidden rounded-lg bg-white/5",
        className
      )}
    >
      <div
        className="absolute inset-0 -translate-x-full animate-shimmer"
        style={{
          background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent)',
        }}
      />
    </div>
  );
}

// CSS
// @keyframes shimmer { 100% { transform: translateX(100%); } }
// .animate-shimmer { animation: shimmer 1.5s infinite; }

// ✅ Pulsing Dot Loader
function PulsingDots() {
  return (
    <div className="flex gap-1">
      {[0, 1, 2].map((i) => (
        <motion.div
          key={i}
          className="w-2 h-2 rounded-full bg-white"
          animate={{ scale: [1, 1.2, 1], opacity: [0.5, 1, 0.5] }}
          transition={{
            duration: 0.8,
            repeat: Infinity,
            delay: i * 0.15,
          }}
        />
      ))}
    </div>
  );
}

// ✅ Progress Ring
function ProgressRing({ progress }: { progress: number }) {
  const circumference = 2 * Math.PI * 45;
  const offset = circumference - (progress / 100) * circumference;

  return (
    <svg className="w-24 h-24 -rotate-90">
      {/* Background */}
      <circle
        cx="48" cy="48" r="45"
        className="fill-none stroke-white/10"
        strokeWidth="6"
      />
      {/* Progress */}
      <motion.circle
        cx="48" cy="48" r="45"
        className="fill-none stroke-gradient-primary"
        strokeWidth="6"
        strokeLinecap="round"
        initial={{ strokeDashoffset: circumference }}
        animate={{ strokeDashoffset: offset }}
        style={{ strokeDasharray: circumference }}
        transition={{ duration: 0.5, ease: 'easeOut' }}
      />
    </svg>
  );
}
```

---

## Resilient UX Patterns

### Optimistic Updates

```tsx
// ✅ Optimistic UI with rollback
function LikeButton({ postId, initialLiked }: LikeButtonProps) {
  const [liked, setLiked] = useState(initialLiked);
  const [isPending, startTransition] = useTransition();

  const handleLike = async () => {
    // Optimistic update
    setLiked(!liked);
    
    startTransition(async () => {
      try {
        await toggleLike(postId);
      } catch (error) {
        // Rollback on failure
        setLiked(liked);
        toast.error('Failed to update. Please try again.');
      }
    });
  };

  return (
    <button
      onClick={handleLike}
      disabled={isPending}
      className={cn(
        "transition-all duration-200",
        liked ? "text-red-500 scale-110" : "text-gray-400 hover:text-red-400"
      )}
    >
      <Heart className={cn("w-6 h-6", liked && "fill-current")} />
    </button>
  );
}
```

### Offline Support

```tsx
// ✅ Offline-aware component
function OfflineIndicator() {
  const isOnline = useOnlineStatus();

  if (isOnline) return null;

  return (
    <motion.div
      initial={{ y: -50, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      className={cn(
        "fixed top-0 left-0 right-0 z-50",
        "bg-yellow-500/90 text-black",
        "px-4 py-2 text-center text-sm font-medium"
      )}
    >
      <WifiOff className="inline w-4 h-4 mr-2" />
      You're offline. Some features may be unavailable.
    </motion.div>
  );
}

// ✅ Pending action queue
function usePendingActions() {
  const [pending, setPending] = useState<Action[]>([]);
  const isOnline = useOnlineStatus();

  useEffect(() => {
    if (isOnline && pending.length > 0) {
      // Process queued actions
      pending.forEach(async (action) => {
        try {
          await action.execute();
          setPending((prev) => prev.filter((a) => a.id !== action.id));
          toast.success('Synced pending changes');
        } catch (error) {
          toast.error('Failed to sync. Will retry.');
        }
      });
    }
  }, [isOnline, pending]);

  return { queueAction: (action: Action) => setPending((prev) => [...prev, action]) };
}
```

### Error Recovery

```tsx
// ✅ Error boundary with retry
function ErrorFallback({ error, resetErrorBoundary }: FallbackProps) {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4">
      <div className="w-16 h-16 rounded-full bg-red-500/10 flex items-center justify-center mb-4">
        <AlertTriangle className="w-8 h-8 text-red-500" />
      </div>
      
      <h2 className="text-xl font-semibold mb-2">Something went wrong</h2>
      <p className="text-muted text-center mb-6 max-w-sm">
        {error.message || 'An unexpected error occurred. Please try again.'}
      </p>
      
      <div className="flex gap-3">
        <button
          onClick={resetErrorBoundary}
          className="px-4 py-2 bg-white/10 rounded-lg hover:bg-white/20 transition"
        >
          Try Again
        </button>
        <button
          onClick={() => window.location.reload()}
          className="px-4 py-2 text-muted hover:text-white transition"
        >
          Refresh Page
        </button>
      </div>
    </div>
  );
}
```

---

## Motion-Safe Animations

```tsx
// ✅ Respect user preferences
function MotionSafeWrapper({ children }: { children: React.ReactNode }) {
  const prefersReducedMotion = useReducedMotion();

  return (
    <motion.div
      initial={prefersReducedMotion ? false : { opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={prefersReducedMotion ? { duration: 0 } : { duration: 0.3 }}
    >
      {children}
    </motion.div>
  );
}

// CSS fallback
// @media (prefers-reduced-motion: reduce) {
//   *, ::before, ::after {
//     animation-duration: 0.01ms !important;
//     transition-duration: 0.01ms !important;
//   }
// }
```

---

## Quality Checklist

### Core UI
- [ ] Typography uses consistent scale
- [ ] Colors follow semantic system
- [ ] Spacing follows 8px grid
- [ ] All interactive elements have hover/focus states
- [ ] Loading states implemented
- [ ] Error states designed
- [ ] Empty states guide users

### Web3 Standards
- [ ] Dark theme as default
- [ ] Glassmorphism for elevated surfaces
- [ ] Gradient accents and glows
- [ ] Animated backgrounds (subtle)
- [ ] Transaction state indicators
- [ ] Wallet connection UI
- [ ] Optimistic updates implemented

### Animation
- [ ] Spring physics for natural motion
- [ ] Staggered animations for lists
- [ ] Micro-interactions on all buttons
- [ ] Page transitions smooth
- [ ] Motion-safe for reduced motion users

### Resilience
- [ ] Offline indicator present
- [ ] Error boundaries with retry
- [ ] Optimistic updates with rollback
- [ ] Loading skeletons match content shape

### Accessibility
- [ ] Dark mode text contrast meets WCAG AA
- [ ] Focus indicators visible on dark backgrounds
- [ ] Animations respect prefers-reduced-motion
- [ ] Touch targets ≥ 44px on mobile
- [ ] Screen reader tested

---

*"The best Web3 UI is indistinguishable from magic."*

