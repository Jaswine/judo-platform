from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from ..services import get_user, get_user_profile
from ..forms import UpdateUserForm, UpdateProfileForm
from ..utils import password_checking
from ..models import Participant


@login_required(login_url='base:login')
def show_profile(request, username):
   page_type = 'view_profile'
   
   user = get_user(username)
   profile = get_user_profile(user)
   
   if request.method == 'POST':
      form_type = request.POST.get('form_type')
      
      if form_type == 'change__status':
         user_type = request.POST.get('user_type')
         
         if user_type:
            profile.userType = user_type
            profile.save()
   
   context = {
      'page_type': page_type,
      'user': user,
      'profile': profile,
   }
   return render(request, 'base/profile.html', context)
   
@login_required(login_url='base:login')
def edit_profile(request, username):
   page_type = 'edit_profile'
   
   user = get_user(username)
   profile = get_user_profile(user)
   
   if request.user.username == user.username:
      user_form = UpdateUserForm(instance=user)
      profile_form = UpdateProfileForm(instance=profile)
      
      if request.method == 'POST':
         user_form = UpdateUserForm(request.POST, instance=user)
         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
         
         if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('base:show_profile', username=user.username)
      
      context = {
         'page_type': page_type,
         
         'user': user,
         'profile': profile,
         
         'user_form': user_form,
         'profile_form': profile_form,
         'form': [user_form, profile_form],
      }
      return render(request, 'base/profile.html', context)
   else:
      return redirect('base:show_profile', username=user.username)
   
@login_required(login_url='base:login')
def edit_password_profile(request, username):
   page_type = 'edit_password'
   
   user = get_user(username)
   
   if request.user.username == user.username:
      profile = get_user_profile(user)
      if request.method == 'POST':
         # get data from form
         password = request.POST.get('password')
         password_confirmation = request.POST.get('password_confirmation')
         
         validation = password_checking(user, password, password_confirmation)
         print(validation[0])
         
         if validation:
            user.password = password
            user.save()
            
            return redirect('base:show_profile', username=user.username)
         else:
            messages.error(request, validation[1])
         
      context = {
         'page_type': page_type,
         
         'user': user,
         'profile': profile,
      }
      return render(request, 'base/profile.html', context)
   else:
      return redirect('base:show_profile', username=user.username)
   
@login_required(login_url='base:login')
def delete_account(request, username):
   page_type = 'delete_account'
   
   user = get_user(username)
   profile = get_user_profile(user)
   
   if request.user.username == user.username:
      if request.method == 'POST':
         user.delete()
         profile.delete()
         
         return redirect('base:login')
   else:
      return redirect('base:show_profile', username=user.username)
   
   context =  {
      'page_type': page_type,
      
      'user': user,
      'profile': profile,
   }
   return render(request, 'base/profile.html', context)

def show_all_athletes_profile(request, username):
   page_type = 'show_all_athletes'
   
   user = get_user(username)
   profile = get_user_profile(user)
   
   participants = Participant.objects.filter(user=user) 
   # participants_count = Participant.objects.filter(user=user).count()  
   
   context =  {
      'page_type': page_type,
      
      'user': user,
      'profile': profile,
      
      'participants': participants
   }
   return render(request, 'base/profile.html', context)