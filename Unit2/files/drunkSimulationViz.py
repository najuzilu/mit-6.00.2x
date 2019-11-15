# python 3

import pylab
import random

class Location(object):
	def __init__(self, x, y):
		""" x and y are floats """
		self.x = x
		self.y = y

	def move(self, deltaX, deltaY):
		""" deltaX and deltaY are floats """
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

	def getLoc(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		return self.drunks[drunk]

	def moveDrunk(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		xDist, yDist = drunk.takeStep()
		currentLocation = self.drunks[drunk]
		# use move method of Location to get new location
		self.drunks[drunk] = currentLocation.move(xDist, yDist)

""" Basic because we will use to create two subclasses that inherit this one.
	Two subclasses of drunk are:
		1. The "usual" drunk, who wanders around at random
		2. The "I hate winter" drunk, who tries to move southward
"""
class Drunk(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0,0.0), (-1.0,0.0)]
		return random.choice(stepChoices)

class ColdDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0.0, 0.9),(0.0,-1.1),(1.0, 0.0),(-1.0,0.0)] # heads north, slightly less than one unit, and heads south, slightly more than one unit >> think of this as a biased walk
		return random.choice(stepChoices)

""" Simulate a single walk """
def walk(f, d, numSteps):
	""" Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
		Moves d numSteps times; returns the distance between the final 
		location and the location at the start of the walk.
	"""
	start = f.getLoc(d)
	for s in range(numSteps):
		f.moveDrunk(d)
	return start.distFrom(f.getLoc(d))

""" Simulate multiple walks """
def simWalks(numSteps, numTrials, dClass):
	"""	Assumes numSteps an int >= 0, numTrials an int > 0, dClass a subclass of Drunk
		Simulates numTrials walk of numSteps steps each. Returns a list of the final distances
		for each trial.
	"""
	Homer = dClass(dClass)
	origin = Location(0, 0)
	distances = []
	for t in range(numTrials):
		f = Field()
		f.addDrunk(Homer, origin)
		distances.append(round(walk(f, Homer, numSteps), 1))
	return distances

# Iterating over styles
class styleIterator(object):
	def __init__(self, styles):
		self.index = 0
		self.styles = styles

	def nextStyle(self):
		result = self.styles[self.index]
		if self.index == len(self.styles) - 1:
			self.index = 0
		else:
			self.index += 1
		return result

def simDrunk(numTrials, dClass, walkLengths):
	meanDistances = []
	for numSteps in walkLengths:
		print('starting simulation of', numSteps, 'steps')
		trials = simWalks(numSteps, numTrials, dClass)
		mean = sum(trials)/len(trials)
		meanDistances.append(mean)
	return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
	styleChoice = styleIterator(('m-','b--', 'g-.'))
	for dClass in drunkKinds:
		curStyle = styleChoice.nextStyle()
		print('Starting simulation of', dClass.__name__)
		means = simDrunk(numTrials, dClass, walkLengths)
		pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
	pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
	pylab.xlabel('Number of Steps')
	pylab.ylabel('Distance from Origin')
	pylab.legend(loc = 'best')
	pylab.show() # to show

if __name__ == '__main__':
	random.seed(0)
	numSteps = (10, 100, 1000, 10000)
	simAll((UsualDrunk, ColdDrunk), numSteps, 100)