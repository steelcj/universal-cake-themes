---
Title: "Implementing Multiple Layout Modes for the Stijl Content Grid in MkDocs"
Description: "Step-by-step guide explaining how to extend a De Stijl CSS Grid layout used in Material for MkDocs so that pages can support both content mode and viewport mode."
Author: "Christopher Steel"
Date: "2026-03-03"
Last_Modified_Date: "2026-03-03"
License: "CC BY-SA 4.0"
Tags:
  - "mkdocs"
  - "material-for-mkdocs"
  - "css-grid"
  - "de-stijl"
  - "layout-systems"
URL: "https://example.com/resources/design/mkdocs-stijl-layout-modes-guide"
Path: "resources/design/mkdocs-stijl-layout-modes-guide.md"
Canonical: "https://example.com/resources/design/mkdocs-stijl-layout-modes-guide"
Sitemap: "true"
Keywords:
  - "mkdocs layout modes"
  - "material for mkdocs css grid"
  - "mondrian layout mkdocs"
  - "viewport layout css grid"
  - "mkdocs theme customization"
DC_Title: "Implementing Multiple Layout Modes for the Stijl Content Grid in MkDocs"
DC_Creator: "Christopher Steel"
DC_Subject: "Extending a De Stijl CSS Grid layout to support both content and viewport modes in MkDocs."
DC_Description: "Walkthrough explaining how to modify an MkDocs De Stijl layout so that pages can opt into either content-driven or viewport-driven grid behavior."
DC_Language: "en"
DC_License: "https://creativecommons.org/licenses/by-sa/4.0/"
Robots: "index, follow"
OG_Title: "Implementing Multiple Layout Modes for the Stijl Content Grid in MkDocs"
OG_Description: "How to add content and viewport layout modes to a Mondrian-style MkDocs grid layout."
OG_URL: "https://example.com/resources/design/mkdocs-stijl-layout-modes-guide"
OG_Image: ""
Schema:
  "@context": "https://schema.org"
  "@type": "TechArticle"
  "headline": "Implementing Multiple Layout Modes for the Stijl Content Grid in MkDocs"
  "author":
    "@type": "Person"
    "name": "Christopher Steel"
  "about": "MkDocs theme customization"
Video_Metadata: {}
---

# Implementing Multiple Layout Modes for the Stijl Content Grid in MkDocs

This document provides a walkthrough explaining how to extend the **Stijl Standard grid layout** used with **Material for MkDocs** so that pages can support both:

- **Content layout mode**
- **Viewport layout mode**

The goal is to allow the same grid system to behave differently depending on the type of page.

This keeps documentation pages readable while allowing visually expressive landing pages.

## Overview of Layout Modes

Two layout behaviors are useful for MkDocs sites.

### Content Layout Mode

In the default MkDocs model, page content behaves like a traditional document.

```
header
content (grid)
footer
```

In this mode:

- the grid grows based on its content
- the footer follows immediately after the content
- the page behaves like standard documentation

This is the correct behavior for most pages.

### Viewport Layout Mode

Some pages benefit from a full-height visual layout.

```
header
viewport-filling grid
footer
```

In this mode:

- the grid expands vertically
- the grid visually connects the header and footer
- the page behaves more like a landing page

This is useful for:

- homepages
- navigation dashboards
- section index pages

## Strategy

Instead of creating separate grid systems, we modify the existing grid so that **layout behavior can be selected using a wrapper class**.

The grid itself remains unchanged.

Only its **layout behavior** changes.

## Step 1 — Keep the Existing Grid Definition

Your existing grid definition should remain intact.

Example:

```css
/* =====================================================
   Stijl Standard Layout Layer
   ===================================================== */

/* 1) Base canvas */
.uc-stijl-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: var(--uc-line, 10px);
  padding: var(--uc-line, 10px);
  background: var(--uc-color-black, #000);
  grid-auto-rows: minmax(150px, 1fr);
}
```

This defines the **Mondrian canvas**.

Do not modify this rule.

## Step 2 — Add Layout Modifier Classes

Just below add two new layout modifier classes.

```
/* 2) Layout modes (must come after base canvas) */
.uc-layout--viewport .uc-stijl-grid {
  flex: 1;
}

/* Optional, not required */
.uc-layout--content .uc-stijl-grid {
  display: grid;
}
```

These classes will control how the grid behaves within the page layout.

## Step 3 — Define CSS for Layout Modes

Add the following CSS rules.

```css
/* Default grid behavior */
.uc-stijl-grid {
  display: grid;
}

/* Viewport layout mode */
.uc-layout--viewport .uc-stijl-grid {
  flex: 1;
}
```

The important detail is that the grid only becomes **flex-aware** when the viewport layout is activated.

This allows the grid to stretch vertically.

## Step 4 — Ensure the Flex Chain Exists

For viewport mode to work, the MkDocs content container must support flex growth.

Your CSS should already contain something similar to the following:

```css
.md-main {
  flex: 1;
  display: flex;
}

.md-main__inner {
  flex: 1;
  display: flex;
}

.md-content__inner {
  flex: 1;
  display: flex;
  flex-direction: column;
}
```

Mine

```css
/* Page column layout */
.md-container {
  min-height: 100%;
  display: flex;
  flex-direction: column;
}

/* Main region stretches between header and footer */
.md-main {
  flex: 1;
  padding: 0;
  display: flex;
}

/* Remove centering constraints */
.md-main__inner {
  flex: 1;
  width: 100%;
  margin: 0;
  padding: 0;
  display: flex;
}

/* Remove default content padding */
/* Content container participates in flex layout */
.md-content {
  flex: 1;
  margin: 0;
}

/* Inner wrapper becomes vertical flex stack */
.md-content__inner {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 0;
}

```

What you have is **almost perfect**, but there is one small adjustment that will make the layout modes behave more predictably.

Right now you are making **every page flex-aware all the way down to the grid**, which is fine, but the important thing to understand is:

> The flex chain should exist, but the grid should only stretch when viewport mode is enabled.

Your current code is very close to the ideal structure for Material for MkDocs. I would only suggest **one small cleanup** and one clarification.

body
└─ md-container
   ├─ header
   ├─ md-main
   │  └─ md-main__inner
   │     └─ md-content
   │        └─ md-content__inner
   │           └─ page content
   └─ footer

Because `md-content__inner` is `display:flex`, your grid can now stretch vertically when needed.

That part is **correct**.

#### One small improvement

You don't actually need `width: 100%` on `.md-main__inner`.

Material already manages width.

So this is slightly cleaner:

```
.md-main__inner {
  flex: 1;
  margin: 0;
  padding: 0;
  display: flex;
}
```

Removing that avoids some subtle layout interactions.

This allows the grid to expand within the available page space.

## Step 5 — Using Layout Modes in Markdown

### Content Mode (Default)

#### index.html

```bash
nano docs/index.md
```



Most pages will simply include the grid directly.

```html
<div class="uc-stijl-grid">

<section class="uc-block uc-block--red uc-span-4">
Projects
</section>

<section class="uc-block uc-block--blue uc-span-2">
Areas
</section>

<section class="uc-block uc-block--yellow uc-span-3">
Resources
</section>

<section class="uc-block uc-block--white uc-span-3">
About
</section>

</div>
```

This produces:

```
header
content grid
footer
```

#### More complex example for mkdocs

```markdown
---
hide:
  - toc
  - navigation
  - title
---
<div class="uc-stijl-grid">

<section class="uc-block uc-block--white uc-span-6">
<h1>Studio De Stijl</h1>
<nav>
Home · Projects · Areas · Resources · About
</nav>
</section>

<section class="uc-block uc-block--red uc-span-4">
Projects
</section>

<section class="uc-block uc-block--blue uc-span-2">
Areas
</section>

<section class="uc-block uc-block--yellow uc-span-3">
Resources
</section>

<section class="uc-block uc-block--white uc-span-3">
About
</section>

<section class="uc-block uc-block--white uc-span-6">
© 2026 Studio De Stijl

```

### Viewport Mode (Landing Page)

For landing pages, wrap the grid in the layout modifier container.

```html
<div class="uc-layout--viewport">

<div class="uc-stijl-grid">

<section class="uc-block uc-block--red uc-span-4">
Projects
</section>

<section class="uc-block uc-block--blue uc-span-2">
Areas
</section>

<section class="uc-block uc-block--yellow uc-span-3">
Resources
</section>

<section class="uc-block uc-block--white uc-span-3">
About
</section>

</div>
</div>
```

This produces:

```
header
viewport grid
footer
```

## Step 6 — Optional Explicit Content Mode

If desired, an explicit content mode can also be defined.

```css
.uc-layout--content .uc-stijl-grid {
  display: grid;
}
```

However, this is not strictly necessary because the grid already behaves as content by default.

## Result

With this approach the site now supports both page styles.

Landing pages:

```
header
viewport grid
footer
```

Documentation pages:

```
header
content
footer
```

Both layouts use the **same grid system**.

## Advantages

This pattern provides several advantages:

- preserves the MkDocs documentation workflow
- allows expressive visual landing pages
- avoids modifying core Material templates
- keeps the layout system simple and reusable
- supports design experimentation without breaking documentation pages

## Summary

The Stijl grid system can support both documentation layouts and visual landing layouts by introducing a small set of layout modifier classes.

By keeping the grid definition independent from page layout behavior, the system remains flexible, maintainable, and compatible with future MkDocs updates.

## License

This document, *Implementing Multiple Layout Modes for the Stijl Content Grid in MkDocs*, by **Christopher Steel**, with AI assistance from **ChatGPT-4 (OpenAI)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

![CC License](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)