from fractions import *

num = 3
den = 2

counter = 0

for i in range(999):
    old_num = num
    old_den = den
    num = old_num+2*old_den
    den = old_num + old_den
    result = Fraction(num,den)
    if len(str(result.numerator)) > len(str(result.denominator)):
        counter += 1

print counter
    
