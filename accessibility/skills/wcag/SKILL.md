---
description: WCAG accessibility expertise
triggers:
  - creating ui components
  - working with forms
  - adding images
  - building navigation
  - accessibility
---

# WCAG Accessibility Skill

Expert WCAG 2.1/2.2 compliance capabilities.

## Quick Fixes

### Images
```tsx
// ❌ Missing alt
<img src="user.jpg" />

// ✅ Descriptive alt
<img src="user.jpg" alt="Profile photo of John Smith" />

// ✅ Decorative (empty alt)
<img src="decoration.svg" alt="" role="presentation" />
```

### Buttons & Links
```tsx
// ❌ Icon-only without label
<button><TrashIcon /></button>

// ✅ With accessible name
<button aria-label="Slett element">
  <TrashIcon aria-hidden="true" />
</button>

// ❌ Non-specific link text
<a href="/more">Les mer</a>

// ✅ Descriptive link
<a href="/article/123">Les mer om tilgjengelighet</a>
```

### Forms
```tsx
// ❌ Missing label
<input type="email" placeholder="E-post" />

// ✅ Proper label
<label htmlFor="email">E-post</label>
<input id="email" type="email" />

// ✅ With error handling
<label htmlFor="email">E-post</label>
<input
  id="email"
  type="email"
  aria-invalid={hasError}
  aria-describedby="email-error"
/>
{hasError && <span id="email-error">Ugyldig e-post</span>}
```

### Focus Management
```tsx
// ✅ Visible focus indicator
<button className="focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Klikk meg
</button>

// ✅ Focus trap for modals
import { FocusTrap } from '@radix-ui/react-focus-trap'

<FocusTrap>
  <dialog open>
    <h2>Dialog tittel</h2>
    <button>Lukk</button>
  </dialog>
</FocusTrap>
```

### Skip Links
```tsx
// ✅ Skip to main content
<a
  href="#main-content"
  className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4"
>
  Hopp til hovedinnhold
</a>

<main id="main-content" tabIndex={-1}>
  {/* Content */}
</main>
```

### Color Contrast
```css
/* ❌ Low contrast (2.5:1) */
.text { color: #aaa; background: #fff; }

/* ✅ AA compliant (4.5:1 for normal text) */
.text { color: #595959; background: #fff; }

/* ✅ Large text (24px+) needs 3:1 */
.heading { color: #767676; background: #fff; }
```

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Testing Checklist

```
AUTOMATED (Lighthouse, axe)
├── Run Lighthouse accessibility audit
├── Run axe DevTools
└── Fix all automated issues

KEYBOARD
├── Tab through entire page
├── All interactive elements focusable
├── Focus order logical
├── No keyboard traps
└── Skip links work

SCREEN READER
├── Test with NVDA (Windows)
├── Test with VoiceOver (Mac)
├── All content announced
├── Landmarks identified
└── Forms labeled correctly

VISUAL
├── Zoom to 200% - content reflows
├── Color contrast verified
├── Focus indicators visible
└── Content readable without CSS
```

## When to Use

Apply automatically when:
- Creating new UI components
- Building forms
- Adding images
- Implementing navigation
- Creating interactive elements

