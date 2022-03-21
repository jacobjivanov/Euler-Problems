# Work out the first ten digits of the sum of the
# following one-hundred 50-digit numbers.
# Numbers are in Large Sum Numbers.txt

total = 0
numbers = open("/Users/jacobivanov/Documents/Programming/Programs/Euler Problems/(13) Large Sum/Large Sum Numbers.txt", "r")

for n in numbers:
	total += int(n)

total = str(total)
print(total)
print()

total = total[0:9]
print(total)

# Answer: 5537376230
