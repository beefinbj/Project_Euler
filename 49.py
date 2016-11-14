from itertools import permutations

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

def permute(n):
    return [int(''.join(p)) for p in permutations(str(n))]

def seq(nums):
    return ((max(nums)-min(nums))/2 in nums)

def seqexists(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if (nums[i] != nums[j]) and ((nums[j] + (nums[j]-nums[i]) in nums) == True):
                return True
    return False

primelist = primes(10000)

for i in range(len(primelist)):
    if len(str(primelist[i])) == 4:
        bigprimes = primelist[i:]
        break

primeperms = {}

for i in range(len(bigprimes)):
    primetest = bigprimes[i]
    if primeperms.has_key(''.join(sorted(str(primetest)))) == False:
        primeperms[''.join(sorted(str(primetest)))] = []
    perms = permute(primetest)
    for number in perms:
        if (number in bigprimes) and ((number in primeperms[''.join(sorted(str(primetest)))]) == False):
            primeperms[''.join(sorted(str(primetest)))].append(number)

allperms = primeperms.keys()

for perm in allperms:
    if len(primeperms[perm]) < 4:
        del primeperms[perm]

cands = primeperms.keys()

winners = []

for candidate in cands:
    candlist = primeperms[candidate]
    if seqexists(candlist) == True:
        winners += candlist
print winners
