import sys
import math

card_pk, door_pk = [int(n) for n in open(sys.argv[1]).read().split('\n') if n != '']

print(card_pk, door_pk)

DIV_CONST = 20201227

def transform(n: int, subj: int) -> int:
	n *= subj
	n %= DIV_CONST
	return n

def get_loop_sz(subj: int, target: int) -> int:
	value = 1
	loop_count = 0
	while value != target:
		value = transform(value, subj)
		loop_count += 1
	return loop_count

card_loop_count = get_loop_sz(7, card_pk)
door_loop_count = get_loop_sz(7, door_pk)
enc_key = pow(card_pk, door_loop_count, DIV_CONST)

print(card_loop_count, door_loop_count, enc_key)
