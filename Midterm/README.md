## Midterm ##

### Pset 1 ###

1. The following function is stochastic:
```python
def f(x):
    # x is an integer
    return int(x + random.choice([0.25, 0.5, 0.75]))
```
**Answer** False

2. In Python, we can use random.seed(100) at the beginning of a program to generate the same sequence of random numbers each time we run a program.  
**Answer**: True

3. A brute force solution to the 0/1 knapsack problem will always produce an optimal solution.  
**Answer**: True

4. The following function is stochastic:
```python
import random

def A():
    mylist = []
    r = 1
    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    print(mylist)
```
**Answer**: True

5. Consider an undirected graph with non-negative weights that has an edge between each pair of nodes. The shortest distance between any two nodes is always the path that is the edge between the two nodes.  
**Answer**: False

### Pset 2 ###

1. Which of the following problems can be solved using dynamic programming? Check all that work
* Sum of elements - Given a list of integer elements, find the sum of all the elements
* Binary search - given a list of elements, check if the element X is in the list
* Dice throws - Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of values of each face when all the dice are thrown.  
**Answer**: 2, 3 _INCORRECT_

2. What is the exact probability of rolling at least two 6's when rolling a die three times?  
**Answer**: 2/27

3. A greedy optimization algorithm  
**Answer**: is typically efficient in time

4. Suppose you have a weighted directed graph and want to find a path between nodes A and B with the smallest total weight. Select the most accurate statement.  
**Answer**: If all edges have weight 2, breadth-first search guarantees that the first path found to be is the shortest path.

5. Which of the following functions are deterministic?
```python
import random
        
def F():
    mylist = []
    r = 1
    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print(mylist)

def G():  
    random.seed(0)
    mylist = []
    r = 1
    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            print(mylist)
```
**Answer**: Both F and G

6. Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a contiguous subsequence. For example,
* in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
* in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
One algorithm goes through all possible subsequences and compares the sums of each contiguous subsequence with the largest sum it has seen. What is the time complexity of this algorithm in terms of the length of the list, N?  
**Answer**: O(n^2)

### Pset3 ###
You are given a list of unique positive integers L sorted in descending order and a positive integer sum s. The list has n elements. Consider writing a program that finds values for multipliers  𝑚0,𝑚1,...,𝑚𝑛−1  such that the following equation holds:  𝑠=𝐿[0]∗𝑚0+𝐿[1]∗𝑚1+...+𝐿[𝑛−1]∗𝑚𝑛−1   
Assume a greedy approach to this problem. You calculate the integer multipliers m_0, m_1, ..., m_(n-1) by finding the largest multiplier possible for the largest value in the list, then for the second largest, and so on. Write a function that returns the sum of the multipliers using this greedy approach. If the greedy approach does not yield a set of multipliers such that the equation above sums to s, return the string "no solution". Write the function implementing this greedy algorithm with the specification below:
```python
def greedySum(L, s):
	""" input: s, positive integer, what the sum should add up to
			   L, list of unique positive integers sorted in descending order
		Use the greedy approach where you find the largest multiplier for 
		the largest value in L then for the second largest, and so on to 
		solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
		return: the sum of the multipliers or "no solution" if greedy approach does 
				not yield a set of multipliers such that the equation sums to 's'
	"""
	def find_largest_multiplier(largest_value, s):
		return int(s / largest_value)

	sum_of_multipliers = 0

	for i in range(len(L)):
		lm = find_largest_multiplier(L[i], s)
		sum_of_multipliers += lm
		s -= lm * L[i]

	if s == 0:
		return sum_of_multipliers
	else:
		return "no solution"
```

### Pset 4 ###
Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a contiguous subsequence. For example,
* in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
* in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
Write a function that meets the specification below.
```python
def max_contig_sum(L):
	""" L, a list of integers, at least one positive
	Returns the maximum sum of a contiguous subsequence in L """
	def sum_window(rightBound, L, maxSum):
		subarrayMax.append(maxSum)
		if rightBound == len(L):
			return maxSum
		maxSum += L[rightBound]
		sum_window(rightBound + 1, L, maxSum)

	leftBound = 0
	array = []
	while leftBound <= len(L):
		global subarrayMax
		subarrayMax = []
		sum_window(leftBound, L, 0)
		array.append(max(subarrayMax))
		leftBound += 1
	return max(array)
```

### Pset 5 ###
In lecture, we explored the concept of a random walk, using a set of different models of drunks. Below is the code we used for locations and fields and the base class of drunks – you should not have to study this code in detail, since you have seen it in lecture.
```python
import pylab

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
```
**NEW CODE**:  
The following function is new, and returns the actual x and y distance from the start point to the end point of a random walk.
```python
def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())
```
**DRUNK VARIATIONS**:  
Here are several different variations on a drunk.
```python
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)
```
**PROBLEM**:  
Suppose we use a simulation to simulate a random walk of a class of drunk, returning a collection of actual distances from the origin for a set of trials.

Each graph below was generated by using one of the above five classes of a drunk (UsualDrunk, ColdDrunk, EDrunk, PhotoDrunk, or DDrunk). For each graph, indicate which Drunk class is mostly likely to have resulted in that distribution of distances. Click on each image to see a larger view.

1. **Answer**: UsualDrunk
2. **Answer**: PhotoDrunk
3. **Answer**: ColdDrunk
4. **Answer**: DDrunk
5. **Answer**: EDrunk

### Pset 6 ###
Graphs are a convenient way to represent the relations between people, objects, concepts, and more.

There are many ways to create a graph, some of which are random. A random graph is one that is generated by randomly adding edges to a list of nodes. The list of nodes for this problem is initialized as follows:
```python
nodes = []
for i in range(n):
    nodes.append(Node(i)) # newNode takes one parameter, the number of the node
```
A helper method, addEdge, is referenced in this problem. The addEdge method takes two integers - representing nodes in the graph - and adds a directed edge from the first node to the second node. So, addEdge(8, 2) adds a directed edge from Node 8 to Node 2.

In each code piece below, a graph is generated using the above node set by adding edges in some fashion. Your job is to examine the code and select the type of graph that will be generated. Your choices for each question will be: tree; graph (undirected graph); line graph; digraph (directed graph); complete graph or clique; bar graph; bipartite graph; loop or connected chain of nodes. Note that this last option refers to a graph that consists of one single, large loop or connected chain of nodes.

1. 
```python
for i in range(len(nodes)):
	x = random.choice(nodes)
	y = random.choice(nodes)
	addEdge(x,y)
```
**Answer**: digraph (directed graph)

2. 
```python
for i in range(len(nodes)):
	x = random.choice(nodes)
	y = random.choice(nodes)
	addEdge(x,y)
	addEdge(y,x)
```
**Answer**: graph (undirected graph)

3. 
```python
for i in range(len(nodes)):
	w = random.choice(nodes)
	x = random.choice(nodes)
	y = random.choice(nodes)
	z = random.choice(nodes)
	addEdge(w,x)
	addEdge(x,y)
	addEdge(y,z)
	addEdge(z,w)
```
**Answer**: digraph (directed graph)

4. 
```python
for x in nodes:
	for y in nodes:
		addEdge(x,y)
		addEdge(y,x)
```
**Answer**: complete graph or clique correct

5. 
The out degree of a node is the number of its neighbors, i.e. for a node x, its degree is the number edges, of the form (x, y_i), where y_i is some other node.

Which graph has the largest out degree per node?  
**Answer**: complete graph or clique correct

### Pset 7 ###
Write a function that meets the specification below:
```python
def solveit(test):
	""" test, a function that takes an int parameter and returns a Boolean
		Assumes there exists an int, x, such that test(x) is True
		Returns an int, x, with the smallest absolute value such that test(x) is True 
		In case of ties, return any one of them. 
	"""
	x = 0
	while True:
		if test(x):
			return x
		elif test(-x):
			return -x
		x += 1
```