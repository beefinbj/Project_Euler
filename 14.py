def chain_length(n,numlen,lennum):
    if n in numlen:
        return numlen[n]
    else:
        if n%2 == 0:
            numlen[n] = chain_length(n/2,numlen,lennum)+1
            lennum[numlen[n]] = n
            return numlen[n]
        else:
            numlen[n] = chain_length(3*n+1,numlen,lennum)+1
            lennum[numlen[n]] = n
            return numlen[n]

def solve():
    numlen = {}
    numlen[1] = 1
    lennum = {}
    lennum[1] = 1
    for i in range(1,1000000):
        chain_length(i,numlen,lennum)
    return lennum[max(lennum.keys())]

print solve()
