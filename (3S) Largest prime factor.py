# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

primes = [2]
value = 3
number = 600851475143
while value < (number ** 0.5):
	isPrime = True
	for k in primes:
		if value % k == 0:
			isPrime = False
			value += 2
	if isPrime:
		primes.append(value)
		if number % value == 0:
			print(value)
			number /= value

print(number)

# Answer: 6857