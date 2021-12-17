import re
from bitstring import ConstBitStream

f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('') 
f.close()

m = re.match(r'^target area: x=(\d+)\.\.(\d+), y=-(\d+)\.\.-(\d+)', lines[0])
if m:
    xmin = int(m.group(1))
    xmax = int(m.group(2))
    ymin = int(m.group(3))
    ymax = int(m.group(4))
    print('{} {} {} {}'.format(m.group(1), m.group(2), m.group(3), m.group(4)))

def hit_target(vx, vy):
    x = 0
    y = 0
    while True:
        if vx == 0 and x<xmin:
            return 0
        
        if x>xmax or y<-ymin:
            return 0

        if x>=xmin and x<=xmax and y>=-ymin and y<=-ymax:
            return 1

        x += vx
        y += vy

        vx = max(vx-1,0)
        vy -= 1

# Whatever VY, the Y position will come back to 0 with a negative speed = -(VY+1)
# To hit the target with the maximum height, this VY+1 must be equal to YMIN
def part1():
    return ((ymin-1)*ymin)//2

def part2():
    count = 0
    for vy in range(-ymin, ymin+1):
        for vx in range(0, xmax+1):
            count += hit_target(vx, vy)
    return count

print("Solution part1 is {}".format(part1()))
print("Solution part2 is {}".format(part2()))
