from modeltranslation.translator import register, TranslationOptions
from .models import Profile, Participant, WeightCategory, Tournament

@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
   fields = ('fullName', 'userType', )
   
@register(Participant)
class ParticipantTranslationOptions(TranslationOptions):
   fields = ('fullName', 'discharge', 'comand', 'country', 'city', 'trainer')
   
@register(WeightCategory)
class WeightCategoryTranslationOptions(TranslationOptions):
   fields = ('gender', )
   
@register(Tournament)
class TournamentTranslationOptions(TranslationOptions):
   fields = ('title', 'about','rang', 'place', 'credit', 'chiefJustice', 'chiefSecretary' )