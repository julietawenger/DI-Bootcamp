import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""  Exercise 1 : Matrix Operations
Instructions

In this exercise, you’ll work with a 3x3 matrix. Here’s a brief explanation of the concepts:

    Determinant: The determinant is a value that can be computed from the elements of a square matrix. It provides important information about the matrix, such as whether it has an inverse, and is used in various areas like linear algebra and calculus. To understand more about it you can watch this video.
    Inverse of a Matrix: The inverse of a matrix is a matrix that, when multiplied with the original matrix, results in an identity matrix. Not all matrices have inverses. The inverse is crucial in solving systems of linear equations.

Create a 3x3 matrix and perform the following operations:

    Calculate the determinant.
    Find the inverse of the matrix.
 """

print("\nExercise 1\n")

arr = np.array(np.random.random(9)).reshape([3,3])

print(f"M = {arr}\ndet(M) = {np.linalg.det(arr)}\nM^(-1) = {np.linalg.inv(arr)}")

""" Exercise 2 : Statistical Analysis
Instructions

In this exercise, you’ll calculate statistical measures for a dataset:

    Mean: The average value of a dataset.
    Median: The middle value in a dataset when it is arranged in ascending or descending order.
    Standard Deviation: A measure of the amount of variation or dispersion in a set of values.

Using NumPy, generate an array of 50 random numbers and compute:

    The mean and median.
    The standard deviation.
"""

print("\nExercise 2\n")

arr = np.random.randint(0,100,50)
print(f"Array: {arr}\nMean: {np.mean(arr)}\nMedian: {np.median(arr)}\nstd: {np.std(arr)}")

""" 
Exercise 3 : Date Manipulation
Instructions

Create a NumPy array of dates for the month of January 2023. Convert these dates to another format (e.g., YYYY/MM/DD). """

print("\nExercise 3\n")


dates = np.arange('2023-01', '2023-02', dtype='datetime64[D]')

def format_date(date):
    return str(date).replace("-", "/")
print("January 2023 Dates:\n", dates)
dates = [format_date(d) for d in dates]
print("Formatted January 2023 Dates:\n", dates)

"""  Exercise 4 : Data Manipulation with NumPy and Pandas
Instructions

Create a DataFrame with random numbers and perform:

    Conditional selection of data.
    Aggregation functions like sum and average.
"""

print("\nExercise 4\n")

df = pd.DataFrame(np.random.randint(0,100,49).reshape([7,7]), columns = ["A", "B", "C", "D", "E", "F", "G"])
print(f"Dataframe: {df}")
print(f"Rows with D values greater than 50: \n{df[df["D"]>50]}")

print(f"sum(A): {np.sum(df["A"])}\nmean(A): {np.mean(df["A"])}")

""" Exercise 5 : Image Representation
Instructions

Explain how images are represented in NumPy arrays and demonstrate with a simple example (e.g., creating a 5x5 grayscale image). """

print("\nExercise 5\n")

arr= np.array(range(25)).reshape([5,5])
plt.imshow(arr)
plt.show()

# Images are represented with colormap, in which each color represents a different intensity, given by the matrix.

"""  Exercise 6 : Basic Hypothesis Testing
Instructions

Create a sample dataset to test the effectiveness of a new training program on employee productivity: 

Given a dataset, formulate a simple hypothesis and test it using basic statistical functions in NumPy.

"""

# Productivity scores of employees before the training program
productivity_before = np.random.normal(loc=50, scale=10, size=30)

# Productivity scores of the same employees after the training program
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

# Your task is to formulate a hypothesis regarding the training program's effectiveness 
# and test it using basic statistical functions in NumPy.

print("\nExercise 6\n")

print("Null hypothesis: the productivity did not change.\nAlternative Hypothesis: the productivity increased.")

from scipy import stats

# I want to prove that the two samples have the same average. I need to use ttest_rel. This Calculates the T-test on TWO RELATED samples of scores, a and b.
t_statistic, p_value = stats.ttest_rel(productivity_before, productivity_after)

# Interpreting the result
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

print("This means that productivity increased, with a p-value < 0.05.")    


""" Exercise 7 : Complex Array Comparison
Instructions

Create two arrays and perform element-wise comparison to find which elements are greater in the first array.

The expected output is a boolean array showing which elements in the first array are greater than the corresponding elements in the second array. """

print("\nExercise 7\n")

arr_1 = np.random.randint(0,100,10)
arr_2 = np.random.randint(0,100,10)
arr_3 = arr_1>arr_2
print(f"arr_1: {arr_1}\narr_2: {arr_2}\narr_3 = arr_1 > arr_2 = {arr_3}")


""" Exercise 8 : Time Series Data Manipulation
Instructions

Generate time series data for the year 2023. Demonstrate slicing for the following intervals:

    January to March
    April to June
    July to September
    October to December

Generate a time series data for a specific period and demonstrate how to slice this data for different intervals. """

print("\nExercise 8\n")


dates = np.arange('2022-01', '2023-01', dtype='datetime64[M]')
print(f"January to March: {dates[:3]}\nApril to June: {dates[3:6]}\nJuly to September: {dates[6:9]}\nOctober to December: {dates[9:]}\n")
#Example
dates= np.arange('2023-01', '2023-03', dtype='datetime64[D]')
dates[1::3] # Goes from the second day till the end by 3 days intervals.


""" Exercise 9 : Data Conversion
Instructions

Demonstrate how to convert a NumPy array to a Pandas DataFrame and vice versa. """


print("\nExercise 9\n")

arr = np.array(range(9)).reshape([3,3])
df = pd.DataFrame(arr)

print(f"Array: {arr}\nDataframe: {df}\nBack to array: {df.to_numpy()}")


""" Exercise 10 : Basic Visualization
Instructions

Use Matplotlib to visualize a simple dataset created with NumPy (e.g., a line graph of random numbers). """

print("\nExercise 10\n")

x = np.linspace(0,np.pi*2)
y = np.sin(x) + np.random.random(len(x))
plt.plot(x,y, color = "teal")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()