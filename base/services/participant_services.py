from ..models import Participant


def filter_participants_by_user(user) -> list:
    """
        Взятие всех спортсменов по пользователю
    """
    return Participant.objects.filter(user=user)


def participant_exists(id) -> bool:
    """
        Проверяем, что пользователь существует по id
    """
    return Participant.objects.filter(id=id).exists()