ceil = 49382716

digits = ['1','2','3','4','5','6','7','8','9']

def find_pan(integer):
    tracker = ''
    index = 1
    while sorted(tracker) != digits and len(tracker) < 10:
        tracker = tracker + str(integer*index)
        index += 1
    if len(tracker) >= 10:
        return 0
    return tracker

for i in range(ceil+1):
    if find_pan(i) > 0:
        print i
        print find_pan(i)
