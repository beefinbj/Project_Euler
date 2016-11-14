from fractions import *

klist = [2,1,2]

for i in range(4,101):
    if i%3 != 0:
        klist.append(1)
    else:
        klist.append(i/3*2)

num = klist[98]*klist[99]+1
den = klist[99]

for i in range(97,-1,-1):
    old_num = num
    old_den = den
    num = old_num*klist[i] + old_den
    den = old_num

print num

answer = 0

for dig in str(num):
    answer += int(dig)

print answer
