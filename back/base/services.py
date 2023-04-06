from django.contrib.auth.models import User
from .models import Profile


def get_user(username):
   return User.objects.get(username=username)

def get_user_profile(user):
   return Profile.objects.get(user=user)