from ..models import WeightCategory


def filter_weight_categories_by_tournament(tournament) -> list:
    """
        Взятие всех весовых категорий по турниру
    """
    return WeightCategory.objects.filter(tournament=tournament)
