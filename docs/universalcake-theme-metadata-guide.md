# UniversalCake Theme Metadata Guide

Include a metadata file named:

```bash
theme.yml
```

UniversalCake uses Dublin Core as the canonical metadata format.

Dublin Core allows theme information to remain structured, portable, and compatible with future systems.

---

## Core Dublin Core Elements Primer

The 15 Simple Dublin Core elements include:

- title
- creator
- subject
- description
- publisher
- contributor
- date
- type
- format
- identifier
- source
- language
- relation
- coverage
- rights

Only relevant fields need to be used.

---

## Minimal Example

```yaml
dc:identifier: "mondrian-grid"
dc:title: "Mondrian Grid"
dc:creator: "Christopher Steel"
dc:type: "InteractiveResource"
dc:format: "text/html"
dc:rights: "CC BY-SA 4.0"
```

---

## Short Example With Keywords

Here the subject can be used as keyword and the description can be use as well.

```yaml
dc:identifier: "mondrian-grid"
dc:title: "Mondrian Grid"
dc:creator: "Christopher Steel"
dc:type: "InteractiveResource"
dc:format: "text/html"
dc:subject:
  - "CSS Grid"
  - "Responsive design"
  - "Accessibility"
  - "Structural clarity"
  - "De Stijl"
dc:description: >
  An experimental grid-based web theme inspired by Piet Mondrian.
  Uses asymmetrical CSS Grid segmentation and primary color blocks
  to express structural clarity and interdependence. Fully responsive
  and JavaScript-free.
dc:source: "Piet Mondrian and the De Stijl movement"
dc:rights: "CC BY-SA 4.0"
```

---

## Multiple Creators and Contributors

```yaml
dc:identifier: "mondrian-grid"
dc:title: "Mondrian Grid"

dc:creator:
  - "Alex Rivera (Design)"
  - "Jordan Lee (CSS Implementation)"

dc:contributor:
  - "Vishpala Patel (Logo refinement)"
  - "ChatGPT-4 (OpenAI)"

dc:type: "InteractiveResource"
dc:format: "text/html"
dc:rights: "CC BY-SA 4.0"
```

---

## Creator vs Contributor

- **dc:creator** → Primary intellectual authors.
- **dc:contributor** → Secondary contributors.

If an AI tool assists in creation, it should be listed under `dc:contributor`.

---

## Formatting Guidance

- Use `dc:title`, not `dc_title`.
- Use `dc:rights`, not `dc_rights`.
- Keep formatting consistent across themes.
- Do not invent non-standard Dublin Core fields.

---

## Philosophy

Metadata should:

- Be minimal
- Be accurate
- Reflect intent
- Avoid redundancy

Dublin Core is used to preserve clarity and long-term compatibility.