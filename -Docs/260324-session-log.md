# Session Log — 2026-03-24

## Project
Admin Design System — `admin-design-system/`
Showcase runs locally via Flask at `localhost:5001` (`-showcase/app.py`)
Demo file: `bogdan-demo-rendered.html` (standalone, no server needed)

---

## What we worked on today

### 1. Showcase left nav — restyled to match demo sidebar
- Changed background to `--surface-sidebar`, border to `--border-strong`
- Width fixed to 240px (matching demo sidebar)
- Nav items: flat rows with `border-bottom`, inset 2px left shadow for active/hover state
- Group headers (Color, Typography, Atoms, Molecules, Organisms) made clickable `<a>` tags
- Sub-level links styled as `.encounter-nav-item` equivalents: smaller text, shorter row height
- Added `scroll-behavior: smooth` on `html, body`
- Added `scroll-margin-top: 68px` on `.sc-section`, `.sc-component`, `.sc-variant` to offset sticky topbar on anchor nav
- Scrollspy updated to include group header `<a>` elements

### 2. Feed Item — multiple Figma sync iterations (node 39:1526 → 32:227)

#### Structure
- **Patient col** split into two sub-columns: Person (name, chief) + Vitals (2×2 grid)
- Person col: user icon (18px, `--text-tertiary`) + "Patient:" label + name/age, chief complaint below with `gap: 32px`
- Vitals: switched from `display: flex; flex-wrap: wrap` → `display: grid; grid-template-columns: repeat(2, 1fr)` — true CSS 2×2 grid; borders via `nth-child` selectors
- **Agent col**: "Agent:" label + timestamp heading row (no gap to title below), then `feed-agent-texts` (title + badges), then reasoning paragraph — all within `.feed-agent-text-group` wrapper
- Progress bar: 4px at bottom of card, `transition: width 0.4s ease`

#### Key CSS classes added/changed
| Class | Notes |
|---|---|
| `.feed-person-patient` | flex, `align-items: flex-end`, `gap: 10px` — icon + headings |
| `.feed-person-headings` | flex-col, `gap: 4px` — Patient: label + name |
| `.feed-vitals` | `display: grid; grid-template-columns: repeat(2, 1fr)` |
| `.feed-agent-text-group` | flex-col, no gap — wraps heading + texts |
| `.feed-agent-heading` | no `margin-bottom` (was 8px) — sits flush above title |
| `.feed-agent-reasoning` | 12px regular, secondary color, line-height 1.4 |

#### Jinja2 macro gotchas discovered
- `vitals={}` as default param silently truncates all subsequent parameters — always use `vitals=none`
- Positional args beyond param index conflict with keyword args of the same name — removed stray positional `time_display` from all showcase calls

### 3. Activity Feed — one card per patient
Changed `renderFeed` from showing one card per event (N events = N cards) to one card per patient, always reflecting the latest event for that patient:
- `latestByPatient` map: iterates `state.feedItems` chronologically, last event per patient wins
- Live patients: last `_actions` entry used
- New patients append to the list; existing cards updated in-place
- `data-patient-id` attribute on each card for stable DOM identification

### 4. In-place feed card updates — no flash
Split rendering into `buildFeedCardHtml(pid, item)` and `buildAgentContentHtml(item)`. On update:
- Patient col (name, vitals, chief) is **never touched**
- Agent col updated via targeted DOM writes, not `innerHTML` replacement
- Current values tracked as `data-feed-title`, `data-feed-status`, `data-feed-pct`, `data-feed-reasoning` on the card element — only changed fields update
- Removed `animation: slideIn` from `.feed-item`

### 5. Feed update transitions — staggered fade
- **Title** (`.feed-agent-title`): fades — 0ms delay
- **Status + confidence badges**: update instantly (no animation)
- **Reasoning** (`.feed-agent-reasoning`): fades — 70ms delay
- Fade curve: 120ms `ease-in` out → 550ms `ease-out` in (fast leave, slow arrive)
- Timeout buffer: 140ms (slightly longer than 120ms fade-out) to ensure swap never happens mid-transition
- Reasoning appear/disappear: same curve, fades in on `requestAnimationFrame` after DOM insert

### 6. Analytics — Action Distribution by Risk Tier chart fixed
- `tierColor()` was referencing `--t1`/`--t2`/`--t3`/`--t4` which don't exist
- Corrected to `--tier-1` / `--tier-2` / `--tier-3` / `--tier-4` (matching tokens.css)
- Same fix applied to the legend colour swatches in the HTML

### 7. Activity column — full-height right panel
- Added `<aside class="activity-col">` as a direct child of `.app` (CSS grid column 3, not inside `<main>`)
- `.app.has-activity-col` extends the grid: `grid-template-columns: var(--sidebar-width) 1fr 476px`
- `switchView` toggles `.has-activity-col` on `.app` and shows/hides the panel; only visible on the feed view
- Panel contains: heading, 2-col metrics grid, two-column bar chart (bars + legend)
- Width 476px, header padding 40px — matches Figma node 32:102
- Feed view header gets `margin-bottom: 40px` so first card top-border aligns with Activity header bottom-border

### 8. Live Consultations heading + count badge
- Feed view heading changed from "Activity" → "Live Consultations"
- `<span class="feed-count-badge" id="feedCountBadge">` added next to heading; count updates via `renderFeed()`
- View switcher right-aligned with `margin-left: auto`

### 9. Time metric card — independent wall-clock ticking
- `state.simTime` is a sim-tick counter, not real elapsed time
- Added `state.simStartWall`, `state.simPausedMs`, `state.simPauseStartedAt` to track real wall time
- `startSimulation()` records `Date.now()` on first run; `togglePause()` accumulates paused duration
- Separate 1s `setInterval` updates `#activityTimeValue` and `#analyticsTimeValue` directly, bypassing the render cycle

### 10. Metric count-up animation
- `parseAnimatable(str)` — returns `{ num, suffix }` for plain integers and `"N%"` strings; returns `null` for anything else (Encounters `"1/3 + 0"`, Time `"0:12"` are excluded automatically)
- `animateCountUp(el, oldStr, newStr)` — 600ms cubic ease-out via `requestAnimationFrame`
- `metricLastValues` map keyed by `data-metric-key` attribute — stable across `innerHTML` replacements
- `applyMetricAnimations(grid)` called after each metrics grid render

### 11. Animated tier bar chart
- `updateTierChart(chartId, tierCounts, maxCount, opts)` — unified helper for both Activity panel (`feedTierChart`) and Analytics page (`tierChart`)
- First render: builds bars at `height:0`, then `requestAnimationFrame` sets target heights → enter animation
- Subsequent renders: finds `[data-tier-bar]` elements and updates `height` in-place; CSS `transition: height 0.5s ease-out` animates the change
- Replaced old `chart.innerHTML = [...].join('')` calls in `renderActivitySidebar` and `renderAnalytics`

### 12. Broken token names fixed in demo
All occurrences replaced globally:
| Old (broken) | Correct |
|---|---|
| `--text-muted` | `--text-tertiary` |
| `--danger` | `--status-danger` |
| `--danger-light` | `--status-danger-bg` |
| `--success` | `--status-success` |
| `--warning` | `--status-warning` |
| `--border` | `--border-default` |

### 13. Button border-radius unified
- All buttons (`.btn`, `.btn-lg`, `.overlay-cta`) now use `var(--radius-lg)`
- Welcome modal width updated to 1060px, height 580px

### 14. Showcase — unused components removed
Deleted from Showcase (not used in demo):
- `section_label` (atom)
- `code_label` (atom)
- `kbd_hint` (atom) + `.kbd-hint` CSS removed from `components.css`
- `alert_banner` / `paused_banner` (molecule) + showcase-only `.sc-show-banner` hack removed

Nav counts updated: Atoms 9→6, Molecules 8→7. Four template files deleted.

---

## Current state of the system

### Token files
| File | Purpose |
|---|---|
| `-styles/tokens.css` | All design tokens — primitives → semantic → component |
| `-styles/components.css` | All component styles, consumes tokens |

### Key feed rendering architecture
| Function | Role |
|---|---|
| `buildFeedCardHtml(pid, item)` | Full card HTML for first-time patient appearance |
| `buildAgentContentHtml(item)` | Agent col inner HTML (used only for initial render) |
| `renderFeed()` | Diffs `latestByPatient` against DOM; updates in-place or creates |
| `feedFade(el, updateFn, delay)` | Fade-out → swap → fade-in helper with stagger delay |
| `updateTierChart(chartId, counts, max, opts)` | Animated bar chart — enter animation + in-place updates |
| `applyMetricAnimations(grid)` | Count-up animation on metric value changes |

### Token name patterns
- Tier colours: `--tier-1` through `--tier-4`
- Status colours: `--status-danger`, `--status-warning`, `--status-success` (no shorthand aliases)
- Text: `--text-primary`, `--text-secondary`, `--text-tertiary` (no `--text-muted`)
- Borders: `--border-default`, `--border-subtle`, `--border-strong` (no `--border`)

---

## What's not done / possible next steps
- Aktiv Grotesk font still not loaded from a reliable source (falls back to system sans-serif)
- Feed card ordering is insertion-order stable — no re-sorting as events fire
- Live patient feed cards use `livePatients[pid]` for demographics; sim patients use `SIM_PATIENTS[pid]`
- No dark mode testing done

---

## Files changed this session
- `-styles/components.css`
- `-styles/tokens.css`
- `-showcase/templates/showcase.html`
- `-showcase/templates/components/molecules/feed_item.html`
- `-showcase/templates/components/molecules/metric_card.html`
- `-showcase/templates/components/molecules/nav_item.html`
- `-showcase/templates/components/molecules/dropdown_menu.html` (new)
- `-showcase/templates/components/atoms/status_indicator.html`
- `-showcase/templates/components/atoms/view_icons.html` (new)
- `-showcase/templates/components/organisms/sidebar.html`
- `-showcase/templates/components/organisms/top_bar.html`
- `-showcase/templates/components/atoms/section_label.html` (deleted)
- `-showcase/templates/components/atoms/code_label.html` (deleted)
- `-showcase/templates/components/atoms/kbd_hint.html` (deleted)
- `-showcase/templates/components/molecules/alert_banner.html` (deleted)
- `bogdan-demo-rendered.html`
