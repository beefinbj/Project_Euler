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

primelist = primes(1000000)
data = {}

def numfacs(n):
    if n in data:
        return data[n]
    rem = n
    index = 0
    count = 0
    while rem != 1:
        if rem % primelist[index] == 0:
            count += 1
            while rem % primelist[index] == 0:
                rem = rem/primelist[index]
        index += 1
    data[n] = count
    return count

def success(i):
    first = numfacs(i)
    second = numfacs(i+1)
    third = numfacs(i+2)
    fourth = numfacs(i+3)
    if first == 4 and second == 4 and third == 4 and fourth == 4:
        return True
    return False

for i in range(3,1000000-4):
    if i%20000 == 0:
            print i
    if success(i):
        print data
        break
