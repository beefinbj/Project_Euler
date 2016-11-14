from math import *

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def good(n):
    if n >= 1000000:
        return False
    return primedict[n]

primelist = primes(2500000)

primedict = {}
for i in range(2500000):
    primedict[i] = False
for prime in primelist:
    primedict[prime] = True

def test(a,b):
    n = 0
    while primedict[abs(n**2+a*n+b)] and n**2+a*n+b > 0:
        n += 1
    return n-1

maxn = 0
maxa = 0
maxb = 0

for b in range(1,1000):
    for a in range(1000):
        if test(a,b) > maxn:
            maxn = test(a,b)
            maxa = a
            maxb = b

print maxa
print maxb

for b in range(1,1000):
    for a in range(-b,0):
        if test(a,b) > maxn:
            maxn = test(a,b)
            maxa = a
            maxb = b

print maxa
print maxb
