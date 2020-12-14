import sys
import re
from collections import defaultdict
input_lines = open(sys.argv[1]).read().split('\n')[:-1]

mem = defaultdict(lambda _: 0)
mem_assign_exp = re.compile(r'^mem\[(\d+)\] = (\d+)$')

mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
for line in input_lines:
	print(line)

	if line.startswith('mask'):
		mask = line.split(' = ')[1]
		continue

	print(mask)
	matches = mem_assign_exp.match(line)
	addr = list(bin(int(matches[1]))[2:].zfill(len(mask)))
	val = int(matches[2])
	print(''.join(addr))

	for i, b in enumerate(mask):
		addr[i] = addr[i] if b == '0' else mask[i]

	print(''.join(addr))

	x_count = addr.count('X')
	for n in range(2**x_count):
		addr_copy = [b for b in addr]
		bin_x = bin(n)[2:].zfill(x_count)
		assigned_xs = 0
		for i, b in enumerate(addr):
			addr_copy[i] = b if b != 'X' else bin_x[-(assigned_xs+1)]
			if b == 'X': assigned_xs += 1
		addr_copy = int(''.join(addr_copy), base=2)
		mem[addr_copy] = val

print('SUM =', sum(mem.values()))
