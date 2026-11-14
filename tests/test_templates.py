import unittest

from scripts.validate_templates import discover_templates, validate_template


class PromptTemplateValidationTests(unittest.TestCase):
    def test_all_repository_templates_are_valid(self):
        templates = discover_templates()
        self.assertEqual(len(templates), 8)
        errors = [error for path in templates for error in validate_template(path)]
        self.assertEqual(errors, [])

    def test_templates_are_yaml_and_have_documented_variables(self):
        for path in discover_templates():
            with self.subTest(template=path.name):
                self.assertEqual(validate_template(path), [])


if __name__ == "__main__":
    unittest.main()
