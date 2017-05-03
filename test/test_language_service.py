from src.language_service import get_singular_or_plural, get_synonyms
import unittest

class TestLanguageService(unittest.TestCase):

    def test_get_singular_or_plural_returns_plural_by_adding_s(self):
        word = "room"
        actual = get_singular_or_plural(word)
        expected = "rooms"
        self.assertEqual(actual, expected)

    def test_get_singular_or_plural_returns_singular_by_removing_s(self):
        word = "rooms"
        actual = get_singular_or_plural(word)
        expected = "room"
        self.assertEqual(actual, expected)

    def test_get_singular_or_plural_returns_plural_for_y(self):
        word = "baby"
        actual = get_singular_or_plural(word)
        expected = "babies"
        self.assertEqual(actual, expected)

    def test_get_singular_or_plural_returns_singular_for_ies(self):
        word = "facilities"
        actual = get_singular_or_plural(word)
        expected = "facility"
        self.assertEqual(actual, expected)

    def test_get_singular_or_plural_returns_none_for_plural_only_terms(self):
        word = "staff"
        actual = get_singular_or_plural(word)
        expected = None
        self.assertEqual(actual, expected)

    def test_get_synonyms_returns_synonyms_when_synonyms_found(self):
        word = "lavatory"
        actual = get_synonyms(word)
        expected = ["toilet"]
        self.assertEqual(actual, expected)

    def test_get_synonyms_returns_empty_list_when_no_synonyms_found(self):
        word = "room"
        actual = get_synonyms(word)
        expected = []
        self.assertEqual(actual, expected)
