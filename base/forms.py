from django.forms import ModelForm, forms
from django.contrib.auth.models import User
from .models import Profile, Tournament, Logos, WeightCategory, Participant
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import FileField, ClearableFileInput


# create user
class CreateUserForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['username', 'email', 'password1','password2']
      
# update user
class UpdateUserForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email']

class UpdateProfileForm(ModelForm):
   class Meta:
      model = Profile
      fields = ['fullName', 'phone', 'image', 'organization', 'city', 'region']   

# Tournament
class TournamentForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['title_en', 'title_ru', 'title_kk', 
                  'logo', 
                  'about_en', 'about_ru', 'about_kk', 
                  'rang', 
                  'place_en', 'place_ru',  'place_kk',  # Make sure to add the fields for all languages
                  'startData', 'finishData', 'startTime', 'credit', 'tatamis_count', 
                  'chiefJustice_en', 'chiefJustice_ru', 'chiefJustice_kk', 
                  'chiefSecretary_en', 'chiefSecretary_ru', 'chiefSecretary_kk', 
                  'status', 'public']
        labels = {
            'title_en': 'Title in English',
            'title_ru': 'Title in Russian',
            'title_kk': 'Title in Kazakh',
            'about_en': 'About in English',
            'about_ru': 'About in Russian',
            'about_kk': 'About in Kazakh',
            'place_en': 'Location in English',
            'place_ru': 'Location in Russian',
            'place_kk': 'Location in Kazakh',
            'rang': 'Rang', 
            'logo': 'Logo',   
            'startData': 'Start Datе',
            'finishData': 'Finish Datе',  
            'startTime': 'Start Time',  
            'credit': 'Credit',  
            'tatamis_count': 'Tatamis Count', 
            'chiefJustice_en': 'English Chief Justice',
            'chiefJustice_ru': 'Russian Chief Justice',
            'chiefJustice_kk': 'Kazakh Chief Justice',
            'chiefSecretary_en': 'English Chief Secretary',
            'chiefSecretary_ru': 'Russian Chief Secretary', 
            'chiefSecretary_kk': 'Kazakh Chief Secretary', 
            'status': 'Status',  
            'public': 'Public',  
        }
      
class WeightCategoryForm(ModelForm):
   class Meta:
      model = WeightCategory
      fields = [
               # 'weight', 
               'year', 
               'gender',
            ]
      
class SortingTournamentForm(ModelForm):
   class Meta:
      model = Tournament
      fields = ['rang']
      
# Participant
class ParticipantForm(ModelForm):
   class Meta:
      model = Participant
      fields = ['firstName', 'lastName', 'thirdName', 'year', 'discharge', 'gender']