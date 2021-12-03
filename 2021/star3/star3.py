f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

def int_base2(x):
    return int(x, base=2)

numbers = list(map(int_base2, lines))
print(numbers[0])

MOST_COMMON=0
LEAST_COMMON=1

def get_bit(numbers, bit, algo):
    mask = 1<<bit
    count1 = 0
    total = len(numbers)

    for n in numbers:
        if n & mask:
            count1 += 1

    if count1 >= total / 2:
        return 1 if algo == MOST_COMMON else 0
    else:
        return 1 if algo == LEAST_COMMON else 0

def part1():
    width = len(lines[0])
    gamma = 0
    for i in range(width):
        gamma += get_bit(numbers, i, MOST_COMMON) << i
    
    epsilon = ~gamma & ((1 << width)-1)
    return gamma * epsilon

def filter_numbers(numbers, bit, algo):
    if len(numbers) == 1:
        return numbers[0]
    elif bit == -1:
        print("error")
        return 0

    mask = get_bit(numbers, bit, algo)
    filtered_numbers = []
    for n in numbers:
        if (n >> bit) & 0x1 == mask:
            filtered_numbers.append(n)
    
    return filter_numbers(filtered_numbers, bit-1, algo)

def part2():
    width = len(lines[0])
    oxy = filter_numbers(numbers, width-1, MOST_COMMON)
    co2 = filter_numbers(numbers, width-1, LEAST_COMMON)
    return oxy*co2

res1 = part1()
print("Soution part1 is {}".format(res1))

res2 = part2()
print("Soution part2 is {}".format(res2))
