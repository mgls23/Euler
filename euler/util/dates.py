def calculate_number_of_days_in_month(year, month):
    if month in {9, 4, 6, 11, }: return 30

    if month == 2:
        if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
            return 29
        else:
            return 28

    return 31
