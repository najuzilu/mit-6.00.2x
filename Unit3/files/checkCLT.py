# python3

import random
import pylab

def getMeanAndStd(X):
	mean = sum(X) / float(len(X))
	tot = 0.0
	for x in X:
		tot += (x - mean)**2
	std = (tot/len(X))**0.5
	return mean, std

def plotMeans(numDice, numRolls, numBins, legend, color, style):
	means = []
	for i in range(numRolls // numDice):
		vals = 0
		for j in range(numDice):
			vals += 5 * random.random()
		means.append(vals/float(numDice))
	pylab.hist(means, numBins, color = color, label = legend,
		# we don't want to show the no of elements in each bin;
		# we want each bin to show the probability of the mean falling within that bin;
		# value on y-axis is the prob of the mean falling within that bin
		weights = pylab.array(len(means)*[1]) / len(means),
		hatch = style)
	return getMeanAndStd(means)

mean, std = plotMeans(1, 100000, 19, '1 die', 'b', '*')
print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)
mean, std = plotMeans(50, 100000, 19, 'Mean of 50 dice', 'r', '//')
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
pylab.show()