from django.views.decorators.csrf import csrf_exempt
from base.models import Weight
from ...models import Tournament, WeightCategory, Participant, Weight
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@csrf_exempt
def show_weight_categories(request, id):
        tournament = Tournament.objects.get(id=id)
        weight_categories = WeightCategory.objects.filter(tournament=tournament)
        participants = Participant.objects.filter(user=request.user)
        
        if request.method == 'GET':
            athletes = []

            for participant in participants:
                user = {}
                weights_for_registration = []
                only_year = int(str(participant.year).split('-')[0])
                
                for weight_category in weight_categories:
                    user_in_weight_category_count = 0
                    year_list = [int(i) for i in weight_category.year.split('-')]
                    
                    if len(year_list) == 2:
                        year_list = [year_list[1] - i for i in range(year_list[1] - year_list[0] + 1) ]
                        
                    if only_year in year_list:
                        for w in weight_category.weight.all():
                            if participant in w.participants.all():
                                user_in_weight_category_count += 1
                            
                        if user_in_weight_category_count == 0:
                            for w in weight_category.weight.all():
                                if participant.gender == weight_category.gender:
                                    weights_for_registration.append({
                                        'id': w.id,
                                        'name': w.name,
                                    })
                
                if len(weights_for_registration) > 0:
                    user['id'] = participant.id
                    user['fio'] = f'{participant.lastName} {participant.firstName} {participant.thirdName}'
                    user['discharge'] = participant.discharge
                    user['gender'] = participant.gender
                    user['year'] = only_year
                    user['weights'] = weights_for_registration

                    athletes.append(user)

            return JsonResponse({
                'athletes': athletes,
            }, status=200)
            
        if request.method == 'POST':
            if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
                athlete = request.POST.get('athlete', None)
                weight = request.POST.get('weight', None)

                print('Athlete: ' + athlete, 'Weight: ' + weight)

                if weight:
                    weigh = Weight.objects.get(id=weight)
                    weigh.participants.add(athlete)

                    return JsonResponse({
                        'message': 'Athlete added successfully'
                    }, status=200)
                else:
                    return JsonResponse({
                        'message': 'Invalid weight'
                    }, status=400)
            else:
                return JsonResponse({
                    'message': "You don't have any permissions"
                }, status=401)
            
        return JsonResponse({
            'message': 'Method not allowed',
        }, status=402)
    
@csrf_exempt
def list_of_registered_on_tournament(request, id):
        tournament = Tournament.objects.get(id=id)
        weight_categories = WeightCategory.objects.filter(tournament=tournament)
        participants = Participant.objects.filter(user=request.user)
        
        if request.method == 'GET':
            athletes = []

            for participant in participants:
                user = {}
                weights_for_registration = []
                only_year = int(str(participant.year).split('-')[0])
                
                for weight_category in weight_categories:
                    user_in_weight_category_count = 0
                    year_list = [int(i) for i in weight_category.year.split('-')]
                    
                    if len(year_list) == 2:
                        year_list = [year_list[1] - i for i in range(year_list[1] - year_list[0] + 1) ]
                        
                    if only_year in year_list:
                        for w in weight_category.weight.all():
                            if participant in w.participants.all():
                                user_in_weight_category_count += 1

                                weights_for_registration.append({
                                    'id': w.id,
                                    'name': w.name,
                                })
                                
                
                if len(weights_for_registration) > 0:
                    user['id'] = participant.id
                    user['fio'] = f'{participant.lastName} {participant.firstName} {participant.thirdName}'
                    user['discharge'] = participant.discharge
                    user['gender'] = participant.gender
                    user['year'] = only_year
                    user['weights'] = weights_for_registration

                    athletes.append(user)

            return JsonResponse({
                'athletes': athletes,
            }, status=200)
            
        if request.method == 'POST':
            if (request.user.profile.userType == 'Админ' or request.user.is_superuser or request.user.profile.userType == 'Секретарь'):
                athlete = request.POST.get('athlete', None)
                weight = request.POST.get('weight', None)

                if weight:
                    weight_category = Weight.objects.get(id=weight)
                    weight_category.participants.remove(athlete)

                    return JsonResponse({
                        'message': 'Athlete added successfully'
                    }, status=200)
                else:
                    return JsonResponse({
                        'message': 'Invalid weight'
                    }, status=400)
            else:
                return JsonResponse({
                    'message': "User don't have any permissions"
                }, status=401)
            
        return JsonResponse({
            'message': 'Method not allowed',
        }, status=402)