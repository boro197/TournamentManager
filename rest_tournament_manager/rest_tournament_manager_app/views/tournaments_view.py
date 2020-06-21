from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from rest_tournament_manager_app.forms import TournamentForm
from rest_tournament_manager_app.models import TournamentModel, MatchModel


@login_required
def change_score(response, pk):
    player = ''
    if response.GET.get('matchid_a') is not None:
        player = 'a'
    else:
        player = 'b'
    match_id = response.GET.get('matchid_' + player)
    quantity = response.GET.get('quantity_' + player)
    model = MatchModel.objects.get(pk=match_id)

    if player == 'a':
        model.match_score_a = quantity
    else:
        model.match_score_b = quantity

    next_match = model.next_match

    # so-called artificial intelligence
    if next_match is not None and int(model.match_score_a) > int(model.match_score_b):
        if next_match.match_player_a != model.match_player_a and \
                next_match.match_player_a != model.match_player_a and \
                next_match.match_player_a != model.match_player_b and \
                next_match.match_player_a != model.match_player_b:

            if next_match.match_player_a is None:
                next_match.match_player_a = model.match_player_a
            else:
                next_match.match_player_b = model.match_player_a
        while next_match is not None:
            if next_match.match_player_a == model.match_player_b:
                next_match.match_player_a = model.match_player_a
            elif next_match.match_player_b == model.match_player_b:
                next_match.match_player_b = model.match_player_a
            next_match.save()
            next_match = next_match.next_match

    if next_match is not None and int(model.match_score_a) < int(model.match_score_b):
        if next_match.match_player_a != model.match_player_a and \
                next_match.match_player_a != model.match_player_a and \
                next_match.match_player_a != model.match_player_b and \
                next_match.match_player_a != model.match_player_b:
            if next_match.match_player_a is None:
                next_match.match_player_a = model.match_player_b
            else:
                next_match.match_player_b = model.match_player_b
        while next_match is not None:
            if next_match.match_player_a == model.match_player_a:
                next_match.match_player_a = model.match_player_b
            elif next_match.match_player_b == model.match_player_a:
                next_match.match_player_b = model.match_player_b
            next_match.save()
            next_match = next_match.next_match

    model.save()

    return redirect('/tournaments/' + str(pk))


@login_required
def start_tournament(response, pk):
    model = TournamentModel.objects.get(pk=pk)

    current_stage = len(model.tournament_players.all()) / 2
    matches = [MatchModel(match_stage=current_stage)]

    for player in model.tournament_players.all():
        if matches[-1].match_player_a is not None and matches[-1].match_player_b is not None:
            matches[-1].save()
            matches.append(MatchModel(match_stage=current_stage))
        if matches[-1].match_player_a is None:
            matches[-1].match_player_a = player
            matches[-1].save()
        elif matches[-1].match_player_b is None:
            matches[-1].match_player_b = player
            matches[-1].save()
    matches[-1].save()

    rival = None

    while current_stage > 1:
        for match in matches:
            if match.next_match is None and match.match_stage == current_stage:
                if rival is None:
                    rival = match
                else:
                    matches.append(MatchModel(match_stage=match.match_stage / 2))
                    match.next_match = matches[-1]
                    rival.next_match = matches[-1]
                    matches[-1].save()
                    rival = None
        current_stage = current_stage / 2

    for match in matches:
        if match is not None:
            match.save()
            model.tournament_matches.add(match)
    model.tournament_is_started = True
    model.save()
    return redirect('/tournaments')


class AllTournamentsView(ListView):
    template_name = "rest_tournament_manager_app/tournaments_list.html"
    model = TournamentModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['now'] = timezone.now()
        return context


class TournamentDetailView(DetailView):
    template_name = "rest_tournament_manager_app/tournament_bracket.html"
    model = TournamentModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['now'] = timezone.now()
        return context


class CreateTournamentView(LoginRequiredMixin, CreateView):
    form_class = TournamentForm
    model = TournamentModel


class UpdateTournamentView(LoginRequiredMixin, UpdateView):
    model = TournamentModel
    fields = ['tournament_name', 'tournament_players', 'tournament_start_date', 'tournament_is_started']


class DeleteTournamentView(LoginRequiredMixin, DeleteView):
    model = TournamentModel

    def get_success_url(self):
        return reverse('tournaments_list')
