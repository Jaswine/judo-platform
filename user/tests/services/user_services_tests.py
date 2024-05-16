from django.test import TestCase
from django.contrib.auth.models import User

from user.services.user_services import get_user_by_email, get_user_by_username, user_exists, \
    user_exists_by_username, user_exists_by_email


class ParticipantServicesTestCase(TestCase):
    def setUp(self):
        # Объявляем тестовые данные
        test_user_username = 'jon_due'
        test_user_email = 'example@example.com'
        test_user_password = 'password'

        # Создаем тестового пользователя
        self.user = User.objects.create_user(username=test_user_username,
                                             email=test_user_email,
                                             password=test_user_password)

    def test_get_user_by_email(self):
        # Проверяем, что функция возвращает пользователя по почте
        user = get_user_by_email(self.user.email)

        self.assertEqual(user, self.user)

    def test_get_user_by_username(self):
        # Проверяем, что функция возвращает пользователя по имени
        user = get_user_by_username(self.user.username)

        self.assertEqual(user, self.user)

    def test_user_exists(self):
        # Проверяем, что функция возвращает, что пользователь существует
        ue = user_exists(self.user.id)
        self.assertTrue(ue)

    def test_user_exists_by_username(self):
        # Проверяем, что функция возвращает, что пользователь существует
        ue = user_exists_by_username(self.user.username)
        self.assertTrue(ue)

    def test_user_exists_by_email(self):
        # Проверяем, что функция возвращает, что пользователь существует
        ue = user_exists_by_email(self.user.email)
        self.assertTrue(ue)