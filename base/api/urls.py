from django.urls import path
from .views import tournaments

urlpatterns = [
   path('tournament-list/',  tournaments.tournament_list, name="tournament_list"),
]
