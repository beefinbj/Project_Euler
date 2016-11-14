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

ps = primes(1000000)

LIMIT = 1000000

def using_sieve():
    totients = [n for n in xrange(0, LIMIT+1)]
    totients[0] = totients[1] = 0

    for p in ps:
        for n in xrange(p, LIMIT+1, p):
            totients[n] = totients[n] * (p-1) / p
    return sum(totients)

def p072():
    # return using_totient()
    # return using_generation()
    return using_sieve()

print p072()
