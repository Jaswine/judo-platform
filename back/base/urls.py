from django.urls import path

from .views import auth as views
from .views import profile
from .views import tournaments, tournament_admin
from .views import athletes

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
   path('athletes/<int:athlete_id>/update', athletes.update_athlete, name = 'update_athlete'),
   path('athletes/<int:athlete_id>/delete', athletes.delete_athlete, name = 'delete_athlete'),
   
   # Tournaments
   path('tournaments', tournaments.show_tournaments, name='show_tournaments'),
   path('tournaments/create', tournaments.create_tournamets, name='create_tournamets'),
   path('tournaments/<str:slug>/create-tournamets-images', tournaments.create_tournamets__images, name='create_tournamets__images'),
   path('tournaments/<str:slug>/', tournaments.tournamet_show, name='tournamet_show' ),
   
   # Tournament panel
   path('tournaments/<str:slug>/panel/update-info', tournament_admin.tournamets_admin_update_info, name='tournamets_admin_update_info'),
   path('tournaments/<str:slug>/panel/delete-tournament', tournament_admin.tournamets_admin_delete, name='tournamets_admin_delete'),
   
   path('tournaments/<str:slug>/panel/categories/<str:category_slug>/', tournament_admin.tournamets_admin_category, name='tournamets_admin_category'),
   path('tournaments/<str:slug>/panel/categories/<str:category_slug>/athletes', tournament_admin.athletes_admin_category, name='athletes_admin_category'),
   path('tournaments/<str:slug>/panel/categories/<str:category_slug>/toss', tournament_admin.toss_admin_category, name='toss_admin_category'),
   
   # Weight Categoris
   path('tournaments/weight-categories', tournaments.weight_categories, name='weight_categories'),
   path('tournaments/weight-categories-delete/<int:pk>', tournaments.weight_categories_delete, name='weight_categories_delete')
]