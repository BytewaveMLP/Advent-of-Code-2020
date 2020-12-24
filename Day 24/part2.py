import sys
import operator
import copy
from collections import defaultdict

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

DIRECTION_TO_NEIGHBOR_OFFSET = {
	'e': (1, 0),
	'se': (1, -1),
	'sw': (0, -1),
	"w": (-1, 0),
	'nw': (-1, 1),
	'ne': (0, 1),
}

NEIGHBOR_OFFSETS = list(DIRECTION_TO_NEIGHBOR_OFFSET.values())

tile_states = defaultdict(bool) # False = white, True = black

addpos = lambda x, y: tuple(map(operator.add, x, y))

print('Setting initial state...')
for line in input_lines:
	pos = (0, 0)
	while line != '':
		for d in DIRECTION_TO_NEIGHBOR_OFFSET:
			if line.startswith(d):
				pos = addpos(pos, DIRECTION_TO_NEIGHBOR_OFFSET[d])
				line = line[len(d):]
	tile_states[pos] = not tile_states[pos]

state = {pos for pos in tile_states if tile_states[pos]}

Point = tuple[int, int]
Grid = dict[Point, bool]

def live_around(grid: Grid, coord: Point) -> int:
	"""Count the number of living cells surrounding a grid coordinate"""
	return sum(1 for neighbor_offset in NEIGHBOR_OFFSETS if addpos(coord, neighbor_offset) in grid)

def kill(grid: Grid, coord: Point) -> bool:
	"""Tests if the cell at coord should be killed"""
	active_count = live_around(grid, coord)
	return active_count == 0 or active_count > 2

def revive(grid: Grid, coord: Point) -> Grid:
	"""Generates a set of all cells which can be revived near coord"""
	revives = set()

	for offset in NEIGHBOR_OFFSETS:
		possible_revive = addpos(coord, offset)
		if possible_revive in grid: continue
		active_count = live_around(grid, possible_revive)

		if active_count == 2:
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

print(f'Day 0: {len(state)}')

for i in range(100):
	state = iterate(state)
	print(f'Day {i+1}: {len(state)}')

print(len(state))
