from itertools import permutations

winners = []

perms = [''.join(p) for p in permutations('0123456789')]
for perm in perms:
    if int(perm[1:4]) % 2 == 0:
        if int(perm[2:5]) % 3 == 0:
            if int(perm[3:6]) % 5 == 0:
                if int(perm[4:7]) % 7 == 0:
                    if int(perm[5:8]) % 11 == 0:
                        if int(perm[6:9]) % 13 == 0:
                            if int(perm[7:]) % 17 == 0:
                                winners.append(perm)

tot = 0

for number in winners:
    tot += int(number)
