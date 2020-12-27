import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()

N = []
D = []
max_len = len(lines)
for l in lines:
    N.append(int(l))
N.append(max(N)+3)
N.sort()

def part1():
    p = 0
    deltas = { 1:0, 2:0, 3:0}
    for n in N:
        d = n-p
        if d == 0 or d>3:
            print("invalid set for {} {}".format(n,p))
        deltas[d] += 1
        D.append(d)
        p=n
    print(deltas)
    print(D)
    return deltas[1]*deltas[3]

def count_combinations(s, l):
    if l == 1:
        return 1
    else:
        if s == 2:
            return count_combinations(0, l-1)
        else:
            return count_combinations(0, l-1) + count_combinations(s+1, l-1)

def part2():
    l = 0
    c = 1
    for d in D:
        if d == 3:
            if l>0:
                print("compute combinations for seq {}".format(l))
                r = count_combinations(0, l)
                c *= r
                print("combination seq {} res {} total {}".format(l, r, c))
                l = 0
        else:
            l += 1
    return c

res1 = part1()
print("solution is {}".format(res1))

res2 = part2()
print("solution is {}".format(res2))

