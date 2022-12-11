#/bin/env python3

import re
import numpy as np 

mk_re = r"^\s+Starting items: (.+)$"
mk_re += r"\s+Operation: new = (.+)$"
mk_re += r"\s+Test: divisible by (.+)$"
mk_re += r"\s+If true: throw to monkey (.+)$"
mk_re += r"\s+If false: throw to monkey (.+)$"

class Monkey():

    def __init__(self, description):
        self.activity = 0
        m = re.search(mk_re, description, re.MULTILINE)
        if m:
            # Need to use float due to integer overflow in part 2 otherwise
            self.items=list(map(float, m.group(1).split(',')))
            self.operation = m.group(2)
            self.modulus = int(m.group(3))
            self.true = int(m.group(4))
            self.false = int(m.group(5))
        else:
            raise RuntimeError(f"Cannot parse Monkey description {description}")

    def __str__(self):
        print(self.items)
        return str(self.items)
        
    def process_items(self, divide, LCM):
        result = []
        while len(self.items) > 0:
            self.activity += 1
            old = self.items.pop(0)
            # operarion uses "old" as variable
            new = eval(self.operation)
            if divide:
                new //= 3
            
            # we can operate modulus LCM of all modulus to avoid too large numbers
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
