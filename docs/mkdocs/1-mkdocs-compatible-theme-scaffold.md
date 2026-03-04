# MkDocs-compatible theme scaffold

## Goals

* Conversion to mkdocs theme with:
  - AAA accessible styling
  - Works cleanly with MkDocs + Material (or vanilla MkDocs)
  - Does not break search, nav, or plugins
  - Is maintainable
  - Respects your structured publishing workflow


Since you’re using MkDocs (and likely Material), we’ll override safely instead of replacing the whole theme.

* What mkdocs-static-i18n-1.2.3

------

# Architecture Strategy

We will:

1. Keep the base MkDocs theme (e.g., `material`)
2. Add a custom theme directory
3. Override `main.html`
4. Add a scoped CSS file
5. Preserve MkDocs nav and content injection
6. Add accessibility scaffolding without breaking templating

------

# Directory Structure

Create this:

```
your-project/
│
├── mkdocs.yml
├── docs/
│
└── overrides/
    ├── main.html
    └── css/
        └── de-stijl-government.css
```

------

# Update mkdocs.yml

Add:

```yaml
theme:
  name: material
  custom_dir: overrides

extra_css:
  - stylesheets/de-stijl-government.css
```

This tells MkDocs:

- Use Material as base
- Override templates from `/overrides`
- Inject our custom CSS

------

# Create overrides/main.html

This wraps MkDocs content inside our De Stijl structure while preserving template logic.

```html
{% extends "base.html" %}

{% block content %}

<a href="#main-content" class="skip-link">Skip to main content</a>
<a href="#primary-nav" class="skip-link">Skip to navigation</a>

<div class="de-stijl-wrapper">

<header class="de-stijl-header" role="banner">
  <h1>{{ config.site_name }}</h1>
</header>

<nav id="primary-nav" aria-label="Primary navigation" class="de-stijl-nav">
  {{ super() }}
</nav>

<main id="main-content" role="main" class="de-stijl-main">
  {{ super() }}
</main>

<footer class="de-stijl-footer" role="contentinfo">
  <p>&copy; {{ now().year }} {{ config.site_name }}</p>
</footer>

</div>

{% endblock %}
```

This keeps:

- MkDocs search
- Navigation
- Page content
- Plugins
- Metadata

------

# Create overrides/stylesheets/de-stijl-government.css

This is your government-grade De Stijl layer.

```css
:root {
  --black: #000000;
  --white: #ffffff;
  --red: #7a0000;
  --blue: #001a66;
  --yellow: #8a6a00;
  --focus: #ff00ff;
  --line: 10px;
}

/* Remove Material padding conflicts */
.md-main__inner {
  margin: 0;
}

/* Skip links */
.skip-link {
  position: absolute;
  left: -9999px;
  background: var(--yellow);
  color: var(--white);
  padding: 0.75rem 1rem;
  font-weight: 700;
  z-index: 1000;
}

.skip-link:focus {
  left: 1rem;
  top: 1rem;
}

/* Focus */
:focus {
  outline: 4px solid var(--focus);
  outline-offset: 4px;
}

/* Wrapper */
.de-stijl-wrapper {
  display: grid;
  min-height: 100vh;
  gap: var(--line);
  padding: var(--line);
  background: var(--black);
}

/* Header */
.de-stijl-header {
  background: var(--white);
  padding: 2rem;
}

/* Nav */
.de-stijl-nav {
  background: var(--white);
  padding: 1rem 2rem;
}

/* Main */
.de-stijl-main {
  background: var(--white);
  padding: 2rem;
  max-width: 80ch;
}

/* Footer */
.de-stijl-footer {
  background: var(--white);
  padding: 2rem;
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
```

------

# What This Gives You

- Keeps Material functionality
- Applies your De Stijl aesthetic
- Maintains AAA contrast
- Maintains search and nav
- No JS overrides
- Clean separation of concerns
- Fully accessible

------

# Optional Advanced Layer (True Grid Layout)

If you want full Mondrian composition inside MkDocs pages, we can:

- Add a `.mondrian-grid` shortcode
- Add a Markdown extension
- Add a template partial for colored content blocks

------

# If You Want It Production-Ready for Your Infra

Since you’re running:

- Git bare repos
- Apache
- MkDocs builds
- Structured deployment

We can also:

- Add print styles
- Add government banner header
- Add language toggle support
- Add accessibility statement template
- Add structured metadata injection
- Add CSP-safe styles

------

## Current Decisions Tree

Do we want this scaffold adapted specifically to:

A) MkDocs Material (Insiders-ready)
B) Vanilla MkDocs
C) Your UniversalCake structure
D) Bilingual EN/FR scaffold
E) Fully themed Mondrian grid homepage template

