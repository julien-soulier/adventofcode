f = open("input.txt", "r")
fishes = list(map(int, f.read().split(',')))
f.close()

#fishes = [3,4,3,1,2]

def count_children(age, days):
    population=[age]
    for day in range(days):
        #print("beg day {} count {}".format(day, len(population)))
        for i in range(len(population)):
            if population[i]==0:
                population[i]=6
                population.append(8)
            else:
                population[i] -= 1

    return len(population)


def count_children_fast(age, days):
    count = 1

    days -= age
    while days > 0:
        count += children_table[days-1][8]
        days-=7
    
    return count

def part1():
    children = {}
    for a in range(7):
        children[a] = count_children(a, 80)
    print(children)

    count=0
    for f in fishes:
        count += children[f]

    return count

children_table = {}
def part2():
    for day in range(257):
        children_table[day] = {}
        for a in range(9):
            children_table[day][a]= count_children_fast(a, day)
    
    count=0
    for f in fishes:
        count += children_table[256][f]

    return count

res1 = part1()
print("Soution part1 is {}".format(res1))

res2 = part2()
print("Soution part2 is {}".format(res2))
