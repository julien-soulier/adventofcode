import re
import string
import math

f = open("input.txt", "r")
lines = f.read().split('\n')
f.close()

tiles = {}
TILE_SIZE = len(lines[1])
REAL_SIZE = TILE_SIZE - 2
DESC_SIZE = TILE_SIZE + 2
TILE_COUNT = (len(lines)+1)//DESC_SIZE
IMAGE_SIZE = int(math.sqrt(TILE_COUNT))
WIDTH = IMAGE_SIZE * REAL_SIZE

print('{} {} {}'.format(TILE_SIZE, DESC_SIZE, TILE_COUNT))

def get_value(s):
    translation = s.maketrans('#.', '01')
    s = s.translate(translation)
    return int(s, base=2)

for i in range(TILE_COUNT):
    m = re.match(r'^Tile (\d+):$', lines[i*DESC_SIZE])
    if m:
        id = int(m.group(1))
    else:
        print("Cannot parse tile id {}: {}".format(i, lines[i*DESC_SIZE]))
        break

    row0 = lines[i*DESC_SIZE+1]
    row1 = lines[i*DESC_SIZE+TILE_SIZE]
    col0 = ''
    col1 = ''
    for j in range(TILE_SIZE):
        col0 += lines[i*DESC_SIZE+1+j][0]
        col1 += lines[i*DESC_SIZE+1+j][-1]
    tile = {}
    tile['sides'] = []
    tile['sides'].append(get_value(row0))
    tile['sides'].append(get_value(row1))
    tile['sides'].append(get_value(col0))
    tile['sides'].append(get_value(col1))
    tile['sides'].append(get_value(row0[::-1]))
    tile['sides'].append(get_value(row1[::-1]))
    tile['sides'].append(get_value(col0[::-1]))
    tile['sides'].append(get_value(col1[::-1]))
    tile['content'] = []
    for j in range(2,TILE_SIZE-1):
        tile['content'].append(lines[i*DESC_SIZE+j][1:-1])
    tile['used'] = False
    tile['index'] = i
    tiles[id] = tile

def count_matching_sides(tile_id):
    count = 0
    for s in range(4):
        for k in tiles.keys():
            if k != tile_id and tiles[tile_id]['sides'][s] in tiles[k]['sides']:
                count += 1
                break
    return count

def get_matching_tile(id, side):
    res = 0,0
    count = 0
    for k in tiles.keys():
        if k==id or tiles[k]['used']:
            continue

        try:
            m = tiles[k]['sides'].index(tiles[id]['sides'][side])
        except:
            pass
        else:
            count += 1
            res = k,m
    if count > 1:
        print("several options for {} {}".format(id, side))

    return res

corners = []
def part1():
    res = 1
    for id in tiles.keys():
        c = count_matching_sides(id)
        if c==2:
            print("found corner {}".format(id))
            res *= int(id)
            corners.append(id)
    return res

opposite_side = [1, 0, 3, 2, 5, 4, 7, 6]
adjacent_side = [3, 7, 1, 5, 2, 6, 0, 4]
image = []
for y in range(IMAGE_SIZE):
    image.append([])
    for x in range(IMAGE_SIZE):
        image[y].append({})

def construct_image():
    image[0][0]['id'] = corners[0]
    image[0][0]['right'] = 3
    image[0][0]['bottom'] = 1

    for y in range(IMAGE_SIZE):
        #print(image)
        for x in range(IMAGE_SIZE-1):
            tile_id,side = get_matching_tile(image[x][y]['id'], image[x][y]['right'])
            if tile_id==0:
                print("error. Cannot find next HZ tile @{}x{} for {}->{}".format(x,y,image[x][y]['id'], image[x][y]['right']))
                return
            print('H: {}:{} -> {}:{}'.format(image[x][y]['id'], image[x][y]['right'], side, tile_id))
            tiles[tile_id]['used'] = True
            image[x+1][y]['id'] = tile_id
            image[x+1][y]['right'] = opposite_side[side]

        if y<IMAGE_SIZE-1:
            tile_id,side = get_matching_tile(image[0][y]['id'], image[0][y]['bottom'])
            if tile_id==0:
                print("error. Cannot find next VT tile {} {}".format(x,y))
                return
            print('V: {}:{} -> {}:{}'.format(image[0][y]['id'], image[0][y]['bottom'], side, tile_id))
            image[0][y+1]['id'] = tile_id
            image[0][y+1]['bottom'] = opposite_side[side]
            image[0][y+1]['right'] = adjacent_side[side]

def get_index_list(right_side, size):
    if right_side==3: #OK
        return [(x,y) for y in range(size) for x in range(size)]
    elif right_side==1: #OK
        return [(x,y) for x in range(size) for y in range(size)]
    elif right_side==6:
        return [(x,y) for y in range(size-1,-1,-1) for x in range(size-1,-1,-1)]
    elif right_side==0: #OK
        return [(x,y) for x in range(size) for y in range(size-1,-1,-1)]
        #######
    elif right_side==2: #OK
        return [(x,y) for y in range(size) for x in range(size-1,-1,-1)]
    elif right_side==4: #OK
        return [(x,y) for x in range(size-1,-1,-1) for y in range(size-1,-1,-1)]
    elif right_side==7: #OK
        return [(x,y) for y in range(size-1,-1,-1) for x in range(size)]
    elif right_side==5: #OK
        return [(x,y) for x in range(size-1,-1,-1) for y in range(size)]

def get_pixels():
    pixels = [[0] * WIDTH for i in range(WIDTH)]
    for y in range(IMAGE_SIZE):
        for x in range(IMAGE_SIZE):
            tile_id = image[x][y]['id']
            idx = tiles[tile_id]['index']
            x0 = 0
            y0 = 0
            for i,j in get_index_list(image[x][y]['right'], REAL_SIZE):
                pixels[x*REAL_SIZE+x0][y*REAL_SIZE+y0] = lines[idx*DESC_SIZE+1+j+1][i+1]
                x0 += 1
                if x0 == REAL_SIZE:
                    y0 += 1
                    x0 = 0

    return pixels.copy()

monster_pixels=[(18,0), (0,1), (5,1), (6,1), (11,1), (12,1), (17,1), (18,1), (19,1), (1,2), (4,2), (7,2), (10,2), (13,2), (16,2)]
def match_monster(pixels, x,y):
    for x0,y0 in monster_pixels:
        if pixels[x+x0][y+y0]!='#':
            return False
    return True

res1 = part1()
print("solution 1 is {}".format(res1))

construct_image()
pixels = get_pixels()

hit_count = 0
for y in range(WIDTH):
    for x in range(WIDTH):
        if pixels[x][y]=='#':
            hit_count +=1

print("total # is {}".format(hit_count))
for right in range(8):
    pixels_xform = [[0] * WIDTH for i in range(WIDTH)]
    x0 = 0
    y0 = 0
    for x,y in get_index_list(right, WIDTH):
        pixels_xform[x0][y0] = pixels[x][y]
        x0 += 1
        if x0 == WIDTH:
            y0 += 1
            x0 = 0

    print('try position {}'.format(right))
    for y in range(WIDTH-2):
        for x in range(WIDTH-19):
            if match_monster(pixels_xform,x,y):
                hit_count -= len(monster_pixels)
                print('Find a monster for {} at {}x{}'.format(right, x,y))

res2 = hit_count
print("solution 2 is {}".format(res2))
