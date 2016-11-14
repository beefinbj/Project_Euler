divisors = {}

for i in range(1,28123):
    divs = [1]
    for j in range(2,int(i**(0.5))+1):
        if i % j == 0:
            if j*j == i:
                divs = divs + [j]
            else:
                divs = divs + [j, i/j]
    divisors[i] = divs

sumdivs = {}

for i in range(1,28123):
    sumdivs[i] = sum(divisors[i])

abundants = []
for key in sumdivs.keys():
    if sumdivs[key] > key:
        abundants.append(key)

def merge(leftArray, rightArray):
    result = []
    LIndex, RIndex = 0, 0
    while LIndex < len(leftArray) and RIndex < len(rightArray):
        if leftArray[LIndex] <= rightArray[RIndex]:
            result.append(leftArray[LIndex])
            LIndex += 1
        else:
            result.append(rightArray[RIndex])
            RIndex += 1
    if LIndex < len(leftArray):
        result = result + leftArray[LIndex:]
    if RIndex < len(rightArray):
        result = result + rightArray[RIndex:]
    return result

def merge_sort(array):
    """merge_sort: int array -> int array
    Purpose: Sort the input array of integers in descending order using the merge sort algorithm
    Consumes: an array of integers
    Produces: an array of integers sorted in descending order
    Example: merge_sort([4,5,1,3,2]) -> [5,4,3,2,1]
    """
    if len(array) <= 1:
        return array
    mid = len(array)/2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left,right)

sortedabs = merge_sort(abundants)
print "Found abs"

bank = {}

for i in range(28123):
    bank[i] = True

for i in range(len(sortedabs)):
    for j in range(i,len(sortedabs)):
        if sortedabs[i]+sortedabs[j] < 28123:
            if bank[sortedabs[i]+sortedabs[j]] == True:
                bank[sortedabs[i]+sortedabs[j]] = False

total = 0

for num in bank.keys():
    if bank[num] == True:
        total += num

print total

def binsearch(num,array):
    if len(array) == 0:
        return False
    if len(array) == 1:
        return array[0] == num
    mid = len(array)/2
    if num == array[mid]:
        return True
    elif num < array[mid]:
        return binsearch(num,array[:mid])
    else:
        return binsearch(num,array[mid:])

def cansum(number,sortedlist):
    i = 0
    while sortedlist[i] < number:
        rem = number-sortedlist[i]
        if binsearch(rem,sortedlist) == True:
            return True
        i += 1
    return False
