""" Excercise
Given this list 
l = [5,10,15,20,25,50,20]
1. Print index 3
2. Change 50 to 70 
3. Delete number 20 (first apperance)
4. Add a new number to the end of the list
"""


l = [5,10,15,20,25,50,20]
print(l)
print(l[3])
l[5] =70
print(l)
l.pop(3)
print(l)
l.append(3)
print(l)