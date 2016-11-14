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

primelist = primes(1000000)

def rots(n):
    output = []
    prev = str(n)
    output.append(int(prev))
    for i in range(len(prev)-1):
        rot = prev[1:]+prev[0]
        output.append(int(rot))
        prev = rot
    return output

def even(n):
    if '2' in str(n):
        return True
    if '4' in str(n):
        return True
    if '6' in str(n):
        return True
    if '8' in str(n):
        return True
    if '0' in str(n):
        return True
    if '5' in str(n):
        return True
    return False

def circ(rots):
    for rotation in rots:
        if (rotation in primelist) == False:
            return False
    return True

winners = []

for i in primelist:
    if even(i) == False:
        rota = rots(i)
        if circ(rota) == True:
            winners.append(i)

print winners
