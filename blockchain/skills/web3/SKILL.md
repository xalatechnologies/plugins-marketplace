---
description: Web3 development expertise - ethers.js, viem, contract interaction, signing
triggers:
  - working with ethereum
  - connecting to blockchain
  - calling smart contracts
  - signing messages
  - web3 development
---

# Web3 Development Skill

Expert Web3 development capabilities for blockchain interaction.

## Provider Setup Patterns

### Multi-chain Support

```typescript
import { ethers } from 'ethers'

const CHAINS = {
  ethereum: {
    chainId: 1,
    rpc: 'https://eth.llamarpc.com',
  },
  polygon: {
    chainId: 137,
    rpc: 'https://polygon-rpc.com',
  },
  norchain: {
    chainId: 42161,
    rpc: 'https://rpc.norchain.org',
  },
}

function getProvider(chain: keyof typeof CHAINS) {
  const config = CHAINS[chain]
  return new ethers.JsonRpcProvider(config.rpc, config.chainId)
}
```

### Retry Logic

```typescript
async function withRetry<T>(
  fn: () => Promise<T>,
  maxRetries = 3,
  delay = 1000
): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn()
    } catch (error) {
      if (i === maxRetries - 1) throw error
      await new Promise(r => setTimeout(r, delay * (i + 1)))
    }
  }
  throw new Error('Max retries exceeded')
}

// Usage
const balance = await withRetry(() => provider.getBalance(address))
```

## Contract Interaction Patterns

### Type-Safe Contract Wrapper

```typescript
import { ethers } from 'ethers'
import type { TypedContract } from './types'

class TokenContract {
  private contract: ethers.Contract
  
  constructor(address: string, signerOrProvider: ethers.Signer | ethers.Provider) {
    this.contract = new ethers.Contract(address, ERC20_ABI, signerOrProvider)
  }
  
  async balanceOf(account: string): Promise<bigint> {
    return this.contract.balanceOf(account)
  }
  
  async transfer(to: string, amount: bigint): Promise<ethers.TransactionResponse> {
    return this.contract.transfer(to, amount)
  }
  
  async approve(spender: string, amount: bigint): Promise<ethers.TransactionResponse> {
    return this.contract.approve(spender, amount)
  }
}
```

### Multicall Pattern

```typescript
import { ethers } from 'ethers'

const MULTICALL_ABI = [
  'function aggregate(tuple(address target, bytes callData)[] calls) view returns (uint256 blockNumber, bytes[] returnData)',
]

async function multicall(
  provider: ethers.Provider,
  calls: Array<{ target: string; callData: string }>
): Promise<string[]> {
  const multicall = new ethers.Contract(
    MULTICALL_ADDRESS,
    MULTICALL_ABI,
    provider
  )
  
  const [, returnData] = await multicall.aggregate(calls)
  return returnData
}

// Usage: batch multiple balance calls
const balanceCalls = addresses.map(addr => ({
  target: tokenAddress,
  callData: iface.encodeFunctionData('balanceOf', [addr]),
}))

const results = await multicall(provider, balanceCalls)
const balances = results.map(data => 
  iface.decodeFunctionResult('balanceOf', data)[0]
)
```

## Transaction Management

### Gas Estimation with Buffer

```typescript
async function sendTransaction(
  signer: ethers.Signer,
  tx: ethers.TransactionRequest,
  gasBuffer = 1.2 // 20% buffer
): Promise<ethers.TransactionResponse> {
  const gasEstimate = await signer.estimateGas(tx)
  tx.gasLimit = BigInt(Math.ceil(Number(gasEstimate) * gasBuffer))
  
  return signer.sendTransaction(tx)
}
```

### Transaction Replacement (Speed Up)

```typescript
async function speedUpTransaction(
  signer: ethers.Wallet,
  pendingTxHash: string,
  gasPriceMultiplier = 1.1
): Promise<ethers.TransactionResponse> {
  const pendingTx = await signer.provider!.getTransaction(pendingTxHash)
  if (!pendingTx) throw new Error('Transaction not found')
  
  const feeData = await signer.provider!.getFeeData()
  const newMaxFeePerGas = BigInt(
    Math.ceil(Number(feeData.maxFeePerGas || 0) * gasPriceMultiplier)
  )
  
  return signer.sendTransaction({
    to: pendingTx.to,
    data: pendingTx.data,
    value: pendingTx.value,
    nonce: pendingTx.nonce,
    gasLimit: pendingTx.gasLimit,
    maxFeePerGas: newMaxFeePerGas,
    maxPriorityFeePerGas: feeData.maxPriorityFeePerGas,
  })
}
```

## Event Handling

### Event Listener with Reconnection

```typescript
function listenToEvents(
  contract: ethers.Contract,
  eventName: string,
  callback: (...args: any[]) => void
) {
  contract.on(eventName, callback)
  
  // Reconnection logic
  contract.provider?.on('error', async () => {
    console.log('Provider error, reconnecting...')
    await new Promise(r => setTimeout(r, 5000))
    contract.on(eventName, callback)
  })
  
  return () => contract.off(eventName, callback)
}

// Usage
const unsubscribe = listenToEvents(
  tokenContract,
  'Transfer',
  (from, to, amount) => {
    console.log(`Transfer: ${from} -> ${to}: ${amount}`)
  }
)
```

### Historical Event Fetching

```typescript
async function getHistoricalEvents(
  contract: ethers.Contract,
  eventName: string,
  fromBlock: number,
  toBlock: number | 'latest',
  batchSize = 10000
): Promise<ethers.Log[]> {
  const allEvents: ethers.Log[] = []
  const latestBlock = toBlock === 'latest' 
    ? await contract.provider!.getBlockNumber()
    : toBlock
  
  for (let start = fromBlock; start <= latestBlock; start += batchSize) {
    const end = Math.min(start + batchSize - 1, latestBlock)
    const events = await contract.queryFilter(
      contract.filters[eventName](),
      start,
      end
    )
    allEvents.push(...events)
  }
  
  return allEvents
}
```

## When to Use

Apply this skill when:
- Connecting to blockchain networks
- Reading/writing to smart contracts
- Handling transactions
- Listening to events
- Building Web3 frontends

