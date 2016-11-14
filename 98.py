from math import *
from itertools import permutations

def permute(n):
    return [int(''.join(p)) for p in permutations(str(n))]

def pandig(a):
    tots = list(str(a))
    digs = ['1','2','3','4','5','6','7','8','9']
    sotots = sorted(tots)
    return sotots == digs

words = open("words2.txt",'r',0)

words2 = []
for line in words:
    words2.append(line.strip().lower())

wordstring = words2[0]
wordlist = []
start = 0
while start < len(wordstring):
    if wordstring[start] != ',' and wordstring[start] != '"':
        end = start
        while wordstring[end] != '"':
            end += 1
        wordlist.append(wordstring[start:end])
        start = end
    start += 1

print "Done"

anagrams = {}

for word in wordlist:
    if ''.join(sorted(word)) in anagrams.keys():
        anagrams[''.join(sorted(word))].append(word)
    else:
        anagrams[''.join(sorted(word))] = [word]

print "Sorted"

for ana in anagrams.keys():
    if len(anagrams[ana]) <= 1:
        del anagrams[ana]

print "Cleaned"


tots = []

for perm in anagrams.values():
    tots += perm

ninedigs = 
