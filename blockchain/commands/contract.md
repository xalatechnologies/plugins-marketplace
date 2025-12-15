---
description: Create, analyze, or audit smart contracts
arguments:
  - name: action
    description: Action (create, analyze, audit, deploy)
    required: true
  - name: name
    description: Contract name or file path
    required: false
  - name: type
    description: Contract type (token, nft, governance, staking, custom)
    required: false
---

# Smart Contract Command

Create, analyze, audit, or deploy smart contracts.

## Create Contract (`/contract create`)

```bash
/contract create TokenContract type=token
/contract create NFTMarketplace type=nft
/contract create GovernanceDAO type=governance
```

### ERC-20 Token Template

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";

/**
 * @title {Name}Token
 * @dev ERC-20 token with pausable, burnable, and access control features
 * @custom:security-contact security@xalatechnologies.com
 */
contract {Name}Token is ERC20, ERC20Burnable, ERC20Pausable, AccessControl, ERC20Permit {
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");

    constructor(address defaultAdmin, address pauser, address minter)
        ERC20("{Name}", "{SYMBOL}")
        ERC20Permit("{Name}")
    {
        _grantRole(DEFAULT_ADMIN_ROLE, defaultAdmin);
        _grantRole(PAUSER_ROLE, pauser);
        _grantRole(MINTER_ROLE, minter);
    }

    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }

    function unpause() public onlyRole(PAUSER_ROLE) {
        _unpause();
    }

    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        _mint(to, amount);
    }

    // Required overrides
    function _update(address from, address to, uint256 value)
        internal
        override(ERC20, ERC20Pausable)
    {
        super._update(from, to, value);
    }
}
```

### Security Token Template (for PM-EQ, NV-EQ)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

/**
 * @title SecurityToken
 * @dev Security token with mandatory KYC, whitelist, and compliance features
 * @notice This token is NOT tradeable on public exchanges
 * @custom:security-contact security@xalatechnologies.com
 */
contract SecurityToken is ERC20, ERC20Pausable, AccessControl {
    bytes32 public constant COMPLIANCE_ROLE = keccak256("COMPLIANCE_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    
    // Whitelist for KYC-verified addresses
    mapping(address => bool) private _whitelisted;
    mapping(address => bool) private _kycVerified;
    
    // Transfer restrictions
    bool public transfersEnabled = false; // NEVER enable for public trading
    
    event AddressWhitelisted(address indexed account);
    event AddressRemovedFromWhitelist(address indexed account);
    event KYCVerified(address indexed account);
    event KYCRevoked(address indexed account);
    
    error NotWhitelisted(address account);
    error KYCNotVerified(address account);
    error PublicTradingNotAllowed();
    
    constructor(address admin, address compliance)
        ERC20("Security Token", "SEC")
    {
        _grantRole(DEFAULT_ADMIN_ROLE, admin);
        _grantRole(COMPLIANCE_ROLE, compliance);
        _grantRole(PAUSER_ROLE, admin);
    }
    
    /**
     * @dev Whitelist an address after KYC verification
     */
    function whitelist(address account) external onlyRole(COMPLIANCE_ROLE) {
        _whitelisted[account] = true;
        emit AddressWhitelisted(account);
    }
    
    /**
     * @dev Remove address from whitelist
     */
    function removeFromWhitelist(address account) external onlyRole(COMPLIANCE_ROLE) {
        _whitelisted[account] = false;
        emit AddressRemovedFromWhitelist(account);
    }
    
    /**
     * @dev Mark address as KYC verified
     */
    function verifyKYC(address account) external onlyRole(COMPLIANCE_ROLE) {
        _kycVerified[account] = true;
        emit KYCVerified(account);
    }
    
    /**
     * @dev Revoke KYC verification
     */
    function revokeKYC(address account) external onlyRole(COMPLIANCE_ROLE) {
        _kycVerified[account] = false;
        emit KYCRevoked(account);
    }
    
    function isWhitelisted(address account) public view returns (bool) {
        return _whitelisted[account];
    }
    
    function isKYCVerified(address account) public view returns (bool) {
        return _kycVerified[account];
    }
    
    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }
    
    function unpause() public onlyRole(PAUSER_ROLE) {
        _unpause();
    }
    
    /**
     * @dev Override transfer to enforce compliance
     */
    function _update(address from, address to, uint256 value)
        internal
        override(ERC20, ERC20Pausable)
    {
        // Skip checks for minting
        if (from != address(0)) {
            if (!_whitelisted[from]) revert NotWhitelisted(from);
            if (!_kycVerified[from]) revert KYCNotVerified(from);
        }
        
        // Skip checks for burning
        if (to != address(0)) {
            if (!_whitelisted[to]) revert NotWhitelisted(to);
            if (!_kycVerified[to]) revert KYCNotVerified(to);
        }
        
        super._update(from, to, value);
    }
}
```

## Analyze Contract (`/contract analyze`)

```bash
/contract analyze path=contracts/Token.sol
```

**Analysis includes:**
- Code quality and patterns
- Gas optimization opportunities
- Reentrancy risks
- Access control review
- Upgrade safety (if proxy)

## Audit Contract (`/contract audit`)

```bash
/contract audit path=contracts/Token.sol severity=all
```

See `/audit` command for full security audit.

## Deploy Contract (`/contract deploy`)

```bash
/contract deploy Token network=sepolia
/contract deploy Token network=mainnet verify=true
```

**Deployment checklist:**
- [ ] All tests passing
- [ ] Security audit complete
- [ ] Gas estimates acceptable
- [ ] Constructor args verified
- [ ] Network configured
- [ ] Etherscan verification ready

## Guidelines

1. **Always use OpenZeppelin** for standard implementations
2. **Follow CEI pattern** (Checks-Effects-Interactions)
3. **Use custom errors** instead of require strings
4. **Add NatSpec comments** for all public functions
5. **Include security contact** in contract header
6. **Test thoroughly** before deployment

