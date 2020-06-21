from rest_tournament_manager_app.views.index_view import IndexView
from rest_tournament_manager_app.views.login_view import LoginView, LogoutView, register
from rest_tournament_manager_app.views.players_view import AllPlayersView, PlayerDetailView, \
    CreatePlayerView, UpdatePlayerView, DeletePlayerView
from rest_tournament_manager_app.views.tournaments_view import AllTournamentsView, TournamentDetailView, \
    CreateTournamentView, UpdateTournamentView, DeleteTournamentView

__all__ = ['IndexView', 'LoginView', 'LogoutView', 'AllTournamentsView', 'TournamentDetailView',
           'CreateTournamentView', 'UpdateTournamentView', 'DeleteTournamentView', 'AllPlayersView', 'PlayerDetailView',
           'CreatePlayerView', 'UpdatePlayerView', 'DeletePlayerView', 'register']
