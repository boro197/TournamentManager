from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from rest_tournament_manager_app.forms import *
from rest_tournament_manager_app.models import PlayerModel


class AllPlayersView(ListView):
    model = PlayerModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['now'] = timezone.now()
        return context


class PlayerDetailView(DetailView):
    model = PlayerModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['now'] = timezone.now()
        return context


class CreatePlayerView(LoginRequiredMixin, CreateView):
    form_class = PlayerForm
    model = PlayerModel


class UpdatePlayerView(LoginRequiredMixin, UpdateView):
    form_class = PlayerForm
    model = PlayerModel


class DeletePlayerView(LoginRequiredMixin, DeleteView):
    model = PlayerModel

    def get_success_url(self):
        return reverse('players')
