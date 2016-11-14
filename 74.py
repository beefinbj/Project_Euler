facs = {}

facs[0] = 1
facs[1] = 1
facs[2] = 2
facs[3] = 6
facs[4] = 24

for i in range(5,10):
    facs[i] = facs[i-1]*i

nums = {}

for i in range(1,4000001):
    nums[i] = 100

def iterate(n):
    string = str(n)
    new = 0
    for dig in string:
        new += facs[int(dig)]
    return new

def loop(n):
    new = iterate(n)
    newvals = []
    while nums[new] == 100 and new != n and ((new in newvals) == False):
        newvals.append(new)
        new = iterate(new)
    if new == n:
        nums[n] = len(newvals)+1
        for num in newvals:
            nums[num] = len(newvals)+1
    elif (new in newvals) == True:
        nums[n] = len(newvals)+1
        for i in range(len(newvals)):
            if newvals[i] == new:
                break
        for j in range(i,len(newvals)):
            nums[newvals[j]] = len(newvals)-i
        for k in range(i):
            nums[newvals[k]] = len(newvals)-k
    else:
        nums[n] = len(newvals)+1+nums[new]
        for i in range(len(newvals)):
            nums[newvals[i]] = nums[new]+len(newvals)-i
    return nums[n]

count = 0

for f in range(1,1000000):
    if nums[f] == 100:
        if loop(f) == 60:
            count += 1
            print 'Found: ' + str(f)
