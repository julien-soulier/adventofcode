import re
import itertools

f = open("input.txt", "r")
lines = f.read().split('\n')
f.close()

CONV = list(map(lambda x: 0 if x=='.' else 1, lines[0]))
MARGIN = 150
WIDTH = len(lines[2])

image = []
for _ in range(MARGIN):
    line = [0 for x in range(WIDTH + 2*MARGIN)]
    image.append(line)

for l in lines[2:-1]:
    line = [0 for x in range(MARGIN)]
    line.extend(list(map(lambda x: 0 if x=='.' else 1, l)))
    line.extend([0 for x in range(MARGIN)])
    image.append(line)

for _ in range(MARGIN):
    line = [0 for x in range(WIDTH + 2*MARGIN)]
    image.append(line)

v = sum(map(lambda x: sum(x), image))
print(v)

def copy_image(img):
    mod = []
    for l in img:
        mod.append(l.copy())
    return mod

def index(img,x0,y0):
    v = 0
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            v = 2*v + img[y][x]

    return v

def convert_pixel(img, x0, y0):
    i = index(img,x0,y0)
    return CONV[i]

def convert_image(img):
    mod = copy_image(img)
    for y in range(1, len(img)-1):
        for x in range(1, len(img[y])-1):
            mod[y][x] = convert_pixel(img,x,y)

    #modify border of the image as well
    for y in range(len(img)):
        mod[y][0] = CONV[0] if img[y][0] == 0 else CONV[-1]
        mod[y][-1] = CONV[0] if img[y][-1] == 0 else CONV[-1]

    for x in range(len(img[0])):
        mod[0][x] = CONV[0] if img[0][x] == 0 else CONV[-1]
        mod[-1][x] = CONV[0] if img[-1][x] == 0 else CONV[-1]

    return mod

def part1(image):
    img = copy_image(image)
    for _ in range(2):
        img = convert_image(img)

    v = sum(map(lambda x: sum(x), img))
    return v

def part2(image):
    img = copy_image(image)
    for _ in range(50):
        img = convert_image(img)

    v = sum(map(lambda x: sum(x), img))
    return v

print("Solution part1 is {}".format(part1(image)))
print("Solution part2 is {}".format(part2(image)))
