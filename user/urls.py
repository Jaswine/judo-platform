from django.urls import path
from .views import auth

urlpatterns = [
    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('registration/', auth.registration_view, name='registration'),

]