import sys
input_lines = open(sys.argv[1]).read().split('\n')

answered_questions = set()
count_sum = 0

for line in input_lines:
	if line == '':
		# reset
		count_sum += len(answered_questions)
		print(answered_questions)
		print(len(answered_questions))
		answered_questions = set()
		continue

	[answered_questions.add(q) for q in line]

print(count_sum)
