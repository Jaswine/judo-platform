from .views import tournaments
from django.urls import path


urlpatterns = [
   path('tournaments/logos', tournaments.logos_view, name='logos_view'),
   path('tournaments/logos/<int:id>/', tournaments.one_logo_view, name='one_logo_view'),
]

