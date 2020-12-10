import sys
input_lines = open(sys.argv[1]).read().split('\n')
input_lines = [int(n) for n in input_lines if n != '']
input_lines.append(0)
input_lines.append(max(input_lines) + 3)
input_lines.sort()

arrangements = { j: 0 for j in input_lines }
arrangements[0] = 1

for adapter in input_lines:
	for step in range(1, 4):
		if adapter + step in arrangements:
			arrangements[adapter + step] += arrangements[adapter]

print(max(arrangements.values()))
