# Largest Product in a Series

f = open('thousandDigitNumber.txt', 'r')
num_lines = sum(1 for line in open('thousandDigitNumber.txt'))

numString = ''
start = 0
products = []

for line in range(num_lines):
	numString += f.readline().strip('\n')
# print numString

for i in range(len(numString) - 13):
	subString = numString[i:i+13]
	product = 0
	for letter in subString:
		if product == 0: 
			product += int(letter)
		else: product = product*(int(letter))
	products.append(product)
		
print max(products)

