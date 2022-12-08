#/bin/env python3
import numpy as np

with open("input.txt", "r") as f:
    MAP = np.array([list(line.strip()) for line in f.readlines()], int)

VIS = np.zeros((len(MAP), len(MAP[0])), int)

def get_visible_map():
    global MAP

    v_map = np.zeros((len(MAP), len(MAP[0])), int)
    for y in range(len(MAP)):
        prev = -1
        for x in range(len(MAP[0])):
            if MAP[y][x] > prev:
                v_map[y][x] = 1

            prev = max(MAP[y][x], prev)

    return v_map

for _ in range(4):
    VIS |= get_visible_map()
    MAP = np.rot90(MAP, k=1, axes=(0,1))
    VIS = np.rot90(VIS, k=1, axes=(0,1))

print(f"Soution part1 is {np.sum(VIS)}")
