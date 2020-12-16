import sys
import re

input_lines = open(sys.argv[1]).read().split('\n')
RULE_DEF_REGEX = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')
rules = {}
tickets_start = 0
my_ticket_start = 0

print('Finding field defs:')

for i, line in enumerate(input_lines):
	if line == '':
		my_ticket_start = i + 2
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

my_ticket = [int(n) for n in input_lines[my_ticket_start].split(',')]

def find_invalid(fields):
	fields = set(fields)
	valid_fields = set()
	for rule in rules:
		for rng in rules[rule]:
			for n in fields:
				if n in rng:
					valid_fields.add(n)
	return fields - valid_fields

print('Determine order:')

possible_fields = [
	[rule for rule in rules] for _ in range(len(my_ticket))
]

for i, line in enumerate(input_lines[tickets_start-1:-1]):
	if line == 'nearby tickets:': line = input_lines[my_ticket_start] # hack to consider own ticket as well
	print(line)
	ticket = [int(n) for n in line.split(',')]
	invalid = find_invalid(ticket)
	if len(invalid) > 0: continue
	for i in range(len(ticket)):
		for rule in possible_fields[i]:
			if rule not in possible_fields[i]: continue
			valid_for = False
			for rng in rules[rule]:
				if ticket[i] in rng:
					valid_for = True
			if not valid_for:
				possible_fields[i].remove(rule)

while sum([len(possible) for possible in possible_fields]) > len(rules):
	for i, possible in enumerate(possible_fields):
		if len(possible) == 1:
			actual = possible[0]
			for j in range(len(possible_fields)):
				if i == j: continue
				if actual in possible_fields[j]: possible_fields[j].remove(actual)

print(possible_fields)

mul = 1
for i, field in enumerate(possible_fields):
	if len(field) == 0: continue
	if not field[0].startswith('departure'): continue
	print(field, my_ticket[i])
	mul *= my_ticket[i]

print(mul)
