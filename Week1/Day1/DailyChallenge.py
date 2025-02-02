
import random
""" 
Exercise 1
    Using the input function, ask the user for a string. The string must be 10 characters long.

    If it’s less than 10 characters, print a message which states “string not long enough”.
    If it’s more than 10 characters, print a message which states “string too long”.
    If it’s 10 characters, print a message which states “perfect string” and continue the exercise. 
"""

string = input("Write a string: ")
if len(string) == 10:
    print('Perfect string.')
elif len(string) < 10:
    print('String not long enough')    
else:
    print('String too long.')

""" 
Then, print the first and last characters of the given text.
"""

print(string[0])
print(string[-1])

""" 
Using a for loop, construct the string character by character: 
Print the first character, then the second, then the third, until the full string is printed.
"""
reconstructed_string =''
for ch in string:
    reconstructed_string+= ch
    print(reconstructed_string)

""" 
Bonus: Swap some characters around then print the newly jumbled string 
"""
char_list = list(string) 
random.shuffle(char_list)
print(''.join(char_list))