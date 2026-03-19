# Admin Design System — Project Overview

## What is this?

A design system for **Admin**, an AI-powered clinical supervision platform. Admin lets physicians supervise autonomous AI agents handling patient encounters — reviewing actions, approving decisions, and stepping in when needed.

This design system defines the visual language for Admin's supervisor-facing interfaces: the tokens, components, and patterns that make up the UI.

## Why are we building it?

The product is early-stage. Rather than designing screens in isolation, we're building a shared foundation — tokens, components, a live showcase — so that new screens can be assembled quickly and consistently without reinventing decisions each time.

The showcase also serves as a living reference: what does a button look like? What's our heading scale? What color means "warning"? It answers these questions in the browser, with real rendered output, not static mockups.

## What does it consist of?

**Two CSS files** drive everything:
- `tokens.css` — all design decisions as variables: color, type scale, spacing, radius, shadows, icons
- `components.css` — all UI components, built entirely from those tokens

**A showcase** (`-showcase/`) — a Flask-served HTML page that documents every token and component with live rendered examples and usage specs. Think of it as a Storybook, but simpler.

**A demo** (`bogdan-demo-rendered.html`) — a standalone interactive prototype of the Supervisor Console: the main product surface. Physicians can watch AI agents work through patient encounters, approve actions, and manage multiple cases simultaneously.

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
