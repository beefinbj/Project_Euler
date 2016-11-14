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

primelist = primes(10000000)

primedict = {}
for i in range(10000000):
    primedict[i] = False
for prime in primelist:
    primedict[prime] = True

print 'Done'

def even(n):
    if '4' in str(n):
        return True
    if '6' in str(n):
        return True
    if '8' in str(n):
        return True
    if '0' in str(n):
        return True
    return False

def truncprime(n):
    string = str(n)
    for i in range(len(string)):
        if primedict[int(string[i:])] == False:
            return False
        if string[:-1*i]!= '' and primedict[int(string[:-1*i])] == False:
            return False
    return True

start = 4

while start < len(primelist):
    if even(primelist[start]) == False:
        if truncprime(primelist[start]):
            print primelist[start]
    start += 1
