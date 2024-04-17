from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password

from ..forms import CreateUserForm
from ..services.tournament_services import get_public_tournaments
from ..services.user_services import user_exists_by_email, user_exists_by_username, get_user_by_email


def index(request):
    """
       Главная страница
   """
    # Берем все публичные турниры
    tournaments = get_public_tournaments().order_by('-updated')[:3]

    return render(request, 'base/index.html', {
        'tournaments': tournaments,
    })


def registration_view(request):
    """
         Регистрация новых пользователей
    """
    # Берем форму
    form = CreateUserForm()

    if request.method == 'POST':
        # Берем данные формы
        form = CreateUserForm(request.POST)

        # Проверяем форму на валидность
        if form.is_valid():
            # Сохраняем данные
            new_user = form.save(commit=False)
            # Проверяем, что такого пользователя не существует
            if user_exists_by_username(new_user.username) or user_exists_by_email(new_user.email):
                # Возвращаем сообщение об ошибке, если пользователь уже существует
                messages.error(request, 'Имя пользователя или почта уже занята')
            else:
                new_user.save()

                # Вход в аккаунт
                login(request, new_user)
                return redirect('base:index')

    return render(request, 'base/auth.html', {
        'page_type': 'registration',
        'form': form,
    })


def login_view(request):
    """
      Вход пользователя в аккаунт
    """
    if request.method == 'POST':
        # Взятие данных из формы
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Взятие пользователя по email
            user = get_user_by_email(email)

            # Проверка пароля
            if check_password(password, user.password):
                # Входим в аккаунт
                login(request, user)
                return redirect('base:index')
        except Exception as e:
            messages.error(request, 'Email or Password is incorrect')

    return render(request, 'base/auth.html', {
        'page_type': 'login',
    })


def logout_view(request):
    """
      Выход пользователя из аккаунта
    """
    logout(request)
    return redirect('base:index')
