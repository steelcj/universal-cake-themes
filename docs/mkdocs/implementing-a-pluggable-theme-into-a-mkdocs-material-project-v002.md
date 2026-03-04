# Implementing a Pluggable Theme into a MkDocs Material Project

This guide outlines the exact steps required to convert an existing MkDocs Material project to use a pluggable theme architecture.

------

## Phase 1 — Preparation

### 1. Confirm Baseline Environment

Verify:

- MkDocs is working
- Material theme is active
- mkdocs-static-i18n is functioning (if used)
- The site builds cleanly

Run:

```
mkdocs serve
```

Ensure there are no template overrides yet.

------

## Phase 2 — Create the Theme Root

### 2. Create Override Directory (Templates Only)

Inside the project root:

```
mkdir -p overrides/stijl-standard-mkdocs
```

This directory should contain only:

- Template overrides
- Partials
- Macros
- Optional minimal `main.html`

**Do not place assets here.**

------

### 3. Assets Live in `docs/`

Create the asset structure inside `docs/`:

```
mkdir -p docs/assets/css/{tokens,layout,components}
mkdir -p docs/assets/js
mkdir -p docs/assets/images
mkdir -p docs/assets/fonts
```

Assets inside `docs/` are automatically served by MkDocs.

This ensures:

- No override dependency for CSS
- Clear separation between templates and static assets
- Upgrade-safe structure

------

## Phase 3 — Add Base CSS Layers

### Create Token File

#### Design Goals

Tokens should:

- Be theme-agnostic
- Be composable
- Support AA/AAA overlays
- Map cleanly to Material CSS variables when needed
- Be stable long-term

#### Create tokens directory

```
mkdir -p docs/assets/css/tokens
```

#### Create `uc-base.css`

```
nano docs/assets/css/tokens/uc-base.css
```

Content:

```
/* =====================================================
   UniversalCake Base Tokens
   Theme: stijl-standard-mkdocs
   Purpose: Identity layer variables only
   ===================================================== */

:root {

  --uc-color-black: #000000;
  --uc-color-white: #ffffff;

  --uc-color-red:    #d00000;
  --uc-color-blue:   #0033cc;
  --uc-color-yellow: #f2c200;

  --uc-color-bg-primary: var(--uc-color-white);
  --uc-color-bg-accent:  var(--uc-color-yellow);

  --uc-color-text-primary: var(--uc-color-black);
  --uc-color-text-inverse: var(--uc-color-white);

  --uc-color-surface: var(--uc-color-white);
  --uc-color-border:  rgba(0, 0, 0, 0.1);

  --uc-space-xxs: 0.25rem;
  --uc-space-xs:  0.5rem;
  --uc-space-sm:  0.75rem;
  --uc-space-md:  1rem;
  --uc-space-lg:  1.5rem;
  --uc-space-xl:  2rem;
  --uc-space-xxl: 3rem;

  --uc-grid-gap: 10px;

  --uc-radius-sm: 4px;
  --uc-radius-md: 8px;
  --uc-radius-lg: 16px;

  --uc-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.08);
  --uc-shadow-md: 0 4px 8px rgba(0, 0, 0, 0.12);

  --uc-transition-fast: 150ms ease;
  --uc-transition-normal: 250ms ease;

}
```

------

### Create Layout File

#### Create layout directory

```
mkdir -p docs/assets/css/layout
nano docs/assets/css/layout/stijl-standard.css
```

Content remains identical to your previous layout file — only the path changed.

The same applies to the components file.

------

### Create Component File

```
mkdir -p docs/assets/css/components
nano docs/assets/css/components/blocks.css
```

Content remains unchanged.

------

## Phase 4 — Wire Into mkdocs.yml

### Update Theme Configuration

```
theme:
  name: material
  custom_dir: overrides/stijl-standard-mkdocs
```

------

### Register CSS Files

```
extra_css:
  - assets/css/tokens/uc-base.css
  - assets/css/layout/stijl-standard.css
  - assets/css/components/blocks.css
```

Optional JS:

```
extra_javascript:
  - assets/js/interactions.js
```

Note:

Because assets live inside `docs/`, paths begin with `assets/`, not `docs/assets/`.

------

## Phase 5 — Optional Homepage Customization

Create partials only if necessary:

```
nano overrides/stijl-standard-mkdocs/partials/homepage.html
```

Do not move assets back into overrides.

Overrides are for templates only.

------

## Phase 6 — i18n Validation

When testing i18n:

- Close all browser tabs
- Run:

```
mkdocs build --clean
mkdocs serve
```

Multiple open tabs can cause odd behavior with language switching.

------

## Phase 7 — Upgrade Safety Check

Ensure `overrides/` contains only:

- Template overrides
- Partials
- Macros
- Optional minimal `main.html`

and does not contain:

* css
* js
* images

------

## Phase 8 — Test Build

```
mkdocs serve
```

Verify:

- Desktop layout
- Tablet layout
- Mobile layout
- Language switching
- Navigation behavior
- Search functionality

------

## Phase 9 — Commit Structure

Final expected structure:

```
docs/
├── assets/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
└── ...
overrides/
└── stijl-standard-mkdocs/
    ├── partials/
    ├── macros/
    └── main.html (optional)
```

------

## Result

You now have:

- A pluggable theme
- Assets separated from template overrides
- Upgrade-safe structure
- Clear separation of concerns
- No Material fork
- Deterministic asset loading

------

## Final Principle

Material remains the engine.
 Overrides modify behavior.
 Assets define identity.

Separation prevents technical debt.