from functools import wraps
from .models import Tournament

import random
import os


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

def generate_slug(form):
   # create massive for slug
   slug = []
   
   # create slug
   if form.cleaned_data.get('category'):
      slug.append(str(form.cleaned_data['category']))
      
   if form.cleaned_data.get('gender'):
      slug.append(str(form.cleaned_data['gender']))
      
   if form.cleaned_data.get('weight'):
      slug.append(str(form.cleaned_data['weight']))
      
   if form.cleaned_data.get('year'):
      slug.append(str(form.cleaned_data['year']))
   
   slug = ' '.join(slug)  
   
   return slug
   