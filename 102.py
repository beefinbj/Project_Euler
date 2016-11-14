def cross(x1,y1,x2,y2):
    if x1 == x2:
        return -2000
    intercept = float(y2-y1)/float(x2-x1)*(-1*x1)+y1
    if (intercept >= y2 and intercept <= y1) or (intercept >= y1 and intercept <= y2):
        return intercept
    else:
        return -2000

def cont(x1,y1,x2,y2,x3,y3):
    cept1 = cross(x1,y1,x2,y2)
    cept2 = cross(x1,y1,x3,y3)
    cept3 = cross(x2,y2,x3,y3)
    if (cept1 >= 0) and ((cept2 <= 0 and cept2 >= -1000) or (cept3 <= 0 and cept3 >= -1000)):
        return True
    elif (cept2 >= 0) and ((cept1 <= 0 and cept1 >= -1000) or (cept3 <= 0 and cept3 >= -1000)):
        return True
    elif (cept3 >= 0) and ((cept2 <= 0 and cept2 >= -1000) or (cept1 <= 0 and cept1 >= -1000)):
        return True
    return False

f = open('triangles.txt','r')

count = 0

for line in f:
    line = line.rstrip()
    nums = []
    start = 0
    run = 0
    while len(nums) < 5:
        while line[run] != ',':
            run += 1
        nums.append(int(line[start:run]))
        start = run+1
        run = start
    nums.append(int(line[start:]))
    if cont(nums[0],nums[1],nums[2],nums[3],nums[4],nums[5]):
        count += 1

print count
