from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

from user.forms.user_forms import CreateUserForm
from user.services.user_services import user_exists_by_username, user_exists_by_email, get_user_by_email


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
                return redirect('/')

    return render(request, 'user/auth.html', {
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
                return redirect('/')
        except Exception as e:
            messages.error(request, 'Email or Password is incorrect')

    return render(request, 'user/auth.html', {
        'page_type': 'login',
    })

@login_required(login_url='login')
def logout_view(request):
    """
      Выход пользователя из аккаунта
    """
    logout(request)
    return redirect('logout')