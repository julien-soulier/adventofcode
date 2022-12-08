#/bin/env python3
import numpy as np

with open("input.txt", "r") as f:
    MAP = np.array([list(line.strip()) for line in f.readlines()], int)

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

def get_scenic_map():
    global MAP

    s_map = np.zeros((len(MAP), len(MAP[0])), int)
    for y in range(len(MAP)):
        for x in range(len(MAP[0])):
            count = 0
            for z in range(x+1, len(MAP[0])):
                count += 1
                if MAP[y][z] >= MAP[y][x]:
                    break
            s_map[y][x] = count

    return s_map

VIS = np.zeros((len(MAP), len(MAP[0])), int)
for _ in range(4):
    VIS |= get_visible_map()
    MAP = np.rot90(MAP, k=1, axes=(0,1))
    VIS = np.rot90(VIS, k=1, axes=(0,1))

SCE = np.ones((len(MAP), len(MAP[0])), int)
for _ in range(4):
    SCE *= get_scenic_map()
    MAP = np.rot90(MAP, k=1, axes=(0,1))
    SCE = np.rot90(SCE, k=1, axes=(0,1))

print(f"Soution part1 is {np.sum(VIS)}")
print(f"Soution part2 is {np.max(SCE)}")
