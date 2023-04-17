import django_filters
from .models import Tournament
from django_filters import ChoiceFilter, CharFilter, ModelMultipleChoiceFilter


class TournamentFilter(django_filters.FilterSet):
   rang = ChoiceFilter(field_name = 'rang', choices = Tournament.RANGS)
   title = CharFilter(field_name = 'title', lookup_expr='icontains')
   
   startData = CharFilter(field_name ='startData', lookup_expr='icontains')
   finishData = CharFilter(field_name = 'finishData', lookup_expr='icontains')
   
   class Meta: 
      model = Tournament
      fields = ['rang', 'title', 'startData', 'finishData']