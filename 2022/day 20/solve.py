#/bin/env python3

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def append(self, node):
        self.next = node
        node.prev = self

    def insert_next(self, node):
        next_node = self.next
        self.next = node
        node.prev = self
        node.next = next_node
        next_node.prev = node

    def insert_prev(self, node):
        self.prev.insert_next(node)

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def reorder(self, LEN):
        count = ((abs(self.value) - 1) % (LEN - 1)) + 1
        node = self
        if self.value != 0:
            self.remove()
            for _ in range(count):
                node = node.next if self.value > 0 else node.prev
            node.insert_next(self) if self.value > 0 else node.insert_prev(self)
               
    def print_list(self, LEN):
        node = self
        print("<<<<<<<<<<<")
        for _ in range(LEN):
            print(node.value)
            node = node.next
        print(">>>>>>>>>>>")

def read_node_list(infile="input.txt"):
    l_dict = dict()
    current_node = None
    count = 0
    with open(infile, "r") as f:
        for line in f.readlines():
            next_node = Node(int(line.strip()))
            if current_node:
                current_node.append(next_node)
            l_dict[count] = next_node
            current_node = next_node
            count  += 1

    l_dict[0].prev = l_dict[count-1]
    l_dict[count-1].next = l_dict[0]
    return l_dict

def get_coordindate(l_dict, index, LEN):
    # find node with value 0
    for i in range(LEN):
        if l_dict[i].value == 0:
            break
    print(f"Found value 0 @{i}")
    node = l_dict[i]
    for _ in range(index):
        node = node.next

    return node.value

def decrypt_file(infile="input.txt", decryption_key=1, loop_count=1):
    l_dict = read_node_list()
    LEN = len(l_dict)

    # apply decryption key
    for i in range(LEN):
        l_dict[i].value *= decryption_key

    for l in range(loop_count):
        print(f"LOOP {l}")
        for i in range(LEN):
            l_dict[i].reorder(LEN)
            # l_dict[i].print_list(LEN)

    return sum(get_coordindate(l_dict, index, LEN) for index in [1000, 2000, 3000])

print(f"Soution part1  is {decrypt_file()}")
print(f"Soution part2  is {decrypt_file(decryption_key=811589153, loop_count=10)}")
