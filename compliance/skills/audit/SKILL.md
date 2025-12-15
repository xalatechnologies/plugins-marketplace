---
description: Autonomous compliance auditing capability - Claude will proactively check for violations
triggers:
  - modifying security token code
  - changing trading functionality
  - updating transfer logic
  - working on payment features
---

# Compliance Audit Skill

You have the ability to automatically check for compliance violations. Use this skill when:

- Working on any code related to tokens (PM-EQ, NV-EQ, NOR)
- Modifying transfer or trading functionality
- Adding payment or financial features
- Changing authentication or KYC flows

## Automatic Checks

When you detect work related to compliance-sensitive areas, automatically verify:

### For Security Tokens (PM-EQ, NV-EQ)
1. ❌ No public trading enabled
2. ❌ No DEX/CEX integration
3. ✅ KYC verification required
4. ✅ Whitelist verification enforced
5. ✅ Pause mechanism present
6. ✅ Audit logging enabled

### For All Financial Operations
1. ❌ No direct FIAT handling
2. ✅ Audit trail for mutations
3. ✅ Rate limiting on sensitive endpoints

## Proactive Warnings

If you detect a potential violation during normal work, immediately warn the user:

```
⚠️ COMPLIANCE WARNING

I noticed you're about to [action]. This may violate compliance rule:

Rule: [Rule name]
Reason: [Why this is problematic]

Recommended approach:
[Compliant alternative]

Would you like me to help implement this the compliant way?
```

## Token Classification Reference

| Token | Type | Public Trading | KYC Required |
|-------|------|----------------|--------------|
| NOR | Utility | ✅ Allowed | Optional |
| PM-EQ | Security | ❌ Prohibited | Required |
| NV-EQ | Security | ❌ Prohibited | Required |

## Integration

When Xala PM MCP tools are available:
- Log compliance checks to activity feed
- Update compliance status in dashboard
- Create tasks for violations

