# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:44:24 2016

@author: Angus
"""

import random

def roll_pete():
    score = 0
    for i in range(9):
        k = random.randint(1,4)
        score += k
    return score

def roll_colin():
    score = 0
    for i in range(6):
        k = random.randint(1,6)
        score += k
    return score

trials = 10000000

counter = 0
for i in range(trials):
    pscore = roll_pete()
    cscore = roll_colin()
    if pscore > cscore:
        counter += 1

print counter/float(trials)