from django import forms
from django.utils.datetime_safe import datetime

from rest_tournament_manager_app.models import PlayerModel


class PlayerForm(forms.ModelForm):
    player_birth_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(datetime.now().year - 100, datetime.now().year - 10)))
    player_mail = forms.EmailField()

    class Meta:
        model = PlayerModel
        fields = ['player_name', 'player_mail', 'player_birth_date']
