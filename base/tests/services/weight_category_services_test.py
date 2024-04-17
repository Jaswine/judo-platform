from django.test import TestCase
from base.services.weight_category_services import filter_weight_categories_by_tournament, get_weight_category, \
    filter_weight_categories_by_tournament_year_gender
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

    def test_get_weight_category(self):
        # Проверяем, что функция возвращает весовую категорию
        category = get_weight_category(self.weight_category1.id)

        self.assertEqual(category, self.weight_category1)

    def test_filter_weight_categories_by_tournament(self):
        # Проверяем, что функция возвращает список весовых категорий
        categories = filter_weight_categories_by_tournament(self.tournament)

        self.assertEqual(len(categories), 2)
        self.assertEqual(categories[0], self.weight_category1)
        self.assertEqual(categories[1], self.weight_category2)

    def test_filter_weight_categories_by_tournament_year_gender(self):
        # Проверяем, что функция возвращает список весовых категорий
        categories = filter_weight_categories_by_tournament_year_gender(self.tournament, self.weight_category1.year, self.weight_category1.gender)

        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0], self.weight_category1)

