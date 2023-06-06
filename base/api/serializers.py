from rest_framework.serializers import ModelSerializer, SerializerMethodField
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
   participants_count = SerializerMethodField()
   
   class Meta:
      model = Weight
      fields = ['id', 'name', 'participants_count', 'participants']
   
   def get_participants_count(self, obj):
        return obj.participants.count()
      
class WeightCategorySerializer(ModelSerializer):
   # tournament = TournamentSerializer(many=False)
   # weight = WeightSerializer(many=True)
   
   class Meta:
      model = WeightCategory
      fields = ['id', 'year', 'gender']