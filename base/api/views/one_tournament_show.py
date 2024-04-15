from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from base.api.utils.response_utils import create_response
from base.models import Tournament, Weight, WeightCategory
from base.services.tournament_services import get_tournament_by_id
from base.services.weight_category_services import filter_weight_categories_by_tournament


def show_weight_categories_and_weights_and_sorting(request, id: int):
    """
        Выводит список категорий весов и сами веса
    """
    # Берем турнир
    tournament = get_tournament_by_id(id=id)
    # Берем весовые категории турнира
    weight_categories = filter_weight_categories_by_tournament(tournament)

    if request.method == 'GET':
        weights = []

        # Прокручиваем весовые категории
        for weight_category in weight_categories:
            weight_cat, weights_cat = dict(), []

            # Заполняем весовую категорию
            weight_cat['id'] = weight_category.id
            weight_cat['year'] = weight_category.year
            weight_cat['gender'] = weight_category.gender

            for w in weight_category.weight.all():
                # Создаем пустой словарь веса
                weight = dict()
                # Заполняем словарь веса
                weight['name'], weight['sorting'] = w.name, w.sorting
                # Добавляем в список весовых категорий
                weights_cat.append(weight)

            # Добавляем список веса в весовую категорию
            weight_cat['weights'] = weights_cat

            # Добавляем весовую категорию в список весов
            weights.append(weight_cat)

        return JsonResponse({
            "status": "success",
            "weights": weights
        }, status=200)

    return create_response('Method not allowed', 402)