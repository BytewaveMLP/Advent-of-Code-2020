import sys
import itertools
import pyparsing as pp

input_lines = open(sys.argv[1]).read().split('\n')

raw_rules = list(itertools.takewhile(lambda l: l != '', input_lines))
received_messages = list(itertools.takewhile(lambda l: l != '', input_lines[len(raw_rules) + 1:]))

trace = lambda *x, **y: [x[-1], print(*x, **y)][0]

rules = {}

for raw_rule in raw_rules:
	rule_name, raw_rule_def = raw_rule.split(': ')

	rule_def = raw_rule_def.split(' | ')
	if rule_name not in rules: rules[rule_name] = pp.Forward()
	if len(rule_def) == 1 and rule_def[0].startswith('"'): # single character
		c = rule_def[0][1] # extract character
		rules[rule_name] <<= pp.Char(c)
		continue
	rule_def_exp = None
	for sub in rule_def:
		all_needed = sub.split(' ')
		pattern_for_group = None
		for referenced in all_needed:
			if referenced not in rules:
				rules[referenced] = pp.Forward()
			if not pattern_for_group:
				pattern_for_group = rules[referenced] # get first referenced as pattern start
			else:
				pattern_for_group += rules[referenced] # and append future ones
		if not rule_def_exp:
			rule_def_exp = pattern_for_group
		else:
			rule_def_exp |= pattern_for_group
		rule_def_exp.setName(rule_name)#.setParseAction(trace)
	rules[rule_name] <<= rule_def_exp

rules['0']   = pp.Forward()
rules['0'] <<= (rules['42'] + rules['0'] + rules['31']) | rules['42'][1, ...]

print(rules)

valid_count = 0
for message in received_messages:
	print(message)
	if message == rules['0']:
		print('Valid!')
		valid_count += 1
	else:
		print('Invalid!')
	print()

print(valid_count)
