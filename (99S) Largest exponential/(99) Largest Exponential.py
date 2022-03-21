# Comparing two numbers written in index form like 211 and 37 is not difficult,
# as any calculator would confirm that 211 = 2048 < 37 = 2187.
# However, confirming that 632382518061 > 519432525806 would be much more 
# difficult, as both numbers contain over three million digits.

# Using "Base Pairs.txt" a 22K text file containing one thousand lines with a 
# base/exponent pair on each line, determine which line number has the 
# greatest numerical value.

# NOTE: The first two lines in the file represent the numbers 
# in the example given above.

pairs = open("Programs/Euler Problems/(99S) Largest exponential/Number Pairs.txt", "r")
largest_exponential = 0
largest_exponential_line = 0
n = 0.0
current_line = 0
for p in pairs:
	p = p.split(" ")
	b = int(p[0])
	e = int(p[1])
	t = (b ** e)
	current_line += 1
	if largest_exponential < t:
		largest_exponential = t
		largest_exponential_line = current_line
	n += 0.1
	print(str(n) + "%")

print()
print(largest_exponential)
print("Line Number: " + str(largest_exponential_line))

# 895447 504922
# Line 709