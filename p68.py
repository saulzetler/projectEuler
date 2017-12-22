# if prev is None then it is external
class Node:
	def __init__(self, value = None, prev = None, next = None):
		self.value = value
		self.prev = prev
		self.next = next

	def __str__(self):
		return str(self.value)
		

def addLine(node):
	return node.value + node.next.value + node.next.next.value

def returnLine(node):
	return str(node.value) + str(node.next.value) + str(node.next.next.value)

def returnAllLines(cur, start):
	if cur.next.next.prev == start:
		return returnLine(cur)
	else:
		return returnLine(cur) + returnAllLines(cur.next.next.prev, start)

def sortByValue(nodes):
	out = []
	for n in nodes:
		out.append(n)
	nodeValues = list(map(lambda x: x.value, nodes))
	sortedNodeValues = sorted(nodeValues)
	for node in nodes:
		index = sortedNodeValues.index(node.value)
		out[index] = node
	return out

def findMin(nodes):
	nodeValues = list(map(lambda x: x.value, nodes))
	minElem = nodes[nodeValues.index(min(nodeValues))]
	return minElem	


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(7)
n7 = Node(9)
n8 = Node(5)
n9 = Node(6)
n10 = Node(12)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n1
n6.next = n1
n7.next = n2
n8.next = n3
n9.next = n4
n10.next = n5

n1.prev = n6
n2.prev = n7
n3.prev = n8
n4.prev = n9
n5.prev = n10

innerNodes = [n1, n2, n3, n4, n5]
outerNodes = [n6, n7, n8, n9, n10]
allNodes = innerNodes + outerNodes

def addAllLines():
	totals = []
	for node in outerNodes:
		totals.append(addLine(node))
	return totals

def populate(values):
	i = 0
	for node in allNodes:
		node.value = values[i]
		i += 1

from itertools import permutations
def allValues():
	n = range(1, 11)
	ps = permutations(n)
	out = []
	for p in ps:
		out.append(list(p))
	return out

def checkEqual(iterator):
   return len(set(iterator)) == 1		

def genStrings():
	ss = []
	for v in allValues():
		populate(v)
		totals = addAllLines()
		if checkEqual(totals):
			minNode = findMin(outerNodes)
			s = returnAllLines(minNode, minNode)
			ss.append(s)
	return ss

def findLen16():
	out = []
	for s in genStrings():
		if len(s) == 16:
			out.append(int(s))
	return max(out)

print findLen16()







