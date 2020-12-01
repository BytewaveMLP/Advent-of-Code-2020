import sys

with open(sys.argv[1]) as f:
	lines = f.readlines()

expense_report = [int(n) for n in lines]

for a in expense_report:
	if a > 2020: continue
	for b in expense_report:
		if b > 2020: continue
		for c in expense_report:
			if a + b + c == 2020:
				print(a * b * c)
				exit(0)
