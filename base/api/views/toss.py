from django.http import JsonResponse
from base.api.utils.response_utils import create_response
from base.models import Tournament, Weight
from base.services.tournament_services import get_tournament_by_id
from base.services.weight_category_services import filter_weight_categories_by_tournament
from base.services.weight_services import get_weight_by_id
from base.utils.check_user_permissions_util import check_user_permissions


def show_weight_categories_and_weights(request, id: int):
    """
        Выводит список категорий весов, сами веса и спортсменов под ними
    """
    # Берем турнир
    tournament = get_tournament_by_id(id)
    # Берем весовые категории турнира
    weight_categories = filter_weight_categories_by_tournament(tournament)

    if request.method == 'GET':
        weights = []

        # Прокручиваем весовые категории
        for weight_category in weight_categories:
            # Создаем пустой словарь весовой категории
            #                           и список весов в весовой категории
            weight_cat, weights_cat = dict(), []

            # Заполняем словарь весовой категории
            weight_cat['id'] = weight_category.id
            weight_cat['year'] = weight_category.year
            weight_cat['gender'] = weight_category.gender

            # Прокручиваем список весов в весовой категории
            for w in weight_category.weight.all():
                # Создаем пустой словарь веса и список спортсменов
                weight, athletes = dict(), []

                # Заполняем словарь веса
                weight['id'], weight['name'] = w.id,  w.name
                weight['participants_count'] = w.participants.count()
                weight['sorting'] = w.sorting

                # Прокручиваем список спортсменов в весе весовой категории
                for participant in w.participants.all():
                    # Создаем пустой словарь спортсмена
                    athlete = dict()

                    # Заполняем словарь спортсмена
                    athlete['id'] = participant.id
                    athlete['fio'] = f'{participant.firstName} {participant.lastName} {participant.thirdName}'
                    athlete['discharge'], athlete['year'] = participant.discharge, participant.year

                    # Добавляем спортсмена в список спортсменов
                    athletes.append(athlete)

                # Добавляем к весу список спортсменов
                weight['athletes'] = athletes

                # Добавляем вес в список весов в весовой категории
                weights_cat.append(weight)

            # Добавляем список с весами к весовой категории
            weight_cat['weights'] = weights_cat

            # Добавляем весовые категории в список весовых категорий
            weights.append(weight_cat)

        return JsonResponse({
            "status": "success",
            "weights": weights
        }, status=200)
    return create_response('Method not allowed', 402)


def show_weight_categories_and_weights_update(request, tournament_id: int, weight_id: int):
    """
        Добавляем сортировку пользователей в весе весовой категории
    """
    if check_user_permissions(request.user):
        # Берем турнир
        tournament = get_tournament_by_id(tournament_id)
        # Берем вес по id
        weight = get_weight_by_id(weight_id)

        if request.method == 'POST':
            # Берем данные
            data = request.POST.get('data')

            # Проверяем данные на существование
            if data is None:
                return create_response("Invalid data", 400)

            if data == weight.sorting:
                return create_response("Data is sorted", 204)

            # Сохраняем данные
            weight.sorting = data
            weight.save()

            return create_response("Weight updated successfully", 200)
        return create_response("Method not allowed", 402)
    return create_response('You don\'t have any permissions', 403)
