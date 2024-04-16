from django.test import TestCase
from base.api.utils.data_utils import takeYearFromDate


class DataUtilsAPITestCase(TestCase):
    def setUp(self):
        self.test_date = '2005-2007'

    def test_takeYearFromDate(self):
        # Проверяем, что выводится год в числе
        year = takeYearFromDate(self.test_date)

        self.assertEquals(2005, year)
