import copy

# to simplify count positions from 0 to 9
# read values manually from input.txt
init_pos= [9, 3]

roll_count = 0
last_dice = -1
def roll_dice():
    global roll_count
    global last_dice
    roll_count += 1
    last_dice = (last_dice + 1) % 100
    return last_dice + 1

def part1():
    score = [0,0]
    player = 0
    pos = init_pos.copy()
    while True:
        v = 0
        for _ in range(3):
            v += roll_dice()
        pos[player] = (pos[player] + v) % 10
        score[player] += pos[player] + 1
        if score[player] >= 1000:
            break
        player = 1 - player
    
    return score[1-player]*roll_count

def part2():
    wins = [0,0]
    sums = [1,1]

    # store the number of universes per score per player
    V0 = {}
    for score in range(21):
        V0[score] = {}
        for pos in range(10):
            V0[score][pos] = 0

    V = {}
    V[0] = copy.deepcopy(V0)
    V[0][0][init_pos[0]] = 1
    
    V[1] = copy.deepcopy(V0)
    V[1][0][init_pos[1]] = 1

    dirac_dice = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
    player = 0
    U = {}
    while min(sums)>0:
        U[player] = copy.deepcopy(V0)

        for score in range(21):
            for pos in range(10):
                u = V[player][score][pos] 
                if u>0:
                    for dice in dirac_dice.keys():
                        new_pos = (pos + dice) % 10
                        new_score = score + new_pos + 1
                        if new_score >= 21:
                            wins[player] += u * dirac_dice[dice] * sums[1-player]
                        else:
                            U[player][new_score][new_pos] += u * dirac_dice[dice]

        v=0
        for score in range(21):
            v += sum(U[player][score].values())
        sums[player] = v

        V[player] = U[player]

        player = 1 - player

    return max(wins)

print("Solution part1 is {}".format(part1()))
print("Solution part2 is {}".format(part2()))
