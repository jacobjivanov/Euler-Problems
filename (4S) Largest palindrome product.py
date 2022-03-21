# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

x = 999
y = 999
palindromic_products = []

def testpalindrome(number):
	numberf = list(str(number))
	numberb = list(str(number))
	numberb = numberb[:: -1]
	
	if numberf == numberb:
		return True
	else:
		return False

for x in range(999, 1, -1):
	for y in range(999, 1, -1):
		if testpalindrome(x * y) == True:
			palindromic_products.append(x * y)
			
print(palindromic_products)
print()
print(max(palindromic_products))

# Answer: 906609