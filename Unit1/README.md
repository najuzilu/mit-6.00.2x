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

Brute Force Algorithm:
* enumerate all possible combinations of items
* remove all the combinations whole total units exceeds the allowed weight
* from the remaining combinations choose any one whose value is the largest

**Search Tree/Decision Tree Implementation**:
* left-frist, depth-first enumeration
* left - YES
* right - NO  
**Computational Complexity**:
* time based on number of nodes generated
* number of levels = number of items to choose from
* number of nodes at level i is 2^i (exponential complexity)
* an obvious optimization: don't explore parts of tree that violate constraint but this _does not_ change complexity  
**Header for Decision Tree Implementation**
```python
def maxVal(toConsider, avail):
	''' Assumes toConsider a list of items, avail a weight
		Returns a tuple of the total value of a solution to 0/1 knapsack problem and the items of that solution
	'''
	# if there is nothing to consider or value is 0
	if toConsider == [] or avail = 0:
		result = (0, ())
	# however, first thing we're going to do is check the first item fits in the knapsack if first item won't fit in the knapsack I can assume I'm not going to take it and I go to the next item
	elif toConsider[0].getUnits() > avail:
		result = maxVal(toConsider[1:], avail)
	# if it does fit in the knapsack, I have to consider two branches: left where I take it, and right branch where I do not.
	else:
		nextItem = toConsider[0]
		withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getUnits())
		withVal += nextItem.getValue()
		withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

		# choose the better of the two branches and return the results
		if withVal > withoutVal:
			result = (withVal, withToTake + (nextItem, ))
		else:
			result = (withoutVal, withoutToTake)
	return result
# We are not building the search tree. The local variable result records best solution found so far
```

##### Exercise 1 #####
```python
# generate all combinations of N items
def powerSet(items):
	N = len(items)
	# enumerate the 2**N possible combinations
	for i in range(2**N):
		combo = []
		for j in range(N):
			# test bit jth of integer i
			if (i >> j) % 2 == 1:
				combo.append(items[j])
		yield combo
```
Functions referenced in the grader:
```python
class Item(object):
	def __init__(self, n, v, w):
		self.name = n
		self.value = float(v)
		self.weight = float(w)
	def getName(self):
		return self.name
	def getValue(self):
		return self.value
	def getWeight(self):
		return self.weight
	def __str__(self):
		return '<' + self.name + ', ' + str(self.value) + ', '\
					 + str(self.weight) + '>'
def buildItems():
	return [Item(n,v,w) for n,v,w in (('clock', 175, 10), ('painting', 90, 9), ('radio', 20, 4), ('vase', 50, 2),('book', 10, 1),('computer', 200, 20))]

def buildRandomItems(n):
	return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
			for i in range(n)]

def yieldAllCombos(items):
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

items = buildItems()
combos = yieldAllCombos(items)
```

#### Recursive Fibonacci ####

**Dynamic Programming**

```python
def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2) 
# time: O(n)
```

* Create a table to record what we've done
	* before computing fib(x), check if value of fib(x) already stored in the table
	* if so, look it up
	* if not, compute it and then add it to table
* Called **memoization**

**Using a Memo to Compute Fibonnaci**:
```python
def fastFib(n, memo = {}):
	'''	Assumes n is an int >= 0, memo used only by recursive calls
		Returns Fibonacci of n
	'''
	if n == 0 or n == 1:
		return 1
	try:
		return memo[n]
	except KeyError:
		result = fastFib(n-1, memo) + fastFib(n-2, memo)
		memo[n] = result
		return result
```

**When does dynamic programming work well?**
* Optimal substructure: a globally optimal solution can be found by computing optimal solutions to local subproblems
	* For x > 1, fib(x) = fib(x-1) + fib(x-2)
* Overlapping subproblems: finding an optimal solution involves solving the same problem multple times
	* Compute fib(x) or many times

#### Dynamic Programming ####

Dynamic programming can be used to solve a Knapsack problem:
* Add memo as a third argument: `def fastMaxVal(toConsider, avail, memo={})`
* Key of memo is a tuple
	* (items left to be considered, available weight)
	* items left to be considered represented by len(toConsider)
```python
def fastMaxVal(toConsider, avail, memo = {}):
	''' Assumes toConsider a list of items, avail a weight
		Returns a tuple of the total value of a solution to 0/1 knapsack problem and the items of that solution
	'''
	if (len(toConsider), avail) in memo:
		result = memo[(len(toConsider), avail) ]
	elif toConsider == [] or avail = 0:
		result = (0, ())
	elif toConsider[0].getUnits() > avail:
		# explore right branch only
		result = maxVal(toConsider[1:], avail, memo)
	else:
		nextItem = toConsider[0]
		# explore left branch
		withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem.getUnits(), memo)
		withVal += nextItem.getValue()
		# explore right branch
		withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)

		# choose better branch
		if withVal > withoutVal:
			result = (withVal, withToTake + (nextItem, ))
		else:
			result = (withoutVal, withoutToTake)
		memo[(len(toConsider), avail)] = result
	return result
```

```python
# change recursion depth
import sys
sys.getrecursionlimit()
sys.setrecursionlimit(2000)
```

##### Exercise 2 #####

1. Dynamic programming can be used to solve optimization problems where the size of the space of possible solutions is exponentially large.  
**Answer**: True

2. Dynamic programming can be used to find an approximate solution to an optimization problem, but cannot be used to find a solution that is guaranteed to be optimal.  
**Answer**: False

3. Recall that sorting a list of integers can take `O(n log n` using an algorithm like merge sort. Dynamic programming can be used to reduce the order of algorithmic complexity of sorting a list of integers to something below `n log n`, where `n` is the length of the list to be sorted.  
**Answer**: False

4. Problem: I need to go up a flight of `N` stairs. I can either go up 1 or 2 steps every time. How many different ways are there for me to traverse these steps? For example:
```
3 steps -> could be 1,1,1 or 1,2 or 2,1
4 steps -> could be 1,1,1,1 or 1,1,2 or 1,2,1 or 2,1,1 or 2,2
5 steps -> could be 1,1,1,1,1 or 1,1,1,2 or 1,1,2,1 or 1,2,1,1 or 2,1,1,1 or 2,2,1 or 1,2,2 or 2,1,2
```
Does this problem have optimal substructure and overlapping subproblems?  
**Answer**: It has optimal substructure and overlapping subproblems

## Lecture 3 - Graph Problems ##

#### Graphs ####

#### Graph Class ####

#### Finding the Shortest Path ####

#### Reachable Nodes ####