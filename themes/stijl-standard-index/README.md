# stijl-standard-index README.md

**stijl-standard-index** is a minimalist layout theme inspired by **De Stijl design principles**.  
It emphasizes geometric balance, strong structural lines, and careful use of color to create a clean, accessible, and highly adaptable layout system.

The theme is designed to work both as:

- a **stand-alone HTML layout**
- a **drop-in visual layer for static site generators**
- a **foundation for accessible editorial layouts**

The design philosophy prioritizes:

- clarity
- strong visual structure
- minimal CSS complexity
- accessibility
- adaptability to modern static publishing workflows

---

# Design Inspiration

The theme draws inspiration from the **De Stijl movement**, particularly the works of:

- Piet Mondrian
- Theo van Doesburg
- Gerrit Rietveld

Key design characteristics include:

- orthogonal grid structures
- black structural lines
- white dominant surfaces
- restrained use of primary colors
- strong visual balance

Unlike decorative themes, **stijl-standard-index** treats layout as an architectural structure rather than a stylistic overlay.

---

# Current Features

## Mondrian-Inspired Grid Layout

The theme implements a **structured grid composition** with clear visual divisions. Blocks can be arranged to form editorial layouts or landing pages.

Key characteristics:

- modular block units
- strong grid boundaries
- flexible block sizes
- responsive behavior

Typical block scale variables:

```
--block-sm
--block-md
--block-lg
--block-xl
```

These allow a consistent visual rhythm across layouts.

---

## Structural Line System

The grid uses strong structural separators to emphasize layout geometry.

```
--line
```

The line variable controls the thickness of grid separators.

Changing this variable allows the entire theme to visually shift between:

- minimalist editorial
- bold graphic layout
- museum-style compositions

---

## Responsive Scaling

The theme uses `clamp()` and viewport-aware sizing to scale layout blocks smoothly.

Example variable:

```
--block-unit: clamp(40px, 7vh, 70px);
```

This ensures:

- good visual proportions
- balanced layouts across screen sizes
- predictable scaling behavior

---

## Minimal Dependency Architecture

The theme intentionally avoids reliance on heavy frameworks.

It works with:

- plain HTML
- static site generators
- documentation systems
- lightweight CMS platforms

This keeps the theme:

- portable
- maintainable
- long-lived

---

# Customizing the Theme

The theme is designed to be customized primarily through **CSS variables**.

## Layout Scale

Adjust the base block unit to control the overall visual scale:

```
--block-unit
```

Smaller values produce a denser grid.  
Larger values create a more architectural layout.

---

## Grid Line Thickness

Adjust the grid separator thickness:

```
--line
```

Examples:

Thin editorial style

```
--line: 6px;
```

Classic De Stijl

```
--line: 10px;
```

Bold graphic layout

```
--line: 16px;
```

---

## Color Palette

The theme typically uses the classic De Stijl palette:

```
--black
--white
--red
--blue
--yellow
```

However these can easily be replaced with alternative palettes for:

- brand integration
- accessibility improvements
- dark mode support

---

# Accessibility Goals

Accessibility is a core design objective.

Future accessibility enhancements will include:

## WCAG AAA Color Profiles

Optional palette variants designed to meet:

- WCAG AA
- WCAG AAA

contrast standards.

---

## Keyboard Navigation Support

Future improvements will support:

- skip links
- improved focus visibility
- predictable tab navigation across grid elements

---

## Reduced Motion Support

Animations and transitions will respect the user preference:

```
prefers-reduced-motion
```

---

## Screen Reader Landmarks

Future layouts may include structured landmark regions:

- header
- navigation
- main content
- complementary regions
- footer

---

# Integration With Static Site Generators

The theme is designed to integrate cleanly with modern static publishing systems.

## MkDocs Integration

The theme can be used with **Material for MkDocs** by placing the grid layout inside the content area.

Typical integration involves:

- custom CSS overrides
- a landing page layout
- optional theme palette adjustments

Example override file:

```
docs/assets/css/stijl-standard.css
```

Example landing page wrapper:

```
<div class="uc-stijl-grid">
    ...
</div>
```

Because MkDocs uses predictable container classes such as:

```
.md-main
.md-content
.md-grid
```

the theme can be integrated without modifying the generator itself.

---

## Other Static Generators

The theme can also be adapted for:

- Hugo
- Jekyll
- Eleventy
- Astro

Integration generally requires only:

- including the CSS file
- wrapping layout sections in grid containers

---

# Future Enhancements

The theme is still evolving.

Planned improvements include:

## Generator-Specific Adapters

Example adapters may be created for:

- MkDocs
- Hugo
- Eleventy

These adapters would include:

- recommended directory structures
- example layouts
- configuration guidance

---

## Accessibility Profiles

Additional theme variants may include:

- **stijl-AA**
- **stijl-AAA**
- **high-contrast accessibility mode**

---

## Component Library

Future versions may introduce reusable layout components such as:

- editorial cards
- gallery panels
- feature blocks
- split layouts
- grid navigation panels

---

## Dark Mode

Future development may include a De Stijl inspired dark palette.

Example concept:

- black structural surfaces
- muted primary accents
- high contrast typography

---

# Philosophy

The goal of **stijl-standard-index** is to create a layout system that is:

- visually timeless
- structurally clear
- accessible
- easy to maintain
- generator-agnostic

By focusing on simple geometric structure and careful color use, the theme avoids trends that quickly become obsolete.

This approach supports long-term static publishing projects where stability and clarity are more valuable than visual novelty.

---

# License

This theme may be distributed under an open license such as:

Creative Commons Attribution-ShareAlike 4.0  
or another appropriate open source license depending on the repository.

Refer to the repository license file for details.

---

# Project Status

Current status: **experimental but stable for landing page layouts**

The theme is actively evolving and improvements will focus on:

- accessibility
- generator integration
- documentation
- modular layout patterns