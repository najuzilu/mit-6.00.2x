## Unit 2 ##

#### Lecture 4 - Plotting ####
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

##### An Example: Compound Interest #####

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