# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above, starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_sequence_length(n):
	sequence_length = 1
	
	while n != 1:
		if n % 2 == 0:
			n /= 2
			sequence_length += 1
	
		else:
			n = 3 * n + 1
			sequence_length += 1
	
	return sequence_length

max_sequence_n_length = [1, 1]
for n in range(1, 1000000, 1):
	print("Testing: " + str(n) + "              Sequence Length = "\
	+ str(collatz_sequence_length(n)))
	
	if collatz_sequence_length(n) > max_sequence_n_length[1]:
		max_sequence_n_length[0] = n
		max_sequence_n_length[1] = collatz_sequence_length(n)

print()
print("Max @ n = " + str(max_sequence_n_length[0]) + \
", Sequence Length = " + str(max_sequence_n_length[1]))

# Output: Max @ n = 837799, Sequence Length = 525
# Answer: 837799