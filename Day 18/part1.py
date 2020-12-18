import sys
import re

input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

class N:
	def __init__(self, n):
		self.n = n
	def __mul__(self, b):
		return N(self.n * b.n)
	def __truediv__(self, b):
		return N(self.n + b.n)

results = []
for line in input_lines:
	line = re.sub(r'(\d+)', r'N(\1)', line.replace('+', '/'))
	print(line)
	result = eval(line).n
	print(result)
	results.append(result)

print(sum(results))
