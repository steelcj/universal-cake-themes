# stijl-standard-index Theme Conversion Outline Example for Mkdocs

Right now the index page is acting like a **mini standalone website**. We want to convert it into:

- reusable **CSS**
- a reusable **layout template**
- a clean **index.md** that only contains content

This aligns with how **Material for MkDocs expects customization to work**.

------

# Target Architecture

You want something like this:

```
docs/
  index.md
  assets/
    stylesheets/
      stijl.css
overrides/
  main.html
  partials/
    mondrian-home.html
mkdocs.yml
```

------

# Step 1 — Move CSS out of `index.md`

Create:

```
docs/assets/stylesheets/stijl.css
```

Move **everything inside `<style>`** into that file.

Remove:

```
<style>
...
</style>
```

from `index.md`.

------

# Step 2 — Load CSS in `mkdocs.yml`

Add:

```yaml
extra_css:
  - assets/stylesheets/stijl.css
```

MkDocs will now load the Mondrian system **globally**.

------

# Step 3 — Remove HTML shell from `index.md`

Delete these lines from the page:

```
<!DOCTYPE html>
<html>
<head>
<meta>
<title>
</head>
<body>
</body>
</html>
```

MkDocs already provides the HTML document structure.

Your `index.md` should eventually look like this:

```markdown
---
hide:
  - toc
  - navigation
  - title
---

<main class="grid">

<section class="block red projects h-lg">

## Projects

Current projects we are working on.

[Join Us](#)

</section>

<section class="block blue areas h-md">

## Areas

Areas of ongoing responsibility and attention.

[Explore](#)

</section>

<section class="block yellow resources h-lg">

## Resources

Reference materials, research, and useful information.

[Learn More](#)

</section>

<section class="block white archives h-sm">

## Archives

Completed or inactive work kept for reference.

[Our Philosophy](#)

</section>

<section class="block red contact h-md">

## About Us

Information about who we are and what we do.

[Get in Touch](#)

</section>

</main>
```

This keeps Markdown semantics while still allowing layout control.

------

# Step 4 — Add theme override (optional but recommended)

Create:

```
overrides/main.html
```

Minimal override:

```html
{% extends "base.html" %}

{% block extrahead %}
  {{ super() }}
{% endblock %}
```

Then in `mkdocs.yml`:

```yaml
theme:
  name: material
  custom_dir: overrides
```

This lets you extend the theme later if needed.

------

# Step 5 — Clean up MkDocs wrappers (already done)

Your CSS already includes the correct overrides:

```css
.md-grid { max-width: 100% !important; }
.md-main__inner { margin: 0 !important; }
.md-content__inner { padding: 0 !important; }
```

So the Mondrian grid will **span the full page width**.

------

# Result

You now get:

- **clean Markdown content**
- **reusable Mondrian layout system**
- **CSS maintained in one place**
- **proper MkDocs integration**

------

# Future nice improvement

Once this is integrated, the **next level refinement** is making the Mondrian layout a **homepage component** instead of raw HTML sections.

That would look like:

```
{% include "partials/mondrian-home.html" %}
```

which makes the homepage extremely maintainable.

------

If you'd like, I can show you the **cleanest MkDocs architecture for this layout (used by documentation teams)** that keeps themes, layouts, and content completely separated.