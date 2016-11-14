names = open("names.txt",'r',0)
names2 = []
for line in names:
    names2.append(line.strip().lower())

namestring = names2[0]
namelist = []
start = 0
while start < len(namestring):
    if namestring[start] != ',' and namestring[start] != '"':
        end = start
        while namestring[end] != '"':
            end += 1
        namelist.append(namestring[start:end])
        start = end
    start += 1

print "Done"

def merge(leftArray, rightArray):
    result = []
    LIndex, RIndex = 0, 0
    while LIndex < len(leftArray) and RIndex < len(rightArray):
        if leftArray[LIndex] < rightArray[RIndex]:
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
    if len(array) <= 1:
        return array
    mid = len(array)/2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left,right)

def compute_score(name):
    score = 0
    for char in name:
        score += ord(char)-96
    return score

sortednames = merge_sort(namelist)
scorelist = []
for i in range(len(sortednames)):
    scorelist.append(compute_score(sortednames[i])*(i+1))
print sum(scorelist)
