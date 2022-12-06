import collections
import itertools

def read_input():
	with open("input.txt", 'r') as f:
		end_of_file = False
		while not end_of_file:
			c = f.read(1).strip()
			if not c:
				end_of_file = True
			else:
				yield c


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


print(f"Solution part 1: {min([i for i, v in enumerate(map(len, map(set, sliding_window(read_input(), 4)))) if v == 4]) + 4 }")

print(f"Solution part 1: {min([i for i, v in enumerate(map(len, map(set, sliding_window(read_input(), 14)))) if v == 14]) + 14}" )
