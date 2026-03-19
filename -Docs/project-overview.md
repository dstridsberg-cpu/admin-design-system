# Admin Design System — Project Overview

## What is this?

A design system for **Admin**, an AI-powered clinical supervision platform. Admin lets physicians supervise autonomous AI agents handling patient encounters — reviewing actions, approving decisions, and stepping in when needed.

This design system defines the visual language for Admin's supervisor-facing interfaces: the tokens, components, and patterns that make up the UI.

## Why are we building it?

The product is early-stage. Rather than designing screens in isolation, we're building a shared foundation — tokens, components, a live showcase — so that new screens can be assembled quickly and consistently without reinventing decisions each time.

The showcase also serves as a living reference: what does a button look like? What's our heading scale? What color means "warning"? It answers these questions in the browser, with real rendered output, not static mockups.

## Where did it come from?

The design system grew out of a working prototype built by Bogdan — a fully functional interactive demo of the Supervisor Console, written as a single self-contained HTML file with all styles defined inline in a `<style>` block.

The inline approach was fine for prototyping, but it made visual control difficult: changing a color or font size meant hunting through hundreds of hardcoded values scattered across the file. There was no single place to make a design decision — every change had to be applied manually, in multiple places, with no guarantee of consistency.

The first major step was extracting all of those inline styles into two separate CSS files: `tokens.css` and `components.css`. Every hardcoded color, font size, spacing value, border radius, and shadow was replaced with a CSS custom property (a variable). This meant that a decision like "what is our primary text color?" now lives in exactly one place — and changing it updates the entire interface instantly.

This gave the designer (rather than just the developer) direct control over the visual language. Adjusting the type scale, redefining a color, or changing the border radius of cards is now a one-line edit in `tokens.css`, with no risk of missing an instance.

## What does it consist of?

**Two CSS files** drive everything:
- `-styles/tokens.css` — all design decisions as variables: color, type scale, spacing, radius, shadows, icons
- `-styles/components.css` — all UI components, built entirely from those tokens

Any page that links both files in order gets the full design system. Visual changes are made exclusively in these files — the HTML never needs to change for a design update.

This approach was chosen for designer control. Having all styles in two predictable files makes it straightforward to find, change, and reason about any visual decision without touching component markup. Anton has noted that the longer-term ambition is to allow macros to carry their own inline CSS using CSS variables — keeping styles closer to the component they belong to. For now, the centralised two-file approach is the right tradeoff: it's simpler to manage and gives the designer a clear single place to work.

**A showcase** (`-showcase/`) — a Flask-served HTML page that documents every token and component with live rendered examples and usage specs. Think of it as a Storybook, but simpler. Served locally at `localhost:5001`.

**A demo** (`bogdan-demo-rendered.html`) — Bogdan's original prototype, now refactored to consume the design system. It's a standalone HTML file (no server needed) showing the Supervisor Console working end-to-end: live agent activity, patient encounters, approvals, analytics, and configuration.

### Jinja compatibility

The showcase and its components are built with **Jinja2** templating, served by a small Flask app. Each UI component is a Jinja macro — a reusable template function that accepts parameters and renders HTML. This means components are defined once and can be composed to build new screens, much like a component library in React or SwiftUI, but staying entirely within HTML and CSS.

For example, the top bar is a single macro call:
```
{{ top_bar(active_autonomy=2, active_speed='1') }}
```

The macro handles all the internal structure. Changing how the top bar looks means editing the macro and the CSS — every screen using it updates automatically.

This architecture means the design system can grow into a real front-end framework for Admin's UI: new screens are assembled from existing macros, styled by existing tokens, with no redundant code.

## Where are we as of 2026-03-19?

The foundation is in place. The token system is mature, the component library covers the core UI patterns, and the showcase documents both. The demo is a credible, interactive representation of the actual product.

### Tokens
A full token system exists across: color (primitives + semantic), typography, spacing, radius, shadows, icon sizing, and component-level aliases. Colors follow a 3-step severity scale (green → amber → red) and an 8-step autonomy scale (L0–L4).

### Typography
- Two typefaces: **Aktiv Grotesk** (UI) and **Tiempos Headline Light** (brand accents)
- A complete H1–H6 heading scale with defined sizes, weights, and letter-spacing
- 12 named text styles covering every recurring text role in the interface
- Heading weight is Medium (500) throughout; Bold has been removed from the system

### Components
The component library covers atoms, molecules, and organisms — badges, buttons, inputs, pills, status indicators, feed items, approval cards, patient cards, nav items, toasts, the top bar, and the sidebar.

### Demo
The Supervisor Console demo shows the product working: live agent activity, a patient panel with three concurrent encounters, an approvals queue, analytics, and configuration. It uses the design system's tokens and components directly.

### Showcase
The showcase documents all of the above with live rendered output. It is served locally at `localhost:5001`.

## What's still missing?

- **Aktiv Grotesk** is not yet loaded from a real font source — the UI currently falls back to system sans-serif. This is the single biggest visual gap.
- No mobile or responsive work has been done.
- Dark mode is defined in tokens but not tested in the demo.
