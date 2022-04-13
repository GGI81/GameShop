from django.db import models
# from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.contrib.auth import models as auth_models
from Game_store_project.auth_app.manager import AppUserManager
from Game_store_project.auth_app.validtors import validate_only_letters_numbers_underscores, validate_only_letters

"""
1. Create a model extending AbstractBaseUser and PermissionsMixin
2. Tell Django for your user model -> settings.py 'auth_app.AppUser'
3. Create user manager
"""


class GameStoreUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=(
            validate_only_letters_numbers_underscores,
        ),
    )

    email = models.EmailField()

    # date_joined = models.DateTimeField(
    #     auto_now_add=True,
    # )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = AppUserManager()


class UserProfile(models.Model):
    USERNAME_MAX_LEN = 15

    FIRST_NAME_MAX_LEN = 20
    FIRST_NAME_MIN_LEN = 2

    LAST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 2

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        unique=False,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        unique=False,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
        null=True,
        blank=True,
        # upload_to='profile_pic',
        # default='no_profile.jpg',
    )

    wallet = models.FloatField(
        default=0,
    )

    user = models.OneToOneField(
        GameStoreUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

