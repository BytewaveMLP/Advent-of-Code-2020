import sys
input_lines = open(sys.argv[1]).read().split('\n')

required_fields = [
	'byr',
	'iyr',
	'eyr',
	'hgt',
	'hcl',
	'ecl',
	'pid',
	# 'cid',
]

has_required_fields = { k: False for k in required_fields }

valid_passports = 0

for line in input_lines:
	if line == '':
		valid = True
		for k in has_required_fields:
			if not has_required_fields[k]:
				valid = False
				break
		if valid: valid_passports += 1
		has_required_fields = { k: False for k in required_fields }
		continue

	fields = line.split(' ')
	field_names = [ v.split(':')[0] for v in fields ]

	for f in field_names:
		has_required_fields[f] = True

print(valid_passports)
