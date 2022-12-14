#/bin/env python3

def tuple_sign(a):
    return tuple(1 if v>0 else -1 if v<0 else 0 for v in a)

def add_tuple(a, b):
    return tuple(i + j for i, j in zip(a,b))

def tuple_neg(a):
    return tuple(-i for i in a)

def get_vector(start, end):
    return tuple_sign(add_tuple(end, tuple_neg(start)))

def draw_line(rocks, start, end):
    vector = get_vector(start, end)
    #print(f"{start}-{end} => {vector}")
    point = start
    rocks.add(point)
    while point!=end:
        point = add_tuple(point, vector)
        rocks.add(point)

def fill_rocks(input="input.txt"):
    rocks = set()
    with open(input, "r") as f:
        for path in f.readlines():
            points  = [eval('('+coord+')') for coord in path.strip().split(' -> ')]
            for line in [points[i:i+2] for i in range(len(points)-1)]:
                draw_line(rocks, line[0], line[1])
                
    return rocks

def simulate_one_sand_unit(rocks, sands, bottom):
    next = (500,0)
    while True:
        move = False
        curt = next
        for mvt in [(0,1), (-1,1), (1,1)]:
            next = add_tuple(curt, mvt)
            if next not in rocks and next not in sands:
                move = True
                break
        
        if not move or next[1] >= bottom+2:
            break
    
    return curt

def simulate_all_sands(rocks, mode):
    bottom = max((rock[1] for rock in rocks))
    sands = set()
    count = 0
    while True:
        rest = simulate_one_sand_unit(rocks, sands, bottom)
        if mode == 1 and  rest[1] > bottom:
            return count
        elif mode == 2 and rest == (500,0):
            return count + 1
        else:
            count += 1
            sands.add(rest)

rocks = fill_rocks()
print(f"Soution part1 is {simulate_all_sands(rocks, 1)}")
print(f"Soution part1 is {simulate_all_sands(rocks, 2)}")
