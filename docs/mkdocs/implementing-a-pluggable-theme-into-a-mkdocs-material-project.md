# Implementing a Pluggable Theme into a MkDocs Material Project

This guide outlines the exact steps required to convert an existing MkDocs Material project to use a pluggable theme architecture.

---

## Phase 1 — Preparation

### 1. Confirm Baseline Environment

Verify:

- MkDocs is working
- Material theme is active
- mkdocs-static-i18n is functioning
- The site builds cleanly

Run:

```
mkdocs serve
```

Ensure there are no template overrides yet.

---

## Phase 2 — Create the Theme Root

### 2. Create Override Directory

Inside the project root:

```bash
mkdir -p overrides/stijl-standard-mkdocs
```

---

### 3. Create Asset Structure

```
mkdir -p overrides/stijl-standard-mkdocs/assets/css/{tokens,layout,components}
mkdir -p overrides/stijl-standard-mkdocs/assets/js
mkdir -p overrides/stijl-standard-mkdocs/assets/images
mkdir -p overrides/stijl-standard-mkdocs/assets/fonts
mkdir -p overrides/stijl-standard-mkdocs/partials
mkdir -p overrides/stijl-standard-mkdocs/macros
```

---

## Phase 3 — Add Base CSS Layers

### Create Token File

#### Design Goals

Tokens should:

- Be theme-agnostic
- Be composable
- Support AA/AAA overlays
- Map cleanly to Material CSS variables when needed
- Be stable long-term

#### Create tokens directory path

```bash
mkdir -p overrides/stijl-standard-mkdocs/assets/css/tokens
```

Add your base variables (colors, spacing, etc.).

The token layer should define:

- Color system
- Spacing system
- Radius
- Borders
- Elevation
- Motion timing
- Z-index scale
- Layout rhythm

It should NOT:

- Define layout grids
- Target Material classes
- Contain component styles
- Override `.md-*` selectors
- Contain media queries

Tokens = pure variables.

#### Create uc-base.css

Example: uc-base.css (Production-Ready Version)

```bash
nano overrides/stijl-standard-mkdocs/assets/css/tokens/uc-base.css
```

Content

```
/* =====================================================
   UniversalCake Base Tokens
   Theme: stijl-standard-mkdocs
   Purpose: Identity layer variables only
   ===================================================== */

:root {

  /* -------------------------------------------------
     Core Brand Colors
     ------------------------------------------------- */

  --uc-color-black: #000000;
  --uc-color-white: #ffffff;

  --uc-color-red:    #d00000;
  --uc-color-blue:   #0033cc;
  --uc-color-yellow: #f2c200;

  /* -------------------------------------------------
     Semantic Color Aliases
     (Never use raw brand tokens in components)
     ------------------------------------------------- */

  --uc-color-bg-primary: var(--uc-color-white);
  --uc-color-bg-accent:  var(--uc-color-yellow);

  --uc-color-text-primary: var(--uc-color-black);
  --uc-color-text-inverse: var(--uc-color-white);

  --uc-color-surface: var(--uc-color-white);
  --uc-color-border:  rgba(0, 0, 0, 0.1);

  /* -------------------------------------------------
     Spacing Scale
     ------------------------------------------------- */

  --uc-space-xxs: 0.25rem;
  --uc-space-xs:  0.5rem;
  --uc-space-sm:  0.75rem;
  --uc-space-md:  1rem;
  --uc-space-lg:  1.5rem;
  --uc-space-xl:  2rem;
  --uc-space-xxl: 3rem;

  /* -------------------------------------------------
     Layout Rhythm
     ------------------------------------------------- */

  --uc-grid-gap: 10px;

  /* -------------------------------------------------
     Border Radius
     ------------------------------------------------- */

  --uc-radius-sm: 4px;
  --uc-radius-md: 8px;
  --uc-radius-lg: 16px;

  /* -------------------------------------------------
     Elevation
     ------------------------------------------------- */

  --uc-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.08);
  --uc-shadow-md: 0 4px 8px rgba(0, 0, 0, 0.12);

  /* -------------------------------------------------
     Motion
     ------------------------------------------------- */

  --uc-transition-fast: 150ms ease;
  --uc-transition-normal: 250ms ease;

}
```

###  Create Layout File

#### Goals

All layout styles must be **scoped under a container class** (e.g., `.uc-stijl-grid`).

Do **NOT** override:

- `.md-main`
- `.md-content`
- `.md-header`
- `.md-nav`
- `.md-grid`

Material remains the layout engine.  
This file defines a **scoped grid system**, not a replacement layout.

#### Create the layout directory and file:

```bash
mkdir -p overrides/stijl-standard-mkdocs/assets/css/layout
```

```bash
nano overrides/stijl-standard-mkdocs/assets/css/layout/stijl-standard.css
```



#### stijl-standard.css content example

```css
/* =====================================================
   Stijl Standard Layout Layer
   Scoped Layout System
   ===================================================== */

/* -----------------------------------------------------
   Root Layout Container
   Use only when explicitly wrapping content:
   <div class="uc-stijl-grid">...</div>
   ----------------------------------------------------- */

.uc-stijl-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: var(--uc-grid-gap);
  padding: var(--uc-space-xl);
  background: var(--uc-color-black);
  min-height: 60vh;
}


/* -----------------------------------------------------
   Generic Block Container
   ----------------------------------------------------- */

.uc-block {
  padding: var(--uc-space-xl);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: var(--uc-color-surface);
  color: var(--uc-color-text-primary);
}


/* -----------------------------------------------------
   Color Variants
   ----------------------------------------------------- */

.uc-block--red {
  background: var(--uc-color-red);
  color: var(--uc-color-text-inverse);
}

.uc-block--blue {
  background: var(--uc-color-blue);
  color: var(--uc-color-text-inverse);
}

.uc-block--yellow {
  background: var(--uc-color-yellow);
  color: var(--uc-color-text-primary);
}

.uc-block--white {
  background: var(--uc-color-white);
  color: var(--uc-color-text-primary);
}


/* -----------------------------------------------------
   Grid Span Utilities (Desktop Default)
   ----------------------------------------------------- */

.uc-span-1 { grid-column: span 1; }
.uc-span-2 { grid-column: span 2; }
.uc-span-3 { grid-column: span 3; }
.uc-span-4 { grid-column: span 4; }
.uc-span-5 { grid-column: span 5; }
.uc-span-6 { grid-column: span 6; }


/* -----------------------------------------------------
   Tablet Breakpoint
   ----------------------------------------------------- */

@media (max-width: 1024px) {

  .uc-stijl-grid {
    grid-template-columns: repeat(4, 1fr);
  }

  .uc-span-5,
  .uc-span-6 {
    grid-column: span 4;
  }

}


/* -----------------------------------------------------
   Mobile Breakpoint
   ----------------------------------------------------- */

@media (max-width: 600px) {

  .uc-stijl-grid {
    grid-template-columns: 1fr;
  }

  .uc-span-1,
  .uc-span-2,
  .uc-span-3,
  .uc-span-4,
  .uc-span-5,
  .uc-span-6 {
    grid-column: span 1;
  }

}


/* -----------------------------------------------------
   Defensive Safety Notes
   ----------------------------------------------------- */

/*
  - Never style .md-* classes here
  - Never modify global body or html
  - Never alter navigation containers
  - Never rewrite Material structural layout
*/
```

#### Example Usage

Use this layout only inside scoped sections (e.g., homepage partial):

```html
<div class="uc-stijl-grid">

  <section class="uc-block uc-block--red uc-span-4">
    <h2>Projects</h2>
  </section>

  <section class="uc-block uc-block--blue uc-span-2">
    <h2>Areas</h2>
  </section>

</div>
```

This ensures:

- Material documentation pages remain untouched
- The grid system is modular
- Breakpoints are scoped
- The theme remains pluggable
- Upgrades remain safe

###  Create Component File

Create the components directory and file:

```bash
mkdir -p overrides/stijl-standard-mkdocs/assets/css/components
```

```bash
nano overrides/stijl-standard-mkdocs/assets/css/components/blocks.css
```



Component styles must:

- Be **scoped**
- Use **design tokens**
- Avoid targeting `.md-*` classes
- Avoid structural overrides
- Enhance — not replace — Material components

This file defines reusable visual components that can be used inside documentation pages or layout blocks.

#### Content example

```css
/* =====================================================
   Stijl Standard Component Layer
   Reusable UI Components
   ===================================================== */


/* -----------------------------------------------------
   Card Component
   ----------------------------------------------------- */

.uc-card {
  background: var(--uc-color-surface);
  color: var(--uc-color-text-primary);
  padding: var(--uc-space-lg);
  border-radius: var(--uc-radius-md);
  box-shadow: var(--uc-shadow-sm);
  transition: box-shadow var(--uc-transition-normal);
}

.uc-card:hover {
  box-shadow: var(--uc-shadow-md);
}


/* -----------------------------------------------------
   Callout Block
   ----------------------------------------------------- */

.uc-callout {
  padding: var(--uc-space-lg);
  border-left: 6px solid var(--uc-color-blue);
  background: var(--uc-color-bg-primary);
}

.uc-callout--warning {
  border-left-color: var(--uc-color-red);
}

.uc-callout--highlight {
  border-left-color: var(--uc-color-yellow);
}


/* -----------------------------------------------------
   Utility Spacing Classes
   ----------------------------------------------------- */

.uc-mt-lg { margin-top: var(--uc-space-lg); }
.uc-mb-lg { margin-bottom: var(--uc-space-lg); }

.uc-pt-lg { padding-top: var(--uc-space-lg); }
.uc-pb-lg { padding-bottom: var(--uc-space-lg); }


/* -----------------------------------------------------
   Button Style (Non-Destructive)
   ----------------------------------------------------- */

.uc-button {
  display: inline-block;
  padding: var(--uc-space-sm) var(--uc-space-md);
  border-radius: var(--uc-radius-sm);
  background: var(--uc-color-blue);
  color: var(--uc-color-text-inverse);
  text-decoration: none;
  transition: background var(--uc-transition-fast);
}

.uc-button:hover {
  background: var(--uc-color-red);
}


/* -----------------------------------------------------
   Defensive Safety Notes
   ----------------------------------------------------- */

/*
  - Never override .md-button
  - Never modify .md-typeset globally
  - Never alter navigation or layout containers
  - Never redefine Material utility classes
*/
```

---

#### Usage Example

Inside Markdown (via HTML block):

```html
<div class="uc-card">
  <h3>Example Card</h3>
  <p>This is a reusable component.</p>
</div>
```

Callout example:

```html
<div class="uc-callout uc-callout--warning">
  <strong>Important:</strong> Review upgrade notes before deploying.
</div>
```

Button example:

```html
<a class="uc-button" href="/projects/">View Projects</a>
```

---

This ensures:

- Components are reusable
- Layout remains untouched
- Tokens control visual identity
- The theme remains pluggable
- Material upgrades remain safe



## Phase 4 — Wire Into mkdocs.yml

### Update Theme Configuration

Edit `mkdocs.yml`:

```bash
nano mkdocs.yml
```



```yaml
theme:
  name: material
  custom_dir: overrides/stijl-standard-mkdocs
```

---

### Register CSS Files

```yaml
extra_css:
  - assets/css/tokens/uc-base.css
  - assets/css/layout/stijl-standard.css
  - assets/css/components/blocks.css
```

Add JS only if needed:

```yaml
extra_javascript:
  - assets/js/interactions.js
```

---

## Phase 5 — Optional Homepage Customization

### Add a Homepage Partial (Optional)

Create:

```bash
nano overrides/stijl-standard-mkdocs/partials/homepage.html
```

Example usage:

```jinja
{% extends "base.html" %}

{% block content %}
  {% include "partials/homepage.html" %}
{% endblock %}
```

Only do this for landing page customization.

Do NOT modify navigation templates.

---

## Phase 6 — i18n Validation

Notes:

When testing you may end up with multiple browser tabs open to your site. When making changes to i18n this can lead to peculiar behavior when you have multiple tabs open to various "versions" served. When making changes to mkdocs.yml and or documents close any open browser tabs, then do `mkdocs build --clean` (or simply dele the site directory) and then `mkdocs serve` in order to test your current setup without experience peculiar side effects, like site freezing, intermittent functionality of the language switcher.

This will sace you a lot of frustrations!

### Validate mkdocs-static-i18n Compatibility

The goal is to confirm that your pluggable theme:

- Does not interfere with language routing
- Does not break generated URLs
- Does not override language UI
- Does not couple layout to a specific language

---

### Step 1 — Confirm Plugin Is Active

In **mkdocs-static-i18n 1.2.3**, each language entry must include:

- `locale`
- `name`
- `default` (for one language)

Check `mkdocs.yml`:

```bash
nano mkdocs.yml
```

#### Minmal Configuration for v1.2.3

```
plugins:
  - search
  - i18n:
      languages:
        - locale: en
          name: English
          default: true
        - locale: fr
          name: Français
```

Run:

```bash
mkdocs build
```

Create englsih and french indexes:

```bash
mkdir docs/fr
```

```bash
nano docs/fr/index.md
```

Layout:

```
site/
├── index.html
├── fr/
│   └── index.html
```

If you do not see language directories, the plugin is not active.

---

### Step 2 — Validate Language Switcher

Run:

```bash
mkdocs serve
```

Open the site in your browser.

Check:

- The language dropdown is visible
- Switching languages reloads correctly
- URL updates appropriately

Example expected behavior:

```
/         → English
/fr/      → French
```

If switching does nothing, your theme may be interfering with the language partial.


### Validate mkdocs-static-i18n Compatibility

Confirm:

- Language switching works
- URLs are correct
- No hardcoded links
- Navigation renders normally

Do not override:

- `partials/language.html`
- Navigation templates

---

## Phase 7 — Upgrade Safety Check

### Confirm You Did NOT Override Core Templates

Ensure you have not added:

- `partials/header.html`
- `partials/nav.html`
- `partials/search.html`
- `partials/sidebar.html`

Unless absolutely necessary.

---

## Phase 8 — Test Build

### Test Locally

```bash
mkdocs serve
```

Verify:

- Desktop layout
- Tablet layout
- Mobile layout
- Language switching
- Search
- Navigation behavior

---

## Phase 9 — Commit Structure

### Commit Only What You Own

You should now have:

```
overrides/stijl-standard-mkdocs/
```

Containing only:

- CSS
- Optional JS
- Optional homepage partial
- Optional minimal `main.html`

No Material core templates copied.

---

## Result

You now have:

- A pluggable theme
- Namespaced assets
- Upgrade-safe overrides
- i18n compatibility
- Clear separation of concerns
- No Material fork

Switching themes in the future becomes:

```yaml
custom_dir: overrides/another-theme
```

Not a structural rewrite.

---

## Final Principle

Material remains the engine.  
Your theme is a replaceable identity layer.

Discipline now prevents technical debt later.