---
description: Perform WCAG 2.1/2.2 accessibility audit
arguments:
  - name: level
    description: Conformance level (A, AA, AAA)
    required: false
    default: AA
  - name: scope
    description: Audit scope (page, component, full)
    required: false
    default: page
---

# WCAG Accessibility Audit Command

Perform comprehensive WCAG 2.1/2.2 accessibility audit.

## WCAG Principles (POUR)

### 1. Perceivable
Users must be able to perceive the information.

**1.1 Text Alternatives**
```html
<!-- ❌ Missing alt text -->
<img src="logo.png">

<!-- ✅ With alt text -->
<img src="logo.png" alt="Company Logo">

<!-- ✅ Decorative image -->
<img src="decoration.png" alt="" role="presentation">
```

**1.2 Time-based Media**
- Captions for video
- Audio descriptions
- Transcripts

**1.3 Adaptable**
```html
<!-- ❌ Visual-only structure -->
<div class="big-text">Heading</div>

<!-- ✅ Semantic structure -->
<h1>Heading</h1>

<!-- ❌ Order only visual -->
<div style="order: 2">First</div>
<div style="order: 1">Second</div>

<!-- ✅ Logical DOM order matches visual -->
<div>First</div>
<div>Second</div>
```

**1.4 Distinguishable**
```css
/* ❌ Low contrast */
.text { color: #999; background: #fff; } /* 2.8:1 ratio */

/* ✅ AA compliant (4.5:1 for normal text) */
.text { color: #595959; background: #fff; } /* 4.5:1 ratio */

/* ✅ AAA compliant (7:1 for normal text) */
.text { color: #3d3d3d; background: #fff; } /* 7:1 ratio */
```

### 2. Operable
Users must be able to operate the interface.

**2.1 Keyboard Accessible**
```tsx
// ❌ Only mouse accessible
<div onClick={handleClick}>Click me</div>

// ✅ Keyboard accessible
<button onClick={handleClick}>Click me</button>

// ✅ Custom keyboard handling
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      handleClick()
    }
  }}
>
  Click me
</div>
```

**2.2 Enough Time**
- Adjustable time limits
- Pause, stop, hide moving content
- No timing-based interactions required

**2.3 Seizures and Physical Reactions**
- No flashing content >3 times/second
- Motion can be disabled

**2.4 Navigable**
```html
<!-- Skip link for keyboard users -->
<a href="#main-content" class="sr-only focus:not-sr-only">
  Skip to main content
</a>

<!-- Proper page structure -->
<main id="main-content">
  <h1>Page Title</h1>
  <!-- Focus visible -->
  <button class="focus:ring-2 focus:ring-offset-2">Action</button>
</main>
```

### 3. Understandable
Content must be understandable.

**3.1 Readable**
```html
<!-- Language declaration -->
<html lang="no">

<!-- Language changes -->
<p>This is English. <span lang="no">Dette er norsk.</span></p>
```

**3.2 Predictable**
- Consistent navigation
- Consistent identification
- No unexpected context changes

**3.3 Input Assistance**
```tsx
// ✅ Error identification and suggestions
<div>
  <label htmlFor="email">E-post</label>
  <input
    id="email"
    type="email"
    aria-invalid={hasError}
    aria-describedby="email-error"
  />
  {hasError && (
    <p id="email-error" role="alert">
      Vennligst skriv inn en gyldig e-postadresse
    </p>
  )}
</div>
```

### 4. Robust
Content must be robust for assistive technologies.

```html
<!-- ✅ Valid HTML -->
<!DOCTYPE html>
<html lang="no">
<head>
  <meta charset="UTF-8">
  <title>Page Title</title>
</head>

<!-- ✅ ARIA when needed -->
<div role="tablist" aria-label="Innstillinger">
  <button role="tab" aria-selected="true" aria-controls="panel-1">
    Generelt
  </button>
</div>
```

## Audit Output Format

```
♿ WCAG 2.1 AA AUDIT REPORT
═══════════════════════════════════════════════════════════════

Page: /dashboard
Date: 2024-12-15
Level: AA

SUMMARY
───────────────────────────────────────────────────────────────
✅ Passing:     42 criteria
⚠️ Warnings:    5 criteria
❌ Failing:     3 criteria

CRITICAL FAILURES
───────────────────────────────────────────────────────────────

[1.1.1] Non-text Content - Level A
Location: src/components/UserAvatar.tsx:15
Issue: Image missing alt attribute
Code: <img src={user.avatar} className="avatar" />
Fix: Add descriptive alt text
<img src={user.avatar} alt={`${user.name}'s avatar`} />

[1.4.3] Contrast (Minimum) - Level AA  
Location: src/components/Button.tsx:28
Issue: Text contrast ratio 3.2:1 (required 4.5:1)
Element: Secondary button text
Fix: Change text color from #888 to #595959

[2.1.1] Keyboard - Level A
Location: src/components/Dropdown.tsx:42
Issue: Custom dropdown not keyboard accessible
Fix: Add keyboard event handlers and focus management

WARNINGS
───────────────────────────────────────────────────────────────

[2.4.4] Link Purpose (In Context) - Level A
Location: src/components/BlogPost.tsx:89
Issue: Link text "Les mer" repeated without context
Suggestion: Add aria-label or improve link text

RECOMMENDATIONS
───────────────────────────────────────────────────────────────

1. Add skip link to main content
2. Improve focus indicators on custom components
3. Add aria-live regions for dynamic content
4. Test with screen reader (NVDA, VoiceOver)
```

## Universal Utforming (Norway)

Norwegian regulations require WCAG 2.1 AA compliance for:
- All new web solutions (from 2023)
- All existing solutions (deadline passed)
- Both public and private sector

Additional requirements:
- Norwegian language support
- Tilsynet for universell utforming compliance

## Guidelines

1. **Test with real users** - Include people with disabilities
2. **Use automated + manual** - Axe, Lighthouse, plus manual testing
3. **Screen reader testing** - Test with NVDA, VoiceOver, JAWS
4. **Keyboard-only navigation** - Complete all tasks without mouse
5. **Color blindness** - Test with color blindness simulators

