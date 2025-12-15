---
description: Check GDPR compliance for data handling and privacy
arguments:
  - name: scope
    description: Check scope (forms, storage, api, full)
    required: false
    default: full
---

# GDPR Compliance Check Command

Verify GDPR (General Data Protection Regulation) compliance.

## GDPR Principles

### 1. Lawfulness, Fairness, Transparency
- Clear legal basis for processing
- Transparent privacy notices
- Fair data handling

### 2. Purpose Limitation
- Data collected for specified purposes
- Not processed incompatibly

### 3. Data Minimization
```typescript
// ❌ Collecting unnecessary data
interface UserRegistration {
  email: string
  password: string
  phone: string      // Not needed for login
  birthDate: string  // Not needed for service
  address: string    // Not needed
}

// ✅ Minimal data collection
interface UserRegistration {
  email: string
  password: string
  // Only collect what's necessary
}
```

### 4. Accuracy
- Keep data accurate and up-to-date
- Allow users to correct their data

### 5. Storage Limitation
```typescript
// ❌ Indefinite storage
const userData = await db.users.insert(data)

// ✅ With retention policy
const userData = await db.users.insert({
  ...data,
  retention_until: addYears(new Date(), 2),
  created_at: new Date(),
})

// Automated cleanup
async function cleanupExpiredData() {
  await db.users.delete({
    retention_until: { lt: new Date() }
  })
}
```

### 6. Integrity & Confidentiality
```typescript
// ✅ Encryption at rest
const encryptedData = encrypt(sensitiveData, key)
await db.sensitiveInfo.insert({ data: encryptedData })

// ✅ Encryption in transit (HTTPS required)
// ✅ Access controls
// ✅ Audit logging
```

### 7. Accountability
- Document all processing activities
- Maintain records
- Demonstrate compliance

## Code Patterns

### Consent Management

```typescript
// consent/types.ts
interface ConsentRecord {
  userId: string
  purpose: 'marketing' | 'analytics' | 'necessary'
  granted: boolean
  timestamp: Date
  version: string
  ipAddress?: string
}

// consent/service.ts
class ConsentService {
  async recordConsent(
    userId: string,
    purpose: string,
    granted: boolean
  ): Promise<void> {
    await db.consent.insert({
      userId,
      purpose,
      granted,
      timestamp: new Date(),
      version: PRIVACY_POLICY_VERSION,
    })
  }
  
  async hasConsent(userId: string, purpose: string): Promise<boolean> {
    const latest = await db.consent.findFirst({
      where: { userId, purpose },
      orderBy: { timestamp: 'desc' },
    })
    return latest?.granted ?? false
  }
  
  async withdrawConsent(userId: string, purpose: string): Promise<void> {
    await this.recordConsent(userId, purpose, false)
    // Trigger data deletion if necessary
    if (purpose === 'marketing') {
      await this.deleteMarketingData(userId)
    }
  }
}
```

### Right to Access (Data Export)

```typescript
// gdpr/export.ts
async function exportUserData(userId: string): Promise<UserDataExport> {
  const user = await db.users.findUnique({ where: { id: userId } })
  const activities = await db.activities.findMany({ where: { userId } })
  const consents = await db.consent.findMany({ where: { userId } })
  
  return {
    exportDate: new Date().toISOString(),
    user: {
      email: user.email,
      name: user.name,
      createdAt: user.createdAt,
    },
    activities: activities.map(a => ({
      type: a.type,
      date: a.createdAt,
      description: a.description,
    })),
    consents: consents.map(c => ({
      purpose: c.purpose,
      granted: c.granted,
      date: c.timestamp,
    })),
  }
}
```

### Right to Erasure (Data Deletion)

```typescript
// gdpr/deletion.ts
async function deleteUserData(userId: string): Promise<DeletionReport> {
  const report: DeletionReport = {
    userId,
    requestedAt: new Date(),
    deletedRecords: {},
  }
  
  // Delete from all tables
  const tables = ['activities', 'preferences', 'sessions', 'consents']
  
  for (const table of tables) {
    const count = await db[table].deleteMany({ where: { userId } })
    report.deletedRecords[table] = count
  }
  
  // Anonymize user record (keep for audit)
  await db.users.update({
    where: { id: userId },
    data: {
      email: `deleted-${userId}@deleted.local`,
      name: 'Deleted User',
      deletedAt: new Date(),
    },
  })
  
  // Log the deletion
  await auditLog.create({
    action: 'GDPR_DELETION',
    userId,
    timestamp: new Date(),
  })
  
  return report
}
```

### Cookie Consent

```typescript
// components/CookieConsent.tsx
export function CookieConsent() {
  const [preferences, setPreferences] = useState({
    necessary: true,  // Cannot be disabled
    analytics: false,
    marketing: false,
  })
  
  const handleAcceptAll = () => {
    setPreferences({ necessary: true, analytics: true, marketing: true })
    saveConsent({ necessary: true, analytics: true, marketing: true })
  }
  
  const handleAcceptNecessary = () => {
    saveConsent({ necessary: true, analytics: false, marketing: false })
  }
  
  return (
    <div role="dialog" aria-label="Cookie innstillinger">
      <h2>Vi bruker informasjonskapsler</h2>
      <p>
        Vi bruker informasjonskapsler for å forbedre opplevelsen din.
        Les vår <a href="/personvern">personvernerklæring</a>.
      </p>
      
      <div>
        <label>
          <input type="checkbox" checked disabled />
          Nødvendige (påkrevd)
        </label>
        
        <label>
          <input
            type="checkbox"
            checked={preferences.analytics}
            onChange={(e) => setPreferences(p => ({
              ...p, analytics: e.target.checked
            }))}
          />
          Analyse
        </label>
        
        <label>
          <input
            type="checkbox"
            checked={preferences.marketing}
            onChange={(e) => setPreferences(p => ({
              ...p, marketing: e.target.checked
            }))}
          />
          Markedsføring
        </label>
      </div>
      
      <button onClick={handleAcceptNecessary}>
        Kun nødvendige
      </button>
      <button onClick={handleAcceptAll}>
        Godta alle
      </button>
    </div>
  )
}
```

## Audit Output Format

```
🔒 GDPR COMPLIANCE AUDIT
═══════════════════════════════════════════════════════════════

Scope: Full Application
Date: 2024-12-15

SUMMARY
───────────────────────────────────────────────────────────────
✅ Compliant:    12 requirements
⚠️ Needs Review: 4 requirements
❌ Non-Compliant: 2 requirements

CRITICAL ISSUES
───────────────────────────────────────────────────────────────

[DATA-001] Missing Cookie Consent
Location: src/app/layout.tsx
Issue: No cookie consent mechanism found
Required: Must obtain consent before non-essential cookies
Fix: Implement CookieConsent component

[DATA-002] Data Retention Not Implemented
Location: Database schema
Issue: No retention_until field on user data
Required: Data should not be kept longer than necessary
Fix: Add retention policies to all personal data tables

RECOMMENDATIONS
───────────────────────────────────────────────────────────────

1. Implement data export endpoint (/api/gdpr/export)
2. Implement data deletion endpoint (/api/gdpr/delete)
3. Add consent management for marketing emails
4. Document data processing activities
5. Appoint Data Protection Officer (if >250 employees)
```

## Guidelines

1. **Privacy by Design** - Build privacy into systems from start
2. **Document everything** - Keep records of processing activities
3. **Regular audits** - Review compliance periodically
4. **Train staff** - Everyone should understand GDPR
5. **Breach procedures** - Have plan for data breaches (72h reporting)

