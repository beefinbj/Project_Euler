def sumdig(numstring):
    output = 0
    for dig in numstring:
        output += int(dig)
    return output

maxsum = 0

for a in range(1,100):
    for b in range(1,100):
        if sumdig(str(a**b)) > maxsum:
            maxsum = sumdig(str(a**b))

print maxsum
