from django.core.checks import register
from django.db import models
from django.urls import reverse
from django.utils import timezone

from rest_tournament_manager_app.models.player_model import PlayerModel
from rest_tournament_manager_app.models.match_model import MatchModel


class TournamentModel(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    tournament_name = models.CharField(max_length=255)
    tournament_players = models.ManyToManyField(PlayerModel)
    tournament_matches = models.ManyToManyField(MatchModel)
    tournament_is_started = models.BooleanField(default=False)
    tournament_start_date = models.DateTimeField(default=timezone.now)
    tournament_max_number_of_players = models.PositiveIntegerField(default=8)

    def get_absolute_url(self):
        return reverse('tournament_details', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.tournament_name)

    def start(self):
        print("Hello ! " + self.id)
