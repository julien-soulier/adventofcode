f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()


def part1():
    SCORE={'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
    return sum(map(lambda x: SCORE[x], lines))

def part2():
    SCORE={'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
    return sum(map(lambda x: SCORE[x], lines))

print("Soution part1 is {}".format(part1()))
print("Soution part2 is {}".format(part2()))
