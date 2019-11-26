# python 3

import pylab
import random
import math

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

class Drunk(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'This drunk is named ' + self.name


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

def walkVector(f, d, numSteps):
	start = f.getLoc(d)
	for s in range(numSteps):
		f.moveDrunk(d)
	return(f.getLoc(d).getX() - start.getX(),
		   f.getLoc(d).getY() - start.getY())

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
		xDist, yDist = walkVector(f, Homer, numSteps)
		distances.append(round((xDist**2 + yDist**2)**0.5, 1))
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
	styleChoice = styleIterator(('k+', 'r^', 'mo', 'o', 's'))
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
	for each in (UsualDrunk, ColdDrunk, PhotoDrunk, DDrunk, EDrunk):
		plotLocs((each,), 10000, 1000)