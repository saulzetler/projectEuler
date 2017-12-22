#  this is not completed

cur = 987654321

# cur = 192384576

cur = 918273645

def next(cur):
	found = False
	while not found:
		cur -= 1
		x = set(list(str(cur)))
		if not '0' in x and len(x) == 9:
			found = True
	return int(cur)
	
def check(cur):
	found = False
	n = 0
	while n < (cur) and not found:
		n += 1
		# print "n is " + str(n)
		i = 2
		p = str(n) + str(2*n)
		if int(p) > cur:
			break 
		while int(p) <= cur:
			# print "p is " + str(p)
			if p == str(cur):
				print "n is " + str(n) + " i is " + str(i)
				found = True
				break
			i += 1
			p += str(n*i)
	return found			
		


while not check(cur):
	print str(cur) + " is not a multiple"
	cur = next(cur) 




