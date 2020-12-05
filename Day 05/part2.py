import sys
input_lines = open(sys.argv[1]).read().split('\n')

seen_seats = set()

NUM_COLS = 8
NUM_ROWS = 128

for line in input_lines:
	if line == '': continue
	seat_id = int(''.join(['1' if c in 'BR' else '0' for c in line]), base=2)
	print(line, seat_id)
	seen_seats.add(seat_id)

seat_range = range(min(*seen_seats), max(*seen_seats)+1)
for n in seat_range:
	if n not in seen_seats:
		print(n)
