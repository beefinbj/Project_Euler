# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Unencrypted characters are in range [97,122]
#ASCII values from 1 to 255

import re
from collections import defaultdict

txt = open('p059_cipher.txt').read()
chars = re.split(",|\n",txt)
del chars[-1]

dict1 = defaultdict(int)
dict2 = defaultdict(int)
dict3 = defaultdict(int)

for i in range(len(chars)):
    if i%3 == 1:
        dict1[chars[i]] += 1
    elif i%3 == 2:
        dict2[chars[i]] += 1
    else:
        dict3[chars[i]] += 1

max1count = 0
for key in dict1.keys():
    if dict1[key] > max1count:
        max1char = key
        max1count = dict1[key]

max2count = 0
for key in dict2.keys():
    if dict2[key] > max2count:
        max2char = key
        max2count = dict2[key]

max3count = 0
for key in dict3.keys():
    if dict3[key] > max3count:
        max3char = key
        max3count = dict3[key]

code1 = []
code2 = []
code3 = []

for i in range(len(chars)):
    if i%3 == 1:
        code1.append(int(chars[i]))
    elif i%3 == 2:
        code2.append(int(chars[i]))
    else:
        code3.append(int(chars[i]))
        
key1 = []
#Find the first key
for k1 in range(1,256):
    for ind in range(len(code1)):
        if (int(code1[ind])^k1) not in range(32,123):
            break
        elif ind == len(code1)-1:
            key1.append(k1)

key2 = []
#Find the second key
for k2 in range(1,256):
    for ind in range(len(code2)):
        if (int(code2[ind])^k2) not in range(32,123):
            break
        elif ind == len(code2)-1:
            key2.append(k2)

key3 = []
#Find the third key
for k3 in range(1,256):
    for ind in range(len(code3)):
        if (int(code3[ind])^k3) not in range(32,123):
            break
        elif ind == len(code3)-1:
            key3.append(k3)
for i in range(len(code1)):
    code1[i] = chr(int(code1[i])^key1[2])
for i in range(len(code2)):
    code2[i] = chr(int(code2[i])^key2[0])
for i in range(len(code3)):
    code3[i] = chr(int(code3[i])^key3[1])

output = []
for i in range(len(chars)):
    if i%3 == 1:
        output.append(code1[(i-1)/3])
    elif i%3 == 2:
        output.append(code2[(i-2)/3])
    else:
        output.append(code3[i/3])

sum(map(ord,output))
outString = ''
for ch in output:
    outString = outString+ch