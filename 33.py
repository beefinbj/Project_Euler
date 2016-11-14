def has0(n):
    return '0' in str(n)

def sharedig(i,j):
    for dig in str(i):
        if str(j)[0] == dig or str(j)[1] == dig:
            return True
    return False

def success(i,j):
    denom = str(i)
    numer = str(j)
    if denom[0] == numer[0]:
        if float(numer[1])/int(denom[1]) == float(j)/i:
            return True
    if denom[0] == numer[1]:
        if float(numer[0])/int(denom[1]) == float(j)/i:
            return True
    if denom[1] == numer[1]:
        if float(numer[0])/int(denom[0]) == float(j)/i:
            return True
    if denom[1] == numer[0]:
        if float(numer[1])/int(denom[0]) == float(j)/i:
            return True
    return False

winners = []

print success(11,11)
print success(98,49)
print success(51,10)

for i in range(11,100):
    if has0(i) == False:
        for j in range(11,i):
            if has0(j) == False:
                if sharedig(i,j):
                    if success(i,j):
                        winners.append([i,j])

print winners
