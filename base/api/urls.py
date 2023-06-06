from .views import tournaments
from django.urls import path

urlpatterns = [
   path('tournaments/<str:slug>/weight_categories', tournaments.weight_category),
   path('tournaments/<str:slug>/weight_categories/<int:category_id>/weights', tournaments.weight_category_weights),
   path('tournaments/<str:slug>/weight_categories/<int:category_id>/weights/<int:weight_id>/participants', tournaments.show_participants),
]
