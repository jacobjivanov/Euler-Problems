# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

series_total = 0
for n in range(1, 1001, 1):
	series_total += n ** n
	
series_total = str(series_total)
print(series_total[-10::])

# Answer: 9110846700