from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from ..models import Participant
from ..forms import ParticipantForm
from ..services.participant_services import get_participant
from ..utils.check_user_permissions_util import check_user_permissions


@login_required(login_url='base:login')
def add_new_athlete(request):
    """
        Страница добавления нового спортсмена
   """
    if check_user_permissions(request.user):
        # Инициализируем форму
        form = ParticipantForm()

        if request.method == 'POST':
            # Берем данные из формы
            form = ParticipantForm(request.POST)
            # Берем тренера
            coach = request.POST.get('coach', request.user.profile.fullName)

            # Проверяем валидность
            if form.is_valid():
                # Сохраняем данные без явного сохранения
                athlete = form.save(commit=False)

                # Добавляем текущего пользователя и тренера
                athlete.user = request.user
                athlete.coach = coach

                # Сохраняем данные
                athlete.save()

                return redirect('base:show_all_athletes', request.user.username)

        return render(request, 'base/profile/athlete/add_athlete.html', {
            'page_type': 'add_new_athlete',
            'form': form
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def update_athlete(request, athlete_id):
    """
        Страница обновления выбранного спортсмена взятого по ID
    """
    # Берем спортсмена по id
    athlete = get_participant(athlete_id)

    if check_user_permissions(request.user):
        # Инициализируем форму
        form = ParticipantForm(instance=athlete)

        if request.method == 'POST':
            # Берем данные из формы
            form = ParticipantForm(request.POST, instance=athlete)
            coach = request.POST.get('coach', request.user.profile.fullName)

            if form.is_valid():
                # Сохраняем данные
                athlete = form.save(commit=False)
                athlete.coach = coach
                athlete.save()

                return redirect('base:show_all_athletes', request.user.username)

        return render(request, 'base/profile/athlete/add_athlete.html', {
            'page_type': 'update_athlete',

            'form': form,
            'athlete': athlete,
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def delete_athlete(request, athlete_id):
    """
         Страница удаления выбранного спортсмена взятого по ID
    """
    # Берем спортсмена по id
    athlete = get_participant(athlete_id)

    if check_user_permissions(request.user):
        if request.method == 'POST':
            # Удаляем пользователя
            athlete.delete()
            return redirect('base:show_all_athletes', request.user.username)

        return render(request, 'base/profile/athlete/delete_athlete.html', {
            'page_type': 'delete_athlete',
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')
