from django.urls import path

from .views import auth as views
from .views import profile
from .views import tournaments, tournament_admin

app_name = 'base'

urlpatterns = [
   path('', views.index, name='index'),
   
   # Auth
   path('registration', views.registration_view, name='registration'),
   path('login', views.login_view, name='login'),
   path('logout', views.logout_view, name='logout'),
   
   # Profile
   path('profile/<str:username>/', profile.show_profile, name='show_profile'),
   path('profile/<str:username>/edit', profile.edit_profile, name='edit_profile'),
   path('profile/<str:username>/edit-password', profile.edit_password_profile, name='edit_password_profile'),
   path('profile/<str:username>/delete', profile.delete_account, name='delete_profile'),
   
   # Tournaments
   path('tournaments', tournaments.show_tournaments, name='show_tournaments'),
   path('tournaments/create', tournaments.create_tournamets, name='create_tournamets'),
   path('tournaments/<str:slug>/create-tournamets-images', tournaments.create_tournamets__images, name='create_tournamets__images'),
   path('tournaments/<str:slug>/', tournaments.tournamet_show, name='tournamet_show' ),
   
   # Tournament panel
   path('tournaments/<str:slug>/panel/update-info', tournament_admin.tournamets_admin_update_info, name='tournamets_admin_update_info'),
   path('tournaments/<str:slug>/panel/delete-tournament', tournament_admin.tournamets_admin_delete, name='tournamets_admin_delete'),
   
   # Weight Categoris
   path('tournaments/weight-categories', tournaments.weight_categories, name='weight_categories'),
   path('tournaments/weight-categories-delete/<int:pk>', tournaments.weight_categories_delete, name='weight_categories_delete')
]