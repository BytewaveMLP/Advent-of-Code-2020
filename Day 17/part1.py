import sys
import copy
from collections import defaultdict

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']
grid = set()
for y, line in enumerate(input_lines):
	for x, c in enumerate(input_lines[y]):
		if c == '#':
			grid.add((x, y, 0))

def kill(grid, coord):
	cx, cy, cz = coord
	active_count = 0

	for z in range(cz - 1, cz + 2):
		for y in range(cy - 1, cy + 2):
			for x in range(cx - 1, cx + 2):
				if x == cx and y == cy and z == cz: continue
				neighbor = (x, y, z)
				if neighbor in grid:
					active_count += 1

	return not 2 <= active_count <= 3

def revive(grid, coord):
	cx, cy, cz = coord
	revives = set()

	for z in range(cz - 1, cz + 2):
		for y in range(cy - 1, cy + 2):
			for x in range(cx - 1, cx + 2):
				if x == cx and y == cy and z == cz: continue
				active_count = 1

				for z2 in range(z - 1, z + 2):
					for y2 in range(y - 1, y + 2):
						for x2 in range(x - 1, x + 2):
							if x2 == cx and y2 == cy and z2 == cz: continue
							if x2 == x and y2 == y and z2 == z: continue
							neighbor = (x2, y2, z2)
							if neighbor in grid:
								active_count += 1

				if active_count == 3:
					revives.add((x, y, z))

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
