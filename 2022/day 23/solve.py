#/bin/env python3

def add_tuple(a, b):
    return tuple(i + j for i, j in zip(a,b))

MVT = [(0,-1), (0,1), (-1,-0), (1,0)]

class Elf():
    elves = list()
    curts = set()
    nexts = set()
    dups = list()
    move = 1

    def __init__(self, position):
        self.position = position
        self.next_pos = position
        Elf.elves.append(self)
        Elf.curts.add(position)

    def __str__(self):
        return f"Elf @ {self.position}"

    def __repr__(self):
        return str(self)

    def read_file(infile="input.txt",x0=1000,y0=1000):
        with open(infile, "r") as f:
            y = y0
            for line in f.readlines():
                x = x0
                y += 1
                for c in line.strip():
                    x += 1
                    if c == '#':
                        elf = Elf((x,y))
    

    def get_neighboors(self):
        x0 = self.position[0]
        y0 = self.position[1]
        neighboors = list()
        # north, south, west, east in this order
        neighboors.append(set(((x,y0-1) for x in range(x0-1,x0+2))))
        neighboors.append(set(((x,y0+1) for x in range(x0-1,x0+2))))
        neighboors.append(set(((x0-1,y) for y in range(y0-1,y0+2))))
        neighboors.append(set(((x0+1,y) for y in range(y0-1,y0+2))))

        return neighboors

    def compute_next(self, round):
        neighboors = self.get_neighboors()
        all_neighboors = neighboors[0].union(neighboors[1], neighboors[2], neighboors[3])

        # by default does not move
        self.next_pos = self.position

        # if there is at least one elf nearby
        if all_neighboors.intersection(Elf.curts):
            for i in range(4):
                idx = (i + round) % 4

                # no elf on this side, move there
                if not neighboors[idx].intersection(Elf.curts):
                    self.next_pos = add_tuple(self.position, MVT[idx])
                    break

        if self.next_pos in Elf.nexts:
            Elf.dups.append(self.next_pos)
        else:
            Elf.nexts.add(self.next_pos)

    def move_next(self):
        if self.position != self.next_pos:
            if not self.next_pos in Elf.dups:
                Elf.move += 1
                self.position = self.next_pos
        Elf.curts.add(self.position)

def simulate_one_round(round):
    Elf.nexts.clear()
    Elf.dups.clear()
    for elf in Elf.elves:
        elf.compute_next(round)
    
    Elf.curts.clear()
    for elf in Elf.elves:
        elf.move_next()

def compute_empty_cells(do_print=False):
    x0 = min((c[0] for c in Elf.curts))
    x1 = max((c[0] for c in Elf.curts))
    y0 = min((c[1] for c in Elf.curts))
    y1 = max((c[1] for c in Elf.curts))

    if do_print:
        print(f"{x0}-{x1} / {y0}-{y1}")
        for y in range(y0,y1+1):
            for x in range(x0,x1+1):
                if (x,y) in Elf.curts:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    return len(list(((x,y) for x in range(x0, x1+1) for y in range(y0, y1+1) if not (x,y) in Elf.curts)))

Elf.read_file()
compute_empty_cells()
for round in range(10):
    simulate_one_round(round)

print(f"Soution part1  is {compute_empty_cells()}")

round=10
while Elf.move > 0:
    Elf.move = 0
    simulate_one_round(round)
    round += 1
    if round % 100 == 0:
        print(f"round {round} => Moved {Elf.move}")

print(f"Soution part2  is {round}")
