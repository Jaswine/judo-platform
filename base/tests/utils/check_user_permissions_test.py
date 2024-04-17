from django.test import TestCase
from base.utils.check_user_permissions_util import check_user_permissions
from django.contrib.auth.models import User


class CheckUserPermissionsTestCase(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='username',
                                             password='password',
                                             is_superuser=True)

    def test_check_user_permissions_user_is_superuser(self):
        # Проверяем, что пользователь является администратором
        self.assertTrue(check_user_permissions(self.user))
