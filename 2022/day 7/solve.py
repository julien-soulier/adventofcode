#/bin/env python3
from parse import *

class DIR():
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.dirs={}
        self.files={}

    def add_dir(self, dirname):
        dir = DIR(self, dirname)
        self.dirs[dirname] = dir

    def add_file(self, size, filename):
        file = FILE(filename, size)
        self.files[filename] = file

    def get_dir(self, dirname):
        return self.parent if dirname == '..' else self.dirs[dirname]

    def get_sizes(self):
        size_array = []
        val = 0
        for dir in self.dirs.values():
            dir_size_array = dir.get_sizes()
            val += dir_size_array[0]
            size_array.extend(dir_size_array)

        val  += sum(f.size for f in self.files.values())
        size_array.insert(0, val)
        return size_array

class FILE():
    def __init__(self, name, size):
        self.name = name
        self.size = size

def process_command(line):
        dirname = line[5:]
        
root_dir = DIR(None, '/')
def process_input(input="input.txt"):
    global root_dir

    curt_dir = None
    with open(input, "r") as f:
        for line in f.read().split('\n'):
            if line == '':
                continue

            if line[0:4] == "$ cd":                  
                curt_dir = root_dir if line[5] == '/' else curt_dir.get_dir(line[5:])
            elif line[0:4] == "$ ls":
                pass
            elif line[0:4] == 'dir ':
                curt_dir.add_dir(line[4:])
            else:
                r = parse("{size:d} {name}", line)
                if not r:
                    print(f"ERROR: {line}")
                else:
                    curt_dir.add_file(r['size'], r['name'])

process_input()
sizes = root_dir.get_sizes()
print(f"Soution part1 is {sum(x for x in sizes if x<=100000)}")

required_space = 30000000 - (70000000 - sizes[0])
print(f"Soution part2 is {min(x for x in sizes if x>=required_space)}")
