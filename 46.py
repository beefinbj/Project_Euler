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
	return [x for x in s if x]

primelist = primes(10000)

def success(odd):
    index = 0
    while primelist[index] <= odd:
        a = odd-primelist[index]
        b = a/2
        if int(sqrt(b)) == sqrt(b):
            return True
        index += 1
    return False

num = 9
while success(num) == True:
    num += 2
    while (num in primelist) == True:
        num += 2

print num
