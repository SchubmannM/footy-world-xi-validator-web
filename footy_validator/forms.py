from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, MultiField
from django import forms
from .logic.get_player_from_transfermarkt import get_player
from .models import FootballPlayer
from .dataclasses import FootballPlayerData


class FootballPlayerForm(forms.ModelForm):
    class Meta:
        model = FootballPlayer
        fields = ("full_name",)
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Full name (e.g. Thomas Müller)",
                    "required": True,
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get("full_name", "").strip()
        if full_name:
            if not FootballPlayer.objects.filter(full_name__iexact=full_name).exists():
                player = get_player(full_name)
            else:
                player = FootballPlayerData.from_instance(
                    player=FootballPlayer.objects.get(full_name__iexact=full_name)
                )
            if not player:
                msg = "The player with this name could not be found. Please try a different name."
                self.add_error("full_name", msg)
            cleaned_data["player"] = player
        return cleaned_data


class FootballPlayerFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FootballPlayerFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = "post"
        self.layout = Layout(Fieldset("Player {{ forloop.counter }}", "full_name",),)
        self.render_required_fields = True
        self.form_show_labels = False
