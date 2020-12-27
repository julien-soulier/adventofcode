import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()

ts = int(lines[0])
bus_line = lines[1].rstrip('\n')
bus_sched = bus_line.split(',')
ids = list(filter(lambda x: x != 'x', bus_sched))
ids = list(map(int, ids)) 

def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    while b!=0:
        a,b=b,a%b
    return a

def ppcm(a,b):
    """ppcm(a,b): calcul du 'Plus Petit Commun Multiple' entre 2 nombres entiers a et b"""
    return (a*b)//pgcd(a,b)

def part1():
    wt = {}
    for id in ids:
        w = id - (ts % id)
        wt[id] = w
    min_id = min(wt, key=wt.get)
    delay = wt[min_id]
    return min_id*delay

def part2():
    start = 0
    inc = 1
    for id in ids:
        pos = bus_sched.index(str(id))
        while (start + pos) % id != 0:
            start += inc
        inc = ppcm(inc, id)
        
    return start

res1 = part1()
print("solution is {}".format(res1))

res2 = part2()
print("solution is {}".format(res2))

