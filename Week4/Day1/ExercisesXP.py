import numpy as np
""" Exercise 1 : Array Creation and Manipulation
Instructions

Create a 1D NumPy array containing numbers from 0 to 9."""
#%%
print("\nExercise 1\n")
print(np.array(range(10)))

""" Exercise 2 : Type Conversion and Array Operations
Instructions

Convert a list [3.14, 2.17, 0, 1, 2] into a NumPy array and convert its data type to integer. """

print("\nExercise 2\n")

l = [3.14, 2.17, 0, 1, 2]
print(np.int64(l))

""" Exercise 3 : Working with Multi-Dimensional Arrays
Instructions

Create a 3x3 NumPy array with values ranging from 1 to 9. """

print("\nExercise 3\n")

arr = np.array(range(1,10)).reshape(3,3)
print(arr)

""" Exercise 4 : Creating Multi-Dimensional Array with Random Numbers
Instructions

Create a 2D NumPy array of shape (4, 5) filled with random numbers. """

print("\nExercise 4\n")
print(np.round(np.random.random([4,5]),2))

""" Exercise 5 : Indexing Arrays
Instructions

Select the second row from a given 2D NumPy array. """

print("\nExercise 5\n")
arr = np.array([[21,22,23,22,22],[20, 21, 22, 23, 24],[21,22,23,22,22]])
print(f"Array: {arr}")

print(f"Second row: {arr[1,:]}")

""" Exercise 6 : Reversing elements
Instructions

Reverse the order of elements in a given 1D NumPy array (first element becomes last). """

print("\nExercise 6\n")

arr = np.array(range(10))
print(f'Array: {arr}')
print(f'Reversed: {arr[::-1]}')

""" Exercise 7 : Identity Matrix
Instructions

Create a 4x4 identity matrix using NumPy. """

print("\nExercise 7\n")
print(np.diag([1,1,1,1]))
print(np.eye(4, dtype = int))

""" Exercise 8 : Simple Aggregate Funcs
Instructions

Find the sum and average of a given 1D array. """

print("\nExercise 8\n")
arr = np.array(range(10))
print(f"Array:{arr}\nSum: {sum(arr)}\nAverage: {np.mean(arr)}")


""" Exercise 9 : Create Array and Change its Structure
Instructions

Create a NumPy array with elements from 1 to 20; then reshape it into a 4x5 matrix. """

print("\nExercise 9\n")
arr = np.array(range(1,21))
print(f"Array: {arr}\nReshaped: {arr.reshape(4,5)}")


""" Exercise 10 : Conditional Selection of Values
Instructions

Extract all odd numbers from a given NumPy array. """
print("\nExercise 10\n")
arr = np.array(range(1,21))
print(f"Array: {arr}\nOdd numbers: {arr[arr %2==1]}")
