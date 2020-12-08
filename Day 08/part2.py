import sys
raw_input_lines = open(sys.argv[1]).read().split('\n')

acc = 0
working = False
changed_lines = set()

while not working:
	visited_lines = set()
	acc = 0
	i = 0

	working = True
	is_first_jmp_or_nop = True

	print(changed_lines)

	input_lines = [str(s) for s in raw_input_lines]

	while i < len(input_lines):
		cur_line = i
		line = input_lines[i]
		if line == '':
			i += 1
			continue
		print(f'{cur_line}:\t{line}')
		if i in visited_lines:
			print(f'got to the same line {i} again')
			working = False
			break
		inst, str_arg = line.split(' ')
		arg = int(str_arg)
		if inst == 'jmp':
			if is_first_jmp_or_nop and i not in changed_lines:
				print(f'changed {cur_line} from jmp to nop')
				input_lines[cur_line] = f'nop {str_arg}'
				is_first_jmp_or_nop = False
				changed_lines.add(cur_line)
			else:
				i += arg - 1
		elif inst == 'acc':
			acc += arg
		elif inst == 'nop' and is_first_jmp_or_nop and i not in changed_lines:
			print(f'changed {cur_line} from nop to jmp')
			input_lines[cur_line] = f'jmp {str_arg}'
			is_first_jmp_or_nop = False
			changed_lines.add(cur_line)
			i += arg - 1
		visited_lines.add(cur_line)
		i += 1

print(acc)
