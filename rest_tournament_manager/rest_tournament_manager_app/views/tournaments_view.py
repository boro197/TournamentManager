from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from rest_tournament_manager_app.forms import TournamentForm
from rest_tournament_manager_app.models import TournamentModel


class AllTournamentsView(ListView):
    template_name = "rest_tournament_manager_app/tournaments_list.html"
    model = TournamentModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['now'] = timezone.now()
        return context


class TournamentDetailView(DetailView):
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
