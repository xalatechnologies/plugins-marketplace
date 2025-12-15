# Shipping Strategy

This document outlines how to distribute and maintain the Xala PM Plugin Marketplace.

---

## Distribution Channels

### 1. GitHub Repository (Primary)

The marketplace is distributed as a GitHub repository that users add directly to Claude Code.

**Repository URL:**
```
https://github.com/xalatechnologies/plugins-marketplace
```

**Installation:**
```shell
/plugin marketplace add https://github.com/xalatechnologies/plugins-marketplace
```

### 2. Local Development

For internal use before publishing:
```shell
/plugin marketplace add /path/to/local/plugins-marketplace
```

---

## Release Process

### Version Numbering

Follow Semantic Versioning (SemVer):
- **MAJOR.MINOR.PATCH** (e.g., `1.2.3`)
- **MAJOR**: Breaking changes to plugin API or command signatures
- **MINOR**: New plugins, agents, or features
- **PATCH**: Bug fixes, documentation updates

### Release Checklist

```bash
# 1. Update version in marketplace.json
jq '.version = "1.2.0"' .claude-plugin/marketplace.json > tmp && mv tmp .claude-plugin/marketplace.json

# 2. Update CHANGELOG.md
echo "## [1.2.0] - $(date +%Y-%m-%d)" >> CHANGELOG.md

# 3. Run validation
./scripts/validate-marketplace.sh

# 4. Commit and tag
git add -A
git commit -m "release: v1.2.0"
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin main --tags
```

### Pre-Release Testing

Before each release:

1. **Plugin Validation**
   ```bash
   ./scripts/validate-plugins.sh
   ```

2. **Hook Testing**
   - Install each plugin locally
   - Verify hooks trigger correctly
   - Test Python scripts execute

3. **Documentation Review**
   - All plugins have README.md
   - Commands documented
   - Skills documented

---

## Repository Structure (Shipping)

```
plugins-marketplace/
├── .claude-plugin/
│   └── marketplace.json       # Plugin registry (required)
├── docs/                      # Developer documentation
│   ├── SHIPPING.md           # This file
│   ├── CONTRIBUTING.md       # Contribution guidelines
│   └── guides/               # Usage guides
├── scripts/                   # Maintenance scripts
│   ├── validate-marketplace.sh
│   ├── validate-plugins.sh
│   └── generate-docs.sh
├── [plugin-directories]/      # Individual plugins
├── CHANGELOG.md              # Version history
├── LICENSE                   # MIT License
├── README.md                 # Main documentation
└── INSTALL.md                # Installation guide
```

---

## Maintenance Tasks

### Weekly

- Review GitHub issues
- Merge approved PRs
- Update dependencies if any

### Monthly

- Audit plugin compatibility with Claude Code updates
- Review and update agent personas if needed
- Performance review of Python scripts

### Quarterly

- Major feature planning
- Documentation audit
- User feedback review

---

## Plugin Compatibility

### Claude Code Version Support

| Marketplace Version | Claude Code Version | Notes |
|---------------------|---------------------|-------|
| 1.x | Latest | Primary support |

### Breaking Changes Policy

1. Announce breaking changes 30 days before release
2. Provide migration guide in CHANGELOG.md
3. Maintain previous major version for 90 days

---

## Monitoring

### Usage Metrics (Future)

Track via MCP server if implemented:
- Plugin installations
- Command usage frequency
- Error rates

### Issue Tracking

Use GitHub Issues with labels:
- `bug`: Something broken
- `enhancement`: Feature request
- `plugin-request`: New plugin request
- `documentation`: Docs improvement

---

## Security Considerations

### Code Review Requirements

All PRs must be reviewed for:
- No hardcoded credentials
- No external network calls without explicit permission
- Python scripts sandboxed appropriately

### Vulnerability Response

1. Security issues reported privately via GitHub Security Advisories
2. Patches released within 7 days for critical issues
3. Users notified via GitHub release notes

---

## Future Enhancements

### Planned

- [ ] npm package for MCP server components
- [ ] Plugin auto-update mechanism
- [ ] Plugin usage analytics (opt-in)
- [ ] Online documentation site

### Under Consideration

- Web-based plugin browser
- Plugin rating system
- Community plugin submissions

