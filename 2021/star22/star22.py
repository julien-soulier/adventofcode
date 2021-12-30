import re

f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('') 
f.close()

def part1():
    ON = set()
    for line in lines:
        m = re.match(r'^(?P<action>on|off)\s+x=(?P<x0>-?\d+)\.\.(?P<x1>-?\d+),y=(?P<y0>-?\d+)\.\.(?P<y1>-?\d+),z=(?P<z0>-?\d+)\.\.(?P<z1>-?\d+)$', line)
        if m:
            x0 = max(-50, int(m.group('x0')))
            x1 = min(50, int(m.group('x1')))
            y0 = max(-50, int(m.group('y0')))
            y1 = min(50, int(m.group('y1')))
            z0 = max(-50, int(m.group('z0')))
            z1 = min(50, int(m.group('z1')))

            if x1>x0 and y1>y0 and z1>z0:
                cubes = {(x,y,z) for x in range(x0,x1+1) for y in range(y0,y1+1) for z in range(z0, z1+1)}
        
                if m['action'] == 'on':
                    ON = ON.union(cubes)
                else:
                    ON.difference_update(cubes)

    return len(ON)

def part2():
    ON = set()
    i = 0
    for line in lines:
        m = re.match(r'^(?P<action>on|off)\s+x=(?P<x0>-?\d+)\.\.(?P<x1>-?\d+),y=(?P<y0>-?\d+)\.\.(?P<y1>-?\d+),z=(?P<z0>-?\d+)\.\.(?P<z1>-?\d+)$', line)
        if m:
            x0 = int(m.group('x0'))
            x1 = int(m.group('x1'))
            y0 = int(m.group('y0'))
            y1 = int(m.group('y1'))
            z0 = int(m.group('z0'))
            z1 = int(m.group('z1'))

            cubes = {(x,y,z) for x in range(x0,x1+1) for y in range(y0,y1+1) for z in range(z0, z1+1)}
        
            if m['action'] == 'on':
                ON = ON.union(cubes)
            else:
                ON.difference_update(cubes)
        i += 1
        print(i)
    return len(ON)

print("Solution part1 is {}".format(part1()))
print("Solution part2 is {}".format(part2()))
