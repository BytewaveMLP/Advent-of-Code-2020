import sys
import math
input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

def lcm(a, b):
	return abs(a * b) // math.gcd(a, b)

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, _ = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

bus_ids = input_lines[1].split(',')
bus_ids = [(i, int(bus)) for i, bus in enumerate(bus_ids) if bus != 'x']
print(bus_ids)

timestamp = 2
cur_lcm = 1
for i, bus in bus_ids:
	timestamp += cur_lcm * (((-i - timestamp) * modinv(cur_lcm, bus)) % bus)
	cur_lcm = lcm(cur_lcm, bus)

print(timestamp)
