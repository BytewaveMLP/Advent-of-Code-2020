import sys
import math
import functools
input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

sign = functools.partial(math.copysign, 1)

cur_position = [0, 0]
cur_direction = [0, 1] # east

def rotate(direction, deg, left=False):
	while deg != 0:
		# rotate right in steps of 90 degrees
		if abs(direction[0]) == 1:
			direction[1] = direction[0]
			direction[0] = 0
		else:
			direction[0] = -direction[1]
			direction[1] = 0

		deg -= 90

	return direction

for line in input_lines:
	n = int(line[1:])
	if line[0] == 'N':
		cur_position[0] += n
	elif line[0] == 'S':
		cur_position[0] -= n
	elif line[0] == 'E':
		cur_position[1] += n
	elif line[0] == 'W':
		cur_position[1] -= n
	elif line[0] == 'R':
		cur_direction = rotate(cur_direction, n)
	elif line[0] == 'L':
		cur_direction = rotate(cur_direction, 360 - n)
	elif line[0] == 'F':
		for part, coord in enumerate(cur_direction):
			cur_position[part] += n * coord
	print(line)
	print(cur_position)
	print(cur_direction)

print(abs(cur_position[0]) + abs(cur_position[1]))
