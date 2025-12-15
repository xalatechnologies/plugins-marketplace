---
description: Check codebase for compliance violations against Xala PM rules
---

# Check Compliance Command

Verify that the codebase follows all compliance rules for security tokens and regulated applications.

## Compliance Rules (NEVER VIOLATE)

### 🔴 Critical Rules

1. **No Public Trading for Security Tokens**
   - PM-EQ and NV-EQ tokens must NEVER have public trading enabled
   - Check for: `tradingEnabled: true` or similar flags
   - DEX/CEX integration for security tokens is prohibited

2. **KYC Verification Required**
   - All security token transfers require KYC verification
   - Check for: bypass patterns, missing verification calls
   - Whitelist verification must be enforced

3. **No Direct FIAT Handling**
   - Application must not directly handle FIAT currency
   - Check for: payment processing, bank integrations

4. **Pause Mechanism Required**
   - Security tokens must have pause functionality
   - Check for: pausable patterns, emergency stop

5. **Whitelist Verification**
   - Transfers must verify sender AND receiver are whitelisted
   - Check for: missing whitelist checks

### 🟠 High Priority Rules

6. **Audit Trail Required**
   - All mutations must be logged
   - Check for: missing log_activity calls

7. **Private Placement Status**
   - Maintain private placement exemption
   - No public solicitation patterns

## Detection Patterns

```javascript
// VIOLATION: Public trading enabled
tradingEnabled: true  // ❌ for PM-EQ, NV-EQ

// VIOLATION: DEX integration
uniswapRouter.swap(PM_EQ, ...)  // ❌

// VIOLATION: Missing KYC check
function transfer(to, amount) {
  // No KYC verification  // ❌
  _transfer(msg.sender, to, amount);
}

// CORRECT: With KYC
function transfer(to, amount) {
  require(isWhitelisted(msg.sender), "Sender not whitelisted");
  require(isWhitelisted(to), "Recipient not whitelisted");
  require(kycVerified(to), "Recipient KYC not verified");
  _transfer(msg.sender, to, amount);
}
```

## Output Format

```
⚖️ COMPLIANCE CHECK
═══════════════════════════════════════════════════════════════

Token Classification:
├── NOR:    Utility Token ✅ (Public trading allowed)
├── PM-EQ:  Security Token 🔐 (Private only)
└── NV-EQ:  Security Token 🔐 (Private only)

───────────────────────────────────────────────────────────────

🔴 CRITICAL VIOLATIONS: [count]

┌─────────────────────────────────────────────────────────────┐
│ COMP-001: Security Token Public Trading                     │
├─────────────────────────────────────────────────────────────┤
│ Location: src/contracts/PMEquity.sol:42                     │
│ Code:     tradingEnabled: true                              │
│                                                             │
│ Rule:     Security tokens must NOT have public trading      │
│ Fix:      Set tradingEnabled: false                         │
│ Impact:   REGULATORY VIOLATION                              │
└─────────────────────────────────────────────────────────────┘

🟠 HIGH VIOLATIONS: [count]
[List...]

✅ PASSING RULES: [count]
- Pause mechanism: ✅ Implemented
- Whitelist verification: ✅ Enforced
[...]

───────────────────────────────────────────────────────────────

COMPLIANCE STATUS: ❌ FAILING

Required Actions:
1. [Most critical fix]
2. [Second priority]
...

⚠️ WARNING: Do not deploy until all violations are resolved.
```

## Guidelines

- Be extremely thorough - compliance failures have legal consequences
- Always cite specific code locations
- Provide clear remediation steps
- Distinguish between utility and security tokens
- Check both Solidity contracts AND application code

