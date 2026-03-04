# README for Themes Directory

## Description

Place for themes in development

```bash
themes/archive # themes and ideas, tests not ready for prime time
```

## Stijl Themes

### stijl-standard-index

This directory contains the latest and greatest index.md files adapted for running in mkdocs.



It took a while to figure out but by far the easiest and fastest way to work on themes for the content area of mkdocs is to place everything into the standard mkdocs base installation's docs/index.md file.

In the `stijl-standard-index` directory you will find various versions of index.md files and a really boring mkdocs setup like this:

```bash
mkdocs/├── docs
│      └── index.md
├── index-001.md
├── index-002.md
├── index-003.md
├── index-004.md
├── index-hot.md
├── index.md
├── mkdocs.yml
└── readme-mondrian-landing-page-layout-index-004-md.md
```

Super fast way to check them out using mkdocs goes like this:

```bash
cp index-004.md docs/index.md
mkdocs build --clean
mkdocs serve
```

that's is

### stijl-standard

This is a base stijl theme without any fancy stuff.

### archives/stijl



