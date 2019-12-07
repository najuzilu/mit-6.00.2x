## Unit 4 ##

### Experimental Data ###

Statistics meets experimental science:
* Conduct an experiment to gather data
	* Physical (e.g., in a biology lab)
	* Social (e.g., questionnaires)
* Use theory to generate some questions about data
	* Physcial (e.g., gravitational fields)
	* Social (e.g., people give inconsistent answers)
* Design a computation to help answer questions about data

*Linear spring*: amount of force needed to stretch or compress spring is linear in the distance the spring is stretched or compressed.
* each spring has a spring constant k, that determines how much force is needed

**Hooke's Law**:
* `F = -kd`
* How much does a rider have to weigh to compress spring 1cm?
* E.g.: `F = 0.01m * 35,000 N/m = 350 N` =>
* `F = mass * acc = mass * 9.8 m/s^2` =>
* `mass = 350N / (9.81 m/s^2)` =>
* `mass ~ 35.68k`

![Alt text](./HookesLaw.png)

Fitting Curves to Data:
* When we fit a curve to a set of dara, we are finding a fit that relates an independent variable (the mass) to an estimated value of a dependent variable (the distance).
* We need to define an objective function that provides a quantitative assessment of how well the curve fits that data.
* Finding the best fit can be formulated as finding the curve that minimizes the value of that function.
* Intuitively, you want to find a line, such that the space between the line and the observed points is minimized.

**Least Square Objective Function**:
* ![Alt text](./LOS.png)
* the difference between observed and predicted is often called the residual
* if we minimize the residual, then we minimize the variance

#### Exercise 1 ####
Using the formula derived in this segment, compute k from the second experimental observation: m = 0.15 kg, x = 0.1015 m. Use 9.81 m/s^2 as the gravitational constant (g). Enter your answer to at least 1 decimal place of accuracy.  
**Answer**: 14.5

### Fitting a Model to Data ###
* Use linear regression to find a polynomial
* We will use a degree-one polynomial, `y=ax + b` as model of our data (we want a line)
* Find values of a and b such that when we use the polynomial to compute y values for all of the x values in our experiment, the squared difference of these values and the corresponding observed values is minimized.
* A **linear regression** problem
* Many algorithms for doing this, including one similar to Newton's method (shown in 6.00.1x)

Polynomials with one variable (x):
* 0 or sum of finite number of non-zero terms
* each term of the form `cx^p`
	* c, the coefficient, a real number
	* p, the degree of the term, a non-negative integer
* the degree of the polynomial is the largest degree of any term
* Examples:
	* line: `ax + b`
	* parabola: `ax^2 + bx + c`

polyFit
* `pylab.polyfit(observedX, observedY, n)`
* Finds coefficients of a polynomial of degree n, that provides a best least squares fit for the observed data
```python
def fitData(fileName):
	xVals, yVals = getData(fileName)
	xVals = pylab.array(xVals)
	yVals = pylab.array(yVals)
	xVals = xVals * 9.81 # get force
	pylab.plot(xVals, yVals, 'bo', label = 'measured points')
	labelPlot()

	a, b = pylab.polyfit(xVals, yVals, 1)
	estYVals = a * pylab.array(xVals) + b
	print('a =', a, 'b =', b)
	pylab.plot(xVals, estYVals, 'r', label = 'Linear fit, k =' + str(round(1/a, 5)))
	pylab.legend(loc = 'best')
```

Version using polyval:
```python
def fitData1(fileName):
	xVals, yVals = getData(fileName)
	xVals = pylab.array(xVals)
	yVals = pylab.array(yVals)
	xVals = xVals * 9.81 # get force
	pylab.plot(xVals, yVals, 'bo', label = 'Measured points')
	labelPlot()
	model = pylab.polyfit(xVals, yVals)
	estYVals = pylab.polyval(model, xVals)
	pylab.plot(xVals, estYVals, 'r', label = 'Linear fit, k =' + str(round(1/model[0], 5)))
	pylab.legend(loc = 'best')
```

Higher degree models:
```python
model2 = pylab.polyfit(xVals, yVals, 2)
pylab.plot(xVals, pylab.polyval(model2, xVals), 'r--', label = 'Quadratic Model')
```

#### Exercise 2 ####
Which of the following lines will fit a parabola to the spring data given in the lecture file, springData.txt? Check all that work.  
**Answer**: 
* model = pylab.polyfit(xVals, yVals, 2)
* a,b,c = pylab.polyfit(xVals, yVals, 2)

Suppose the coefficients returned by polyval are in the tuple (c1, c2, c3). Which of the following lines calculate the estimated y values?  
**Answer**: estYVals = c1 * xVals ** 2 + c2 * xVals + c3

### Goodness of Fit ###

How good are these fits:
* Relative to each other
* In an absolute sense

Relative to each other:
* Fit is a function from the independent variable to the dependent variable 
(equivalent to asking about the accuracy of these estimations)
* Given an independent value, provides an estimate of the dependent value
* Which fit provides better estimates

Comparing Mean Squared Error:
```python
def aveMeanSquareError(data, predicted):
	error = 0.0
	for i in range(len(data)):
		error += (data[i] - predicted[i])**2
	return error/len(data)

estYVals = pylab.polyval(model1, xVals)
print('Ave mean square error for linear model =', aveMeanSquareError(yVals, estYVals))
estYVals = pylab.polyval(model2, xVals)
print('Ave mean square error for quadratic model =', aveMeanSquareError(yVals, estYVals))
```

In an Absolute Sense:
* Mean square error useful for comparing two different models for the same data
* Useful for getting a sense of absolute goodness of fit?
	* Is 1524 good?
* Hard to know, since there is no upper bound and not scale independent
* Instead we use **coefficient of determination**, R^2 ![Alt text](./rSquared.png)
	* {y_i} is actual value
	* {p_i} is predicted value
	* {mu} is the mean
	* Think of the numerator as the amount of error in the estimates
	* Think of the denominator as capturing the variability in the estimates, how much they differ from the mean

```python
def rSquared(observed, predicted):
	error = ((predicted - observed)**2).sum()
	meanError = error/len(observed)
	return 1 - (meanError/numpy.var(observed))
```

R^2:
* By comparing the estimation error (the numerator) with the variability of the original values (the denominator), R^2 is intended to capture the proportion of variability in a data set that is accounted for by the statistical model provided by the fit.
* If the dataset is highly variable, then it's harder to model it, if it's very constant, it's easier to model it
* Always between 0 and 1 when fit generated by a linear regression and tested on training data
* If R^2 = 1, the model explains all the variability in the data. If R^2 = 0, there is no relationship between the values predicted by the model and the actual data. If R^2 = 0.5, the model explains half the variability in the data

```python
def genFits(xVals, yVals, degrees):
	models = []
	for d in degrees:
		model = pylab.polyfit(xVals, yVals, d)
		models.append(model)
	return models

def testFits(models, degrees, xVals, yVals, title):
	pylab.plot(xVals, yVals, 'o', label = 'Data')
	for i in range(len(models)):
		estYVals = pylab.polyval(models[i], xVals)
		error = rSquared(yVals, estYVals)
		pylab.plot(xVals, estYVals, label = 'Fit of degree ' + str(degrees[i]) + ', R2 = ' + str(round(error, 5)))
		pylab.legend(loc = 'best')
		pylab.title(title)

xVals, yVals = getData('mysteryData.txt')
degrees = (1, 2)
models = genFits(xVals, yVals, degrees)
testFits(models, degrees, xVals, yVals, 'Mystery data')

### Compare higher-order fits
xVals, yVals = getData('mysteryData.txt')
degrees = (2, 4, 8, 16)
models = genFits(xVals, yVals, degrees)
testFits(models, degrees, xVals, yVals, 'Mystery data')
```
#### Exercise 4 ####

Recall from the previous video the concept of the coefficient of determination, also known as the  𝑅2  value. This is computed by (formula). The variability of the errors is computed by taking the sum of the squares of (observed - predicted) errors. We normalize this variablity by dividing it by the variability of the data, which is sum of the squares of (observation - average_observation) for each observation.
In this file, this  𝑅2  value is computed by the function rSquare.
In that file, revise fitData and fitData3 to report the coefficient of determination for the fitted line in each case. Did this measure of the "goodness of fit" improve when we eliminated the measurements after the spring reached its elastic limit and Hooke's Law no longer applied?  
**Answer**: Yes

