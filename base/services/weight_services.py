from base.models import Weight


def get_weight_by_id(id: int) -> Weight:
    """
        Берем вес по id
    """
    return Weight.objects.get(id=id)


def get_weight_list() -> list:
    """
        Берем все веса
    """
    return Weight.objects.all()


def weight_exists(id: int) -> bool:
    """
        Проверяет, существует ли вес по id
    """
    return Weight.objects.filter(id=id).exists()
