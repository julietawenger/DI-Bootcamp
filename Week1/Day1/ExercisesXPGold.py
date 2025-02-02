""" Exercise 1
    Print the following output in one line of code:

    Hello world
    Hello world
    Hello world
    Hello world
    I love python
    I love python
    I love python
    I love python 
"""
print('Exercise 1')

print("Hello world\n" * 4)


""" 
Exercise 2 : What is the Season ?

    Ask the user to input a month (1 to 12).
    Display the season of the month received :
        Spring runs from March (3) to May (5)
        Summer runs from June (6) to August (8)
        Autumn runs from September (9) to November (11)
        Winter runs from December (12) to February (2)
 """

month = int(input('What is the month? (In numbers): '))
if 2 < month < 6:
    print("It's spring")
elif 5 < month < 9:
    print("It's summer.")
elif 8 < month < 12:
    print("It's autumn.")        
elif 11 < month or month < 3:
    print("It's winter.")        
