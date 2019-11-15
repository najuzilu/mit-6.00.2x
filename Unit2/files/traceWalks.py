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

class OddField(Field):
	def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
		Field.__init__(self)
		self.wormholes = {}
		for w in range(numHoles):
			x = random.randint(-xRange, xRange)
			y = random.randint(-yRange, yRange)
			newX = random.randint(-xRange, xRange)
			newY = random.randint(-yRange, yRange)
			newLoc = Location(newX, newY)
			self.wormholes[(x,y)] = newLoc

	def moveDrunk(self, drunk):
		Field.moveDrunk(self, drunk)
		x = self.drunks[drunk].getX()
		y = self.drunks[drunk].getY()
		if (x,y) in self.wormholes:
			self.drunks[drunk] = self.wormholes[(x, y)]

# Tracing a Walk
def traceWalk(fieldKinds, numSteps):
	styleChoice = styleIterator(('b+', 'r^', 'ko'))
	for fClass in fieldKinds:
		d = UsualDrunk(UsualDrunk)
		f = fClass()
		f.addDrunk(d, Location(0,0))
		locs = []
		for s in range(numSteps):
			f.moveDrunk(d)
			locs.append(f.getLoc(d))
		xVals, yVals = [], []
		for loc in locs:
			xVals.append(loc.getX())
			yVals.append(loc.getY())
		curStyle = styleChoice.nextStyle()
		pylab.plot(xVals, yVals, curStyle, label = fClass.__name__)
	pylab.title('Spots Visited on Walk (' + str(numSteps) + ' steps)')
	pylab.xlabel('Steps East/West of Origin')
	pylab.ylabel('Steps North/South of Origin')
	pylab.legend(loc = 'best')
	pylab.show()

if __name__ == '__main__':
	traceWalk((Field, OddField), 500)