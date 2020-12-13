import sys
input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

timestamp = int(input_lines[0])
bus_ids = [int(bus_id) for bus_id in input_lines[1].split(',') if bus_id != 'x' ]

min_wait = 2**32
min_bus = -1
for bus in bus_ids:
	wait = bus - (timestamp % bus)
	if wait < min_wait:
		min_wait = wait
		min_bus = bus
	print(bus, wait)

print(min_wait * min_bus)
