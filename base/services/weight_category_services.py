from ..models import WeightCategory, Tournament


def get_weight_category(id: int) -> WeightCategory:
    """
        Взятие весовой категории по id
    """
    return WeightCategory.objects.get(id=id)


def filter_weight_categories_by_tournament(tournament: Tournament) -> list:
    """
        Взятие всех весовых категорий по турниру
    """
    return WeightCategory.objects.filter(tournament=tournament)


def filter_weight_categories_by_tournament_year_gender(tournament: Tournament, year: str, gender: str) -> list:
    """
        Взятие всех весовых категорий по турниру, году и полу
    """
    return WeightCategory.objects.filter(tournament=tournament, year=year, gender=gender)
