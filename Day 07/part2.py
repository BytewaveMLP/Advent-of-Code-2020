import sys
import re
input_lines = open(sys.argv[1]).read().split('\n')

bag_container_rules = {}

for line in input_lines:
	if line == '': continue
	parts = line.split(' contain ')
	if parts[1].startswith('no'): continue
	container = re.sub(r' bags?$', '', parts[0])
	contained_raw = [re.sub(r' bags?\.?$', '', bag).split(' ', 1) for bag in parts[1].split(', ')]
	contained = [(int(_raw[0]), _raw[1]) for _raw in contained_raw]
	bag_container_rules[container] = contained

print(bag_container_rules)

def bag_contains_n(bag):
	if not bag_container_rules.get(bag): return 1
	n_contained = 1
	for contained in bag_container_rules[bag]:
		print(bag, contained)
		n_contained += contained[0] * bag_contains_n(contained[1])
		print(n_contained)
	return n_contained

print(bag_contains_n('shiny gold')-1)
