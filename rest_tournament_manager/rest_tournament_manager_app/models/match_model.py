from django.db import models
from django.urls import reverse

from rest_tournament_manager_app.models.player_model import PlayerModel


class MatchModel(models.Model):
    match_name = models.CharField(max_length=255, default="")
    match_stage = models.CharField(max_length=255, default=0)

    match_score_a = models.PositiveIntegerField(default=0)
    match_score_b = models.PositiveIntegerField(default=0)

    next_match = models.ForeignKey("MatchModel", on_delete=models.CASCADE, null=True)

    match_player_a = models.ForeignKey(PlayerModel, on_delete=models.CASCADE, related_name='winner', null=True)
    match_player_b = models.ForeignKey(PlayerModel, on_delete=models.CASCADE, related_name='loser', null=True)

    def get_absolute_url(self):
        return reverse('match_details', kwargs={'md': self.id})

    def __str__(self):
        return str(self.match_name)
