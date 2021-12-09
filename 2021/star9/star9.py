f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

HEIGHT = len(lines)
WIDTH = len(lines[0])

height_map=[]
height_map.append([9]*(WIDTH+2))
for l in lines:
    l = '9' + l + '9'
    height_map.append(list(map(int, list(l))))
height_map.append([9]*(WIDTH+2))

low_points = []
def part1():
    total = 0
    for y in range(1,HEIGHT+1):
        for x in range(1, WIDTH+1):
            if height_map[y][x]<height_map[y][x-1] and height_map[y][x]<height_map[y][x+1] and height_map[y][x]<height_map[y-1][x] and height_map[y][x]<height_map[y+1][x]:
                low_points.append((x,y))
                total += height_map[y][x]+1
    return total

def grow_basin(basin, x,y):
    if height_map[y][x]==9:
        return basin

    basin.add((x,y))
    if height_map[y][x]<height_map[y][x+1]:
        basin = grow_basin(basin, x+1, y)

    if height_map[y][x]<height_map[y][x-1]:
        basin = grow_basin(basin, x-1, y)

    if height_map[y][x]<height_map[y+1][x]:
        basin = grow_basin(basin, x, y+1)

    if height_map[y][x]<height_map[y-1][x]:
        basin = grow_basin(basin, x, y-1)

    return basin


def part2():
    basins = []
    for coord in low_points:
        basin = set()
        basin = grow_basin(basin, coord[0], coord[1])
        basins.append(len(basin))

    basins.sort(reverse=True)
    return basins[0]*basins[1]*basins[2]

res1 = part1()
print("Soution part1 is {}".format(res1))

res2 = part2()
print("Soution part2 is {}".format(res2))