def dynamicFib():
    fibs = [1,1]
    while len(str(fibs[-1]))<1000:
        fibs.append(fibs[-1]+fibs[-2])
    return len(fibs)

print dynamicFib()
