from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from base.models import Tournament, Weight, WeightCategory

def show_weight_categories_and_weights(request, id):
    if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь' or request.user.is_superuser):
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
                    athletes = []

                    weight['id'] = w.id
                    weight['name'] = w.name
                    weight['participants_count'] = w.participants.count()

                    for participant in w.participants.all():
                        athlete = dict()

                        athlete['id'] = participant.id
                        athlete['fio'] = f'{participant.firstName} {participant.lastName} {participant.thirdName}'
                        athlete['discharge'] = participant.discharge
                        athlete['year'] = participant.year

                        athletes.append(athlete)

                    weight['athletes'] = athletes
                    weights_cat.append(weight)

                weight_cat['weights'] = weights_cat
                weights.append(weight_cat)

            return JsonResponse({
                "status": "success",
                "weights": weights
            }, status=200)
    else:
        return JsonResponse({
            "status": "error",
            "message": "You are not a superuser"
        }, status=403)


def show_weight_categories_and_weights_update(request, tournament_id, weight_id):
    if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь' or request.user.is_superuser):
        tournament = Tournament.objects.get(id=tournament_id)
        weight = Weight.objects.get(id=weight_id)

        if request.method == 'POST':
            data = request.POST.get('data')

            if data is None:
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid data"
                }, status=400)

            weight.sorting = data
            weight.save()

            return JsonResponse({
                "status": "success",
                "message": "Weight updated successfully"
            }, status=200)
        else:
            return JsonResponse({
                "status": "error",
                "message": "Method not allowed"
            }, status=402)
    else:
        return JsonResponse({
            "status": "error",
            "message": "You are not a superuser"
        }, status=403)
