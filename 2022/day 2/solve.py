#/bin/env python3

def get_score(SCORE):
    with open("input.txt", "r") as f:
        return sum(SCORE[x] for x in f.read().splitlines())

SCORE1={'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
SCORE2={'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}

print(f"Soution part1 is {get_score(SCORE1)}")
print(f"Soution part2 is {get_score(SCORE2)}")
