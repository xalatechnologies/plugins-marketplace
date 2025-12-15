---
description: Create intuitive, delightful, and user-friendly interactions
globs: ["**/*.tsx", "**/*.jsx"]
---

# Interactive UX Skill

> Every interaction should be intuitive, responsive, and delightful. Users should never be confused.

## UX Principles

```
┌─────────────────────────────────────────────────────────────────┐
│                    INTERACTIVE UX PYRAMID                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                        🎉 DELIGHT                               │
│                      Surprise & joy                              │
│                    ─────────────────                             │
│                    🎯 EFFICIENCY                                 │
│               Fast, optimized workflows                          │
│              ─────────────────────────                           │
│              🧭 DISCOVERABILITY                                  │
│          Features easy to find & understand                      │
│            ───────────────────────────                           │
│            💬 FEEDBACK                                           │
│        Every action has clear response                           │
│          ─────────────────────────────                           │
│          🔒 TRUST & SAFETY                                       │
│       Errors prevented, recovery easy                            │
│            ───────────────────────────                           │
│            ⚡ FUNCTIONAL                                         │
│          It works, it's reliable                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Feedback Patterns

### Immediate Visual Feedback

```tsx
// ✅ Button with complete feedback cycle
function SubmitButton({ onClick, children }: SubmitButtonProps) {
  const [state, setState] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const handleClick = async () => {
    setState('loading');
    try {
      await onClick();
      setState('success');
      // Reset after showing success
      setTimeout(() => setState('idle'), 2000);
    } catch {
      setState('error');
      setTimeout(() => setState('idle'), 3000);
    }
  };

  return (
    <button
      onClick={handleClick}
      disabled={state === 'loading'}
      className={cn(
        "relative flex items-center justify-center gap-2 px-6 py-3 rounded-lg",
        "font-medium transition-all duration-200",
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2",
        {
          'bg-primary text-white hover:bg-primary-hover': state === 'idle',
          'bg-primary/70 text-white cursor-wait': state === 'loading',
          'bg-green-500 text-white': state === 'success',
          'bg-red-500 text-white': state === 'error',
        }
      )}
    >
      {/* Icon transitions */}
      <span className="relative w-5 h-5">
        <Transition
          show={state === 'idle'}
          enter="transition-all duration-200"
          enterFrom="opacity-0 scale-50"
          enterTo="opacity-100 scale-100"
          leave="transition-all duration-200"
          leaveFrom="opacity-100 scale-100"
          leaveTo="opacity-0 scale-50"
        >
          <span className="absolute inset-0">{children}</span>
        </Transition>

        <Transition show={state === 'loading'}>
          <Spinner className="absolute inset-0 animate-spin" />
        </Transition>

        <Transition show={state === 'success'}>
          <CheckIcon className="absolute inset-0" />
        </Transition>

        <Transition show={state === 'error'}>
          <XIcon className="absolute inset-0" />
        </Transition>
      </span>

      {/* Text */}
      <span>
        {state === 'idle' && 'Submit'}
        {state === 'loading' && 'Submitting...'}
        {state === 'success' && 'Done!'}
        {state === 'error' && 'Failed'}
      </span>
    </button>
  );
}
```

### Form Inline Validation

```tsx
// ✅ Real-time validation with helpful hints
function EmailInput({ onValidChange }: EmailInputProps) {
  const [email, setEmail] = useState('');
  const [touched, setTouched] = useState(false);
  const [isChecking, setIsChecking] = useState(false);
  const [availability, setAvailability] = useState<'available' | 'taken' | null>(null);

  const validation = useMemo(() => {
    if (!email) return { valid: false, message: null };
    if (!email.includes('@')) return { valid: false, message: 'Please enter a valid email' };
    if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
      return { valid: false, message: 'Email format looks incorrect' };
    }
    return { valid: true, message: null };
  }, [email]);

  // Debounced availability check
  useEffect(() => {
    if (!validation.valid) {
      setAvailability(null);
      return;
    }

    setIsChecking(true);
    const timer = setTimeout(async () => {
      const available = await checkEmailAvailability(email);
      setAvailability(available ? 'available' : 'taken');
      setIsChecking(false);
      onValidChange?.(available ? email : null);
    }, 500);

    return () => clearTimeout(timer);
  }, [email, validation.valid]);

  return (
    <div className="space-y-2">
      <label htmlFor="email" className="block text-sm font-medium">
        Email Address
      </label>

      <div className="relative">
        <input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          onBlur={() => setTouched(true)}
          className={cn(
            "w-full px-4 py-3 pr-12 rounded-lg border-2 transition-colors",
            "focus:outline-none focus:ring-0",
            {
              'border-gray-200 focus:border-primary': !touched || validation.valid,
              'border-red-400 focus:border-red-500': touched && !validation.valid,
              'border-green-400': validation.valid && availability === 'available',
              'border-red-400': validation.valid && availability === 'taken',
            }
          )}
          aria-invalid={touched && !validation.valid}
          aria-describedby="email-feedback"
        />

        {/* Status indicator */}
        <div className="absolute right-3 top-1/2 -translate-y-1/2">
          {isChecking && <Spinner className="w-5 h-5 animate-spin text-gray-400" />}
          {!isChecking && availability === 'available' && (
            <CheckCircle className="w-5 h-5 text-green-500" />
          )}
          {!isChecking && availability === 'taken' && (
            <XCircle className="w-5 h-5 text-red-500" />
          )}
        </div>
      </div>

      {/* Feedback message */}
      <div id="email-feedback" className="min-h-[20px] text-sm" role="alert">
        {touched && validation.message && (
          <p className="text-red-600 flex items-center gap-1">
            <AlertCircle className="w-4 h-4" />
            {validation.message}
          </p>
        )}
        {validation.valid && availability === 'taken' && (
          <p className="text-red-600 flex items-center gap-1">
            <AlertCircle className="w-4 h-4" />
            This email is already registered.{' '}
            <Link href="/login" className="underline">Sign in instead?</Link>
          </p>
        )}
        {validation.valid && availability === 'available' && (
          <p className="text-green-600 flex items-center gap-1">
            <CheckCircle className="w-4 h-4" />
            Email is available!
          </p>
        )}
      </div>
    </div>
  );
}
```

## Discoverability Patterns

### Progressive Disclosure

```tsx
// ✅ Show advanced options only when needed
function SettingsPanel() {
  const [showAdvanced, setShowAdvanced] = useState(false);

  return (
    <div className="space-y-6">
      {/* Basic settings - always visible */}
      <section className="space-y-4">
        <h2 className="text-lg font-semibold">General Settings</h2>
        <SettingRow label="Language" setting="language" />
        <SettingRow label="Time Zone" setting="timezone" />
        <SettingRow label="Theme" setting="theme" />
      </section>

      {/* Advanced settings - expandable */}
      <div className="border-t pt-4">
        <button
          onClick={() => setShowAdvanced(!showAdvanced)}
          className="flex items-center gap-2 text-sm text-gray-600 hover:text-gray-900"
        >
          <ChevronDown
            className={cn(
              "w-4 h-4 transition-transform duration-200",
              showAdvanced && "rotate-180"
            )}
          />
          Advanced Settings
        </button>

        <AnimatePresence>
          {showAdvanced && (
            <motion.section
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: 'auto', opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="overflow-hidden"
            >
              <div className="pt-4 space-y-4">
                <SettingRow label="API Key" setting="apiKey" type="secret" />
                <SettingRow label="Webhook URL" setting="webhookUrl" />
                <SettingRow label="Rate Limiting" setting="rateLimit" />
              </div>
            </motion.section>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
```

### Contextual Help & Tooltips

```tsx
// ✅ Helpful tooltips that don't obstruct
function SettingWithHelp({ label, help, children }: SettingWithHelpProps) {
  return (
    <div className="flex items-center justify-between">
      <div className="flex items-center gap-2">
        <label className="text-sm font-medium">{label}</label>
        <Tooltip content={help}>
          <button
            className="text-gray-400 hover:text-gray-600 transition-colors"
            aria-label={`Help: ${label}`}
          >
            <HelpCircle className="w-4 h-4" />
          </button>
        </Tooltip>
      </div>
      {children}
    </div>
  );
}

// Tooltip component with smart positioning
function Tooltip({ content, children }: TooltipProps) {
  const [isOpen, setIsOpen] = useState(false);
  const triggerRef = useRef<HTMLElement>(null);

  return (
    <div className="relative inline-flex">
      <span
        ref={triggerRef}
        onMouseEnter={() => setIsOpen(true)}
        onMouseLeave={() => setIsOpen(false)}
        onFocus={() => setIsOpen(true)}
        onBlur={() => setIsOpen(false)}
      >
        {children}
      </span>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: 4 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 4 }}
            transition={{ duration: 0.15 }}
            className={cn(
              "absolute z-50 px-3 py-2 rounded-lg shadow-lg",
              "bg-gray-900 text-white text-sm max-w-xs",
              "bottom-full left-1/2 -translate-x-1/2 mb-2"
            )}
            role="tooltip"
          >
            {content}
            {/* Arrow */}
            <div className="absolute top-full left-1/2 -translate-x-1/2 border-4 border-transparent border-t-gray-900" />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

## Error Prevention & Recovery

### Destructive Action Confirmation

```tsx
// ✅ Two-step confirmation for dangerous actions
function DeleteButton({ onDelete, itemName }: DeleteButtonProps) {
  const [step, setStep] = useState<'idle' | 'confirm' | 'deleting'>('idle');

  const handleDelete = async () => {
    setStep('deleting');
    try {
      await onDelete();
      toast.success(`${itemName} deleted`);
    } catch (error) {
      toast.error('Failed to delete. Please try again.');
      setStep('idle');
    }
  };

  if (step === 'idle') {
    return (
      <button
        onClick={() => setStep('confirm')}
        className="px-3 py-1.5 text-sm text-red-600 hover:bg-red-50 rounded-md transition-colors"
      >
        Delete
      </button>
    );
  }

  return (
    <div className="flex items-center gap-2">
      <span className="text-sm text-gray-600">Are you sure?</span>
      <button
        onClick={handleDelete}
        disabled={step === 'deleting'}
        className="px-3 py-1.5 text-sm bg-red-600 text-white rounded-md hover:bg-red-700 disabled:opacity-50"
      >
        {step === 'deleting' ? 'Deleting...' : 'Yes, delete'}
      </button>
      <button
        onClick={() => setStep('idle')}
        disabled={step === 'deleting'}
        className="px-3 py-1.5 text-sm text-gray-600 hover:bg-gray-100 rounded-md"
      >
        Cancel
      </button>
    </div>
  );
}
```

### Undo Actions

```tsx
// ✅ Allow undo for reversible actions
function useUndoableAction<T>() {
  const [lastAction, setLastAction] = useState<{
    type: string;
    data: T;
    undo: () => Promise<void>;
  } | null>(null);

  const executeWithUndo = useCallback(async (
    actionType: string,
    data: T,
    execute: () => Promise<void>,
    undo: () => Promise<void>
  ) => {
    await execute();

    setLastAction({ type: actionType, data, undo });

    // Show toast with undo option
    toast.custom((t) => (
      <div className="flex items-center gap-4 bg-gray-900 text-white px-4 py-3 rounded-lg shadow-lg">
        <span>Item {actionType}d</span>
        <button
          onClick={async () => {
            await undo();
            toast.dismiss(t.id);
            toast.success('Action undone');
            setLastAction(null);
          }}
          className="px-2 py-1 bg-white/10 hover:bg-white/20 rounded text-sm font-medium transition-colors"
        >
          Undo
        </button>
      </div>
    ), { duration: 5000 });

    // Clear undo after timeout
    setTimeout(() => setLastAction(null), 5000);
  }, []);

  return { lastAction, executeWithUndo };
}

// Usage
const { executeWithUndo } = useUndoableAction<Item>();

const handleArchive = (item: Item) => {
  executeWithUndo(
    'archive',
    item,
    () => archiveItem(item.id),
    () => unarchiveItem(item.id)
  );
};
```

## Empty States

```tsx
// ✅ Helpful empty states that guide users
function EmptyState({
  icon: Icon,
  title,
  description,
  action,
}: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4 text-center">
      <div className="w-16 h-16 rounded-full bg-gray-100 flex items-center justify-center mb-4">
        <Icon className="w-8 h-8 text-gray-400" />
      </div>

      <h3 className="text-lg font-semibold text-gray-900 mb-2">
        {title}
      </h3>

      <p className="text-gray-600 max-w-sm mb-6">
        {description}
      </p>

      {action && (
        <Button onClick={action.onClick} variant="primary">
          {action.icon && <action.icon className="w-4 h-4 mr-2" />}
          {action.label}
        </Button>
      )}
    </div>
  );
}

// Usage
<EmptyState
  icon={FolderOpen}
  title="No projects yet"
  description="Get started by creating your first project. It only takes a minute."
  action={{
    label: 'Create Project',
    icon: Plus,
    onClick: () => openCreateDialog(),
  }}
/>
```

## Loading States

```tsx
// ✅ Skeleton loading that matches content shape
function TableSkeleton({ rows = 5 }: { rows?: number }) {
  return (
    <div className="border rounded-lg overflow-hidden">
      {/* Header */}
      <div className="bg-gray-50 px-6 py-3 border-b">
        <div className="flex gap-4">
          <Skeleton className="h-4 w-24" />
          <Skeleton className="h-4 w-32" />
          <Skeleton className="h-4 w-20" />
          <Skeleton className="h-4 flex-1" />
        </div>
      </div>

      {/* Rows */}
      {Array.from({ length: rows }).map((_, i) => (
        <div
          key={i}
          className="px-6 py-4 border-b last:border-b-0 flex items-center gap-4"
        >
          <Skeleton className="w-10 h-10 rounded-full" />
          <div className="flex-1 space-y-2">
            <Skeleton className="h-4 w-1/3" />
            <Skeleton className="h-3 w-1/4" />
          </div>
          <Skeleton className="h-6 w-16 rounded-full" />
          <Skeleton className="h-8 w-8 rounded" />
        </div>
      ))}
    </div>
  );
}

function Skeleton({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "animate-pulse bg-gray-200 rounded",
        className
      )}
    />
  );
}
```

## Keyboard Navigation

```tsx
// ✅ Full keyboard support for custom components
function SelectMenu({ options, value, onChange }: SelectMenuProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [focusIndex, setFocusIndex] = useState(-1);
  const listRef = useRef<HTMLUListElement>(null);

  const handleKeyDown = (e: KeyboardEvent) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        if (!isOpen) {
          setIsOpen(true);
          setFocusIndex(0);
        } else {
          setFocusIndex((i) => Math.min(i + 1, options.length - 1));
        }
        break;

      case 'ArrowUp':
        e.preventDefault();
        setFocusIndex((i) => Math.max(i - 1, 0));
        break;

      case 'Enter':
      case ' ':
        e.preventDefault();
        if (isOpen && focusIndex >= 0) {
          onChange(options[focusIndex]);
          setIsOpen(false);
        } else {
          setIsOpen(true);
        }
        break;

      case 'Escape':
        setIsOpen(false);
        break;

      case 'Home':
        e.preventDefault();
        setFocusIndex(0);
        break;

      case 'End':
        e.preventDefault();
        setFocusIndex(options.length - 1);
        break;
    }
  };

  return (
    <div className="relative" onKeyDown={handleKeyDown}>
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        aria-haspopup="listbox"
        aria-expanded={isOpen}
        className="w-full px-4 py-2 border rounded-lg text-left flex items-center justify-between"
      >
        <span>{value?.label || 'Select...'}</span>
        <ChevronDown className="w-4 h-4" />
      </button>

      {isOpen && (
        <ul
          ref={listRef}
          role="listbox"
          className="absolute z-10 w-full mt-1 bg-white border rounded-lg shadow-lg max-h-60 overflow-auto"
        >
          {options.map((option, index) => (
            <li
              key={option.value}
              role="option"
              aria-selected={value?.value === option.value}
              className={cn(
                "px-4 py-2 cursor-pointer",
                focusIndex === index && "bg-blue-50",
                value?.value === option.value && "font-medium"
              )}
              onClick={() => {
                onChange(option);
                setIsOpen(false);
              }}
              onMouseEnter={() => setFocusIndex(index)}
            >
              {option.label}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

## Checklist

- [ ] Every action has immediate visual feedback
- [ ] Loading states show progress or activity
- [ ] Error messages are helpful and actionable
- [ ] Destructive actions require confirmation
- [ ] Undo available for reversible actions
- [ ] Empty states guide users to next action
- [ ] Tooltips explain complex features
- [ ] Keyboard navigation complete
- [ ] Focus management correct in modals
- [ ] Form validation is real-time and helpful
- [ ] Progress indicators for multi-step flows
- [ ] Success states celebrate completion

