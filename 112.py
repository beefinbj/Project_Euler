def inc(n):
    string = str(n)
    if len(string) == 1:
        return True
    for i in range(1,len(string)):
        if int(string[i]) < int(string[i-1]):
            return False
    return True

def dec(n):
    string = str(n)
    if len(string) == 1:
        return True
    for i in range(1,len(string)):
        if int(string[i]) > int(string[i-1]):
            return False
    return True

def bounce(n):
    return not(inc(n) or dec(n))

bounces = 0
totals = 100

while float(bounces)/totals*100 < 99:
    totals += 1
    if bounce(totals):
        bounces += 1

print totals
