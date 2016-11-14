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

primelist = primes(1000000)

maxlen = 0
maxp = 0

primedict = {}
for i in range(1000000):
    primedict[i] = False
for prime in primelist:
    primedict[prime] = True

for i in range(len(primelist)):
    for j in range(i+1,len(primelist)):
        if good(sum(primelist[i:j+1])) and j-i > maxlen:
            maxlen = j-i
            maxp = sum(primelist[i:j+1])
            print 'Sum start: ' + str(primelist[i])
            print 'Sum end: ' + str(primelist[j])
            print 'Sum length: ' + str(j-i)
            print 'Sum: ' + str(sum(primelist[i:j+1]))

