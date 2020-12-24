import sys
import operator
from collections import defaultdict

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

direction_translations = {
	'e': (1, 0),
	'se': (1, -1),
	'sw': (0, -1),
	"w": (-1, 0),
	'nw': (-1, 1),
	'ne': (0, 1),
}

tile_states = defaultdict(bool) # False = white, True = black

addpos = lambda x, y: tuple(map(operator.add, x, y))

for line in input_lines:
	print(line)
	pos = (0, 0)
	while line != '':
		for d in direction_translations:
			if line.startswith(d):
				print(d)
				pos = addpos(pos, direction_translations[d])
				print(pos)
				line = line[len(d):]
	tile_states[pos] = not tile_states[pos]

print(sum(1 for pos in tile_states if tile_states[pos]))
