import sys
import re
input_lines = open(sys.argv[1]).read().split('\n')[:-1]

mem = {}
mem_assign_exp = re.compile(r'^mem\[(\d+)\] = (\d+)$')

mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
for line in input_lines:
	print(line)

	if line.startswith('mask'):
		mask = line.split(' = ')[1]
		continue

	print(mask)
	matches = mem_assign_exp.match(line)
	addr = int(matches[1])
	val = list(bin(int(matches[2]))[2:].zfill(len(mask)))
	print(''.join(val))

	for i, b in enumerate(mask):
		val[i] = val[i] if b == 'X' else b

	print(''.join(val))
	val = int(''.join(val), base=2)
	print(val)
	mem[addr] = val

print('SUM =', sum(mem.values()))
