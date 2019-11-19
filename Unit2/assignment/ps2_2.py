import math
import random

import ps2_visualize
import pylab

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement

class Position(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getNewPosition(self, angle, speed):
		old_x, old_y = self.getX(), self.getY()
		angle = float(angle)
		delta_x = speed * math.sin(math.radians(angle)) # fixed
		delta_y = speed * math.cos(math.radians(angle)) # fixed
		new_x = old_x + delta_x
		new_y = old_y + delta_y
		return Position(new_x, new_y)

class RectangularRoom(object):
	"""
	Represents a rectangular region containing clean or dirty tiles.
	"""
	def __init__(self, width, height):
		"""
		Initialize a rectangular room with the specified width and height.

		Initially, no tiles in the room have been cleaned.
		"""
		self.width = width
		self.height = height
		self.tiles = [[False for i in range(width)] for i in range(height)] # horizontal is width; vertical is height
		self.cleaned_tiles = []

	def cleanTileAtPosition(self, pos):
		"""
		Mark the tile under the position POS as cleaned.
		"""
		x = math.floor(pos.getX())
		y = math.floor(pos.getY())
		self.tiles[y][x] = True

	def isTileCleaned(self, m, n):
		"""
		Return True if tile (m, n) has been cleaned, False otherwise.
		"""
		m = math.floor(m)
		n = math.floor(n)
		return self.tiles[n][m]

	def getNumTiles(self):
		"""
		Return the total number of tiles in the room.
		"""
		return self.width * self.height

	def getNumCleanedTiles(self):
		"""
		Return the total number of clean tiles in the room
		"""
		count = 0
		for row in self.tiles:
			for tile in row:
				if tile:
					count += 1
		return count

	def getRandomPosition(self):
		"""
		Returns a random position inside the room
		"""
		randX = random.randint(0, self.width - 1)
		randY = random.randint(0, self.height - 1)
		return Position(math.floor(randX), math.floor(randY))
		# randX = self.width * random.random()
		# randY = self.height * random.random()
		# return Position(randX, randY)

	def isPositionInRoom(self, pos):
		"""
		Return True if pos is inside the room, False otherwise.
		"""
		posX = pos.getX()
		posY = pos.getY()
		return (posX < self.width) and (posX >= 0) and (posY >= 0) and (posY < self.height)

class Robot(object):
	def __init__(self, room, speed):
		self.room = room
		self.speed = speed
		self.position = room.getRandomPosition()
		self.angle = random.randint(0, 360)
		self.room.cleanTileAtPosition(self.position)

	def getRobotPosition(self):
		return self.position

	def getRobotDirection(self):
		return self.angle

	def setRobotPosition(self, position):
		self.position = position

	def setRobotDirection(self, angle):
		self.angle = angle

	def updatePositionAndClean(self):
		raise NotImplementedError # don't change this!

class StandardRobot(Robot):

	def updatePositionAndClean(self):
		position = self.position.getNewPosition(self.angle, self.speed)

		# If position not in room continue calculating until position in room
		while not self.room.isPositionInRoom(position):
			self.angle = random.randint(0, 360)
			position = position.getNewPosition(self.angle, self.speed)
		
		self.position = position
		self.room.cleanTileAtPosition(self.position)

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):
	"""
		In each trial, the objective is to determine how many time-steps are on 
		average needed before a specified fraction of the room has been cleaned?
	"""
	all_simulations = []
	for _ in range(num_trials):
		counter = 0
		room = RectangularRoom(width, height)
		robots = [robot_type(room, speed) for _ in range(num_robots)]
		tilesToClean = math.ceil(min_coverage * room.getNumTiles())
		while (robots[0].room.getNumCleanedTiles() < tilesToClean):
			anim.update(room, robots)
			for rbt in robots:
				rbt.updatePositionAndClean()
			counter += 1
		all_simulations.append(counter)
	anim.done()
	return sum(all_simulations) / len(all_simulations)

class RandomWalkRobot(Robot):

	def updatePositionAndClean(self):
		self.angle = random.randint(0, 360)
		position = self.position.getNewPosition(self.angle, self.speed)

		while not self.room.isPositionInRoom(position):
			self.angle = random.randint(0, 360)
			position = position.getNewPosition(self.angle, self.speed)

		self.position = position
		self.room.cleanTileAtPosition(self.position)


def showPlot1(title, x_label, y_label):
	"""
	What information does the plot produced by this function tell you?
	"""
	num_robot_range = range(1, 11)
	times1 = []
	times2 = []
	for num_robots in num_robot_range:
		print("Plotting", num_robots, "robots...")
		times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
		times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
	pylab.plot(num_robot_range, times1)
	pylab.plot(num_robot_range, times2)
	pylab.title(title)
	pylab.legend(('StandardRobot', 'RandomWalkRobot'))
	pylab.xlabel(x_label)
	pylab.ylabel(y_label)
	pylab.show()

	
def showPlot2(title, x_label, y_label):
	"""
	What information does the plot produced by this function tell you?
	"""
	aspect_ratios = []
	times1 = []
	times2 = []
	for width in [10, 20, 25, 50]:
		height = 300//width
		print("Plotting cleaning time for a room of width:", width, "by height:", height)
		aspect_ratios.append(float(width) / height)
		times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
		times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
	pylab.plot(aspect_ratios, times1)
	pylab.plot(aspect_ratios, times2)
	pylab.title(title)
	pylab.legend(('StandardRobot', 'RandomWalkRobot'))
	pylab.xlabel(x_label)
	pylab.ylabel(y_label)
	pylab.show()

if __name__ == '__main__':
	num_robots = 3
	speed = 1.0
	width = 5
	height = 5
	percentCleaned = 0.7
	trials = 1
	delay = 0.6

	# global anim
	# #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
	# anim = ps2_visualize.RobotVisualization(num_robots, width, height, delay)
	# avg = runSimulation(num_robots, speed, width, height, percentCleaned, trials, StandardRobot)

testRobotMovement(RandomWalkRobot, RectangularRoom)
# testRobotMovement(StandardRobot, RectangularRoom)
