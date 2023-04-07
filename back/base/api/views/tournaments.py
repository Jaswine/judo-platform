from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import TournamentSerializer, LogosSerializer, SponsorsSerializer

from ...models import Tournament, Logos, Sponsors

@api_view(['POST'])
def logos_view(request):
   if request.method == 'POST':
      logo = Logos.objects.create(
         image = request.data.get('image')
      )
      
      return Response(LogosSerializer(logo, many=False).data)
   
@api_view(['GET', 'DELETE'])
def one_logo_view(request, id):
   logo = Logos.objects.get(id=id)
   
   if logo:
      if request.method == 'GET':
         return Response(LogosSerializer(logo, many=False).data)
      
      elif request.method == 'DELETE':
         sponsors.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
      
   else:
      return Response(status=status.HTTP_404_NOT_FOUND)