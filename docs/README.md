# Documentation

Developer documentation for the Xala PM Plugin Marketplace.

---

## Quick Links

| Document | Description |
|----------|-------------|
| [Quickstart](./guides/QUICKSTART.md) | Get started in 5 minutes |
| [Developer Guide](./guides/DEVELOPER_GUIDE.md) | In-depth usage guide |
| [Creating Plugins](./guides/CREATING_PLUGINS.md) | Build your own plugins |
| [Contributing](./CONTRIBUTING.md) | Contribution guidelines |
| [Shipping](./SHIPPING.md) | Distribution and release process |

---

## Documentation Structure

```
docs/
├── README.md              # This file
├── SHIPPING.md            # Release and distribution
├── CONTRIBUTING.md        # How to contribute
├── guides/
│   ├── QUICKSTART.md      # Getting started
│   ├── DEVELOPER_GUIDE.md # Usage documentation
│   └── CREATING_PLUGINS.md # Plugin development
├── api/                   # API reference (future)
└── plugins/               # Per-plugin docs (future)
```

---

## For New Users

Start here:

1. [Quickstart Guide](./guides/QUICKSTART.md) - Installation and first commands
2. [Developer Guide](./guides/DEVELOPER_GUIDE.md) - Full usage documentation

---

## For Contributors

1. [Contributing](./CONTRIBUTING.md) - Code standards and PR process
2. [Creating Plugins](./guides/CREATING_PLUGINS.md) - Plugin structure and templates
3. [Shipping](./SHIPPING.md) - Release process

---

## Key Concepts

### Spec-Driven Development

Create specifications before coding:

```
/spec feature-name -> Write code -> /verify feature-name
```

### Expert Agents

AI agents with specialized expertise automatically engage based on context:

- Frontend files activate `@frontend-dev`
- Security code activates `@owasp-expert`
- Tests activate `@testing-specialist`

### Quality Gates

Every code change is validated against:
- TypeScript strict mode
- SOLID principles
- Security standards
- Accessibility requirements
- Performance targets

---

## Related Files

| File | Purpose |
|------|---------|
| `xalapm-core/CLAUDE.md` | Agent routing for Claude CLI |
| `xalapm-core/.cursorrules` | Agent routing for Cursor |
| `xalapm-core/standards/QUALITY_STANDARDS.md` | Quality framework |
| `xalapm-core/standards/STANDARDS.md` | Coding standards |
| `xalapm-core/AGENT_REGISTRY.md` | Available agents |

