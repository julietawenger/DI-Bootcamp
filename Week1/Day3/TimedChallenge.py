""" 
Write a program to reverse the sentence wordwise.

Input:
You have entered a wrong domain
Output:
domain wrong a entered have You
"""

phrase = input("Enter a sentence: ")
print(' '.join(phrase.split()[::-1]))