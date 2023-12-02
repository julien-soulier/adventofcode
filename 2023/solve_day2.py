#!/bin/env python3

import re

MAX_CUBE={'red': 12, 'green': 13, 'blue': 14}

def get_picks(game_str):
    for round in game_str.split(";"):
        for cube in round.split(","):
            m = re.match(r'(\d+) (red|green|blue)', cube.strip())
            if not m:
                raise RuntimeError(f"Bad cube pick {cube}")

            cnt = int(m.group(1))
            color = m.group(2)
            yield {'color': color, 'cnt': int(cnt)}

def pick_is_valid(pick):
    return True if pick['cnt'] <= MAX_CUBE[pick['color']] else False

def game_is_valid(game_str):
    for pick in get_picks(game_str):
        if not pick_is_valid(pick):
            return False
    return True

def game_power(game_str):
    max_cnt = {'red': 0, 'green': 0, 'blue': 0}
    for pick in get_picks(game_str):
        max_cnt[pick['color']] = max(pick['cnt'], max_cnt[pick['color']])

    return max_cnt['red']*max_cnt['green']*max_cnt['blue']

def process_input(fname="input_2.txt", part=1):
    with open(fname, "r") as f:
        for l in f:
            tokens = l.split(":")
            m = re.match(r'Game (\d+)', tokens[0])
            if not m:
                raise RuntimeError(f"Bad game id {tokens[0]}")
            
            game_id = int(m.group(1))
            game_picks = tokens[1].strip()
            if part==1 and game_is_valid(game_picks):
                yield game_id
            if part==2:
                yield game_power(game_picks)

print(f"The total calibration part1 is {sum(process_input(part=1))}")
print(f"The total calibration part2 is {sum(process_input(part=2))}")
    