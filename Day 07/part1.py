import sys
import re
input_lines = open(sys.argv[1]).read().split('\n')

bag_contained_rules = {}

for line in input_lines:
	if line == '': continue
	parts = line.split(' contain ')
	if parts[1].startswith('no'): continue

	container_bag = parts[0].replace(' bags', '')
	contained_bags_raw = [s.strip('.') for s in parts[1].split(', ')]
	contained_bags_raw = [s.split(' ', 1) for s in contained_bags_raw]
	contained_bags = [(int(p[0]), re.sub(' bags?', '', p[1])) for p in contained_bags_raw]

	for bag in contained_bags:
		if not bag_contained_rules.get(bag[1]):
			bag_contained_rules[bag[1]] = [(bag[0], container_bag)]
		else:
			bag_contained_rules[bag[1]].append((bag[0], container_bag))

print(bag_contained_rules)

def bags_which_contain(target):
	print(target)
	target_contained_by = bag_contained_rules.get(target)
	print(target_contained_by)

	bags_containing = set()
	bags_containing.add(target)
	if not target_contained_by:
		return bags_containing
	for container in target_contained_by:
		bags_containing = bags_containing.union(bags_which_contain(container[1]))
	print(bags_containing)
	return bags_containing

print(len(bags_which_contain('shiny gold')) - 1)
