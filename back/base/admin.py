from django.contrib import admin
from .models import  Profile,Logos, WeightCategory, Sponsors,Participant, Tournament

admin.site.register(Profile)
admin.site.register(Logos)
admin.site.register(Sponsors)
admin.site.register(WeightCategory)
admin.site.register(Tournament)
admin.site.register(Participant)