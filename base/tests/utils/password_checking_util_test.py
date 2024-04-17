from django.test import TestCase
from django.contrib.auth.models import User

from base.utils.password_checking_util import password_checking


class PasswordCheckingUtilTestCase(TestCase):
    def setUp(self):
        self.password = 'password12345'
        self.password_confirmation = 'password12345'
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='username',
                                             password=self.password,
                                             is_superuser=True)

    def test_password_checking_ok(self):
        # Пароль проверен успешно
        list = password_checking(self.user, self.password, self.password_confirmation)

        self.assertEquals(len(list), 2)
        self.assertTrue(list[0])
        self.assertEquals(list[1], 'OK')

    def test_password_checking_password_is_too_short(self):
        # Пароль слишком маленький
        list = password_checking(self.user, '123', '123')

        self.assertEquals(len(list), 2)
        self.assertFalse(list[0])
        self.assertEquals(list[1], 'password is too short')

    def test_password_checking_password_incorrect(self):
        # Пароли разные
        list = password_checking(self.user, self.password, '123')

        self.assertEquals(len(list), 2)
        self.assertFalse(list[0])
        self.assertEquals(list[1], 'confirm password is not the same')
