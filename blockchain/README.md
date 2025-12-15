# Blockchain Expert Plugin

Comprehensive blockchain development agent covering Web3, validators, smart contracts, security, and infrastructure.

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/contract create` | Create new smart contracts (ERC-20, NFT, governance, security tokens) |
| `/contract analyze` | Analyze contract for issues |
| `/contract deploy` | Deploy contract to network |
| `/audit` | Perform security audit on smart contracts |
| `/validator setup` | Set up blockchain validator |
| `/validator status` | Check validator health and metrics |
| `/validator monitor` | Monitor validator performance |
| `/web3 connect` | Connect to blockchain network |
| `/web3 call` | Call contract methods |
| `/web3 sign` | Sign messages and transactions |

### Agent

Expert blockchain engineer with deep knowledge of:
- Ethereum and EVM chains
- PoSA consensus mechanisms
- Solidity smart contracts
- Web3 development (ethers.js, viem)
- Security auditing
- AWS/Ansible infrastructure
- Go for node development

### Skills

| Skill | Expertise |
|-------|-----------|
| **Web3** | Provider setup, contract interaction, transactions, events |
| **Smart Contracts** | Solidity patterns, security, testing, deployment |
| **Infrastructure** | AWS, Terraform, Ansible, monitoring |
| **Security** | Vulnerability detection, audit, secure patterns |

### Hooks

- Check Solidity files for security issues
- Audit changes to smart contracts
- Verify Terraform security best practices
- Review Ansible playbook security

### MCP Integration

- Ethereum RPC interaction
- Foundry testing and deployment
- Slither static analysis
- Etherscan verification

## Security Token Compliance

⚠️ **Critical Rules for Security Tokens (PM-EQ, NV-EQ):**

```
🚫 NEVER allow:
├── Public trading
├── DEX/CEX integration
├── KYC bypass
└── Direct FIAT handling

✅ ALWAYS include:
├── Pause mechanism
├── Whitelist verification
├── KYC verification
└── Complete audit trail
```

## Usage Examples

### Create Security Token

```bash
/contract create SecurityToken type=security
```

### Audit Contract

```bash
/audit path=contracts/Token.sol severity=high
```

### Setup Validator

```bash
/validator setup network=testnet consensus=posa
```

### Monitor Validator

```bash
/validator status
```

## Installation

```bash
/plugin install blockchain@xalapm-marketplace
```

## Technology Stack

- **Smart Contracts**: Solidity 0.8+, OpenZeppelin
- **Testing**: Foundry (Forge, Cast, Anvil)
- **Web3**: ethers.js, viem
- **Node**: Go (geth fork)
- **Infrastructure**: AWS, Terraform, Ansible
- **Monitoring**: Prometheus, Grafana

