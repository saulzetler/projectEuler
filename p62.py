def isPerfectCube(x):
	return int(round(x**(1./3))) ** 3 == x


from itertools import permutations
def perms(n):
	n = [int(x) for x in str(n)]
	ps = permutations(n)
	out = []
	for p in ps:
		l = []
		for i in p:
			l.append(i)
		l = int(''.join([str(x) for x in l]))
		if isPerfectCube(l):
			out.append(l)
	return out

def countCubes(ps):
	count = 0
	for p in ps:
		if isPerfectCube(p):
			count += 1
	return count	

def slowMethod():
	found = False
	i = 680
	while not found:
		iCubed = i**3
		ps = perms(iCubed)
		if len(ps) == 5:
			found = True
		else:
			print str(i) + " is not the answer"
			i += 1
	print str(i) + " is the answer"
		
# much fater method	
cubes = []
for i in range(1, 100000):
	cubes.append(i**3)	
sortedCubes = []	
for cube in cubes:
	sortedCubes.append(sorted([int(x) for x in str(cube)]))
for cube in sortedCubes:
	if sortedCubes.count(cube) == 5:
		index = sortedCubes.index(cube)
		break

print cubes[index]
