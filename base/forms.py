from django.forms import (ModelForm, 
                                          DateField, 
                                          SelectDateWidget, 
                                          CharField, 
                                          Select, 
                                          DateInput, 
                                          TimeField, 
                                          TimeInput)
from django.contrib.auth.models import User
from .models import Profile, Tournament, Logos, WeightCategory, Participant
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import FileField, ClearableFileInput
import datetime
from django.utils.translation import gettext_lazy as _

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

class DateInput(DateInput):
   input_type = 'date'  

class TimeInput(TimeInput):
   input_type = 'time'  

# Tournament
class TournamentForm(ModelForm):
   title_en = CharField(required=True)
   title_ru = CharField(required=True)
   title_kk = CharField(required=True)
   tatamis_count = CharField(required=True)
   # startData = DateField(widget=SelectDateWidget(years=range(datetime.date.today().year - 100, datetime.date.today().year + 1)))
   startData=  DateField(widget=DateInput())
   finishData=  DateField(widget=DateInput())
   startTime = TimeField(widget=TimeInput())

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
                        'chiefJustice_en', 'chiefJustice_ru', 'chiefJustice_kk', 
                        'chiefSecretary_en', 'chiefSecretary_ru', 'chiefSecretary_kk',
                        'status', 'public']
      
class WeightCategoryForm(ModelForm):
   year = CharField(required=True)
   gender = CharField(required=True)

   class Meta:
      model = WeightCategory
      fields = [
               'year', 
               'gender',
            ]
      
class SortingTournamentForm(ModelForm):
   class Meta:
      model = Tournament
      fields = ['rang']
      
class DateParticipantInput(DateInput):
   input_type = 'date'  

# Participant
class ParticipantForm(ModelForm):
   firstName = CharField(required=True)
   lastName = CharField(required=True)
   year = DateField(widget=DateParticipantInput())
   
   class Meta:
      model = Participant
      fields = ['firstName', 'lastName', 'thirdName', 'year', 'discharge', 'gender']