from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Tournament

from django.db.models.signals import post_save
from modeltranslation.utils import get_language
from django.utils.translation import activate, deactivate


@receiver(post_save, sender=User)
def create_profile_model(sender,instance, created, **kwargs):
   if created:
      Profile.objects.create(
         user = instance,
         # userType = 'Админ'
      )
      
@receiver(post_save, sender=Tournament)
def translate_model_content(sender, instance, **kwargs):
    current_language = get_language()
    activate('en')  
    instance.title = instance.title
    instance.about = instance.about
    
    instance.rang = instance.rang
    instance.place = instance.place 
    instance.credit = instance.credit
    instance.status = instance.status
     
    deactivate()  

    instance.save()