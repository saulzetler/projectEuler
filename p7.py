# 10001th prime

import math

primes = []
cur = 0

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

for i in range(0, 10001):
  while not is_prime(cur):
    cur += 1
  primes.append(cur)
  cur += 1
print primes[-1]


