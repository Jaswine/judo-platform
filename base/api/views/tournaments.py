from ...models import Tournament
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q

def tournament_list(request):
    if request.method == 'GET':
        data = []
        tournament_list = Tournament.objects.filter(public=True).order_by('-updated')

        search = request.GET.get('search')
        startDate = request.GET.get('startDate')
        endDate = request.GET.get('endDate') 
        print("\n\nSEARCH", search, startDate, endDate)

        if startDate:
            tournament_list = tournament_list.filter(startData=startDate)

        if endDate:
            tournament_list = tournament_list.filter(finishData=endDate)
        
        if search:
            tournament_list = Tournament.objects.filter(public=True).filter(Q(title__icontains=search) | Q(rang__icontains=search) | Q(place__icontains=search) | Q(startData__icontains=search) | Q(finishData__icontains=search) | Q(credit__icontains=search) ).order_by('-updated')

        for tournament in tournament_list:
            element = {}

            element['id'] = tournament.id
            element['slug'] = tournament.slug
            element['title'] = tournament.title[0:50]
            element['logo'] =  f'/static/media/{tournament.logo}'

            element['place'] = tournament.place
            element['rang'] = tournament.rang
            element['status'] = tournament.status

            element['startDate'] = tournament.startData
            element['endDate'] = tournament.finishData

            categories = []

            for tournament_category in tournament.weightcategory_set.all():
                category = {
                    "gender": tournament_category.gender,
                    "year": tournament_category.year,
                }

                categories.append(category)

            user = {
                'username': '',
                'type': '',
                'status': '',
            }

            if request.user.is_authenticated:
                user['username'] = request.user.username
                user['type'] = request.user.profile.userType
                user['status'] = request.user.is_superuser

            element['categories'] = categories
            element['user'] = user
            data.append(element)

        return JsonResponse({
            'size': tournament_list.count(),
            'tournament_list': data,
        }, status=200)