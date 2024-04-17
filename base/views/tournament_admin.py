from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage

from ..models import Tournament, Logos, WeightCategory, Sponsors, Participant, Weight
from ..forms import UpdateTournamentMainInformationForm
from ..services.tournament_services import get_tournament_by_slug
from ..services.weight_category_services import filter_weight_categories_by_tournament_year_gender
from ..utils.check_user_permissions_util import check_user_permissions


@csrf_exempt
@login_required(login_url='base:login')
def tournamets_admin_update_info(request, slug: str):
    """
        Страница обновления информации о турнире
    """
    if check_user_permissions(request.user):
        # Берем данные турнира
        tournire = get_tournament_by_slug(slug)
        # Создаем форму
        form = UpdateTournamentMainInformationForm(instance=tournire)

        if request.method == 'POST':
            # Берем данные из формы
            form = UpdateTournamentMainInformationForm(request.POST, request.FILES, instance=tournire)

            # Проверяем форму на валидность
            if form.is_valid():
                # Берем логотипы спонсоров и фото для загрузки
                logotips = request.FILES.getlist('files')
                sponsors_logotips = request.FILES.getlist('sponsors-logotips')

                # Берем логотипы спонсоров и фото для удаления
                delete_logotips = request.POST.getlist('delete-logotips')
                delete_sponsors = request.POST.getlist('delete-sponsors')

                # Удаляем выбранные фото, если они есть
                if len(delete_logotips) > 0:
                    for logotip in delete_logotips:
                        tournire.logos.filter(id=int(logotip)).delete()

                # Удаляем выбранные логотипы спонсоров, если они есть
                if len(delete_sponsors) > 0:
                    for sponsor in delete_sponsors:
                        tournire.sponsors.filter(id=int(sponsor)).delete()

                # Добавляем фото, если они есть
                if len(logotips) > 0:
                    for logo in logotips:
                        new_file = Logos(image=logo)

                        new_file.save()
                        tournire.logos.add(new_file)

                # Добавляем логотипы спонсоров, если они есть
                if len(sponsors_logotips) > 0:
                    for logo in sponsors_logotips:
                        new_file = Sponsors(image=logo)

                        new_file.save()
                        tournire.sponsors.add(new_file)

                tournire.title = form.cleaned_data.get('title_en')
                tournire.title_en = form.cleaned_data.get('title_en')
                tournire.title_ru = form.cleaned_data.get('title_ru')
                tournire.title_kk = form.cleaned_data.get('title_kk')

                tournire.logo = form.cleaned_data.get('logo')

                tournire.about = form.cleaned_data.get('about_en')
                tournire.about_en = form.cleaned_data.get('about_en')
                tournire.about_ru = form.cleaned_data.get('about_ru')
                tournire.about_kk = form.cleaned_data.get('about_kk')

                tournire.rang = form.cleaned_data.get('rang')

                tournire.startData = form.cleaned_data.get('startData')
                tournire.finishData = form.cleaned_data.get('finishData')
                tournire.startTime = form.cleaned_data.get('startTime')

                tournire.credit = form.cleaned_data.get('credit')
                tournire.tatamis_count = form.cleaned_data.get('tatamis_count')

                tournire.place = form.cleaned_data.get('place_en')
                tournire.place_en = form.cleaned_data.get('place_en')
                tournire.place_ru = form.cleaned_data.get('place_ru')
                tournire.place_kk = form.cleaned_data.get('place_kk')

                tournire.chiefJustice = form.cleaned_data.get('chiefJustice_en')
                tournire.chiefJustice_en = form.cleaned_data.get('chiefJustice_en')
                tournire.chiefJustice_ru = form.cleaned_data.get('chiefJustice_ru')
                tournire.chiefJustice_kk = form.cleaned_data.get('chiefJustice_kk')

                tournire.chiefSecretary = form.cleaned_data.get('chiefSecretary_en')
                tournire.chiefSecretary_en = form.cleaned_data.get('chiefSecretary_en')
                tournire.chiefSecretary_ru = form.cleaned_data.get('chiefSecretary_ru')
                tournire.chiefSecretary_kk = form.cleaned_data.get('chiefSecretary_kk')

                tournire.status = form.cleaned_data.get('status')
                tournire.public = form.cleaned_data.get('public')

                try:
                    # Сохраняем данные
                    tournire.save()
                    return redirect('base:show_tournaments')
                except:
                    return redirect('base:show_tournaments')

        return render(request, 'base/tournaments/panel/tournament_panel.html', {
            'page_type': 'tournament_panel_update_info',

            'tournire': tournire,
            'tournament_form': form,
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def tournamets_admin_delete(request, slug: str):
    """
        Удаление турнира
    """
    if check_user_permissions(request.user):
        # Берем турнир
        tournire = get_tournament_by_slug(slug)

        if request.method == 'POST':
            # Удаляем турнир
            tournire.delete()

            return redirect('base:show_tournaments')

        return render(request, 'base/tournaments/panel/tournament_panel.html', {
            'page_type': 'tournamets_admin_delete',
            'tournire': tournire,
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def athletes_admin_category(request, slug: str, year: str, gender: str):
    """
        Показ участников категории
    """
    if check_user_permissions(request.user):
        # Взятие турнира
        tournament = get_tournament_by_slug(slug)
        # Взятие первой весовой категории
        weight_category = filter_weight_categories_by_tournament_year_gender(tournament, year, gender).first()

        return render(request, 'base/tournaments/panel/tournament_panel.html', {
            'page_type': athletes_admin_category,

            'category': weight_category,
            'tournire': tournament,
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')
