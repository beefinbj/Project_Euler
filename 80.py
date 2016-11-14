from math import *

##def log_10(n):
##    return log(n)/log(10)
##
##def add(block):
##    r = block
##    out = 0
##    for i in range(20):
##        r = r*10
##        dig = int(r)
##        out += dig
##        r = r-dig
##    return out
##
##blocks = []
##
##for i in range(10,110,10):
##    r = sqrt((100**i)*2)
##    trail = int(r % 10**10)
##    print trail
##    blocks.append(trail)
##
##def sumdigs(n):
##    out = 0
##    k = str(n)
##    for dig in k:
##        out += int(dig)
##    return out
##
##tot = 0
##for num in blocks:
##    tot += sumdigs(num)
##
##print tot

def sumdigs(n):
    out = 0
    r = n
    while r > 0:
        out += int(r%10)
        r = r/10
    return out

def sumroot(n):
    dec = sqrt(n)-int(sqrt(n))
    first = int(dec*(10**100))
    print first
    return sumdigs(first)

print sumroot(2)
