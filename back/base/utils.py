from functools import wraps
from .models import Tournament
import random


# Password checking
def password_checking(user, password, password_confirmation):
   if password == password_confirmation:
      if password != user.password:
         if len(password) < 8:
            return [True, 'OK']
         else:
            return [False, 'password is too short']
      else:
         return [False, 'password == user.password']
   else:
      return [False, 'confirm password is not the same']
   
# Slugs Utils
def slug_generator(string):
   return '-'.join(string.lower().split(' '))

def checking_slug(slug):
   tournaments = Tournament.objects.filter(slug=slug)
   
   if (tournaments.count() > 0):
      slug += str(random.randrange(10000))
      return slug 
   else:
      return slug 

# def Admin_Secretary(function=None, login_url=None):
   #if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь'):