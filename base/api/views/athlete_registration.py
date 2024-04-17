from django.views.decorators.csrf import csrf_exempt
from ..utils.data_utils import takeYearFromDate
from ..utils.response_utils import create_response
from ...models import Tournament, WeightCategory, Participant, Weight
from django.http import JsonResponse

from base.utils.check_user_permissions_util import check_user_permissions
from ...services.participant_services import filter_participants_by_user, participant_exists
from ...services.tournament_services import get_tournament_by_id
from ...services.weight_category_services import filter_weight_categories_by_tournament
from ...services.weight_services import get_weight_by_id, weight_exists


@csrf_exempt
def show_weight_categories(request, id: int):
    """
        Показывает список категорий весов для выбора и
                добавляет определенного человека в весовую категорию
    """
    # Берем турнир
    tournament = get_tournament_by_id(id)
    # Берем весовые категории турнира
    weight_categories = filter_weight_categories_by_tournament(tournament)
    # Берем участников текущего пользователя
    participants = filter_participants_by_user(request.user)

    if request.method == 'GET':
        """
            Показывает список категорий весов для выбора
        """
        athletes = []

        # Прокручиваем участников текущего пользователя
        for participant in participants:
            user, weights_for_registration = {}, []
            # Берем только год из даты
            only_year = takeYearFromDate(participant.year)

            # Прокручиваем весовые категории
            for weight_category in weight_categories:
                user_in_weight_category_count, year_list = 0, [int(i) for i in weight_category.year.split('-')]

                # Если в year_list указано 2 даты,
                #   то создаем список, содержащий последовательные года от начального до конечного, включительно
                if len(year_list) == 2:
                    year_list = [year_list[1] - i for i in range(year_list[1] - year_list[0] + 1)]

                # Проверяем, если год пользователя,
                #                       находится в списке годов, что указано в списке категорий
                if only_year in year_list:
                    # Прокручиваем все веса в весовой категории
                    for w in weight_category.weight.all():
                        # Если вес пользователя есть в весах у весовой категории,
                        #                               то меняем значение состояния пользователя
                        if participant in w.participants.all():
                            user_in_weight_category_count += 1

                    # Если значение состояния пользователя равно 0
                    if user_in_weight_category_count == 0:
                        # Прокручиваем все веса в весовой категории
                        for w in weight_category.weight.all():
                            # Проверяем, что пол пользователя равен полу указанному в категории
                            if participant.gender == weight_category.gender:
                                # Добавляем вес в специальный список
                                weights_for_registration.append({
                                    'id': w.id,
                                    'name': w.name,
                                })

            # Если значение состояния пользователя больше 0
            if len(weights_for_registration) > 0:
                # Заполняем словарь пользователя
                user['id'] = participant.id
                user['fio'] = f'{participant.lastName} {participant.firstName} {participant.thirdName}'
                user['discharge'], user['gender'] = participant.discharge,  participant.gender
                user['year'], user['weights'] = only_year, weights_for_registration

                # Добавляем пользователя в список спортсменов
                athletes.append(user)

        return JsonResponse({
            'status': 'success',
            'athletes': athletes,
        }, status=200)

    if request.method == 'POST':
        """
            Добавляет определенного человека в вес в весовой категории
        """
        if check_user_permissions(request.user):
            # Берем ID спортсмена и ID веса, куда надо его добавить
            athlete = request.POST.get('athlete', None)
            weight = request.POST.get('weight', None)

            # Убеждаемся во взятии ID веса и ID спортсмена
            if weight and athlete:
                # Проверяем, что спортсмен и вес по данным ID существуют
                if participant_exists(athlete) and weight_exists(weight):
                    # Берем вес по ID
                    weigh = get_weight_by_id(weight)
                    # Добавляем в вес ID спортсмена
                    weigh.participants.add(athlete)

                    return create_response('Athlete added successfully', 200)
                return create_response('Invalid weight and athlete', 400)
            return create_response('Invalid weight', 400)
        return create_response('You don\'t have any permissions', 401)
    return create_response('Method not allowed', 402)


@csrf_exempt
def list_of_registered_on_tournament(request, id: int):
    """
        Показывает список категорий весов для выбора и
                добавляет определенного человека в весовую категорию
    """
    # Берем турнир
    tournament = get_tournament_by_id(id)
    # Берем весовые категории турнира
    weight_categories = filter_weight_categories_by_tournament(tournament)
    # Берем участников текущего пользователя
    participants = filter_participants_by_user(request.user)
        
    if request.method == 'GET':
        """
           Показывает список категорий весов для выбора
        """
        athletes = []

        # Прокручиваем участников текущего пользователя
        for participant in participants:
            user, weights_for_registration = {}, []

            # Берем только год из даты
            only_year = takeYearFromDate(participant.year)

            # Прокручиваем весовые категории
            for weight_category in weight_categories:
                user_in_weight_category_count, year_list = 0, [int(i) for i in weight_category.year.split('-')]

                # Если в year_list указано 2 даты,
                #   то создаем список, содержащий последовательные года от начального до конечного, включительно
                if len(year_list) == 2:
                    year_list = [year_list[1] - i for i in range(year_list[1] - year_list[0] + 1) ]

                # Проверяем, если год пользователя,
                #                       находится в списке годов, что указано в списке категорий
                if only_year in year_list:
                    # Прокручиваем все веса в весовой категории
                    for w in weight_category.weight.all():
                        # Если вес пользователь есть в весах у весовой категории,
                        #                               то меняем значение состояния пользователя
                        if participant in w.participants.all():
                            user_in_weight_category_count += 1

                            # Добавляем пользователя в список
                            weights_for_registration.append({
                                'id': w.id,
                                'name': w.name,
                            })

            # Если значение состояния пользователя больше 0
            if len(weights_for_registration) > 0:
                # Заполняем словарь пользователя
                user['id'] = participant.id
                user['fio'] = f'{participant.lastName} {participant.firstName} {participant.thirdName}'
                user['discharge'], user['gender'] = participant.discharge, participant.gender
                user['year'], user['weights'] = only_year, weights_for_registration

                # Добавляем пользователя в список спортсменов
                athletes.append(user)

        return JsonResponse({
            'status': 'success',
            'athletes': athletes,
        }, status=200)

    if request.method == 'POST':
        """
            Удаляем определенного человека из веса в весовой категории
        """
        if check_user_permissions(request.user):
            # Берем ID спортсмена и ID веса, куда надо его добавить
            athlete = request.POST.get('athlete', None)
            weight = request.POST.get('weight', None)

            # Убеждаемся во взятии ID веса и ID спортсмена
            if weight and athlete:
                # Проверяем, что спортсмен и вес по данным ID существуют
                if participant_exists(athlete) and weight_exists(weight):
                    # Берем вес по ID
                    weight_category = get_weight_by_id(weight)
                    # Удаляем ID спортсмена из веса
                    weight_category.participants.remove(athlete)

                    return create_response('Athlete removed successfully', 200)
                return create_response('Invalid weight and athlete', 400)
            return create_response('Invalid weight', 400)
        return create_response('You don\'t have any permissions', 401)
    return create_response('Method not allowed', 402)