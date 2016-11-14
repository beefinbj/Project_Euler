def first_sun_year(numDays, jan1):
    counter = 0
    if jan1 == 0:
        counter += 1
    feb1 = (jan1+31) % 7
    if feb1 == 0:
        counter += 1
    if numDays == 365:
        mar1 = (feb1+28) % 7
    else:
        mar1 = (feb1+28) % 7
    if mar1 == 0:
        counter += 1
    apr1 = (mar1+28) % 7
    if apr1 == 0:
        counter += 1
    may1 = (apr1+30) % 7
    if may1 == 0:
        counter += 1
    jun1 = (may1+31) % 7
    if jun1 == 0:
        counter += 1
    jul1 = (jun1+30) % 7
    if jul1 == 0:
        counter += 1
    aug1 = (jul1+31) % 7
    if aug1 == 0:
        counter += 1
    sep1 = (aug1+31) % 7
    if sep1 == 0:
        counter += 1
    oct1 = (sep1+30) % 7
    if oct1 == 0:
        counter += 1
    nov1 = (oct1+31) % 7
    if nov1 == 0:
        counter += 1
    dec1 = (nov1+30) % 7
    if dec1 == 0:
        counter += 1
    return counter, (dec1+31)%7

def solve():
    counts = 0
    year = 1901
    numdays = 365
    jan1 = 2
    while year <= 2000:
        if year%4 == 0:
            numdays = 366
        else:
            numdays = 365
        yearsuns, nextyear = first_sun_year(numdays, jan1)
        counts += yearsuns
        jan1 = nextyear
        year += 1
    return counts

print solve()
