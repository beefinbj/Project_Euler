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

primelist = primes(8000)

revprimes = reversed(primelist)

tot = 0

winners = {}

fr_ind = 0

while primelist[fr_ind]**4 <= 50000000:
    cb_ind = 0
    while primelist[cb_ind]**3 <= 50000000-primelist[fr_ind]**4:
        sq_ind = 0
        subcount = 0
        while primelist[fr_ind]**4+primelist[cb_ind]**3+primelist[sq_ind]**2 <= 50000000:
            try:
                x = winners[primelist[fr_ind]**4+primelist[cb_ind]**3+primelist[sq_ind]**2]
            except KeyError:
                winners[primelist[fr_ind]**4+primelist[cb_ind]**3+primelist[sq_ind]**2] = True
                subcount += 1
            sq_ind += 1
            if sq_ind == len(primelist):
                print 'Done'
                break
        tot += subcount
        cb_ind += 1
        if cb_ind == len(primelist):
            break
    fr_ind += 1
    if fr_ind == len(primelist):
        break

print tot
