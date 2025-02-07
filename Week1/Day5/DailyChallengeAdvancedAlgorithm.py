""" Instructions

Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728


Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

For example

1000 and 2728 sums to the target_number 3728
1864 and 1864 sums to the target_number 3728
"""

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728
list_of_numbers = [num for num in list_of_numbers if num<=target_number ]
list_of_numbers_copy = [num for num in list_of_numbers if num<=target_number ]
print(list_of_numbers)


stored_pairs=[]
for i in list_of_numbers:
    for j in list_of_numbers:
        if i + j == target_number:
            if (i in list_of_numbers_copy) and (j in list_of_numbers_copy) and i!=j:
                list_of_numbers_copy.remove(i)
                list_of_numbers_copy.remove(j)
            else:
                continue                    
            stored_pairs.append((i,j))

lst = [i for i in list_of_numbers_copy if i == int(target_number/2) and target_number%2==0]  # If the target number is even, I'll have pairs of equal numbers       

pairs = [(lst[i], lst[i+1]) for i in range(0, len(lst) - 1, 2)] # This are all the pairs of equal numbers
remaining = lst[-1] if len(lst) % 2 != 0 else [] # This is the remaining one
stored_pairs += pairs # I add those to the stored pairs
list_of_numbers_copy = [i for i in list_of_numbers_copy if i!=int(target_number/2)] # I take those out
list_of_numbers_copy += [remaining] # I add the remaining one, if there's any
print(stored_pairs)  
print(list_of_numbers_copy)

