from django.db import models
from django.urls import reverse


class PlayerModel(models.Model):
    player_first_name = models.CharField(max_length=255, default="")
    player_last_name = models.CharField(max_length=255, default="")

    def get_absolute_urls(self):
        return reverse('player_details', kwargs={'pd': self.id})

    def __str__(self):
        return str(self.player_first_name + " " + self.player_last_name)
