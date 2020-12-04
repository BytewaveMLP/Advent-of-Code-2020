import sys
input_lines = open(sys.argv[1]).read().split('\n')

total_trees = 1

# over, down
steps = [
	(1, 1),
	(3, 1),
	(5, 1),
	(7, 1),
	(1, 2),
]

for step in steps:
	trees = 0
	pos = 0
	for i in range(0, len(input_lines), step[1]):
		line = input_lines[i]
		if line == '': continue
		if line[pos] == '#':
			trees += 1

		pos = (pos + step[0]) % len(line)
	print(trees)
	total_trees *= trees

print(total_trees)
