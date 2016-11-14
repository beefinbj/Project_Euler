ones = [1]
eightynines = [89]

dicts = {}

for i in range(1,10000000):
    dicts[i] = None

dicts[1] = False
dicts[89] = True

print 'Done'

def iterate(n):
    output = 0
    for digit in str(n):
        output += int(digit)**2
    return output

def check(n):
    if dicts[n] == False:
        return False
    elif dicts[n] == True:
        return True
    else:
        return check(iterate(n))


counter = 0

for i in range(1,10000000):
    if i % 1000000 == 0:
        print 'Million'
    if check(i):
        dicts[i] = True
        counter += 1
    else:
        dicts[i] = False

print counter
