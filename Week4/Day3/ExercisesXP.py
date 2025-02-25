import scipy
import numpy as np
import matplotlib.pyplot as plt

""" Exercise 1: Basic Usage of SciPy

    Task: Import the SciPy library and explore its version.
"""
print("\nExercise 1\n")

print(scipy.__version__)


""" Exercise 2: Descriptive Statistics

    Task: Given a sample dataset, calculate the mean, median, variance, and standard deviation using SciPy.
    Sample Dataset: 
"""

data = [12, 15, 13, 12, 18, 20, 22, 21]
print("\nExercise 2\n")

print(f"Mean: {scipy.stats.tmean(data)}\nMedian: {np.median(data)}\nVariance: {scipy.stats.tvar(data)}\nstd: {scipy.stats.tstd(data)}") 


"""  Exercise 3: Understanding Distributions

    Task: Generate a normal distribution using SciPy with a mean of 50 and a standard deviation of 10. Plot this distribution.
"""

print("\nExercise 3\n")
mu = 50
std = 10

x = np.linspace(mu - 3*std, mu + 3*std, 100)
plt.plot(x, scipy.stats.norm.pdf(x, mu, std))
plt.title("Normal Distribution")
#plt.show()

""" Exercise 4: T-Test Application

    Task: Perform a T-test on two sets of randomly generated data.
"""

print("\nExercise 4\n")

data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)

t_stat, p_val = scipy.stats.ttest_ind(data1, data2)
print(f"t-statistic: {np.round(np.abs(t_stat),2)}\np-value {p_val,2}\nt-statistic > 2 and p-value < 0.05, therefore we can reject the null hypothesis that the to distibutions have the same mean value.")

print("\nExercise 5\n")

""" Exercise 5: Linear Regression Analysis

Objective: Apply linear regression to a dataset and interpret the results.

    Task: Given a dataset of housing prices (house_prices) and their corresponding sizes (house_sizes), use linear regression to predict the price of a house given its size.
    Dataset:
        house_sizes: [50, 70, 80, 100, 120] (in square meters)
        house_prices: [150,000, 200,000, 210,000, 250,000, 280,000] (in currency units)
    Questions:
    What is the slope and intercept of the regression line?
    Predict the price of a house that is 90 square meters.
    Interpret the meaning of the slope in the context of housing prices.
"""

print("\nExercise 5\n")

house_sizes= [50, 70, 80, 100, 120] # (in square meters)
house_prices= [150000, 200000, 210000, 250000, 280000]  # (in currency units)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(house_sizes, house_prices)

print("Slope:", slope)
print("Intercept:", intercept)
print(f"The price of a house that is 90 sqm wil be ${round(slope*90+intercept)}.")


""" Exercise 6: Understanding ANOVA

Objective: Test understanding of ANOVA and its application.

    Task: Three different fertilizers are applied to three separate groups of plants to test their effectiveness. The growth in centimeters is recorded.
    Dataset:
        fertilizer_1: [5, 6, 7, 6, 5]
        fertilizer_2: [7, 8, 7, 9, 8]
        fertilizer_3: [4, 5, 4, 3, 4]
    Questions:
    Perform an ANOVA test on the given data. What are the F-value and P-value?
    Based on the P-value, do the fertilizers have significantly different effects on plant growth?
    Explain what would happen if the P-value were greater than 0.05. """


print("\nExercise 6\n")

fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]

f_value, p_value = scipy.stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)
print("F-value:", f_value)
print("P-value:", p_value)
print("Mean values: ",  np.mean(fertilizer_1), np.mean(fertilizer_2), np.mean(fertilizer_3))

print("f-values is high and p-value is low. Therefore we can reject the null hypothesis that the three fertilizers generate the same effects on plant growth (equal mean values). That means the fertilizers generate different growth rates.")
print("If p-value is not lower than 0.05, that would mean that we can't reject the null hypothesis, ie, maybe the three fertilizers do generate the same effect.")
