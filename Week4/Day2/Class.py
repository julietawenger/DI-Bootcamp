
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
