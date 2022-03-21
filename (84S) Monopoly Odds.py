# In the game, Monopoly, the standard board is set up in the following way:
# GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	J
# H2										C1
# T2									 	U1
# H1									 	C2
# CH3										C3
# R4										R2
# G3										D1
# CC3									 	CC2
# G2										D2
# G1	 									D3
# GTJ	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP

# A player starts on the GO square and adds the scores on two 6-sided dice
# to determine the number of squares they advance in a clockwise direction.
#Without any further rules we would expect to visit each square with equal
# probability: 2.5%. However, landing on G2J (Go To Jail), CC
# (community chest), and CH (chance) changes this distribution.
# In addition to G2J, and one card from each of CC and CH, that orders 
# the player to go directly to jail, if a player rolls three consecutive
# doubles, they do not advance the result of their 3rd roll. Instead they
# proceed directly to jail.

# At the beginning of the game, the CC and CH cards are shuffled.
# When a player lands on CC or CH they take a card from the top of the
# respective pile and, after following the instructions, it is returned to
# the bottom of the pile. There are sixteen cards in each pile, but for the
# purpose of this problem we are only concerned with cards that order a
# movement; any instruction not concerned with movement will be ignored and
# the player will remain on the CC/CH square.

# Community Chest (2/16 cards):
# Advance to GO
# Go to JAIL

# Chance (10/16 cards):
# Advance to GO
# Go to JAIL
# Go to C1
# Go to E3
# Go to H2
# Go to R1
# Go to next R (railway company)
# Go to next R
# Go to next U (utility company)
# Go back 3 squares.

# The heart of this problem concerns the likelihood of visiting a
# particular square. That is, the probability of finishing at that square
# after a roll. For this reason it should be clear that, with the exception
# of G2J for which the probability of finishing on it is zero, the CH squares
# will have the lowest probabilities, as 5/8 request a movement to another
# square, and it is the final square that the player finishes at on each roll
# that we are interested in. We shall make no distinction between
# "Just Visiting" and being sent to JAIL, and we shall also ignore
# the rule about requiring a double to "get out of jail", assuming
# that they pay to get out on their next turn.

# By starting at GO and numbering the squares sequentially from 00 to 39
# we can concatenate these two-digit numbers to produce strings
# that correspond with sets of squares.

# Statistically it can be shown that the three most popular squares,
# in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and
# GO (3.09%) = Square 00. So these three most popular squares can be listed
# with the six-digit modal string: 102400.

# If, instead of using two 6-sided dice, two 4-sided dice are used,
# find the six-digit modal string.

import random

board_spaces = {
	0 : "GO",
	1 : "A1",
	2 : "CC1",
	3 : "A2",
	4 : "T1",
	5 : "R1",
	6 : "B1",
	7 : "CH1",
	8 : "B2",
	9 : "B3",
	10 : "JAIL",
	11 : "C1",
	12 : "U1",
	13 : "C2",
	14 : "C3",
	15 : "R2",
	16 : "D1",
	17 : "CC2",
	18 : "D2",
	19 : "D3",
	20 : "FP",
	21 : "E1",
	22 : "CH2",
	23 : "E2",
	24 : "E3",
	25 : "R3",
	26 : "F1",
	27 : "F2",
	28 : "U2",
	29 : "F3",
	30 : "GTJ",
	31 : "G1",
	32 : "G2",
	33 : "CC3",
	34 : "G3",
	35 : "R4",
	36 : "CH3",
	37 : "H1",
	38 : "T2",
	39 : "H2"
}

space_visitations = {
	"GO"   : 0,
	"A1"   : 0,
	"CC1"  : 0,
	"A2"   : 0,
	"T1"   : 0,
	"R1"   : 0,
	"B1"   : 0,
	"CH1"  : 0,
	"B2"   : 0,
	"B3"   : 0,
	"JAIL" : 0,
	"C1"   : 0,
	"U1"   : 0,
	"C2"   : 0,
	"C3"   : 0,
	"R2"   : 0,
	"D1"   : 0,
	"CC2"  : 0,
	"D2"   : 0,
	"D3"   : 0,
	"FP"   : 0,
	"E1"   : 0,
	"CH2"  : 0,
	"E2"   : 0,
	"E3"   : 0,
	"R3"   : 0,
	"F1"   : 0,
	"F2"   : 0,
	"U2"   : 0,
	"F3"   : 0,
	"GTJ"  : 0,
	"G1"   : 0,
	"G2"   : 0,
	"CC3"  : 0,
	"G3"   : 0,
	"R4"   : 0,
	"CH3"  : 0,
	"H1"   : 0,
	"T2"   : 0,
	"H2"   : 0
}

current_space = "GO"
current_space_index = 0
doubles = 0

for repeats in range(1, 10000001, 1):
	dice1 = random.randrange(1, 5, 1)
	dice2 = random.randrange(1, 5, 1)
	if dice1 == dice2:
		doubles += 1
	else:
		doubles = 0
	if doubles == 3:
		doubles = 0
		current_space = "JAIL"
		current_space_index = 10
	else:
		current_space_index += dice1 + dice2

	if 39 < current_space_index:
		current_space_index -= 40
	current_space = board_spaces[current_space_index]

	if current_space == "GTJ":
		current_space = "JAIL"
		current_space_index = 10

	if current_space == "CC1" or current_space == "CC2" \
	or current_space == "CC3":
		drawn_card = random.randrange(1, 17, 1)
		if drawn_card == 1:
			current_space = "GO"
			current_space_index = 0
		if drawn_card == 2:
			current_space = "JAIL"
			current_space_index = 10

	if current_space == "CH1" or current_space == "CH2" \
	or current_space == "CH3":
		drawn_card = random.randrange(1, 17, 1)
		if drawn_card == 1:
			current_space = "GO"
			current_space_index = 0
		if drawn_card == 2:
			current_space = "JAIL"
			current_space_index = 10
		if drawn_card == 3:
			current_space = "C1"
			current_space_index = 11
		if drawn_card == 4:
			current_space = "E3"
			current_space_index = 24
		if drawn_card == 5:
			current_space = "H2"
			current_space_index = 39
		if drawn_card == 6:
			current_space = "R1"
			current_space_index = 5
		if drawn_card == 7 or drawn_card == 8:
			if current_space == "CH1":
				current_space = "R2"
				current_space_index = 15
			if current_space == "CH2":
				current_space = "R3"
				current_space_index = 25
			if current_space == "CH3":
				current_space = "R1"
				current_space_index = 5
		if drawn_card == 9:
			if current_space == "CH1" or current_space == "CH3":
				current_space = "U1"
				current_space_index = 12
			if current_space == "CH2":
				current_space = "U2"
				current_space_index = 28
		if drawn_card == 10:
			current_space_index -= 3
			current_space = board_spaces[current_space_index]

	current_space = board_spaces[current_space_index]
	space_visitations[current_space] += 1

for k in space_visitations:
	print(str(k) + ":      " + str(space_visitations[k]))

# Answer: 101524
