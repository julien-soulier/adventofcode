f = open("input.txt", "r")
opcodes = list(map(int, f.read().split(',')))
f.close()

def run(opcodes):
    pos = 0
    while opcodes[pos] != 99:
        cmd = opcodes[pos]
        if cmd == 1:
            opcodes[opcodes[pos+3]] = opcodes[opcodes[pos+1]] + opcodes[opcodes[pos+2]]
            pos += 4
        elif cmd == 2:
            opcodes[opcodes[pos+3]] = opcodes[opcodes[pos+1]] * opcodes[opcodes[pos+2]]
            pos += 4
        else:
            print("invalid cmd {} at {}".format(opcodes[pos], pos))
            break

def part1():
    opcodes[1] = 12
    opcodes[2] = 2
    state = opcodes.copy()
    run(state)
    return state[0]
    
def part2():
    done = False
    for noun in range(1,100):
        for verb in range(1,100):
            opcodes[1] = noun
            opcodes[2] = verb
            tmp_code = opcodes.copy()
            run(tmp_code)
            if tmp_code[0] == 19690720:
                done = True
                break
        if done:
            break
    if not done:
        print("Error. Could not find solution")

    return 100*noun+verb

print("Solution part1 is {}".format(part1()))

print("Solution part2 is {}".format(part2()))
