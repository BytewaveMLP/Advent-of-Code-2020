import sys
import math
import functools
input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

sign = functools.partial(math.copysign, 1)

cur_position = [0, 0]
wpt_position = [1, 10]

def rotate(position, deg, left=False):
	rad = math.radians(-deg)
	s = math.trunc(math.sin(rad))
	c = math.trunc(math.cos(rad))

	position = [position[0] * c - position[1] * s, position[0] * s + position[1] * c]

	return position

for line in input_lines:
	n = int(line[1:])
	if line[0] == 'N':
		wpt_position[0] += n
	elif line[0] == 'S':
		wpt_position[0] -= n
	elif line[0] == 'E':
		wpt_position[1] += n
	elif line[0] == 'W':
		wpt_position[1] -= n
	elif line[0] == 'R':
		wpt_position = rotate(wpt_position, 360 - n)
	elif line[0] == 'L':
		wpt_position = rotate(wpt_position, n)
	elif line[0] == 'F':
		cur_position[0] += n * wpt_position[0]
		cur_position[1] += n * wpt_position[1]

	print(line)
	print(cur_position)
	print(wpt_position)

print(abs(cur_position[0]) + abs(cur_position[1]))
