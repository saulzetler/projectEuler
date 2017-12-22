def isPerm(i):
	if set(str(i)) == set(str(2*i)) == set(str(3*i)) == set(str(4*i)) == set(str(5*i)) == set(str(6*i)):
		return True
	else:
		return False



for i in range(1, 1000000):
	if isPerm(i):
		print i
		break

