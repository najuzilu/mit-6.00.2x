# python3

import random

def throwNeedles(numNeedles):
	inCircle = 0
	for Needles in range(1, numNeedles + 1, 1):
		x = random.random()
		y = random.random()
		if (x * x + y * y)**0.5 <= 1.0:
			inCircle += 1
	return 4 * (inCircle / float(numNeedles))

def stdDev(est):
	mean = sum(est) / float(len(est))
	total = 0.0
	for value in est:
		total += (value - mean)**2
	return (total / float(len(est)))**0.5

def getEst(numNeedles, numTrials):
	estimates = []
	for  t in range(numTrials):
		piGuess = throwNeedles(numNeedles)
		estimates.append(piGuess)
	sDev = stdDev(estimates)
	curEst = sum(estimates) / len(estimates)
	print('Est. = ' + str(curEst) + ', Std. dev. = ' + str(round(sDev, 6)) + ', Needles = ' + str(numNeedles))
	return (curEst, sDev)

def estPi(precision, numTrials):
	numNeedles = 1000
	sDev = precision
	while sDev >= precision / 1.96: # (1.96)
		curEst, sDev = getEst(numNeedles, numTrials)
		numNeedles *= 2
	return curEst

random.seed(0)
estPi(0.005, 100)