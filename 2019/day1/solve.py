f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

depths = list(map(int, lines))

def fuel(x):
    return (x // 3) - 2

def fuel2(x):
    total_fuel = 0
    while True:
        fuel = (x // 3) - 2
        fuel = max(0, fuel)
        if fuel == 0:
            break
        total_fuel += fuel
        x = fuel

    return total_fuel
    
def part1():
    return sum(map(fuel, map(int, lines)))
    
def part2():
    return sum(map(fuel2, map(int, lines)))

print("Solution part1 is {}".format(part1()))

print("Solution part2 is {}".format(part2()))
