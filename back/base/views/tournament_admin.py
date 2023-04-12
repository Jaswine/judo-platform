from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import get_object_or_404

from ..models import Tournament, Logos, WeightCategory, Sponsors
from ..forms import TournamentForm, WeightCategoryForm
from ..services import get_tournaments

@csrf_exempt
@login_required(login_url='base:login')
def tournamets_admin_update_info(request, slug):
   page_type = 'tournament_panel_update_info'
   
   if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь'):
      tournire = get_object_or_404(Tournament, slug=slug)
      tournament_form = TournamentForm(instance=tournire)
      
      if request.method == 'POST':
         form = TournamentForm(request.POST, instance=tournire)
         
         if form.is_valid():            
            article = form.save(commit=False)
                        
            logotips = request.FILES.getlist('files')
            sponsors_logotips = request.FILES.getlist('sponsors-logotips')
            
            print(len(logotips))
         
            # Add Logotips and Photos
            if len(logotips) > 0:
               for logo in logotips:
                  new_file = Logos(image = logo)
                  
                  new_file.save()  
                  tournire.logos.add(new_file)
               
            # # Add Sponsor Emblems
            if len(sponsors_logotips) > 0:
               for logo in sponsors_logotips:
                  new_file = Sponsors(image = logo)
                  
                  new_file.save()
                  tournire.sponsors.add(new_file)
            
            article.save()
         
      context = {
         'page_type': page_type,
         
         'tournire': tournire,
         'tournament_form': tournament_form,
      }
      return render(request, 'base/tournaments/panel/tournament_panel.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
   
@login_required(login_url='base:login')
def tournamets_admin_delete(request, slug):
   page_type = 'tournamets_admin_delete'
   
   if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь'):
      tournire = get_object_or_404(Tournament, slug=slug)
      
      if request.method == 'POST':
         tournire.delete()
         return redirect('base:show_tournaments')
      
      context = {
         'tournire': tournire,
         'page_type': page_type,
      }
      return render(request, 'base/tournaments/panel/tournament_panel.html',context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')