from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from ..serializers import (TournamentSerializer,
                           WeightCategorySerializer,
                           WeightSerializer,
                           ParticipantSerializer)
from ...models import Tournament, WeightCategory, Weight
 
@api_view(['GET'])
def weight_category(request, slug):
   tournament = Tournament.objects.get(slug=slug)
   categories = WeightCategory.objects.filter(tournament=tournament)
   
   return Response(WeightCategorySerializer(categories, many=True).data)

@api_view(['GET'])
def weight_category_weights(request, slug, category_id):
   tournament = Tournament.objects.get(slug=slug)
   category = WeightCategory.objects.get(id=category_id)
   weights  = category.weight.all()
   
   return Response(WeightSerializer(weights, many=True).data)
   
@api_view(['GET'])
def show_participants(request, slug, category_id, weight_id):
   tournament = Tournament.objects.get(slug=slug)
   category = WeightCategory.objects.get(id=category_id)
   weight  = Weight.objects.get(id=weight_id)
   participants = weight.participants.all()
   
   return Response(ParticipantSerializer(participants, many=True).data)