from fractions import Fraction
from math import *

##fractodec = {}
##dectofrac = {}
##visited = {}
##for i in range(1,1000000):
##    if i % 100000 == 0:
##        print 'Hundred Thousand'
##    for j in range(i*3/7-1,i*3/7+1):
##        res = Fraction(j,i)
##        visited[(res.numerator,res.denominator)] = False
##
##print 'Initialized'
##
##for i in range(1,1000000):
##    if i % 100000 == 0:
##        print 'Hundred Thousand'
##    for j in range(i*3/7-1,i*3/7+1):
##        res = Fraction(j,i)
##        if visited[(res.numerator,res.denominator)] == False:
##            fractodec[(res.numerator,res.denominator)] = float(res.numerator)/res.denominator
##            dectofrac[float(res.numerator)/res.denominator] = (res.numerator,res.denominator)
##            visited[(res.numerator,res.denominator)] = True

bestdiff = float(3)/7
bestnum = 0
bestden = 1

def valid(num,den):
    test = Fraction(num,den)
    if test.numerator == 3 and test.denominator == 7:
        return False
    return True

for i in range(8,1000001):
    num = i*3/7
    den = i
    test = float(num)/den
    diff = float(3/7)-test
    if diff < bestdiff and valid(num,den):
        bestdiff = diff
        bestnum = num
        bestden = den

print bestnum
print bestden
