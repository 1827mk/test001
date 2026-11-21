import unittest

from labels import is_valid, normalize


class LabelsTest(unittest.TestCase):
    def test_outer_spaces_are_dropped(self):
        self.assertEqual(normalize("  Bug "), "bug")

    def test_an_empty_label_is_not_valid(self):
        self.assertFalse(is_valid("   "))

    def test_twenty_characters_is_the_longest_valid_label(self):
        self.assertTrue(is_valid("a" * 20))
        self.assertFalse(is_valid("a" * 21))

    def test_the_limit_can_be_set(self):
        self.assertTrue(is_valid("abcde", max_length=5))
        self.assertFalse(is_valid("abcdef", max_length=5))


if __name__ == "__main__":
    unittest.main()
