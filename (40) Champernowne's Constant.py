# An irrational decimal fraction is created by 
# concatenating the positive integers:
# 0.1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the 
# value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

champ_constant = str(0.1)
for n in range(2, 1000000, 1):
	champ_constant += str(n)

def nth_digit(n):
	return champ_constant[n + 1]

value = 1
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
	i_digit = nth_digit(i)
	value = value * int(i_digit)

print value

# Answer: 210