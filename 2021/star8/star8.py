f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

from collections import Counter

def is_simple(l):
    if l==2 or l==3 or l==4 or l==7:
        return 1
    else:
        return 0

def count_simple_digits(line):
    res = line.split(' | ')[1]
    digits = res.split(' ')
    lengths = list(map(len, digits))
    return sum(list(map(is_simple, lengths)))

def solve_order(patterns):
    reference = "abcdefg"
    string = ""
    for p in patterns:
        string += p

    tmp = [string.count(t) for t in ['a', 'b', 'c', 'd', 'e', 'f', 'g']]
    tmp = list(map(lambda x: 'e' if x==4 else x, tmp))
    tmp = list(map(lambda x: 'b' if x==6 else x, tmp))
    tmp = list(map(lambda x: 'f' if x==9 else x, tmp))

    cf = list(filter(lambda x: True if len(x)==2 else False, patterns))[0]
    x = tmp.index(8)
    if reference[x] in cf:
        tmp[x] = 'c'
        tmp = list(map(lambda x: 'a' if x==8 else x, tmp))
    else:
        tmp[x] = 'a'
        tmp = list(map(lambda x: 'c' if x==8 else x, tmp))

    bcdf = list(filter(lambda x: True if len(x)==4 else False, patterns))[0]
    x = tmp.index(7)
    if reference[x] in bcdf:
        tmp[x] = 'd'
        tmp = list(map(lambda x: 'g' if x==7 else x, tmp))
    else:
        tmp[x] = 'g'
        tmp = list(map(lambda x: 'd' if x==7 else x, tmp))

    return((''.join(tmp)))

def part1():
    return sum(list(map(count_simple_digits, lines)))


def get_value(digit):
    if digit == {'a', 'b', 'c', 'e', 'f', 'g'}:
        return 0
    elif digit == {'c', 'f'}:
        return 1
    elif digit == {'a', 'c', 'd', 'e', 'g'}:
        return 2
    elif digit == {'a', 'c', 'd', 'f', 'g'}:
        return 3
    elif digit == {'b', 'c', 'd', 'f'}:
        return 4
    elif digit == {'a', 'b', 'd', 'f', 'g'}:
        return 5
    elif digit == {'a', 'b', 'd', 'e', 'f', 'g'}:
        return 6
    elif digit == {'a', 'c', 'f'}:
        return 7
    elif digit == {'a', 'b', 'c', 'd', 'e', 'f', 'g'}:
        return 8
    elif digit == {'a', 'b', 'c', 'd', 'f', 'g'}:
        return 9
    else:
        print("ERROR {}".format(digit))
        return 0

def part2():
    total = 0
    for line in lines:
        pattern = line.split(' | ')[0] 
        patterns = pattern.split(' ') 
        conv = solve_order(patterns)
        translation = "".maketrans('abcdefg', conv)
        res = line.split(' | ')[1]
        res = res.translate(translation)

        digits = (res.split(' '))
        digits = list(map(set, digits))
        values = list(map(get_value, digits))
        num = int(values[3]) + 10*int(values[2]) + 100*int(values[1]) + 1000*int(values[0])
        total += num

    return total

res1 = part1()
print("Soution part1 is {}".format(res1))

res2 = part2()
print("Soution part2 is {}".format(res2))