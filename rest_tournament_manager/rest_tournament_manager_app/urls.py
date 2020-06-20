
from django.contrib import admin
from django.urls import path, include
from rest_tournament_manager_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='Index')
]
