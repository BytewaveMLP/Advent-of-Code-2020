import sys
input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

def iterate(state):
	new_state = [str(line) for line in state]
	for y in range(0, len(state)):
		for x in range(0, len(state[0])):
			if state[y][x] == '.':
				continue
			elif state[y][x] == 'L':
				found_full = False
				for xp in range(-1 if x > 0 else 0, 2 if x < len(state[0]) - 1 else 1):
					for yp in range(-1 if y > 0 else 0, 2 if y < len(state) - 1 else 1):
						if xp == 0 and yp == 0: continue
						if state[y+yp][x+xp] == '#':
							found_full = True
							break
				if not found_full:
					new_state[y] = new_state[y][0:x] + '#' + new_state[y][x+1:len(new_state[y])]
			elif state[y][x] == '#':
				found_occupied = 0
				for xp in range(-1 if x > 0 else 0, 2 if x < len(state[0]) - 1 else 1):
					for yp in range(-1 if y > 0 else 0, 2 if y < len(state) - 1 else 1):
						if xp == 0 and yp == 0: continue
						if state[y+yp][x+xp] == '#':
							found_occupied += 1
				if found_occupied >= 4:
					new_state[y] = new_state[y][0:x] + 'L' + new_state[y][x+1:len(new_state[y])]
	return new_state

def print_state(state):
	for l in state:
		print(l)

state = input_lines
print_state(state)
new_state = []
while True:
	print('-' * len(state[0]))
	new_state = iterate(state)
	print_state(new_state)
	if new_state == state:
		break
	state = new_state

occupied = 0
for y in range(len(state)):
	for x in range(len(state[0])):
		if state[y][x] == '#':
			occupied += 1

print(occupied)
