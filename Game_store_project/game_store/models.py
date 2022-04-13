from django.core.validators import MinValueValidator
from django.db import models


class Games(models.Model):
    NAME_MAX_LEN = 30
    PRICE_MIN_VALUE = 0.01

    image = models.ImageField(
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=30,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )