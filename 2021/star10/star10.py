f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

matching = { '(' : ')', '{': '}', '[': ']', '<': '>'}
corrupted_scoring = { ')' : 3, ']': 57, '}': 1197, '>': 25137}
incomplete_scoring = { '(' : 1, '[': 2, '{': 3, '<': 4}

corrupted_score = 0
incomplete_scores = []
for line in lines:
    stack = []
    ignore = False
    for c in line:
        if c in matching.keys():
            stack.append(c)
        else:
            o = stack.pop()
            if matching[o] != c:
                corrupted_score += corrupted_scoring[c]
                ignore = True
                continue

    if not ignore:
        incomplete_score = 0
        while len(stack) > 0:
            c = stack.pop()
            incomplete_score = incomplete_score * 5 + incomplete_scoring[c]
        incomplete_scores.append(incomplete_score)


print("Solution part1 is {}".format(corrupted_score))

incomplete_scores.sort()
index = (len(incomplete_scores)-1)//2
print("Solution part2 is {}".format(incomplete_scores[index]))
