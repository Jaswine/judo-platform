from modeltranslation.translator import register, TranslationOptions
from .models import Profile, Tournament

@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
   fields = ('fullName', )
   
@register(Tournament)
class TournamentTranslationOptions(TranslationOptions):
   fields = ('title', 'about', 'place', 'chiefJustice', 'chiefSecretary' )