# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
mof3 = []
mof5 = []
mofboth = []

for n in range(0, 1000, 3):
	mof3.append(n)

for k in range(0, 1000, 5):
	mof5.append(k)

for number in mof5:
	if number % 15 == 0:
		mof5.remove(number)

print(sum(mof3) + sum(mof5))

# Answer: 233168