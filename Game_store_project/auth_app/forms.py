from django import forms
from django.core.validators import MinValueValidator
from Game_store_project.auth_app.models import UserProfile
from django.contrib.auth import forms as auth_forms, get_user_model
from Game_store_project.auth_app.common.custom_mixins import BootstrapFormMixin
from Game_store_project.auth_app.validtors import validate_only_letters_numbers_underscores, validate_only_letters


UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    username = forms.CharField(
        max_length=UserProfile.USERNAME_MAX_LEN,
        validators=(
            validate_only_letters_numbers_underscores,
        ),
    )

    first_name = forms.CharField(
        max_length=UserProfile.FIRST_NAME_MAX_LEN,
        validators=(
            MinValueValidator(UserProfile.FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    last_name = forms.CharField(
        max_length=UserProfile.LAST_NAME_MAX_LEN,
        validators=(
            MinValueValidator(UserProfile.LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    profile_image = forms.ImageField()

    date_of_birth = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        user_profile = UserProfile(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_image=self.cleaned_data['profile_image'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            user=user,
        )

        if commit:
            user_profile.save()
        return user

    class Meta:
        model = UserModel
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'profile_image',
            'date_of_birth'
        )
        widgets = {
            'username': forms.Textarea(
                attrs={
                    'placeholder': 'Create Username'
                }
            ),
            'first_name': forms.Textarea(
                attrs={
                    'placeholder': 'Enter First Name'
                }
            ),
            'last_name': forms.Textarea(
                attrs={
                    'placeholder': 'Enter First Name'
                }
            ),
        }