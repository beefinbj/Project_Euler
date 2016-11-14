divisors = {}

for i in range(1,10000):
    divs = [1]
    for j in range(2,int(i**(0.5))+1):
        if i % j == 0:
            if j*j == i:
                divs = divs + [j]
            else:
                divs = divs + [j, i/j]
    divisors[i] = divs

sumdivs = {}

for i in range(1,10000):
    sumdivs[i] = sum(divisors[i])

amicables = []
for key in sumdivs.keys():
    if sumdivs[key] < 10000:
        if key == sumdivs[sumdivs[key]] and key != sumdivs[key]:
            amicables = amicables + [key]

print sum(amicables)
