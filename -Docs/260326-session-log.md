# Session Log — 2026-03-26

## Project
Admin Design System — `admin-design-system/`
Showcase runs locally via Flask at `localhost:5001` (`-showcase/app.py`)
Demo file: `bogdan-demo-rendered.html` (standalone, no server needed)

---

## What we worked on today

### 1. Fix Jinja2 TemplateSyntaxError in side_panel.html
- `{% macro side_panel(...) caller %}` is invalid Jinja2 syntax — `caller` cannot appear on the definition line
- Fixed by removing `caller` from the macro definition: `{% macro side_panel(...) %}`

### 2. Showcase intro — dark hero banner
- Replaced plain intro section with a two-column dark hero banner (`.sc-hero`)
- Left column: brand logo + "Design System 1.0" heading, Body Large description paragraph, meta table
- Right column: background image (embedded as base64)
- Introduced **Body Large** text style: `--text-2xl`, weight 400, line-height 1.5
- Description text max-width set to 580px for controlled line breaking
- Hero left padding: 120px → 160px (more space above logo)
- Logo `margin-top` nudged from 5px → 7px for alignment with "Design System 1.0" text

### 3. brand.html — new reusable brand atom
- Created `-showcase/templates/components/atoms/brand.html` with two macros:
  - `brandmark(width=24, height=19, extra_classes='')` — the A-mark icon
  - `wordmark(width=54, height=10, extra_classes='')` — the "admin." logotype
- Both use inline SVG with `fill="currentColor"` — automatically adapts to light/dark mode via parent text color
- No CSS filter hacks, no external URLs, no base64 duplication
- Imported and used in `top_bar.html` and `showcase.html` (hero logo + nav logo/wordmark)

### 4. Reasoning Trace side panel (bogdan-demo-rendered.html)
- Replaced the old reasoning trace column inside the encounter layout with a proper app-level side panel
- Panel (`#reasoningPanel`) sits as a sibling to `#activityPanel` at `.app` level, uses same `.activity-col` structure and `has-activity-col` grid mechanism
- Available only on the individual patient encounter view (not the patients list/rollout page)
- `toggleReasoningPanel()` / `renderReasoningPanel()` functions added
- Reopen button added to patient header, same pattern as Activity and Timeline panels

### 5. Timeline panel — reopen button on Pending Approvals
- When closing the Timeline side panel on the Pending Approvals page there was no button to bring it back
- Added `.activity-toggle-btn` reopen button to the Pending Approvals view header, matching the Activity panel pattern
- All reopen buttons now targeted via `querySelectorAll('.activity-toggle-btn')` (not a single `getElementById`)

### 6. Light / Dark mode switcher on Configuration page
- Added Appearance section at the top of the Config page with Light / Dark toggle buttons (sun / moon icons)
- `setTheme(theme)` function: toggles `body.dark` class, re-renders config, calls `lucide.createIcons()`

### 7. Dark mode fixes
Multiple hardcoded values replaced with semantic tokens that have proper dark overrides:

| Issue | Fix |
|---|---|
| Logo/wordmark bright in dark mode | Replaced `<img>` with inline SVG `currentColor` (brand.html atom) |
| Escalation banner bright pink | `background: var(--red-100)` → `var(--status-danger-bg)` |
| `attentionPulse` / `pulse-red` animations bright pink | Replaced hardcoded `var(--red-100)` / `#fecaca` in `@keyframes` with `var(--status-danger-bg)` + opacity variation |
| Progress bar very bright | `background: var(--grey-200)` → `var(--border-strong)` |
| Agent active pill bright green | All hex colors → `var(--status-success-bg)`, `var(--status-success-text)` etc. |
| View count missing border | `rgba(0,0,0,0.08)` → `var(--border-strong)` |
| Count badge number not white | `color: var(--text-inverse)` → `var(--text-on-dark)` |
| Light/Dark icons not showing | Added `lucide.createIcons()` call after `renderConfig()` |
| Status/tier backgrounds too bright | Added dark mode rgba overrides (28% opacity) for all tier and status-danger tokens in `tokens.css` |

### 8. Onboarding modal photo
- Updated onboarding modal photo to new image provided by user
- Embedded as base64 data URI — no external file attachments needed

### 9. Overlay logo fade-in animation restored (bogdan-demo-rendered.html)
- `.overlay-logo` was using an expiring Figma MCP URL — element was invisible, breaking the `overlayFadeIn` animation
- Replaced `<img>` with inline SVG using same paths as the `wordmark()` macro, `fill="currentColor"`, `width="119" height="22"`
- Animation now works correctly; logo adapts to light/dark mode

### 10. Showcase section titles — brand font
- `.sc-section-title` (Tokens, Atoms, Molecules, Organisms headings) now use `var(--brand-font)`, `font-weight: 300`, `font-size: var(--text-7xl)`

### 11. Showcase side nav icons
- Added Lucide icons to all top-level nav items:

| Nav item | Icon |
|---|---|
| Introduction | `book-open` |
| Color | `palette` |
| Typography | `type` |
| Spacing | `ruler` |
| Radius | `radius` |
| Shadow | `layers` |
| Animations | `sparkles` |
| Icons | `grid-2x2` |
| Atoms | `atom` |
| Molecules | `boxes` |
| Organisms | `component` |

- Added `.sc-nav-group-label` wrapper (flex, `gap: 8px`) for icon + text alignment
- "Overview" renamed to "Introduction"

---

## Architecture notes

### Brand assets
- Single source of truth: `-showcase/templates/components/atoms/brand.html`
- Jinja2 templates (showcase, top_bar) import and use `{{ brandmark() }}` / `{{ wordmark() }}` — logo changes propagate automatically
- `bogdan-demo-rendered.html` has SVG paths hardcoded inline (static file, manual sync needed if logo changes)

### App-level side panels
All three panels (Activity, Timeline, Reasoning Trace) share the same mechanism:
- `.activity-col` aside at `.app` grid level (column 3)
- `.app.has-activity-col` extends grid to `var(--sidebar-width) 1fr 476px`
- `switchView()` shows/hides the appropriate panel and toggles `has-activity-col`
- Reopen buttons use class `.activity-toggle-btn` (targeted via `querySelectorAll`)

---

## Files changed this session
- `-showcase/templates/components/atoms/brand.html` (new)
- `-showcase/templates/components/organisms/side_panel.html` (new — Jinja2 fix)
- `-showcase/templates/components/molecules/view_header.html` (new)
- `-showcase/templates/components/organisms/top_bar.html`
- `-showcase/templates/showcase.html`
- `-styles/components.css`
- `-styles/tokens.css`
- `bogdan-demo-rendered.html`
