# Euler's Totient function, phi(n), is 
# used to determine the number of numbers less than n which are relatively 
# prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine 
# and relatively prime to nine, phi(9) = 6.

# n	    Relatively Prime	phi(n)		n/phi(n)
# 2	    1	                1	    	2
# 3	    1,2	                2	    	1.5
# 4	    1,3	                2	    	2
# 5	    1,2,3,4	            4	    	1.25
# 6	    1,5	                2	    	3
# 7	    1,2,3,4,5,6	        6	    	1.1666...
# 8	    1,3,5,7	            4	    	2
# 9	    1,2,4,5,7,8	        6	    	1.5
# 10	1,3,7,9	            4	    	2.5

# It can be seen that n = 6 produces a maximum n/phi(n) for n <= 10.
# Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.

def coprime(n1, n2):
	n1_factors = set()
	n2_factors = set()
	
	for pn1 in range(1, n1 + 1, 1):
		if n1 % pn1 == 0:
			n1_factors.add(pn1)
	n1_factors.remove(1)

	for pn2 in range(1, n2 + 1, 1):
		if n2 % pn2 == 0:
			n2_factors.add(pn2)
	n2_factors.remove(1)
	
	factors = set()
	factors = (n1_factors | n2_factors)
	
	if (len(n1_factors) + len(n2_factors)) == len(factors):
		return True
	else: 
		return False
	
def phi(n):
	relative_primes = []
	
	for pn in range(1, n, 1):
		if coprime(n, pn) == True:
			relative_primes.append(pn)
	
	return len(relative_primes)

def n_div_phi(n):
	return (float(n) / float(phi(n)))

n_div_phi_n = []

for n in range(2, 1000000, 2):
	print str(n) + ": " + str(n_div_phi(n))
	n_div_phi_n.append(n_div_phi(n))

print
print
print
a = str(2 * (n_div_phi_n.index(max(n_div_phi_n)) + 1))
b = str(max(n_div_phi_n))
print a + b