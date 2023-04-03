from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
   path('', views.index, name='index'),
   
   path('registration', views.registration, name='registration'),
   path('login', views.login, name='login'),
]