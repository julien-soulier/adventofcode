import re

f = open("input.txt", "r")
lines = f.read().split('\n')
f.close()

dots = set()
folds = []
for line in lines:
    m = re.match(r'^(\d+),(\d+)$', line)
    if m:
        x = int(m.group(1))
        y = int(m.group(2))
        dots.add((x,y))
        continue

    m = re.match(r'^fold along (x|y)=(\d+)$', line)
    if m:
        axis = m.group(1)
        position = int(m.group(2))
        folds.append((0 if axis=='x' else 1, position))
        continue

def do_fold(dots, axis, position):
    new_dots = set()
    for dot in dots:
        if dot[axis] > position:
            new_coordinate = position - (dot[axis]-position) 
            if axis == 0:
                new_dot = (new_coordinate, dot[1])
            else:
                new_dot = (dot[0],new_coordinate)
        else:
            new_dot = dot
        new_dots.add(new_dot)
    return new_dots

def show_dots(dots):
    width = max(dots, key=lambda x: x[0])[0]
    height = max(dots, key=lambda x: x[1])[1]

    screen = []
    for y in range(height+1):
        screen.append([' ' for x in range(width+1)])

    for dot in dots:
        x = dot[0]
        y = dot[1]
        screen[y][x] = 'o'

    for line in screen:
        print(''.join(line))

def part1():
    fold = folds[0]
    my_dots = dots
    my_dots = do_fold(my_dots, fold[0], fold[1])
    return len(my_dots)

def part2():
    my_dots = dots
    for fold in folds:
        my_dots = do_fold(my_dots, fold[0], fold[1])

    show_dots(my_dots)

print("Solution part1 is {}".format(part1()))

part2()
print("Read password for solution 2")
