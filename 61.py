from math import *

toCheck = [3,4,5,6,7]

i = 19

LIMIT = 59

def tri(n):
    return (-1+sqrt(1+8*n))/2

def squ(n):
    return sqrt(n)

def pen(n):
    return (1+sqrt(1+24*n))/6

def hxe(n):
    return (1+sqrt(1+8*n))/4

def hep(n):
    return (3+sqrt(9+40*n))/10

def interval(dim,lo,hi):
    if dim == 3:
        a = tri(lo)
        b = tri(hi)
    elif dim == 4:
        a = squ(lo)
        b = squ(hi)
    elif dim == 5:
        a = pen(lo)
        b = pen(hi)
    elif dim == 6:
        a = hxe(lo)
        b = hxe(hi)
    elif dim == 7:
        a = hep(lo)
        b = hep(hi)
    if (int(b)-int(a)) > 0:
        print 'Successful Interval: ' + str(dim)
        return dim
    else:
        return 0

def getnext(dim,lo,hi):
    if dim == 3:
        n = int(tri(lo))+1
        return n*(n+1)/2
    elif dim == 4:
        n = int(squ(lo))+1
        return n*n
    elif dim == 5:
        n = int(pen(lo))+1
        return n*(3*n-1)/2
    elif dim == 6:
        n = int(hxe(lo))+1
        return n*(2*n-1)
    elif dim == 7:
        n = int(hep(lo))+1
        return n*(5*n-3)/2

def iterate(dims,latest,initial):
    if int(str(latest)[2:]) < 10:
        return False
    if len(dims) == 1:
        lo = int(str(latest)[2:])*100
        hi = (int(str(latest)[2:])+1)*100
        if interval(dims[0],lo,hi) == 0:
            return False
        else:
            iteration = getnext(dims[0],lo,hi)
            return str(iteration)[2:] == str(initial)[:2]
    else:
        for i in range(len(dims)):
            lo = int(str(latest)[2:])*100
            hi = (int(str(latest)[2:])+1)*100
            if interval(dims[i],lo,hi) > 0:
                iteration = getnext(dims[i],lo,hi)
                rem = dims[:i]+dims[i+1:]
                if iterate(rem,iteration,initial):
                    return True
        return False

while i < LIMIT:
    test = i*(3*i-2)
    print 'Testing: ' + str(test)
    if iterate(toCheck,test,test):
        print test
        print 'Yay!'
        break
    i += 1

print 'Done runnning'
