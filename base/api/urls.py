from django.urls import path
from .views import tournaments, athlete_registration, toss, one_tournament_show

urlpatterns = [
   path('tournament-list/',  tournaments.tournament_list, name="tournament_list"),
   
   path('athlete-registration/<int:id>/',
            athlete_registration.show_weight_categories,
                name="athlete_registration"),
   path('list-of-registered-on-tournament/<int:id>/',
            athlete_registration.list_of_registered_on_tournament,
                name="list_of_registered_on_tournament"),

   path('tournament/<int:id>/show-all-categories-weights/',
            toss.show_weight_categories_and_weights,
                name="show_weight_categories_and_weights"),
   path('tournaments/<int:tournament_id>/weight/<int:weight_id>/update',
            toss.show_weight_categories_and_weights_update,
                name='show_weight_categories_and_weights_update'),

   path('tournament/<int:id>/show-all-categories-weights-sorting/',
            one_tournament_show.show_weight_categories_and_weights_and_sorting,
                name="show_weight_categories_and_weights_and_sorting"),
]
