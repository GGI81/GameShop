from django import forms
# from django.core.validators import MinValueValidator
from Game_store_project.auth_app.models import UserProfile
from django.contrib.auth import forms as auth_forms, get_user_model
from Game_store_project.auth_app.common.custom_mixins import BootstrapFormMixin
# from Game_store_project.auth_app.validtors import validate_only_letters_numbers_underscores, validate_only_letters


UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=UserProfile.FIRST_NAME_MAX_LEN,
    )
    last_name = forms.CharField(
        max_length=UserProfile.LAST_NAME_MAX_LEN,
    )
    profile_image = forms.ImageField()
    date_of_birth = forms.DateField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = UserProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_image=self.cleaned_data['profile_image'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'profile_image', 'date_of_birth', 'email',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
        }