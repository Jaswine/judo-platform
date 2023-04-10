from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile, Tournament, Logos
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
      fields = ['fullName', 'phone', 'image']   

# Tournament
class TournamentForm(ModelForm):
   class Meta:
      model = Tournament
      fields = ['title', 'about', 'rang', 'place', 'startData', 'finishData', 'startTime', 'credit', 'tatamis_count', 'weight_categories', 'chiefJustice', 'chiefSecretary']