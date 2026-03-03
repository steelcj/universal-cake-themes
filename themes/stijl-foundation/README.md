# Stijl Foundation

Stijl Foundation is the structural base of the Stijl theme family — a responsive De Stijl–inspired grid layout focused purely on architectural clarity.

It provides the core layout system and visual language without accessibility tuning, framework integration, or breakpoint refinement beyond mobile collapse.

This version is intentionally minimal.

------

## Design Inspiration

Stijl Foundation draws from the principles of the Dutch De Stijl movement, associated with artists such as **Piet Mondrian** and **Theo van Doesburg**.

Key influences:

- Geometric abstraction
- Primary color palette
- Black structural framing
- Asymmetrical balance
- Rational grid composition

------

## Purpose

Stijl Foundation exists to:

- Serve as the architectural root of the Stijl theme family
- Provide a clean responsive grid system
- Separate layout structure from compliance tuning
- Act as a base for MkDocs or other static site integrations
- Allow higher variants (Standard, AA, AAA, Gov) to extend it cleanly

It intentionally does **not** include:

- Accessibility compliance tuning
- Skip links
- Focus styling overrides
- Intermediate tablet breakpoint refinements
- Framework-specific templating

------

## Features

- CSS Grid layout
- 6-column desktop grid
- Mobile breakpoint (single-column collapse)
- Primary color block system
- Structural spacing variable (`--line`)
- System font stack
- Zero dependencies
- No JavaScript

------

## Layout Structure

```
.wrapper
├── header
│   └── nav
├── main
│   ├── .projects
│   ├── .areas
│   ├── .resources
│   └── .about
└── footer
```

------

## Grid Behavior

### Desktop

- 6-column grid
- Asymmetrical spans
- Structural black framing

### Mobile (≤ 600px)

- Single-column layout
- Vertical stacking
- Navigation becomes column-oriented

There is **no distinct tablet layout** in this version.
 Intermediate refinement is intentionally deferred to higher variants such as `stijl-standard`.

------

## Color System

```
--black:  #000
--white:  #ffffff
--red:    #d00000
--blue:   #0033cc
--yellow: #f2c200
--line:   10px
```

These variables define the structural rhythm and color identity.

Higher variants may override these tokens.

------

## Architectural Role in the Stijl Family

```
stijl-foundation  → structural base
stijl-standard    → refined breakpoints
stijl-aa          → WCAG AA tuning
stijl-aaa         → WCAG AAA tuning
stijl-gov         → compliance-oriented variant
```

Foundation defines structure.
 Variants define refinement and compliance.

------

## Intended Use Cases

- Experimental grid-based sites
- Portfolio layouts
- Structural prototype systems
- Base for accessibility overlays
- Candidate for MkDocs theme conversion

Because this version is layout-pure and unopinionated about compliance, it is the recommended candidate for conversion into a generator-native theme.

------

## Converting to MkDocs

To make this a MkDocs-native theme:

1. Replace content areas with `{{ content }}`
2. Replace navigation with `{{ nav }}`
3. Introduce Jinja template blocks
4. Move CSS into a static assets directory
5. Add search integration if desired

The simplicity of this version makes it ideal for controlled adaptation.

------

## License

Specify a license when distributing:

- MIT (recommended for themes)
- CC BY-SA 4.0 (aligned with UniversalCake philosophy)
- GPL (if bundled with tooling)