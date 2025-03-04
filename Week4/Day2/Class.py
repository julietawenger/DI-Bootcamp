
import numpy as np
movie_ratings = np.array([
    [5, 1, 4],
    [4, 4, 2],
    [4, 3, 5],
    [1, 1, 5],
    [3, 2, 1]
])
for row in movie_ratings:
    print(np.mean(row))

for i in movie_ratings.transpose():
    print(max(i))


# Temperature data matrix (4 cities, 7 days)
temperature_data = np.array([
    [27, 20, 15, 18, 26, 18, 22],
    [24, 18, 20, 17, 19, 22, 21],
    [23, 23, 27, 25, 16, 21, 22],
    [22, 29, 23, 16, 20, 24, 28]
])

# Tasks: Calculate average, max, min temperatures and make day comparisons

for i in temperature_data:
    print(np.mean(i), min(i), max(i))


dates = np.arange('2020-01', '2020-02', dtype='datetime64[D]')
print("January 2020 Dates:\n", dates)

formatted_dates = np.datetime_as_string(dates, unit='D')
print("Formatted Dates:\n", formatted_dates)


import numpy as np

""" 1. Data Creation Exercise:

Objective: Create a simulated time series dataset.

Instructions:

    Generate a date range from January 1, 2022, to December 31, 2022, with a daily frequency.
    Simulate daily temperature data for this period. Assume temperature varies between 10°C and 35°C.
    Simulate daily humidity data for the same period. Assume humidity varies between 30% and 90%.
    Structure the data into a DataFrame with columns: Date, Temperature, and Humidity.

2. Data Analysis Exercise:

Objective: Perform basic data analysis on the time series data.

Instructions:

    Calculate the mean, median, and standard deviation for both temperature and humidity.
    Identify the date with the highest temperature and the date with the highest humidity.
    [bonus] Plot the temperature and humidity trends over the year.

3. Window Function Exercise:

Objective: Apply window functions to the time series data.

Instructions:

    Use a rolling window of 7 days to calculate the moving average for both temperature and humidity.
    [bonus] Plot the original data and the 7-day moving average on the same graph for comparison.
 """

dates = np.arange('2022-01-01', '2023-12-31', dtype='datetime64[D]')
temperatures = np.random.uniform(10,35,len(dates))
print(temperatures)