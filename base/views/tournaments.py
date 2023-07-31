from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404

from ..models import Tournament, Logos, WeightCategory, Sponsors, Weight ,Participant
from ..forms import TournamentForm, WeightCategoryForm
from ..utils import slug_generator, checking_slug, generate_slug
from ..services import get_tournaments, get_all_weight_category, get_user_profile
from ..filters import TournamentFilter


def show_tournaments(request):
   tournaments = get_tournaments()
   
   filter = TournamentFilter(request.GET, queryset=tournaments)
   tournaments = filter.qs
   
   context = {
      'filter': filter,
      'tournaments': tournaments,     
   }
   return render(request, 'base/tournaments/show_tournaments.html', context)
   
def tournamet_show(request, slug):
   tournament = get_object_or_404(Tournament, slug=slug)
   person_count = 0

   context = {
      'tournament': tournament,
   }
   return render(request, 'base/tournaments/show_tournament.html', context)

def show_tournament_category(request, slug, pk):
   tournament = get_object_or_404(Tournament, slug=slug)
   category = get_object_or_404(WeightCategory, id=pk)
   weights = category.weight.all()
   
   context = {
      'tournament': tournament,
      
      'category': category,
      'weights': weights
   }
   return render(request, 'base/tournaments/show_tournament_category.html', context)

@csrf_exempt
@login_required(login_url= 'base:login')
def create_tournamets(request):
   page_type = 'create_tournament__part__one'
   
   if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь' or request.user.is_superuser):
      form = TournamentForm()
                     
      if request.method == 'POST':
         form = TournamentForm(request.POST, request.FILES)
         
         if form.is_valid():
            slug = checking_slug(slug_generator(form.cleaned_data.get('title_en')))
            
            try:
               tournire = Tournament.objects.populate(True).create(
                  user = request.user,
                  
                  title = form.cleaned_data.get('title_en'),
                  title_en = form.cleaned_data.get('title_en'),
                  title_ru = form.cleaned_data.get('title_ru'),
                  title_kk = form.cleaned_data.get('title_kk'),
                  
                  slug = slug,
                  logo = form.cleaned_data.get('logo'),
                  
                  about = form.cleaned_data.get('about_en'),
                  about_en = form.cleaned_data.get('about_en'),
                  about_ru = form.cleaned_data.get('about_ru'),
                  about_kk = form.cleaned_data.get('about_kk'),
                  
                  rang = form.cleaned_data.get('rang'),
                  
                  startData = form.cleaned_data.get('startData'),
                  finishData = form.cleaned_data.get('finishData'),
                  startTime = form.cleaned_data.get('startTime'),
                  
                  credit = form.cleaned_data.get('credit'),
                  tatamis_count = form.cleaned_data.get('tatamis_count'),

                  place = form.cleaned_data.get('place_en'),
                  place_en = form.cleaned_data.get('place_en'),
                  place_ru = form.cleaned_data.get('place_ru'),
                  place_kk = form.cleaned_data.get('place_kk'),
                  
                  chiefJustice = form.cleaned_data.get('chiefJustice_en'),
                  chiefJustice_en = form.cleaned_data.get('chiefJustice_en'),
                  chiefJustice_ru = form.cleaned_data.get('chiefJustice_ru'),
                  chiefJustice_kk = form.cleaned_data.get('chiefJustice_kk'),
                  
                  chiefSecretary = form.cleaned_data.get('chiefSecretary_en'),
                  chiefSecretary_en = form.cleaned_data.get('chiefSecretary_en'),
                  chiefSecretary_ru = form.cleaned_data.get('chiefSecretary_ru'),
                  chiefSecretary_kk = form.cleaned_data.get('chiefSecretary_kk'),
                  
                  status = form.cleaned_data.get('status'),
                  public = form.cleaned_data.get('public'),
               )
               
               return redirect('base:create_tournamets__images', slug)
            except:
               return redirect('base:create_tournamets__images', slug)
   
      context = {
         'form': form,
         'page_type': page_type
      }
      return render(request, 'base/tournaments/create_tournament.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
   
@csrf_exempt
@login_required(login_url= 'base:login')
def create_tournamets__images(request, slug):
   page_type = 'create_tournament__part__two'   
   
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      tournire = get_object_or_404(Tournament, slug=slug)
      
      if request.method == 'POST':
         logotips = request.FILES.getlist('files')
         sponsors_logotips = request.FILES.getlist('sponsors-logotips')
         
          # Add Logotips and Photos
         try:
            if (len(logotips) > 0):
               for logo in logotips:
                  new_file = Logos(image = logo)
                  
                  new_file.save()  
                  tournire.logos.add(new_file)
               
            # Add Sponsor Emblems
            if (len(sponsors_logotips) > 0):
               for logo in sponsors_logotips:
                  new_file = Sponsors(image = logo)
                  
                  new_file.save()
                  tournire.sponsors.add(new_file)
                  
            tournire.save()   
            return redirect('base:weight_categories', tournire.slug)
         except:
            return redirect('base:create_tournamets__images', slug)
   
      context = {
         'page_type': page_type,
         
         'tournire': tournire,
      }
      return render(request, 'base/tournaments/create_tournament.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')

# Weight Category
@login_required(login_url='base:login')
def weight_categories(request, slug):
   # get data and form
   tournament = Tournament.objects.get(slug=slug)
   weight_categories = WeightCategory.objects.filter(tournament=tournament)
   form = WeightCategoryForm()
   
   # get data from form
   if request.method == 'POST':
      form = WeightCategoryForm(request.POST)
      
      # validation checking
      if form.is_valid():
         category = form.save(commit=False)
         category.tournament = tournament
         category.save()
         
         return redirect('base:weight_category_weight', tournament.slug,category.id)
         
   context = {
      'weight_categories': weight_categories,
      'form': form,
      'tournament': tournament
   }
   return render(request, 'base/tournaments/weight_categories.html', context)
      
@login_required(login_url='base:login')
def weight_category_weight(request, slug, id):
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      tournament = Tournament.objects.get(slug=slug)
      weight_category = WeightCategory.objects.get(id=id)
      
      if request.method == 'POST':
         weight = request.POST.get('weight')
         
         if weight is not None and len(weight) > 1 and len(weight) < 3:
            weight_type = Weight.objects.create(
               name=weight
            )
            
            weight_type.save()

            weight_category.weight.add(weight_type.id)
            weight_category.save()
            return redirect('base:weight_category_weight',tournament.slug, weight_category.id)
         else:
            messages.error(request, 'Error creating weight category')
            
         # return redirect('base:weight_categories')
      
      context = {
         'tournament': tournament,
         'weight_category': weight_category,
      }
      return render(request, 'base/tournaments/weight_add.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')

@login_required(login_url='base:login')
def weight_category_weight_delete(request,slug, id, weight_id):
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      tournament = Tournament.objects.get(slug=slug)
      weight_category = WeightCategory.objects.get(id=id)
      weight = Weight.objects.get(id=weight_id)
      
      if weight:
         weight.delete()
         
         messages.success(request,'Weight category deleted successfully')
         return redirect('base:weight_category_weight', tournament.slug, weight_category.id)
      else:
         messages.error(request,'Weight category not found')
         return redirect('base:weight_category_weight', tournament.slug, weight_category.id)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')

#Weight Categories Delete
@login_required(login_url='base:login')
def weight_categories_delete(request, slug, pk):
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      tournament = Tournament.objects.get(slug=slug)
      weight_category = get_object_or_404(WeightCategory, id=pk)
      
      # Delete weight category
      weight_category.delete()
      return redirect('base:weight_categories', tournament.slug)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')

@login_required(login_url='base:sign-in')
def registration_on_tournament(request, slug):
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
   
      page_type = 'registration'
      tournament = get_object_or_404(Tournament, slug=slug)
      weight_category = WeightCategory.objects.filter(tournament=tournament)
      
      participants = Participant.objects.filter(user=request.user)

      weight  = Weight.objects.all()
      
      if request.method == 'POST':
         athlete = request.POST.get('athlete', None)
         weight = request.POST.get('weight', None)
         
         if weight:
            weigh = Weight.objects.get(id=weight)
            weigh.participants.add(athlete)
            
            return redirect('base:registration_on_tournament', slug)
         else:
            messages.error(request, 'Choose your own weight category')
      
      context = { 
         'page_type': page_type,
         
         'tournament': tournament,
         'participants': participants,
         
         'weight': weight,
         'weight_category': weight_category
      }
      return render(request, 'base/tournaments/athlete_registration.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')

@login_required(login_url='base:sign-in')
def list_of_registered_on_tournament(request, slug):
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
   
      page_type = 'list_of_registered'
      tournament = get_object_or_404(Tournament, slug=slug)
      
      participants = Participant.objects.filter(user=request.user) 
      
      if request.method == 'POST':
         athlete = request.POST.get('athlete', None)
         weight = request.POST.get('weight', None)
         
         weight_category = Weight.objects.get(id=weight) 
         weight_category.participants.remove(athlete)   
         return redirect('base:list_of_registered_on_tournament', slug)
         
      
      context = {
         'page_type': page_type,
         
         'tournament': tournament,
         'athletes': participants,
      }
      return render(request, 'base/tournaments/athlete_registration.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
   
@login_required(login_url='base:sign-in')
def tournament_toss(request, slug):
   if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
      tournament = get_object_or_404(Tournament, slug=slug)
            
      context = {
         'tournament': tournament,
      }
      return render(request, 'base/tournaments/toss.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')