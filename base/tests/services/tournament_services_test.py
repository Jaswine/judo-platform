from django.test import TestCase
from base.services.tournament_services import get_public_tournaments, get_tournament_by_id, get_tournament_by_slug
from base.models import Tournament
from django.contrib.auth.models import User
import datetime


class TournamentServicesTestCase(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        # Создаем несколько тестовых турниров для использования в тестах
        self.tournament1 = Tournament.objects.create(title='Турнир 1',
                                                     slug="tournament1",
                                                     startData=datetime.datetime.now(),
                                                     finishData=datetime.datetime.now(),
                                                     startTime=datetime.datetime.now().time(),
                                                     user=self.user,
                                                     public=True)
        self.tournament2 = Tournament.objects.create(title='Турнир 2',
                                                     slug="tournament2",
                                                     startData=datetime.datetime.now(),
                                                     finishData=datetime.datetime.now(),
                                                     startTime=datetime.datetime.now().time(),
                                                     user=self.user,
                                                     public=False)

        self.notExistsId = 999

    def test_get_tournament_by_id_exists(self):
        # Проверяем, что функция возвращает правильный турнир, если он существует
        tournament = get_tournament_by_id(self.tournament1.id)

        self.assertEquals(tournament, self.tournament1)

    def test_get_tournament_by_slug_exists(self):
        # Проверяем, что функция возвращает правильный турнир, если он существует
        tournament = get_tournament_by_slug(self.tournament1.slug)

        self.assertEquals(tournament, self.tournament1)

    def test_get_public_tournaments(self):
        # Проверяем, что функция возвращает только публичные турниры и отсортированы по дате обновления
        public_tournaments = get_public_tournaments()

        self.assertEqual(len(public_tournaments), 1)
        self.assertEqual(public_tournaments[0], self.tournament1)
