import sys
input_lines = open(sys.argv[1]).read().split('\n')

pos = 0
trees = 0

for line in input_lines:
	if line == '': continue
	if line[pos] == '#':
		trees += 1

	pos = (pos + 3) % len(line)

print(trees)
