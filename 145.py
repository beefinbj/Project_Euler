leadsums = {}

for i in range(19):
    leadsums[i] = 0

for i in range(1,10):
    for j in range(1,10):
        leadsums[i+j] += 1

sums = {}

for i in range(19):
    sums[i] = 0

for i in range(10):
    for j in range(10):
        sums[i+j] += 1

headsingleeven = leadsums[0]+leadsums[2]+leadsums[4]+leadsums[6]+leadsums[8]
headsingleodd = leadsums[1]+leadsums[3]+leadsums[5]+leadsums[7]+leadsums[9]
headdoubleodd = leadsums[11]+leadsums[13]+leadsums[15]+leadsums[17]
headdoubleeven = leadsums[10]+leadsums[12]+leadsums[14]+leadsums[16]+leadsums[18]

midsingleeven = sums[2]+sums[0]+sums[4]+sums[6]+sums[8]
midsingleodd = sums[1]+sums[3]+sums[5]+sums[7]+sums[9]
middoubleeven = sums[10]+sums[12]+sums[14]+sums[16]+sums[18]
middoubleodd = sums[11]+sums[13]+sums[15]+sums[17]

repsingleeven = 5
repdoubleeven = 5

dig2 = headsingleodd
dig3 = headdoubleodd*repsingleeven
dig4 = headsingleodd*midsingleodd
dig6 = dig4*midsingleodd
dig8 = dig6*midsingleodd
dig7 = headdoubleodd*repsingleeven*middoubleodd*midsingleeven

def hit(n):
    k = str(n)
    for r in k:
        if r == '2':
            return False
        if r == '0':
            return False
        if r == '4':
            return False
        if r == '6':
            return False
        if r == '8':
            return False
    return True

##count = 0
##
##check = {}
##for i in range(1000000,10000000):
##    check[i] = False
##
##for i in range(1000000,10000000):
##    a = i
##    b = int(''.join(reversed(str(i))))
##    c = a+b
##    d = str(c)
##    if b/100000>0:
##        if hit(d) and check[i] == False:
##            check[i] = True
####            print 'A: ' + str(a)
####            print 'B: ' + str(b)
####            print 'Sum: ' + d
##            count += 1

print dig2+dig3+dig4+dig6+dig7+dig8
