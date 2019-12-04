# python3

def makeHist(data, title, xlabel, ylabel, bins = 20):
	pylab.hist(data, bins = bins)
	pylab.title(title)
	pylab.xlabel(xlabel)
	pylab.ylabel(ylabel)

def getHighs():
	inFile = open('temperatures.csv')
	population = []
	for l in inFile:
		try:
			tempC = float(l.split(',')[1])
			population.append(tempC)
		except:
			continue
	return population

def getMeansAndSDs(population, sample, verbose = False):
	popMean = sum(population)/len(population)
	sampleMean = sum(sample)/len(sample)
	if verbose:
		makeHist(population, 'Daily High 1961-2015 Population (mean = ' + str(rount(popMean, 2)) + ')', 'Degrees C', 'Number Days')
		pylab.figure()
		makeHist(sample, 'Daily High 1961-2015 Sample (mean = ' + str(rount(sampleMean, 2)) + ')', 'Degrees C', 'Number Days')
		print('Population mean =', popMean)
		print('Standard deviation of population =', numpy.std(population))
		print('Sample mean =', sampleMean)
		print('Standard deviation of sample =', numpy.std(sample))
		return popMean, sampleMean, numpy.std(population), numpy.std(sample)

# random.sample(population, sampleSize)  # returns a list containing sampleSize randomly chosen distint elements of population (sampling without replacement)

random.seed(0)
population = getHighs()
sample = random.sample(population, 100)
getMeansAndSDs(population, sample, True)