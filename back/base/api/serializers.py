from rest_framework.serializers import ModelSerializer
from ..models import Logos, Sponsors, Tournament


class TournamentSerializer(ModelSerializer):
   class Meta:
      model = Tournament()
      fields = '__all__'

class LogosSerializer(ModelSerializer):
   class Meta:
      model = Logos
      fields = '__all__'
      
class SponsorsSerializer(ModelSerializer):
   class Meta:
      model = Sponsors
      fields = '__all__'