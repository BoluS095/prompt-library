# 📚 Prompt Library

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> Curated, battle-tested prompt templates for AI visual production.

## Why This Exists

Consistent quality in AI visual production requires consistent prompts. This library contains tested, categorized prompt templates that produce reliable results across different generative models.

## Categories

| Category | Templates | Models Tested |
|----------|-----------|---------------|
| 🏢 Product Photography | 15+ | SDXL, DALL-E 3, Midjourney |
| 👤 Portraits & Headshots | 10+ | SDXL, Midjourney |
| 🎨 Abstract & Backgrounds | 20+ | SDXL, DALL-E 3 |
| 📱 Social Media Graphics | 15+ | DALL-E 3, SDXL |
| 🏷️ Ad Creatives | 10+ | DALL-E 3, SDXL |
| 🎬 Thumbnails & Covers | 10+ | SDXL, Midjourney |

## Structure

```
prompt-library/
├── templates/
│   ├── product/          # Product photography prompts
│   ├── abstract/         # Abstract art & backgrounds
│   ├── social/           # Social media graphics
│   ├── ads/              # Ad creative prompts
│   └── thumbnails/       # Video thumbnails & covers
├── modifiers/
│   ├── lighting.md       # Lighting modifier reference
│   ├── cameras.md        # Camera & lens modifiers
│   ├── styles.md         # Style & aesthetic modifiers
│   └── colors.md         # Color palette modifiers
└── negative/
    └── common.md         # Common negative prompt patterns
```

## Template Format

Each template is a YAML file:

```yaml
# templates/product/hero_banner.yaml
name: "Product Hero Banner"
description: "Clean product shot for hero sections"
models: [sdxl, dalle3]

prompt: |
  Professional product photography of {product}, centered composition,
  clean white background, studio lighting, 8k, commercial photography,
  sharp focus, {style_modifier}

parameters:
  product: "your product description"
  style_modifier: "modern minimalist"

negative: "blurry, low quality, distorted, watermark, text"

tips:
  - Works best with simple, well-defined products
  - Add brand colors via style_modifier for consistency
```

## Usage

Templates are designed to work with the [AI Visual Production Toolkit](https://github.com/BoluS095/ai-visual-production-toolkit):

```python
from src.intake.parser import load_template

template = load_template("templates/product/hero_banner.yaml")
prompt = template.render(product="wireless headphones", style_modifier="tech minimalist")
```

Or use standalone — just copy the prompt text and customize the `{variables}`.

## Modifiers

The `modifiers/` directory contains reference sheets for fine-tuning prompts:

- **Lighting** — Studio, natural, dramatic, neon, golden hour, etc.
- **Cameras** — Lens types, focal lengths, depth of field settings
- **Styles** — Art movements, photography styles, aesthetics
- **Colors** — Color theory, palette suggestions, mood mapping

## Contributing

Have a prompt template that consistently produces great results? Contributions welcome!

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE).

## Author

**Rafał Korzeniewski** — Python developer, trainer, and [PyWaw](https://pywaw.org) co-organizer.
