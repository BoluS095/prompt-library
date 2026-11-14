# Contributing to Prompt Library

We welcome prompt template contributions! Here's how to submit yours.

## Adding a Template

1. Create a YAML file in the appropriate `templates/` subcategory.
2. Follow the existing template format.
3. Document every `{placeholder}` used in the prompt under `variables`.
4. Include practical `tips` or `notes` for best results.
5. If you have tested a prompt on specific models, record the model and method; do not imply testing that was not performed.
6. Submit a focused Pull Request.

## Automated validation

Install the validator dependency and run:

```bash
python -m pip install pyyaml
python scripts/validate_templates.py
python -m unittest discover -s tests -v
```

The validator checks YAML structure, required fields, category-directory consistency, documented prompt placeholders, and practical notes. It does not measure image quality or prove cross-model compatibility.

## Template quality criteria

- **Consistency** — explain expected use and known limitations.
- **Clarity** — variables should be clearly named and documented.
- **Evidence** — distinguish tested behavior from suggestions or assumptions.

## Modifier contributions

For new modifiers, add to the relevant `.md` file in `modifiers/` with examples.
