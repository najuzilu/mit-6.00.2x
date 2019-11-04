import random

def genEven():
	'''
	Returns a random even number x, where 0 <= x < 100
	'''
	randInt = int(random.uniform(0, 100))

	while  randInt % 2 != 0:
		randInt = int(random.uniform(0, 100))

	return randInt

if __name__ == '__main__':
	print(genEven())
