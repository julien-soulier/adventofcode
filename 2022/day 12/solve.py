#/bin/env python3

class Node():
    def __init__(self, position, distance, prev_node, height):
        self.position = position
        self.distance = distance
        self.prev_node = prev_node
        self.height = height 

    def __str__(self):
        return str(self.position)

    def __repr__(self):
        return str(self)

def generate_map(input="input.txt"):
    global START, END, H, W

    with open(input, "r") as f:
        y = 0
        MAP = []
        for line in f.readlines():
            x = line.find('S')
            if x>=0:
                START = (x,y)
                line = line.replace('S', 'a')

            x = line.find('E')
            if x>=0:
                END = (x,y)
                line = line.replace('E', 'z')
            
            MAP.append(list(map(ord, line.strip())))
            y+=1

    H = len(MAP)
    W = len(MAP[0])

    return MAP

def is_valid(position):
    global H, W

    x = position[0]
    y = position[1]

    return True if (x>=0) and (x<W) and (y>=0) and (y<H) else False

def add_tuple(a, b):
    return tuple(i + j for i, j in zip(a,b))

def get_height(MAP, position):
    return MAP[position[1]][position[0]]

def get_neighboors(MAP, node, reverse):
    MVT = [(0,1), (0,-1), (1,0), (-1,0)]

    curt_height = get_height(MAP, node.position)

    res = []
    for m in MVT:
        new_pos = add_tuple(node.position, m)
        if not is_valid(new_pos):
            continue
        
        new_height = get_height(MAP, new_pos)
        if not reverse and new_height - curt_height > 1:
            continue

        if reverse and new_height - curt_height < -1:
            continue

        res.append(Node(new_pos, node.distance+1, node, new_height))

    return res

def index_of_node(array, position):
    res = [idx for idx,node in enumerate(array) if node.position == position]
    return res.pop() if len(res)>0 else -1

def find_path(MAP, start, end=None, reverse=False, target_height=None):
    REM = set(((x,y) for x in range(W) for y in range(H)))
    last = Node(start, 0, None, ord('a'))
    known_list = [last]
    pool = []
    REM.remove(start)
    while (len(REM)>0):
        print(f"last is {last}, remains {len(REM)}")
        distance = last.distance + 1
        for neighboor in get_neighboors(MAP, last, reverse):
            idx = index_of_node(pool, neighboor.position)
            if idx >= 0:
                if pool[idx].distance > distance:
                    pool.pop(idx)
                else:
                    continue

            idx = index_of_node(known_list, neighboor.position)
            if idx >= 0:
                continue

            pool.append(neighboor)

        pool.sort(key=lambda x: x.distance)
        last = pool.pop(0)
        known_list.append(last)
        REM.remove(last.position)

        if end and last.position == end:
            break

        if target_height and get_height(MAP, last.position) == target_height:
            break

    return known_list

MAP = generate_map(input="input.txt")
path_map1 = find_path(MAP, START, END)
path_map2 = find_path(MAP, END, None, reverse=True, target_height=ord('a'))

idx = index_of_node(path_map1, END)
print(f"Soution part1 is {path_map1[idx].distance}")

idx = [idx for idx,node in enumerate(path_map2) if node.height == ord('a')].pop()
print(f"Soution part2 is {path_map2[idx].distance}")