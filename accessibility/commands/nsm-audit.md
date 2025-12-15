---
description: NSM (Nasjonal Sikkerhetsmyndighet) security audit and Digdir compliance
arguments:
  - name: framework
    description: Framework (nsm-grunnprinsipper, digdir-sikkerhet, both)
    required: false
    default: both
---

# NSM & Digdir Security Audit Command

Audit against Norwegian security standards from NSM and Digdir.

## NSM Grunnprinsipper for IKT-sikkerhet

### 1. Identifisere og kartlegge

```typescript
// Asset inventory
interface SystemAsset {
  id: string
  name: string
  type: 'application' | 'database' | 'server' | 'network'
  classification: 'public' | 'internal' | 'confidential' | 'secret'
  owner: string
  dependencies: string[]
  dataTypes: DataType[]
}

// Data classification
type DataType = {
  name: string
  sensitivity: 'low' | 'medium' | 'high' | 'critical'
  personalData: boolean
  retention: string
}
```

### 2. Beskytte og opprettholde

#### Access Control
```typescript
// Role-based access control
const ROLES = {
  admin: ['read', 'write', 'delete', 'admin'],
  editor: ['read', 'write'],
  viewer: ['read'],
} as const

// Principle of least privilege
function checkAccess(user: User, action: string, resource: Resource): boolean {
  const userPermissions = ROLES[user.role] || []
  const required = resource.requiredPermissions[action]
  return required.every(p => userPermissions.includes(p))
}
```

#### Encryption
```typescript
// Data at rest
import { createCipheriv, createDecipheriv, randomBytes } from 'crypto'

function encrypt(data: string, key: Buffer): EncryptedData {
  const iv = randomBytes(16)
  const cipher = createCipheriv('aes-256-gcm', key, iv)
  let encrypted = cipher.update(data, 'utf8', 'hex')
  encrypted += cipher.final('hex')
  return {
    encrypted,
    iv: iv.toString('hex'),
    tag: cipher.getAuthTag().toString('hex'),
  }
}

// Data in transit - require TLS 1.3
// HSTS header required
app.use((req, res, next) => {
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
  next()
})
```

#### Authentication
```typescript
// Multi-factor authentication
async function authenticate(credentials: Credentials): Promise<AuthResult> {
  // Step 1: Password verification
  const user = await verifyPassword(credentials.email, credentials.password)
  if (!user) throw new AuthError('Invalid credentials')
  
  // Step 2: MFA verification (required for sensitive systems)
  if (user.mfaEnabled) {
    const mfaValid = await verifyMFA(user.id, credentials.mfaCode)
    if (!mfaValid) throw new AuthError('Invalid MFA code')
  }
  
  // Step 3: Session creation with security attributes
  return createSession(user, {
    ipAddress: credentials.ipAddress,
    userAgent: credentials.userAgent,
    expiresIn: '8h',
  })
}
```

### 3. Oppdage

#### Logging and Monitoring
```typescript
// Security event logging
interface SecurityEvent {
  timestamp: Date
  eventType: 'auth' | 'access' | 'admin' | 'error' | 'threat'
  severity: 'info' | 'warning' | 'error' | 'critical'
  userId?: string
  ipAddress: string
  action: string
  resource: string
  result: 'success' | 'failure'
  details: Record<string, unknown>
}

async function logSecurityEvent(event: SecurityEvent): Promise<void> {
  // Immutable audit log
  await auditLog.insert({
    ...event,
    timestamp: new Date(),
    // Hash for integrity verification
    hash: createHash('sha256')
      .update(JSON.stringify(event))
      .digest('hex'),
  })
  
  // Alert on critical events
  if (event.severity === 'critical') {
    await alertSecurityTeam(event)
  }
}

// Monitor for anomalies
async function detectAnomalies(): Promise<void> {
  // Failed login attempts
  const failedLogins = await getFailedLogins(last15Minutes)
  if (failedLogins > 10) {
    await alert('Brute force attack detected')
  }
  
  // Unusual access patterns
  const unusualAccess = await detectUnusualPatterns()
  if (unusualAccess.length > 0) {
    await alert('Unusual access patterns detected', unusualAccess)
  }
}
```

### 4. Håndtere og gjenopprette

```typescript
// Incident response
interface IncidentResponse {
  id: string
  detectedAt: Date
  severity: 'low' | 'medium' | 'high' | 'critical'
  type: 'breach' | 'dos' | 'malware' | 'unauthorized_access'
  status: 'detected' | 'contained' | 'eradicated' | 'recovered' | 'closed'
  affectedSystems: string[]
  actions: IncidentAction[]
}

// Backup and recovery
async function performBackup(): Promise<BackupResult> {
  const backup = await db.backup({
    encrypted: true,
    location: 's3://backups/',
    retention: '90d',
  })
  
  // Verify backup integrity
  const verified = await verifyBackup(backup.id)
  
  return { backup, verified }
}
```

## Digdir Security Requirements

### Sikkerhetskrav for offentlige tjenester

```typescript
// ID-porten integration (Norwegian public login)
import { IDPorten } from '@digdir/idporten-client'

const idporten = new IDPorten({
  clientId: process.env.IDPORTEN_CLIENT_ID,
  clientSecret: process.env.IDPORTEN_CLIENT_SECRET,
  redirectUri: process.env.IDPORTEN_REDIRECT_URI,
  // Security level
  acrValues: 'idporten-loa-substantial', // or 'high' for sensitive data
})

// Maskinporten for machine-to-machine
import { Maskinporten } from '@digdir/maskinporten-client'

const maskinporten = new Maskinporten({
  clientId: process.env.MASKINPORTEN_CLIENT_ID,
  scope: 'digdir:security-audit',
})
```

### Referansekatalogen Requirements

```yaml
# Security controls checklist
access_control:
  - authentication: required
  - authorization: role_based
  - session_management: secure
  - mfa: required_for_sensitive

data_protection:
  - encryption_at_rest: aes_256
  - encryption_in_transit: tls_1.3
  - key_management: hsm_backed
  
logging:
  - security_events: all
  - retention: 12_months
  - integrity: hash_verified
  
availability:
  - backup_frequency: daily
  - recovery_time: 4_hours
  - disaster_recovery: documented
```

## Audit Output Format

```
🛡️ NSM & DIGDIR SECURITY AUDIT
═══════════════════════════════════════════════════════════════

Framework: NSM Grunnprinsipper + Digdir Sikkerhet
Date: 2024-12-15

SUMMARY
───────────────────────────────────────────────────────────────
✅ Compliant:     28 controls
⚠️ Partial:       6 controls  
❌ Non-Compliant: 4 controls

NSM GRUNNPRINSIPPER
───────────────────────────────────────────────────────────────

1. Identifisere og kartlegge
   ✅ Asset inventory documented
   ⚠️ Data classification incomplete (3 systems missing)
   ✅ Risk assessment performed

2. Beskytte og opprettholde
   ✅ Access control implemented
   ✅ MFA enabled for admin users
   ❌ MFA not required for all users
   ✅ TLS 1.3 configured
   ⚠️ Password policy needs strengthening

3. Oppdage
   ✅ Security logging enabled
   ⚠️ Log retention only 30 days (require 12 months)
   ❌ No anomaly detection implemented

4. Håndtere og gjenopprette
   ✅ Incident response plan documented
   ✅ Daily backups configured
   ⚠️ Recovery testing not performed recently

DIGDIR REQUIREMENTS
───────────────────────────────────────────────────────────────

✅ ID-porten integration compliant
❌ Maskinporten not configured
✅ HTTPS only
⚠️ Security headers incomplete

RECOMMENDATIONS
───────────────────────────────────────────────────────────────

1. Enable MFA for all users (Critical)
2. Extend log retention to 12 months
3. Implement anomaly detection
4. Complete data classification
5. Configure Maskinporten for API access
6. Perform quarterly recovery testing
```

## Guidelines

1. **Follow NSM Grunnprinsipper** - All 4 areas must be addressed
2. **Regular audits** - Security assessment at least annually
3. **Document everything** - Policies, procedures, incidents
4. **Train personnel** - Security awareness for all staff
5. **Report incidents** - NSM notification within 24 hours for serious incidents

