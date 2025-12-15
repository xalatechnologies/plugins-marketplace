---
description: NSM/Digdir security standards expertise
triggers:
  - implementing authentication
  - handling sensitive data
  - setting up logging
  - configuring security
  - norwegian public sector
---

# Norwegian Security Standards Skill

Expert NSM Grunnprinsipper and Digdir compliance.

## Authentication Patterns

### MFA Implementation
```typescript
// Required for sensitive systems per NSM
import speakeasy from 'speakeasy'

// Generate TOTP secret
function generateMFASecret(userId: string): MFASecret {
  const secret = speakeasy.generateSecret({
    name: `MyApp (${userId})`,
    issuer: 'MyApp',
  })
  
  return {
    secret: secret.base32,
    qrCodeUrl: secret.otpauth_url,
  }
}

// Verify TOTP code
function verifyMFACode(secret: string, code: string): boolean {
  return speakeasy.totp.verify({
    secret,
    encoding: 'base32',
    token: code,
    window: 1, // Allow 30 seconds drift
  })
}
```

### Session Security
```typescript
// Secure session configuration
const sessionConfig = {
  name: '__session',
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'lax' as const,
  maxAge: 8 * 60 * 60, // 8 hours
  path: '/',
}

// Session with security attributes
interface SecureSession {
  userId: string
  createdAt: Date
  expiresAt: Date
  ipAddress: string
  userAgent: string
  mfaVerified: boolean
}
```

## Logging Requirements

### Security Event Logging (12 months retention)
```typescript
interface SecurityLog {
  id: string
  timestamp: Date
  eventType: SecurityEventType
  severity: 'info' | 'warning' | 'error' | 'critical'
  userId?: string
  ipAddress: string
  userAgent?: string
  action: string
  resource: string
  result: 'success' | 'failure'
  details: Record<string, unknown>
  // Integrity verification
  previousHash?: string
  hash: string
}

type SecurityEventType =
  | 'authentication'
  | 'authorization'
  | 'data_access'
  | 'data_modification'
  | 'admin_action'
  | 'security_alert'

async function logSecurityEvent(event: Omit<SecurityLog, 'id' | 'hash'>): Promise<void> {
  // Get previous log hash for chain integrity
  const lastLog = await db.securityLogs.findFirst({
    orderBy: { timestamp: 'desc' }
  })
  
  const logEntry = {
    ...event,
    id: generateId(),
    previousHash: lastLog?.hash,
    hash: '', // Will be computed
  }
  
  // Compute hash for integrity
  logEntry.hash = computeHash(logEntry)
  
  await db.securityLogs.create({ data: logEntry })
  
  // Alert on critical events
  if (event.severity === 'critical') {
    await alertSecurityTeam(logEntry)
  }
}
```

### Required Log Events
```typescript
// Authentication events
await logSecurityEvent({
  eventType: 'authentication',
  severity: 'info',
  action: 'login',
  result: success ? 'success' : 'failure',
  ...
})

// Admin actions
await logSecurityEvent({
  eventType: 'admin_action',
  severity: 'warning',
  action: 'user_role_change',
  details: { oldRole, newRole },
  ...
})

// Data access
await logSecurityEvent({
  eventType: 'data_access',
  severity: 'info',
  action: 'export_user_data',
  resource: `user:${userId}`,
  ...
})
```

## Encryption Standards

### At Rest (AES-256)
```typescript
import { createCipheriv, createDecipheriv, randomBytes } from 'crypto'

const ALGORITHM = 'aes-256-gcm'

function encrypt(plaintext: string, key: Buffer): EncryptedData {
  const iv = randomBytes(16)
  const cipher = createCipheriv(ALGORITHM, key, iv)
  
  let encrypted = cipher.update(plaintext, 'utf8', 'hex')
  encrypted += cipher.final('hex')
  
  return {
    ciphertext: encrypted,
    iv: iv.toString('hex'),
    authTag: cipher.getAuthTag().toString('hex'),
  }
}

function decrypt(data: EncryptedData, key: Buffer): string {
  const decipher = createDecipheriv(
    ALGORITHM,
    key,
    Buffer.from(data.iv, 'hex')
  )
  decipher.setAuthTag(Buffer.from(data.authTag, 'hex'))
  
  let decrypted = decipher.update(data.ciphertext, 'hex', 'utf8')
  decrypted += decipher.final('utf8')
  
  return decrypted
}
```

### In Transit (TLS 1.3)
```typescript
// Security headers middleware
app.use((req, res, next) => {
  // HSTS - force HTTPS
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains; preload')
  
  // Prevent clickjacking
  res.setHeader('X-Frame-Options', 'DENY')
  
  // Content Security Policy
  res.setHeader('Content-Security-Policy', "default-src 'self'")
  
  // Prevent MIME sniffing
  res.setHeader('X-Content-Type-Options', 'nosniff')
  
  next()
})
```

## Digdir Integration

### ID-porten (for public sector)
```typescript
// ID-porten OAuth2 configuration
const idportenConfig = {
  issuer: 'https://idporten.no',
  clientId: process.env.IDPORTEN_CLIENT_ID,
  clientSecret: process.env.IDPORTEN_CLIENT_SECRET,
  redirectUri: `${process.env.APP_URL}/auth/callback`,
  scope: 'openid profile',
  // Security level
  acrValues: 'idporten-loa-substantial', // or 'high'
}
```

## When to Use

Apply automatically when:
- Implementing authentication
- Building admin functionality
- Handling sensitive data
- Setting up logging
- Integrating with Norwegian public services

