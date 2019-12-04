# python3

import random

def noReplacementSimulation(numTrials):
	'''
	Runs numTrials trials of a Monte Carlo simulation
	of drawing 3 balls out of a bucket containing
	3 red and 3 green balls. Balls are not replaced once
	drawn. Returns the a decimal - the fraction of times 3 
	balls of the same color were drawn.
	'''

	def drawThreeConsequtiveBalls(balls = 6):
		count = 0.0
		arrayOfBalls = [_ for _ in range(balls)]
		finalSelection = []

		for i in range(3): # 3 consecutive picks
			currentPick = random.choice(arrayOfBalls)
			arrayOfBalls.remove(currentPick)
			if currentPick <= 2:
				finalSelection.append(1)
			else:
				finalSelection.append(0)
		if sum(finalSelection) == 3 or sum(finalSelection) == 0:
			count += 1
		return count

	totalCount = 0.0
	count = 0.0
	for t in range(numTrials):
		totalCount += 1
		count += drawThreeConsequtiveBalls()

	return count / totalCount


print('Test case 1 with 5000 trials expected value between 0.088 and 0.112')
print(noReplacementSimulation(5000))

print('Test case 2 with 5000 trials expected value between 0.088 and 0.112')
print(noReplacementSimulation(5000))