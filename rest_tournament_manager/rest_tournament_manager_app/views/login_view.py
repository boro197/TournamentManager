from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from rest_tournament_manager_app.forms import *


class NewLoginView(LoginView):
    template_name = "rest_tournament_manager_app/index.html"

    def get_success_url(self):
        return reverse_lazy('Index')


class NewLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('Index')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})
