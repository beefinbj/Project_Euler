from math import *

def ispent(n):
    return int((1+sqrt(1+24*n))/6) == (1+sqrt(1+24*n))/6

pents = [n*(3*n-1)/2 for n in range(1,10000)]

for i in range(len(pents)):
    for j in range(i+1,len(pents)):
        if ispent(pents[i]+pents[j]) and ispent(pents[j]-pents[i]):
            print pents[i],pents[j]
