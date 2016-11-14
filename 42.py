from math import *

words = open("words.txt",'r',0)
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

def code(word):
    summ = 0
    for letter in word:
        summ += (ord(letter)-96)
    return summ
    
def tri(n):
    return int((-1+sqrt(1+8*n))/2) == (-1+sqrt(1+8*n))/2

winners = []

for word in wordlist:
    if tri(code(word)) == True:
        winners.append(word)

print winners
