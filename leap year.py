def is_leap(years):
    leap = False
    special_years = [1800, 1900, 2100, 2200, 2300, 2500]
    if year in special_years:
        leap = False
    else:
        if year % 400 == 0:
            leap = True
        else:
            if year % 100 == 0:
                leap = False
            else:
                if year % 4 == 0:
                    leap = True

    return leap


year = int(input())
print(is_leap(year))