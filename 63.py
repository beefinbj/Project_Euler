def ndigpow(n):
    base = 1
    counter = 0
    while len(str(base**n)) < n:
        base += 1
    if len(str(base**n)) == n:
        while len(str(base**n)) == n:
            print n
            print base
            counter += 1
            base += 1
    if counter > 0:
        print counter
    return counter

totalcount = 0

for n in range(1000):
    totalcount += ndigpow(n)

print totalcount
