---
description: Manage blockchain validators and nodes
arguments:
  - name: action
    description: Action (setup, status, monitor, rotate, stake)
    required: true
  - name: network
    description: Network (mainnet, testnet, local)
    required: false
    default: testnet
---

# Validator Management Command

Set up, monitor, and manage blockchain validators.

## Setup Validator (`/validator setup`)

```bash
/validator setup network=testnet
/validator setup network=mainnet consensus=posa
```

### PoSA Validator Setup (Go/Geth)

```go
// validator/config.go
package validator

import (
    "github.com/ethereum/go-ethereum/common"
    "github.com/ethereum/go-ethereum/consensus/clique"
)

type ValidatorConfig struct {
    // Network configuration
    NetworkID   uint64
    ChainID     uint64
    GenesisHash common.Hash
    
    // Validator identity
    ValidatorAddress common.Address
    SignerKey       *ecdsa.PrivateKey
    
    // Consensus parameters
    BlockPeriod     uint64 // seconds between blocks
    Epoch           uint64 // blocks per epoch
    
    // P2P configuration
    ListenAddr      string
    MaxPeers        int
    BootNodes       []string
    
    // RPC configuration
    HTTPHost        string
    HTTPPort        int
    WSHost          string
    WSPort          int
}

func DefaultTestnetConfig() *ValidatorConfig {
    return &ValidatorConfig{
        NetworkID:   421614,
        ChainID:     421614,
        BlockPeriod: 3,
        Epoch:       30000,
        ListenAddr:  ":30303",
        MaxPeers:    50,
        HTTPPort:    8545,
        WSPort:      8546,
    }
}
```

### Ansible Playbook for Validator Deployment

```yaml
# ansible/playbooks/validator.yml
---
- name: Deploy Blockchain Validator
  hosts: validators
  become: yes
  vars:
    geth_version: "1.13.5"
    data_dir: "/data/geth"
    network_id: 421614
    
  tasks:
    - name: Install dependencies
      apt:
        name:
          - build-essential
          - golang-go
          - git
        state: present
        update_cache: yes
        
    - name: Create geth user
      user:
        name: geth
        system: yes
        shell: /bin/false
        home: "{{ data_dir }}"
        
    - name: Download and install Geth
      get_url:
        url: "https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-{{ geth_version }}.tar.gz"
        dest: /tmp/geth.tar.gz
        
    - name: Extract Geth
      unarchive:
        src: /tmp/geth.tar.gz
        dest: /usr/local/bin
        remote_src: yes
        extra_opts: [--strip-components=1]
        
    - name: Copy genesis file
      copy:
        src: files/genesis.json
        dest: "{{ data_dir }}/genesis.json"
        owner: geth
        group: geth
        
    - name: Initialize genesis
      command: >
        geth --datadir {{ data_dir }} init {{ data_dir }}/genesis.json
      become_user: geth
      args:
        creates: "{{ data_dir }}/geth/chaindata"
        
    - name: Copy validator keystore
      copy:
        src: "files/keystore/{{ inventory_hostname }}"
        dest: "{{ data_dir }}/keystore/"
        owner: geth
        group: geth
        mode: '0600'
        
    - name: Create systemd service
      template:
        src: templates/geth.service.j2
        dest: /etc/systemd/system/geth.service
        
    - name: Start and enable geth
      systemd:
        name: geth
        state: started
        enabled: yes
        daemon_reload: yes
```

### Systemd Service Template

```ini
# ansible/templates/geth.service.j2
[Unit]
Description=Geth Validator Node
After=network.target

[Service]
Type=simple
User=geth
Group=geth
Restart=always
RestartSec=5
ExecStart=/usr/local/bin/geth \
    --datadir {{ data_dir }} \
    --networkid {{ network_id }} \
    --syncmode full \
    --gcmode archive \
    --mine \
    --miner.etherbase {{ validator_address }} \
    --unlock {{ validator_address }} \
    --password {{ data_dir }}/password.txt \
    --allow-insecure-unlock \
    --http \
    --http.addr 127.0.0.1 \
    --http.port 8545 \
    --http.api eth,net,web3,txpool \
    --ws \
    --ws.addr 127.0.0.1 \
    --ws.port 8546 \
    --ws.api eth,net,web3 \
    --metrics \
    --metrics.addr 127.0.0.1 \
    --metrics.port 6060 \
    --verbosity 3

[Install]
WantedBy=multi-user.target
```

## AWS Infrastructure

### Terraform for Validator Infrastructure

```hcl
# terraform/validator.tf
provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "validator" {
  count         = var.validator_count
  ami           = var.ami_id
  instance_type = "m5.xlarge"
  
  vpc_security_group_ids = [aws_security_group.validator.id]
  subnet_id              = aws_subnet.private[count.index % length(aws_subnet.private)].id
  
  root_block_device {
    volume_size = 500
    volume_type = "gp3"
    iops        = 3000
    throughput  = 125
    encrypted   = true
  }
  
  tags = {
    Name        = "validator-${count.index + 1}"
    Environment = var.environment
    Role        = "validator"
  }
}

resource "aws_security_group" "validator" {
  name        = "validator-sg"
  description = "Security group for blockchain validators"
  vpc_id      = aws_vpc.main.id
  
  # P2P
  ingress {
    from_port   = 30303
    to_port     = 30303
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 30303
    to_port     = 30303
    protocol    = "udp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  # Internal RPC (from bastion only)
  ingress {
    from_port       = 8545
    to_port         = 8546
    protocol        = "tcp"
    security_groups = [aws_security_group.bastion.id]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

## Monitor Validator (`/validator status`)

```
📊 VALIDATOR STATUS
═══════════════════════════════════════════════════════════════

Network: NorChain Testnet (421614)
Node: validator-1.norchain.org

HEALTH
──────────────────────────────────────────────────────────────
Status:         🟢 Healthy
Synced:         ✅ Yes (block 12,456,789)
Peers:          23/50
Uptime:         14d 6h 32m

CONSENSUS
──────────────────────────────────────────────────────────────
Role:           Active Validator
Blocks Mined:   1,234 (last 24h)
Miss Rate:      0.2%
Next Turn:      ~45 seconds

STAKING
──────────────────────────────────────────────────────────────
Self-Stake:     100,000 NOR
Delegated:      450,000 NOR
Total Stake:    550,000 NOR
Rank:           #3 / 21 validators

REWARDS
──────────────────────────────────────────────────────────────
Today:          +156.78 NOR
This Week:      +1,098.45 NOR
Total:          +45,678.90 NOR

RESOURCES
──────────────────────────────────────────────────────────────
CPU:            45%
Memory:         12.3 GB / 32 GB
Disk:           234 GB / 500 GB
Network:        ↓ 12 MB/s  ↑ 8 MB/s
```

## Guidelines

1. **Geographic distribution** - Spread validators across regions
2. **Key security** - Use HSM or secure key management
3. **Monitoring** - Set up 24/7 monitoring and alerts
4. **Backup** - Regular backups of chain data
5. **Updates** - Keep node software up to date

