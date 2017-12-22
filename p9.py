# special pythagorean triplet

import math

for a in range(1, 333):
	for b in range(a, 1000):
		n = a*a + b*b
		c = int(math.sqrt(n))
		if n == c*c and a+b+c == 1000:
			print str(a) + " " + str(b) + " " + str(c)
			print a*b*c
			break

