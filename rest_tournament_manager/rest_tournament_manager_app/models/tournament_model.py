from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from rest_tournament_manager_app.models.player_model import PlayerModel


class TournamentModel(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    tournament_name = models.CharField(max_length=255)
    tournament_players = models.ManyToManyField(PlayerModel)
    tournament_is_started = models.BooleanField(default=False)

    def get_absolute_urls(self):
        return reverse('tournament_details', kwargs={'td': self.id})

    def __str__(self):
        return str(self.tournament_name)

    def save(self, **kwargs):
        print(self._meta.concrete_fields[0], self.tournament_is_started.__)
        super().save(**kwargs)
