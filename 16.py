def solve():
    power = 1
    digs = 1
    first_dig = 1
    while power <= 10:
        first_dig = first_dig * 2
        if first_dig > 9:
            first_dig = 1
            digs = digs*2-9
        else:
            digs = digs*2
        print "Power: " + str(power)
        print "First dig: " + str(first_dig)
        print "Digs: " + str(digs)
        power += 1
    return digs

def altsolve():
    power = 7
    digs = 11
    while power <= 1000:
        digs = digs*2-9
        power += 1
    return digs


print altsolve()
