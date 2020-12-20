import sys
import itertools
import functools
import operator

def rotate(matrix):
	return [list(xs) for xs in zip(*matrix[::-1])]

def flip(matrix):
	return [xs[::-1] for xs in matrix]

def borders(matrix):
	return list(''.join(border) for border in
		[[l[0] for l in matrix], # left
		matrix[0], # top
		[l[-1] for l in matrix], # right
		matrix[-1]]
	)

raw_image_parts = [part.strip() for part in open(sys.argv[1]).read().split('\n\n')]
parts = {}
for raw_part in raw_image_parts:
	raw_part_lines = raw_part.splitlines()
	part_id = int(raw_part_lines[0].split(' ')[1].strip(':'))
	part = [list(line) for line in raw_part_lines[1:]]
	parts[part_id] = part
	print(part_id, part)

corners = []

for part_id in parts:
	part = parts[part_id]
	other_borders = []
	for other_id in parts:
		if other_id == part_id: continue
		other_borders += borders(parts[other_id])
	other_borders += [border[::-1] for border in other_borders]
	other_borders = set(other_borders)
	part_borders = borders(part)
	part_borders += [border[::-1] for border in part_borders]
	part_borders = set(part_borders)
	uncommon_borders = part_borders - other_borders
	print(uncommon_borders)
	if len(uncommon_borders) == 4: # corner
		corners.append(part_id)

print(functools.reduce(operator.mul, corners))
