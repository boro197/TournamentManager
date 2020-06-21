from math import log10, floor, ceil

from django import forms

from rest_tournament_manager_app.models import TournamentModel


def log2(x):
    return (log10(x) / log10(2));


def is_power_of_two(n):
    return ceil(log2(n)) == floor(log2(n)) and n > 1;


class TournamentForm(forms.ModelForm):
    tournament_max_number_of_players = forms.IntegerField(min_value=2, max_value=64)

    def clean_tournament_players(self):
        data = self.cleaned_data['tournament_players']
        max_players = self.data['tournament_max_number_of_players']
        if len(data) > int(max_players):
            raise forms.ValidationError("To many players !")
        if not is_power_of_two(len(data)):
            raise forms.ValidationError("Number of players has to be power of 2 !")

        return data

    def clean_tournament_max_number_of_players(self):
        data = self.cleaned_data['tournament_max_number_of_players']
        if not is_power_of_two(int(data)):
            raise forms.ValidationError("Number of players has to be power of 2 !")
        return data

    class Meta:
        model = TournamentModel
        fields = ['tournament_name', 'tournament_max_number_of_players', 'tournament_players', 'tournament_start_date']
