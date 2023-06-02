from rest_framework.serializers import ModelSerializer
from ..models import (Tournament, 
                      WeightCategory, 
                      Weight, 
                      Participant)

class TournamentSerializer(ModelSerializer):
   class Meta:
      model = Tournament
      fields = '__all__'
      
class ParticipantSerializer(ModelSerializer):
   class Meta:
      model = Participant
      fields = '__all__'
      
class WeightSerializer(ModelSerializer):
   participants = ParticipantSerializer(many=True)
   class Meta:
      model = Weight
      fields = ['id', 'name', 'participants']
      
class WeightCategorySerializer(ModelSerializer):
   # tournament = TournamentSerializer(many=False)
   # weight = WeightSerializer(many=True)
   
   class Meta:
      model = WeightCategory
      fields = ['id', 'year', 'gender']