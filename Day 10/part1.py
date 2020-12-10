import sys
input_lines = open(sys.argv[1]).read().split('\n')
input_lines = [int(n) for n in input_lines if n != '']
input_lines.sort()

device_joltage = input_lines[-1] + 3

differences = {
	1: 1,
	2: 1,
	3: 1,
}

for adapter_n in range(1, len(input_lines)):
	differences[abs(input_lines[adapter_n] - input_lines[adapter_n - 1])] += 1

print(differences)
print(differences[1] * differences[3])
