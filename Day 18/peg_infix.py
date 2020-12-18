import pyparsing as pp
import functools
import sys
import operator

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

num = pp.pyparsing_common.integer

def p1_eval_math(tokens):
	tokens = tokens[0]
	ret = tokens[0]
	for op, n in zip(tokens[1::2], tokens[2::2]):
		if op == '*': ret *= n
		elif op == '+': ret += n
	return ret

p1_expr = pp.infixNotation(num, [
	(pp.oneOf('+ *'), 2, pp.opAssoc.LEFT, p1_eval_math)
])

add_all = functools.partial(functools.reduce, operator.add)
mul_all = functools.partial(functools.reduce, operator.mul)

p2_expr = pp.infixNotation(num, [
	(pp.Literal('+'), 2, pp.opAssoc.LEFT, lambda a: add_all(a[0][::2])),
	(pp.Literal('*'), 2, pp.opAssoc.LEFT, lambda a: mul_all(a[0][::2])),
])

p1 = 0
p2 = 0

for line in input_lines:
	print(f'{line} = ', end='')
	p1_result = p1_expr.parseString(line, parseAll=True)[0]
	p2_result = p2_expr.parseString(line, parseAll=True)[0]
	p1 += p1_result
	p2 += p2_result
	print(p1_result, end='')
	print(', ', end='')
	print(p2_result)

print(f'{p1}, {p2}')
