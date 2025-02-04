""" A perfect number is a positive integer that is equal to the sum of its divisors.
However, the number itself is not included in the sum.

    Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
    Hint: Google perfect numbers

Example

Input -- Enter the number:6
Output -- True

Input -- Enter the number:10
Output --  False
 """
x = int(input('Enter a number: ')) 

# A formula for finding perfect numbers is 2^{p-1}(2^{p}-1)

def perfect_number(number):
    perfect_numbers_list = [ (2**(p-1)) * (2**p - 1) for p in range(30)]
    if number in perfect_numbers_list:
        return print(True)
    else:
        return print(False)
    
perfect_number(x)    