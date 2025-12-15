---
description: GDPR data protection expertise
triggers:
  - handling user data
  - creating forms
  - storing personal data
  - implementing consent
  - data processing
---

# GDPR Compliance Skill

Expert GDPR data protection capabilities.

## Data Collection Patterns

### Minimal Collection
```typescript
// ❌ Over-collection
interface UserRegistration {
  email: string
  password: string
  phone: string         // Not needed
  birthDate: string     // Not needed
  address: string       // Not needed
}

// ✅ Minimal collection
interface UserRegistration {
  email: string
  password: string
  // Add only when business need is documented
}
```

### Consent Collection
```typescript
interface ConsentRecord {
  userId: string
  purpose: string
  granted: boolean
  timestamp: Date
  policyVersion: string
  collectionMethod: 'checkbox' | 'banner' | 'settings'
}

async function recordConsent(
  userId: string,
  purpose: string,
  granted: boolean
): Promise<void> {
  await db.consent.create({
    data: {
      userId,
      purpose,
      granted,
      timestamp: new Date(),
      policyVersion: CURRENT_POLICY_VERSION,
    }
  })
}

// Check before processing
async function canProcess(userId: string, purpose: string): Promise<boolean> {
  const consent = await db.consent.findFirst({
    where: { userId, purpose },
    orderBy: { timestamp: 'desc' }
  })
  return consent?.granted ?? false
}
```

## Data Subject Rights

### Right to Access
```typescript
async function exportUserData(userId: string): Promise<DataExport> {
  const user = await db.users.findUnique({ where: { id: userId } })
  const activities = await db.activities.findMany({ where: { userId } })
  const consents = await db.consent.findMany({ where: { userId } })
  
  return {
    exportedAt: new Date().toISOString(),
    personalData: {
      email: user.email,
      name: user.name,
      createdAt: user.createdAt,
    },
    activityHistory: activities,
    consentHistory: consents,
    // Include all personal data categories
  }
}
```

### Right to Erasure
```typescript
async function deleteUserData(userId: string): Promise<void> {
  // 1. Delete from all tables
  await db.activities.deleteMany({ where: { userId } })
  await db.preferences.deleteMany({ where: { userId } })
  await db.sessions.deleteMany({ where: { userId } })
  
  // 2. Anonymize user (keep for audit if needed)
  await db.users.update({
    where: { id: userId },
    data: {
      email: `deleted-${userId}@deleted.local`,
      name: 'Slettet bruker',
      deletedAt: new Date(),
    }
  })
  
  // 3. Log the deletion
  await auditLog.create({
    action: 'USER_DELETED',
    userId,
    performedAt: new Date(),
  })
}
```

### Data Portability
```typescript
async function generatePortableData(userId: string): Promise<Buffer> {
  const data = await exportUserData(userId)
  
  // Machine-readable format (JSON)
  return Buffer.from(JSON.stringify(data, null, 2))
}
```

## Cookie Consent Pattern

```typescript
// types/consent.ts
type CookieCategory = 'necessary' | 'analytics' | 'marketing' | 'preferences'

interface CookiePreferences {
  necessary: true  // Always true, cannot be disabled
  analytics: boolean
  marketing: boolean
  preferences: boolean
}

// hooks/useCookieConsent.ts
function useCookieConsent() {
  const [preferences, setPreferences] = useState<CookiePreferences | null>(null)
  const [showBanner, setShowBanner] = useState(false)
  
  useEffect(() => {
    const stored = getCookiePreferences()
    if (stored) {
      setPreferences(stored)
    } else {
      setShowBanner(true)
    }
  }, [])
  
  const acceptAll = () => {
    const prefs = { necessary: true, analytics: true, marketing: true, preferences: true }
    saveCookiePreferences(prefs)
    setPreferences(prefs)
    setShowBanner(false)
  }
  
  const acceptNecessary = () => {
    const prefs = { necessary: true, analytics: false, marketing: false, preferences: false }
    saveCookiePreferences(prefs)
    setPreferences(prefs)
    setShowBanner(false)
  }
  
  return { preferences, showBanner, acceptAll, acceptNecessary, setPreferences }
}
```

## Privacy Notice Requirements

```markdown
# Personvernerklæring

## Behandlingsansvarlig
[Selskapsnavn], org.nr. [nummer]
Adresse: [adresse]
E-post: personvern@example.no

## Hvilke opplysninger vi samler
- E-postadresse (for innlogging og kommunikasjon)
- [Liste andre kategorier]

## Behandlingsgrunnlag
- Samtykke (Art. 6(1)(a))
- Avtale (Art. 6(1)(b))
- [Andre grunnlag]

## Dine rettigheter
- Rett til innsyn
- Rett til retting
- Rett til sletting
- Rett til dataportabilitet
- Rett til å protestere

## Kontakt
For spørsmål: personvern@example.no
Klage til Datatilsynet: datatilsynet.no
```

## When to Use

Apply automatically when:
- Creating user registration
- Building forms that collect data
- Implementing cookies/tracking
- Processing personal information
- Building data export/delete features

