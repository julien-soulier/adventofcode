#!/bin/env python3

from collections import Counter

CARD_VALUE = {'A':1, 'K': 2, 'Q':3, 'J':4, 'T':5, '9':6, '8':7, '7':8, '6':9, '5':10, '4':11, '3':12, '2':13}
CARD_VALUE_JOKER = {'A':1, 'K': 2, 'Q':3, 'T':4, '9':5, '8':6, '7':7, '6':8, '5':9, '4':10, '3':11, '2':12, 'J':13}
HAND_VALUE = {'FIVE':1, 'FOUR':2, 'FULL': 3, 'THREE':4, 'TWO_PAIRS':5, 'ONE_PAIR':6, 'ONE':7}

def get_hands(fname):
    with open(fname, "r") as f:
        for l in f:
            m = l.split()
            hand = {}
            hand['cards']=m[0]
            hand['bid']=int(m[1])
            yield hand

def score_hand(cards, with_joker=False):
    cnt = Counter(cards)
    cmn = cnt.most_common()
    most1 = cmn[0][1]
    if with_joker:
        if cmn[0][0]=='J':
            # if 5 'J' there is no cmn[1]
            if len(cmn)>1:
                most1 += cmn[1][1]
        else:
            most1 += cards.count('J')

    if most1 == 5:
        hand = 'FIVE'
    elif most1 == 4:
        hand = 'FOUR'
    elif most1 == 3:      
        most2 = cmn[1][1] if not with_joker or (cmn[1][0] != 'J' and cmn[0][0] != 'J') else cmn[2][1]
        hand = 'FULL' if most2 == 2 else 'THREE'
    elif most1 == 2:
        most2 = cmn[1][1] if not with_joker or (cmn[1][0] != 'J' and cmn[0][0] != 'J') else cmn[2][1]
        hand = 'TWO_PAIRS' if most2 == 2 else 'ONE_PAIR'
    else:
        hand = 'ONE'           

    return HAND_VALUE[hand]

def process_input(fname, part=1):
    if part==1:
        hands = sorted(get_hands(fname), key=lambda h: (score_hand(h['cards']), CARD_VALUE[h['cards'][0]], CARD_VALUE[h['cards'][1]], CARD_VALUE[h['cards'][2]], CARD_VALUE[h['cards'][3]], CARD_VALUE[h['cards'][4]]), reverse=True)
    else:
        hands = sorted(get_hands(fname), key=lambda h: (score_hand(h['cards'], with_joker=True), CARD_VALUE_JOKER[h['cards'][0]], CARD_VALUE_JOKER[h['cards'][1]], CARD_VALUE_JOKER[h['cards'][2]], CARD_VALUE_JOKER[h['cards'][3]], CARD_VALUE_JOKER[h['cards'][4]]), reverse=True)

    for i,h in enumerate(hands):
#        print(f"{i} -> {h}")
        yield h['bid']*(i+1)

print(f"The answer for part1 is {sum(process_input(fname='input_7.txt'))}")
print(f"The answer for part2 is {sum(process_input(fname='input_7.txt', part=2))}")
    