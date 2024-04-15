from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from ..forms import CreateUserForm

from ..models import Profile
from django.contrib.auth.models import User
from ..services_file import get_tournaments


"""
   Главная страница 
"""
def index(request):
   tournaments = get_tournaments().order_by('-updated')[:3]
   
   context = {
      'tournaments': tournaments,     
   }
   return render(request, 'base/index.html', context)

"""
   Страница регистрации новых пользователей
"""
def registration_view(request):
   page_type = 'registration'
   
   form = CreateUserForm()
   
   if request.method == 'POST':
      # get data from form
      form = CreateUserForm(request.POST)
      
      # check if form is valid
      if form.is_valid():
         new_user = form.save(commit=False)
         new_user.save()
         
         # create user profile
         profile = Profile.objects.create(
            user = new_user, 
            userType = 'Свободный'
         )
         profile.save()
         
         login(request, new_user)
         
         # login user
         return redirect('base:index')
         
   context = {
      'page_type': page_type, 
      'form': form
   }
   return render(request, 'base/auth.html', context)

"""
   Страница аутентификации пользователей
"""
def login_view(request):
   page_type = 'login'
   
   if request.method == 'POST':
      # get data from form
      email = request.POST.get('email')
      password = request.POST.get('password')
            
      try:
         user = User.objects.get(email=email)
         
         if check_password(password, user.password):
            login(request, user)
            return redirect('base:index')
         
      except:
         messages.error(request, 'Email or Password is incorrect')
   
   context = {
      'page_type': page_type,
   }
   return render(request, 'base/auth.html', context)

"""
   Выход пользователя из аккаунта
"""
def logout_view(request):
   logout(request)
   return redirect('base:index') 