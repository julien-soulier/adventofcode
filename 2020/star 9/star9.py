import re
import string

f = open("input.txt", "r")

N = []
lines = f.readlines()
max_len = len(lines)
for l in lines:
    N.append(int(l))


def find_contiguous(idx, tgt):
    sum = 0
    i = idx
    while sum < tgt and i<max_len:
        sum += N[i]
        i += 1

    if sum == tgt:
        return i - idx
    else:
        return 0

def is_valid(idx):
    for i in range(idx-25, idx):
        for j in range(i+1, idx):
            if N[j] != N[i] and N[j]+N[i]==N[idx]:
                return True
    return False

def part1():
    for idx in range(25,max_len):
        if not is_valid(idx):
            return N[idx]
    
    return 0

def part2(tgt):
    for idx in range(max_len):
        l = find_contiguous(idx, tgt)
        if l>0:
            mi = min(N[idx:idx+l])
            ma = max(N[idx:idx+l])
            print("found contiguous: {} - {}".format(idx, idx+l-1))
            return mi, ma

res = part1()
print("Part1 {}".format(res))

mi, ma = part2(res)
print("Part2 {}+{}={}".format(mi, ma, mi+ma))

f.close()
