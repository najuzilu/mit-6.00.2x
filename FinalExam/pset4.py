import random, pylab

# You are given this function
def getMeanAndStd(X):
	mean = sum(X)/float(len(X))
	tot = 0.0
	for x in X:
		tot += (x - mean)**2
	std = (tot/len(X))**0.5
	return mean, std

# You are given this class
class Die(object):
	def __init__(self, valList):
		""" valList is not empty """
		self.possibleVals = valList[:]
	def roll(self):
		return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
	"""
	  - values, a sequence of numbers
	  - numBins, a positive int
	  - xLabel, yLabel, title, are strings
	  - Produces a histogram of values with numBins bins and the indicated labels
		for the x and y axis
	  - If title is provided by caller, puts that title on the figure and otherwise
		does not title the figure
	"""
	# TODO
	pylab.hist(values, bins = numBins)
	pylab.xlabel(xLabel)
	pylab.ylabel(yLabel)
	if title:
		pylab.title(title)
	pylab.show()
					
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
	"""
	  - die, a Die
	  - numRolls, numTrials, are positive ints
	  - Calculates the expected mean value of the longest run of a number
		over numTrials runs of numRolls rolls.
	  - Calls makeHistogram to produce a histogram of the longest runs for all
		the trials. There should be 10 bins in the histogram
	  - Choose appropriate labels for the x and y axes.
	  - Returns the mean calculated
	"""
	results = []

	for t in range(numTrials):
		dieRolls = [die.roll() for i in range(numRolls)]

		size = 1
		max_size = 0
		for i in range(len(dieRolls)-1):
			if dieRolls[i+1] == dieRolls[i]:
				size += 1
			else: 
				size = 1
			if max_size < size:
				max_size = size
		if max_size > 0:
			results.append(max_size)
		else:
			results.append(1)

	makeHistogram(results, numBins = 10, xLabel = 'Length of the longest run', yLabel = 'frequency', title = 'Histogram of the longest runs')
	return sum(results)/len(results)

# # Test cases for makeHistogram method:
# makeHistogram([], 1, "A", "B", "C")
# makeHistogram([1], 4, "Aa", "Bb", "Cc")
# makeHistogram([1,2], 4, "Aaa", "Bbb")
	
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))