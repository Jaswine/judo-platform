from django.forms import (ModelForm, 
                                          DateField, 
                                          CharField, 
                                          FileField, 
                                          DateInput, 
                                          TimeField, 
                                          TimeInput, 
                                          ClearableFileInput)
from django.contrib.auth.models import User
from .models import Profile, Tournament, Logos, WeightCategory, Participant
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


"""
   Форма для создания пользователя
"""
class CreateUserForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['username', 'email', 'password1','password2']
      
      
"""
   Форма для обновления главной информации пользователя
"""
class UpdateUserForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email']


"""
   Форма для обновления информации профиля пользователя
"""
class UpdateProfileForm(ModelForm):
   class Meta:
      model = Profile
      fields = ['fullName', 'phone', 'image', 'organization', 'city', 'region'] 

class DateInput(DateInput):
   input_type = 'date'  

class TimeInput(TimeInput):
   input_type = 'time'  

"""
   Форма для создания турнира
"""
class CreateTournamentForm(ModelForm):
   title_en = CharField(required=True)
   title_ru = CharField(required=True)
   title_kk = CharField(required=True)
   tatamis_count = CharField(required=True)
   
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
      
      
"""
   Форма для обновления главной информации турнира
"""
class UpdateTournamentMainInformationForm(ModelForm):
   title_en = CharField(required=True)
   title_ru = CharField(required=True)
   title_kk = CharField(required=True)
   tatamis_count = CharField(required=True)
   
   logo = FileField()
   
   # startData=  DateField(widget=DateInput())
   # finishData=  DateField(widget=DateInput())
   startTime = TimeField(widget=TimeInput())

   class Meta:
      model = Tournament
      fields = ['title_en', 'title_ru', 'title_kk', 
                        'logo', 
                        'about_en', 'about_ru', 'about_kk', 
                        'rang', 
                        'place_en', 'place_ru',  'place_kk',  
                        'startData', 'finishData', 'startTime',
                        'credit', 'tatamis_count', 
                        'chiefJustice_en', 'chiefJustice_ru', 'chiefJustice_kk', 
                        'chiefSecretary_en', 'chiefSecretary_ru', 'chiefSecretary_kk', 
                        'status', 'public']

      
"""
   Форма для обновления информации о организаторах турнира
"""
class UpdateTournamentOrganizatorsInformationForm(ModelForm):
   class Meta: 
      model = Tournament 
      fields = [
         'chiefJustice_en', 'chiefJustice_ru', 'chiefJustice_kk', 
         'chiefSecretary_en', 'chiefSecretary_ru', 'chiefSecretary_kk', 
      ]

"""
   Форма для создания/обновления весовых категорий
"""
class WeightCategoryForm(ModelForm):
   year = CharField(required=True)
   class Meta:
      model = WeightCategory
      fields = [
               'year', 
               'gender',
            ]
      
      
class DateParticipantInput(DateInput):
   input_type = 'date'  

"""
   Форма для создания/обновления спортсменов
"""
class ParticipantForm(ModelForm):
   firstName = CharField(required=True)
   lastName = CharField(required=True)
   year = DateField(widget=DateParticipantInput())
   
   class Meta:
      model = Participant
      fields = ['firstName', 'lastName', 'thirdName', 'year', 'discharge', 'gender']