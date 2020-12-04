import sys
import re
input_lines = open(sys.argv[1]).read().split('\n')

def valid_hgt(v):
	matches = re.match(r'(\d+)(cm|in)', v)
	if not matches: return False

	measure = int(matches.group(1))

	if matches.group(2) == 'cm':
		return 150 <= measure <= 193

	return 59 <= measure <= 76

field_validators = {
	'byr': lambda v: 1920 <= int(v) <= 2002,
	'iyr': lambda v: 2010 <= int(v) <= 2020,
	'eyr': lambda v: 2020 <= int(v) <= 2030,
	'hgt': valid_hgt,
	'hcl': lambda v: re.match(r'#[0-9a-f]{6}', v) != None,
	'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
	'pid': lambda v: len(str(v)) == 9,
	'cid': lambda v: True
}

valid_passports = 0
field_values = {}

for line in input_lines:
	if line == '':
		valid = True
		for k in field_validators:
			if not field_validators[k](field_values.get(k, '0')):
				valid = False
				break
		if valid: valid_passports += 1
		field_values = {}
		continue

	fields = line.split(' ')
	field_kv = [ fields.split(':') for fields in fields ]
	field_values = { **field_values, **{ field[0]: field[1] for field in field_kv } }

print(valid_passports)
