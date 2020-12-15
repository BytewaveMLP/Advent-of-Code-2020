import sys
input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']
numbers = [int(n) for n in input_lines[0].split(',')]

LIMIT = 30000000

last_spoken = {}
for i, n in enumerate(numbers):
	last_spoken[n] = i + 1

last_last_said = 0
last_said = numbers[-1]

print(last_spoken)

for turn in range(len(numbers), LIMIT):
	last_last_said = last_said
	if last_said in last_spoken:
		last_said = turn - last_spoken[last_said]
	else:
		last_said = 0
	last_spoken[last_last_said] = turn

print(last_said)
