from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from base.models import Tournament, Weight, WeightCategory

def show_weight_categories_and_weights_and_sorting(request, id):
    tournament = Tournament.objects.get(id=id)
    weight_categories = WeightCategory.objects.filter(tournament=tournament)

    if request.method == 'GET':
        weights = []

        for weight_category in weight_categories:
            weight_cat = dict()
            weights_cat = []

            weight_cat['id'] = weight_category.id
            weight_cat['year'] = weight_category.year
            weight_cat['gender'] = weight_category.gender

            for w in weight_category.weight.all():
                weight = dict()

                weight['name'] = w.name
                weight['sorting'] = w.sorting

                weights_cat.append(weight)

            weight_cat['weights'] = weights_cat
            weights.append(weight_cat)

        return JsonResponse({
            "status": "success",
            "weights": weights
        }, status=200)
