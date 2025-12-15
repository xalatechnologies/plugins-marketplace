---
description: Create a mobile screen with navigation
arguments:
  - name: name
    description: Screen name
    required: true
  - name: type
    description: Screen type (stack, tab, modal)
    required: false
    default: stack
---

# Create Screen Command

Create a new mobile screen with proper navigation setup.

## Screen Template

```typescript
// screens/DashboardScreen.tsx
import { View, Text, StyleSheet, ScrollView } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { NativeStackScreenProps } from '@react-navigation/native-stack'
import { RootStackParamList } from '@/navigation/types'

type Props = NativeStackScreenProps<RootStackParamList, 'Dashboard'>

export function DashboardScreen({ navigation }: Props) {
  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.content}>
        <Text style={styles.title}>Dashboard</Text>
        {/* Screen content */}
      </ScrollView>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  content: {
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  },
})
```

## Navigation Types

```typescript
// navigation/types.ts
export type RootStackParamList = {
  Home: undefined
  Dashboard: undefined
  Settings: undefined
  Profile: { userId: string }
}

export type TabParamList = {
  HomeTab: undefined
  ProjectsTab: undefined
  SettingsTab: undefined
}
```

## Screen Registration

```typescript
// navigation/RootNavigator.tsx
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import { DashboardScreen } from '@/screens/DashboardScreen'

const Stack = createNativeStackNavigator<RootStackParamList>()

export function RootNavigator() {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="Dashboard"
        component={DashboardScreen}
        options={{
          title: 'Dashboard',
          headerShown: true,
        }}
      />
    </Stack.Navigator>
  )
}
```

## Patterns

### Data Fetching Screen

```typescript
import { useQuery } from '@tanstack/react-query'
import { ActivityIndicator } from 'react-native'

export function ProjectsScreen() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['projects'],
    queryFn: fetchProjects,
  })

  if (isLoading) {
    return <ActivityIndicator size="large" />
  }

  if (error) {
    return <ErrorView message={error.message} />
  }

  return (
    <FlatList
      data={data}
      renderItem={({ item }) => <ProjectCard project={item} />}
      keyExtractor={item => item.id}
    />
  )
}
```

### Form Screen

```typescript
import { useForm, Controller } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'

const schema = z.object({
  name: z.string().min(1, 'Name required'),
  email: z.string().email('Invalid email'),
})

export function ProfileEditScreen() {
  const { control, handleSubmit, formState: { errors } } = useForm({
    resolver: zodResolver(schema),
  })

  const onSubmit = async (data: z.infer<typeof schema>) => {
    await updateProfile(data)
  }

  return (
    <ScrollView>
      <Controller
        control={control}
        name="name"
        render={({ field: { onChange, value } }) => (
          <TextInput
            value={value}
            onChangeText={onChange}
            placeholder="Name"
          />
        )}
      />
      {errors.name && <Text style={styles.error}>{errors.name.message}</Text>}
      
      <Button title="Save" onPress={handleSubmit(onSubmit)} />
    </ScrollView>
  )
}
```

