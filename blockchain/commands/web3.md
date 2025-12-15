---
description: Web3 development utilities and patterns
arguments:
  - name: action
    description: Action (connect, call, sign, encode, decode)
    required: true
---

# Web3 Development Command

Web3 utilities for blockchain interaction.

## Connect (`/web3 connect`)

```bash
/web3 connect network=mainnet
/web3 connect rpc=https://rpc.norchain.org
```

### Ethers.js Connection

```typescript
// lib/web3/provider.ts
import { ethers } from 'ethers'

export type NetworkName = 'mainnet' | 'testnet' | 'local'

const NETWORKS: Record<NetworkName, { rpc: string; chainId: number }> = {
  mainnet: {
    rpc: 'https://rpc.norchain.org',
    chainId: 42161,
  },
  testnet: {
    rpc: 'https://testnet-rpc.norchain.org',
    chainId: 421614,
  },
  local: {
    rpc: 'http://localhost:8545',
    chainId: 31337,
  },
}

export function getProvider(network: NetworkName): ethers.JsonRpcProvider {
  const config = NETWORKS[network]
  return new ethers.JsonRpcProvider(config.rpc, config.chainId)
}

export function getWallet(
  privateKey: string,
  network: NetworkName
): ethers.Wallet {
  const provider = getProvider(network)
  return new ethers.Wallet(privateKey, provider)
}

// Browser wallet connection
export async function connectWallet(): Promise<ethers.BrowserProvider> {
  if (typeof window.ethereum === 'undefined') {
    throw new Error('No wallet found. Please install MetaMask.')
  }
  
  const provider = new ethers.BrowserProvider(window.ethereum)
  await provider.send('eth_requestAccounts', [])
  
  return provider
}
```

### Viem Connection (Alternative)

```typescript
// lib/web3/viem.ts
import { createPublicClient, createWalletClient, http } from 'viem'
import { privateKeyToAccount } from 'viem/accounts'
import { mainnet, sepolia } from 'viem/chains'

// Custom chain definition
export const norchain = {
  id: 42161,
  name: 'NorChain',
  network: 'norchain',
  nativeCurrency: {
    decimals: 18,
    name: 'NOR',
    symbol: 'NOR',
  },
  rpcUrls: {
    default: { http: ['https://rpc.norchain.org'] },
    public: { http: ['https://rpc.norchain.org'] },
  },
  blockExplorers: {
    default: { name: 'NorScan', url: 'https://scan.norchain.org' },
  },
} as const

export const publicClient = createPublicClient({
  chain: norchain,
  transport: http(),
})

export function getWalletClient(privateKey: `0x${string}`) {
  const account = privateKeyToAccount(privateKey)
  return createWalletClient({
    account,
    chain: norchain,
    transport: http(),
  })
}
```

## Call Contract (`/web3 call`)

```bash
/web3 call contract=0x... method=balanceOf args=["0x..."]
```

```typescript
// Contract interaction patterns
import { ethers } from 'ethers'

// ABI for ERC-20
const ERC20_ABI = [
  'function name() view returns (string)',
  'function symbol() view returns (string)',
  'function decimals() view returns (uint8)',
  'function totalSupply() view returns (uint256)',
  'function balanceOf(address) view returns (uint256)',
  'function transfer(address to, uint256 amount) returns (bool)',
  'function approve(address spender, uint256 amount) returns (bool)',
  'function allowance(address owner, address spender) view returns (uint256)',
  'event Transfer(address indexed from, address indexed to, uint256 value)',
  'event Approval(address indexed owner, address indexed spender, uint256 value)',
]

async function getTokenBalance(
  tokenAddress: string,
  walletAddress: string,
  provider: ethers.Provider
): Promise<bigint> {
  const contract = new ethers.Contract(tokenAddress, ERC20_ABI, provider)
  return contract.balanceOf(walletAddress)
}

async function transferTokens(
  tokenAddress: string,
  to: string,
  amount: bigint,
  signer: ethers.Signer
): Promise<ethers.TransactionResponse> {
  const contract = new ethers.Contract(tokenAddress, ERC20_ABI, signer)
  return contract.transfer(to, amount)
}
```

## Sign Message (`/web3 sign`)

```bash
/web3 sign message="Hello, World!"
/web3 sign typed=true domain=... types=... value=...
```

```typescript
// Message signing
async function signMessage(
  signer: ethers.Signer,
  message: string
): Promise<string> {
  return signer.signMessage(message)
}

// EIP-712 Typed Data Signing
async function signTypedData(
  signer: ethers.Signer,
  domain: ethers.TypedDataDomain,
  types: Record<string, ethers.TypedDataField[]>,
  value: Record<string, any>
): Promise<string> {
  return signer.signTypedData(domain, types, value)
}

// Example: Sign permit (EIP-2612)
const domain = {
  name: 'NOR Token',
  version: '1',
  chainId: 42161,
  verifyingContract: '0x...',
}

const types = {
  Permit: [
    { name: 'owner', type: 'address' },
    { name: 'spender', type: 'address' },
    { name: 'value', type: 'uint256' },
    { name: 'nonce', type: 'uint256' },
    { name: 'deadline', type: 'uint256' },
  ],
}

const value = {
  owner: '0x...',
  spender: '0x...',
  value: ethers.parseEther('100'),
  nonce: 0,
  deadline: Math.floor(Date.now() / 1000) + 3600,
}

const signature = await signer.signTypedData(domain, types, value)
```

## Encode/Decode (`/web3 encode`, `/web3 decode`)

```typescript
// ABI encoding/decoding
const iface = new ethers.Interface(ERC20_ABI)

// Encode function call
const calldata = iface.encodeFunctionData('transfer', [
  '0x...',
  ethers.parseEther('100'),
])

// Decode function call
const decoded = iface.decodeFunctionData('transfer', calldata)

// Encode constructor
const bytecode = '0x...'
const constructorArgs = iface.encodeDeploy([arg1, arg2])
const deployData = bytecode + constructorArgs.slice(2)

// Decode event logs
const log = { topics: [...], data: '0x...' }
const event = iface.parseLog(log)
```

## Gas Estimation

```typescript
// Estimate gas for transaction
async function estimateGas(
  contract: ethers.Contract,
  method: string,
  args: any[]
): Promise<{
  gasLimit: bigint
  gasPrice: bigint
  maxFeePerGas: bigint
  maxPriorityFeePerGas: bigint
  estimatedCost: bigint
}> {
  const provider = contract.runner?.provider
  if (!provider) throw new Error('No provider')
  
  const gasLimit = await contract[method].estimateGas(...args)
  const feeData = await provider.getFeeData()
  
  const estimatedCost = gasLimit * (feeData.maxFeePerGas || feeData.gasPrice || 0n)
  
  return {
    gasLimit,
    gasPrice: feeData.gasPrice || 0n,
    maxFeePerGas: feeData.maxFeePerGas || 0n,
    maxPriorityFeePerGas: feeData.maxPriorityFeePerGas || 0n,
    estimatedCost,
  }
}
```

## Guidelines

1. **Never expose private keys** in code
2. **Use environment variables** for sensitive data
3. **Validate addresses** before transactions
4. **Estimate gas** before sending transactions
5. **Handle errors gracefully** (revert reasons)
6. **Use typed contracts** when possible

