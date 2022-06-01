def cat_dog_years(human_years: int) -> list:
    """
    Convert human years to dog and cat years.
    :param human_years:
    :return: list containing human, cat and dog years
    """
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    else:
        cat_years = 24 + ((human_years - 2) * 4)
        dog_years = 24 + ((human_years - 2) * 5)

    return [human_years, cat_years, dog_years]
