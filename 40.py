output = ''

num = 1

while len(output) < 1000000:
    output = output + str(num)
    num += 1

print output[0]
print output[9]
print output[99]
print output[999]
print output[9999]
print output[99999]
print output[999999]
