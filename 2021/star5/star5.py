import re
from collections import Counter

f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

def resolve(algo):
    hydro=[]
    for l in lines:
        m = re.match(r'^(\d+),(\d+) -> (\d+),(\d+)$', l)
        if not m:
            print("Invalid line {}".format(l))
            exit(1)

        x1 = int(m.group(1))
        y1 = int(m.group(2))
        x2 = int(m.group(3))
        y2 = int(m.group(4))

        if (x1==x2) or (y1==y2):
            for x in range(min(x1,x2), max(x1,x2)+1):
                for y in range(min(y1,y2), max(y1,y2)+1):
                    hydro.append((x,y))

        elif algo==2:
            xstep = 1 if x2 > x1 else -1
            ystep = 1 if y2 > y1 else -1
            y=y1
            for x in range(x1, x2+xstep, xstep):
                hydro.append((x,y))
                y += ystep

    counts = Counter(hydro)
    return len([t for t in counts.keys() if counts[t]>1])

res1 = resolve(1)
print("Soution part1 is {}".format(res1))

res2 = resolve(2)
print("Soution part2 is {}".format(res2))
