# python3

import numpy as np
import random
import pylab

def genNoisyParabolicData(a, b, c, xVals, fName):
	yVals = []
	for x in xVals:
		theoreticalVal = a*x**2 + b*x + c
		yVals.append(theoreticalVal + random.gauss(0, 35))
	f = open(fName, 'w')
	f.write('x,y\n')
	for i in range(len(yVals)):
		f.write(str(xVals[i]) + ',' + str(yVals[i]) + '\n')
	f.close()

def getData(fName):
	xVals, yVals = [], []
	f = open(fName, 'r')
	line = f.readline()

	while line:
		row = line.strip().split(',')
		if row[0] != 'x':
			xVals.append(float(row[0]))
			yVals.append(float(row[1]))
		line = f.readline()
	return xVals, yVals

def rSquared(observed, predicted):
	error = ((predicted - observed)**2).sum()
	meanError = error/len(observed)
	return 1 - (meanError/np.var(observed))

def genFits(xVals, yVals, degrees):
	models = []
	for d in degrees:
		model = pylab.polyfit(xVals, yVals, d)
		models.append(model)
	return models

def testFits(models, degrees, xVals, yVals, title):
	pylab.plot(xVals, yVals, 'o', label = 'Data')
	for i in range(len(models)):
		estYVals = pylab.polyval(models[i], xVals)
		error = rSquared(yVals, estYVals)
		pylab.plot(xVals, estYVals, label = 'Fit of degree ' + str(degrees[i]) + ', R2 = ' + str(round(error, 5)))
		pylab.legend(loc = 'best')
		pylab.title(title)

xVals = range(-10, 11, 1)
a, b, c = 3, 0, 0
degrees = (2, 4, 8, 16)

random.seed(0)

genNoisyParabolicData(a, b, c, xVals, 'Dataset 1.txt')
genNoisyParabolicData(a, b, c, xVals, 'Dataset 2.txt')

xVals1, yVals1 = getData('Dataset 1.txt')
models1 = genFits(xVals1, yVals1, degrees)
testFits(models1, degrees, xVals1, yVals1, 'Dataset 1.txt')

pylab.figure()

xVals2, yVals2 = getData('Dataset 2.txt')
models2 = genFits(xVals2, yVals2, degrees)
testFits(models2, degrees, xVals2, yVals2, 'Dataset 2.txt')

pylab.figure()
testFits(models1, degrees, xVals2, yVals2, 'Dataset 2/Model 1')
pylab.figure()
testFits(models2, degrees, xVals1, yVals1, 'Dataset 1/Model 2')

pylab.show()