---
description: Smart contract development expertise - Solidity, security, testing, deployment
triggers:
  - writing solidity
  - creating smart contracts
  - auditing contracts
  - deploying contracts
  - smart contract security
---

# Smart Contract Development Skill

Expert Solidity development and security capabilities.

## Security Patterns

### Reentrancy Protection

```solidity
// Option 1: ReentrancyGuard
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

contract Safe is ReentrancyGuard {
    function withdraw(uint amount) external nonReentrant {
        // Safe from reentrancy
    }
}

// Option 2: CEI Pattern
function withdraw(uint amount) external {
    // Checks
    require(balances[msg.sender] >= amount, "Insufficient");
    
    // Effects (before external call)
    balances[msg.sender] -= amount;
    
    // Interactions (last)
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
}
```

### Access Control

```solidity
import "@openzeppelin/contracts/access/AccessControl.sol";

contract Controlled is AccessControl {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant OPERATOR_ROLE = keccak256("OPERATOR_ROLE");
    
    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(ADMIN_ROLE, msg.sender);
    }
    
    function adminOnly() external onlyRole(ADMIN_ROLE) {
        // Only admins
    }
    
    function operatorOnly() external onlyRole(OPERATOR_ROLE) {
        // Only operators
    }
}
```

### Pausable

```solidity
import "@openzeppelin/contracts/utils/Pausable.sol";

contract Pausable is Pausable, AccessControl {
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    
    function pause() external onlyRole(PAUSER_ROLE) {
        _pause();
    }
    
    function unpause() external onlyRole(PAUSER_ROLE) {
        _unpause();
    }
    
    function transfer(address to, uint amount) external whenNotPaused {
        // Can only transfer when not paused
    }
}
```

## Gas Optimization

```solidity
// ❌ Expensive
string public name = "Token"; // Storage is expensive
uint256[] public array; // Dynamic arrays are expensive to iterate

// ✅ Cheaper
string public constant NAME = "Token"; // Constants are free
bytes32 public constant NAME_HASH = keccak256("Token");

// ❌ Multiple storage reads
function transfer(address to, uint amount) external {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount;
    balances[to] += amount;
}

// ✅ Cache storage in memory
function transfer(address to, uint amount) external {
    uint senderBalance = balances[msg.sender];
    require(senderBalance >= amount);
    unchecked {
        balances[msg.sender] = senderBalance - amount;
    }
    balances[to] += amount;
}

// ❌ Multiple SLOADs for same variable
function process() external {
    for (uint i = 0; i < items.length; i++) { // items.length read each iteration
        // ...
    }
}

// ✅ Cache length
function process() external {
    uint len = items.length;
    for (uint i = 0; i < len; i++) {
        // ...
    }
}

// ✅ Use unchecked for safe math
function increment() external {
    unchecked {
        counter++; // Safe if we know it won't overflow
    }
}
```

## Testing Patterns

### Foundry Tests

```solidity
// test/Token.t.sol
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../src/Token.sol";

contract TokenTest is Test {
    Token token;
    address alice = makeAddr("alice");
    address bob = makeAddr("bob");
    
    function setUp() public {
        token = new Token();
        token.mint(alice, 1000 ether);
    }
    
    function test_Transfer() public {
        vm.prank(alice);
        token.transfer(bob, 100 ether);
        
        assertEq(token.balanceOf(alice), 900 ether);
        assertEq(token.balanceOf(bob), 100 ether);
    }
    
    function test_RevertWhen_InsufficientBalance() public {
        vm.prank(alice);
        vm.expectRevert("Insufficient balance");
        token.transfer(bob, 2000 ether);
    }
    
    function testFuzz_Transfer(uint256 amount) public {
        vm.assume(amount <= token.balanceOf(alice));
        
        vm.prank(alice);
        token.transfer(bob, amount);
        
        assertEq(token.balanceOf(bob), amount);
    }
}
```

### Invariant Testing

```solidity
// test/invariants/TokenInvariant.t.sol
contract TokenInvariantTest is Test {
    Token token;
    Handler handler;
    
    function setUp() public {
        token = new Token();
        handler = new Handler(token);
        
        targetContract(address(handler));
    }
    
    function invariant_TotalSupplyEqualsSumOfBalances() public {
        uint256 totalSupply = token.totalSupply();
        uint256 sumOfBalances = handler.sumOfBalances();
        
        assertEq(totalSupply, sumOfBalances);
    }
}

contract Handler is Test {
    Token token;
    address[] public actors;
    
    constructor(Token _token) {
        token = _token;
    }
    
    function transfer(uint256 actorIndex, uint256 amount) public {
        // Bounded random actor
        address from = actors[actorIndex % actors.length];
        address to = actors[(actorIndex + 1) % actors.length];
        
        vm.prank(from);
        try token.transfer(to, amount) {} catch {}
    }
    
    function sumOfBalances() external view returns (uint256) {
        uint256 sum;
        for (uint i = 0; i < actors.length; i++) {
            sum += token.balanceOf(actors[i]);
        }
        return sum;
    }
}
```

## Upgrade Patterns

### UUPS Proxy

```solidity
import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";

contract TokenV1 is Initializable, UUPSUpgradeable {
    uint256 public value;
    
    /// @custom:oz-upgrades-unsafe-allow constructor
    constructor() {
        _disableInitializers();
    }
    
    function initialize() public initializer {
        __UUPSUpgradeable_init();
    }
    
    function _authorizeUpgrade(address) internal override onlyOwner {}
}
```

## When to Use

Apply this skill when:
- Writing new smart contracts
- Reviewing contract security
- Optimizing gas usage
- Writing tests
- Deploying contracts

