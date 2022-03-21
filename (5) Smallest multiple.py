# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

def LCM(n1, n2):
	m1, m2 = n1, n2
	
	while m1 != m2:
		if m1 < m2:
			m1 += n1
		if m2 < m1:
			m2 += n2
	
	return m1
	
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

LCM = 1
for eachn in n:
	M = LCM(LCM, eachn)

print(LCM)