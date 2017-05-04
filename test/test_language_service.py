from src.language_service import LanguageService

import unittest

class TestLanguageService(unittest.TestCase):

    def setUp(self):
        self._language_service = LanguageService()

    def test_get_singular_or_plural_returns_plural_by_adding_s(self):
        word = "room"
        actual = self._language_service.get_singular_or_plural(word)
        expected = "rooms"
        self.assertEqual(actual, expected)

    def test_get_singular_or_plural_returns_singular_by_removing_s(self):
        word = "rooms"
        actual = self._language_service.get_singular_or_plural(word)
        expected = "room"
        self.assertEqual(actual, expected)

    def test_get_singular_or_plural_returns_plural_for_y(self):
        word = "baby"
        actual = self._language_service.get_singular_or_plural(word)
        expected = "babies"
        self.assertEqual(actual, expected)

    def test_get_singular_or_plural_returns_singular_for_ies(self):
        word = "facilities"
        actual = self._language_service.get_singular_or_plural(word)
        expected = "facility"
        self.assertEqual(actual, expected)

    def test_get_singular_or_plural_returns_none_for_plural_only_terms(self):
        word = "staff"
        actual = self._language_service.get_singular_or_plural(word)
        expected = None
        self.assertEqual(actual, expected)

    def test_get_synonyms_returns_synonyms_when_synonyms_found(self):
        word = "lavatory"
        actual = self._language_service.get_synonyms(word)
        expected = ["toilet"]
        self.assertEqual(actual, expected)

    def test_get_synonyms_returns_empty_list_when_no_synonyms_found(self):
        word = "room"
        actual = self._language_service.get_synonyms(word)
        expected = []
        self.assertEqual(actual, expected)
