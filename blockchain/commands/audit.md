---
description: Perform security audit on smart contracts
arguments:
  - name: target
    description: Contract file or directory to audit
    required: true
  - name: severity
    description: Minimum severity to report (critical, high, medium, low, info)
    required: false
    default: low
---

# Security Audit Command

Perform comprehensive security audit on smart contracts.

## Audit Process

### 1. Static Analysis

Check for common vulnerabilities:

```
🔍 STATIC ANALYSIS
═══════════════════════════════════════════════════════════════

Checking for known vulnerability patterns...

✅ No reentrancy vulnerabilities detected
⚠️ Unchecked external call at line 142
❌ Unprotected selfdestruct at line 89
✅ No integer overflow (Solidity 0.8+)
⚠️ Missing zero-address validation at line 67
```

### 2. Vulnerability Categories

**Critical (Immediate action required):**
- Reentrancy attacks
- Unprotected selfdestruct
- Unauthorized access to funds
- Logic errors allowing theft
- Oracle manipulation

**High (Must fix before deployment):**
- Missing access control
- Integer overflow/underflow (pre-0.8)
- Unchecked external calls
- Front-running vulnerabilities
- Flash loan attacks

**Medium (Should fix):**
- Missing zero-address checks
- Floating pragma
- Missing event emissions
- Centralization risks
- Denial of service vectors

**Low (Consider fixing):**
- Gas optimization issues
- Code style inconsistencies
- Missing NatSpec
- Redundant code
- Magic numbers

**Informational:**
- Best practice suggestions
- Documentation improvements
- Test coverage gaps

### 3. Common Vulnerability Patterns

```solidity
// ❌ REENTRANCY VULNERABLE
function withdraw(uint amount) external {
    require(balances[msg.sender] >= amount);
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
    balances[msg.sender] -= amount; // State change after external call
}

// ✅ REENTRANCY SAFE (CEI Pattern)
function withdraw(uint amount) external {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount; // State change first
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
}

// ✅ REENTRANCY SAFE (ReentrancyGuard)
function withdraw(uint amount) external nonReentrant {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount;
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
}
```

```solidity
// ❌ MISSING ACCESS CONTROL
function setPrice(uint newPrice) external {
    price = newPrice;
}

// ✅ WITH ACCESS CONTROL
function setPrice(uint newPrice) external onlyRole(ADMIN_ROLE) {
    price = newPrice;
}
```

```solidity
// ❌ FRONT-RUNNING VULNERABLE
function swap(uint amountIn, uint minAmountOut) external {
    uint amountOut = calculateOutput(amountIn);
    require(amountOut >= minAmountOut);
    // Attacker can see this tx and front-run
}

// ✅ COMMIT-REVEAL PATTERN
function commitSwap(bytes32 commitment) external {
    commitments[msg.sender] = Commitment(commitment, block.number);
}

function revealSwap(uint amountIn, uint minAmountOut, bytes32 salt) external {
    require(keccak256(abi.encode(amountIn, minAmountOut, salt)) == commitments[msg.sender].hash);
    require(block.number > commitments[msg.sender].blockNumber + DELAY);
    // Execute swap
}
```

## Audit Report Format

```
🔐 SECURITY AUDIT REPORT
═══════════════════════════════════════════════════════════════

Contract: SecurityToken.sol
Auditor: Xala PM Blockchain Agent
Date: 2024-12-15
Solidity: ^0.8.20

───────────────────────────────────────────────────────────────
SUMMARY
───────────────────────────────────────────────────────────────

🔴 Critical:  0
🟠 High:      1
🟡 Medium:    2
🟢 Low:       4
ℹ️  Info:      3

Overall Risk: MEDIUM

───────────────────────────────────────────────────────────────
FINDINGS
───────────────────────────────────────────────────────────────

[H-1] Missing Reentrancy Guard on Withdraw
──────────────────────────────────────────
Severity: HIGH
Location: SecurityToken.sol:142

Description:
The withdraw() function makes an external call before updating state,
making it vulnerable to reentrancy attacks.

Code:
```
function withdraw(uint amount) external {
    require(balances[msg.sender] >= amount);
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
    balances[msg.sender] -= amount; // ❌ State update after call
}
```

Recommendation:
1. Use ReentrancyGuard from OpenZeppelin
2. Or follow CEI pattern (Checks-Effects-Interactions)

```
function withdraw(uint amount) external nonReentrant {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount; // ✅ State update first
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
}
```

[M-1] Missing Zero-Address Validation
──────────────────────────────────────────
Severity: MEDIUM
Location: SecurityToken.sol:67

[... more findings ...]

───────────────────────────────────────────────────────────────
RECOMMENDATIONS
───────────────────────────────────────────────────────────────

1. Fix all HIGH severity issues before deployment
2. Consider implementing commit-reveal for price updates
3. Add comprehensive event logging
4. Increase test coverage to >95%
5. Consider formal verification for critical functions

───────────────────────────────────────────────────────────────
APPENDIX: Test Coverage
───────────────────────────────────────────────────────────────

File                  | Lines  | Branches | Functions
---------------------|--------|----------|----------
SecurityToken.sol    | 78%    | 65%      | 82%
TokenFactory.sol     | 92%    | 88%      | 95%
---------------------|--------|----------|----------
Total                | 85%    | 76%      | 88%
```

## Tools Integration

The audit command integrates with:
- **Slither** - Static analysis
- **Mythril** - Symbolic execution
- **Echidna** - Fuzzing
- **Foundry** - Testing

## Guidelines

1. **Audit before mainnet** - Always audit before deploying to mainnet
2. **Multiple auditors** - Get at least 2 independent audits for critical contracts
3. **Fix and re-audit** - Re-audit after fixing issues
4. **Document findings** - Keep audit reports for compliance
5. **Continuous auditing** - Audit after any changes

