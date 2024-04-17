from django.test import TestCase
from base.services.participant_services import filter_participants_by_user, participant_exists, get_participant
from base.models import Participant
from django.contrib.auth.models import User


class ParticipantServicesTestCase(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        # Создаем несколько тестовых пользователей для использования в тестах
        self.participant1 = Participant.objects.create(user=self.user,
                                                       firstName="First name 1",
                                                       lastName="Last name 1")
        self.participant2 = Participant.objects.create(user=self.user,
                                                       firstName="First name 2",
                                                       lastName="Last name 2")

    def test_filter_participants_by_user(self):
        # Проверяем, что функция возвращает только текущего пользователя турниры
        participants = filter_participants_by_user(self.user)

        self.assertEqual(len(participants), 2)
        self.assertEqual(participants[0], self.participant1)

    def test_get_participant(self):
        # Проверяем, что функция возвращает только текущего пользователя турнира по id
        participant = get_participant(self.participant1.id)

        self.assertEqual(participant, self.participant1)

    def test_participant_exists(self):
        # Проверяем, что пользователь существует по id
        self.assertEqual(participant_exists(self.participant1.id), True)
