f = 1010101030

from math import *

def hit(s):
    p = str(s)
    if len(p) != 19:
        return False
    for i in range(1,10):
        if p[(i-1)*2] != str(i):
            return False
    return True

def test1(s):
    p = str(s)
    a = int(p[-4])
    b = int(p[-3])
    x1 = (6*(a**2)) % 10
    x2 = b**2 % 10
    x3 = (6*b)/10
    xt = x1 + x2 + x3
    return (xt%10) == 8

while f < 1389026623:
    if test1(f):
        print f**2
        if hit(f**2):
            break
        f += 100
