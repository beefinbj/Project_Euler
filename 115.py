data = {}

for j in range(50):
    data[j] = 1

for k in range(50,101):
    r = k-49
    count = r*(r+1)/2+1
    data[k] = count

p = 100

while data[p] < 1000000:
    p += 1
    base = data[p-1]+1
    remright = p-51
    while remright >= 0:
        base += data[remright]
        remright += -1
    data[p] = base


print p
