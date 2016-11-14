sumdict = {}
sumdict[0] = 1

for n in range(1,101):
    sumdict[n] = 0

for add in range(1,101):
    for fill in range(add,101):
        sumdict[fill] = sumdict[fill]+sumdict[fill-add]

print sumdict[100]
