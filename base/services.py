from django.contrib.auth.models import User
from .models import Profile, Tournament, WeightCategory


def get_user(username):
   return User.objects.get(username=username)

def get_user_profile(user):
   return Profile.objects.get(user=user)

def get_tournaments():
   return Tournament.objects.all()

def get_all_weight_category():
   return WeightCategory.objects.all()