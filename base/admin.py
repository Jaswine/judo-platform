from django import forms
from django.contrib import admin
from .models import  Profile,Logos, WeightCategory, Sponsors,Participant, Tournament, Weight, Participant
from modeltranslation.admin import  TranslationAdmin
      
class TournamentAdminForm(forms.ModelForm):
   class Meta:
      model = Tournament
      fields = '__all__'

      
class WeightAdmin(admin.ModelAdmin):
   # enter participants count from
   def participants_count(self, obj):
      return obj.participants.count()
   
   participants_count.short_description =  'Count of many to many field'
   
   list_display = ('name', 'participants_count', )

admin.site.register(Profile)
admin.site.register(Logos)
admin.site.register(Sponsors)
admin.site.register(Weight, WeightAdmin)
admin.site.register(WeightCategory)
admin.site.register(Participant)

@admin.register(Tournament)
class TournamentAdmin(TranslationAdmin):
   form = TournamentAdminForm
   