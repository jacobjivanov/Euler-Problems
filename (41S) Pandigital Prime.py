# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
# also prime.

# What is the largest n-digit pandigital prime that exists?

import itertools

def isPrime(n):
   if n % 2 == 0:
      return False
   for i in range(3, int(n ** 1/2) + 1, 2):
      if n % i == 0:
         return False
   return True

n = 7 # n = 9, n = 8 produce no results
pandigitalList = list(range(1, n + 1))
print(pandigitalList)

pandigital_permutations = list(itertools.permutations(pandigitalList))

pandigitalPrimes = []
for i in range(0, len(pandigital_permutations) - 1):
   pan = ''
   for j in range(0, len(pandigital_permutations[i])):
      pan += str(pandigital_permutations[i][j])
   pan = int(pan)

   if isPrime(pan) == True:
      pandigitalPrimes.append(pan)

print(pandigitalPrimes)
# Kind of a rough way of solving it but I tried it for n = 9, n = 8 and there were no results. So I ran it with n = 7 and picked the last one on the list.

# Answer: 7652413