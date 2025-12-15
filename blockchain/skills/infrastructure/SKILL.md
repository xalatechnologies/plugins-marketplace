---
description: Blockchain infrastructure expertise - AWS, Ansible, Terraform, node operations
triggers:
  - setting up validators
  - deploying nodes
  - aws infrastructure
  - ansible playbooks
  - terraform configuration
---

# Blockchain Infrastructure Skill

Expert blockchain infrastructure and DevOps capabilities.

## AWS Architecture

### High Availability Validator Setup

```
┌─────────────────────────────────────────────────────────────┐
│                         AWS Region                          │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │      AZ-1       │  │      AZ-2       │                   │
│  │  ┌───────────┐  │  │  ┌───────────┐  │                   │
│  │  │Validator 1│  │  │  │Validator 2│  │                   │
│  │  └───────────┘  │  │  └───────────┘  │                   │
│  │                 │  │                 │                   │
│  │  ┌───────────┐  │  │  ┌───────────┐  │                   │
│  │  │  RPC Node │  │  │  │  RPC Node │  │                   │
│  │  └───────────┘  │  │  └───────────┘  │                   │
│  └─────────────────┘  └─────────────────┘                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                  Application Load Balancer          │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                    CloudWatch                        │    │
│  │           (Monitoring & Alerting)                   │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### Terraform Module

```hcl
# modules/validator/main.tf
variable "environment" {
  type = string
}

variable "validator_count" {
  type    = number
  default = 2
}

variable "instance_type" {
  type    = string
  default = "m5.xlarge"
}

resource "aws_instance" "validator" {
  count         = var.validator_count
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  
  subnet_id              = aws_subnet.private[count.index % 2].id
  vpc_security_group_ids = [aws_security_group.validator.id]
  iam_instance_profile   = aws_iam_instance_profile.validator.name
  
  root_block_device {
    volume_size = 500
    volume_type = "gp3"
    iops        = 3000
    encrypted   = true
    kms_key_id  = aws_kms_key.validator.arn
  }
  
  metadata_options {
    http_tokens = "required" # IMDSv2
  }
  
  tags = {
    Name        = "${var.environment}-validator-${count.index + 1}"
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_security_group" "validator" {
  name        = "${var.environment}-validator-sg"
  description = "Validator security group"
  vpc_id      = aws_vpc.main.id
  
  # P2P
  ingress {
    from_port   = 30303
    to_port     = 30303
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "P2P TCP"
  }
  
  ingress {
    from_port   = 30303
    to_port     = 30303
    protocol    = "udp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "P2P UDP"
  }
  
  # No direct RPC access from internet
  # RPC only accessible via internal ALB
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${var.environment}-validator-sg"
  }
}

# CloudWatch Alarms
resource "aws_cloudwatch_metric_alarm" "validator_cpu" {
  count               = var.validator_count
  alarm_name          = "${var.environment}-validator-${count.index + 1}-cpu"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Validator CPU > 80%"
  
  dimensions = {
    InstanceId = aws_instance.validator[count.index].id
  }
  
  alarm_actions = [aws_sns_topic.alerts.arn]
}
```

## Ansible Automation

### Validator Playbook

```yaml
# ansible/playbooks/validator.yml
---
- name: Deploy Blockchain Validator
  hosts: validators
  become: yes
  vars:
    geth_version: "1.13.5"
    data_dir: "/data/geth"
    
  roles:
    - role: common
    - role: security_hardening
    - role: geth
    - role: monitoring
    
  tasks:
    - name: Verify validator is synced
      uri:
        url: "http://localhost:8545"
        method: POST
        body: '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'
        body_format: json
      register: sync_status
      until: sync_status.json.result == false
      retries: 100
      delay: 60
```

### Security Hardening Role

```yaml
# ansible/roles/security_hardening/tasks/main.yml
---
- name: Update system packages
  apt:
    upgrade: dist
    update_cache: yes
    
- name: Install security tools
  apt:
    name:
      - fail2ban
      - ufw
      - unattended-upgrades
    state: present
    
- name: Configure UFW defaults
  ufw:
    direction: incoming
    policy: deny
    
- name: Allow SSH
  ufw:
    rule: allow
    port: 22
    proto: tcp
    
- name: Allow P2P
  ufw:
    rule: allow
    port: 30303
    
- name: Enable UFW
  ufw:
    state: enabled
    
- name: Disable root SSH
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^PermitRootLogin'
    line: 'PermitRootLogin no'
  notify: Restart SSH
  
- name: Enable fail2ban
  service:
    name: fail2ban
    state: started
    enabled: yes
```

## Monitoring Stack

### Prometheus + Grafana

```yaml
# docker-compose.monitoring.yml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
      
  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}
      
  node_exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"

volumes:
  prometheus_data:
  grafana_data:
```

### Prometheus Config

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  
scrape_configs:
  - job_name: 'geth'
    static_configs:
      - targets:
          - 'validator-1:6060'
          - 'validator-2:6060'
    metrics_path: /debug/metrics/prometheus
    
  - job_name: 'node'
    static_configs:
      - targets:
          - 'validator-1:9100'
          - 'validator-2:9100'

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']
```

## When to Use

Apply this skill when:
- Setting up validator infrastructure
- Deploying blockchain nodes
- Configuring AWS resources
- Writing Ansible playbooks
- Setting up monitoring

