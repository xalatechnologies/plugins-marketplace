# React Development Plugin

Expert React development agent for hooks, patterns, and optimization.

## Features

### Commands
- `/hook <name>` - Create a custom React hook
- `/context <name>` - Create a React context with provider

### Agent
Specialized React agent with expertise in:
- React 18+ features
- Custom hooks and composition
- State management
- Performance optimization
- Testing with RTL

### Skills
- **Component Skill**: Patterns, performance, testing

### Hooks
- Check hook patterns on creation
- Verify context structure
- Detect performance issues

### MCP Tools
- React DevTools integration
- Component tree inspection
- Render profiling

## Usage

```bash
# Create a custom hook
/hook useDebounce type=state

# Create an async hook
/hook useFetch type=async

# Create a context
/context Theme
```

## Installation

```bash
/plugin install react@xalapm-marketplace
```

## Key Patterns

This plugin enforces:
- Memoized context values
- Proper hook dependencies
- Cleanup in effects
- TypeScript strict types

