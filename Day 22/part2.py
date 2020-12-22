import sys

player_cards = [[int(c) for c in deck.split('\n')[1:] if c != ''] for deck in open(sys.argv[1]).read().split('\n\n') if deck != '']

print(player_cards)

def encode(hands):
	return '|'.join(','.join(str(c) for c in hand) for hand in hands)

def rotate(lst, n=1):
	return lst[n:] + lst[:n]

def round(hands, previous_configs, depth, round_no):
	print(f'--- Game {depth}, round {round_no} ---')
	hands_cur = encode(hands)
	p1 = hands[0][0]
	p2 = hands[1][0]
	winner = -1
	if len(hands[0]) > p1 and len(hands[1]) > p2:
		print('Starting a subgame to determien the results...')
		winner = game([hands[0][1:p1+1], hands[1][1:p2+1]], depth + 1)
	else:
		if p1 > p2:
			winner = 0
		else:
			winner = 1

	print(f'Player {winner + 1} wins round {round_no} of game {depth}!')
	loser = (winner + 1) % 2
	hands[winner] = rotate(hands[winner])
	hands[winner].append(hands[loser].pop(0))
	previous_configs.add(hands_cur)

def game(hands, depth=1):
	previous_configs = set()
	round_no = 1
	while len(hands[0]) != 0 and len(hands[1]) != 0:
		if encode(hands) in previous_configs:
			print(f'Player 1 wins game {depth} due to the infinite loop fix.')
			return 0 # p1 instantly wins
		round(hands, previous_configs, depth, round_no)
	if len(hands[1]) == 0:
		print(f'Player 1 wins game {depth}!')
		return 0
	else:
		print(f'Player 2 wins game {depth}!')
		return 1

def score(hand):
	return sum((p+1) * card for p, card in enumerate(hand[::-1]))

winner = game(player_cards)

print(f'Player {winner + 1} wins the final game!!!')
print(score(player_cards[winner]))
