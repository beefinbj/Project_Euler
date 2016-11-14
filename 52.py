def success(n):
    string = sorted(str(n))
    for i in range(1,7):
        if sorted(str(i*n)) != string:
            return False
    return True

for i in range(1,10000000):
    if success(i):
        print i
        break
