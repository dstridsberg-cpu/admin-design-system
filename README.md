# Admin Design System

## Opening the demo

Just open `bogdan-demo-rendered.html` directly in your browser. No server needed.

---

## Opening the component showcase

The showcase requires Flask (Python) to run because the components are Jinja2 macros.

```bash
# First time only — install Flask
pip3 install -r "-showcase/requirements.txt"

# Start the server (full path needed — leading dash confuses Python otherwise)
python3 "$PWD/-showcase/app.py"
```

Then open **http://localhost:5001** in your browser.

---

## Making design changes

Edit `-styles/tokens.css` — this is the only file you need for most visual changes. Refresh the browser to see updates.

Only touch `-styles/components.css` if a specific component needs styling that tokens can't cover.

---

## Using icons

Icons use [Lucide](https://lucide.dev/icons/) — the same library as Linear. Add this script tag to any new demo:

```html
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
```

Then use icons like this:

```html
<i data-lucide="settings" class="icon"></i>
```

Call `lucide.createIcons()` once after the DOM is ready (at the end of your script block).

Browse all icon names at [lucide.dev/icons](https://lucide.dev/icons/).

Size and stroke weight are controlled by tokens:
- `--icon-size-sm` / `--icon-size-md` / `--icon-size-lg`
- `--icon-stroke`

Use `.icon-sm` or `.icon-lg` CSS classes for size variants.

---

## File overview

| File | What it is |
|---|---|
| `bogdan-demo-rendered.html` | The demo — open directly in browser |
| `-styles/tokens.css` | All design decisions: colors, spacing, type, radius, shadows |
| `-styles/components.css` | Component-level styles, references tokens |
| `-showcase/app.py` | Starts the showcase server |
| `-showcase/templates/showcase.html` | The component showcase page |
| `-showcase/templates/components/` | Reusable component macros (atoms, molecules, organisms) |
| `-docs/` | Design analysis documents |
