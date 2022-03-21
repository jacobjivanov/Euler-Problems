# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

primes = [2, 3, 5, 7, 11, 13]

n = primes[len(primes) - 1] + 2

while len(primes) < 10001:
	ptest = []
	for p in primes:
		ptest.append(n % p)

	if 0 in ptest:
		n += 2
	else:
		primes.append(n)
		print("Prime #" + str(len(primes)) + " = " + str(n))
		n += 2

# Answer: 104743