# Design System: Token Architecture & Figma Guide

## How This Works

```
┌──────────────┐    export    ┌──────────────┐    link    ┌──────────────┐
│  Figma       │ ──────────>  │  tokens.css  │ <──────── │ components   │
│  Variables   │              │  (source of  │           │ .css         │
│              │              │   truth)     │           │              │
└──────────────┘              └──────────────┘           └──────────────┘
  Designer edits                Both reference             Engineer uses
  visual decisions              the same names             in demo HTML
```

**You** change how things look by editing Figma variables (or tokens.css directly).
**The engineer** never touches visual values — only structural HTML/Jinja and JS.
**Claude Code** reads tokens.css to understand available design decisions.

---

## File Inventory

| File | Role | Who edits |
|------|------|-----------|
| `tokens.css` | Every visual decision: colors, type, spacing, radii, shadows | Designer |
| `components.css` | Every component style, referencing only tokens | Engineer (structure only) |
| This README | Architecture documentation | Both |

---

## Figma Variable Collections to Create

Set up these collections in Figma. Each collection maps to a section in tokens.css.

### Collection 1: Primitives
These are your raw palette. Don't use them directly on frames — they feed into semantic tokens.

**Group: grey/**
| Variable | Value | CSS token |
|----------|-------|-----------|
| grey/0 | #ffffff | --grey-0 |
| grey/50 | #fafafa | --grey-50 |
| grey/100 | #f5f5f5 | --grey-100 |
| grey/150 | #f0f0f0 | --grey-150 |
| grey/200 | #e5e7eb | --grey-200 |
| grey/300 | #d1d5db | --grey-300 |
| grey/400 | #9ca3af | --grey-400 |
| grey/500 | #6b7280 | --grey-500 |
| grey/600 | #4b5563 | --grey-600 |
| grey/700 | #374151 | --grey-700 |
| grey/800 | #1f2937 | --grey-800 |
| grey/900 | #111827 | --grey-900 |
| grey/950 | #0b0d0f | --grey-950 |

**Group: green/** (success/routine)
| Variable | Value | CSS token |
|----------|-------|-----------|
| green/50 | #f0fdf4 | --green-50 |
| green/100 | #d1fae5 | --green-100 |
| green/500 | #10b981 | --green-500 |
| green/600 | #059669 | --green-600 |
| green/700 | #047857 | --green-700 |
| green/800 | #065f46 | --green-800 |

**Group: amber/** (warning/attention)
| Variable | Value | CSS token |
|----------|-------|-----------|
| amber/50 | #fffbeb | --amber-50 |
| amber/100 | #fef3c7 | --amber-100 |
| amber/500 | #f59e0b | --amber-500 |
| amber/600 | #d97706 | --amber-600 |
| amber/800 | #92400e | --amber-800 |

**Group: red/** (danger/high)
| Variable | Value | CSS token |
|----------|-------|-----------|
| red/50 | #fef2f2 | --red-50 |
| red/100 | #fee2e2 | --red-100 |
| red/200 | #fca5a5 | --red-200 |
| red/500 | #ef4444 | --red-500 |
| red/600 | #dc2626 | --red-600 |
| red/700 | #b91c1c | --red-700 |
| red/800 | #991b1b | --red-800 |

**Group: blue/** (accent/interactive)
| Variable | Value | CSS token |
|----------|-------|-----------|
| blue/50 | #eff6ff | --blue-50 |
| blue/100 | #dbeafe | --blue-100 |
| blue/500 | #3b82f6 | --blue-500 |
| blue/600 | #2563eb | --blue-600 |
| blue/700 | #1e40af | --blue-700 |

### Collection 2: Semantic (what you actually use on designs)
These reference primitives. Use THESE on your Figma frames.

**Group: surface/**
| Variable | References | CSS token |
|----------|-----------|-----------|
| surface/bg | grey/100 | --surface-bg |
| surface/primary | grey/0 | --surface-primary |
| surface/secondary | grey/50 | --surface-secondary |
| surface/tertiary | grey/150 | --surface-tertiary |

**Group: text/**
| Variable | References | CSS token |
|----------|-----------|-----------|
| text/primary | grey/900 | --text-primary |
| text/secondary | grey/500 | --text-secondary |
| text/tertiary | grey/400 | --text-tertiary |
| text/inverse | grey/0 | --text-inverse |
| text/link | blue/600 | --text-link |

**Group: border/**
| Variable | References | CSS token |
|----------|-----------|-----------|
| border/default | grey/200 | --border-default |
| border/subtle | rgba(0,0,0,0.05) | --border-subtle |

**Group: status/**
| Variable | References | CSS token |
|----------|-----------|-----------|
| status/success | green/500 | --status-success |
| status/success-bg | green/100 | --status-success-bg |
| status/warning | amber/600 | --status-warning |
| status/warning-bg | amber/100 | --status-warning-bg |
| status/danger | red/600 | --status-danger |
| status/danger-bg | red/100 | --status-danger-bg |

**Group: accent/**
| Variable | References | CSS token |
|----------|-----------|-----------|
| accent/default | blue/600 | --accent |
| accent/bg | blue/100 | --accent-bg |

### Collection 3: Component
Map directly to UI element properties.

| Variable | Value | CSS token |
|----------|-------|-----------|
| card/radius | 16px | --card-radius |
| card/radius-sm | 8px | --card-radius-sm |
| card/padding | 16px | --card-padding |
| card/shadow | 0 4px 20px rgba(0,0,0,0.06) | --card-shadow |
| button/radius | 8px | --button-radius |
| badge/radius | 10px | --badge-radius |
| topbar/height | 56px | --topbar-height |
| sidebar/width | 220px | --sidebar-width |

---

## How to Reskin the Demo

### Quick method (edit tokens.css directly):
1. Open `tokens.css`
2. Change values in the `:root` semantic section
3. Save → demo updates immediately

### Example: switch to a blue corporate theme
```css
/* In tokens.css, change these semantic tokens: */
--surface-bg: #f0f4f8;
--bg-gradient: linear-gradient(135deg, #dbe4f0 0%, #e8edf5 50%, #f5f5f5 100%);
--text-primary: #1e3a5f;
--accent: #1a56db;
--card-radius: 8px;        /* sharper corners */
--font-sans: 'IBM Plex Sans', sans-serif;
--heading-font: 'IBM Plex Sans', sans-serif;
```

That's it. Every card, button, badge, sidebar, and heading in the demo updates.

### Full method (Figma → CSS):
1. Update variables in Figma
2. Export via Tokens Studio plugin → JSON
3. Run transform script (to be built) → tokens.css
4. Engineer pulls updated tokens.css

---

## For Claude Code

When asked to build a UI component, Claude Code should:

1. **Read tokens.css first** to know what values are available
2. **Never hardcode** a color, font-size, radius, or shadow
3. **Always reference** a semantic token (e.g., `var(--surface-primary)` not `#ffffff`)
4. **If a token doesn't exist**, add it to the appropriate section in tokens.css
5. **Follow the naming pattern**: `--{category}-{role}` for semantics, `--{scale}-{step}` for primitives

### Token naming convention:
```
Primitives:  --{color}-{shade}     e.g. --grey-500, --blue-600
Semantics:   --{role}-{variant}    e.g. --surface-primary, --status-danger-bg
Components:  --{component}-{prop}  e.g. --card-radius, --topbar-height
```

---

## Inline Style Cleanup

The original demo has ~71 inline `style=""` attributes in the HTML.
These should be migrated to CSS classes over time.
For now, the refactored components.css covers all class-based styles.
Inline styles on specific elements (e.g., sidebar patient dots) remain
as-is since they're structural/dynamic, not theming.
