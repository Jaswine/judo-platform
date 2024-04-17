from ..models import Tournament


def get_tournament_by_id(id: int) -> Tournament:
    """
        Взятие турнира по id
    """
    return Tournament.objects.get(id=id)


def get_tournament_by_slug(slug: str) -> Tournament:
    """
        Взятие турнира по slug
    """
    return Tournament.objects.get(slug=slug)


def get_public_tournaments() -> list:
    """
        Взятие всех публичных турниров
    """
    return Tournament.objects.filter(public=True)
