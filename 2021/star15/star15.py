import re
from collections import Counter

f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('') 
f.close()

HEIGHT = len(lines)
WIDTH = len(lines[0])

print("{}x{}".format(WIDTH,HEIGHT))
y=0
risk = {}
for line in lines:
    for x in range(WIDTH):
        risk[(x,y)] = int(line[x])
    y += 1

for tx in range(5):
    for ty in range(5):
        if tx==0 and ty==0:
            continue
        for x in range(WIDTH):
            for y in range(HEIGHT):
                v = risk[(x,y)] + tx + ty
                if v > 9: 
                    v -= 9
                risk[(tx*WIDTH+x,ty*HEIGHT+y)] = v

def neighbors(x,y,w,h):
    n = []
    if x>0:
        n.append((x-1,y)) 
    if x<w:
        n.append((x+1,y)) 
    if y>0:
        n.append((x,y-1)) 
    if y<h:
        n.append((x,y+1)) 

    return n

def find_path(w,h):
    DONE = {}
    COMPUTED = {}
   
    COMPUTED[(0,0)]=0
    POOL = {(0,0)}

    while True:
        if (w, h) in DONE.keys():
            break
        
        min_val = -1
        min_k = (0,0)
        for k in POOL:
            if min_val == -1 or COMPUTED[k] < min_val:
                min_val = COMPUTED[k]
                min_k = k

        for n in neighbors(min_k[0], min_k[1], w, h):
            if n in COMPUTED.keys():
                COMPUTED[n] = min(COMPUTED[n], COMPUTED[min_k]+risk[n])
            else:
                COMPUTED[n] = COMPUTED[min_k]+risk[n]
                POOL.add(n)
                
        DONE[min_k] = COMPUTED[min_k]
        POOL.remove(min_k)
            
    return(DONE[w,h])

def part1():
    return find_path(WIDTH-1, HEIGHT-1)
    
def part2():
    return find_path(5*WIDTH-1, 5*HEIGHT-1)
    
print("Solution part1 is {}".format(part1()))
print("Solution part2 is {}".format(part2()))
