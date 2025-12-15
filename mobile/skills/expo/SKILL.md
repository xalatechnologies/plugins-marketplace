---
description: Expo and React Native development expertise
triggers:
  - mobile development
  - expo
  - react native
  - ios
  - android
---

# Expo/React Native Skill

## Quick Patterns

### App Configuration

```json
// app.json
{
  "expo": {
    "name": "Xala PM",
    "slug": "xala-pm",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#1a1a1a"
    },
    "ios": {
      "supportsTablet": true,
      "bundleIdentifier": "com.xalatechnologies.pm"
    },
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#1a1a1a"
      },
      "package": "com.xalatechnologies.pm"
    },
    "plugins": [
      "expo-router",
      "expo-secure-store"
    ]
  }
}
```

### Authentication

```typescript
import * as SecureStore from 'expo-secure-store'

const TOKEN_KEY = 'auth_token'

export async function saveToken(token: string) {
  await SecureStore.setItemAsync(TOKEN_KEY, token)
}

export async function getToken() {
  return SecureStore.getItemAsync(TOKEN_KEY)
}

export async function deleteToken() {
  await SecureStore.deleteItemAsync(TOKEN_KEY)
}
```

### Push Notifications

```typescript
import * as Notifications from 'expo-notifications'
import * as Device from 'expo-device'

export async function registerForPushNotifications() {
  if (!Device.isDevice) {
    return null
  }

  const { status: existingStatus } = await Notifications.getPermissionsAsync()
  let finalStatus = existingStatus
  
  if (existingStatus !== 'granted') {
    const { status } = await Notifications.requestPermissionsAsync()
    finalStatus = status
  }
  
  if (finalStatus !== 'granted') {
    return null
  }

  const token = await Notifications.getExpoPushTokenAsync()
  return token.data
}
```

### Gestures and Animations

```typescript
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
} from 'react-native-reanimated'

function AnimatedCard() {
  const scale = useSharedValue(1)

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }],
  }))

  const onPressIn = () => {
    scale.value = withSpring(0.95)
  }

  const onPressOut = () => {
    scale.value = withSpring(1)
  }

  return (
    <Pressable onPressIn={onPressIn} onPressOut={onPressOut}>
      <Animated.View style={[styles.card, animatedStyle]}>
        <Text>Card Content</Text>
      </Animated.View>
    </Pressable>
  )
}
```

### Offline Support

```typescript
import NetInfo from '@react-native-community/netinfo'
import AsyncStorage from '@react-native-async-storage/async-storage'

export function useOfflineSync<T>(key: string, fetcher: () => Promise<T>) {
  const [data, setData] = useState<T | null>(null)
  const [isOnline, setIsOnline] = useState(true)

  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsOnline(!!state.isConnected)
    })
    return unsubscribe
  }, [])

  useEffect(() => {
    async function load() {
      if (isOnline) {
        try {
          const fresh = await fetcher()
          setData(fresh)
          await AsyncStorage.setItem(key, JSON.stringify(fresh))
        } catch {
          // Fall back to cached
          const cached = await AsyncStorage.getItem(key)
          if (cached) setData(JSON.parse(cached))
        }
      } else {
        const cached = await AsyncStorage.getItem(key)
        if (cached) setData(JSON.parse(cached))
      }
    }
    load()
  }, [isOnline])

  return { data, isOnline }
}
```

## When to Use

Apply when:
- Building mobile screens
- Setting up Expo configuration
- Implementing native features
- Creating animations

