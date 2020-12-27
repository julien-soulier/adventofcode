import re
import string
import math

init_round_cups = [6,5,3,4,2,7,9,1,8]
CUPS_COUNT = 1000000

def init_linked_list(round_cups):
    round_cups_ll = []
    for i in range(len(round_cups)+1):
        round_cups_ll.append({})
    
    for i in range(0,len(round_cups)-1):
        idx = round_cups[i]
        round_cups_ll[idx]['next'] = round_cups[i+1]
    
    last_cup = round_cups[-1]
    round_cups_ll[last_cup]['next'] = round_cups[0]
    
    return round_cups_ll

def show_cups(round_cups_ll, start, count):
    cup = start
    for i in range(count):
        print(round_cups_ll[cup], end='')
        cup = round_cups_ll[cup]['next']
    print()

def play_one_round(round_cups):
    removed_cups=round_cups[1:4]
    del round_cups[1:4]
    dest_cup = round_cups[0]
    while True:
        dest_cup -= 1
        if dest_cup==0:
            dest_cup = 9
        if dest_cup in round_cups:
            dest_cup_idx = round_cups.index(dest_cup)+1
            break
    round_cups[dest_cup_idx:dest_cup_idx] = removed_cups
    round_cups.append(round_cups.pop(0))

def play_game(round_cups, round_count):
    for i in range(round_count):
        play_one_round(round_cups)
        print(round_cups)

def get_result_1(round_cups):
    one_idx = round_cups.index(1)
    tmp = round_cups[0:one_idx]
    del round_cups[0:one_idx]
    round_cups.extend(tmp)
    return ''.join(map(str, round_cups[1:]))

def play_one_round_ll(curt_cup):
    removed_cups = []
    next_cup = round_cups_ll[curt_cup]['next']
    for i in range(3):
        removed_cups.append(next_cup)
        next_cup = round_cups_ll[next_cup]['next']

    round_cups_ll[curt_cup]['next'] = next_cup

    dest_cup = curt_cup-1
    while True:
        if dest_cup==0:
            dest_cup = CUPS_COUNT
        if dest_cup not in removed_cups:
            break
        dest_cup -= 1
    
    next_cup = round_cups_ll[dest_cup]['next']
    round_cups_ll[dest_cup]['next'] = removed_cups[0]
    round_cups_ll[removed_cups[-1]]['next'] = next_cup

    return round_cups_ll[curt_cup]['next']        


def play_game_ll(count):
    curt_cup = init_round_cups[0]
    step = count // 100
    percent = 0
    for i in range(count):
        curt_cup = play_one_round_ll(curt_cup)
        if i%step == 0:
            percent+=1
            print('{}%'.format(percent))

round_cups = init_round_cups.copy()
print(round_cups)
play_game(round_cups, 100)

res1 = get_result_1(round_cups)
print("solution part 1: {}".format(res1))

init_round_cups.extend([*range(10,CUPS_COUNT+1)])
round_cups_ll = init_linked_list(init_round_cups)
show_cups(round_cups_ll, init_round_cups[0], 10)
play_game_ll(10000000)
show_cups(round_cups_ll, init_round_cups[0], 10)
star1_cup = round_cups_ll[1]['next']
star2_cup = round_cups_ll[star1_cup]['next']
res2 = star1_cup * star2_cup
print("solution part 2: {}".format(res2))