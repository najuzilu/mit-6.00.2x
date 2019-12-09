## Pset 4 ##

In this problem set, you will use regression analysis to model the climate of different areas and try to find evidence of global warming. You will create models to analyze and visualize climate change in terms of temperature. 

Download ps4.zip.

Please do not rename the files we provide you with, change any of the provided helper functions, change function/method names, or delete provided docstrings. You will need to keep data.csv in the same folder as ps4.py.

To model the change in climate of an area, you will need some data. For this problem set, we will use temperature data obtained from the National Centers for Environmental Information (NCEI). The data, stored in data.csv , contains the average temperatures observed in 21 U.S. cities from 1961 to 2015. Open the file, and take a look at the raw data.

In order to parse the raw data, in ps4.py w e have implemented a helper class Climate. You can initialize an instance of the Climate class by providing the filename of the raw data. Look over this class and read its docstrings to figure out how to get data for the following problems.

### Problem 1: Curve Fitting ###

Implement the generate_models function.
* x and y are two lists corresponding to the x-coordinates and y-coordinates of the data samples (or data points); for example, if you have N data points, x = [x1 , x2 , ..., xN ] and y = [y1 , y2 , ..., yN ], where x_i and y_i are the x and y coordinate of the i-th data points. In this problem set, each x coordinate is an integer and corresponds to the year of a sample (e.g., 1997); each corresponding y coordinate is a float and represents the temperature observation (will be computed in multiple ways) of that year in Celsius. This representation will be used throughout the entire problem set.
* degs is a list of integers indicating the degree of each regression model that we want to create. For each model, this function should fit the data (x,y) to a polynomial curve of that degree.
* This function should return a list of models. A model is the numpy 1d array of the coefficients of the fitting polynomial curve. Each returned model should be in the same order as their corresponding integer in degs.

### Problem 2: R^2###
After we create some regression models, we also want to be able to evaluate our models to figure out how well each model represents our data, and tell good models from poorly fitting ones. One way to evaluate how well the model describes the data is computing the model's R^2 value. R^2 provides a measure of how well the total variation of samples is explained by the model.

Implement the function r_squared. This function will take in:

* list, y, that represents the y-coordinates of the original data samples
* estimated, which is a corresponding list of y-coordinates estimated from the regression model

This function should return the computed R^2 value. You can compute R^2 as follows, where  𝑒𝑖  is the estimated y value for the i-th data point (i.e. predicted by the regression),  𝑦𝑖  is the y value for the ith data point, and  𝑚𝑒𝑎𝑛  is the mean of the original data samples.

### Problem 3 ###
We have learned how to obtain a numerical metric for evaluation. Visualizing our data samples along with fitting curves can also help us figure out the goodness of obtained models. In this problem, we will integrate the numerical metrics and visualization for a comprehensive evaluation.

Implement function evaluate_models_on_training. This function takes as input your data samples (x and y) and the list of models (which are lists of coefficients obtained from generate_models) that you want to apply to your data.

This function should generate a figure for each model. In this figure, you are to plot your data along with your best fit curve, and report on the goodness of the fit with the R^2 value. When you are writing this function try to make your graph match the following format:

* Plot the data points as individual blue dots
* Plot your model as a red solid line
* Include a title and label your axes
* Your title should include the value of your model and the R^2 degree of this model. Your title could be longer than your graph. To fix that you can add "\n", which adds a newline to your string, in your title when you concatenate several pieces of information (e.g., title = string_a + "\n" + string_b ).

After you finish writing the function, you have all the components needed to start generating data samples from the raw temperature records and investigate the trend. Run the following code at the bottom ps4.py.
```
# Problem 3
y = []
x = INTERVAL_1
for year in INTERVAL_1:
    y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
models = generate_models(x, y, [1])
evaluate_models_on_training(x, y, models)
```
This code just randomly picks a day from a year (i.e., Jan 10th in this case), and sees whether we can find any trend in the temperature changing over the years. We surmise, due to global warming, that the temperature of this specific date should increase over time. This code generates your data samples; each sample represents a year from 1961 to 2005 (i.e., the years in INTERVAL_1) and the temperature of Jan 10th for Boston in that year (provided helper class is helpful for this). The code fits your data to a linear line with generate_models and plots the regression results with evaluate_models_on_training.

What is the R^2 value? (use 3 decimal places)  
**Answer**: 0.005

### Problem 4 ###
Let's try another way to get data points and see whether we can find some evidence for global warming. We surmise, due to global warming, the average temperature should increase over time. Thus, we are going to plot the results of a linear regression on the average annual temperature of Boston.

In a similar manner to Problem 3, fill in the missing piece to the following code. The code should generate your data samples. Each sample represents a year from 1961 to 2005 and the average annual temperature in Boston in that year (again, the provided helper class is helpful). Fit your data to a linear line with generate_models and plot the regression results with evaluate_models_on_training.

```
# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
# MISSING LINES
models = generate_models(x1, y, [1])    
evaluate_models_on_training(x1, y, models)
```


1. **Answer**:
```
for year in INTERVAL_1:
    y.append(numpy.mean(raw_data.get_yearly_temp('BOSTON', year)))
```

2. What is the R^2 value? (use 3 decimal places)  
**Answer**: 0.085

### Problem 5 ###
Which graph, choosing a specific day (Jan 10) or calculating the yearly average, indicates that almost none of the data variation is learned by our model?  
**Answer**: Choosing a specific day


Which graph, choosing a specific day (Jan 10) or calculating the yearly average, supports more the claim that global warming is leading to an increase in temperature?  
**Answer**: calculating the yearly average