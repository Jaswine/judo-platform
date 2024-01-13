from ...models import Tournament, WeightCategory, Participant, Weight
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url= 'base:login')
def show_weight_categories(request, id):
    if request.method == 'GET':
        athletes = []

        tournament = Tournament.objects.get(id=id)
        weight_categories = WeightCategory.objects.filter(tournament=tournament)
        participants = Participant.objects.filter(user=request.user)

        for participant in participants:
            user = {}
            
            for weight_category in weight_categories:
                all_tournament_weight_categories = weight_category.weight.all()
                
                # weight_categorie_weights = weight_category.year.split('-')

                print('Weight Category', weight_category.year, weight_category.gender, all_tournament_weight_categories)

            user['id'] = participant.id
            user['fio'] = f'{participant.lastName} {participant.firstName} {participant.thirdName}'
            user['year'] = participant.year
            user['discharge'] = participant.discharge
            user['gender'] = participant.gender
            user['coach'] = participant.coach

            athletes.append(user)
            

        return JsonResponse({
            'athletes': athletes,
        }, status=200)