def test_fifth(n):
    string = str(n)
    total = 0
    for char in string:
        total += int(char)**5
    if total == n:
        return True
    return False

def solve():
    output = []
    for n in range(5000000):
        if n%1000000 == 0:
            print 'Fifth'
        if test_fifth(n) == True:
            output.append(n)
    print output
    return output

solve()
