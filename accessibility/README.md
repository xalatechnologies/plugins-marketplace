# Accessibility & Compliance Plugin

Comprehensive accessibility and regulatory compliance agent for WCAG, Universal Utforming, GDPR, and Norwegian security standards.

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/wcag-audit` | WCAG 2.1/2.2 accessibility audit |
| `/gdpr-check` | GDPR data protection compliance check |
| `/nsm-audit` | NSM Grunnprinsipper & Digdir security audit |

### Agent

Expert compliance specialist with deep knowledge of:
- WCAG 2.1/2.2 accessibility standards
- Universal Utforming (Norwegian accessibility law)
- GDPR data protection regulation
- Digdir digitalisation standards
- NSM security principles

### Skills

| Skill | Expertise |
|-------|-----------|
| **WCAG** | Accessibility patterns, fixes, testing |
| **GDPR** | Data protection, consent, data subject rights |
| **Security** | NSM/Digdir standards, authentication, logging |

### Hooks

- Check new components for accessibility
- Audit GDPR compliance on API routes
- Verify NSM security on auth code

### MCP Tools

- Lighthouse accessibility audits
- Color contrast checking
- Accessibility tree snapshots
- axe-core scanning

## Compliance Frameworks

### WCAG 2.1 AA (Universal Utforming)

Norwegian law requires WCAG 2.1 AA compliance for all web solutions.

```bash
/wcag-audit level=AA scope=full
```

Key requirements:
- Text alternatives for images
- Keyboard accessibility
- Color contrast (4.5:1 minimum)
- Focus indicators
- Semantic HTML
- Screen reader compatibility

### GDPR

```bash
/gdpr-check scope=full
```

Requirements:
- Lawful basis for processing
- Consent mechanisms
- Data minimization
- Data subject rights (access, erasure, portability)
- Privacy notices
- Data breach procedures

### NSM Grunnprinsipper

```bash
/nsm-audit framework=both
```

The four pillars:
1. **Identifisere og kartlegge** - Asset inventory, classification
2. **Beskytte og opprettholde** - Access control, encryption, MFA
3. **Oppdage** - Logging, monitoring, anomaly detection
4. **Håndtere og gjenopprette** - Incident response, backups

## Installation

```bash
/plugin install accessibility@xalapm-marketplace
```

## Norwegian Terminology

- Universell utforming - Universal design
- Personvern - Privacy
- Samtykke - Consent
- Tilgjengelighet - Accessibility
- Personopplysninger - Personal data
- Informasjonskapsler - Cookies

