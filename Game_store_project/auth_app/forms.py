from django import forms
from django.core.validators import MinLengthValidator
# from django.core.validators import MinValueValidator
from Game_store_project.auth_app.models import UserProfile
from django.contrib.auth import forms as auth_forms, get_user_model
from Game_store_project.auth_app.validtors import validate_only_letters
from Game_store_project.auth_app.common.custom_mixins import BootstrapFormMixin


UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=UserProfile.FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(UserProfile.FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    last_name = forms.CharField(
        max_length=UserProfile.LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(UserProfile.FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    date_of_birth = forms.DateField()

    email = forms.EmailField()


    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = UserProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'email')
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


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None