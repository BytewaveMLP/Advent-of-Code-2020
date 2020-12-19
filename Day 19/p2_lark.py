import sys
import lark

rules, messages = open(sys.argv[1]).read().split('\n\n')

rules = rules.replace('8: 42', '8: 42 | 42 8').replace('11: 42 31', '11: 42 31 | 42 11 31')
rules = rules.translate(str.maketrans('0123456789', 'abcdefghij'))
parser = lark.Lark(rules, start='a')

valid_count = 0
for message in messages.split('\n'):
	if message == '': continue
	print(message)
	try:
		parser.parse(message)
		print('Valid!')
		valid_count += 1
	except lark.LarkError as err:
		print('Invalid!')
		# print(err)
	print()

print(valid_count)
