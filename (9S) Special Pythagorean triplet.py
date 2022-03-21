# A Pythagorean triplet is a set of three natural numbers, a < b < c, for 
# which, a ^ 2 + b ^ 2 = c ^ 2
# For example, 3 ^ 2 + 4 ^ 2 = 9 + 16 = 25 = 5 ^ 2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# sqrt(a ^ 2 + b ^ 2) = c
# a + b + sqrt(a ^ 2 + b ^ 2) = 1000

def sqrt(n):
	return float(n) ** 0.5

def power(n, p):
	return float(n) ** p

tri = []

for b in range(1, 1000, 1):
	for a in range(1, b, 1):
		c = sqrt(power(a, 2) + power(b, 2))
		if c == int(c) and c < 1000:
			tri.append([a, b, int(c)])
			
for eachtriple in tri:
	if eachtriple[0] + eachtriple[1] + eachtriple[2] == 1000:
		print(eachtriple)
		print(eachtriple[0] * eachtriple[1] * eachtriple[2])

# Answer: 31875000