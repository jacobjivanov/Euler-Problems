# PROBLEM DETAILS
# The 5-digit number, 16807=75, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=89, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

# THOUGHT PROCESS
# We can solve this in the reverse strategy. We can solve x ^ n,
# then test whether it is n digits long.

x, n = 0, 0
successful_pairs = []

for x in range(1, 11, 1):
	for n in range(1, 11, 1):
		if len(str(x ** n)) == n:
			successful_pairs.append("x = " + str(x) + "n = " + str(n)\
			+ "x ^ n = " + str(x ^ n))

print(successful_pairs)