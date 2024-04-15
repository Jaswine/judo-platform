def takeYearFromDate(year) -> int:
    """
        Берем только год из даты
    """
    try:
        return int(str(year).split('-')[0])
    except Exception as e:
        print("Exception: ", e)
        return 0
