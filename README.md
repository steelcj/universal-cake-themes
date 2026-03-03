# universal-cake-themes

## Description

**Universal Cake Themes** is a repository of experimental, resilient, and accessibility-centered web theme explorations.

This repository is not a template marketplace.

It is a design laboratory focused on:

- Structural clarity  
- Accessibility by default  
- Cross-environment resilience  
- Minimal dependency architecture  
- Long-term maintainability  

Each theme is a self-contained exploration of layout, visual language, and semantic structure.

## Contributing Themes

* [/docs/universalcake-theme-contribution-guide.md](./docs/universalcake-theme-contribution-guide.md)

## 

---

## File system layout

```bash
universal-cake-themes/
├── README.md
├── VALUES.md
├── EVALUATION.md
├── docs/
│   ├── theme-values-and-evaluation.md
│   └── automated-verification-plan.md
├── themes/
│   ├── calm-editorial-v2/
│   ├── minimal-structured/
│   └── experimental-grid/
├── tools/
│   └── verify-theme.sh
```

# UniversalCake Themes

## Philosophy

Themes are evaluated not only by visual appeal, but by:

- How clearly they communicate structure  
- How well they respect accessibility standards  
- How gracefully they degrade across environments  
- How independent they are from fragile dependencies  

The goal is not novelty.  
The goal is durable expression and utility.

---

## Core Values

UniversalCake themes aim to prioritize:

- **Accessibility** — semantic HTML, visible focus states, keyboard navigation, WCAG AA contrast targets  
- **Agnosticism** — functional across browsers, devices, and environments  
- **Restraint** — minimal reliance on JavaScript and external frameworks  
- **Portability** — themes should run locally without mandatory external resources  
- **Transparency** — clear metadata and documentation  

---

## universalcake-theme-metadata-guide.mdRepository Structure

All themes live inside:

```bash
themes/
```

Each theme directory contains everything required to understand and run that theme, typically including:

```bash
README.md
index.html
theme.yml
css/
assets/
```

## Generating a Theme Skeleton

You can create a theme skeleton by running `generate-theme-skeleton.py` from the project root.

By default, the script loads:

```
scripts/theme-definition.yml
```

### Basic Usage

```bash
python3 scripts/generate-theme-skeleton.py
```

This will generate a theme using the values defined in `scripts/theme-definition.yml`.

---

### Overriding Theme Metadata

You may override the theme name and creator at runtime:

Create a new theme directory called **stijl-civic**

```bash
python3 scripts/generate-theme-skeleton.py \
  --theme-name stijl-civic 
```

Create a new theme directory called **stijl-civic** by creator **Christopher Steel**

```bash
python3 scripts/generate-theme-skeleton.py \
  --theme-name stijl-civic \
  --theme-creator "Christopher Steel"
```

This allows you to reuse the same YAML structure definition while customizing identity fields.

---

### Optional: Custom YAML File

If you are going to create a number of themes you can specify a custom YAML definition file:

```bash
python3 scripts/generate-theme-skeleton.py --yaml path/to/another-definition.yml
```

The script will generate the theme inside:

```
themes/<theme-name>/
```

* All paths generated are OS agnostic and work across Linux, macOS, and Windows.
* The `theme.yml` file provides structured metadata using Dublin Core.
* This allows themes to remain portable, discoverable, and compatible with future UniversalCake systems.

## What This Repository Is Not

- Not a framework
- Not a design system
- Not a component library
- Not a UI kit

It is a curated archive of layout explorations and architectural thinking expressed through HTML and CSS.

---

## Intended Audience

This repository may be useful to:

- Designers exploring structural composition 
- Developers interested in dependency-light layouts 
- Accessibility advocates  
- Researchers studying resilient publishing patterns  
- Organizations seeking long-term web stability  

---

## Status

Many themes are experimental.

They are meant to be examined, refined, and evolved — not treated as finished products.

Over time, certification tiers or evaluation metrics may be introduced.

---

## License

Unless otherwise noted, themes in this repository are licensed under CC BY-SA 4.0.
