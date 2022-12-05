from parse import *

class Stack:

	def __init__(self, crates):
		## we remove empty crates
		self.crates = [crate for crate in crates if crate]

	def pop_crates(self, n, keep_order=False):
		result = [''] * n
		for i in range(n):
			index = n - i - 1 if keep_order else i
			result[index] = self.crates.pop()

		return result

	def add_crates(self, new_crates):
		self.crates.extend([new_crate for new_crate in new_crates if new_crate])

	def read_top(self):
		return self.crates[len(self.crates) - 1][1]

	def __str__(self):
		return ''.join(self.crates)

def read_stacks():
	with open("input.txt", "r") as f:
		stop_reading_stack = False
		stacks_input = list()
		while not stop_reading_stack:
			line = f.readline()
			if '1' in line:
				stop_reading_stack = True
			else:
				stacks_input.append(line)


	cargo = dict()
	h_stack_max = len(stacks_input)
	for i in range(h_stack_max - 1, -1, -1):
		characters = list(stacks_input[i])
		current_stack_index = 0
		for i in range(0, len(characters), 4):
			crate = characters[i:(i+3)]
			if current_stack_index not in cargo:
				cargo[current_stack_index] = Stack([])

			cargo[current_stack_index].add_crates([''.join(crate).strip()])
			current_stack_index += 1

	return cargo

def read_procedure():
	with open("input.txt", "r") as f:
		procedure_starts = False
		for line in f.readlines():
			if procedure_starts:
				yield parse("move {:d} from {:d} to {:d}", line.strip())
			else:
				procedure_starts = not line.strip()
	

def apply_procedure(procedure, cargo, keep_order=False):
	for rearrangement in procedure:
		n_crate = rearrangement[0] 
		stack_from = rearrangement[1] - 1
		stack_to = rearrangement[2] - 1

		cargo[stack_to].add_crates(cargo[stack_from].pop_crates(n_crate, keep_order))

	return cargo


## Debug Print cargo before rearrangement procedure
cargo = read_stacks()
for stack_index, stack in cargo.items():
	print(f"Stack index: {stack_index + 1} contain the following crates: {stack}")


## Debug Print cargo after rearragement procedure
cargo = apply_procedure(read_procedure(), cargo)
for stack_index, stack in cargo.items():
	print(f"Stack index: {stack_index + 1} contain the following crates: {stack}")


## Print Solutions
print(f"Solution part 1 is : {''.join([stack.read_top() for stack in cargo.values()])}")

cargo = read_stacks()
cargo = apply_procedure(read_procedure(), cargo, keep_order=True)
print(f"Solution part 2 is : {''.join([stack.read_top() for stack in cargo.values()])}")
