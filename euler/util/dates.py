def get_number_of_days_in_month(year: int, month: int) -> int:
    """ Calculates and returns number of days in a given month """
    if month == 2:
        is_leaf_year = year % 400 == 0 or year % 100 != 0 and year % 4 == 0
        return is_leaf_year and 29 or 28

    return month in {4, 6, 9, 11, } and 30 or 31
