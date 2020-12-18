import pyparsing as pp
import functools
import sys
import operator

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

num = pp.pyparsing_common.integer

OPS = {
	'+': operator.add,
	'*': operator.mul,
}
def eval_math(tokens):
	ret = tokens[0]
	for op, n in zip(tokens[1::2], tokens[2::2]):
		ret = OPS[op](ret, n)
	return ret

p1_expr      = pp.Forward()
p1_operator  = pp.oneOf('+ *')
p1_math_expr = (p1_expr + pp.ZeroOrMore(p1_operator + p1_expr)).setParseAction(eval_math)
p1_expr    <<= (pp.Suppress('(') + p1_math_expr + pp.Suppress(')')) | num

p2_expr   = pp.Forward()
p2_add    = pp.Forward()
p2_mul    = (p2_add + pp.ZeroOrMore(pp.Literal('*') + p2_add)).setParseAction(eval_math)
p2_add  <<= (p2_expr + pp.ZeroOrMore(pp.Literal('+') + p2_expr)).setParseAction(eval_math)
p2_expr <<= (pp.Suppress('(') + p2_mul + pp.Suppress(')')) | num

results = []

for line in input_lines:
	print(f'{line} = ', end='')
	p1_res = p1_math_expr.parseString(line, parseAll=True)[0]
	p2_res = p2_mul.parseString(line, parseAll=True)[0]
	results.append((p1_res, p2_res))
	print(f'{p1_res}, {p2_res}')

print(f'{sum(result[0] for result in results)}, {sum(result[1] for result in results)}')
