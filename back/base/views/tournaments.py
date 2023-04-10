from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.forms import modelformset_factory

from ..models import Tournament, Logos
from ..forms import TournamentForm
from ..utils import slug_generator, checking_slug
from ..services import get_tournaments


def show_tournaments(request):
   tournaments = get_tournaments()
   
   context = {
      'tournaments': tournaments,
   }
   return render(request, 'base/tournaments/show_tournaments.html', context)

@csrf_exempt
@login_required(login_url= 'base:login')
def create_tournamets(request):
   if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь'):
      form = TournamentForm()
      logos = Logos.objects.all()
      
      logo_massive = []
      sponsor_logo_massive = []
                     
      if request.method == 'POST':
         logotips = request.FILES.getlist('files')
         sponsors_logotips = request.FILES.getlist('sponsors-logotips')
         
         print('logotips', logotips)
      
         for logo in logotips:
            new_file = Logos(
               image = logo
            )
            
            new_file.save()
            logo_massive.append(new_file.id)
            
         for logo in sponsors_logotips:
            new_file = Logos(
               image = logo
            )
            
            new_file.save()
            logo_massive.append(new_file.id)
            
      
         form = TournamentForm(request.POST)
         
         if form.is_valid():
            slug = checking_slug(slug_generator(form.cleaned_data.get('title')))
         
            article = form.save(commit=False)
            article.user = request.user 
            article.slug = slug
            article.logos.set(logo_massive)
            article.save()
            
            return redirect('base:tournaments')
   
      context = {
         'form': form,
         'logos': logos
      }
      return render(request, 'base/tournaments/create_tournament.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
