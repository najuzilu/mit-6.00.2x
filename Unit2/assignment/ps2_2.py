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
		# randX = random.randint(0, self.width - 1)
		# randY = random.randint(0, self.height - 1)
		randX = self.width * random.random()
		randY = self.height * random.random()
		# return Position(math.floor(randX), math.floor(randY))
		return Position(randX, randY)

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
			for rbt in robots:
				rbt.updatePositionAndClean()
			counter += 1
		all_simulations.append(counter)
	return sum(all_simulations) / len(all_simulations)




# print("Testing 1 robot at 1.0 speed cleaning 50% of a 20x20 room")
# print(runSimulation(1, 1.0, 5, 5, .5, 1000, StandardRobot))

# print("Testing 1 robot at 1.0 speed cleaning 100% of a 20x20 room")
# print(runSimulation(1, 1.0, 10, 12, 1, 1000, StandardRobot)) # my output=116; correct=115
	
# print("Testing 3 robot at 1.0 speed cleaning 50% of a 20x20 room")
# print(runSimulation(3, 1.0, 5, 5, .5, 1000, StandardRobot))

# print("Testing 3 robot at 1.0 speed cleaning 100% of a 20x20 room")
# print(runSimulation(3, 1.0, 10, 12, 1, 1000, StandardRobot)) # my output=116; correct=115

print('Testing 1 robot with 1.0 speed, cleaning 20-100% of 5x5 room')
print(runSimulation(1, 1.0, 5, 5, 0.2, 1000, StandardRobot))
print(runSimulation(1, 1.0, 5, 5, 0.4, 1000, StandardRobot))
print(runSimulation(1, 1.0, 5, 5, 0.6, 1000, StandardRobot))
print(runSimulation(1, 1.0, 5, 5, 0.8, 1000, StandardRobot))
print(runSimulation(1, 1.0, 5, 5, 1, 1000, StandardRobot))

print('\nTesting 3 robot with 1.0 speed, cleaning 20-100% of 5x5 room')
print(runSimulation(3, 1.0, 5, 5, 0.2, 1000, StandardRobot))
print(runSimulation(3, 1.0, 5, 5, 0.4, 1000, StandardRobot))
print(runSimulation(3, 1.0, 5, 5, 0.6, 1000, StandardRobot))
print(runSimulation(3, 1.0, 5, 5, 0.8, 1000, StandardRobot))
print(runSimulation(3, 1.0, 5, 5, 1, 10000, StandardRobot))

print('\nTesting 3 robot with 4.0 speed, cleaning 20-100% of 5x5 room')
print(runSimulation(3, 4.0, 5, 5, 0.2, 1000, StandardRobot))
print(runSimulation(3, 4.0, 5, 5, 0.4, 1000, StandardRobot))
print(runSimulation(3, 4.0, 5, 5, 0.6, 1000, StandardRobot))
print(runSimulation(3, 4.0, 5, 5, 0.8, 1000, StandardRobot))
print(runSimulation(3, 4.0, 5, 5, 1, 10000, StandardRobot))
