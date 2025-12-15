---
description: Create a new page/route with proper data loading and SEO
arguments:
  - name: route
    description: Route path (e.g., /dashboard/settings)
    required: true
  - name: framework
    description: Framework (remix, nextjs)
    required: false
    default: remix
---

# Create Page Command

Generate a new page/route with proper structure.

## Remix Page Structure

```tsx
// app/routes/dashboard.settings.tsx
import { json, type LoaderFunctionArgs, type MetaFunction } from '@remix-run/node'
import { useLoaderData } from '@remix-run/react'
import { requireUser } from '@/services/auth.server'
import { Page } from '@/components/layout/Page'

export const meta: MetaFunction = () => {
  return [
    { title: 'Settings | Xala PM' },
    { name: 'description', content: 'Manage your account settings' },
  ]
}

export async function loader({ request }: LoaderFunctionArgs) {
  const user = await requireUser(request)
  
  // Fetch data
  const settings = await getSettings(user.id)
  
  return json({ user, settings })
}

export default function SettingsPage() {
  const { user, settings } = useLoaderData<typeof loader>()
  
  return (
    <Page title="Settings" description="Manage your account">
      {/* Page content */}
    </Page>
  )
}
```

## Next.js Page Structure

```tsx
// app/dashboard/settings/page.tsx
import { Metadata } from 'next'
import { redirect } from 'next/navigation'
import { getUser } from '@/lib/auth'
import { Page } from '@/components/layout/Page'

export const metadata: Metadata = {
  title: 'Settings | Xala PM',
  description: 'Manage your account settings',
}

export default async function SettingsPage() {
  const user = await getUser()
  
  if (!user) {
    redirect('/login')
  }
  
  // Fetch data
  const settings = await getSettings(user.id)
  
  return (
    <Page title="Settings" description="Manage your account">
      {/* Page content */}
    </Page>
  )
}
```

## Data Loading Patterns

### Remix
- Use `loader` for GET data
- Use `action` for POST/PUT/DELETE
- `useLoaderData` for accessing loader data
- `useFetcher` for non-navigation mutations

### Next.js App Router
- Use Server Components for data fetching
- Use `use server` for server actions
- `useFormState` for form handling
- Keep interactive parts in Client Components

## SEO Checklist

- [ ] `<title>` with branding
- [ ] Meta description
- [ ] Open Graph tags
- [ ] Canonical URL
- [ ] Structured data (if applicable)
- [ ] Proper heading hierarchy (h1-h6)

## Guidelines

1. **Auth first**: Always check authentication in loaders
2. **Error boundaries**: Handle errors gracefully
3. **Loading states**: Use Suspense or loading.tsx
4. **Type safety**: Type loader/action return values
5. **Keep pages thin**: Extract logic to services/hooks

