from django.db import models
from django.urls import reverse

from rest_tournament_manager_app.models.player_model import PlayerModel
from rest_tournament_manager_app.models.tournament_model import TournamentModel


class MatchModel(models.Model):
    match_name = models.CharField(max_length=255, default="")
    match_stage = models.CharField(max_length=255, default=0)
    match_winner = models.ForeignKey(PlayerModel, on_delete=models.CASCADE, related_name='winner', null=True)
    match_loser = models.ForeignKey(PlayerModel, on_delete=models.CASCADE, related_name='loser', null=True)
    match_winning_score = models.PositiveIntegerField(default=0)
    match_losing_score = models.PositiveIntegerField(default=0)
    match_tournament = models.ForeignKey(TournamentModel, on_delete=models.CASCADE, related_name='tournament',
                                         null=True)

    def get_absolute_url(self):
        return reverse('match_details', kwargs={'md': self.id})

    def __str__(self):
        return str(self.match_name)
