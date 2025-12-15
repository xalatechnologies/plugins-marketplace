---
description: JSDoc documentation standards for comprehensive code documentation
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
---

# JSDoc Standards Skill

> Every exported function, class, and type must be documented. Self-documenting code + JSDoc = maintainable software.

## Documentation Coverage Requirements

| Export Type | JSDoc Required | Minimum Content |
|-------------|----------------|-----------------|
| Public Function | ✅ Yes | Description, @param, @returns |
| Public Class | ✅ Yes | Description, @example |
| Public Method | ✅ Yes | Description, @param, @returns |
| Public Type/Interface | ✅ Yes | Description, property docs |
| Private/Internal | ⚠️ Recommended | Brief description |
| Constants | ⚠️ Recommended | Purpose |

## Function Documentation

### Complete Function JSDoc

```typescript
/**
 * Authenticates a user with email and password credentials.
 *
 * This function validates the provided credentials against the database,
 * verifies the password hash, and creates a new session if successful.
 * Failed attempts are logged for security monitoring.
 *
 * @param credentials - The user's login credentials
 * @param credentials.email - User's email address (validated against email format)
 * @param credentials.password - User's password (min 8 chars)
 * @param options - Optional authentication options
 * @param options.rememberMe - If true, session expires in 30 days instead of 24 hours
 * @param options.deviceId - Device identifier for multi-device session management
 *
 * @returns Promise resolving to authentication result with user and session
 *
 * @throws {ValidationError} When email format is invalid or password too short
 * @throws {AuthenticationError} When credentials don't match any user
 * @throws {AccountLockedError} When account is locked due to too many failed attempts
 * @throws {RateLimitError} When too many login attempts from this IP
 *
 * @example
 * // Basic authentication
 * const result = await authenticate({
 *   email: 'user@example.com',
 *   password: 'SecurePass123!'
 * });
 * console.log(result.user.name); // 'John Doe'
 *
 * @example
 * // With remember me option
 * const result = await authenticate(
 *   { email: 'user@example.com', password: 'SecurePass123!' },
 *   { rememberMe: true }
 * );
 * console.log(result.session.expiresAt); // 30 days from now
 *
 * @see {@link logout} - For ending user sessions
 * @see {@link refreshSession} - For extending session lifetime
 * @since 1.0.0
 * @category Authentication
 */
export async function authenticate(
  credentials: LoginCredentials,
  options?: AuthOptions
): Promise<AuthResult> {
  // Implementation
}
```

### Async Function with Generic Types

```typescript
/**
 * Fetches a paginated list of resources from the API.
 *
 * @typeParam T - The type of resource being fetched
 * @param endpoint - The API endpoint to call (relative to base URL)
 * @param params - Pagination and filter parameters
 * @param params.page - Page number (1-indexed)
 * @param params.limit - Number of items per page (default: 20, max: 100)
 * @param params.sort - Field to sort by (prefixed with '-' for descending)
 * @param params.filter - Optional filter object
 *
 * @returns Promise resolving to paginated response
 *
 * @throws {NetworkError} When request fails due to network issues
 * @throws {ApiError} When API returns an error response
 *
 * @example
 * // Fetch users with pagination
 * const users = await fetchPaginated<User>('/users', {
 *   page: 1,
 *   limit: 20,
 *   sort: '-createdAt'
 * });
 *
 * @example
 * // With filtering
 * const activeUsers = await fetchPaginated<User>('/users', {
 *   page: 1,
 *   limit: 50,
 *   filter: { status: 'active' }
 * });
 */
export async function fetchPaginated<T>(
  endpoint: string,
  params: PaginationParams
): Promise<PaginatedResponse<T>> {
  // Implementation
}
```

## Class Documentation

```typescript
/**
 * Manages user authentication state and session lifecycle.
 *
 * This service handles all authentication-related operations including
 * login, logout, session refresh, and multi-factor authentication.
 * It integrates with the session store and emits events on auth state changes.
 *
 * @example
 * // Initialize and use the auth service
 * const authService = new AuthService({
 *   sessionStore: redisStore,
 *   tokenSecret: process.env.JWT_SECRET,
 * });
 *
 * // Login a user
 * const session = await authService.login({
 *   email: 'user@example.com',
 *   password: 'password123'
 * });
 *
 * // Check authentication status
 * const isAuthenticated = await authService.isAuthenticated(request);
 *
 * @fires AuthService#login - When user successfully logs in
 * @fires AuthService#logout - When user logs out
 * @fires AuthService#sessionExpired - When session expires
 *
 * @see {@link SessionStore} - For session persistence options
 * @category Services
 * @since 1.0.0
 */
export class AuthService {
  /**
   * The session store instance used for session persistence.
   * @readonly
   */
  private readonly sessionStore: SessionStore;

  /**
   * JWT secret used for token signing and verification.
   * @readonly
   * @private
   */
  private readonly tokenSecret: string;

  /**
   * Creates a new AuthService instance.
   *
   * @param config - Service configuration options
   * @param config.sessionStore - Session storage implementation
   * @param config.tokenSecret - Secret key for JWT operations
   * @param config.tokenExpiry - Token expiration time in seconds (default: 86400)
   * @throws {ConfigurationError} When required config options are missing
   */
  constructor(config: AuthServiceConfig) {
    // Implementation
  }

  /**
   * Authenticates a user and creates a new session.
   *
   * @param credentials - User login credentials
   * @returns Promise resolving to new session
   * @throws {AuthenticationError} When credentials are invalid
   */
  async login(credentials: LoginCredentials): Promise<Session> {
    // Implementation
  }

  /**
   * Terminates the current user session.
   *
   * @param sessionId - The session to terminate
   * @returns Promise resolving when session is destroyed
   */
  async logout(sessionId: string): Promise<void> {
    // Implementation
  }
}
```

## Interface/Type Documentation

```typescript
/**
 * Configuration options for the authentication service.
 *
 * @interface AuthServiceConfig
 * @category Configuration
 */
export interface AuthServiceConfig {
  /**
   * The session store implementation for persisting sessions.
   * Can be Redis, database, or in-memory (for development only).
   */
  sessionStore: SessionStore;

  /**
   * Secret key used for JWT signing.
   * Must be at least 32 characters for security.
   * @minLength 32
   */
  tokenSecret: string;

  /**
   * Token expiration time in seconds.
   * @default 86400 (24 hours)
   * @minimum 3600
   * @maximum 2592000 (30 days)
   */
  tokenExpiry?: number;

  /**
   * Enable multi-factor authentication requirement.
   * When enabled, users must complete MFA after password verification.
   * @default false
   */
  requireMFA?: boolean;

  /**
   * Maximum concurrent sessions per user.
   * Set to 1 to force single-session policy.
   * @default 5
   */
  maxSessions?: number;
}

/**
 * Result of a successful authentication attempt.
 *
 * @interface AuthResult
 */
export interface AuthResult {
  /**
   * The authenticated user's profile.
   * Excludes sensitive fields like password hash.
   */
  user: UserProfile;

  /**
   * The newly created session.
   * Contains token and expiration information.
   */
  session: Session;

  /**
   * Indicates if MFA verification is still required.
   * When true, call `verifyMFA()` before granting access.
   */
  mfaRequired: boolean;
}

/**
 * User profile information returned after authentication.
 *
 * @remarks
 * This type intentionally excludes sensitive information like
 * password hashes and security questions.
 */
export type UserProfile = Omit<User, 'passwordHash' | 'securityQuestions'>;
```

## React Component Documentation

```typescript
/**
 * A sophisticated data table component with sorting, filtering, and pagination.
 *
 * This component provides a full-featured table experience with:
 * - Column sorting (single and multi-column)
 * - Advanced filtering with multiple operators
 * - Pagination with customizable page sizes
 * - Row selection (single and multi-select)
 * - Responsive design with horizontal scroll on mobile
 * - Keyboard navigation support
 * - Screen reader accessibility
 *
 * @typeParam T - The type of data objects in the table
 *
 * @example
 * // Basic usage
 * <DataTable
 *   data={users}
 *   columns={[
 *     { key: 'name', header: 'Name', sortable: true },
 *     { key: 'email', header: 'Email', sortable: true },
 *     { key: 'role', header: 'Role', filterable: true },
 *   ]}
 * />
 *
 * @example
 * // With selection and custom actions
 * <DataTable
 *   data={users}
 *   columns={columns}
 *   selectable
 *   onSelectionChange={(selected) => setSelectedUsers(selected)}
 *   renderActions={(row) => (
 *     <Button onClick={() => editUser(row)}>Edit</Button>
 *   )}
 * />
 *
 * @see {@link Column} - Column configuration options
 * @see {@link useDataTable} - Hook for controlled table state
 * @category Components
 * @accessibility Implements ARIA table patterns
 */
export function DataTable<T extends Record<string, unknown>>({
  data,
  columns,
  selectable = false,
  pageSize = 20,
  onSelectionChange,
  renderActions,
  emptyState,
  loading,
  ...props
}: DataTableProps<T>): JSX.Element {
  // Implementation
}

/**
 * Props for the DataTable component.
 *
 * @typeParam T - The type of data objects in the table
 */
export interface DataTableProps<T> {
  /**
   * Array of data objects to display in the table.
   * Each object should have a unique `id` property.
   */
  data: T[];

  /**
   * Column configuration array.
   * Defines which fields to show and how to render them.
   */
  columns: Column<T>[];

  /**
   * Enable row selection checkboxes.
   * @default false
   */
  selectable?: boolean;

  /**
   * Number of rows per page.
   * @default 20
   */
  pageSize?: number;

  /**
   * Callback fired when selection changes.
   * Only called when `selectable` is true.
   */
  onSelectionChange?: (selectedRows: T[]) => void;

  /**
   * Render prop for row action buttons.
   * @param row - The data object for the current row
   * @returns Action elements to render in the actions column
   */
  renderActions?: (row: T) => React.ReactNode;

  /**
   * Custom empty state to show when no data is available.
   * If not provided, a default empty state is shown.
   */
  emptyState?: React.ReactNode;

  /**
   * Show loading skeleton while data is being fetched.
   * @default false
   */
  loading?: boolean;
}
```

## Custom Hook Documentation

```typescript
/**
 * Manages form state with validation, submission, and error handling.
 *
 * This hook provides a complete form management solution including:
 * - Field-level and form-level validation
 * - Async validation support
 * - Touched/dirty state tracking
 * - Submission handling with loading states
 * - Error handling and display
 *
 * @typeParam T - The shape of the form values object
 *
 * @param config - Form configuration options
 * @param config.initialValues - Initial form values
 * @param config.validationSchema - Zod schema for validation
 * @param config.onSubmit - Async function called on valid submission
 *
 * @returns Form state and handlers
 *
 * @example
 * // Basic form with validation
 * const form = useForm({
 *   initialValues: { email: '', password: '' },
 *   validationSchema: loginSchema,
 *   onSubmit: async (values) => {
 *     await api.login(values);
 *   },
 * });
 *
 * return (
 *   <form onSubmit={form.handleSubmit}>
 *     <input
 *       {...form.getFieldProps('email')}
 *       aria-invalid={form.errors.email ? 'true' : undefined}
 *     />
 *     {form.errors.email && <span>{form.errors.email}</span>}
 *     <button type="submit" disabled={form.isSubmitting}>
 *       {form.isSubmitting ? 'Loading...' : 'Submit'}
 *     </button>
 *   </form>
 * );
 *
 * @category Hooks
 * @since 1.2.0
 */
export function useForm<T extends Record<string, unknown>>(
  config: UseFormConfig<T>
): UseFormReturn<T> {
  // Implementation
}
```

## Inline Comments

```typescript
export async function processOrder(order: Order): Promise<OrderResult> {
  // Validate order items before processing
  // This catches issues like out-of-stock items or invalid quantities
  const validationResult = await validateOrderItems(order.items);
  if (!validationResult.valid) {
    return { success: false, errors: validationResult.errors };
  }

  // Calculate totals with tax and discounts
  // Note: Tax calculation is region-specific (see TaxService)
  const totals = calculateOrderTotals(order);

  // Reserve inventory to prevent overselling
  // Uses optimistic locking to handle concurrent orders
  const reservationId = await inventoryService.reserve(order.items, {
    timeout: 300, // 5 minutes to complete payment
  });

  try {
    // Process payment through the configured gateway
    // Supports multiple payment methods (see PaymentGateway interface)
    const payment = await paymentService.charge({
      amount: totals.total,
      currency: order.currency,
      method: order.paymentMethod,
    });

    // Commit the inventory reservation
    await inventoryService.commit(reservationId);

    // Create order record with all computed fields
    const savedOrder = await orderRepository.create({
      ...order,
      ...totals,
      paymentId: payment.id,
      status: 'confirmed',
    });

    // Send confirmation email asynchronously
    // Failure here shouldn't fail the order (fire-and-forget)
    emailService.sendOrderConfirmation(savedOrder).catch((error) => {
      logger.warn('Failed to send confirmation email', { orderId: savedOrder.id, error });
    });

    return { success: true, order: savedOrder };
  } catch (error) {
    // Release inventory reservation on failure
    await inventoryService.release(reservationId);
    throw error;
  }
}
```

## Documentation Generation

### TypeDoc Configuration

```json
// typedoc.json
{
  "entryPoints": ["src/index.ts"],
  "out": "docs",
  "excludePrivate": true,
  "excludeProtected": false,
  "includeVersion": true,
  "categorizeByGroup": true,
  "categoryOrder": [
    "Services",
    "Hooks",
    "Components",
    "Types",
    "Utilities"
  ],
  "plugin": [
    "typedoc-plugin-markdown",
    "typedoc-plugin-mermaid"
  ]
}
```

## Checklist

- [ ] All public exports have JSDoc
- [ ] Functions have @param and @returns
- [ ] Error cases documented with @throws
- [ ] At least one @example per function
- [ ] Complex logic has inline comments
- [ ] Types/interfaces fully documented
- [ ] @see links to related functions
- [ ] @since version tags for new APIs
- [ ] @deprecated for obsolete APIs
- [ ] Documentation generates without errors

