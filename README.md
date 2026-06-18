# 📚 Prompt Library

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
│   ├── portrait/         # Portrait & headshot prompts
│   ├── abstract/         # Abstract art & backgrounds
│   ├── social/           # Social media graphics
│   ├── ads/              # Ad creative prompts
│   └── thumbnails/       # Video thumbnails & covers
├── modifiers/
│   ├── styles.md         # Style modifier library
│   ├── lighting.md       # Lighting modifiers
│   ├── cameras.md        # Camera & lens modifiers
│   └── colors.md         # Color & mood modifiers
├── negative/
│   └── common.md         # Common negative prompts
├── examples/             # Before/after examples
└── README.md
```

## Quick Example

```yaml
# templates/product/floating_product.yaml
name: Floating Product Shot
model: sdxl
category: product

prompt: >
  {product} floating in mid-air, studio lighting, soft gradient
  background {color}, professional product photography, 8K,
  ultra detailed, commercial quality, soft shadows,
  {style_modifier}

negative: >
  blurry, low quality, watermark, text, distorted,
  oversaturated, amateur

variables:
  product: "your product description"
  color: "#hex or color name"
  style_modifier: "see modifiers/styles.md"

settings:
  steps: 30
  cfg_scale: 7
  sampler: DPM++ 2M Karras
  size: 1024x1024
```

## Usage

Each template includes:
- ✅ Tested prompt with variable placeholders
- ✅ Recommended negative prompt
- ✅ Optimal generation settings per model
- ✅ Example outputs (where possible)
- ✅ Tips for customization

## Contributing

Found a great prompt? Submit a PR with:
1. The prompt template in YAML format
2. Which model(s) you tested it on
3. Example output (if you can share)

## License

MIT
