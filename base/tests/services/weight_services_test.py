from django.test import TestCase
from base.services.weight_services import get_weight_by_id, weight_exists
from base.models import Weight


class WeightServicesTestCase(TestCase):
    def setUp(self):
        # Создаем тестовый вес
        self.weight = Weight.objects.create(name="60")

    def test_get_weight_by_id(self):
        # Проверяем, что функция возвращает правильный вес, если он существует
        weight = get_weight_by_id(self.weight.id)

        self.assertEquals(weight, self.weight)

    def test_weight_exists(self):
        # Проверяем, существует ли вес по id
        self.assertEqual(weight_exists(self.weight.id), True)