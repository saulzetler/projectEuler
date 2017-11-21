class player():
	def __init__(self):
		self.hand = []
		self.suits = []
		self.nums = []
		self.rank = 0
	def setHand(self, hand):
		self.hand = hand	
	def addSuit(self, suit):
		self.suits.append(suit)
	def addNum(self, num):
		self.nums.append(num)
	def setRank(self, rank):
		self.rank = rank
	def clear(self):
		self.rank = 0
		self.hand = []
		self.nums = []
		self.suits = []

def numberOfPairs(nums):
	pairs = 0
	for card in nums:
		if nums.count(card) == 2:
			pairs += 1
	return pairs/2

def cardsWithMatch(nums):
	matches = []
	for card in nums:
		if nums.count(card) > 1:
			matches.append(card)
	return matches

def hasThreeOfAKind(nums):
	for card in nums:
		if nums.count(card) == 3:
			return True
	return False

def hasFourOfAKind(nums):
	for card in nums:
		if nums.count(card) == 4:
			return True
	return False

def isAFlush(suits):
	if all(x==suits[0] for x in suits):
		return True
	else:
		return False

def isRoyal(suits, sortedNums):
	if isAFlush(suits):
		if isAStraight(sortedNums):
			if sortedNums[0] == 10:
				return True
	return False

def sortNums(nums):
	temp = []
	for s in nums:
		s = s.replace('T', '10')
		s = s.replace('J', '11')
		s = s.replace('Q', '12')
		s = s.replace('K', '13')
		s = s.replace('A', '14')
		s = int(s)
		temp.append(s)
	temp.sort()
	return temp

def isAStraight(sorted):
	for index in range(1, len(sorted)):
		if sorted[index] != sorted[index - 1] + 1:
			return False
	return True

p1wins = 0
p1 = player()
p2 = player()
players = [p1, p2]

f = open('poker.txt', 'r')
num_lines = sum(1 for line in open('poker.txt'))


for deal in range(num_lines):
	hands = f.readline()
	cards = hands.split(' ')
	cards[9] = cards[9].rstrip('\n') 

	p1.clear()
	p2.clear()

	p1.setHand(cards[0:5])
	p2.setHand(cards[5:10])

	for player in players:
		
		for card in player.hand:
			player.addNum(card[0])
			player.addSuit(card[1])

		if numberOfPairs(player.nums) > 0:
			player.setRank(numberOfPairs(player.nums))

		if hasThreeOfAKind(player.nums):
			player.setRank(3)

			if numberOfPairs(player.nums) == 1:
				player.setRank(6)

		elif hasFourOfAKind(player.nums):
			player.setRank(7)
		elif isAStraight(sortNums(player.nums)):
			player.setRank(4)

			if isAFlush(player.suits):
				player.setRank(8)

				if isRoyal(player.suits, sortNums(player.nums)):
					player.setRank(9)
		elif isAFlush(player.suits):
			player.setRank(5)

	p1numsSorted = sortNums(p1.nums)
	p2numsSorted = sortNums(p2.nums)
	p1mc = cardsWithMatch(p1numsSorted)  
	p2mc = cardsWithMatch(p2numsSorted)  
	if p1.rank > p2.rank:
		p1wins += 1
	elif p1.rank == p2.rank:
		if (len(p1mc) == len(p2mc)) and (len(p1mc) != 0) and (len(p2mc) != 0):
			for i in range(len(p1mc) - 1, 0, -1):
				if p1mc[i] > p2mc[i]:
					p1wins += 1
					break
				elif p1mc[i] < p2mc[i]:
					break
		else:
			for i in range(4, 0, -1):
				if p1numsSorted[i] > p2numsSorted[i]:
					p1wins += 1
					break
				elif p1numsSorted[i] < p2numsSorted[i]:
					break
print p1wins



