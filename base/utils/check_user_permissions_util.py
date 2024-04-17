
def check_user_permissions(user) -> bool:
    """
    Проверяет разрешения пользователя
    """
    return (user.profile.userType == 'Админ' or
            user.is_superuser or
            user.profile.userType == 'Секретарь')