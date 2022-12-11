#/bin/env python3

import re
import numpy as np 

class Monkey():

    def __init__(self, description):
        self.activity = 0

        # Need to use float due to integer overflow in part 2
        m = re.search("Starting items: (.*)\n", description)
        if m:
            self.items=list(map(float, m.group(1).split(',')))
        else:
            raise RuntimeError(f"Cannot find items in {description}")

        m = re.search("Operation: new = (.*)\n", description)
        if m:
            self.operation = m.group(1)
        else:
            raise RuntimeError(f"Cannot find operation in {description}")

        m = re.search("Test: divisible by (.*)\n", description)
        if m:
            self.modulus = int(m.group(1))
        else:
            raise RuntimeError(f"Cannot find modulus in {description}")
        
        m = re.search("If true: throw to monkey (.*)\n", description)
        if m:
            self.true = int(m.group(1))
        else:
            raise RuntimeError(f"Cannot find true condition in {description}")

        m = re.search("If false: throw to monkey (.*)$", description)
        if m:
            self.false = int(m.group(1))
        else:
            raise RuntimeError(f"Cannot find false condition in {description}")

    def __str__(self):
        print(self.items)
        return str(self.items)
        
    def process_items(self, divide, LCM):
        result = []
        while len(self.items) > 0:
            self.activity += 1
            old = self.items.pop(0)
            new = eval(self.operation)
            if divide:
                new //= 3
            new %= LCM
            r = {'item': new}
            r['monkey'] = self.true if new % self.modulus == 0 else self.false
            result.append(r)

        return result


def init_monkey_array(input="input.txt"):
    M = []
    with open(input, "r") as f:
        for desc in f.read().split("\n\n"):
            M.append(Monkey(desc))
    return M

def get_monkey_business(M, round, divide=True):
    LCM = np.lcm.reduce([m.modulus for m in M])

    for _ in range(round):
        for m in M:
            for a in m.process_items(divide, LCM):
                M[a['monkey']].items.append(a['item'])

    activity = [m.activity for m in M]
    activity.sort(reverse=True)
    return activity[0] * activity[1]

M = init_monkey_array()
print(f"Soution part1 is {get_monkey_business(M, 20)}")

M = init_monkey_array()
print(f"Soution part2 is {get_monkey_business(M, 10000, divide=False)}")
