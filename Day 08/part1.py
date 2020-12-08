import sys
input_lines = open(sys.argv[1]).read().split('\n')

visited_lines = set()
acc = 0
i = 0

while i < len(input_lines):
	line = input_lines[i]
	print(line)
	if line == '': continue
	if i in visited_lines:
		break
	inst, arg = line.split(' ')
	arg = int(arg)
	if inst == 'jmp':
		i += arg - 1
	elif inst == 'acc':
		acc += arg
	visited_lines.add(i)
	i += 1

print(acc)
