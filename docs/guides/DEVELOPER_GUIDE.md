# Developer Guide

Comprehensive guide for using Xala PM plugins in your projects.

---

## Table of Contents

1. [Project Setup](#project-setup)
2. [Using Agents](#using-agents)
3. [Spec-Driven Development](#spec-driven-development)
4. [Commands Reference](#commands-reference)
5. [Quality Standards](#quality-standards)
6. [Customization](#customization)
7. [Troubleshooting](#troubleshooting)

---

## Project Setup

### Initial Configuration

After installing plugins, set up your project:

1. **Create standards folder** (if using custom standards):
   ```bash
   mkdir -p .claude/standards
   mkdir -p .claude/specs
   mkdir -p .claude/product
   ```

2. **Copy templates**:
   ```bash
   cp xalapm-core/templates/SPEC_TEMPLATE.md .claude/templates/
   ```

3. **Create CLAUDE.md** in project root:
   ```bash
   # This file is read automatically by Claude CLI
   echo "# Project Standards" > CLAUDE.md
   echo "Follow xalapm-core standards." >> CLAUDE.md
   ```

### Directory Structure

Recommended project structure:

```
your-project/
├── .claude/
│   ├── standards/          # Project-specific standards
│   ├── specs/              # Feature specifications
│   │   └── SPEC-2024-001.md
│   ├── product/            # Product documentation
│   │   ├── vision.md
│   │   └── roadmap.md
│   └── templates/          # Custom templates
├── CLAUDE.md               # Agent routing (Claude CLI)
├── .cursorrules            # Agent routing (Cursor)
└── [your code]
```

---

## Using Agents

### Automatic Agent Routing

Agents activate automatically based on context:

| Context | Agent | Persona |
|---------|-------|---------|
| React/UI files | `@frontend-dev` | Sarah Kim |
| API/Backend files | `@backend-dev` | Dr. Marcus Rivera |
| Test files | `@testing-specialist` | Dr. Elena Vasquez |
| Security keywords | `@owasp-expert` | Dr. Aisha Thompson |
| Accessibility | `@accessibility-expert` | Dr. Maya Patel |
| Database/SQL | `@supabase-dev` | Supabase Expert |
| Smart contracts | `@blockchain-expert` | Dr. Wei Zhang |
| CI/CD | `@devops-engineer` | James O'Brien |

### Manual Agent Delegation

Override automatic routing:

```
/delegate @backend-dev "Create user service with CRUD operations"
```

### Agent Communication

Agents announce themselves briefly:

```
[Acting as @frontend-dev - Sarah Kim]

I'll create this component following our UI excellence standards...
```

---

## Spec-Driven Development

### The Workflow

```
/spec -> /implement -> /verify
```

### Creating a Specification

```
/spec feature-name
```

This creates a specification file with:
- Summary
- Acceptance criteria (Gherkin format)
- Implementation plan
- Test requirements
- Definition of Done

### Example Specification

```markdown
# SPEC-2024-001: User Login

## Summary
Users can log in with email/password to access protected features.

## Acceptance Criteria

### AC-1: Successful Login
```gherkin
Given a registered user with valid credentials
When they submit the login form
Then they are authenticated and redirected to dashboard
And a session token is stored securely
```

## Implementation Plan

| Task | Agent | Plugin | Est. |
|------|-------|--------|------|
| Database schema | @backend-dev | backend | 2h |
| API endpoint | @backend-dev | backend | 4h |
| Login form UI | @frontend-dev | frontend | 4h |
| Unit tests | @testing-specialist | testing | 3h |

## Definition of Done

- [ ] All acceptance criteria pass
- [ ] 80% test coverage
- [ ] Security scan clear
- [ ] Accessibility audit pass
- [ ] Documentation complete
```

### Implementing a Specification

```
/implement SPEC-2024-001
```

Claude will:
1. Read the specification
2. Route tasks to appropriate agents
3. Follow the implementation plan
4. Reference acceptance criteria

### Verifying Implementation

```
/verify SPEC-2024-001
```

Runs quality gates against the specification.

---

## Commands Reference

### Orchestration Commands

| Command | Purpose |
|---------|---------|
| `/spec <feature>` | Create specification |
| `/implement <spec-id>` | Implement from spec |
| `/verify <spec-id>` | Verify implementation |
| `/delegate @agent "task"` | Route to specific agent |
| `/quality-gate <spec-id>` | Run all quality checks |

### Frontend Commands

| Command | Purpose |
|---------|---------|
| `/component <name>` | Generate React component |
| `/page <name>` | Generate page component |
| `/hook <name>` | Generate custom hook |

### Backend Commands

| Command | Purpose |
|---------|---------|
| `/endpoint <method> <path>` | Generate API endpoint |
| `/service <name>` | Generate service class |
| `/migration <name>` | Generate database migration |

### Testing Commands

| Command | Purpose |
|---------|---------|
| `/unit <file>` | Generate unit tests |
| `/e2e <feature>` | Generate E2E tests |
| `/performance <target>` | Performance test |

### Documentation Commands

| Command | Purpose |
|---------|---------|
| `/docs <file>` | Generate documentation |

---

## Quality Standards

### Enforced Standards

Every code change is validated against:

| Category | Requirement |
|----------|-------------|
| **TypeScript** | Strict mode, no `any` types |
| **Tests** | Minimum 80% coverage |
| **Security** | OWASP Top 10 compliance |
| **Accessibility** | WCAG 2.1 AA |
| **Performance** | LCP < 2.5s, API < 200ms |
| **Documentation** | JSDoc on exports |

### SOLID Principles

Code must follow SOLID:

| Principle | Enforcement |
|-----------|-------------|
| Single Responsibility | Functions < 30 lines |
| Open/Closed | Extensible without modification |
| Liskov Substitution | Subtypes substitutable |
| Interface Segregation | Interfaces < 5 methods |
| Dependency Inversion | Depend on abstractions |

### Size Limits

| Element | Maximum |
|---------|---------|
| Function | 30 lines |
| Class | 200 lines |
| File | 300 lines |
| Parameters | 4 |

---

## Customization

### Project-Specific Standards

Create `.claude/standards/project-standards.md`:

```markdown
# Project-Specific Standards

## Technology Stack
- React 18 with TypeScript
- Tailwind CSS
- Supabase backend

## Naming Conventions
- Components: PascalCase
- Utilities: camelCase
- Constants: SCREAMING_SNAKE_CASE
```

### Custom Agent Rules

Modify `CLAUDE.md` in project root:

```markdown
# Project Agent Rules

## Additional Context
This is a fintech application. Apply extra security scrutiny.

## Custom Routing
- For files in `payments/`, always consult @owasp-expert
- For files in `admin/`, apply compliance checks
```

### Custom Templates

Create project-specific templates in `.claude/templates/`.

---

## Troubleshooting

### Plugins Not Loading

1. Verify marketplace is added:
   ```shell
   /plugin marketplace list
   ```

2. Verify plugin is installed:
   ```shell
   /plugin list
   ```

3. Restart Claude Code

### Hooks Not Triggering

1. Check hooks.json syntax:
   ```json
   {
     "hooks": {
       "PostToolUse": [...]
     }
   }
   ```

2. Verify matcher regex is correct

### Agent Not Activating

1. Check file extension matches routing rules
2. Verify CLAUDE.md is in project root
3. Check for conflicting rules

### Python Scripts Failing

1. Verify Python 3.8+ installed
2. Check script permissions: `chmod +x script.py`
3. Check script output for errors

---

## Best Practices

### Do

- Create specs before implementing features
- Let agents route automatically
- Follow the quality gates
- Document as you code
- Write tests first (TDD)

### Don't

- Skip the spec phase for non-trivial features
- Override agents without good reason
- Ignore quality gate failures
- Leave console.logs in code
- Use `any` type in TypeScript

