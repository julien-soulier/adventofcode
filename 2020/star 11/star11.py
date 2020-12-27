import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()

directions = [(-1 , -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

max_r = len(lines)
max_c = len(lines[0])-1
print("grid is {}x{}".format(max_c, max_r))
seats = {}
seats[0] = []
for l in lines:
    seats[0].append(l.rstrip("\n"))

def inside(r, c):
    if r>=0 and r<max_r and c>=0 and c<max_c:
        return True
    else:
        return False

def count_neigbours_part1(i, r, c):
    s=0
    for dr, dc in directions:
        if inside(r+dr, c+dc):
            if seats[i][r+dr][c+dc] == '#':
                s+=1
    return s

def count_neigbours(algo, i, r, c):
    s=0
    for dr, dc in directions:
        go = True
        k = 0
        while go:
            k += 1
            if inside(r+k*dr, c+k*dc):
                if seats[i][r+k*dr][c+k*dc]=='L':
                    go = False
                elif seats[i][r+k*dr][c+k*dc]=='#':
                    go = False
                    s += 1
            else:
                go = False

            if algo == 1:
                go = False

    return s

def count_total_occupied(i):
    s = 0
    for r in seats[i]:
        for c in range(max_c):
            if r[c] == '#':
                s += 1
    return s

def fill_grid(algo, threshold):
    mvt = True
    i = 0
    while mvt:
        mvt = False
        j=i+1
        seats[j] = []
        for r in range(max_r):
            row = ""
            for c in range(max_c):
                if seats[i][r][c] == '.':
                    row += '.'
                elif seats[i][r][c] == 'L':
                    if count_neigbours(algo, i, r, c) == 0:
                        row += '#'
                        mvt = True
                    else:
                        row += 'L'
                else:
                    if count_neigbours(algo, i, r, c) >= threshold:
                        mvt = True
                        row += 'L'
                    else:
                        row += '#'
            seats[j].append(row)
        i+=1
    
    return count_total_occupied(i-1)

res1 = fill_grid(1, 4)
print("solution is {}".format(res1))

res2 = fill_grid(2, 5)
print("solution is {}".format(res2))

