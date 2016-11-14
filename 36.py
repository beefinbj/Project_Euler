def pal(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    else:
        return pal(n[1:-1])

winners = []

for i in range(1000000):
    if pal(str(i)) == True and pal(bin(i)[2:]) == True:
        print i
        winners.append(i)


print winners
