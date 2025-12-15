---
description: CI/CD and deployment expertise
triggers:
  - setting up ci
  - github actions
  - docker
  - deployment
  - kubernetes
---

# CI/CD Skill

## GitHub Actions Patterns

### Matrix Builds

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [18, 20, 22]
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
```

### Reusable Workflows

```yaml
# .github/workflows/deploy-reusable.yml
on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
    secrets:
      SSH_KEY:
        required: true

jobs:
  deploy:
    environment: ${{ inputs.environment }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        run: echo "Deploying to ${{ inputs.environment }}"
```

### Conditional Jobs

```yaml
jobs:
  deploy:
    if: github.ref == 'refs/heads/main'
    needs: [build, test]
```

## Docker Patterns

### Build Arguments

```dockerfile
ARG NODE_VERSION=20
FROM node:${NODE_VERSION}-alpine

ARG APP_VERSION
ENV APP_VERSION=${APP_VERSION}
```

### Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

### Layer Caching

```dockerfile
# Copy package files first (cache layer)
COPY package.json pnpm-lock.yaml ./
RUN pnpm install

# Then copy source (changes frequently)
COPY . .
RUN pnpm build
```

## Kubernetes Patterns

### Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: xala-pm
spec:
  replicas: 3
  selector:
    matchLabels:
      app: xala-pm
  template:
    spec:
      containers:
        - name: web
          image: ghcr.io/xalatechnologies/xala-pm:latest
          ports:
            - containerPort: 3000
          resources:
            requests:
              memory: "128Mi"
              cpu: "100m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
          readinessProbe:
            httpGet:
              path: /ready
              port: 3000
```

## When to Use

Apply when:
- Setting up CI/CD pipelines
- Creating Docker configurations
- Deploying applications
- Infrastructure automation

