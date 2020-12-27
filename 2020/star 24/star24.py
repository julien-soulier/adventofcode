import re
import string
import operator

f = open("input.txt", "r")
lines = f.read().split('\n')
f.close()

mvt = {'e': (-2,0), 'ne': (-1,1), 'se': (-1,-1), 'w': (2,0), 'nw': (1,1), 'sw': (1,-1)}
q = re.compile('|'.join(mvt.keys()))
tiles = {}
for line in lines:
    if len(line) == 0:
        continue

    coord = (0,0)
    for m in q.finditer(line):
        coord = tuple(map(operator.add, coord, mvt[m.group(0)]))
    if coord in tiles.keys():
        tiles[coord] = 1 - tiles[coord]
    else:
        tiles[coord] = 1

res1 = sum(tiles.values())
print("solution part 1: {}".format(res1))
    

def get_tiles_area():
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    for coord in tiles.keys():
        xmin = min(xmin, coord[0])
        xmax = max(xmax, coord[0])
        ymin = min(ymin, coord[1])
        ymax = max(ymax, coord[1])
    xmin -= 2
    xmax += 2
    ymin -= 2
    ymax += 2
    return xmin, xmax, ymin, ymax


def count_adjacent_black_tiles(local_tiles, coord):
    count = 0
    for m in mvt.values():
        tile_key = tuple(map(operator.add, coord, m))
        if tile_key in local_tiles.keys():
            count += local_tiles[tile_key] 
    return count

def process_one_day():
    prev_tiles = tiles.copy()
    xmin, xmax, ymin, ymax = get_tiles_area()
    tile_key_list =  [(x,y) for x in range(xmin, xmax+1) for y in range(ymin,ymax+1)]
    for tile_key in tile_key_list:
        c = count_adjacent_black_tiles(prev_tiles, tile_key)
        if tile_key in prev_tiles and prev_tiles[tile_key]==1:
            if c==0 or c>2:
                tiles[tile_key] = 0
        else:
            if c==2:
                tiles[tile_key] = 1
    
def process_multiple_days(count):
    for i in range(count):
        process_one_day()
        print("day {}".format(i))

process_multiple_days(100)
res2 = sum(tiles.values())
print("solution part 2: {}".format(res2))