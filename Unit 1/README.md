## Lecture 1 - Optimization and the Knapsack Problem ##

#### Knapsack Problem ####

What is an optimization model?
* objective function that is to be maximize or minimize
* a set of constraints (possibly empty) that must be honored

Takeaways:
* solving optimization problems is computationally challenging
* a greedy algorithm is often a practical approach to finding a pretty good **approximate** solution to an optimization problem

**Kanpsack and Bin-packing Problems**

Two variants:
* 0/1 knapsack problem (much difficult then the next one)
* continuous or fractional knapsack problem

**0/1 Knapsack Problem, Formalized**

* each item is represented by a pair `<value, weight>`
* the knapsack can accommodate items with a total weight of no more than `w`
* a vector `L` of length n represents the set of available items. Each element of the vector is an item
* a vector `V` of length n is used to indicate whether or not items are taken. If `V[i]=1`, item `I[i]` is taken. If `V[i]=0`, item `I[i]` is not taken

Find a V that maximizes:
![Image](https://github.com/najuzilu/MITx-6.00.2x/tree/master/Unit%201/knapsacProblem.png)

Brute force algorithm:  
1. Enumerate all possible combinations of items. That is to say, generate all subsets of the set of subjects. This is called the **power set**
2. Remove all of the combinations whose total units exceeds the allowed weight
3. From the remaining combinations choose any one whose value is the largest (there might be more than one optimal solution)
_This is often not practical_  
**0/1 knapsack problem is inherently exponential**

**Exercise 1**:  
1. Choose the item with the best value to weight ratio first.
	* The algorithm does not run
2. Choose the lighest object first
	* The algorithm runs and returns a non-optimal solution.
3. Choose the most valuable object first.
	* The algorithm runs and returns a non-optimal solution.

#### Greedy Algorithm ####

> while knapsack not full
> put "best" available item in knapsack

Class Food:
```python
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

def buildMenu(name, values, calories):
	'''	names, values, calories lists of same length.
		name a list of strings
		values and calories lists of numbers
		returns list of Foods'''
	menu = []
	for i in range(len(values)):
		menu.append(Food(names[i], values[i], calories[i]))
	return menu

def greedy(items, maxCost, keyFunction):
	'''	Assumes items a list, maxCost >= 0,
		keyFunction maps elements of items to numbers '''
	itemCopy = sorted(items, key = keyFunction, reverse = True) # O(nlogn)
	result = []
	totalValue, totalCost = 0.0, 0.0

	for i in range(len(itemCopy)): # O(n)
		if(totalCost+itemCopy[i].getCost()) <= maxCost:
			result.append(itemsCopy[i])
			totalCost += itemCopy[i].getCost()
			totalValue += itemCopy[i].getValue()
	return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
	taken, val = greedy(items. constraint, keyFunction)
	print('Total value of items taken =', val)
	for item in taken:
		print(' ', item)

def testGreedys(maxUnits):
	print('Use greedy by value to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.getValue)

	print('Use greedy by cost to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))

	print('Use greedy by density to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(750)
testGreedys(1000)

```

**Why different answers?**
* sequence of locally **optimal** choices don't always yield a globally optimal solution

**lambda**  
* used to create anonymous functions

**Exercise 3**:
1. n
2. n^2
3. 2^n

## Lecture 2 - Decision Trees & Dynamic Programming ##

#### Brute Force Algorithms ####

#### Recursive Fibonacci ####

#### Dynamic Programming ####

## Lecture 3 - Graph Problems ##

#### Graphs ####

#### Graph Class ####

#### Finding the Shortest Path ####

#### Reachable Nodes ####