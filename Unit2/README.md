# Unit 2 #

## Lecture 4 - Plotting ##
```python
import pylab as plt

# generate some example data
mySample = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
	mySample.append(i)
	myLinear.append(i)
	myQuadratic.append(i**2)
	myCubic.append(i**3)
	myExponential.append(1.5**i)

plt.figure('lin')
plt.clf()
plt.ylim(0, 1000)
plt.title('Linear')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySample, myLinear)

plt.figure('quad')
plt.clf()
plt.ylim(0, 1000)
plt.title('Quadratic')
plt.xlabel('sample points')
plt.ylabel('quadratic function')
plt.plot(mySample, myQuadratic)

plt.figure('cube')
plt.clf()
plt.title('Cube')
plt.xlabel('sample points')
plt.ylabel('cube function')
plt.plot(mySample, myCubic)

plt.figure('expo')
plt.clf()
plt.title('Expo')
plt.xlabel('sample points')
plt.ylabel('exponential function')
plt.plot(mySample, myExponential)

# cleaning up the window first
plt.clf()

### overlay plots
plt.figure('lin quad')
plt.clf()
plt.plot(mySample, myLinear, label = 'linear')
plt.plot(mySample, myQuadratic, label = 'quadratic')

plt.figure('cube exp')
plt.clf()
plt.plot(mySample, myCubic, label = 'cubic')
plt.plot(mySample, myExponential, label = 'exponential')

plt.figure('lin quad')
plt.title('Linear vs Quadratic')
plt.legend(loc = 'upper left')

plt.figure('cube exp')
plt.title('Cubic vs Exponential')
plt.legend()
```

```python
plt.plot(mySample, myLinear, '-b', label = 'linear', linewidth = 2.0)
plt.plot(mySample, myQuadratic, 'ro', label = 'quadratic')
plt.plot(mySample, myCubic, 'g^', label = 'exponential')
plt.plot(mySample, myExponential, 'r--', label = 'exponential')
```

Using subplots:
```python
plt.figure('lin quad')
plt.clf()

plt.subplot(211) # 2 rows and 1 col; 3rd arg is location
plt.ylim(0, 900)
plt.plot(mySample, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(mySample, myQuadratic, 'r', label = 'quadratic', linewidth = 3.0)
plt.legend(loc = 'upper left')
plt.title('Linear vs Quadratic')

plt.figure('cube exp')
plt.clf()
plt.subplot(121) # 1 row and 2 col; 3rd arg is location
plt.ylim(0, 140000)
plt.plot(mySample, myCubic, 'g--', label = 'cubic', linewidth = 4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(mySample, myExponential, 'r', label = 'exponential', linewidth = 5.0)
plt.legend()
plt.title('Cubic vs Exponential')
```

Changing scales:
```python
plt.yscale('log')
```

#### An Example: Compound Interest ####

```python
def retire(monthly, rate, terms):
	savings = [0]
	base = [0]
	mRate = rate/12
	for i in range(terms):
		base += [i]
		savings += [savings[-1] * (1 + mRate) + monthly]
	return base, savings

def displayRetireMonthlies(monthlies, rate, terms):
	plt.figure('retureMonth')
	plt.clf()
	for monthly in monthlies:
		xvals, yvals = retire(monthly, rate, terms)
		plt.plot(xvals, yvals, label = 'retire:' + str(month))
		plt.legend(loc = 'upper left')

displayRetireMonthlies([500,600, 700, 800, 900, 1000, 1100], .05, 40* 12)


def displayRetireWRates(month, rates, terms):
	plt.figure('retureRate')
	plt.clf()
	for rate in rates:
		xvals, yvals = retire(month, rate, terms)
		plt.plot(xvals, yvals, label = 'retire:'+str(month) + ':'+str(int(rate*100)))
		plt.legend(loc = 'upper left')

displayRetireWRates(800, [.03, .05, .07], 40*12)

def displayretureWMonthsAndRates(monthlies, rates, terms):
	plt.figure('retireBoth')
	plt.clf()
	plt.xlim(30*12, 40*12)
	for monthly in monthlies:
		for rate in rates:
			xvals, yvals = retire(monthly, rate, terms)
			plt.plot(xvals, yvals, label = 'retire:'+str(monthly) + ':'+str(int(rate*100)))
			plt.legend(loc = 'upper left')

displayretureWMonthsAndRates([500,700,900,1100], [.03, .05,.07], 40*12)
```

```python
def displayRetireWMonthsAndRates(monthlies, rates, terms):
	plt.figure('retireBoth')
	plt.clf()
	plt.xlim(30*12, 40*12)
	monthLabels = ['r', 'b', 'g', 'k']
	rateLabels = ['-', 'o', '-']
	for i in range(len(monthlies)):
		monthly = monthlies[i]
		monthLabel = monthLabels[i % len(monthLabels)]
		for j in range(len(rates)):
			rate = rates[j]
			rateLabel = rateLabels[j % len(rateLabels)]
			xvals, yvals = retire(monthly, rate, terms)
			plt.plot(xvals, yvals, monthLabel+rateLabel, label = 'retire:'+str(monthly)+':'+str(int(rate*100)))
			plt.legend(loc = 'upper left')
displayRetireWMonthsAndRates([500,700,900,1100],[.03,.05,.07], 40*12)
```

### Stochastic Thinking ###

Newtonian mechanics:
* every effect has a cause
* the world can be understood causally

Two centries lates:
* Copenhagen Doctrine (Bohr and Heisenberg) of **causal nondeterminism**
	* At its most fundamental level, the behavior of the physical world cannot be predicted
	* Fine to make statements of the form "x is highly likely to occur," but not of the form "x is certain to occur"

* Einstein and Schrodinger objected
	* "God does not play dice." -- Albert Einstein

* Does it really matter?
	* the world may or may not be inherently unpredictable
	* but our lack of knowledge does not allow us to make accurate predictions
	* therefore we might as well treat the world as inherently unpredictable
	* **predictive nondeterminism** - the concept that our inability to make accurate measurements about the physical world makes it impossible to make precise predictions about future states.
		* very different from **causal non-determinism** - the belief that not every event is caused by previous events.
	* the question of causal non-determinism is still unsettled
	* the reason we cannot predict events is because they are truly unpredictable or is because we simply do not have enough information to predict them is of no practical importance.

**Stochastic process** is an ongoing process where the next state might depend on both the previous states _and some random element_.

```python
def rollDie():
	"""Returns an int between 1 and 6; under determined """
	pass

def rollDie():
	""" Returns a randomly chosen int between 1 and 6; stochastic process """
```

```python
def squareRoot(x, epsilon):
	""" Assumes x and epsilon are of type float
			x >= 0 and epsilon > 0
		Returns float y such that 
			x - epsilon <= y*y <= x + epsilon """

	# This specification allows but does not require, 
	# a nondeterministic implementation
```
* The thing to keep in mind about non-deterministic programs is that they can be very tricky when debugging programs that call them, because sometimes we might get an answer that works and sometimes we might get an answer that does not work.

**Implement a random process**:
```python
import random

def rollDie():
	""" returns a random int between 1 and 6 """
	return random.choice([1, 2, 3, 4, 5, 6])

def testRoll(n = 10):
	result = ''
	for i in range(n):
		result = result + str(rollDie())
	print(result)
```

#### Exercise 1 ####
For the following explanations of different types of programmatic models, fill in the blank with the appropriate model the definition describes.

1. A _deterministic_ model is one whose behavior is entirely predictable. Every set of variable states is uniquely determined by parameters in the model and by sets of previous states of these variables. Therefore, these models perform the same way for a given set of initial conditions, and it is possible to predict precisely what will happen.


2. A _stochastic_ model is one in which randomness is present, and variable states are not described by unique values, but rather by probability distributions. The behavior of this model cannot be entirely predicted.


3. A _static_ model does not account for the element of time. In this type of model, a simulation will give us a snapshot at a single point in time.


4. A _dynamic_ model does account for the element of time. This type of model often contains state variables that change over time.


5. A _discrete_ model does not take into account the function of time. The state variables change only at a countable number of points in time, abruptly from one state to another.


6. A _continuous_ model does take into account the function of time, typically by modelling a function f(t) and the changes reflected over time intervals. The state variables change in an unbroken way through an infinite number of states.

---

1. If you are using differential equations to model a simulation, are you more likely to be doing a discrete or continuous model?  
**Answer**: Continuous

2. Let's say you run a stochastic simulation 100 times. How many times do you need to run the simulation again to get the same result?  
**Answer**: None will necessarily give you the same result.

3. Which modelling system would be best to model a bank account?  
**Answer**: Either discrete or continuous would work, depending on the specifics of the model you wish to use.

#### Exercise 2 ####

This problem asks you to write a short function that uses the the random module. Click on the above link to be taken to the Python docs on the random module, where you can see all sorts of cool functions the module provides.

The random module has many useful functions - play around with them in your interpreter to see how much you can do! To test this code yourself, put the line import random at the top of your code file, to import all of the functions in the random module. To call random module methods, preface them with random., as in this sample interpreter session:
```python
>>> import random
>>> random.randint(1, 5)
4
>>> random.choice(['apple', 'banana', 'cat'])
'cat'
```
How would you randomly generate an even number x, 0 <= x < 100? Fill out the definition for the function genEven(). Please generate a uniform distribution over the even numbers between 0 and 100 (not including 100).
```python
import random

def genEven():
	'''
	Returns a random even number x, where 0 <= x < 100
	'''
	randInt = int(random.uniform(0, 100))

	while  randInt % 2 != 0:
		randInt = int(random.uniform(0, 100))

	return randInt
```
#### Exercise 3.1 ####
Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.
```python
import random
def deterministicNumber():
	'''
	Deterministically generates and returns an even number between 9 and 21
	'''
	for i in range(9, 21):
		if i % 2 == 0:
			return i
```

#### Exercise 3.2 ####
Write a uniformly distributed stochastic program, stochasticNumber, that returns an even number between 9 and 21.
```python
import random
def stochasticNumber():
	'''
	Stochastically generates and returns a uniformly distributed even number between 9 and 21
	'''
	randInt = int(random.uniform(9, 21))

	while  randInt % 2 != 0:
		randInt = int(random.uniform(9, 21))

	return randInt
```
#### Exercise 4 ####

1. Are the following two distributions equivalent?
```python
import random
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1
```
**Answer**: Yes

2. Are the following two distributions equivalent?
```python
import random
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)
```
**Answer**: Yes

3. Are the following two distributions equivalent?
```python
import random
def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)
```
**Answer**: No

### Probabilities ###

Probability of various results:
* Consider `testRoll(5)`
	* which of the following outputs would surprise you?
		* 11111
		* 54424
	* what is the probability of each?

* Probability is about counting:
	* count the number of possible events
	* count the number of events that have the property of interest
	* divide one by the other
	* Probability of 11111?
		* 00000, 00001, 00002, ..., 66666
		* 1 / (6 ** 5) ~ 0.0001286 
	*  Probability of 54425? Exactly the same as above

Three Basic Facts About Probability
1. Probabilities are always in the range 0 to 1. 0 if impossible, and 1 if guaranteed.
2. If the probability of an event occurring is p, the probability of it not occurring must be 1-p.
3. When events are _independent_ of each other, the probability of all of the events occurring is equal to a _product_ of the probabilities of each of the events occurring.

**Independence**:
* Two events are _independent_ if the outcome of one event has no influence on the outcome of the other.  

Example: Will one of Real Madrid or Barca Lose?
* both good teams
* assume that both are playing
* assume each wins, on average, 7 out of 8 games
* probability of both winning is 7/8 * 7/8 = 49/64
* probability of at least one losing is 1 - 49/64 = 15/64
* probability of one team winning or losing is independent of the probability of the other team winning or losing. But suppose they play each other... Outcomes no longer independent.

**A Simulation**:
```python
import random
random.seed(0)

def runSim(goal, numTrials):
	total = 0
	for i in range(numTrials):
		result = ''
		for j in range(len(goal)):
			result += str(rollDie())
		if result == goal:
			total += 1
		print('Actual probability =', round(1/(6 ** (len(goals))), 8))
		estProbability = round(total/numTrials, 8)
		print('Estimated probability =', round(estProbability, 8))

runSim('11111', 1000)
```
Pseudorandom numbers generators work, typically, by reading some unexpected value, for ex, the number of milliseconds since Jan 1, 1968, which changes pretty quickly in a calc computer, and then off of that, what's called a seed generating the sequence of results. Given a seed, you always get the same sequence. But the seed is predictably non-deterministic. That is to say, we do not know what the seed will be. But you can cheat by setting the seed number; for example: `random.seed(0)`.  This is very useful when you're dubugging your program.  

If you try only a small number of trials, and you're looking at a very rare event, then you're likely to get the wrong answer out.

**How common are boxcars (double 6 when rolling dice)**?
* 6^2 possible combinations of two die
	* one 1 with two 6's
	* hence probability = 1/36
* another way of computing it
	* probability of rolling 6 with 1nd die = 1/6
	* probability of rolling 6 with 2nd die = 1/6
	* since these events are independent, probability of rolling a 6 with both die = 1/6 * 1/6 = 1/36

```python
def fracBoxCars(numTests):
	numBoxCars = 0
	for i in range(numTests):
		if rollDie() == 6 and rollDie() == 6:
			numBoxCars += 1
	return numBoxCars / numTests

print('Frequency of rolling double 6 =', str(fracBoxCars(1000000) * 100) + '%')
```
**Morals**:
* Moral 1: It takes a lot of trials to get a good estimate of the frequency of occurrence of a rare event. We'll talk lots more in later lectures about how to know when we have enough trials.
* Moral 2: One should not confuse the sample probability with the actual probability
* Moral 3: There was really no need to do this by simulation, since there is a perfectly good closed form answer. We will see many examples where this is not true.

#### Exercise 5 ####

In this problem, we're going to calculate some probabilities of dice rolls. Imagine you have two fair four-sided dice (if you've never seen one, here's a picture. The result, a number between 1 and 4, is displayed at the top of the die on each of the 3 visible sides). 'Fair' here means that there is equal probability of rolling any of the four numbers.

You can answer the following questions in one of two ways - you can calculate the probability directly, or, if you're having trouble, you can simply write out the entire sample space for the problem. A sample space is defined as a listing of all possible outcomes of a problem, and it can be written in many ways - a tree or a grid are popular options. For example, here is a diagram of the sample space for 3 coin tosses.

Some vocabulary before we begin: an event is a subset of the sample space, or, a collection of possible outcomes. A probability function assigns an event, A, a probability P(A) that represents the likelihood of event A occuring.

As an example, let's say we flip a coin. Define the event H as the event that the coin comes up heads. We can assign the probability P(H) = 1/2; the likelihood that event H occurs.

The following problems will ask for the probability that a given event occurs.

1. What is the size of the sample space for one roll of a four sided die?  
**Answer**: 4

2. What is the size of the sample space for two rolls of a four sided die?  
**Answer**: 4^2 = 16

3. Assume we roll 2 four sided dice. What is P({sum of the rolls is even})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/2

4. Assume we roll 2 four sided dice. What is P({rolling a 2 followed by a 3})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/4 * 1/4 = 1/16 #order matters

5. Assume we roll 2 four sided dice. What is P({rolling a 2 and a 3, in any order})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/8 #order doesnt matter

6. Assume we roll 2 four sided dice. What is P({sum of the rolls is odd})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/2

7. Assume we roll 2 four sided dice. What is P({first roll equal to second roll})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 4/16 = 1/4

8. Assume we roll 2 four sided dice. What is P({first roll larger than second roll})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 6/16 = 3/8

9. Assume we roll 2 four sided dice. What is P({at least one roll is equal to 4})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 7/16

10. Assume we roll 2 four sided dice. What is P({neither roll is equal to 4})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 9/16

#### Exercise 6 ####

In this problem, we're going to calculate some various probabilities.

1. What is the size of the sample space for two rolls of a ten sided die?  
**Answer**: 10^2 = 100


2. What is the size of the sample space for three rolls of an eight sided die?  
**Answer**: 8^3 = 512


3. What is the size of the sample space for drawing one card from a deck of 52 cards?  
**Answer**: 52


4. What is the size of the sample space for drawing one card from each of two decks of 52 cards? That is, drawing one card from one deck of cards, then a second card from a second deck of cards.  
**Answer**: 52^2 = 2704


5. Assume we roll 2 ten sided dice. What is P({rolling a 2 followed by a 3})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/10^2 = 1/100


6. Assume we roll 2 ten sided dice. What is P({first roll larger than second roll})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 45/100 = 9/20  #(n-1)+(n-2)+(n-3)+(n-4)+(n-5)+(n-6)+(n-7)+(n-8)+(n-9)+(n-10)=9+8+7+6+5+4+3+2+1+0=10+10+10+10+5=45


7. Assume we roll 3 eight sided dice. What is P({all three rolls are equal})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/64


8. A standard deck of cards contains 52 cards, 13 each of four suits - diamonds, clubs, hearts, and spades. Each suit contains one of 13 cards: A (ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, J (jack), Q (queen), K (king). Given one deck of 52 playing cards, you flip one over. Assuming a fair deck,what is P({ace of hearts})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/52


9. Given one deck of 52 playing cards, you flip one over. Assuming a fair deck, what is P({drawing a card with suit spades})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**:1/4


10. Given one deck of 52 playing cards, you flip one over. Assuming a fair deck, what is P({ace of any suit})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 4/52 = 1/13


11. Given one deck of 52 playing cards, you flip one over. Assuming a fair deck, what is P({any card except an ace})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1 - 4/52 = 1 - 1/13 = (13-1)/13 = 12/13


12. Given one deck of 52 playing cards, you draw two random cards. (The cards are drawn at the same time, so the selection is considered without replacement) Assuming a fair deck, what is P({both cards are aces})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 4/52 * 3/51 =12/2652 = 1/221


13. Given two decks of 52 playing cards, you flip one over from each deck. Assuming fair decks, what is P({the two cards are the same suit})? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/4


#### Exercise 7 ####

You pick three balls in succession out of a bucket of 3 red balls and 3 green balls. Assume replacement after picking out each ball. What is the probability of each of the following events?

1. Three red balls: A : {R,R,R}. Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 3/6 * 3/6 * 3/6 = 1/2 * 1/2 * 1/2 = 1/8

2. The sequence red, green, red: A : {R,G,R}. Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 3/6 * 3/6 * 3/6 = 1/2 * 1/2 * 1/2 = 1/8

3. Any sequence with 2 reds and 1 green. Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 3/8 #OPTIONS = {{R R R} {R R G -} {R G G} {G G G} {G G R} {G R R -} {G R G} {R G R -}}

4. Any sequence where the number of reds is greater than or equal to the number of greens. Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 4/8 = 1/2 #OPTIONS = {{R R R -} {R R G -} {R G G} {G G G} {G G R} {G R R -} {G R G} {R G R -}}

5. You have a bucket with 3 red balls and 3 green balls. This time, assume you _don't_ replace the ball after taking it out. What is the probability of drawing 3 balls of the same color? Answer in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 2 * 3/6 * 2/5 * 1/4 = 2* 1/2 * 2/5 * 1/4 = 2* 1/5 * 1/4 = 2* 1/20 = 2/20 = 1/10 #Prob of picking three balls of the color red. The prob of picking 3 balls of the same color is P{G,G,G} + P(R,R,R) = 1/20 + 1/20 = 2/20 = 1/10

### Random Walks ###

**Simulation Models**:
* A description of computations that provide useful information about the possible behaviors of the system being modeled.
* Simulation models are _typically_ most useful when there is more than one possible behavior, but that's certainly not the only situation.
* Simulation models are descriptive, not perscriptive. They're used to tell us what might happen, but they don't tell us how to make something happen.
* Only an approximation to reality
* "All models are wrong, but some are useful." - George Box

Simulations are used a lot:
* to model systems that are mathematically intractable
* to extract useful intermediate results
* lend themselves to development by successive refinement and "what if" questions - we can start with a relatively simple simulation that captures only some aspect of the system we're interested in and then slowly, step by step, make it more complicated, more realistic.

Why Random Walks?
* random walks are important in many domains
	* understanding the stock market
	* modeling diffusion processes
* good illustration of how to use simulations to understand things
* excuse to cover some important programming topics
	* using inheritance mechanisms
	* more about plotting

**Drunkard's Walk**:
* assume the following:
	* each step taken is of length 1
	* each step is parallel to either the x-axis or the y-axis
* with a prob of .25, he'll be 0 units away. With a prob of .25 he'll be 2 units away. With a prob of .5 he'll be sqrt(2) units away (due to Pythagorean theorem).
* .25 * 0 + .25 * 2 + .5 * sqrt(2) = 1.2

## Random Walks ##

### Location, Field, and Drunk ####
* Simulated, by hand, a walk in last lecture
* Process too labor intensive to be practical for more than a few steps
* But we can write a program to simulate lots of steps

**Structure of Simulation**:
* Simulate one walk of k steps
* Simulate n such walks
* Report average distance from origin

Some userful abstractions:
* Location - a place
* Field - a collection of places and drunks
* Drunk - somebody wanders from place to place in a field

```python
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
```

### Simulating a Walk ###

```python
""" Simulate a single walk """
def walk(f, d, numSteps):
	""" Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
		Moves d numSteps times; returns the distance between the final 
		location and the location at the start of the walk.
	"""
	start = f.getLoc(d)
	for s in range(numSteps):
		f.moveDrunk(d)
	return start.distFrom(f.getLoc(d))

""" Simulate multiple walks """
def simWalks(numSteps, numTrials, dClass, name):
	"""	Assumes numSteps an int >= 0, numTrials an int > 0, dClass a subclass of Drunk
		Simulates numTrials walk of numSteps steps each. Returns a list of the final distances
		for each trial.
	"""
	Homer = dClass(name)
	origin = Location(0, 0)
	distances = []
	for t in range(numTrials):
		f = Field()
		f.addDrunk(Homer, origin)
		distances.append(round(walk(f, Homer, numSteps), 1))
	return distances

def drunkTest(walkLengths, numTrials, dClass, name):
	"""	Assumes walkLengths a sequence of ints >= 0
			numTrials an int > 0
			dClass a subclass of Drunk
		For each number of steps in walkLengths,
			runs simWalks with numTrials walks and 
			prints results
	"""
	for numStep in walkLengths:
		distances = simWalks(numStep, numTrials, dClass, name)
		print(dClass.__name__, ' random walk of ', numStep, ' steps')
		print('Mean =', round(sum(distances)/len(distances), 4))
		print('Max =', max(distances), ' Min =', min(distances))
```

**Let's Try a Sanity Check**
* Try on cases where we think we know the anaswer
	* A very important precaution!

#### Exercise 1 ####
1. Would placing the drunk's starting location not at the origin change the distances returned?  
**Answer**: No

2. If so, what line would you modify to compensate? Enter the line number (eg 17). If not, just type None.  
```python
def simWalks(numSteps, numTrials, dClass):
	homer = UsualDrunk()
	notOrigin = Location(1, 0)
	distances = []
	for t in range(numTrials):
		f = Field()
		f.addDrunk(homer, notOrigin)
		distances.append(round(walk(f, homer, numSteps), 1))
	return distances
```
**Answer**: None

3. If you were going to use random.seed in a real-life simulation instead of just when you are debugging a simulation, would you want to seed it with 0?  
**Answer**: No

#### Exercise 2 ####

1. Is the following code deterministic or stochastic?
```python
import random
mylist = []

def main():
    myList = []
    for i in range(random.randint(1,10)):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1,10)
            myList.append(number)
    return myList
```
**Answer**: Stochastic

2. Which of the following alterations (Code Sample A or Code Sample B) would result in a deterministic process?
```python
import random

# Code Sample A
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print(mylist)

# Code Sample B
mylist = []

random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print(mylist)
```
**Answer**: Code Sample A AND Code Sample B

### Random Walks and More Plotting ###

```python
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

def simDrunk(numTrials, dClass, walkLengths):
	meanDistances = []
	for numSteps in walkLengths:
		print('starting simulation of', numSteps, 'steps')
		trials = simWalks(numSteps, numTrials, dClass)
		mean = sum(trials)/len(trials)
		meanDistances.append(mean)
	return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
	styleChoice = styleIterator(('m-','b--', 'g-.'))
	for dClass in drunkKinds:
		curStyle = styleChoice.nextStyle()
		print('Starting simulation of', dClass.__name__)
		means = simDrunk(numTrials, dClass, walkLengths)
		pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
	pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
	pylab.xlabel('Number of Steps')
	pylab.ylabel('Distance from Origin')
	pylab.legend(loc = 'best')

# Getting Ends of Multiple Walks
def getFinalLocs(numSteps, numTrials, dClass):
	locs = []
	d = dClass()
	for t in range(numTrials):
		f = Field()
		f.addDrunk(d, Location(0,0))
		for s in range(numSteps):
			f.moveDrunk(d)
		locs.append(f.getLoc(d))
	return locs
# Plotting Ending Locations
def plotLocs(drunkKinds, numSteps, numTrials):
	styleChoice = styleIterator(('k+', 'r^', 'mo'))
	for dClass in drunkKinds:
		locs = getFinalLocs(numSteps, numTrials, dClass)
		xVals, yVals = [], []
		for loc in locs:
			xVals.append(loc.getX())
			yVal.append(loc.getY())
		xVals = pylab.array(xValsx)
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
```

**Fields with Wormholes** - Einstein-Rosen Bridge:
```python
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
		d = UsualDrunk()
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
```

**Summary**:
* Point is not the simulations themselves, but how we built them
* Three classes corresponding to domain-specific types
	* Location
	* Field
	* Drunk
* Functions corresponding to:
	* One trial
	* Multiple trials
	* Result reporting
* Created two subclasses of Drunk
* Simulation had an argument of type class, so we could easily investigate both classes of Drunk
* Made series of incremental changes to simulation so that we could investigate different questions
	* Get simple version working first
	* Elaborate a step at a time
* Introduced a weird subclass of Field
	* Easy to add to simulation
	* Would have been hard to model analytically

#### Exercise 3 ####

1. The output of random.randint(1, 10) after a specific seed is shown below.
```python
>>> import random
>>> random.seed(9001)
>>> random.randint(1, 10)
1
>>> random.randint(1, 10)
3
>>> random.randint(1, 10)
6
>>> random.randint(1, 10)
6
>>> random.randint(1, 10)
7
```
We would like you to solve this problem using just the above output, without using the interpreter. (Note that the actual output you get when you run the above commands is actually going to be 1, 5, 5, 2, 10) What is printed in the following programs? Separate new lines with commas - so the above output would be 1, 3, 6, 6, 7.
```python
random.seed(9001)
for i in range(random.randint(1, 10)):
    print(random.randint(1, 10))
```
**Answer**: 3

2. 
```python
random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    print(d)
```
**Answer**: 1, 1, 1

3. 
```python
random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print(random.randint(1, 10))
```
**Answer**: 1, 1, 3

#### Exercise 4 ####

1. Suppose we wanted to create a class PolarBearDrunk, a drunk polar bear who moves randomly along the x and y axes taking large steps when moving South, and small steps when moving North.
```python
class PolarBearDrunk(Drunk):
    def takeStep(self):
        # code for takeStep()
```
Which of the following would be an appropriate implementation of takeStep()?
* Option A
```python
directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0)]
myDirection = random.choice(directionList)
if myDirection[0] == 0.0:
    return myDirection + (0.0, -0.5)
return myDirection
```
* Option B
```python
directionList = [(0.0, 0.5), (1.0, -0.5), (-1.0, -0.5), (0.0, -1.5)]
return random.choice(directionList)
```
* Option C
```python
directionList = [(0.0, 0.5), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.5)]
return random.choice(directionList)
```
* Option D
```python
directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (0.0, -1.0)]
return random.choice(directionList)
```
**Answer**: C