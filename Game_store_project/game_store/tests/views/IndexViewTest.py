from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from Game_store_project.auth_app.models import UserProfile

UserModel = get_user_model()


class IndexViewTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'Georgi_123',
        'password': '12345qwe',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Georgi',
        'last_name': 'Ivanov',
        'image': 'gosho.jpg',
        'date_of_birth': '2005-10-30',
        'wallet': 0,
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(
            **credentials
        )

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)

        profile = UserProfile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

