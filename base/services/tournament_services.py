from ..models import Tournament


def get_tournament_by_id(id) -> Tournament:
    """
        Взятие турнира по id
    """
    try:
        return Tournament.objects.get(id=id)
    except Tournament.DoesNotExist as e:
        print("Exception", e)
        return None


def get_public_tournaments() -> list:
    """
        Взятие всех публичных турниров
    """
    return Tournament.objects.filter(public=True).order_by('-updated')
