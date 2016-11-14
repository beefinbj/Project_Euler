from math import *

def firstpan(n):
    p = str(n)
    if len(p) < 10:
        return False
    digs = ['1','2','3','4','5','6','7','8','9']
    fdigs = sorted(p[:9])
    return fdigs == digs

def lastpan(n):
    p = str(n)
    if len(p) < 10:
        return False
    digs = ['1','2','3','4','5','6','7','8','9']
    fdigs = sorted(p[-9:])
    return fdigs == digs

fibs = {}

fibs[1] = 1
fibs[2] = 1

def comp(k):
    fib = fibs[k-1] + fibs[k-2]
    fibs[k] = fib
    return fib

##for k in range(3,1000000):
##    if k % 100000 == 0:
##        print k
##    fib = comp(k)
##    if firstpan(fib):
##        print 'Front matches: ' + str(k)
##    if lastpan(fib):
##        print 'Back matches: ' + str(k)
##    if firstpan(fib) and lastpan(fib):
##        print 'Whoopee: ' + str(k)
##        break

phi = (1+sqrt(5))/2

def logfib(n):
    return n*log(phi,10)-log(sqrt(5),10)

def first(lfib):
    med = lfib - int(lfib)
    
