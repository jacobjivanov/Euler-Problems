# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10) ^ 2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

sum_of_squares = 0
for n in range(1, 101, 1):
	sum_of_squares += n ** 2
print("Sum of Squares = " + str(sum_of_squares))

square_of_sums = 0
for n in range(1, 101, 1):
	square_of_sums += n
square_of_sums = square_of_sums ** 2
print("Square of Sums = " + str(square_of_sums))

difference = sum_of_squares - square_of_sums

print("Difference = " + str(difference))

# Answer: 25164150