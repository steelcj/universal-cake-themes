# UniversalCake Theme Contribution Guide

This repository contains theme explorations and reference implementations.

All themes live inside:

```
themes/
```

## Documentation

* [universalcake-theme-metadata-guide.md](./universalcake-theme-metadata-guide.md)

Theme Directories

Each theme directory is in a theme named directory. This is self-contained and includes all of the information required in order to understand and used the theme. So documentation, assets, and metadata and all other requirements.

```bash
themes/
├── mondrian-grid/
├── calm-editorial/
├── structured-minimal/
├── pride-spectrum/
├── disability-clarity/
└── ...
```

---

## Adding a New Theme

### Create a Theme Directory

Use lowercase, hyphen-separated naming:

```
themes/your-theme-name/
```

Examples:

- `mondrian-grid`
- `calm-editorial`
- `structured-minimal`
- `disability-clarity`
- `pride-spectrum`

Avoid:

- CamelCase
- Spaces
- Excessively long names
- Slogans
- Trend-driven naming

Names should describe structural or aesthetic characteristics.

### Directory Contents

A theme directory might contain the following depending on how the theme is setup:

```
README.md
index.html
theme.yml
css/
assets/
(optional) js/
```

Themes must run locally in a browser, preferably without any mandatory external dependencies for core rendering.

So that means, no CDN fonts, remote icons, or other external frameworks required for baseline functionality.

If the answer to the following is "Yes", then you are good to go

> Will the theme be fully functional when used on a system that is never connected to the internet?



---

## Accessibility

We work towards themes that:

- Use semantic HTML
- Maintain logical heading hierarchy
- Provide visible focus states
- Meet WCAG AA contrast standards
- Be fully keyboard navigable
- Respect `prefers-reduced-motion`

Themes experimenting beyond these boundaries must clearly document tradeoffs.

---

## Agnosticism

High quality themes:

- Render consistently across major browser engines
- Function at narrow mobile widths
- Work without JavaScript for core content
- Avoid fragile CSS hacks
- Avoid mandatory external dependencies

---

## Review Process

Themes may undergo:

- Human review
- Qualitative evaluation across:
  - Accessibility
  - Agnosticism
  - Cognitive clarity

Certification tiers may be introduced over time.

---

## Metadata

Each theme includes a `theme.yml` file.

UniversalCake uses Dublin Core metadata as a canonical metadata format.

See  [Universalcake Theme Metadata Guide](./universalcake-theme-metadata-guide.md)



------

for detailed guidance and examples.

---

## References



[Universalcake Theme Metadata Guide]: ./universalcake-theme-metadata-guide.md	"Universalcake Theme Metadata Guide.md"

## License

This repository is licensed under CC BY-SA 4.0 unless otherwise noted.