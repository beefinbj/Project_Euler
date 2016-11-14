from math import *

def match(H):
    if int((-1+sqrt(1+8*H))/2) != (-1+sqrt(1+8*H))/2:
        return False
    if int((1+sqrt(1+24*H))/6) != (1+sqrt(1+24*H))/6:
        return False
    return True


i = 144

H_i = i*(2*i-1)

while match(H_i) == False:
    i += 1
    H_i = i*(2*i-1)


print H_i
