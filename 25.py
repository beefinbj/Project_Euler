initial = [0,1,2,3,4,5,6,7,8,9]
output = []
index = 1000000
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
print factorial(9)
print factorial(len(initial)-1)
while len(initial) > 0:
    pick = index/factorial(len(initial)-1)
    output.append(initial[pick])
    index = index - pick*factorial(len(initial)-1)
    initial.pop(pick)
    print output
