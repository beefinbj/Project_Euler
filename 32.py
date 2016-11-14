def test_pandig(a,b,c):
    tots = list(str(a)+str(b)+str(c))
    digs = ['1','2','3','4','5','6','7','8','9']
    sotots = sorted(tots)
    if sotots == digs:
        print a
        print b
        print c
        print "Found"
    return sotots == digs

winners = []
            
for i in range(1,10000):
    for j in range(2,int(i**(0.5))+1):
        if i % j == 0:
            if test_pandig(i,j,i/j) == True:
                winners.append(i)

print winners
