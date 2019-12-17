## Final Exam ##

### Problem 1 ###

1. Consider deriving the probability of a coin flip coming up heads by running m trials of 100 flips each. If the coin is fair, the mean probability of the m trials will go to 0.5 as m goes to infinity.  
**Answer**: True

2. Consider two normal distributions, A and B. The standard deviation of A is 3 and the standard deviation of B is 5. For each distribution, 1,000 observations are drawn and plotted in a histogram with 10 bins, creating one histogram for each distribution.  
**Answer**: Any of the above are possible.

3. You roll an unfair (weighted) die. The distribution of the numbers rolled is a uniform distribution.  
**Answer**: False

4. A simulation  
**Answer**: All of the above

5. The following image plots the population of the US over time, along with a model fit to the data. This is an example of  
**Answer**: Overfitting

6. If the  𝑅^2  of a model produced using linear regression is 0.7, the model accounts for 70% of the variance in the observations.  
**Answer**: True

7. Given a finite set of data points there exists a polynomial fit such that the polynomial curve goes through each point in the data.  
**Answer**: False

8. You want to calculate confidence intervals by applying the empirical rule, which requires that you have a normal distribution with a known mean and standard deviation. Which approach can you use to estimate the mean and standard deviation that you need? Choose all that work.  
**Answer**:
* Central Limit Theorem, which requires that you have many sufficiently large samples from the population
* Standard Error, which requires that you have one sufficiently large sample

9. You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. Assume that once you draw a ball out of the bucket, you don't replace it. What is the probability of drawing 3 balls of the same color? Answer the question in reduced fraction form - eg 1/5 instead of 2/10.  
**Answer**: 1/7

### Problem 2 ###
Consider the following code:

```python
import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
```
For each of the following questions, select the best answer from the set of choices.

1. The values in tVals are most closely:  
**Answer**: Distributed with a Gaussian distribution

2. The values in xVals are most closely:  
**Answer**: Uniform distribution

For each of the following expressions using the code above, match the following calls to pylab.plot with one of the graphs shown below.
You can click on the following images to view a larger size.

3. `pylab.plot(xVals, zVals)`  
**Answer**: Graph 5

4. `pylab.plot(xVals, yVals)`  
**Answer**: Graph 4

5. `pylab.plot(xVals, sorted(yVals))`  
**Answer**: Graph 3

6. `pylab.plot(sorted(xVals), yVals)`  
**Answer**: Graph 2

7. `pylab.plot(sorted(xVals), sorted(yVals))`  
**Answer**: Graph 1

### Problem 3 ###

In a lecture, there are 3 things you might do: listen, sleep, or Facebook (in a single lecture, you might do all, some, or none of them). Lectures are independent of each other, the probabilities associated with the activities are independent of each other, and they are all > 0. You are given the following class, Lecture, and the function, get_mean_and_std.

Write a Monte Carlo simulation called lecture_activities(N, aLecture) that meets the specifications below.

```python
import random
        
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
        
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    # IMPLEMENT THIS FUNCTION

          
# sample test cases 
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)
          
b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)
```
You are not allowed to import anything. Do not leave any debugging print stataments. Click "See full output" to see the test cases passed/failed. Paste only the lecture_activities function and any helper functions you made for yourself (if any).

### Problem 4 ###
You are given the following function and class and function specifications for the two coding problems on this page (also available in this file, die.py):
```python
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
```
Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None), with the following specification:
```python
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
```
Paste your entire function (including the definition) in the box.

Restrictions:
* Do not paste import pylab in the box.
* You should only be using the pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show functions from the pylab module.
* Do not leave any debugging print statements when you paste your code in the box.

#### Problem 4.2 ####
Write a function called getAverage(die, numRolls, numTrials), with the following specification:

```python
def getAverage(die, numRolls, numTrials):
	"""
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
```
A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:

* a dice roll of 1 4 3 has a longest run of 1
* a dice roll of 1 3 3 2 has a longest run of 2
* a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3
When this function is called with the test case given in the file, it will return 5.312. Your simulation may give slightly different values.

Paste your entire function (including the definition) in the box.

Restrictions:

* Do not import or use functions or methods from pylab, numpy, or matplotlib.
* Do not leave any debugging print statements when you paste your code in the box.
* If you do not see the return value being printed when testing your function, close the histogram window.

### Problem 5 ###

K-means is a greedy algorithm, meaning it looks for local minimum when choosing points closest to the centroid. For each dataset illustrated below, will k-means, as shown in lecture, using Euclidean distance as the metric be able to find clusters that match the dataset patterns?

1. **Answer**: No
2. **Answer**: Yes
3. **Answer**: No
4. **Answer**: No
5. **Answer**: Yes
6. **Answer**: No

### Problem 6 ###
Write a function that meets the specifications below. You do not have to use dynamic programming.

Hint: You might want to use bin() on an int to get a string, get rid of the first two characters, add leading 0's as needed, and then convert it to a numpy array of ints. Type help(bin) in the console.

For example,

* If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
* If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
* If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
More specifically, write a function that meets the specifications below:
```python
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
```

### Problem 7 ###
Answer the next questions on machine learning, related to the following data. Consider the following 6 people who are either happy or unhappy and the data we know on them:

1. Using the Manhattan distance and looking only at "Income" and "Distance from North Pole", which two people are closest and farthest?  
**Answer**: closest: Person 3 and Person 4 ||| farthest: Person 1 and Person 5

2. If we were to cluster the people, the inclusion/exclusion of which feature would never impact the final clusters?  
**Answer**: Continents Visited

### Problem 8.A ###
For this problem you are going to simulate growth of fox and rabbit population in a forest!

The following facts are true about the fox and rabbit population:

The maximum population of rabbits is determined by the amount of vegetation in the forest, which is relatively stable.

There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.

For each rabbit during each time step, a new rabbit will be born with a probability of  𝑝rabbit reproduction 
𝑝rabbit reproduction=1.0−current rabbit populationmax rabbit population 
In other words, when the current population is near the maximum, the probability of giving birth is very low, and when the current population is small, the probability of giving birth is very high.

The population of foxes is constrained by number of rabbits.

There are never fewer than 10 foxes.

At each time step, after the rabbits have finished reproducing, a fox will try to hunt a rabbit with success rate of  𝑝fox eats rabbit 
𝑝fox eats rabbit=current rabbit populationmax rabbit population 
In other words, the more rabbits, the more likely a fox will eat one.

If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately. Remember that the population of rabbits is never lower than 10.

Additionally, if a fox succeeds in hunting, then it has a 1/3 probability of giving birth in the current time-step.

If a fox fails in hunting then it has a 10 percent chance of dying in the current time-step.

If the starting population is below 10 then you should do nothing. You should not increase the population nor set the population to 10. 
Start with 500 rabbits and 30 foxes.

At the end of each time step, record the number of foxes and rabbits.

Run the simulation for 200 time steps, and then plot the population of rabbits and the population of foxes as a function of time step. (You do not need to paste your code for plotting for Part A of this problem).

Use the following steps, and the template file rabbits.py (click to download .py file), as guides in your implementation of this simulation.

Step 1: Write the procedure, rabbitGrowth, that updates the number of rabbits during the first part of a time step

Step 2: Write the procedure, foxGrowth, that updates the number of rabbits and foxes during the second part of a time step

Step 3: Write the master procedure, runSimulation, that loops for some amount of time steps, doing the first part and then the second part of the simulation. Record the two populations in two different lists, and return those lists.

Paste your code for the three functions rabbitGrowth, foxGrowth, and runSimulation in the following box.

WARNING
DO NOT define the global variables MAXRABBITPOP, CURRENTRABBITPOP, or CURRENTFOXPOP in this box. We alter the values of these variables to test your code. If you define the variables in this box, you may overwrite our values, causing your code to be marked incorrect.

CLARIFICATIONS / HINTS
"See Full Output": If you are getting the line "0 10" in your output for "Test 4 foxGrowth" then for this particular test, your code changes the CURRENTFOXPOP (increases it if the fox population has gone below the minimum fox population), which is not the right behavior -- the code should not reset CURRENTFOXPOP.
It is not correct to assume that there is a 1/3 chance that the population increases in "Test 3 foxGrowth". Pay special attention to the following statement in the docstring of foxGrowth(): "Each fox, based on the probabilities in the problem statement, may eat one rabbit (but only if there are more than 10 rabbits)."

### Problem 8b ###
Follow the next steps of the simulation to answer the remaining questions.

Step 4: Assume MAXRABBITPOP = 1000, CURRENTRABBITPOP = 500, CURRENTFOXPOP = 30, numSteps = 200. Plot two curves, one for the rabbit population and one for the fox population. You won't be submitting the plots. They are for your own understanding.

Step 5: Use polyfit to find the coefficients of a 2nd degree polynomial for the rabbit curve and the same for the fox curve. Then use polyval to evaluation the 2nd degree polynomial and plot it, e.g.

`coeff = polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)`
`plot(polyval(coeff, range(len(rabbitPopulationOverTime))))`
Of course your variables and plotting commands may not look identical to the above code; the above code is shown just to give you an idea of what we mean.

Once you have finished Steps 4 and 5, continue on to answer the following questions.

1. At some point in time, there are more foxes than rabbits.  
**Answer**: True

2. The polyfit curve for the rabbit population is:  
**Answer**: A concave up curve (looks like a U shape)


3. The polyfit curve for the fox population is:  
**Answer**: A concave down curve (looks like a ∩ shape)


4. Changing the initial conditions from 500 rabbits and 30 foxes to 50 rabbits and 300 foxes changes the general shapes of both the polyfit curves for the rabbit population and fox population.  
**Answer**: False


5. Let's say we make a change in the original simulation. That is, we are going to change one detail in the original simulation, but everything else will remain the same as it was explained in Problem 8 - Part A.

Now, if a fox fails in hunting, it has a 90 percent chance of dying (instead of a 10 percent chance, as in the original simulation).

Changing the probability of an unsuccessful fox dying from 10% to 90% changes the general shapes of both the polyfit curves for the rabbit population and fox population.  
**Answer**: False