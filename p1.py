# Multiples of 3 and 5
import sys

multiples = []
limit = int(sys.argv[1])

for i in range(1,limit):
	if i % 3 == 0 or i % 5 == 0:
		multiples.append(i)

ans = sum(multiples)

print ("The sum of multiples of 3 and 5 below " + str(limit) + " is " + str(ans) )




