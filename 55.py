def palin(n):
    if len(str(n)) <= 1:
        return True
    elif len(str(n)) == 2:
        return str(n)[0] == str(n)[-1]
    elif str(n)[0] != str(n)[-1]:
        return False
    else:
        return palin(int(str(n)[1:-1]))

def iterate(n):
    rev = int(str(n)[::-1])
    return n+rev

def lychrel(n):
    counter = 1
    new = iterate(n)
    while counter < 50:
        if palin(new):
            return False
        new = iterate(new)
        counter += 1
    return True

totals = 0

for i in range(1,10000):
    if lychrel(i):
        totals += 1

print totals
