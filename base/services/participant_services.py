from ..models import Participant
from django.contrib.auth.models import User


def filter_participants_by_user(user: User) -> list:
    """
        Взятие всех спортсменов по пользователю
    """
    return Participant.objects.filter(user=user)


def get_participant(id: int) -> Participant:
    """
        Берем пользователя по id
    """
    return Participant.objects.get(id=id)


def participant_exists(id: int) -> bool:
    """
        Проверяем, что пользователь существует по id
    """
    return Participant.objects.filter(id=id).exists()