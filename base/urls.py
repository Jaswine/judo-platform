from django.urls import path

from .views import auth as views
from .views import profile
from .views import tournaments, tournament_admin
from .views import athletes
from .views import main

app_name = 'base'

urlpatterns = [
   path('', views.index, name='index'),
   
   # Auth
   path('registration', views.registration_view, name='registration'),
   path('login', views.login_view, name='login'),
   path('logout', views.logout_view, name='logout'),
   
   # Profile
   path('profile/<str:username>/', profile.show_profile, name='show_profile'),
   path('profile/<str:username>/athletes', profile.show_all_athletes_profile, name='show_all_athletes'),
   path('profile/<str:username>/edit', profile.edit_profile, name='edit_profile'),
   path('profile/<str:username>/edit-password', profile.edit_password_profile, name='edit_password_profile'),
   path('profile/<str:username>/delete', profile.delete_account, name='delete_profile'),
   
   # Athletes
   path('athletes/create', athletes.add_new_athlete, name = 'add_new_athlete'),
   path('athletes/<int:athlete_id>/update', athletes.update_athlete, name='update_athlete'),
   path('athletes/<int:athlete_id>/delete', athletes.delete_athlete, name='delete_athlete'),
   
   # Tournaments
   path('tournaments', tournaments.show_tournaments, name='show_tournaments'),
   path('tournaments/create', tournaments.create_tournamets, name='create_tournamets'),
   path('tournaments/<str:slug>/create-tournamets-images', tournaments.create_tournamets__images, name='create_tournamets__images'),
   
   # Show One Tournament
   path('tournaments/<str:slug>/', tournaments.tournament_show_about, name='tournament_show'),
   path('tournaments/<str:slug>/participants', tournaments.tournament_show_participants, name='tournament_show_participants'),
   path('tournaments/<str:slug>/protocol', tournaments.tournament_show_protocol, name='tournament_show_protocol'),
   path('tournaments/<str:slug>/fights', tournaments.tournament_show_fights, name='tournament_show_fights'),
   path('tournaments/<str:slug>/result', tournaments.tournament_show_results, name='tournament_show_results'),
   path('tournaments/<str:slug>/medals', tournaments.tournament_show_medals, name='tournament_show_medals'),

   # Tournaments Register
   path('tournaments/<str:slug>/registration-on-tournament', tournaments.registration_on_tournament, name='registration_on_tournament'),
   path('tournaments/<str:slug>/list-of-registered-on-tournament', tournaments.list_of_registered_on_tournament, name='list_of_registered_on_tournament'),

   # Tournament sorting
   path('tournaments/<str:slug>/toss', tournaments.tournament_toss, name='toss'),
   
   # Tournament panel
   path('tournaments/<str:slug>/panel/update-info', tournament_admin.tournamets_admin_update_info, name='tournamets_admin_update_info'),
   path('tournaments/<str:slug>/panel/delete-tournament', tournament_admin.tournamets_admin_delete, name='tournamets_admin_delete'),
   
   path('tournaments/<str:slug>/panel/categories/<str:year>/<str:gender>/athletes', tournament_admin.athletes_admin_category, name='athletes_admin_category'),

   # Weight Categoris
   path('tournaments/weight-categories/<str:slug>', tournaments.weight_categories, name='weight_categories'),
   path('tournaments/weight-categories-delete/<str:slug>/<int:pk>', tournaments.weight_categories_delete, name='weight_categories_delete'),
   path('tournaments/weight-categories/<str:slug>/<int:id>/weight', tournaments.weight_category_weight, name='weight_category_weight'),
   path('tournaments/weight-categories/<str:slug>/<int:id>/weight/<int:weight_id>/delete', tournaments.weight_category_weight_delete, name='weight_category_weight_delete'),

   # Main pages
   path('instructions', main.instructions_view, name='instructions'),
   path('medals', main.medals_view, name='medals'),
   path('sorting', main.sorting_view, name='sorting'),
]