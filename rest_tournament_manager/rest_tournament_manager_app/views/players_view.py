from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from forms import *
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


class CreatePlayerView(CreateView):
    form_class = PlayerForm
    model = PlayerModel


class UpdatePlayerView(UpdateView):
    form_class = PlayerForm
    model = PlayerModel


class DeletePlayerView(DeleteView):
    model = PlayerModel

    def get_success_url(self):
        return reverse('players')
