from django.urls import path

from rest_tournament_manager_app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", register, name="register"),

    path('tournaments/', AllTournamentsView.as_view(), name='tournaments_list'),
    path('tournaments/<int:pk>/', TournamentDetailView.as_view(), name='tournament_details'),
    path('tournaments/<int:pk>/add/', CreateTournamentView.as_view(), name='tournament_create'),
    path('tournaments/<int:pk>/delete/', DeleteTournamentView.as_view(), name='tournament_delete'),
    path('tournaments/<int:pk>/update/', UpdateTournamentView.as_view(), name='tournament_update'),

    path('players', AllPlayersView.as_view(), name='PlayersList'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player_details'),
    path('players/<int:pk>/add/', CreatePlayerView.as_view(), name='player_create'),
    path('players/<int:pk>/delete/', DeletePlayerView.as_view(), name='player_delete'),
    path('players/<int:pk>/update/', UpdatePlayerView.as_view(), name='player_update'),
]
