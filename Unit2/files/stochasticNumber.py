import random

def stochasticNumber():
	'''
	Stochastically generates and returns a uniformly distributed even number between 9 and 21
	'''
	randInt = int(random.uniform(9, 21))

	while  randInt % 2 != 0:
		randInt = int(random.uniform(9, 21))

	return randInt

if __name__ == '__main__':
	print(stochasticNumber())