---
Title: "De Stijl Layout Modes for Material for MkDocs"
Description: "Explains the difference between viewport layouts and content layouts when integrating a De Stijl grid with Material for MkDocs, and how to support both modes cleanly."
Author: "Christopher Steel"
Date: "2026-03-03"
Last_Modified_Date: "2026-03-03"
License: "CC BY-SA 4.0"
Tags:
  - "mkdocs"
  - "material-for-mkdocs"
  - "css-layout"
  - "de-stijl"
  - "responsive-design"
URL: "https://example.com/resources/design/de-stijl-layout-modes"
Path: "resources/design/de-stijl-layout-modes.md"
Canonical: "https://example.com/resources/design/de-stijl-layout-modes"
Sitemap: "true"
Keywords:
  - "mkdocs layout"
  - "material for mkdocs grid"
  - "de stijl web layout"
  - "viewport layout vs content layout"
  - "css grid mkdocs"
DC_Title: "De Stijl Layout Modes for Material for MkDocs"
DC_Creator: "Christopher Steel"
DC_Subject: "Web layout design patterns for integrating De Stijl grids with Material for MkDocs."
DC_Description: "A guide describing how De Stijl grid layouts behave in Material for MkDocs and how to support both viewport and document content modes."
DC_Language: "en"
DC_License: "https://creativecommons.org/licenses/by-sa/4.0/"
Robots: "index, follow"
OG_Title: "De Stijl Layout Modes for Material for MkDocs"
OG_Description: "Understanding viewport vs content layouts when integrating Mondrian-style grids with MkDocs."
OG_URL: "https://example.com/resources/design/de-stijl-layout-modes"
OG_Image: ""
Schema:
  "@context": "https://schema.org"
  "@type": "TechArticle"
  "headline": "De Stijl Layout Modes for Material for MkDocs"
  "author":
    "@type": "Person"
    "name": "Christopher Steel"
  "about": "CSS layout patterns and MkDocs theme integration"
Video_Metadata: {}
---

# De Stijl Layout Modes for Material for MkDocs

When integrating a De Stijl–inspired grid layout into **Material for MkDocs**, it is important to understand that two valid layout modes exist. The behavior you observed—where the footer is no longer visually attached to the grid—is the result of switching between these two modes.

Understanding the distinction helps determine when each approach is appropriate.

## Content Layout Mode

In the default MkDocs model, page content behaves like a traditional document. The grid becomes simply part of the page content flow.

The layout structure behaves like this:

```
header
content (your grid)
footer
```

In this mode:

- The grid grows only as large as its content.
- The footer follows directly after the content.
- The page behaves like a normal documentation page.

This is typically the correct behavior for documentation systems such as MkDocs.

### Example CSS

```css
.uc-stijl-grid {
  display: grid;
}
```

Here, the grid is treated like any other block element inside the page.

## Viewport Layout Mode

A De Stijl grid is often used as a **landing page layout** or visual navigation interface. In those cases, the design is intended to fill the available space between the header and footer.

The layout behaves like this:

```
header
viewport-filling grid
footer
```

The grid expands to fill the vertical space available in the page.

### Example CSS

```css
.uc-stijl-grid {
  flex: 1;
  display: grid;
}
```

When the grid participates in the flex layout of the page container, it stretches to occupy the remaining vertical space.

## Choosing the Correct Mode

The appropriate mode depends on the purpose of the page.

### Landing Pages

A viewport layout is typically used for:

- Homepages
- Navigation dashboards
- Visual index pages
- Design-driven landing pages

In these cases the grid should visually connect the header and footer.

### Documentation Pages

A content layout is preferred for:

- Guides
- Articles
- Reference documentation
- Long-form pages

Here the grid should behave like normal page content so the document flow remains predictable.

## Supporting Both Modes

Many sites benefit from supporting both behaviors. A simple way to do this is to use a layout modifier class.

### Layout Modifier Classes

```
.uc-layout--viewport
.uc-layout--content
```

These classes allow pages to explicitly choose their layout behavior.

### CSS Example

```css
.uc-layout--viewport .uc-stijl-grid {
  flex: 1;
}

.uc-layout--content .uc-stijl-grid {
  display: grid;
}
```

This approach allows the same grid component to behave differently depending on the context.

## Example Usage in Markdown

A landing page can enable viewport behavior by wrapping the grid in a modifier container.

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

Documentation pages can simply omit the modifier wrapper.

## Resulting Behavior

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

This pattern allows the site to support both **design-driven layouts** and **document-driven layouts** without complicating the CSS architecture.

## Design System Implications

A well-structured De Stijl integration for MkDocs typically includes:

- a **layout canvas** (`uc-stijl-grid`)
- reusable **block components**
- **span utilities** for grid positioning
- responsive breakpoints
- clean integration with the Material theme

This separation between layout, components, and page content results in a flexible design system rather than a single-purpose page template.

## License

This document, *De Stijl Layout Modes for Material for MkDocs*, by **Christopher Steel**, with AI assistance from **ChatGPT-4 (OpenAI)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

![CC License](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)