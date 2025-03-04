

""" 1. Basic Indexing: Create an array of 10 elements and access the 5th element in it.

2. Basic Slicing: From the same array, extract a slice containing the 3rd to the 8th elements.

3. Boolean Indexing: Create an array of 6 random integers between 10 and 50. Print the elements that are greater than 30.

4. Fancy Indexing: From the same array, use fancy indexing to access the 2nd, 4th, and 6th elements.

Expected Output:

    The 5th element of the first array.
    A slice of the array showing elements from the 3rd to the 8th position.
    Elements greater than 30 from the random array.
    Selected elements (2nd, 4th, 6th) from the random array using fancy indexing.
 """
import numpy as np

arr = np.array(range(10))

print(arr[5])

print(arr[3:8])
arr = np.array([np.random.randint(10,50) for _ in range (6)])
print(arr)
print(arr[arr>30])
print(arr[1::2])

#%%


""" After learning about array indexing and slicing, it's important to practice these concepts. Here are some exercises to help solidify your understanding:

1. Modifying Specific Elements:

Create an array with values from 1 to 10. Change the value of the fifth element to 50.

2. Slicing and Modifying a Range:

Given an array of 10 elements, modify the elements from index 3 to 7 to be their negative equivalent.

3. Conditional Modification with Boolean Indexing:

Create an array with 20 random integers between 1 and 100. Set all values greater than 50 to -1.

4. Advanced Indexing Modification:

Given a 2D array of shape (5, 5), modify the elements in the diagonal to be twice their original value.

5. Understanding Slicing Impact:

Create an array of 10 elements. Slice the array from index 2 to 5, and modify the first element of the slice. Observe the change in the original array.

 """
import numpy as np
arr = np.array(range(10))
print(arr)
arr[3:7] = -arr[3:7]
print(arr)
arr = np.random.randint(1,100,20)
print(arr)
arr[arr>50] = -1
print(arr)
arr = np.ones([5,5])*np.random.randint(0,100)

for i in range(len(arr)):
    for j in range(len(arr)):
        if i==j:
            arr[i,j] = 2*arr[i,j]
print(arr)            

for i in range(len(arr)):
    for j in range(len(arr)):
        if i+j == 4:
            arr[i,j] = 0
print(arr)            

arr = np.array(range(10))
arr = arr[2:5]
arr[0] = 10
print(arr) 

#%%
# Creating two arrays
import numpy as np
a = np.array([[1], [2], [3]])
b = np.array([1, 2, 3])

# Adding the two arrays
result = a + b

print(f"Array a: ", a)
print(f"Array b:", b)
print(f"Broadcasted Addition: ", result)

#%%
import numpy as np

# Creating a 2D array and a 1D array
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2, 3])

# Element-wise multiplication
result = a * b

print(f"2D Array: ", a)
print(f"1D Array:", b)
print(f"Broadcasted Multiplication: ", result)


#1. Reshape Array: Create a 1D array with 12 elements and reshape it to a 4x3 matrix. Then reshape it to a 2x6 matrix.
arr_1d = np.array(range(12))
arr_2d = arr_1d.reshape(2,6)
print(arr_2d)
#2.
print(arr_2d.transpose())

#3. Combine Reshaping and Transposing: 
#Create a 3x4 matrix, transpose it, and then reshape the transposed 
#matrix to a 1D array.
arr_2d = arr_1d.reshape(3,4)
print(arr_2d)
print(arr_2d.transpose())
print(arr_2d.transpose().reshape(1,12))