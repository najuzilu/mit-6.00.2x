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

def getFinalLocs(numSteps, numTrials, dClass):
	locs = []
	d = dClass(dClass)
	for t in range(numTrials):
		f = Field()
		f.addDrunk(d, Location(0,0))
		for s in range(numSteps):
			f.moveDrunk(d)
		locs.append(f.getLoc(d))
	return locs

# Plotting Ending Locations
def plotLocs(drunkKinds, numSteps, numTrials):
	styleChoice = styleIterator(('k+', 'r^', 'mo'))
	for dClass in drunkKinds:
		locs = getFinalLocs(numSteps, numTrials, dClass)
		xVals, yVals = [], []
		for loc in locs:
			xVals.append(loc.getX())
			yVals.append(loc.getY())
		xVals = pylab.array(xVals)
		yVals = pylab.array(yVals)
		meanX = sum(abs(xVals))/len(xVals)
		meanY = sum(abs(yVals))/len(yVals)
		curStyle = styleChoice.nextStyle()
		pylab.plot(xVals, yVals, curStyle, label = dClass.__name__ + ' mean abs dist = <' + str(meanX) + ', ' + str(meanY) + '>')
	pylab.title('Location at End of Walks (' + str(numSteps) + ' trials)')
	pylab.xlabel('Steps East/West of Origin')
	pylab.ylabel('Steps North/South of Origin')
	pylab.ylim(-1000,1000)
	pylab.xlim(-1000,1000)
	pylab.legend(loc = 'upper left')
	pylab.show()

if __name__ == '__main__':
	random.seed(0)
	plotLocs((UsualDrunk, ColdDrunk), 10000, 1000)