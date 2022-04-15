from django import forms
from django.core.validators import MinValueValidator

from Game_store_project.game_store.models import Games
from Game_store_project.auth_app.common.custom_mixins import BootstrapFormMixin


class CreatingGameForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    image = forms.ImageField()

    name = forms.CharField(
        max_length=Games.NAME_MAX_LEN,
    )

    description = forms.CharField(
        widget=forms.Textarea,
    )

    publication_date = forms.DateTimeField()

    price = forms.FloatField(
        validators=(
            MinValueValidator(Games.PRICE_MIN_VALUE),
        ),
    )

    def save(self, commit=True):
        # game = super().save(commit=commit)

        game = Games(
            image=self.cleaned_data['image'],
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
        )

        if commit:
            game.save()
        return game

    class Meta:
        model = Games
        fields = '__all__'



class EditGameForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Games
        fields = '__all__'


class DeleteGameForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Games
        fields = ()
