from django.test import TestCase
from base.services.weight_category_services import filter_weight_categories_by_tournament
from base.models import Tournament, WeightCategory
from django.contrib.auth.models import User
import datetime


class WeightCategoryServicesTestCase(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        # Создаем тестовый турнир
        self.tournament = Tournament.objects.create(title='Турнир 1',
                                                    slug="tournament",
                                                    startData=datetime.datetime.now(),
                                                    finishData=datetime.datetime.now(),
                                                    startTime=datetime.datetime.now().time(),
                                                    user=self.user,
                                                    public=True)
        # Создаем тестовые весовые категории
        self.weight_category1 = WeightCategory.objects.create(tournament=self.tournament,
                                                              year="2000",
                                                              gender="Мужской")
        self.weight_category2 = WeightCategory.objects.create(tournament=self.tournament,
                                                              year="2001",
                                                              gender="Мужской")

    def test_filter_weight_categories_by_tournament(self):
        # Проверяем, что функция возвращает список весовых категорий
        categories = filter_weight_categories_by_tournament(self.tournament)

        self.assertEqual(len(categories), 2)
        self.assertEqual(categories[0], self.weight_category1)
        self.assertEqual(categories[1], self.weight_category2)
