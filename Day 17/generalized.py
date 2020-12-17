import sys
import copy
import itertools
import operator

if not (2 <= len(sys.argv) <= 3):
	print(f'usage: {sys.argv[0]} <input.txt> [<dimensions>]')
	exit(1)

DIMENSIONS = int(sys.argv[2] if len(sys.argv) > 2 else 3)

addpos = lambda x, y: tuple(map(operator.add, x, y))

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']
grid = set()
for y, line in enumerate(input_lines):
	for x, c in enumerate(input_lines[y]):
		if c == '#':
			grid.add(tuple([x, y] + [0] * (DIMENSIONS - 2)))

def kill(grid, coord):
	active_count = 0

	for offset in itertools.product([-1, 0, 1], repeat=DIMENSIONS):
		if all(o == 0 for o in offset): continue
		neighbor = addpos(coord, offset)
		if neighbor in grid:
			active_count += 1

	return not 2 <= active_count <= 3

def revive(grid, coord):
	revives = set()

	for offset in itertools.product([-1, 0, 1], repeat=DIMENSIONS):
		if all(o == 0 for o in offset): continue
		active_count = 1
		possible_revive = addpos(coord, offset)

		for offset2 in itertools.product([-1, 0, 1], repeat=DIMENSIONS):
			if all(o == 0 for o in offset2): continue
			neighbor = addpos(possible_revive, offset2)
			if neighbor == coord: continue

			if neighbor in grid:
				active_count += 1

		if active_count == 3:
			revives.add(possible_revive)

	return revives

def iterate(grid):
	grid_copy = copy.deepcopy(grid)
	for coord in grid:
		if kill(grid, coord):
			grid_copy.remove(coord)
		grid_copy |= revive(grid, coord)
	return grid_copy

print('INITIAL STATE:')
print(grid)

for i in range(6):
	grid = iterate(grid)
	print(f'ITERATION {i}:')
	print(grid)

print(len(grid))
