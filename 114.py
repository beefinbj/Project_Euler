data = {}
data[0] = 1
data[1] = 1
data[2] = 1
data[3] = 2
data[4] = 4
data[5] = 7
data[6] = 11
data[7] = 17

for i in range(7,51):
    base = data[i-1]+1
    remright = i-4
    while remright >= 0:
        base += data[remright]
        remright += -1
    data[i] = base

print data[50]
