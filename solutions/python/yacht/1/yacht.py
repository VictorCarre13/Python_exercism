# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return dice.count(category)*category
    if category==YACHT:
        yacht=True
        for index in range(1, len(dice)):
            if dice[index]!=dice[index-1]:
                yacht=False
        if yacht:
            return 50
        return 0
    if category==FOUR_OF_A_KIND:
        for index in range(0, len(dice)):
            if dice.count(dice[index])>=4:
               return dice[index]*4
        return 0
    if category==CHOICE:
        return sum(dice)
    if category==BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        return 0
    if category==LITTLE_STRAIGHT:
        if sorted(dice)==[1, 2, 3, 4, 5]:
            return 30
        return 0
    if category==FULL_HOUSE:
        three=False
        two= False
        for index in range(0, len(dice)):
            if dice.count(dice[index])==3:
               three=True
            if dice.count(dice[index])==2:
               two=True
        if three and two:
            return sum(dice)
        return 0
    
    
    