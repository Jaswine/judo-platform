from django.forms import ModelForm, forms, DateField, TimeField, SelectDateWidget, CharField
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
   title_en = CharField(required=True)
   title_ru = CharField(required=True)
   title_kk = CharField(required=True)

   class Meta:
      model = Tournament
      fields = ['title_en', 'title_ru', 'title_kk', 
                        'logo', 
                        'about_en', 'about_ru', 'about_kk', 
                        'rang', 
                        'place_en', 'place_ru',  'place_kk',  
                        'startData', 'finishData', 'startTime', 'credit', 'tatamis_count', 
                        'chiefJustice_en', 'chiefJustice_ru', 'chiefJustice_kk', 
                        'chiefSecretary_en', 'chiefSecretary_ru', 'chiefSecretary_kk', 
                        'status', 'public']
      
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