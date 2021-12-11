f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

grid = {}
y=0
for line in lines:
    x=0
    for c in line:
        grid[(x,y)]=int(c)
        x+=1
    y+=1

def valid_coordinate(coord):
    def valid(c):
        return True if c>=0 and c<10 else False

    return valid(coord[0]) and valid(coord[1]) 

def neighboors(coord):
    x = coord[0]
    y = coord[1]
    n = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    return list(filter(valid_coordinate, n))

def do_one_step():
    for c in grid.keys():
        grid[c] += 1

    flashed = []
    count = 0
    prev_count = -1

    while (count > prev_count):
        prev_count = count
        for c,l in grid.items():
            if l>9 and c not in flashed:
                flashed.append(c)
                count += 1
                for n in neighboors(c):
                    grid[n] += 1
    
    for f in flashed:
        grid[f] = 0

    return count

def part1():
    count = 0
    for step in range(100):
        count += do_one_step()

    return count
    
def part2():
    step = 101
    while do_one_step() < 100:
        step +=1

    return step

print("Solution part1 is {}".format(part1()))

print("Solution part2 is {}".format(part2()))
