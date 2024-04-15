from base.models import Weight


def get_weight_by_id(id) -> Weight:
    """
        Берем вес по id
    """
    return Weight.objects.get(id=id)


def weight_exists(id) -> bool:
    """
        Проверяет, существует ли вес по id
    """
    return Weight.objects.filter(id=id).exists()
