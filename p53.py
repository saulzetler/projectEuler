def fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*fact(n-1)

def choose(n, r):
	return fact(n)/(fact(r)*fact(n-r))

count = 0
for n in range(1, 101):
	for r in range(1, n):
		if choose(n, r) > 1000000:
			count += 1

print count