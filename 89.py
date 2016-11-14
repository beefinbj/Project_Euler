def romlen(n):
    out = 0
    out += n/1000
    rem = n % 1000
    if rem >= 900:
        out += 2
        rem = rem-900
    elif rem >= 500:
        out += 1
        rem = rem-500
    elif rem >= 400:
        out += 2
        rem = rem - 400
    out += rem/100
    rem = rem % 100
    if rem >= 90:
        out += 2
        rem = rem-90
    elif rem >= 50:
        out += 1
        rem = rem-50
    elif rem >= 40:
        out += 2
        rem = rem-40
    out += rem/10
    rem = rem % 10
    if rem == 9:
        out += 2
        rem = 0
    elif rem >= 5:
        out += 1
        rem = rem-5
    elif rem == 4:
        out += 2
        rem = 0
    out += rem
    rem = 0
    return out

def romtodig(string):
    if string == '':
        return 0
    tot = 0
    curr = 0
    while curr < len(string):
        if string[curr] == 'M':
            tot += 1000
            curr += 1
        else:
            break
    if curr < len(string)-1:
        if string[curr] == 'C' and string[curr+1] == 'M':
            tot += 900
            curr += 2
    while curr < len(string):
        if string[curr] == 'D':
            tot += 500
            curr += 1
        else:
            break
    if curr < len(string)-1:
        if string[curr] == 'C' and string[curr+1] == 'D':
            tot += 400
            curr += 2
    while curr < len(string):
        if string[curr] == 'C':
            tot += 100
            curr += 1
        else:
            break
    if curr < len(string)-1:
        if string[curr] == 'X' and string[curr+1] == 'C':
            tot += 90
            curr += 2
    while curr < len(string):
        if string[curr] == 'L':
            tot += 50
            curr += 1
        else:
            break
    if curr < len(string)-1:
        if string[curr] == 'X' and string[curr+1] == 'L':
            tot += 40
            curr += 2
    while curr < len(string):
        if string[curr] == 'X':
            tot += 10
            curr += 1
        else:
            break
    if curr < len(string)-1:
        if string[curr] == 'I' and string[curr+1] == 'X':
            tot += 9
            curr += 2
    while curr < len(string):
        if string[curr] == 'V':
            tot += 5
            curr += 1
        else:
            break
    if curr < len(string)-1:
        if string[curr] == 'I' and string[curr+1] == 'V':
            tot += 4
            curr += 2
    while curr < len(string):
        if string[curr] == 'I':
            tot += 1
            curr += 1
        else:
            break
    return tot

f = open('roman.txt','r')

old = 0
new = 0

for line in f:
    old += len(line)-1
    num = romtodig(line)
    new += romlen(num)

old += 1
print 'Old: ' + str(old)
print 'New: ' + str(new)
print 'Diff: ' + str(old-new)
