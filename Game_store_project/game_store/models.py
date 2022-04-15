from django.db import models
from django.core.validators import MinValueValidator


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


class Feedback(models.Model):
    NICE_RATE = 'Nice'
    MAYBE = 'Maybe'
    BAD = 'Bad'
    MAX_LEN = 20

    rate = models.CharField(
        max_length=MAX_LEN,
        choices=(
            (NICE_RATE, 'Nice'),
            (MAYBE, 'Maybe'),
            (BAD, 'Bad'),
        ),
    )

    feedback = models.TextField()


class ContactAdmins(models.Model):
    text = models.TextField()
