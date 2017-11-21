# Sum Square Difference

plainSum = 0
sumOfSquares = 0
squareOfSum = 0

for i in range(1, 101):
	plainSum += i
	sumOfSquares += i**2
squareOfSum = plainSum**2

print squareOfSum - sumOfSquares