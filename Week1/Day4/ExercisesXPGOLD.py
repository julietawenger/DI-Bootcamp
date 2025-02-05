""" Exercise 2 : Sum
Instructions

    Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.

Example:
If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

Hint: treating our number as a int or a str at different points in our code may be helpful """

def sum_exercise(x):
    return x + int(str(x)*2) + int(str(x)*3) + int(str(x)*4)
print(sum_exercise(3))
