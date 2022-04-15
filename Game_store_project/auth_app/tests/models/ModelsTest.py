from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model

from Game_store_project.auth_app.models import UserProfile

UserModel = get_user_model()


class UserProfileTest(TestCase):
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

    def test_when_all_valid__expect_correct(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = UserProfile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        profile.save()

        self.assertIsNotNone(profile.pk)


    def test_when_first_name_contains_a_digit_expect_to_fail(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = UserProfile.objects.create(
            first_name='Georg1',
            last_name='Ivanov',
            image='gosho.jpg',
            date_of_birth='2005-10-30',
            wallet=0,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()


        self.assertIsNotNone(context.exception)

    def test_when_first_name_contains_dollar_sign_expect_to_fail(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = UserProfile.objects.create(
            first_name='Ge$rgi',
            last_name='Ivanov',
            image='gosho.jpg',
            date_of_birth='2005-10-30',
            wallet=0,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_when_first_name_contains_a_space_expect_to_fail(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = UserProfile.objects.create(
            first_name='Ge rgi',
            last_name='Ivanov',
            image='gosho.jpg',
            date_of_birth='2005-10-30',
            wallet=0,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name_when_valid_expect_correct_full_name(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = UserProfile.objects.create(
            first_name='Georgi',
            last_name='Ivanov',
            image='gosho.jpg',
            date_of_birth='2005-10-30',
            wallet=0,
            user=user,
        )

        expected_full_name = f"{self.VALID_PROFILE_DATA['first_name']} {self.VALID_PROFILE_DATA['last_name']}"

        self.assertEqual(profile.get_full_name, expected_full_name)
