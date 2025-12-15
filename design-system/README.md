# Design System Plugin

Expert design system development agent for UI components, theming, and accessibility.

## Features

### Commands
- `/ui-component <name>` - Create a design system UI component
- `/tokens <category>` - Define or update design tokens

### Agent
Specialized design agent with expertise in:
- Component library architecture
- Tailwind CSS and CVA
- Design tokens and theming
- Accessibility (WCAG 2.1 AA)
- Animation and micro-interactions

### Skills
- **UI Skill**: Components, animations, responsive design, a11y

### Hooks
- Check accessibility on new components
- Verify CSS uses design tokens
- Validate Tailwind configuration

### MCP Tools
- Storybook integration
- Figma design specs
- Color contrast checking

## Usage

```bash
# Create a UI component
/ui-component Card base=div

# Create tokens
/tokens colors
/tokens typography
```

## Installation

```bash
/plugin install design-system@xalapm-marketplace
```

## Design Principles

This plugin enforces:
- CVA for variant styles
- CSS custom properties for tokens
- WCAG 2.1 AA accessibility
- Mobile-first responsive design
- Reduced motion support

