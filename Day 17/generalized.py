import sys
import copy
import itertools
import operator

if not (2 <= len(sys.argv) <= 4):
	print(f'usage: {sys.argv[0]} <input.txt> [<dimensions>] [<iterations>]')
	exit(1)

DIMENSIONS = int(sys.argv[2] if len(sys.argv) > 2 else 3)
ITERATIONS = int(sys.argv[3] if len(sys.argv) > 3 else 6)
NEIGHBOR_OFFSETS = list(itertools.product([-1, 0, 1], repeat=DIMENSIONS))

addpos = lambda x, y: tuple(map(operator.add, x, y))

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']
grid = set()
for y, line in enumerate(input_lines):
	for x, c in enumerate(input_lines[y]):
		if c == '#':
			grid.add(tuple([x, y] + [0] * (DIMENSIONS - 2)))

def live_around(grid, coord):
	return sum(1 for neighbor_offset in NEIGHBOR_OFFSETS if addpos(coord, neighbor_offset) in grid)

def kill(grid, coord):
	active_count = live_around(grid, coord)
	return not 3 <= active_count <= 4

def revive(grid, coord):
	revives = set()

	for offset in NEIGHBOR_OFFSETS:
		possible_revive = addpos(coord, offset)
		if possible_revive in grid: continue
		active_count = live_around(grid, possible_revive)

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

for i in range(ITERATIONS):
	grid = iterate(grid)
	print(f'ITERATION {i+1}:')
	print(grid)

print()
print('SIMULATION STOP.')
print(f'LIVE AT END: {len(grid)}')
