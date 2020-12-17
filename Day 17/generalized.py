import sys
import copy
import itertools
import operator
from typing import *

if not (2 <= len(sys.argv) <= 4):
	print(f'usage: {sys.argv[0]} <input.txt> [<dimensions>] [<iterations>]', file=sys.stderr)
	exit(1)

Point = Tuple[int, ...]
Grid = set[Point]
DIMENSIONS = int(sys.argv[2] if len(sys.argv) > 2 else 3)
if DIMENSIONS < 2:
	print('dimemsions must be >= 2', file=sys.stderr)
	exit(1)

ITERATIONS = int(sys.argv[3] if len(sys.argv) > 3 else 6)
if ITERATIONS < 1:
	print('iterations must be >= 1', file=sys.stderr)
	exit(1)

NEIGHBOR_OFFSETS = list(itertools.product([-1, 0, 1], repeat=DIMENSIONS))

addpos = lambda x, y: tuple(map(operator.add, x, y))

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']
grid = set()
for y, line in enumerate(input_lines):
	for x, c in enumerate(input_lines[y]):
		if c == '#':
			grid.add(tuple([x, y] + [0] * (DIMENSIONS - 2)))

def print_grid(grid: Grid):
	RANGE_DIMS = [list(range(min(coord[d] for coord in grid), max(coord[d] for coord in grid) + 1)) for d in range(DIMENSIONS)]
	for higher_dims in itertools.product(*RANGE_DIMS[2:]):
		# reverse dimensions iteration order to make visualization make more sense
		# (iterate lower dimensions before higher ones)
		higher_dims = higher_dims[::-1]
		# don't bother printing the slice if the tuple is empty (2D)
		if higher_dims: print(f'slice ({", ".join(str(d) for d in higher_dims)})')
		# print this dimension's x,y slice
		for y in RANGE_DIMS[1]:
			for x in RANGE_DIMS[0]:
				print('#' if (x, y) + higher_dims in grid else '.', end='')
			print()
		print()

def live_around(grid: Grid, coord: Point) -> int:
	"""Count the number of living cells surrounding a grid coordinate"""
	return sum(1 for neighbor_offset in NEIGHBOR_OFFSETS if addpos(coord, neighbor_offset) in grid)

def kill(grid: Grid, coord: Point) -> bool:
	"""Tests if the cell at coord should be killed"""
	active_count = live_around(grid, coord)
	return not 3 <= active_count <= 4

def revive(grid: Grid, coord: Point) -> Grid:
	"""Generates a set of all cells which can be revived near coord"""
	revives = set()

	for offset in NEIGHBOR_OFFSETS:
		possible_revive = addpos(coord, offset)
		if possible_revive in grid: continue
		active_count = live_around(grid, possible_revive)

		if active_count == 3:
			revives.add(possible_revive)

	return revives

def iterate(grid: Grid) -> Grid:
	"""Runs one iteration of N-dimensional Game of Life, returning the new grid state"""
	grid_copy = copy.deepcopy(grid)
	for coord in grid:
		if kill(grid, coord):
			grid_copy.remove(coord)
		grid_copy |= revive(grid, coord)
	return grid_copy

print('INITIAL STATE:')
print_grid(grid)

for i in range(ITERATIONS):
	grid = iterate(grid)
	print(f'ITERATION {i+1}:')
	print_grid(grid)

print()
print('SIMULATION STOP.')
print(f'LIVE AT END: {len(grid)}')
