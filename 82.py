
file = open('matrix.txt','r')

def linetolist(line):
    out = []
    start = 0
    end = start
    while start < len(line):
        while line[end] != ',':
            end += 1
            if end >= len(line):
                break
        out.append(int(line[start:end]))
        start = end+1
        end = start
    return out

matrix = []
for line in file:
    matrix.append(linetolist(line))

##matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

n = 80

output = [[0 for i in range(n)] for j in range(n)]

def fix(row,col):
    curr = row-1
    currcost = output[curr][col]
    downcost = output[curr+1][col]+matrix[curr][col]
    while currcost >= downcost and curr >= 0:
        output[curr][col] = downcost
        curr = curr-1
        currcost = output[curr][col]
        downcost = output[curr+1][col]+matrix[curr][col]

##output[0][n-1] = matrix[0][n-1]
##
##for col in range(n-2,-1,-1):
##    output[0][col] = output[0][col+1]+matrix[0][col]
##
##for row in range(1,n):
##    output[row][n-1] = matrix[row][n-1]
##    for col in range(n-2,-1,-1):
##        new = matrix[row][col]
##        rightcost = output[row][col+1]
##        upcost = output[row-1][col]
##        if upcost <= rightcost:
##            output[row][col] = upcost + new
##        else:
##            output[row][col] = rightcost + new
##        fix(row,col)


def altfix(row,col):
    curr = row-1
    down = output[curr+1][col]
    currcost = output[curr][col]-matrix[curr][col]
    while (curr >= 0) and down <= currcost:
        output[curr][col] = down + matrix[curr][col]
        curr = curr-1
        down = output[curr+1][col]
        currcost = output[curr][col]-matrix[curr][col]

for i in range(n):
    output[i][n-1] = matrix[i][n-1]

for col in range(n-2,-1,-1):
    for row in range(n):
        if row == 0:
            output[row][col] = matrix[row][col] + output[row][col+1]
        else:
            up = output[row-1][col]
            right = output[row][col+1]
            output[row][col] = matrix[row][col]+min([up,right])
        altfix(row,col)

starts = []

for i in range(80):
    starts.append(output[i][0])

print min(starts)
