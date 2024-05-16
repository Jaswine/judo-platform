from django.contrib.auth.models import User
from user.models import Profile



def get_user_by_email(email: str) -> User:
    """
        Берем пользователя по email
    """
    return User.objects.get(email=email)


def get_user_by_username(username: str) -> User:
    """
        Берем пользователя по username
    """
    return User.objects.get(username=username)


def get_profile_by_user(user: User) -> User:
    """
        Берем профиль пользователя по profile
    """
    return Profile.objects.get(user=user)


def user_exists(id: int) -> bool:
    """
        Проверяем, что пользователь существует по id
    """
    return User.objects.filter(id=id).exists()


def user_exists_by_username(username: str) -> bool:
    """
        Проверяем, что пользователь существует по username
    """
    return User.objects.filter(username=username).exists()


def user_exists_by_email(email: str) -> bool:
    """
        Проверяем, что пользователь существует по email
    """
    return User.objects.filter(email=email).exists()