import sys
input_lines = [line for line in open(sys.argv[1]).read().split('\n') if line != '']

def visible_from(state, x, y):
	old_x = x
	old_y = y
	visible = []
	for xp in range(-1, 2):
		for yp in range(-1, 2):
			if xp == 0 and yp == 0: continue
			x = old_x + xp
			y = old_y + yp
			while 0 <= x < len(state[0]) and 0 <= y < len(state):
				if state[y][x] != '.':
					visible.append((x, y))
					break
				x += xp
				y += yp
	return visible

def iterate(state):
	new_state = [str(line) for line in state]
	for y in range(0, len(state)):
		for x in range(0, len(state[0])):
			if state[y][x] == '.':
				continue
			elif state[y][x] == 'L':
				found_full = False
				visible_seats = visible_from(state, x, y)
				for seat in visible_seats:
					if state[seat[1]][seat[0]] == '#':
						found_full = True
				if not found_full:
					new_state[y] = new_state[y][0:x] + '#' + new_state[y][x+1:len(new_state[y])]
			elif state[y][x] == '#':
				found_occupied = 0
				visible_seats = visible_from(state, x, y)
				for seat in visible_seats:
					if state[seat[1]][seat[0]] == '#':
						found_occupied += 1
				if found_occupied >= 5:
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
