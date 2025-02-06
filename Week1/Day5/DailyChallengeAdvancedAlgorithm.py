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

target_number   = 3728
list_of_numbers = [num for num in list_of_numbers if num<=target_number ]
list_of_numbers_copy = [num for num in list_of_numbers if num<=target_number ]

print(len(list_of_numbers))
LEN_LIST = len(list_of_numbers)
stored_pairs = []
i = 0
j = 0
while i <= len(list_of_numbers):
    while j <= len(list_of_numbers):
        if list_of_numbers[i] + list_of_numbers[j] == target_number:
            stored_pairs.append((i,j))
            list_of_numbers.pop(i)
            list_of_numbers.pop(j)
            print(list_of_numbers[i])
            print(list_of_numbers[j])
        j+=1
    i+=1                
print(stored_pairs)

""" 
stored_pairs=[]
for i in list_of_numbers:
    for j in list_of_numbers:
        if i + j == target_number:
            stored_pairs.append((i,j))
            list_of_numbers_copy.remove(i)
            list_of_numbers_copy.remove(j)
print(stored_pairs) """