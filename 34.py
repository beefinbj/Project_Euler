facdic = {}

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def test_digfac(a):
    tot = 0
    for dig in str(a):
        tot += factorial(int(dig))
    if tot == a:
        print a
        print "Found"
    return tot == a

winners = []
            
for i in range(3,1000000):
    if test_digfac(i) == True:
        winners.append(i)

print winners
