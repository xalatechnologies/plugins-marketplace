---
description: Perform comprehensive security scan of the codebase
args:
  scope: What to scan - owasp, soc2, dependencies, all (default: all)
  path: Path to scan (default: current directory)
---

# Security Scan Command

Perform a comprehensive security scan covering OWASP, SOC2 controls, and dependency vulnerabilities.

## Process

### 1. OWASP Top 10 Scan

Check for:
- A01: Broken Access Control
- A02: Cryptographic Failures  
- A03: Injection
- A04: Insecure Design
- A05: Security Misconfiguration
- A06: Vulnerable Components
- A07: Authentication Failures
- A08: Software Integrity Failures
- A09: Logging Failures
- A10: SSRF

### 2. SOC2 Control Check

Verify:
- CC6.1: Logical access controls
- CC6.6: Encryption requirements
- CC7.2: Monitoring and alerting
- CC8.1: Change management

### 3. Dependency Scan

Check:
- Known CVEs in dependencies
- Outdated packages
- License compliance
- SBOM generation

## Output Format

```markdown
## 🔒 Security Scan Report

**Scan Date:** {date}
**Scope:** {scope}
**Path:** {path}

### Summary

| Severity | Count |
|----------|-------|
| 🔴 Critical | X |
| 🟠 High | X |
| 🟡 Medium | X |
| ℹ️ Low | X |

### OWASP Findings

| OWASP | Issue | Location | Severity |
|-------|-------|----------|----------|
| A03 | SQL Injection | file.ts:45 | Critical |

### SOC2 Gaps

| Control | Status | Gap |
|---------|--------|-----|
| CC6.1 | ⚠️ | Missing auth on /api/admin |

### Dependency Vulnerabilities

| Package | CVE | Severity | Fix |
|---------|-----|----------|-----|
| lodash | CVE-XXX | High | 4.17.21 |

### Recommendations

1. [Priority 1 fix]
2. [Priority 2 fix]
```

