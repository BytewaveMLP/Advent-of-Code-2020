import sys

with open(sys.argv[1]) as f:
	lines = f.readlines()

valid = 0

for line in lines:
	line = line.strip()
	[_range, char_colon, pwd] = line.split(' ')
	_range = _range.split('-')
	range_low = int(_range[0])
	range_hi  = int(_range[1]) + 1
	_range = range(range_low, range_hi)
	char = char_colon.rstrip(':')

	print(_range, char, pwd, pwd.count(char))

	if pwd.count(char) in _range:
		valid += 1
		print('valid')
	else:
		print('invalid')

print(valid)
