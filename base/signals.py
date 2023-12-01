from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Tournament

from django.db.models.signals import post_save
from modeltranslation.utils import get_language
from django.utils.translation import activate, deactivate


@receiver(post_save, sender=User)
def create_profile_model(sender, instance, created, **kwargs):
   if created:
      Profile.objects.create(
         user = instance,
         # userType = 'Админ'
      )