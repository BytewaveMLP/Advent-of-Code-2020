import sys
import re

input_lines = open(sys.argv[1]).read().split('\n')
RULE_DEF_REGEX = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')
rules = {}
tickets_start = 0

print('Finding field defs:')

for i, line in enumerate(input_lines):
	if line == '':
		tickets_start = i + 5
		break

	print(line)
	matches = RULE_DEF_REGEX.match(line)
	rules[matches[1]] = [
		range(int(matches[2]), int(matches[3]) + 1),
		range(int(matches[4]), int(matches[5]) + 1)
	]

	print(line)
	print(matches[1], rules[matches[1]])

print('Finding invalid:')

def find_invalid(line):
	fields       = {int(n) for n in line.split(',')}
	valid_fields = set()
	for rule in rules:
		for rng in rules[rule]:
			for n in fields:
				if n in rng:
					valid_fields.add(n)
	return fields - valid_fields

sum = 0
for i, line in enumerate(input_lines[tickets_start:-1]):
	print(line)
	invalid = find_invalid(line)
	print(invalid)
	if len(invalid) > 0:
		sum += invalid.pop()

print(sum)
