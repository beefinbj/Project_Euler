from math import *

data = {}

for i in range(1,601):
    for j in range(1,601):
        data[(i,j)] = 0

data[(1,1)] = 1
data[(1,2)] = 3
data[(2,1)] = 3
data[(2,2)] = 9


def count(l,w):
    if data[(l,w)] != 0:
        return data[(l,w)]
    elif l == 1:
        data[(l,w)] = w*(w+1)/2
        data[(w,l)] = w*(w+1)/2
        return w*(w+1)/2
    elif w == 1:
        data[(l,w)] = l*(l+1)/2
        data[(w,l)] = l*(l+1)/2
        return l*(l+1)/2
    else:
        orig = data[(l-1,w)]
        new = l*w*(w+1)/2
        data[(l,w)] = orig + new
        data[(w,l)] = orig + new
        return orig + new

bestdif = 2000000
bestl = 0
bestw = 0

for i in range(1,601):
    res = count(1,i)
    if (abs(res-2000000) < bestdif) == True:
        bestdif = abs(res-2000000)
        bestl = 1
        bestw = i

for i in range(2,601):
    for j in range(2,601):
        res = count(i,j)
        if (abs(res-2000000) < bestdif) == True:
            bestdif = abs(res-2000000)
            bestl = i
            bestw = j
