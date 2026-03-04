---
Title: "Auto-Recomposing Mondrian Layouts with CSS Grid Auto-Fit"
Description: "A technique for responsive De Stijl layouts that automatically recomposes grid structures across screen sizes without relying on media queries."
Author: "Christopher Steel"
Date: "2026-03-03"
Last_Modified_Date: "2026-03-03"
License: "CC BY-SA 4.0"
Tags:
  - "css-grid"
  - "responsive-design"
  - "de-stijl"
  - "web-layout"
  - "grid-auto-fit"
URL: "https://example.com/resources/design/mondrian-auto-recomposition"
Path: "resources/design/mondrian-auto-recomposition.md"
Canonical: "https://example.com/resources/design/mondrian-auto-recomposition"
Sitemap: "true"
Keywords:
  - "css grid auto fit"
  - "responsive mondrian layout"
  - "css grid responsive design"
  - "auto responsive grid"
  - "grid design systems"
DC_Title: "Auto-Recomposing Mondrian Layouts with CSS Grid Auto-Fit"
DC_Creator: "Christopher Steel"
DC_Subject: "Responsive grid design patterns for De Stijl layouts."
DC_Description: "How CSS Grid auto-fit enables Mondrian layouts that adapt automatically across screen sizes."
DC_Language: "en"
DC_License: "https://creativecommons.org/licenses/by-sa/4.0/"
Robots: "index, follow"
OG_Title: "Auto-Recomposing Mondrian Layouts with CSS Grid Auto-Fit"
OG_Description: "Responsive De Stijl layouts without media queries using CSS Grid auto-fit."
OG_URL: "https://example.com/resources/design/mondrian-auto-recomposition"
OG_Image: ""
Schema:
  "@context": "https://schema.org"
  "@type": "TechArticle"
  "headline": "Auto-Recomposing Mondrian Layouts with CSS Grid Auto-Fit"
  "author":
    "@type": "Person"
    "name": "Christopher Steel"
  "about": "Responsive CSS Grid layout design"
Video_Metadata: {}
---

# Auto-Recomposing Mondrian Layouts with CSS Grid Auto-Fit

Traditional responsive design relies heavily on media queries to restructure layouts at specific breakpoints. However, CSS Grid offers a more elegant solution for many design systems.

Using `auto-fit` or `auto-fill`, a grid can automatically recompute its structure based on available space. This allows Mondrian-style layouts to adapt fluidly across screen sizes.

## The Traditional Approach

A typical responsive layout might use several media queries:

```
Desktop → 6 column grid
Tablet → 4 column grid
Mobile → 1 column grid
```

Example:

```css
@media (max-width: 1024px) {
  grid-template-columns: repeat(4, 1fr);
}

@media (max-width: 600px) {
  grid-template-columns: 1fr;
}
```

While effective, this approach requires maintaining explicit breakpoints.

## The Auto-Fit Approach

CSS Grid allows the layout to automatically determine how many columns fit within the available space.

Example:

```css
.uc-stijl-grid {
  display: grid;

  grid-template-columns:
    repeat(auto-fit, minmax(220px, 1fr));

  gap: var(--uc-line, 10px);
}
```

This configuration means:

- each column must be at least **220px wide**
- additional columns are created automatically when space allows
- columns collapse naturally as the viewport shrinks

## How the Layout Recomposes

Large screens:

```
[ Projects ][ Areas ][ Resources ][ About ]
```

Medium screens:

```
[ Projects ][ Areas ]
[ Resources ][ About ]
```

Small screens:

```
[ Projects ]
[ Areas ]
[ Resources ]
[ About ]
```

The browser handles the recomposition automatically.

## Why This Works Well with Mondrian Layouts

De Stijl designs emphasize **modular geometric blocks**. These modular panels map naturally onto CSS Grid columns.

Using `auto-fit` allows these blocks to rearrange themselves fluidly while preserving alignment and spacing.

## Example Implementation

```css
.uc-stijl-grid {
  display: grid;

  grid-template-columns:
    repeat(auto-fit, minmax(240px, 1fr));

  gap: var(--uc-line, 10px);
  padding: var(--uc-line, 10px);

  background: var(--uc-color-black, #000);
}
```

This creates a grid that expands and contracts automatically across different screen sizes.

## Advantages

This approach provides several important benefits:

- removes many breakpoint rules
- simplifies responsive design
- creates fluid layouts across device sizes
- works naturally with modular panel designs

## When to Use This Technique

Auto-recomposition works best for:

- card layouts
- modular navigation panels
- dashboard grids
- gallery systems
- content block layouts

## Summary

CSS Grid's `auto-fit` and `minmax()` capabilities allow Mondrian-style layouts to adapt fluidly across screen sizes without relying on explicit media queries.

This technique simplifies responsive design while maintaining the geometric clarity central to De Stijl aesthetics.

## License

This document, *Auto-Recomposing Mondrian Layouts with CSS Grid Auto-Fit*, by **Christopher Steel**, with AI assistance from **ChatGPT-4 (OpenAI)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

![CC License](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)