# Frontend Development Plugin

Expert frontend development agent for React, Remix, Next.js, and modern web applications.

## Features

### Commands
- `/component <name>` - Create a new React component with proper structure
- `/page <route>` - Create a new page/route with data loading and SEO

### Agent
Specialized frontend development agent with expertise in:
- React patterns and best practices
- Remix and Next.js frameworks
- TypeScript
- Tailwind CSS
- Accessibility (WCAG 2.1)
- Performance optimization

### Skills
- **React Skill**: Autonomous React development, hooks, optimization

### Hooks
- Auto-check component structure on file creation
- Warn if components exceed 150 lines
- Verify SEO metadata on pages

### MCP Tools
- Browser automation for testing
- Lighthouse audits for performance/accessibility

## Usage

```bash
# Create a UI component
/component Button type=ui

# Create a feature component
/component UserProfile type=feature

# Create a new page
/page /dashboard/analytics framework=remix
```

## Installation

```bash
/plugin install frontend@xalapm-marketplace
```

## Standards

This plugin enforces:
- Components under 150 lines
- TypeScript strict mode
- Proper accessibility attributes
- Mobile-first responsive design
- Performance best practices

