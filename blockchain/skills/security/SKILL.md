---
description: Blockchain security expertise - auditing, vulnerability detection, secure patterns
triggers:
  - auditing smart contracts
  - security review
  - checking vulnerabilities
  - secure development
---

# Blockchain Security Skill

Expert security auditing and vulnerability detection capabilities.

## Vulnerability Categories

### Critical Vulnerabilities

#### Reentrancy

```solidity
// ❌ VULNERABLE
function withdraw(uint amount) external {
    require(balances[msg.sender] >= amount);
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
    balances[msg.sender] -= amount;
}

// Attacker contract
contract Attacker {
    function attack() external {
        victim.withdraw(1 ether);
    }
    
    receive() external payable {
        if (address(victim).balance >= 1 ether) {
            victim.withdraw(1 ether); // Re-enters!
        }
    }
}
```

#### Unauthorized Access

```solidity
// ❌ VULNERABLE - Missing access control
function mint(address to, uint amount) external {
    _mint(to, amount);
}

// ✅ SECURE
function mint(address to, uint amount) external onlyRole(MINTER_ROLE) {
    _mint(to, amount);
}
```

#### Oracle Manipulation

```solidity
// ❌ VULNERABLE - Spot price manipulation
function getPrice() external view returns (uint) {
    return pair.reserve0 / pair.reserve1; // Can be manipulated with flash loans
}

// ✅ SECURE - TWAP oracle
function getPrice() external view returns (uint) {
    return twapOracle.consult(token, 1 ether); // Time-weighted average
}
```

### High Vulnerabilities

#### Front-Running

```solidity
// ❌ VULNERABLE
function buy(uint minAmount) external payable {
    uint amount = calculateAmount(msg.value);
    require(amount >= minAmount);
    _transfer(address(this), msg.sender, amount);
}

// ✅ SECURE - Commit-reveal
mapping(address => bytes32) public commits;
mapping(address => uint) public commitBlocks;

function commit(bytes32 hash) external {
    commits[msg.sender] = hash;
    commitBlocks[msg.sender] = block.number;
}

function reveal(uint amount, uint salt) external payable {
    require(block.number > commitBlocks[msg.sender] + 5); // Wait 5 blocks
    require(keccak256(abi.encode(amount, salt)) == commits[msg.sender]);
    // Process order
}
```

#### Flash Loan Attacks

```solidity
// ❌ VULNERABLE - Balance-based voting
function vote(uint proposalId) external {
    uint votes = token.balanceOf(msg.sender);
    proposals[proposalId].votes += votes;
}

// ✅ SECURE - Snapshot-based voting
function vote(uint proposalId) external {
    uint snapshotId = proposals[proposalId].snapshotId;
    uint votes = token.balanceOfAt(msg.sender, snapshotId);
    proposals[proposalId].votes += votes;
}
```

### Medium Vulnerabilities

#### Integer Issues

```solidity
// ❌ VULNERABLE (pre-0.8)
function multiply(uint a, uint b) external pure returns (uint) {
    return a * b; // Can overflow
}

// ✅ SECURE (0.8+)
// Automatic overflow checks

// ✅ SECURE (pre-0.8)
function multiply(uint a, uint b) external pure returns (uint) {
    return a.mul(b); // SafeMath
}
```

#### Timestamp Dependence

```solidity
// ❌ VULNERABLE
function isLucky() external view returns (bool) {
    return block.timestamp % 7 == 0; // Miner can manipulate
}

// ✅ For time-sensitive operations, use block.timestamp
// but be aware of ~15 second variance
require(block.timestamp >= deadline - 15 seconds);
```

## Audit Checklist

### Pre-Audit Preparation

- [ ] Code compiled without warnings
- [ ] All tests passing
- [ ] NatSpec documentation complete
- [ ] No TODO/FIXME comments
- [ ] Dependencies up to date
- [ ] Slither/Mythril run locally

### Audit Focus Areas

```
1. ACCESS CONTROL
   □ All functions have appropriate access modifiers
   □ onlyOwner/onlyRole used correctly
   □ No unprotected initializers
   □ No unprotected selfdestruct

2. REENTRANCY
   □ CEI pattern followed
   □ ReentrancyGuard used where needed
   □ No external calls before state updates

3. ARITHMETIC
   □ Solidity 0.8+ or SafeMath
   □ Division by zero handled
   □ Precision loss considered

4. EXTERNAL CALLS
   □ Return values checked
   □ Timeouts for oracles
   □ Fallback handling

5. COMPLIANCE (Xala PM)
   □ No public trading for security tokens
   □ KYC verification required
   □ Whitelist verification
   □ Pause mechanism present
   □ Audit trail complete
```

## Common Attack Patterns

### Proxy Vulnerability

```solidity
// ❌ VULNERABLE - Uninitialized proxy
contract TokenV1 is UUPSUpgradeable {
    function initialize() public initializer {
        // Can be called by anyone if not called during deploy
    }
}

// ✅ SECURE
contract TokenV1 is UUPSUpgradeable {
    /// @custom:oz-upgrades-unsafe-allow constructor
    constructor() {
        _disableInitializers(); // Prevent implementation initialization
    }
    
    function initialize() public initializer {
        // Safe
    }
}
```

### Signature Replay

```solidity
// ❌ VULNERABLE - Replayable signature
function execute(address to, bytes calldata data, bytes calldata sig) external {
    require(verify(sig, keccak256(abi.encode(to, data))));
    (bool success, ) = to.call(data);
}

// ✅ SECURE - Include nonce and chainId
mapping(address => uint) public nonces;

function execute(address to, bytes calldata data, uint nonce, bytes calldata sig) external {
    require(nonce == nonces[msg.sender]++);
    require(verify(sig, keccak256(abi.encode(to, data, nonce, block.chainid))));
    (bool success, ) = to.call(data);
}
```

## When to Use

Apply this skill when:
- Reviewing smart contract security
- Preparing for audits
- Detecting vulnerabilities
- Implementing secure patterns
- Writing security-critical code

