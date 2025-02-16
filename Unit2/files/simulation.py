import random
random.seed(0)

def rollDie():
	""" returns a random int between 1 and 6 """
	return random.choice([1, 2, 3, 4, 5, 6])

def runSim(goal, numTrials):
	total = 0
	for i in range(numTrials):
		result = ''
		for j in range(len(goal)):
			result += str(rollDie())
		if result == goal:
			total += 1
	print('Actual probability =', round(1/(6 ** (len(goal))), 8))
	estProbability = round(total/numTrials, 8)
	print('Estimated probability =', round(estProbability, 8))

runSim('11111', 1000)
runSim('11111', 1000000)