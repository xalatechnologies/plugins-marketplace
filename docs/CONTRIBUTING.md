# Contributing Guide

Guidelines for contributing to the Xala PM Plugin Marketplace.

---

## Code of Conduct

- Be professional and respectful
- Focus on technical merit
- No personal attacks or harassment

---

## Getting Started

### Prerequisites

- Claude Code installed
- Git configured
- Python 3.8+ (for script development)

### Setup

```bash
# Clone the repository
git clone https://github.com/xalatechnologies/plugins-marketplace.git
cd plugins-marketplace

# Add as local marketplace for testing
# In Claude Code:
/plugin marketplace add /path/to/plugins-marketplace
```

---

## Contribution Types

### 1. Bug Fixes

1. Create issue describing the bug
2. Fork repository
3. Create branch: `fix/issue-description`
4. Fix and test
5. Submit PR referencing issue

### 2. New Plugin

1. Discuss in GitHub Discussions first
2. Follow plugin structure template
3. Include all required files
4. Submit PR with documentation

### 3. Documentation

1. Fork repository
2. Create branch: `docs/description`
3. Update documentation
4. Submit PR

---

## Plugin Development Guidelines

### Required Files

Every plugin must have:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        # Required: Plugin metadata
├── README.md              # Required: Plugin documentation
├── agents/
│   └── [name].md          # Required if agent-based
├── commands/
│   └── [command].md       # Required for slash commands
├── skills/
│   └── [skill]/SKILL.md   # Optional: Agent skills
└── hooks/
    └── hooks.json         # Optional: Event handlers
```

### plugin.json Format

```json
{
  "name": "my-plugin",
  "description": "Clear, concise description",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "category": "development|testing|security|devops|documentation",
  "keywords": ["keyword1", "keyword2"]
}
```

### Agent Persona Guidelines

See `xalapm-core/templates/` for templates.

Required sections:
- Name and title
- Background (establishing expertise)
- Core beliefs/philosophy
- Operational guidelines (DO/DON'T)
- Communication style
- Example interactions

### Command Format

```markdown
---
description: What the command does
---

# Command Name

Instructions for Claude on how to execute this command.

## Parameters

- `param1`: Description

## Process

1. Step one
2. Step two

## Output Format

Describe expected output.
```

### Hooks Format

```json
{
  "description": "What this hook does",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Instructions for Claude"
          }
        ]
      }
    ]
  }
}
```

---

## Code Standards

### General

- No emojis in code, comments, commits, or documentation
- Professional, technical language only
- Conventional Commits format

### TypeScript (if applicable)

- Strict mode enabled
- No `any` types
- Explicit return types

### Python Scripts

- Python 3.8+ compatible
- Type hints recommended
- Docstrings required

### Markdown

- ATX headers (# style)
- Fenced code blocks with language
- Tables for structured data

---

## Commit Messages

Use Conventional Commits:

```bash
# Format
<type>(<scope>): <description>

# Types
feat:     New feature
fix:      Bug fix
docs:     Documentation only
refactor: Code change (no feature/fix)
test:     Adding tests
chore:    Maintenance

# Examples
feat(frontend): add new component command
fix(security): resolve injection detection false positive
docs(readme): update installation instructions
refactor(orchestrator): extract validation logic
```

---

## Pull Request Process

### Before Submitting

- [ ] Plugin validates successfully
- [ ] All required files present
- [ ] README.md updated
- [ ] No lint errors
- [ ] Tested locally with Claude Code
- [ ] Commits follow Conventional Commits

### PR Description Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Breaking change

## Testing
Describe testing performed.

## Checklist
- [ ] I have tested this locally
- [ ] Documentation is updated
- [ ] No hardcoded credentials
- [ ] Follows code standards
```

### Review Process

1. Automated checks run
2. Maintainer review
3. Address feedback
4. Approval and merge

---

## Testing

### Manual Testing

1. Install plugin locally
2. Test each command
3. Verify hooks trigger
4. Check error handling

### Validation Script

```bash
./scripts/validate-plugins.sh
```

Validates:
- plugin.json schema
- Required files exist
- hooks.json format
- No syntax errors

---

## Questions?

- GitHub Discussions for questions
- GitHub Issues for bugs
- PRs for contributions

