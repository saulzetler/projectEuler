limit = 1000000

tot = 0
for i in range(1, limit):
	if list(str(i)) == list(str(i))[::-1]:
		# print i
		b = '{0:b}'.format(i)
		if list(str(b)) == list(str(b))[::-1]:
			# print b
			tot += i

print tot