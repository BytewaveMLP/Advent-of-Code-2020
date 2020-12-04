import sys

with open(sys.argv[1]) as f:
	lines = f.readlines()

valid = 0

for line in lines:
	line = line.strip()
	[_range, char_colon, pwd] = line.split(' ')
	_range = _range.split('-')
	range_low = int(_range[0]) - 1
	range_hi  = int(_range[1]) - 1
	char = char_colon.rstrip(':')

	print(_range, char, pwd, pwd.count(char))

	if pwd[range_low] == pwd[range_hi] and pwd[range_low] == char:
		continue

	if pwd[range_low] != char and pwd[range_hi] != char:
		continue

	valid += 1

print(valid)
