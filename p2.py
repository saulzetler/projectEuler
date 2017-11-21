#Sum of Even Fibonacci Numbers

import sys

evens = []
fib = [1, 2]
limit = int(sys.argv[1])
flag = True

while flag:
	next = fib[len(fib)-1] + fib[len(fib)-2]
	if next > limit:
		flag = False
	else:
		fib.append(next)

for n in fib:
	if n % 2 == 0:
		evens.append(n)

ans = sum(evens)

print(fib)
print ( str(ans) )