import sys

player_cards = [[int(c) for c in deck.split('\n')[1:] if c != ''] for deck in open(sys.argv[1]).read().split('\n\n') if deck != '']

print(player_cards)

def rotate(lst, n=1):
	return lst[n:] + lst[:n]

def turn():
	p1 = player_cards[0][0]
	p2 = player_cards[1][0]
	if p1 > p2:
		print('Player 1 wins the round!')
		player_cards[0] = rotate(player_cards[0], 1)
		player_cards[0].append(player_cards[1].pop(0))
	else:
		print('Player 2 wins the round!')
		player_cards[1] = rotate(player_cards[1], 1)
		player_cards[1].append(player_cards[0].pop(0))

def score(hand):
	return sum((p+1) * card for p, card in enumerate(hand[::-1]))

while len(player_cards[0]) != 0 and len(player_cards[1]) != 0:
	turn()
	print(player_cards)

if len(player_cards[0]) == 0:
	print(score(player_cards[1]))
else:
	print(score(player_cards[0]))
