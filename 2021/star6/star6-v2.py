f = open("input.txt", "r")
fishes = list(map(int, f.read().split(',')))
f.close()

def count_fishes(days):
    for d in range(days):
        born = ages.pop(0)
        ages.append(born)
        ages[6]+=born

    return sum(ages)

ages = [fishes.count(i) for i in range(9)]
print("Solution part1 is {}".format(count_fishes(80)))

ages = [fishes.count(i) for i in range(9)]
print("Solution part2 is {}".format(count_fishes(256)))
