def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

out = list(str(factorial(100)))
print sum([int(i) for i in out])

