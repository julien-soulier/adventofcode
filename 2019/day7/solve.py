import itertools

f = open("input.txt", "r")
opcodes = list(map(int, f.read().split(',')))
f.close()

def get_argument(code, pos, mode):
    return code[pos] if mode == 1 else code[code[pos]]

def run(code, input):
    one_arg = [1,2,4,5,6,7,8]
    two_arg = [1,2,5,6,7,8]

    pos = 0
    output = []
    mode = {}
    arg = {}
    while code[pos] != 99:
        cmd = code[pos]
        mode[0] = (cmd // 100) % 10
        mode[1] = (cmd // 1000) % 10
        mode[2] = (cmd // 10000) % 10
        cmd = cmd % 100

        if cmd in one_arg:
            arg[0] = get_argument(code, pos+1, mode[0])
        
        if cmd in two_arg:
            arg[1] = get_argument(code, pos+2, mode[1])

        if cmd == 1:
            code[code[pos+3]] = arg[0] + arg[1] 
            pos += 4
        elif cmd == 2:
            code[code[pos+3]] = arg[0] * arg[1] 
            pos += 4
        elif cmd == 3:
            code[code[pos+1]] = input.pop(0)
            pos += 2
        elif cmd == 4:
            output.append(arg[0])
            pos += 2  
        elif cmd == 5:
            pos = arg[1] if arg[0] != 0 else pos + 3
        elif cmd == 6:
            pos = arg[1] if arg[0] == 0 else pos + 3
        elif cmd == 7:
            code[code[pos+3]] = 1 if arg[0] < arg[1] else 0
            pos += 4
        elif cmd == 8:
            code[code[pos+3]] = 1 if arg[0] == arg[1] else 0
            pos += 4
        else:
            print("invalid cmd {} at {}".format(code[pos], pos))
            break

    return output

def part1():
    final_out = []
    for perm in itertools.permutations(range(5)):
        out = [0]
        phases = list(perm)
        for amp in range(5):
            phase = phases.pop(0)
            out = run(opcodes.copy(), [phase, out.pop()])
        final_out.append(out.pop())

    return max(final_out)
    
def part2():
    return 0

print("Solution part1 is {}".format(part1()))

print("Solution part2 is {}".format(part2()))
