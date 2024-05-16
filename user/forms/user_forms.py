from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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