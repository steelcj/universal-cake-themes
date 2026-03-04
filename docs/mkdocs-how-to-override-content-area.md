# mkdocs - How to Override Content Area

## First: Understand What “Entire Content Area” Means

In Material, the content region is:

```html
<div class="md-content">
  <article class="md-content__inner md-typeset">
    <!-- Your markdown renders here -->
  </article>
</div>
```

Everything inside `.md-content` is controlled by the `content` block in `main.html`.

So if you want to override the entire content area, you must override that block.

------

# OPTION 1 — Full Page Content Override (Recommended Approach)

Create:

```bash
nano overrides/stijl-standard-mkdocs/main.html
```

Minimal override:

```jinja
{% extends "base.html" %}

{% block content %}
  <div class="uc-stijl-grid">

    <section class="uc-block uc-block--red uc-span-4">
      <h2>Projects</h2>
    </section>

    <section class="uc-block uc-block--blue uc-span-2">
      <h2>Areas</h2>
    </section>

  </div>
{% endblock %}
```

This completely replaces the markdown rendering.

Now Material still provides:

- Header
- Tabs
- Language switcher
- Search
- Footer

But your content area is fully controlled.

## Material Template Structure (Simplified)

Material roughly does:

```
base.html
  └── main.html
        └── blocks:
              - header
              - tabs
              - content
              - footer
```

So:

- `material/main.html` already extends `base.html`
- `base.html` does NOT include the page title logic
- The page title (`<h1>Homes</h1>`) is rendered inside `main.html`

## Remove Sidebar + Keep Header + Keep Footer

### Remove tabs if you like

```bash
nano mkdocs.yml
```

comment out tabs and features is your only feature

```yaml
site_name: My Docs
theme:
  name: material
#  features:
#    - navigation.tabs
```

Create:

```
nano overrides/stijl-standard-mkdocs/main.html
```

With this:

```
{% extends "base.html" %}

{% block container %}
  <main class="md-main">
    <div class="uc-stijl-grid">

      <section class="uc-block uc-block--red uc-span-4">
        <h2>Projects</h2>
      </section>

      <section class="uc-block uc-block--blue uc-span-2">
        <h2>Areas</h2>
      </section>

    </div>
  </main>
{% endblock %}
```

## Expand Layout Blocks (stijl-standard.css)

```bash
nano docs/assets/css/layout/stijl-standard.css
```

### Add Size Variants

```css
/* -----------------------------------------------------
   Height Variants
   ----------------------------------------------------- */

.uc-block--sm {
  min-height: 150px;
}

.uc-block--md {
  min-height: 250px;
}

.uc-block--lg {
  min-height: 400px;
}

.uc-block--xl {
  min-height: 600px;
}
```

### Alignment Utilities

```css
/* -----------------------------------------------------
   Alignment Utilities
   ----------------------------------------------------- */

.uc-center {
  align-items: center;
  justify-content: center;
  text-align: center;
}

.uc-align-start {
  align-items: flex-start;
  justify-content: flex-start;
}

.uc-align-end {
  align-items: flex-end;
  justify-content: flex-end;
}
```

### Border System (Mondrian Style Lines)

```css
/* -----------------------------------------------------
   Mondrian Grid Lines
   ----------------------------------------------------- */

.uc-block {
  border: var(--uc-grid-gap) solid var(--uc-color-black);
}
```

If that’s too aggressive, use:

```css
.uc-block {
  border: 4px solid var(--uc-color-black);
}
```

### Full-Width Section Variant

Useful for hero sections:

```css
/* -----------------------------------------------------
   Full Width Variant
   ----------------------------------------------------- */

.uc-full-width {
  grid-column: 1 / -1;
}
```

## Expanded Example Layout (Pure Override Mode)

## main.html

```bash
overrides/stijl-standard-mkdocs/main.html
```

Your `main.html` should look like this:

```
{% extends "base.html" %}

{% block container %}
  <main class="md-main">
    <div class="uc-stijl-grid">

      <!-- Your blocks here -->

    </div>
  </main>
{% endblock %}
```

That is the stable pattern.



If you are overriding `content` instead of `container`, we adjust.

If you are overriding `main`, we adjust.

But container is the clean full-replacement layer.

Now your `main.html` can look like this:

```jinja2
{% extends "base.html" %}

{% block container %}
<main class="md-main">

  <div class="uc-stijl-grid">

    <section class="uc-block uc-block--red uc-span-4 uc-block--lg uc-center">
      <h2>Projects</h2>
    </section>

    <section class="uc-block uc-block--blue uc-span-2 uc-block--md">
      <h2>Areas</h2>
    </section>

    <section class="uc-block uc-block--yellow uc-span-3 uc-block--md">
      <h2>Resources</h2>
    </section>

    <section class="uc-block uc-block--white uc-span-3 uc-block--md">
      <h2>About</h2>
    </section>

    <section class="uc-block uc-block--black uc-full-width uc-block--sm uc-center">
      <p>UniversalCake — Structured Simplicity</p>
    </section>

  </div>

</main>
{% endblock %}
```

#### Quick Sanity Check

If you run:

```bash
mkdocs build --clean
```

### Important Structural Clarification

Material’s layout structure (simplified):

```bash
base.html
  ├── header
  ├── tabs
  ├── container (Here for everything but headers, tabs and footer)
  └── footer
```

So:

- If you override `container` → sidebars disappear
- If you override `content` → sidebars remain
- If you override `main.html` and extend `main.html` → recursion risk
- If you extend `base.html` → no recursion risk

You are currently in the safest structural position.

------

You have successfully:

• Removed sidebar container
 • Removed TOC
 • Removed markdown rendering
 • Removed nav title injection
 • Stabilized template inheritance

You are now in:

> Full Application Layout Mode



### Architectural Reality

Once you override `container`, you are no longer using Material as a documentation engine.

You are using:

Material = header + UI chrome
 You = page application layer

This is stable and clean.

No recursion.
 No partial conflicts.
 No loader tricks.
 No i18n breakage.





















# OPTION 2 — Conditional Override (Cleaner Architecture)

Override only homepage.

Create:

```
overrides/stijl-standard-mkdocs/main.html
```

Use conditional logic:

```jinja
{% extends "!main.html" %}

{% block content %}
  {% if page.file and page.file.src_path == "index.md" %}

    <div class="uc-stijl-grid">
      <section class="uc-block uc-block--red uc-span-4">
        <h2>Projects</h2>
      </section>

      <section class="uc-block uc-block--blue uc-span-2">
        <h2>Areas</h2>
      </section>
    </div>

  {% else %}
    {{ super() }}
  {% endif %}
{% endblock %}
```

Now:

- Homepage = fully custom
- Other pages = normal Material markdown

This is usually the correct pattern.

------

# OPTION 3 — Remove Markdown Rendering Entirely

If you want no `.md-typeset`, no auto H1, no injected title:

Override the inner structure:

```jinja
{% extends "main.html" %}

{% block content %}
  <div class="md-content">
    <div class="md-content__inner">
      <div class="uc-stijl-grid">
        ...
      </div>
    </div>
  </div>
{% endblock %}
```

But this is more invasive.

------

# Important Reality

Right now you are trying to:

- Use Material as shell
- But ignore its content rendering behavior

That is totally valid.

You just need to override the `content` block instead of fighting `hide:` and navigation.

------

# What You Cannot Do

You cannot:

- Remove the title while keeping nav + tabs + i18n perfectly intact
- Without either CSS hacks
- Or template override

Material assumes documentation structure.

------

# My Recommendation

Given everything you’ve built:

Use:

- Material header
- Material language selector
- Material search
- Custom content block override

That gives you:

Stable shell
Full layout control
No hacks
No CSS fighting

------

If you want, I can give you a clean, minimal `main.html` override that:

- Removes the `<h1>`
- Removes TOC
- Keeps header + language
- Gives you full grid control

Do you want:

A) Homepage-only override
B) Entire-site override
C) Hybrid doc + marketing structure

Pick one and I’ll give you the clean implementation.