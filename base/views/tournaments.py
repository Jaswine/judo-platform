from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.forms import ValidationError, IntegerField

from ..models import Tournament, Logos, WeightCategory, Sponsors, Weight, Participant
from ..forms import CreateTournamentForm, WeightCategoryForm
from ..services.participant_services import filter_participants_by_user
from ..services.tournament_services import get_tournament_by_slug
from ..services.weight_category_services import filter_weight_categories_by_tournament, get_weight_category
from ..services.weight_services import get_weight_by_id, get_weight_list
from ..utils.check_user_permissions_util import check_user_permissions
from ..utils_file import slug_generator, checking_slug, generate_slug
from ..services_file import get_tournaments, get_all_weight_category, get_user_profile
from ..filters import TournamentFilter


def show_tournaments(request):
    """
         Вывод всех турниров
   """
    return render(request, 'base/tournaments/show_tournaments.html')


def tournament_show_about(request, slug):
    """
        Вывод одного турнира, описание
    """
    # Берем турнир
    tournament = get_tournament_by_slug(slug)

    # Берем категории турнира
    tournament_women_categories = tournament.weightcategory_set.filter(gender="Женский")
    tournament_men_categories = tournament.weightcategory_set.filter(gender="Мужской")

    return render(request, 'base/tournaments/show_tournament/pages/tournament_about.html', {
        'tournament': tournament,

        'tournament_women_categories': tournament_women_categories,
        'tournament_men_categories': tournament_men_categories,
    })


def tournament_show_participants(request, slug):
    """
      Вывод одного турнира, участники
   """
    # Берем турнир
    tournament = get_tournament_by_slug(slug)

    return render(request, 'base/tournaments/show_tournament/pages/tournament_participants.html', {
        'tournament': tournament,
    })


def tournament_show_protocol(request, slug):
    """
         Вывод одного турнира, протокол
    """
    # Берем турнир
    tournament = get_tournament_by_slug(slug)

    return render(request, 'base/tournaments/show_tournament/pages/tournament_protocol.html', {
        'tournament': tournament,
    })


def tournament_show_fights(request, slug):
    """
         Вывод одного турнира, поединки
   """
    # Берем турнир
    tournament = get_tournament_by_slug(slug)

    return render(request, 'base/tournaments/show_tournament/pages/tournament_fights.html', {
        'tournament': tournament,
    })


def tournament_show_results(request, slug):
    """
         Вывод одного турнира, результаты
    """
    # Берем турнир
    tournament = get_tournament_by_slug(slug)

    return render(request, 'base/tournaments/show_tournament/pages/tournament_results.html', {
        'tournament': tournament,
    })


def tournament_show_medals(request, slug):
    """
         Вывод одного турнира, медали
    """
    # Берем турнир
    tournament = get_tournament_by_slug(slug)

    return render(request, 'base/tournaments/show_tournament/pages/tournament_medals.html', {
        'tournament': tournament,
    })


@login_required(login_url='base:login')
def create_tournamets(request):
    """
         Создание турнира
    """
    if check_user_permissions(request.user):
        # Берем форму
        form = CreateTournamentForm()

        if request.method == 'POST':
            # Берем данные из формы
            form = CreateTournamentForm(request.POST, request.FILES)

            # Проверка формы на валидацию
            if form.is_valid():
                try:
                    # Генерируем слаг
                    slug = checking_slug(slug_generator(form.cleaned_data.get('title_en')))
                    tournament = form.save(commit=False)

                    # Запись пользователя и слага
                    tournament.user = request.user
                    tournament.slug = slug

                    # Сохранил сообщения
                    tournament.save()

                    return redirect('base:create_tournamets__images', slug)
                except Exception as error:
                    messages.error(request, error)
                    return redirect('base:create_tournament')

        return render(request, 'base/tournaments/create_tournament.html', {
            'form': form,
            'page_type': 'create_tournament__part__one',
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def create_tournamets__images(request, slug):
    """
          Загрузка изображений для турнира
    """
    if check_user_permissions(request.user):
        # Берем турнир
        tournire = get_tournament_by_slug(slug)

        if request.method == 'POST':
            # Берем изображения и спонсорские логотипы
            logotips = request.FILES.getlist('files')
            sponsors_logotips = request.FILES.getlist('sponsors-logotips')

            # Проверяем изображения и загружаем их
            if len(logotips) > 0:
                for logo in logotips:
                    new_file = Logos(image=logo)

                    new_file.save()
                    tournire.logos.add(new_file)

            # Проверяем логотипы и загружаем их
            if len(sponsors_logotips) > 0:
                for logo in sponsors_logotips:
                    new_file = Sponsors(image=logo)

                    new_file.save()
                    tournire.sponsors.add(new_file)

            # Сохраняем турнир
            tournire.save()
            return redirect('base:weight_categories', tournire.slug)

        return render(request, 'base/tournaments/create_tournament.html', {
            'page_type': 'create_tournament__part__two',
            'tournire': tournire,
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def weight_categories(request, slug):
    """
         Весовые категории
    """
    # Берем турнир
    tournament = get_tournament_by_slug(slug)
    # Берем весовые категории
    weight_categories = filter_weight_categories_by_tournament(tournament)
    # Берем форму
    form = WeightCategoryForm()

    if request.method == 'POST':
        # Берем данные из формы
        form = WeightCategoryForm(request.POST)

        # Проверяем форму
        if form.is_valid():
            # Сохраняем категорию
            category = form.save(commit=False)
            # Сохраняем турнир
            category.tournament = tournament
            category.save()

            return redirect('base:weight_category_weight', tournament.slug, category.id)

    return render(request, 'base/tournaments/weight_categories.html', {
        'weight_categories': weight_categories,
        'form': form,
        'tournament': tournament
    })


@login_required(login_url='base:login')
def weight_category_weight(request, slug, id):
    """
         Весовые категории, показ и создание категории
    """
    if check_user_permissions(request.user):
        # Берем турнир
        tournament = get_tournament_by_slug(slug)
        # Берем категорию
        weight_category = get_weight_category(id)

        if request.method == 'POST':
            # Берем вес
            weight = request.POST.get('weight')

            # Проверяем вес
            if weight is not None and 1 < len(weight) < 3:
                # Создаем новый вес
                weight_type = Weight.objects.create(
                    name=weight
                )

                # Сохраняем вес
                weight_type.save()

                # Добавляем вес в весовую категорию
                weight_category.weight.add(weight_type.id)

                # Сохраняем весовую категорию
                weight_category.save()
                return redirect('base:weight_category_weight', tournament.slug, weight_category.id)
            else:
                messages.error(request, 'Error creating weight category')

        return render(request, 'base/tournaments/weight_add.html', {
            'tournament': tournament,
            'weight_category': weight_category,
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def weight_category_weight_delete(request, slug, id, weight_id):
    """
          Удаление веса
   """
    if check_user_permissions(request.user):
        # Берем турнир
        tournament = get_tournament_by_slug(slug)
        # Берем категорию
        weight_category = get_weight_category(id)
        # Берем вес
        weight = get_weight_by_id(weight_id)

        if weight:
            # Удаляем вес из весовой категории
            weight.delete()

            messages.success(request, 'Weight category deleted successfully')
            return redirect('base:weight_category_weight', tournament.slug, weight_category.id)
        else:
            messages.error(request, 'Weight category not found')
            return redirect('base:weight_category_weight', tournament.slug, weight_category.id)
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def weight_categories_delete(request, slug, pk):
    """
          Удаление весовой категории
    """
    if check_user_permissions(request.user):
        # Берем турнир
        tournament = get_tournament_by_slug(slug)
        # Берем категорию
        weight_category = get_weight_category(pk)

        # Удаление весовой категории
        weight_category.delete()

        return redirect('base:weight_categories', tournament.slug)
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def registration_on_tournament(request, slug):
    """
         Регистрация пользователей на турнир
    """
    if check_user_permissions(request.user):
        # Взятие турнира
        tournament = get_tournament_by_slug(slug)
        # Взятие весовой категории
        weight_category = filter_weight_categories_by_tournament(tournament)

        # Взятие человек
        participants = filter_participants_by_user(request.user)
        # Взятие всех весов
        weight = get_weight_list()

        context = {
            'page_type': 'registration',

            'tournament': tournament,
            'participants': participants,

            'weight': weight,
            'weight_category': weight_category
        }
        return render(request, 'base/tournaments/athlete_registration.html', context)
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def list_of_registered_on_tournament(request, slug):
    """
            Показ всех зарегистрированных пользователей на турнир
      """
    if check_user_permissions(request.user):
        # Взятие турнира
        tournament = get_tournament_by_slug(slug)
        # Показ всех спортсменов пользователя
        participants = filter_participants_by_user(request.user)

        return render(request, 'base/tournaments/athlete_registration.html', {
            'page_type': 'list_of_registered',

            'tournament': tournament,
            'athletes': participants
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')


@login_required(login_url='base:login')
def tournament_toss(request, slug):
    """
        Сортировка участников турнира
    """
    if check_user_permissions(request.user):
        # Взятие турнира
        tournament = get_tournament_by_slug(slug)

        return render(request, 'base/tournaments/toss.html', {
            'tournament': tournament,
        })
    else:
        messages.error(request, "У вас недостаточно прав")
        return redirect('base:show_tournaments')
