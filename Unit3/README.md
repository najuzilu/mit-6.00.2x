##Unit 3##

###Inferential Statistics###
* Population: a set of examples
* Sample: a proper subset of a population
* Goal: estimate some statcitic about the population based on statistics about the sample
* Key fact: If the sample is **random**, it tends to exhibit the same properties as the population from which it is drawn

**Why the difference in confidence**?
* Confidence in our estimate depends upon two things
	* the size of sample (100 vs 2)
	* variance of sample (all heads versus 52 heads)
* As the variance grows, we need larger samples to have the same degree of confidence

```python
import random

class FairRulette():
	def __init__(self):
		self.pockets = []
		for i in range(1, 37):
			self.pockets.append(i)
		self.ball = None
		self.blackOdds, self.redOdds = 1.0, 1.0
		self.pocketOdds = len(self.pockets) - 1.0

	def spin(self):
		self.ball = random.choice(self.pockets)

	def isBlack(self):
		if type(self.ball) != int:
			return False
		if ((self.ball > 0 and self.ball <= 10)) or (self.ball >18 and self.ball <=28):
			return self.ball % 2 == 0
		else:
			return self.ball % 2 == 1

	def isRed(self):
		return type(self.ball) == int and not self.isBlack()

	def betBlack(self, amt):
		if self.isBlack():
			return amt * self.blackOdds
		return -amt

	def betRed(self, amt):
		if self.isRed():
			return amt * self.redOdds
		return -amt

	def betPocket(self, pocket, amt):
		if str(pocket) == str(self.ball):
			return amt * self.pocketOdds
		return -amt

	def __str__(self):
		return 'Fair Roulette'

def playRoulette(game, numSpins, toPrint = True):
	luckyNumber = '2'
	bet = 1
	toRed, toBlack, toPocket = 0.0, 0.0, 0.0
	for i in range(numSpins):
		game.spin()
		toRed += game.betRed(bet)
		toBlack += game.betBlack(bet)
		toPocket += game.betPocket(luckyNumber, bet)

	if toPrint:
		print(numSpins, ' spins of', game)
		print('Expected return betting red =', str(100 * toRed / numSpins) + '%')
		print('Expected return betting black =', str(100 * toBlack / numSpins) + '%')
		print('Expected return betting ', luckyNumber, '=', str(100 * toPocket / numSpins) + '%')
	return (toRed/numSpins, toBlack/numSpins, toPocket/numSpins)

numSpins = 10000000
game = FairRulette()
playRoulette(game, numSpins)
```
**The Law of Large Numbers** (aka Bernoulli's Law):
* In repeated independent tests with the same actual probability p of a particular outcome in each test, the chance that the fraction of times that outcome occurs differs from p converges to zero as the number of trials goes to infinity.

**Gambler's Fallacy**:
* If deviations from expected behavior occur, these deviations are likely to be evened out by opposite deviations in the future
* Probability of 15 consecutive reds: 1/32,378
* Probability of 25 consecutive reds: 1/33,554,432
* Probability of 26 consecutive reds: 1/67,108,865
* Probability of 26 consecutive reds when previous 25 rolls were red: 1/2
* Gambler's Fallacy is confused with regression to the mean (something that's actually correct)

**Regression to the Mean**:
* Following an extreme random event, the next random event is likely to be less extreme
* If you spin a fair roulette wheel 10 times and get 100% reds, that is an extreme event (probability = 1/1024)
* It is likely that in the next 10 spins, you will get fewer than 10 reds
* So if you look at the average of the 20 spins, it will be closer to the expected mean of 50% reds than to the 100% you saw in the first 10 spins
* First used by Francis Galton, 1885

####Exercise 1####
1. A fair two-sided coin is flipped 4 times. It comes up heads all four times. What is the probability that it comes up heads on the fifth flip? Answer in reduced fraction form - eg 1/5 instead of 2/10.   
**Answer**: 1/2

2. A fair two-sided coin is flipped 1000 times. It comes up heads every time. Which is correct?  
**Answer**: Regression to the mean tells us that the next few tosses will be not as extreme as the first 1000.

3. Next we toss a huge ball with 1,000 dots on it. Half the dots are red and the other half are blue. We roll the ball and when it stops, we note the color of the dot on the very top of the ball.
True or False? If we roll it four times, and it comes up red once and blue three times, then we have proved that the ball is biased.  
**Answer**: False