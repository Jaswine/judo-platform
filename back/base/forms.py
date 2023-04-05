from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

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
