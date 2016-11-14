with open('p054_poker.txt') as f:
    contests = f.readlines()

def number(num):
    return {
        'A': 14,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
    }[num]

class Card(object):
    def __init__(self,value,suit):
        self.suit = suit
        self.num = number(value)

class Hand(object):
    def __init__(self,cards):
        self.hand = [cards]
        self.numbers = [card.num for card in cards]
        self.suits = [card.suit for card in cards]

def triple(hand):
    for val in hand.numbers:
        if hand.numbers.count(val) == 3:
            return True
    return False

def pair(hand):
    for val in hand.numbers:
        if hand.numbers.count(val) == 2:
            return True
    return False

def two_pair(hand):
    if len(set(hand.numbers)) == 3:
        return pair(hand)
    return False
    

def flush(hand):
    if len(set(hand.suits)) == 1:
        return True
    else:
        return False

def straight(hand):
    seq = sorted(hand.numbers)
    if seq[0]+1 == seq[1] and seq[1]+1 == seq[2] and seq[2]+1 == seq[3] and seq[3]+1 == seq[4]:
        return True
    elif seq[0] == 14 and seq[1:] == [2,3,4,5]:
        return True
    return False

def full_house(hand):
    return triple(hand) and pair(hand)

def four_kind(hand):
    seq = sorted(hand.numbers)
    if seq[0] == seq[1] and seq[1] == seq[2] and seq[2] == seq[3]:
        return True
    elif seq[1] == seq[2] and seq[2] == seq[3] and seq[3] == seq[4]:
        return True
    return False

def eval_strength(hand):
    strength = 0
    if straight(hand) and flush(hand):
        strength = 90
        nums = sorted(hand.numbers,reverse=True)
#        if (14 in hand.numbers) and (nums[0] == 2):
#            nums = [5,4,3,2,1]
        for i in range(5):
            strength += nums[i]/(100.0**(i+1))
    elif four_kind(hand):
        print 'Four of a kind: ' + str(hand.numbers)
        strength = 80
        nums = sorted(hand.numbers)
        if hand.numbers.count(nums[0]) == 4:
            strength += nums[0]/100.0
        elif hand.numbers.count(nums[4]) == 4:
            strength += nums[4]/100.0
        else:
            raise(Exception)
    elif full_house(hand):
        print 'Full House: ' + str(hand.numbers)
        strength = 70
        nums = sorted(hand.numbers)
        if hand.numbers.count(nums[0]) == 3:
            strength += nums[0]/100.0
        elif hand.numbers.count(nums[4]) == 3:
            strength += nums[4]/100.0
        else:
            raise(Exception)
    elif flush(hand) and (not straight(hand)):
        strength = 60
        nums = sorted(hand.numbers,reverse=True)
        for i in range(5):
            strength += nums[i]/(100.0**(i+1))
    elif straight(hand) and (not flush(hand)):
        print 'Straight: ' + str(hand.numbers)
        strength = 50
        nums = sorted(hand.numbers,reverse=True)
#        if (14 in hand.numbers) and (nums[0] == 2):
#            nums = [5,4,3,2,1]
        for i in range(5):
            strength += nums[i]/(100.0**(i+1))            
    elif triple(hand) and (not full_house(hand)):
        print 'Triple: ' + str(hand.numbers)
        strength = 40
        nums = sorted(hand.numbers,reverse=True)
        for i in range(5):
            if nums.count(nums[i]) == 3:
                strength += nums[i]/100.0
                repped = nums[i]
                break
        nums[:] = [x for x in nums if x != repped]
        for i in range(2):
            strength += nums[i]/(100.0**(i+2))
    elif two_pair(hand):
        strength = 30
        repped = []
        nums = sorted(hand.numbers,reverse=True)
        for i in range(5):
            if nums.count(nums[i]) == 2:
                strength += nums[i]/100.0
                repped.append(nums[i])
        nums[:] = [x for x in nums if x != repped]
        strength += nums[0]/(100.0**(i+2))
    elif pair(hand):
        strength = 20
        nums = sorted(hand.numbers,reverse=True)
        for i in range(5):
            if nums.count(nums[i]) == 2:
                strength += nums[i]/100.0
                repped = nums[i]
                break
        nums[:] = [x for x in nums if x != repped]
        for i in range(3):
            strength += nums[i]/(100.0**(i+2))
    else:
        strength = 10
        nums = sorted(hand.numbers,reverse=True)
        for i in range(5):
            strength += nums[i]/(100.0**(i+1))
    return strength

def one_wins(hand1,hand2):
    return eval_strength(hand1) > eval_strength(hand2)

def solve(contests):
    counter = 0
    for contest in contests:
        cardArray = []
        for i in range(10):
            card = Card(contest[i*3],contest[i*3+1])
            cardArray.append(card)
        hand_1 = Hand(cardArray[:5])
        hand_2 = Hand(cardArray[5:])
        if one_wins(hand_1,hand_2):
            counter += 1
    return counter

cards1 = [Card('2','S'),Card('9','S'),Card('8','S'),Card('4','C'),Card('8','C'),]
handtest1 = Hand(cards1)
cards2 = [Card('3','D'),Card('6','H'),Card('Q','D'),Card('7','C'),Card('7','H')]
handtest2 = Hand(cards2)


print solve(contests)