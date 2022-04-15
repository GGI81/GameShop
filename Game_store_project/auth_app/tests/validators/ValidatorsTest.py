from django.test import TestCase
from django.core.exceptions import ValidationError
from Game_store_project.auth_app.validtors import validate_only_letters_numbers_underscores, validate_only_letters


class ValidateOnlyLettersNumbersUnderscoresTest(TestCase):
    def test_if_username_contains_only_letters_numbers_and_underscores_expect_correct(self):
        var = 'Georgi_123'
        self.assertEqual(validate_only_letters_numbers_underscores(var), 'Georgi_123')

    def test_if_username_contains_white_space_expect_validation_error(self):
        var = 'Georgi 123'

        with self.assertRaises(ValidationError):
            validate_only_letters_numbers_underscores(var)

    def test_if_username_contains_not_allowed_symbol_expect_validation_error(self):
        var = 'Georgi$123'

        with self.assertRaises(ValidationError):
            validate_only_letters_numbers_underscores(var)


class ValidateOnlyLettersTest(TestCase):
    def test_if_name_contains_only_letters_expect_correct(self):
        var = 'Georgi'
        self.assertEqual(validate_only_letters(var), 'Georgi')

    def test_if_name_contains_white_space_expect_validation_error(self):
        var = 'Georgi '

        with self.assertRaises(ValidationError):
            validate_only_letters_numbers_underscores(var)

    def test_if_name_contains_not_letter_symbols_expect_validation_error(self):
        var = 'Georgi$'

        with self.assertRaises(ValidationError):
            validate_only_letters_numbers_underscores(var)
