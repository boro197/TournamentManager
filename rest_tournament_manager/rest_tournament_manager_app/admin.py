from django.contrib import admin

from rest_tournament_manager_app.models import *

# Register your models here.
admin.site.register(TournamentModel)
admin.site.register(PlayerModel)
admin.site.register(MatchModel)
