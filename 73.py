from fractions import Fraction

visited = {}

total = 0

for i in range(1,12001):
    if i % 1000 == 0:
        print 'Thousand'
    for j in range(i/3,i/2+1):
        res = Fraction(j,i)
        visited[(res.numerator,res.denominator)] = False

print 'Initialized'

def valid(frac):
    num = frac.numerator
    den = frac.denominator
    if float(num)/den <= 1.0/3:
        return False
    if float(num)/den >= 1.0/2:
        return False
    return True

for i in range(1,12001):
    for j in range(i/3,i/2+1):
        res = Fraction(j,i)
        if visited[(res.numerator,res.denominator)] == False:
            if valid(res):
                total += 1
            visited[(res.numerator,res.denominator)] = True

print total
