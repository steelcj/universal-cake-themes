---
Title: "Stijl Standard MkDocs Conversion Plan"
Description: "A clear, layered plan for converting the Stijl Standard layout into a MkDocs Material + mkdocs-static-i18n 1.2.3 compatible theme layer."
Author: "Christopher Steel"
Date: "2026-03-02"
License: "CC BY-SA 4.0"
Tags:
  - "mkdocs"
  - "mkdocs-material"
  - "mkdocs-static-i18n"
  - "theme-conversion"
  - "stijl-standard"
---

# Stijl Standard → MkDocs Material Conversion Plan

This document defines a clear, maintainable plan for converting **Stijl Standard** into a production-ready MkDocs theme layer using:

- **MkDocs**
- **MkDocs Material**
- **mkdocs-static-i18n (v1.2.3)**

The resulting theme will be named:

```
stijl-standard-mkdocs
```

This plan is intentionally layered to avoid technical debt.

---

# Guiding Principles

1. **Material remains the layout engine**
2. **Stijl Standard becomes a design layer**
3. **No forking of Material templates**
4. **No layout engine replacement**
5. **Use CSS tokens and scoped overrides**
6. **Preserve upgrade compatibility**
7. **Fully compatible with mkdocs-static-i18n**

---

# Current Facts (Baseline Reality)

Stijl Standard currently provides:

- 6-column desktop grid
- 4-column tablet breakpoint (≤ 1024px)
- Single-column mobile collapse (≤ 600px)
- Primary color blocks
- Structural spacing token (`--line`)
- Pure HTML + CSS
- No JS
- No accessibility tuning
- No generator awareness

Material already provides:

- Responsive layout system
- Navigation drawer
- Header behavior
- Search
- Accessibility baseline
- Dark mode
- Page layout structure

Therefore:

We do **not** port the grid engine.
We port the visual identity and block layout pattern.

---

# High-Level Architecture

```
MkDocs
└── Material (engine)
    └── stijl-standard-mkdocs (design layer)
```

---

# Phase 1 — Directory Structure

Create a clean override structure:

```
overrides/
├── styles/
│   ├── uc-tokens.css
│   ├── stijl-standard.css
│   └── stijl-components.css
├── partials/
│   └── homepage.html
└── main.html (minimal extension only if required)
```

Important:

- Do not copy Material’s main.html unless strictly necessary.
- Keep overrides surgical.

---

# Phase 2 — Token Extraction

Extract Stijl variables into a dedicated token file:

## uc-tokens.css

```css
:root {
  --uc-black: #000;
  --uc-white: #ffffff;
  --uc-red: #d00000;
  --uc-blue: #0033cc;
  --uc-yellow: #f2c200;
  --uc-line: 10px;
}
```

Do not override Material layout yet.

---

# Phase 3 — Scoped Stijl Layout Blocks

Instead of replacing Material’s article layout, create a scoped container:

Example:

```html
<div class="uc-stijl-grid">
  <section class="uc-block uc-red">...</section>
</div>
```

Define grid only inside `.uc-stijl-grid`:

```css
.uc-stijl-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: var(--uc-line);
}
```

This avoids interfering with Material’s core structure.

---

# Phase 4 — Breakpoint Preservation

Retain existing breakpoints:

```css
@media (max-width: 1024px) {
  .uc-stijl-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 600px) {
  .uc-stijl-grid {
    grid-template-columns: 1fr;
  }
}
```

These apply only to Stijl landing sections — not global layout.

---

# Phase 5 — mkdocs.yml Configuration

Example:

```yaml
theme:
  name: material
  custom_dir: overrides

extra_css:
  - styles/uc-tokens.css
  - styles/stijl-standard.css
  - styles/stijl-components.css
```

No template duplication.
No layout engine modification.

---

# Phase 6 — i18n Compatibility (mkdocs-static-i18n 1.2.3)

Requirements:

- Do not hardcode language URLs.
- Use Material navigation rendering.
- Avoid custom navigation templates.
- Ensure homepage partial uses relative links.

Example homepage partial usage:

```jinja
{% extends "base.html" %}
{% block content %}
  {% include "partials/homepage.html" %}
{% endblock %}
```

All language switching remains handled by the plugin.

---

# Phase 7 — Accessibility Strategy (Future Layer)

Do not bake accessibility tuning into this base.

Instead:

Future overlays:

```
stijl-standard-mkdocs
stijl-aa-mkdocs
stijl-aaa-mkdocs
```

These override only tokens.

---

# Phase 8 — Upgrade Discipline

To avoid tech debt:

- Never override navigation templates.
- Never replace Material JS.
- Minimize HTML overrides.
- Limit changes to CSS and isolated partials.
- Test upgrades quarterly.

---

# What This Conversion Is NOT

It is not:

- A fork of Material
- A custom layout engine
- A replacement navigation system
- A standalone MkDocs theme

It is:

- A disciplined design layer.

---

# Long-Term Stability Model

```
Material = invariant engine
Stijl Standard = identity layer
AA/AAA variants = token overlays
```

This ensures:

- Low maintenance
- Upgrade safety
- Clear separation of concerns
- Predictable growth

---

# Deliverables

After conversion:

- `stijl-standard-mkdocs` override directory
- Token-based design system
- Scoped grid blocks
- Homepage layout pattern
- i18n compatibility
- Clean mkdocs.yml integration

---

# Next Step

If approved, next actions:

1. Extract tokens
2. Build scoped grid
3. Create homepage partial
4. Wire mkdocs.yml
5. Validate i18n switching
6. Test Material upgrade compatibility

---

End of Plan