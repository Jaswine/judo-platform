from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm


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

# class UpdateProfilePasswordForm(PasswordChangeForm):
#    old_password = forms.CharField(
#       label="Current password",
#       strip=False,
#       widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True})
#    )
   
#    new_password1 = forms.CharField(
#       label="New password",
#       strip=False,
#       widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#       help_text = "Your password must contain at least 8 characters."
#    )
   
#    new_password2 = forms.CharField(
#       label="Confirm new password",
#       strip=False,
#       widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#    )
   
#    class Meta:
#       model = User
#       fields = ['old_password', 'new_password1', 'new_password2']