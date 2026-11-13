# Prompt Library

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A compact collection of YAML prompt templates and Markdown reference sheets for AI-assisted visual work.

## Current contents

The repository currently contains **8 YAML templates**:

| Category | Templates |
|---|---|
| Product | 3 — Floating product, hero banner, lifestyle flat lay |
| Abstract | 1 — Gradient background |
| Ads | 1 — Product display ad |
| Social | 2 — Instagram post, LinkedIn thought leadership |
| Thumbnails | 1 — YouTube thumbnail |

It also includes four modifier references (lighting, cameras, styles, colours) and a common negative-prompt reference.

## Maturity and evaluation

This repository is a prompt reference library, not a benchmark. The templates have not been accompanied by a reproducible cross-model evaluation suite or measured quality results. Model names in individual files are compatibility suggestions, not evidence of comparative testing or guaranteed output quality.

## How to use

Open a YAML file, replace its placeholders with your product, brand, composition, and style details, then adapt the prompt for the image model you use.

For example, `templates/product/hero_banner.yaml` includes placeholders for a brand, product, background description, and colour palette. Copy the prompt text into your chosen image-generation tool and replace those values.

The files are intended to be usable independently. No Python package or runtime dependency is required to browse and adapt the templates.

## Repository structure

```
templates/
  abstract/
  ads/
  product/
  social/
  thumbnails/
modifiers/
  cameras.md
  colors.md
  lighting.md
  styles.md
negative/
  common.md
```

## Contributing

Please include a concise use case, the intended category, all required variables, and any model-specific notes. Do not describe a template as tested unless reproducible evaluation evidence is included.

## License

MIT. See [LICENSE](LICENSE).
