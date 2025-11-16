# Code Policies - React

> Standard, convenzioni e politiche di scrittura del codice per il libro su React

## 📋 Indice
- [Standard di Scrittura](#standard-di-scrittura)
- [Convenzioni di Nomenclatura](#convenzioni-di-nomenclatura)
- [Template di Codice](#template-di-codice)
- [Struttura dei File](#struttura-dei-file)
- [Best Practices](#best-practices)
- [Pattern di Programmazione](#pattern-di-programmazione)
- [Gestione State](#gestione-state)
- [Commenti e Documentazione](#commenti-e-documentazione)

---

## Standard di Scrittura

### Formattazione
- **Indentazione**: 2 spazi
- **Lunghezza linea**: max 80-100 caratteri
- **Encoding**: UTF-8
- **Fine riga**: LF (Unix)
- **Quotes**: Single quotes per JS, double quotes per JSX
- **Semicolons**: Sempre usare semicolons

### Stile del Codice
```tsx
// Functional Component con TypeScript
import React, { useState, useEffect } from 'react';
import { User } from './types';
import { fetchUser } from './api';

interface UserProfileProps {
  userId: string;
  onUpdate?: (user: User) => void;
}

export const UserProfile: React.FC<UserProfileProps> = ({
  userId,
  onUpdate
}) => {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadUser = async () => {
      setIsLoading(true);
      try {
        const data = await fetchUser(userId);
        setUser(data);
        onUpdate?.(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setIsLoading(false);
      }
    };

    loadUser();
  }, [userId, onUpdate]);

  if (isLoading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  if (!user) {
    return null;
  }

  return (
    <div className="user-profile">
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  );
};
```

### Regole Generali
- [ ] Sempre usare functional components (no class components)
- [ ] Preferire TypeScript a JavaScript
- [ ] Un componente per file
- [ ] Props drilling max 2-3 livelli
- [ ] Usare ESLint e Prettier

---

## Convenzioni di Nomenclatura

### Componenti
- **Componenti**: `PascalCase` - Esempio: `UserProfile`, `NavBar`
- **File componenti**: `PascalCase.tsx` - Esempio: `UserProfile.tsx`
- **Hooks custom**: `use` prefix + `camelCase` - Esempio: `useAuth`, `useFetch`
- **Context**: `PascalCase` + `Context` - Esempio: `AuthContext`, `ThemeContext`

### Variabili e Funzioni
- **Variabili**: `camelCase` - Esempio: `userName`, `isLoading`
- **Costanti**: `UPPER_SNAKE_CASE` - Esempio: `API_URL`, `MAX_RETRIES`
- **Funzioni**: `camelCase` - Esempio: `handleClick`, `fetchData`
- **Event handlers**: `handle` prefix - Esempio: `handleSubmit`, `handleChange`

### Props e Types
- **Props interface**: `ComponentName` + `Props` - Esempio: `UserProfileProps`
- **Type alias**: `PascalCase` - Esempio: `User`, `ApiResponse`
- **Enum**: `PascalCase` - Esempio: `UserRole`, `Status`

### Files
- **Componenti**: `ComponentName.tsx`
- **Hooks**: `useHookName.ts`
- **Utils**: `kebab-case.ts` - Esempio: `date-utils.ts`
- **Types**: `types.ts` o `ComponentName.types.ts`
- **Styles**: `ComponentName.module.css` o `ComponentName.styled.ts`

---

## Template di Codice

### Template Componente Funzionale
```tsx
import React, { useState, useEffect } from 'react';
import styles from './ComponentName.module.css';

/**
 * ComponentName
 *
 * Brief description of what this component does
 *
 * @example
 * ```tsx
 * <ComponentName title="Hello" onAction={() => console.log('clicked')} />
 * ```
 */

interface ComponentNameProps {
  /** Description of title prop */
  title: string;
  /** Optional description */
  description?: string;
  /** Callback when action occurs */
  onAction?: () => void;
  /** Child components */
  children?: React.ReactNode;
}

export const ComponentName: React.FC<ComponentNameProps> = ({
  title,
  description,
  onAction,
  children
}) => {
  // === STATE ===
  const [isActive, setIsActive] = useState(false);

  // === EFFECTS ===
  useEffect(() => {
    // Effect logic
    return () => {
      // Cleanup
    };
  }, []);

  // === HANDLERS ===
  const handleClick = () => {
    setIsActive(prev => !prev);
    onAction?.();
  };

  // === RENDER HELPERS ===
  const renderContent = () => {
    if (!description) return null;
    return <p className={styles.description}>{description}</p>;
  };

  // === RENDER ===
  return (
    <div className={styles.container}>
      <h2 className={styles.title}>{title}</h2>
      {renderContent()}
      <button
        className={styles.button}
        onClick={handleClick}
        aria-pressed={isActive}
      >
        Click me
      </button>
      {children}
    </div>
  );
};
```

### Template Custom Hook
```ts
import { useState, useEffect, useCallback } from 'react';

interface UseFetchOptions {
  immediate?: boolean;
}

interface UseFetchReturn<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
  refetch: () => Promise<void>;
}

/**
 * Custom hook for data fetching
 *
 * @param url - The URL to fetch from
 * @param options - Fetch options
 * @returns Object with data, loading, error, and refetch
 *
 * @example
 * ```tsx
 * const { data, loading, error } = useFetch<User>('/api/user/1');
 * ```
 */
export function useFetch<T>(
  url: string,
  options: UseFetchOptions = {}
): UseFetchReturn<T> {
  const { immediate = true } = options;

  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err instanceof Error ? err : new Error('Unknown error'));
    } finally {
      setLoading(false);
    }
  }, [url]);

  useEffect(() => {
    if (immediate) {
      fetchData();
    }
  }, [fetchData, immediate]);

  return { data, loading, error, refetch: fetchData };
}
```

### Template Context
```tsx
import React, { createContext, useContext, useState, useCallback } from 'react';

interface AuthContextValue {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

interface AuthProviderProps {
  children: React.ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  const login = useCallback(async (email: string, password: string) => {
    // Login logic
    const userData = await authenticateUser(email, password);
    setUser(userData);
  }, []);

  const logout = useCallback(() => {
    setUser(null);
  }, []);

  const value: AuthContextValue = {
    user,
    login,
    logout,
    isAuthenticated: user !== null
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextValue => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};
```

---

## Struttura dei File

### Organizzazione Progetto
```
src/
├── components/
│   ├── common/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   ├── Button.module.css
│   │   │   └── index.ts
│   │   └── Input/
│   └── features/
│       └── UserProfile/
│           ├── UserProfile.tsx
│           ├── UserProfile.test.tsx
│           └── index.ts
├── hooks/
│   ├── useAuth.ts
│   ├── useFetch.ts
│   └── index.ts
├── contexts/
│   ├── AuthContext.tsx
│   └── ThemeContext.tsx
├── pages/
│   ├── Home.tsx
│   ├── About.tsx
│   └── index.ts
├── services/
│   ├── api.ts
│   └── auth.ts
├── utils/
│   ├── date-utils.ts
│   └── validation.ts
├── types/
│   ├── user.ts
│   └── api.ts
├── constants/
│   └── config.ts
├── styles/
│   ├── globals.css
│   └── variables.css
├── App.tsx
└── index.tsx
```

### Index.ts Pattern (Barrel Exports)
```ts
// components/common/Button/index.ts
export { Button } from './Button';
export type { ButtonProps } from './Button';

// components/common/index.ts
export { Button } from './Button';
export { Input } from './Input';
export { Card } from './Card';
```

---

## Best Practices

### Component Design
- [ ] Componenti piccoli e focalizzati (max 200 righe)
- [ ] Props max 5-7 per componente
- [ ] Composition over configuration
- [ ] Evitare prop drilling (usare context o state management)
- [ ] Separare logica da presentazione

### Performance
- [ ] Usare React.memo per componenti pesanti
- [ ] useMemo per calcoli costosi
- [ ] useCallback per funzioni passate come props
- [ ] Lazy loading con React.lazy e Suspense
- [ ] Virtualizzazione per liste lunghe

```tsx
// Memoization
const ExpensiveComponent = React.memo(({ data }) => {
  const processed = useMemo(() => {
    return processData(data);
  }, [data]);

  const handleClick = useCallback(() => {
    console.log('clicked');
  }, []);

  return <div onClick={handleClick}>{processed}</div>;
});

// Lazy loading
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

### State Management
- [ ] useState per state locale
- [ ] useReducer per state complesso
- [ ] Context per state condiviso (limitato)
- [ ] Redux/Zustand per state globale complesso
- [ ] React Query per server state

---

## Pattern di Programmazione

### Composition Pattern
```tsx
// Compound Components
const Card = ({ children }: { children: React.ReactNode }) => {
  return <div className="card">{children}</div>;
};

Card.Header = ({ children }: { children: React.ReactNode }) => {
  return <div className="card-header">{children}</div>;
};

Card.Body = ({ children }: { children: React.ReactNode }) => {
  return <div className="card-body">{children}</div>;
};

// Usage
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Body>Content</Card.Body>
</Card>
```

### Render Props Pattern
```tsx
interface DataFetcherProps<T> {
  url: string;
  children: (data: T | null, loading: boolean, error: Error | null) => React.ReactNode;
}

function DataFetcher<T>({ url, children }: DataFetcherProps<T>) {
  const { data, loading, error } = useFetch<T>(url);
  return <>{children(data, loading, error)}</>;
}

// Usage
<DataFetcher<User> url="/api/user">
  {(user, loading, error) => {
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;
    return <div>{user?.name}</div>;
  }}
</DataFetcher>
```

### Higher-Order Component (HOC) Pattern
```tsx
interface WithLoadingProps {
  isLoading: boolean;
}

function withLoading<P extends object>(
  Component: React.ComponentType<P>
) {
  return function WithLoadingComponent(
    props: P & WithLoadingProps
  ) {
    const { isLoading, ...rest } = props;

    if (isLoading) {
      return <div>Loading...</div>;
    }

    return <Component {...(rest as P)} />;
  };
}

// Usage
const UserProfileWithLoading = withLoading(UserProfile);
```

---

## Gestione State

### Local State (useState)
```tsx
function Counter() {
  const [count, setCount] = useState(0);

  // Functional update quando dipende dallo stato precedente
  const increment = () => setCount(prev => prev + 1);

  return <button onClick={increment}>Count: {count}</button>;
}
```

### Complex State (useReducer)
```tsx
type State = {
  count: number;
  step: number;
};

type Action =
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'setStep'; payload: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step };
    case 'decrement':
      return { ...state, count: state.count - state.step };
    case 'setStep':
      return { ...state, step: action.payload };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0, step: 1 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </div>
  );
}
```

---

## Commenti e Documentazione

### JSDoc per Componenti
```tsx
/**
 * Button component with various styles and sizes
 *
 * @component
 * @example
 * ```tsx
 * <Button variant="primary" size="large" onClick={handleClick}>
 *   Click me
 * </Button>
 * ```
 */
interface ButtonProps {
  /** Button label */
  children: React.ReactNode;
  /** Visual style variant */
  variant?: 'primary' | 'secondary' | 'danger';
  /** Size of the button */
  size?: 'small' | 'medium' | 'large';
  /** Click handler */
  onClick?: () => void;
  /** Disable button */
  disabled?: boolean;
}

export const Button: React.FC<ButtonProps> = ({ ... }) => {
  // Implementation
};
```

### Commenti Inline
```tsx
// TODO: Add loading state
// FIXME: Button doesn't work on mobile
// NOTE: This component assumes user is authenticated

// Commenta il "perché", non il "cosa"
// ✅ BUONO:
// We disable the button during submission to prevent double-clicks
const isDisabled = isSubmitting;

// ❌ CATTIVO:
// Set disabled to isSubmitting
const isDisabled = isSubmitting;
```

---

## Note Aggiuntive

### Versione React
- **Target**: React 18+
- **Features**: Concurrent features, automatic batching, transitions

### Tool e Linter
- **Build**: Vite, Create React App, Next.js
- **Linter**: ESLint con plugin react, react-hooks
- **Formatter**: Prettier
- **Type checker**: TypeScript
- **Testing**: Jest, React Testing Library, Vitest

### ESLint Configuration
```json
{
  "extends": [
    "react-app",
    "react-app/jest",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended"
  ],
  "rules": {
    "react/prop-types": "off",
    "react/react-in-jsx-scope": "off",
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": "warn"
  }
}
```

### Riferimenti
- React Official Docs
- React TypeScript Cheatsheet
- Airbnb React Style Guide
- Kent C. Dodds Blog

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
