#Largest Prime Factor

import sys
import math

n = int(sys.argv[1])
root = int(math.sqrt(n))
cur = 3
primeFactors = []

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 

while cur < root:
	if is_prime(cur) and n % cur == 0: primeFactors.append(cur)
	cur += 2
print primeFactors

		

