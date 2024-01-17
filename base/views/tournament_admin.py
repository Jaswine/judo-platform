from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage

from ..models import Tournament, Logos, WeightCategory, Sponsors, Participant, Weight
from ..forms import UpdateTournamentMainInformationForm
from ..services import get_tournaments


@csrf_exempt
@login_required(login_url='base:login')
def tournamets_admin_update_info(request, slug):
   page_type = 'tournament_panel_update_info'
   
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      tournire = get_object_or_404(Tournament, slug=slug)
      form = UpdateTournamentMainInformationForm(instance=tournire)
   
      # get data from form        
      if request.method == 'POST':
         form = UpdateTournamentMainInformationForm(request.POST, request.FILES, instance=tournire)
         
         if form.is_valid():           
            logotips = request.FILES.getlist('files')
            sponsors_logotips = request.FILES.getlist('sponsors-logotips')
            
            delete_logotips = request.POST.getlist('delete-logotips')
            delete_sponsors = request.POST.getlist('delete-sponsors')
            
            # # delete choices logtips
            if (len(delete_logotips) > 0):
               for logotip in delete_logotips:
                  tournire.logos.filter(id=int(logotip)).delete()
                  
            # # delete choices logtips
            if (len(delete_sponsors) > 0):
               for sponsor in delete_sponsors:
                  tournire.sponsors.filter(id=int(sponsor)).delete()
         
            # # Add Logotips and Photos
            if len(logotips) > 0:
               for logo in logotips:
                  new_file = Logos(image = logo)
                  
                  new_file.save()  
                  tournire.logos.add(new_file)
               
            # # # Add Sponsor Emblems
            if len(sponsors_logotips) > 0:
               for logo in sponsors_logotips:
                  new_file = Sponsors(image = logo)
                  
                  new_file.save()
                  tournire.sponsors.add(new_file)
            
            
            tournire.title = form.cleaned_data.get('title_en')
            tournire.title_en = form.cleaned_data.get('title_en')
            tournire.title_ru = form.cleaned_data.get('title_ru')
            tournire.title_kk = form.cleaned_data.get('title_kk')
            
            tournire.logo = form.cleaned_data.get('logo')
            
            tournire.about = form.cleaned_data.get('about_en')
            tournire.about_en = form.cleaned_data.get('about_en')
            tournire.about_ru = form.cleaned_data.get('about_ru')
            tournire.about_kk = form.cleaned_data.get('about_kk')
            
            tournire.rang = form.cleaned_data.get('rang')
            
            tournire.startData = form.cleaned_data.get('startData')
            tournire.finishData = form.cleaned_data.get('finishData')
            tournire.startTime = form.cleaned_data.get('startTime')
            
            tournire.credit = form.cleaned_data.get('credit')
            tournire.tatamis_count = form.cleaned_data.get('tatamis_count')

            tournire.place = form.cleaned_data.get('place_en')
            tournire.place_en = form.cleaned_data.get('place_en')
            tournire.place_ru = form.cleaned_data.get('place_ru')
            tournire.place_kk = form.cleaned_data.get('place_kk')
            
            tournire.chiefJustice = form.cleaned_data.get('chiefJustice_en')
            tournire.chiefJustice_en = form.cleaned_data.get('chiefJustice_en')
            tournire.chiefJustice_ru = form.cleaned_data.get('chiefJustice_ru')
            tournire.chiefJustice_kk = form.cleaned_data.get('chiefJustice_kk')
            
            tournire.chiefSecretary = form.cleaned_data.get('chiefSecretary_en')
            tournire.chiefSecretary_en = form.cleaned_data.get('chiefSecretary_en')
            tournire.chiefSecretary_ru = form.cleaned_data.get('chiefSecretary_ru')
            tournire.chiefSecretary_kk = form.cleaned_data.get('chiefSecretary_kk')
            
            tournire.status = form.cleaned_data.get('status')
            tournire.public = form.cleaned_data.get('public')
            
            try: 
               tournire.save()
               return redirect('base:show_tournaments')
            except:
               return redirect('base:show_tournaments')
                     
      context = {
         'page_type': page_type,
         
         'tournire': tournire,
         'tournament_form': form,
      }
      return render(request, 'base/tournaments/panel/tournament_panel.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
   
@login_required(login_url='base:login')
def tournamets_admin_delete(request, slug):
   page_type = 'tournamets_admin_delete'
   
   if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь' or request.user.is_superuser ):
      tournire = get_object_or_404(Tournament, slug=slug)
      
      if request.method == 'POST': 
         weight_categories = WeightCategory.objects.filter(tournament=tournire)
         
         if (weight_categories.count() > 0):
            for weight_category in weight_categories:
               weight_category.delete()      
         
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
   
@login_required(login_url='base:login')
def athletes_admin_category(request, slug, year, gender):
   page_type = 'athletes_admin_category'
   
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      tournire = get_object_or_404(Tournament, slug=slug)
      weight_category = WeightCategory.objects.filter(tournament=tournire, year=year, gender=gender).first()  
      
      if request.method == 'POST':
         weight_id = request.POST.get('weight')
         participant_id = request.POST.get('participant')
         
         weight = Weight.objects.get(id=weight_id)
         weight.participants.remove(participant_id)
         weight.save()
         return redirect( 'base:athletes_admin_category',  tournire.slug, weight_category.year, weight_category.gender)
      
      context = {
         'page_type': page_type,
         
         'category': weight_category,
         'tournire': tournire,
      }
      return render(request, 'base/tournaments/panel/tournament_panel.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
   
@login_required(login_url='base:login')
def toss_admin_category(request, slug, category_slug):
   page_type = 'toss_admin_category'
   weight_category = get_object_or_404(WeightCategory, slug=category_slug)
   
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      tournire = get_object_or_404(Tournament, slug=slug)
      
      context = {
         'page_type': page_type,
         
         'category':weight_category,
         'tournire': tournire,
      }
      return render(request, 'base/tournaments/panel/tournament_panel.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')