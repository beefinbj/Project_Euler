from itertools import permutations

start = 1

cubedict = {}

cubes = []

##for i in range(500**3):
##    cubedict[i] = False
##
##for i in range(500):
##    cubedict[i**3] = True

for i in range(10000):
    cubes.append(i**3)

for i in range(10000):
    if (''.join(sorted(str(i**3))) in cubedict.keys()) == False:
        cubedict[''.join(sorted(str(i**3)))] = [str(i**3)]
    else:
        cubedict[''.join(sorted(str(i**3)))].append(str(i**3))

def permute(n):
    return [int(''.join(p)) for p in permutations(str(n))]

def success(base):
    cube = base**3
    perms = permute(cube)
    counter = 0
    for num in perms:
        if (num in cubes) == True:
            counter += 1
    if counter == 5:
        return True
    return False

for sortedcube in cubedict.keys():
    if len(cubedict[sortedcube]) == 5:
        print sortedcube
        print cubedict[sortedcube]
print 'Ended'
