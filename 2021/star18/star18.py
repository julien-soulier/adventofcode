import re
import itertools

f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('') 
f.close()

def explode(num, p, q, a, b):
    left = num[p::-1]
    m = re.search(r'(\d+)', left)
    if m:
        #print("{} {}".format(a, m[1]))
        a += int(m[1][::-1])
        left = re.sub(r'\d+', str(a)[::-1], left, count=1)

    right = num[p+q:]
    m = re.search(r'(\d+)', right)
    if m:
        b += int(m[1])
        right = re.sub(r'\d+', str(b), right, count=1)
    
    return left[::-1]+'0'+right


def reduce(num):
    done = False
    while not done:
        depth = 0
#        print(num)
        done = True
        # explode first
        for m in re.finditer(r'(\[|\])', num):
            #print("match at {} {} {} {}".format(m.start(), m.end(), m.pos, m.lastindex))
            if m[1]=='[':
                if depth == 4:
                    p = m.start()
                    pair = re.match(r'\[(\d+),(\d+)\]', num[p:])
                    #print("explode at {}: [{} - {}].".format(p, pair[1], pair[2]))
                    num = explode(num, p-1, pair.end()+1, int(pair[1]), int(pair[2]))
                    done = False
                    break
                else:
                    depth += 1
            else:
                depth -= 1

        if not done:
            continue

        # then split
        m = re.search(r'(\d{2,})', num)
        if m:
            #print("need to split {} at {}".format(m[1], m.start()))
            c = int(m[1])
            a = c//2
            b = (c+1)//2
            s = "[{},{}]".format(a,b)
            num = re.sub(r'\d{2,}', s, num, count=1)
            done = False

    return num

def magnitude(val):
    if isinstance(val, int):
        return int(val)
    else:    
        return 3*magnitude(val[0]) + 2*magnitude(val[1])

def part1():
    num = lines[0]
    for l in lines[1:]:
        num = '[' + num + ',' + l + ']'
        num = reduce(num)
    return magnitude(eval(num))

def part2():
    max_mag = 0
    for pair in itertools.permutations(lines, 2):
        num = '[' + pair[0] + ',' + pair[1] + ']'
        num = reduce(num)
        max_mag = max(magnitude(eval(num)), max_mag)

    return max_mag

print("Solution part1 is {}".format(part1()))
print("Solution part2 is {}".format(part2()))
