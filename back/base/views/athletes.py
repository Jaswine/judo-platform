from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from ..models import Participant
from ..forms import ParticipantForm


@login_required(login_url='base:login')
def add_new_athlete(request):
   page_type = 'add_new_athlete'
   
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      form = ParticipantForm()
      
      if request.method == 'POST':
         
         form = ParticipantForm(request.POST)
         coach = request.POST.get('coach', request.user.profile.fullName)
         
         if form.is_valid():
            athlete = form.save(commit=False)
            
            athlete.user = request.user
            athlete.coach = coach
            
            athlete.save()
            
            return redirect('base:show_all_athletes', request.user.username)
               
      context = {
         'page_type': page_type,         
         'form': form
      }
      return render(request, 'base/profile/athlete/add_athlete.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
   
@login_required(login_url='base:login')
def update_athlete(request, athlete_id):
   page_type = 'update_athlete'
   athlete = Participant.objects.get(id=athlete_id)
   
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      form = ParticipantForm(instance=athlete)
      
      if request.method == 'POST':
         
         form = ParticipantForm(request.POST, instance=athlete)
         coach = request.POST.get('coach', request.user.profile.fullName)
         
         if form.is_valid():
            athlete = form.save(commit=False)
            athlete.coach = coach
            athlete.save()
            
            return redirect('base:show_all_athletes', request.user.username)
               
      context = {
         'page_type': page_type,
                  
         'form': form,
         'athlete': athlete,         
      }
      return render(request, 'base/profile/athlete/add_athlete.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
   
@login_required(login_url='base:login')
def delete_athlete(request, athlete_id):
   page_type = 'delete_athlete'
   athlete = Participant.objects.get(id=athlete_id)
   
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):      
      if request.method == 'POST':
         athlete.delete()
         return redirect('base:show_all_athletes', request.user.username)
               
      context = {
         'page_type': page_type,
      }
      return render(request, 'base/profile/athlete/delete_athlete.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
