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
		self.angle = random.randint(0, 359)
		room.cleanTileAtPosition(self.position)

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
			self.angle = random.randint(0, 359)
			position = position.getNewPosition(self.angle, self.speed)
		self.position = position
		self.room.cleanTileAtPosition(self.position)

# robot = Robot(RectangularRoom(8,12), 1.0)
ted = StandardRobot(RectangularRoom(8,12), 1.0)
ted.updatePositionAndClean()
# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)