import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
# Simulating stock prices for a non-existent stock (DVLPRS)
np.random.seed(0)  # For reproducibility

# Generating 100 days of stock prices
dates = pd.date_range(start='2023-01-01', periods=100)
prices = np.random.normal(loc=100, scale=10, size=len(dates))  # Assume a mean price of 100 with a standard deviation of 10

# Creating a DataFrame
stock_data = pd.DataFrame({
    'Date': dates,
    'DVLPRS_Price': prices
})

# Displaying the first few rows of the simulated data
print(stock_data.head())

stock_array = stock_data['DVLPRS_Price'].to_numpy()
print(stock_array)
print(np.mean(stock_array), np.std(stock_array), np.median(stock_array))

import matplotlib.pyplot as plt

plt.hist(stock_array)
plt.show()

from scipy import stats

statistic, pvalue = stats.normaltest(stock_array)
print(pvalue)


""" 
Objective: Implement and interpret linear regression using SciPy.

1. Dataset: x = np.array([2, 4, 6, 8, 10]), y = np.array([3, 5, 7, 9, 11]).

2. Perform linear regression to find slope and intercept.

3. Plot data points and regression line.

4. Interpret the results, focusing on the slope and intercept. """

x = np.array([2, 4, 6, 8, 10])
y = np.array([3, 5, 7, 9, 11])

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.scatter(x,y)
x2 = np.linspace(0,11,1000)
y2 = slope*x2 + intercept
plt.plot(x2,y2)
plt.show()
