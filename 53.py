factdict = {}

factdict[1] = 1
factdict[0] = 1

for i in range(2,101):
    factdict[i] = factdict[i-1]*i

counter = 0

for n in range(1,101):
    for r in range(0,n+1):
        if float(factdict[n])/(factdict[r]*factdict[n-r]) > 1000000:
            counter += 1

print counter
