import sys
raw_input_lines = open(sys.argv[1]).read().split('\n')

input_lines = [int(line) for line in raw_input_lines if line != '']

PREAMBLE_SIZE = 25

def two_sum(arr, n):
	for a in arr:
		if a > n: continue
		for b in arr:
			if a == b: continue
			if a + b == n:
				return a, b

	return None

for n in range(PREAMBLE_SIZE, len(input_lines)):
	preamble = input_lines[n-PREAMBLE_SIZE:n]
	print(preamble)
	nums = two_sum(preamble, input_lines[n])
	if not nums:
		print(input_lines[n])
		break
	print(f'{nums[0]} + {nums[1]} = {input_lines[n]}')
