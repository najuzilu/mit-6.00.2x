## Unit 5 ##

### Machine Learning ###
* Many useful programs learn something
* In the last two 6.00.2x lectures we used linear regression to learn models of data
* "Field of study that gives computers the ability to learn without being explicitly programed." Arthur Samuel.

What is machine learning?
* Modern statistics meets optimization
![Alt text](./ml.png)

How are things learned?
* Memorization
	* Accumulation of individual facts
	* Limited by
		* Time to observe facts
		* Memory to store facts
* Generalization
	* Deduce new facts from old facts
	* Limited by accuracy of deduction process
		* Essentially a predictive activity
		* Assumes that the past predicts the future

Basic paradigm:
* observe set of examples: training data (represents incomplete information)
* infer something about process that generated that data 
* use inference to make predictions about previously unseen data: test data

All ML methods require:
* Represenation of the features
* Distance metric for feature vectors
* Objective function and constraints
* Optimization method for learning the model
* Evaluation method
	* We need to know whether we should put any faith in the model
	* Also, we use these evaluation methods to tune the parameters of the learning method

**Supervised learning**:
* Start with set of feature vector/value pairs
* Goal: find a model that predicts a value for a previously unseen feature vector
* Regression model predict a real number
	* As with linear regression
* Classification models predict a label (chosen from a finite set of labels)

**Unsupervised learning**:
* Start with a set of feature vectors (no labels!)
* Goal: uncover some latent structure in the set of feature vectors
* Clustering: the most common technique
	* Define some metric that captures how similar one feature vector is to another
	* Group examples based on this metric

Choosing features:
* Features never fully describe the situation
* Feature enginnering
	* Represent examples by feature vectors that will facilitate generalization
	* Suppose I want to use 100 examples from past to predict which students will pass the final exam
	* Some features surely helpful, e.g., their grade on the midterm, did they do the problem sets, etc.
	* Others might cause me to overfit, e.g., birth month
* Want to maximize ratio of useful input to irrelevant input
	* Signal-to-noise ratio (SNR)

#### Exercise 1 ####
For the following problems, decide whether it would be better to perform supervised or unsupervised learning given the data.

1. 100,000 emails are read and marked as spam or not spam, depending on some metrics measured on their content(keywords, length, etc). We want to determine what a new email will be marked as.  
**Answer**: Supervised

2. A junkyard has 500 objects with 2 and 4 wheels. We want to separate the objects into 4 different groups.  
**Answer**: Unsupervised

3. A group of 1000 students are asked for a sample of their handwriting. Researchers make pairs of (handwritten text, typed text). Given a new handwriting sample from a new student, we want to determine what the typed version of the handwriting sample would be.  
**Answer**: Supervised

4. Given a set of t-shirts, we want to organize them in 3 different piles.  
**Answer**: Unsupervised

5. Given a greenhouse full of plants, we want to organize them so that they can be given away to novice, intermediate, and expert plant handlers.  
**Answer**: Unsupervised

6. Given a set of colored points on an x-y axis, we want to place a new point on the plot, knowing its color.  
**Answer**: Supervised

7. A school documents the age, grade, score on a math standardized test, and score on a writing standardized test for every student. A new student comes to the school and we want to decide what grade they should be placed in.  
**Answer**: Supervised

### K-Nearest Neighbors ###
Distance between vectors:
* Minkowski metric: 
![Alt text](./MinkowskiMetric.png)

```python
# Producing the distance matrix
columnLabels = []
for a in animals:
	columnLabels.append(a.getName())
rowLabels = columnLabels[:]
tableVals = []

# Get distances between pairs of animals

# for each row
for a1 in animals:
	row = []
	# for each column
	for a2 in animals:
		if a1 == a2:
			row.append('--')
		else:
			distance = a1.distance(a2)
			row.append(str(round(distance, precision)))
	tableVals.append(row)

# Producing the table
table = pylab.table(rowLabels = rowLabels, colLabels = columnLabels, cellText = tableVals, cellLoc = 'center', colWidths = [0.138]*len(animals))
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.5)
pylab.axis('off')
pylab.savefig('distances')
```

Uinsg distance matrix for classification:
* Simplest approach is probably nearest neighbor
* Remember training data
* When predicting the label of a new example
	* Find the nearest example in the training datra
	* Predict the label associated with that example

Advantages and disadvantages of KNN:
* Advantages:
	* Learning fast, no explicit training
	* No theory required
	* Easy to explain method and results
* Disadvantages:
	* Memory intensive and predictions can take a long time
		* Are better algorithms than brute force
	* No model to shed light on process that generated data

A more general approach: scaling:
* Z-scaling
	* Each feature has a mean of 0 and standard deviation of 1
* Interpolation
	* Map min value to 0 and max val to 1, and linearly interpolate

```python
def zScaleFeature(vals):
	"""Assumes vals is a sequence of floats"""
	result = pylab,array(vals)
	mean = float(sum(result))/len(result)
	result = result - mean
	return result/stdDev(result)

def iScaleFeature(vals):
	"""Assumes vals is a sequence of floats"""
	minVal, maxVal = min(vals), max(vals)
	fit = pylab.polyfit([minVal, maxVal], [0, 1], 1)
	return pylab.polyval(fit, vals)
```

#### Exercise 2 ####
For the following question, check the boxes that correspond to the rules that we may be able to learn. Consider the following set of 6 emails, which classify the email as spam or not. Which of the following rules might we learn? Check all that apply.

**Answer**:
* Emails containing both flagged words "cash" and "free" are marked "spam".
* Emails containing at least one flagged word in all capital letters are marked "spam".

#### Exercise 3 ####
For each of the following situations state whether it would be a good idea to scale the features.

1. One feature set is height (in meters) and the other is weight (in kilograms).  
**Answer**: Scale

2. One feature set is the number of detected earthquakes in a city and the other is the population in that city.  
**Answer**: Scale

3. The percent concentration of a virus in a random sampling of healthy and unhealthy people.  
**Answer**: Don't scale

4. The angle of refraction of light (degree that light bends) observed when entering water vs. glass vs a diamond.  
**Answer**: Don't scale

### Clustering ###
