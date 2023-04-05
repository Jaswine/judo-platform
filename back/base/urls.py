from django.urls import path
from .views import auth as views
from .views import profile

app_name = 'base'

urlpatterns = [
   path('', views.index, name='index'),
   
   path('registration', views.registration_view, name='registration'),
   path('login', views.login_view, name='login'),
   path('logout', views.logout_view, name='logout'),
   
   path('profile/<str:username>/', profile.show_profile, name='show_profile'),
   path('profile/<str:username>/edit', profile.edit_profile, name='edit_profile'),
]