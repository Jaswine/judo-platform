from base.api.utils.response_utils import create_response
from base.models import Tournament, WeightCategory
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q

from base.services.tournament_services import get_public_tournaments


def tournament_list(request):
    """
        Выводит список турниров
    """
    if request.method == 'GET':
        # Создаем пустой словарь турниров и берем все турниры
        data, tournament_list = [], get_public_tournaments()

        # Берем данные поиска и фильтрации
        search = request.GET.get('search')
        startDate, endDate = request.GET.get('startDate'), request.GET.get('endDate')

        # Фильтруем
        if startDate:
            tournament_list = tournament_list.filter(startData=startDate)
        if endDate:
            tournament_list = tournament_list.filter(finishData=endDate)
        if search:
            tournament_list = Tournament.objects.filter(public=True).filter(Q(title__icontains=search)
                                                                        | Q(rang__icontains=search)
                                                                        | Q(place__icontains=search)
                                                                        | Q(startData__icontains=search)
                                                                        | Q(finishData__icontains=search)
                                                                        | Q(credit__icontains=search)).order_by('-updated')

        # Прокручиваем все турниры
        for tournament in tournament_list:
            peopleCount, element = 0, {}

            # Заполняем словарь турнира
            element['id'], element['slug'] = tournament.id, tournament.slug
            element['title'] = tournament.title[0:50]
            element['logo'] = f'/static/media/{tournament.logo}'

            element['place'], element['rang'] = tournament.place, tournament.rang
            element['status'] = tournament.status

            element['startDate'],  element['endDate'] = tournament.startData, tournament.finishData

            categories = []

            # Прокручиваем список весовых категорий
            for tournament_category in tournament.weightcategory_set.filter(tournament=tournament):
                category = {
                    "gender": tournament_category.gender,
                    "year": tournament_category.year,
                }

                # Прокручиваем список весов в весовой категории
                for weight in tournament_category.weight.all():
                    peopleCount += weight.participants.count()

                # Добавляем категорию к списку категорий
                categories.append(category)

            user = {
                'username': '',
                'type': '',
                'status': '',
            }
            
            element['peopleCount'] = peopleCount

            # Добавляем информацию о пользователе, если он аутентифицирован
            if request.user.is_authenticated:
                user['username'] = request.user.username
                user['type'] = request.user.profile.userType
                user['status'] = request.user.is_superuser

            # Добавляем категории
            element['categories'] = categories
            # Добавляем пользователя
            element['user'] = user

            # Добавляем турнир в список
            data.append(element)

        return JsonResponse({
            'size': tournament_list.count(),
            'tournament_list': data,
        }, status=200)
    return create_response('Method not allowed', 402)