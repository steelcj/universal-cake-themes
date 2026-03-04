---
Title: "Stabilizing Mondrian Layouts on the Web with Proportional Grid Rows"
Description: "Explains how proportional CSS Grid rows solve the classic instability problem in De Stijl (Mondrian) web layouts when content grows."
Author: "Christopher Steel"
Date: "2026-03-03"
Last_Modified_Date: "2026-03-03"
License: "CC BY-SA 4.0"
Tags:
  - "css-grid"
  - "de-stijl"
  - "mondrian-layout"
  - "web-design"
  - "responsive-design"
URL: "https://example.com/resources/design/mondrian-proportional-rows"
Path: "resources/design/mondrian-proportional-rows.md"
Canonical: "https://example.com/resources/design/mondrian-proportional-rows"
Sitemap: "true"
Keywords:
  - "css grid proportions"
  - "mondrian web layout"
  - "de stijl grid design"
  - "css grid template rows"
  - "stable grid composition"
DC_Title: "Stabilizing Mondrian Layouts on the Web with Proportional Grid Rows"
DC_Creator: "Christopher Steel"
DC_Subject: "CSS grid techniques for stable De Stijl web layouts."
DC_Description: "How proportional CSS Grid rows preserve visual composition in Mondrian-inspired layouts."
DC_Language: "en"
DC_License: "https://creativecommons.org/licenses/by-sa/4.0/"
Robots: "index, follow"
OG_Title: "Stabilizing Mondrian Layouts on the Web with Proportional Grid Rows"
OG_Description: "A CSS Grid technique for maintaining balanced De Stijl layouts even when content grows."
OG_URL: "https://example.com/resources/design/mondrian-proportional-rows"
OG_Image: ""
Schema:
  "@context": "https://schema.org"
  "@type": "TechArticle"
  "headline": "Stabilizing Mondrian Layouts on the Web with Proportional Grid Rows"
  "author":
    "@type": "Person"
    "name": "Christopher Steel"
  "about": "CSS Grid layout design"
Video_Metadata: {}
---

# Stabilizing Mondrian Layouts on the Web with Proportional Grid Rows

De Stijl and Mondrian-inspired layouts are visually powerful because they rely on carefully balanced geometric proportions. However, when implemented on the web, these layouts often break as content grows.

This document explains a simple technique using **proportional CSS Grid rows** that keeps the composition stable while still supporting real-world content.

## The Classic Weakness of Mondrian Web Layouts

Traditional Mondrian compositions rely on **fixed proportions** between panels.

In contrast, web layouts are usually **content-driven**. When text or media inside one panel grows, the entire composition can become distorted.

Example of a typical Mondrian layout structure:

```
Projects  Projects  Projects  Projects  Areas  Areas
Resources Resources Resources About     About  About
```

If the **Projects** block contains significantly more content than the others, it may expand vertically:

```
Projects  Projects  Projects  Projects  Areas  Areas
Projects  Projects  Projects  Projects  Areas  Areas
Resources Resources Resources About     About  About
```

The grid structure remains technically correct, but the visual composition becomes unbalanced.

## The Solution: Proportional Grid Rows

CSS Grid allows rows to be defined using fractional units (`fr`). This allows layouts to maintain stable proportions regardless of content size.

Example:

```css
.uc-stijl-grid {
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: 2fr 1fr;
}
```

This configuration creates:

```
Row 1 = 2 parts height
Row 2 = 1 part height
```

The overall composition remains balanced even if individual panels contain more content.

## Example Layout

```
┌───────────────────────┬───────────────┐
│                       │               │
│       Projects        │     Areas     │
│                       │               │
├───────────────────────┼───────────────┤
│      Resources        │     About     │
└───────────────────────┴───────────────┘
```

The proportions of the rows remain stable regardless of content.

## Handling Overflow

If content becomes too large for a panel, it should scroll internally rather than expanding the entire grid.

Example:

```css
.uc-block {
  overflow: auto;
}
```

This allows panels to contain longer text or additional elements while preserving the grid's visual balance.

## Example Implementation

```css
.uc-stijl-grid {
  flex: 1;
  display: grid;

  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: 2fr 1fr;

  gap: var(--uc-line, 10px);
  padding: var(--uc-line, 10px);

  background: var(--uc-color-black, #000);
}
```

This configuration keeps the layout visually stable while allowing content to grow naturally inside each panel.

## Advantages

Using proportional rows provides several benefits:

- preserves the visual geometry of De Stijl compositions
- prevents large panels from distorting the layout
- allows flexible content inside panels
- works cleanly with CSS Grid and modern responsive design

## Summary

Mondrian layouts often break on the web because they rely purely on content-driven sizing. By introducing **proportional grid rows**, designers can maintain balanced compositions even as content grows.

This approach allows De Stijl layouts to function reliably in modern content-driven environments.

## License

This document, *Stabilizing Mondrian Layouts on the Web with Proportional Grid Rows*, by **Christopher Steel**, with AI assistance from **ChatGPT-4 (OpenAI)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

![CC License](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)
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