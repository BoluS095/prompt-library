# Prompt Library

[![Template validation](https://github.com/BoluS095/prompt-library/actions/workflows/validate-templates.yml/badge.svg)](https://github.com/BoluS095/prompt-library/actions/workflows/validate-templates.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A compact collection of YAML prompt templates and Markdown reference sheets for AI-assisted visual work.

## Current contents

The repository contains **8 YAML templates**:

| Category | Templates |
|---|---|
| Product | 3 — Floating product, hero banner, lifestyle flat lay |
| Abstract | 1 — Gradient background |
| Ads | 1 — Product display ad |
| Social | 2 — Instagram post, LinkedIn thought leadership |
| Thumbnails | 1 — YouTube thumbnail |

It also includes four modifier references (lighting, cameras, styles, colours) and a common negative-prompt reference.

## Maturity and evaluation

This repository is a prompt reference library, not a benchmark. The templates are not accompanied by a reproducible cross-model image-quality evaluation suite or measured quality results. Model names in individual files are compatibility suggestions, not evidence of comparative testing or guaranteed output quality.

## Automated validation

GitHub Actions validates all YAML templates on Python 3.10, 3.11, and 3.12. The checks cover YAML parsing, required metadata, category-directory consistency, documented prompt placeholders, and practical notes.

Run the same checks locally:

```bash
python -m pip install pyyaml
python scripts/validate_templates.py
python -m unittest discover -s tests -v
```

These checks validate structure and documentation; they do not score generated images or establish cross-model performance.

## How to use

Open a YAML file, replace its placeholders with your product, brand, composition, and style details, then adapt the prompt for the image model you use.

For example, `templates/product/hero_banner.yaml` documents placeholders for a brand, product, background description, and colour palette. Copy the prompt text into your chosen image-generation tool and replace those values.

The template files can be browsed and adapted without installing a runtime package. Python and PyYAML are only needed to run the automated validation.

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
scripts/
  validate_templates.py
tests/
  test_templates.py
.github/
  workflows/
    validate-templates.yml
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md). Include a concise use case, intended category, all required variables, and any model-specific notes. Do not describe a template as tested unless reproducible evaluation evidence is included.

## License

MIT. See [LICENSE](LICENSE).
