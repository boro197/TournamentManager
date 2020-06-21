from django.db import models
from django.urls import reverse
from django.utils import timezone


class PlayerModel(models.Model):
    player_name = models.CharField(max_length=255, default="")
    player_mail = models.CharField(max_length=255, default="")
    player_birth_date = models.DateTimeField(timezone.now)

    def get_absolute_url(self):
        return reverse('player_details', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.player_name)
