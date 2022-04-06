import re
from django.core.exceptions import ValidationError


VALIDATION_ERROR_MESSAGE1 = "Ensure this value contains only letters, numbers, and underscore!"
VALIDATION_ERROR_MESSAGE2 = "Ensure this value contains only letters!"


def validate_only_letters_numbers_underscores(value):
    if not re.match(r'^[A-Za-z0-9_]+$', value):
        raise ValidationError(VALIDATION_ERROR_MESSAGE1)
    return value


def validate_only_letters(value):
    for i in value:
        if not i.isalpha():
            raise ValidationError(VALIDATION_ERROR_MESSAGE2)
    return value


