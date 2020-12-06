import sys
input_lines = open(sys.argv[1]).read().split('\n')

answered_questions = []
count_sum = 0

for line in input_lines:
	if line == '':
		# reset
		all_answered = answered_questions[0]
		if len(answered_questions) > 1:
			all_answered = answered_questions[0].intersection(*answered_questions[1:])
		count_sum += len(all_answered)
		print(answered_questions)
		print(len(answered_questions))
		answered_questions = []
		continue

	answered_questions.append(set(line))

print(count_sum)
