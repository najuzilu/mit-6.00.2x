# python3
import random

class Food(object):
	def __init__(self, n, v, w):
		self.name = n
		self.value = v
		self.calories = w

	def getValue(self):
		return self.value

	def getCost(self):
		return self.calories

	def density(self):
		return self.getValue()/self.getCost()

	def __str__(self):
		return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
	"""	names, values, calories lists of same length.
		name a list of strings
		value and calories lists of numbers
		return list of Foods """
	menu = []
	for i in range(len(values)):
		menu.append(Food(names[i], values[i], calories[i]))
	return menu

def greedy(items, maxCost, keyFunction):
	"""	Assumes items a list, maxCost >= 0,
		keyFunction maps elements of items to numbers """
	itemsCopy = sorted(items, key = keyFunction, reverse = True)
	result = []
	totalValue, totalCost = 0.0, 0.0

	for i in range(len(items)):
		if (totalCost+itemsCopy[i].getCost()) <= maxCost:
			result.append(itemsCopy[i])
			totalCost += itemsCopy[i].getCost()
			totalValue += itemsCopy[i].getValue()

	return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
	taken, val = greedy(items, constraint, keyFunction)
	print('Total value of items taken =', val)
	for item in taken:
		print('   ', item)

def testGreedys(foods, maxUnits):
	print('Use greedy by value to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.getValue)
	print('\nUse greedy by cost to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
	print('\nUse greedy by density to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.density)

def maxVal(toConsider, avail):
	""" Assumes toConsider a list of items,
			avail a weight
		Returns a tuple of the total value of a 
			solution to 0/1 knapsack problem 
			and the items of that solution"""
	if toConsider == [] or avail == 0:
		result = (0, ()) # no value and no items

	elif toConsider[0].getCost() > avail:
		result = maxVal(toConsider[1:], avail) # pass cuz units greater than what's available

	else:
		nextItem = toConsider[0]
		# Explore left branch
		withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
		withVal += nextItem.getValue()

		# Explore right branch
		withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

		# Explore better branch
		if withVal > withoutVal:
			result = (withVal, withToTake + (nextItem,))
		else:
			result = (withoutVal, withoutToTake)
	return result

def testMaxVal(foods, maxUnits, algorithm, printItems = True):
	print('Use search tree to allocate', maxUnits, 'calories')
	val, taken = algorithm(foods, maxUnits)
	print('Total value of items taken =', val)
	if printItems:
		for item in taken:
			print('    ', item)
	

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
print(' ')
testMaxVal(foods, 750, maxVal)

# To test how tree works with larger menu:
def buildLargeMenu(numItems, maxVal, maxCost):
	items = []
	for i in range(numItems):
		items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
	return items

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
	items = buildLargeMenu(numItems, 90, 250)
	testMaxVal(items, 750, maxVal, False)