from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import Profile
from ..forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.models import User

@login_required(login_url='base:login')
def show_profile(request, username):
   page_type = 'view_profile'
   
   user = User.objects.get(username=username)
   profile = Profile.objects.get(user=user)
   
   context = {
      'page_type': page_type,
      'user': user,
      'profile': profile,
   }
   return render(request, 'base/profile.html', context)
   
@login_required(login_url='base:login')
def edit_profile(request, username):
   page_type = 'edit_profile'
   
   user = User.objects.get(username=username)
   profile = Profile.objects.get(user=user)
   
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