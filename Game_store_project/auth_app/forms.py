from django import forms
from django.core.validators import MinLengthValidator
from Game_store_project.auth_app.models import UserProfile, MoreInfo
from django.contrib.auth import forms as auth_forms, get_user_model
from Game_store_project.auth_app.validtors import validate_only_letters
from Game_store_project.auth_app.common.custom_mixins import BootstrapFormMixin


UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

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


    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = UserProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'date_of_birth']
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



class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'image']


class ChangePasswordForm(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None


class AddMoreInfo(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = MoreInfo
        fields = '__all__'