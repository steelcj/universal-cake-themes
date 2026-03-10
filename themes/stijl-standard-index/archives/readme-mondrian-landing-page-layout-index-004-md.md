# README — Mondrian Landing Page Layout (`index-004.md`)

This document explains the design and implementation of the **Mondrian landing page layout** used in `index-004.md`.

The layout creates a **full-width De Stijl–inspired composition** within the MkDocs Material theme while preserving accessibility, responsive behavior, and logical document structure.

The system combines:

- CSS Grid composition
- responsive layout simplification
- visual rhythm utilities
- semantic HTML ordering

The result is a **minimal yet flexible landing page layout system** suitable for PARA-style site navigation.

---

## Design Goals

The layout was created with the following goals:

- Remove the default MkDocs content margins
- Allow a full-width visual composition
- Maintain semantic HTML order for accessibility
- Simplify layout progressively on smaller screens
- Create visual hierarchy without complex grid calculations
- Remain portable and easy to modify

The design draws inspiration from **De Stijl compositions**, particularly the work of Piet Mondrian.

---

## Layout Structure

The layout consists of three layers:

### MkDocs Page Shell

The MkDocs theme provides:

- header
- navigation
- footer
- search
- site structure

These elements remain unchanged.

---

### Full-Width Grid Canvas

The landing page overrides the default MkDocs content width and creates a grid canvas.

```
┌────────────────────────────────────┐
│ MkDocs Header                      │
├────────────────────────────────────┤
│ Mondrian Grid Layout               │
│                                    │
│  Projects | Areas                  │
│  Projects | Areas                  │
│  Resources | Archives              │
│  Resources | About                 │
│                                    │
├────────────────────────────────────┤
│ MkDocs Footer                      │
└────────────────────────────────────┘
```

---

### Block Components

Each grid item is a **content block**.

Example:

```
<section class="block red projects h-lg">
```

Block classes control:

- grid placement
- color
- height rhythm

---

## Removing Default MkDocs Spacing

Material for MkDocs constrains the content area using several containers.

These are overridden to allow the grid to fill the page.

```
.md-grid {
  max-width: 100% !important;
  margin: 0 !important;
}

.md-main__inner {
  margin: 0 !important;
}

.md-content {
  margin: 0 !important;
}

.md-content__inner {
  padding: 0 !important;
}
```

This creates a **full-width canvas** inside the theme.

---

## Grid Canvas

The grid itself is defined as follows:

```
.grid {
  display: grid;

  gap: var(--line);
  padding: var(--line);

  grid-template-columns: repeat(4, 1fr);

  grid-auto-rows: minmax(180px, 1fr);

  background: var(--black);
}
```

Key properties:

| Property                | Purpose                       |
| ----------------------- | ----------------------------- |
| `grid-template-columns` | defines base column count     |
| `grid-auto-rows`        | establishes vertical rhythm   |
| `gap`                   | creates Mondrian line spacing |

---

## Desktop Composition

Desktop layout uses explicit spans to create the Mondrian composition.

```
.projects {
  grid-column: span 3;
}

.areas {
  grid-column: span 1;
  grid-row: span 2;
}

.resources {
  grid-column: span 2;
  grid-row: span 2;
}

.archives {
  grid-column: span 1;
}

.contact {
  grid-column: span 2;
}
```

This produces a structured asymmetrical layout.

---

## Responsive Behaviour

The layout simplifies progressively.

### Desktop

Four column Mondrian composition.

```
PROJECTS PROJECTS PROJECTS AREAS
PROJECTS PROJECTS PROJECTS AREAS
RESOURCES RESOURCES ARCHIVES
RESOURCES RESOURCES ABOUT
```

---

### Tablet

Grid simplifies to two columns.

```
PROJECTS PROJECTS
AREAS    RESOURCES
ARCHIVES ABOUT
```

Rules:

```
@media (max-width: 1024px) {

  .grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .block {
    grid-column: span 1;
    grid-row: auto;
  }

  .projects {
    grid-column: span 2;
  }

}
```

The layout keeps the **HTML order intact**.

---

### Mobile

Mobile collapses to a single column stack.

```
PROJECTS
AREAS
RESOURCES
ARCHIVES
ABOUT
```

Rules:

```
@media (max-width: 768px) {

  .grid {
    grid-template-columns: 1fr;
  }

  .block {
    grid-column: span 1 !important;
    grid-row: auto !important;
  }

}
```

---

## Height Utility System

Mondrian compositions rely on asymmetry.

Height utilities introduce visual rhythm without complex row calculations.

```
.h-sm  { min-height: 140px; }
.h-md  { min-height: 220px; }
.h-lg  { min-height: 320px; }
.h-xl  { min-height: 420px; }
```

Example usage:

```
<section class="block red projects h-lg">
<section class="block blue areas h-md">
<section class="block yellow resources h-lg">
<section class="block white archives h-sm">
```

These create subtle visual variation across the layout.

---

## Color System

Blocks use simple semantic color classes.

```
.red
.blue
.yellow
.white
```

Example:

```
<section class="block red projects">
```

Colors are defined using CSS variables for easy customization.

---

## Typography

Block headings receive subtle typographic polish.

```
.block h2 {
  font-weight: 600;
  letter-spacing: .02em;
}
```

Paragraphs are constrained for readability.

```
.block p {
  max-width: 28ch;
}
```

---

## Advantages of This System

The layout system provides several benefits:

### Visual Hierarchy

Large spans and height utilities create clear focal points.

---

### Accessibility

HTML order remains logical.

Screen readers and keyboard navigation follow the correct flow.

---

### Maintainability

Layouts are controlled with simple classes rather than complex grid math.

---

### Portability

The system can be reused across landing pages.

---

## Example Use Cases

The layout works particularly well for:

- site home pages
- project indexes
- knowledge hubs
- documentation portals
- research landing pages

---

## Future Enhancements

Possible future improvements include:

- block hover motion
- composition presets
- layout utilities
- reusable MkDocs components
- automated layout generation

---

## File Relationship

```
docs/
 ├─ index.md
 ├─ index-004.md
 └─ README.md
```

`index-004.md` contains the layout implementation.

This document describes how it works.

---

## Summary

The Mondrian landing page layout provides a flexible, responsive system that integrates cleanly with the MkDocs Material theme while enabling expressive full-width compositions.

It combines:

- CSS Grid structure
- responsive simplification
- visual rhythm utilities
- semantic HTML order

The result is a **minimal, maintainable layout framework suitable for modern documentation sites**.