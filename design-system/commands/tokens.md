---
description: Define or update design tokens (colors, spacing, typography)
arguments:
  - name: category
    description: Token category (colors, spacing, typography, shadows, radius)
    required: true
---

# Design Tokens Command

Create or update design tokens for the design system.

## Token Categories

### Colors

```css
/* packages/ui/src/styles/tokens.css */
:root {
  /* Brand Colors */
  --color-brand-50: 240 249 244;   /* #f0f9f4 */
  --color-brand-100: 220 243 233;  /* #dcf3e9 */
  --color-brand-200: 178 229 203;  /* #b2e5cb */
  --color-brand-300: 120 206 160;  /* #78cea0 */
  --color-brand-400: 64 175 117;   /* #40af75 */
  --color-brand-500: 34 143 85;    /* #228f55 - Primary */
  --color-brand-600: 23 115 68;    /* #177344 */
  --color-brand-700: 20 92 56;     /* #145c38 */
  --color-brand-800: 18 73 46;     /* #12492e */
  --color-brand-900: 16 60 39;     /* #103c27 */

  /* Semantic Colors */
  --color-background: 255 255 255;
  --color-foreground: 15 23 42;
  --color-muted: 241 245 249;
  --color-muted-foreground: 100 116 139;
  --color-border: 226 232 240;
  
  /* Status Colors */
  --color-success: 34 197 94;
  --color-warning: 245 158 11;
  --color-error: 239 68 68;
  --color-info: 59 130 246;
}

.dark {
  --color-background: 15 23 42;
  --color-foreground: 248 250 252;
  --color-muted: 30 41 59;
  --color-muted-foreground: 148 163 184;
  --color-border: 51 65 85;
}
```

### Tailwind Integration

```javascript
// packages/ui/tailwind.preset.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          50: 'rgb(var(--color-brand-50) / <alpha-value>)',
          100: 'rgb(var(--color-brand-100) / <alpha-value>)',
          200: 'rgb(var(--color-brand-200) / <alpha-value>)',
          300: 'rgb(var(--color-brand-300) / <alpha-value>)',
          400: 'rgb(var(--color-brand-400) / <alpha-value>)',
          500: 'rgb(var(--color-brand-500) / <alpha-value>)',
          600: 'rgb(var(--color-brand-600) / <alpha-value>)',
          700: 'rgb(var(--color-brand-700) / <alpha-value>)',
          800: 'rgb(var(--color-brand-800) / <alpha-value>)',
          900: 'rgb(var(--color-brand-900) / <alpha-value>)',
        },
        background: 'rgb(var(--color-background) / <alpha-value>)',
        foreground: 'rgb(var(--color-foreground) / <alpha-value>)',
        muted: {
          DEFAULT: 'rgb(var(--color-muted) / <alpha-value>)',
          foreground: 'rgb(var(--color-muted-foreground) / <alpha-value>)',
        },
        border: 'rgb(var(--color-border) / <alpha-value>)',
      },
    },
  },
}
```

### Typography

```css
:root {
  /* Font Families */
  --font-sans: 'Nunito Sans', system-ui, sans-serif;
  --font-heading: 'Atkinson Hyperlegible', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Font Sizes */
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px */
  --text-lg: 1.125rem;   /* 18px */
  --text-xl: 1.25rem;    /* 20px */
  --text-2xl: 1.5rem;    /* 24px */
  --text-3xl: 1.875rem;  /* 30px */
  --text-4xl: 2.25rem;   /* 36px */

  /* Line Heights */
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  
  /* Letter Spacing */
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
}
```

### Spacing

```css
:root {
  /* Base spacing unit: 4px */
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

### Shadows

```css
:root {
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  
  /* Colored shadows */
  --shadow-brand: 0 4px 14px 0 rgb(var(--color-brand-500) / 0.25);
}
```

### Border Radius

```css
:root {
  --radius-sm: 0.25rem;   /* 4px */
  --radius-md: 0.375rem;  /* 6px */
  --radius-lg: 0.5rem;    /* 8px */
  --radius-xl: 0.75rem;   /* 12px */
  --radius-2xl: 1rem;     /* 16px */
  --radius-full: 9999px;
}
```

## Guidelines

1. **Use CSS custom properties** for runtime theming
2. **Support RGB format** for alpha transparency in Tailwind
3. **Define semantic tokens** (background, foreground, muted)
4. **Provide dark mode variants**
5. **Document token purpose** with comments
6. **Keep spacing consistent** (use 4px base unit)

