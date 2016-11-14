from math import *

perims = {}

for p in range(1001):
    perims[p] = []

for i in range(1,500):
    for j in range(1,500):
        if int(sqrt(i**2+j**2)) == sqrt(i**2+j**2) and i+j+sqrt(i**2+j**2) <= 1000:
            perims[i+j+sqrt(i**2+j**2)].append([i,j,sqrt(i**2+j**2)])

maxlen = 0
maxtot = 0

for per in perims.keys():
    if len(perims[per]) > 0:
        print per
        print perims[per]
    if len(perims[per]) > maxlen:
        maxlen = len(perims[per])
        maxtot = per

print maxtot
print perims[maxtot]
