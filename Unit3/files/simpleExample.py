# python3

import pylab

def getMeanAndStd(X):
	mean = sum(X) / float(len(X))
	tot = 0.0
	for x in X:
		tot += (x - mean)**2
	std = (tot/len(X))**0.5
	return mean, std

L = [1, 1, 1, 1, 2]
pylab.hist(L)
pylab.show()
factor = pylab.array(len(L) * [1]) / len(L)
print(factor)
pylab.figure()
pylab.hist(L, weights = factor)

pylab.show()