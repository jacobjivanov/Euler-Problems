# Surprisingly there are only three numbers that can be written
# as the sum of fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the
# sum of fifth powers of their digits.

# Surprisingly there are only three numbers that can be written
# as the sum of fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the
# sum of fifth powers of their digits.

digit_fifth_powers = []

for n in range(2, 325512, 1): # y1 = (9^5)(x), y2 = (10^x) -1 y-intersect here

	digits = list(str(n))
	s = 0
	for d in digits:
		s += int(d) ** 5

	if s == n:
		digit_fifth_powers.append(n)
		print("Testing: " + str(n) + \
	"   Sum of digits to the fifth power: " + str(s) + "   #")
	else:
		print("Testing: " + str(n) + \
	"          Sum of digits to the fifth power: " + str(s))

print(digit_fifth_powers)
print(sum(digit_fifth_powers))

# Answer: 443839