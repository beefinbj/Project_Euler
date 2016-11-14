total = 1
n = 2
i = 3

def sumloop(start,width):
    return start+start+width+start+2*width+start+3*width

while n < 1001:
    total += sumloop(i,n)
    temp = i + 3*n
    n += 2
    i = temp + n
print total
