f = open('p059_cipher.txt', 'r')

line = f.readline().strip('\n')
chars = line.split(",")

# generate all possible encryption codes
def makeList(l):
	newList =[]
	for element in l:
		newList.append([element])
	return newList

def twoDigitCode(l, i):
	newList = []
	for e in l:
		newList.append([e, i])
	return newList

def threeDigitCode(l, i):
	return l + [i]

def allTwoDigitCodes():
	out = []
	x = range(97, 123)
	for i in x:
		out = out + twoDigitCode(x, i)
	return out

def allThreeDigitCodes(twoDigitCodes):
	out = []
	x = range(97, 123)
	for e in twoDigitCodes:
		for i in x:
			out.append(threeDigitCode(e, i))
	return out

codes = allThreeDigitCodes(allTwoDigitCodes())

def convertToChar(l):
	out = []
	for e in l:
		out.append(chr(e))

def applyCode(code, l):
	out = []
	i = 0
	for c in l:
		out.append( c^code[i] )
		i = (i+1)%3
	return out

def allowed():
	allowed = range(48, 126) + [32, 33, 34, 36, 39, 40, 41, 44, 46, 47]
	allowed = set(list(map(lambda c: chr(c), allowed)))
	return allowed

def isEnglish(string):
	if set(string) <= allowed():
		return True
	else:
		return False

chars = list(map(lambda c: int(c), chars))
# decoded = applyCode([97,98,99], chars)
strings = []
for code in codes:
	
	decoded = applyCode(code, chars)
	decodedAsChars = list(map(lambda c: chr(c), decoded))
	if isEnglish(decodedAsChars):
		print code
		decodedAsString = ''.join(decodedAsChars)
		print decodedAsString
		print sum(decoded)
	




