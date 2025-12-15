# Testing Specialist Plugin

Comprehensive testing agent covering E2E, unit, integration, performance, and security testing.

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/e2e create` | Create E2E tests with Playwright |
| `/e2e run` | Run E2E test suite |
| `/unit create` | Create unit tests with Vitest |
| `/unit run` | Run unit tests |
| `/unit coverage` | Run with coverage report |
| `/performance lighthouse` | Run Lighthouse audit |
| `/performance load` | Run K6 load tests |
| `/performance benchmark` | Run benchmarks |
| `/security scan` | Run security scans |
| `/security pentest` | Run penetration tests |
| `/security dependency` | Audit dependencies |

### Agent

Expert testing specialist with knowledge of:
- Playwright E2E testing
- Vitest/Jest unit testing
- K6 load testing
- Lighthouse performance
- OWASP security testing
- Chrome MCP browser testing

### Skills

| Skill | Expertise |
|-------|-----------|
| **E2E** | Playwright patterns, page objects, fixtures |
| **Unit** | Vitest, mocking, React Testing Library |
| **Performance** | Lighthouse, K6, Core Web Vitals, benchmarks |
| **Security** | Vulnerability scanning, penetration testing |

### Hooks

- Suggest tests for new source files
- Check test coverage on changes
- Review test quality
- Suggest API tests

### MCP Tools

- Browser automation (navigate, click, type)
- Accessibility snapshots
- Network request capture
- Lighthouse audits

## Test Pyramid

```
        /\  E2E (10%)
       /  \ Critical journeys
      /────\
     /      \ Integration (20%)
    /        \ API contracts
   /──────────\
  /            \ Unit (70%)
 /              \ Functions, hooks
/                \ Components
```

## Installation

```bash
/plugin install testing@xalapm-marketplace
```

## Usage Examples

```bash
# Create E2E tests
/e2e create auth-flow

# Run all E2E tests
/e2e run

# Create unit tests for a file
/unit create src/lib/utils.ts

# Run with coverage
/unit coverage

# Performance audit
/performance lighthouse url=http://localhost:3000

# Security scan
/security dependency
/security pentest url=http://localhost:3000
```

## Testing Standards

This plugin enforces:
- 80%+ code coverage
- Accessibility-first selectors
- Isolated, independent tests
- Performance budgets
- Security scanning in CI

