from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db.models import Q


from ..services.participant_services import filter_participants_by_user
from ..services.user_services import get_user_by_username, get_profile_by_user
from ..forms import UpdateUserForm, UpdateProfileForm
from base.utils.password_checking_util import password_checking
from ..models import Participant


@login_required(login_url='base:login')
def show_profile(request, username):
    """
      Страница профиля пользователя с информацией о нем
    """
    # Берем пользователя и его профиль
    user = get_user_by_username(username)
    profile = get_profile_by_user(user)

    if request.method == 'POST':
        # Берем статус формы
        form_type = request.POST.get('form_type')

        # Проверяем статус
        if form_type == 'change__status':
            # Берем тип пользователя
            user_type = request.POST.get('user_type')

            if user_type:
                # Сохраняем данные
                profile.userType = user_type
                profile.save()

    return render(request, 'base/profile.html', {
        'page_type': 'view_profile',
        'user': user,
        'profile': profile,
    })


@login_required(login_url='base:login')
def edit_profile(request, username):
    """
       Страница редактирования информации о пользователе
    """
    # Берем пользователя и его профиль
    user = get_user_by_username(username)
    profile = get_profile_by_user(user)

    # Проверяем текущего пользователя и взятого по имени
    if request.user.username == user.username:
        # Создаем формы
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)

        if request.method == 'POST':
            # Берем данные из формы
            user_form = UpdateUserForm(request.POST, instance=user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

            # Проверяем валидность форм
            if user_form.is_valid() and profile_form.is_valid():
                # Сохраняем данные
                user_form.save()
                profile_form.save()

                return redirect('base:show_profile', username=user.username)

        return render(request, 'base/profile.html',  {
            'page_type':  'edit_profile',

            'user': user,
            'profile': profile,

            'user_form': user_form,
            'profile_form': profile_form,

            'form': [user_form, profile_form],
        })
    else:
        return redirect('base:show_profile', username=user.username)


@login_required(login_url='base:login')
def edit_password_profile(request, username):
    """
       Страница изменения пароль пользователя
    """
    # Берем пользователя по имени
    user = get_user_by_username(username)

    # Проверяем текущего пользователя и взятого по имени
    if request.user.username == user.username:
        if request.method == 'POST':
            # Берем данные из формы
            password = request.POST.get('password')
            password_confirmation = request.POST.get('password_confirmation')

            # Сравниваем пароли
            validation = password_checking(user, password, password_confirmation)

            if validation:
                # Сохраняем данные
                user.password = make_password(password)
                user.save()

                return redirect('base:show_profile', username=user.username)
            else:
                messages.error(request, validation[1])

        return render(request, 'base/profile.html', {
            'page_type': 'edit_password',

            'user': user,
            'profile': user.profile,
        })
    else:
        return redirect('base:show_profile', username=user.username)


@login_required(login_url='base:login')
def delete_account(request, username):
    """
       Страница удаления аккаунта
    """
    # Берем пользователя по имени
    user = get_user_by_username(username)

    # Проверяем текущего пользователя и взятого по имени
    if request.user.username == user.username:
        if request.method == 'POST':
            # Удаляем пользователя
            user.delete()

            return redirect('base:login')
    else:
        return redirect('base:show_profile', username=user.username)

    return render(request, 'base/profile.html', {
        'page_type': 'delete_account',
        'user': user,
    })


@login_required(login_url='base:login')
def show_all_athletes_profile(request, username):
    """
       Страница с выводом, фильтрацией и сортировкой всех спортсменов, добавленых пользователем
    """
    # Берем пользователя по имени и его профиль
    user = get_user_by_username(username)
    profile = get_profile_by_user(user)

    # Берем всех спортсменов у пользователя
    participants = filter_participants_by_user(user).order_by('-updated')

    if request.method == 'GET':
        # Берем данные поиска и сортировки
        search = request.GET.get('search', '')
        new_last = request.GET.get('new_last', '')

        # Проверяем данные поиска и ищем похожих
        if search is not '':
            participants = Participant.objects.filter(Q(firstName__icontains=search)
                                                      | Q(lastName__icontains=search)
                                                      | Q(thirdName__icontains=search)
                                                      | Q(year__icontains=search)
                                                      | Q(discharge__icontains=search)
                                                      | Q(gender__icontains=search)).order_by('-updated')

        # Проверяем данные сортировки
        #                   и сортируем в зависимости от типа пришедших данных
        if new_last is not '':
            if new_last == 'new':
                participants = participants.order_by('-created')
            if new_last == 'last':
                participants = participants.order_by('created')

    return render(request, 'base/profile.html',  {
        'page_type': 'show_all_athletes',

        'user': user,
        'profile': profile,

        'participants': participants,

        'search': search,
        'new_last': new_last,
    })
