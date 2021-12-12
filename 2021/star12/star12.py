import re

f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

graph = {}
for line in lines:
    m = re.match(r'^([a-z]+|[A-Z]+)-([a-z]+|[A-Z]+)$', line)
    if m:
        a = m.group(1)
        b = m.group(2)
        if not a in graph.keys():
            graph[a] = []

        if not b in graph.keys():
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)
    else:
        print("invalid regex for line {}".format(line))

def path_has_duplicate(path):
    small_caves = list(filter(lambda x: x.islower(), path))
    small_caves_set = set(small_caves)
    return len(small_caves) != len(small_caves_set)

def valid_cave(path, cave, algo):
    if algo==1 or cave=='start' or path_has_duplicate(path):
        if cave.islower() and cave in path:
            return False

    return True

def find_path(path, cave, algo):
    if not valid_cave(path, cave, algo):
        return
    
    path.append(cave)

    if cave == 'end':
        valid_paths.append(path.copy())
        path.pop()
        return

    for next_cave in graph[cave]:
        find_path(path, next_cave, algo)

    path.pop()
    return

def part1():
    find_path([], 'start', 1)
    return len(valid_paths)
    
def part2():
    find_path([], 'start', 2)
    return len(valid_paths)

valid_paths = []
print("Solution part1 is {}".format(part1()))

valid_paths = []
print("Solution part2 is {}".format(part2()))
