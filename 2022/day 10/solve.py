#/bin/env python3

import re

def get_instructions(input="input.txt"):
    instructions = []
    with open(input, "r") as f:
        for line in f.readlines():
            m = re.fullmatch("(noop|addx)(.*)", line.strip())
            if not m:
                continue
            instructions.append({'cmd':m.group(1), 'arg': m.group(2)})

    return instructions

def get_signal_strengths(instructions):
    signal_strengths = []
    cycle = 1
    pipeline = [1]
    while True:
        x = pipeline.pop(0)

        crt = (cycle-1) % 40
        print("#" if abs(crt-x)<2 else ' ', end='')
        if crt == 39:
            print("")

        if cycle % 40 == 20:
            signal_strengths.append(cycle*x)

        if len(pipeline)==0 and len(instructions)==0:
            break

        if len(pipeline) == 0:
            instruction = instructions.pop(0)

            if instruction['cmd'] == "noop":
                pipeline.append(x)
            elif instruction['cmd'] == "addx":
                pipeline.extend([x, x+int(instruction['arg'])])
            else:
                raise RuntimeError(f"Invalid Instruction: {instruction['cmd']}{instruction['arg']}")
        
        cycle += 1

    return signal_strengths

print(f"Soution part1 is {sum(get_signal_strengths(get_instructions('input.txt')))}")
