""" 
Exercise 1 : Favorite Numbers
Instructions

    Create a set called my_fav_numbers with all your favorites numbers.
    Add two new numbers to the set.
    Remove the last number.
    Create a set called friend_fav_numbers with your friend’s favorites numbers.
    Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
"""
import numpy as np
print("\n")

print("Exercise 1\n")


my_fav_numbers = set([21, np.pi, np.e, 1])
print(my_fav_numbers)
my_fav_numbers.update([3,5])
print(my_fav_numbers)
my_fav_numbers.remove(max(my_fav_numbers))
print(my_fav_numbers)
friend_fav_numbers = set([np.pi, -1])
our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
print(our_fav_numbers)

print("\n")
""" 
Exercise 2: Tuple
Instructions

    Given a tuple which value is integers, is it possible to add more integers to the tuple?
"""
# No, but I can define it again

print("Exercise 2\n")

original_tuple = (1, 2, 3)
new_integers = (4, 5)
new_tuple = original_tuple + new_integers
print(new_tuple)

print("\n")
""" 
Exercise 3: List
Instructions

    Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

    Remove “Banana” from the list.
    Remove “Blueberries” from the list.
    Add “Kiwi” to the end of the list.
    Add “Apples” to the beginning of the list.
    Count how many apples are in the basket.
    Empty the basket.
    Print(basket)
"""
print("Exercise 3\n")

list_basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(list_basket)
list_basket.pop(0)
print(list_basket)
list_basket.pop(-1)
print(list_basket)
list_basket.insert(0, 'Apples')
print(list_basket)
print(f'There are {list_basket.count("Apples")} apples in the basket.')
list_basket = []
print(list_basket)

print("\n")
""" 
Exercise 4: Floats
Instructions

    Recap – What is a float? What is the difference between an integer and a float?
    Create a list containing the following sequence of floats and integers (it should be a list with mixed types):
    1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
    Can you think of another way to generate a sequence of floats?
"""

print("Exercise 4\n")

print("A float is a rational number so it can be expressed as a fraction mathematically, whereas an integer is literally an integer number.")

mixed_list = sorted([i for i in range(2,6)]+[i+ .5 for i in range(1,5)])

print("Given this list of integers:")
int_list = [i for i in range(6)]
print(int_list)
print("I can create a list of floats using, for example, fractions or float()")
float_list = [i/1 for i in range(6)]
print(float_list)
float_list = [float(i) for i in range(6)]
print(float_list)

print("\n")
""" 
Exercise 5: For Loop
Instructions

    Use a for loop to print all numbers from 1 to 20, inclusive.
    Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
"""
print("Exercise 5\n")

for i in range(1,21):
    print(i)
for i in range(1,21):
    if i%2 == 0:
        print(i)

print("\n")
""" 
Exercise 6 : While Loop
Instructions

Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
"""
print("Exercise 6\n")

name = input("What's your name?: ")
while name != 'Julieta':
    name = input("Incorrect. What's your name again?: ")

print("\n")

""" 
Exercise 7: Favorite fruits
Instructions

    Ask the user to input their favorite fruit(s) (one or several fruits).
    Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
    Store the favorite fruit(s) in a list (convert the string of words into a list of words).
    Now that we have a list of fruits, ask the user to input a name of any fruit.
        If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
        If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

"""
print("Exercise 7\n")

fruits = input("Input your favorite fruit(s). Separate them with a single space, eg. 'apple mango cherry'. ")
fruits_list = fruits.split(" ")
new_fruit = input("Name a fruit: ")
if new_fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!.")
else:
    print("You chose a new fruit. I hope you enjoy.")    
print("\n")

""" 
Exercise 8: Who ordered a pizza ?
Instructions

    Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
    As they enter each topping, print a message saying you’ll add that topping to their pizza.
    Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
"""
print("Exercise 8\n")

topping = input("Input a topping: ")
toppings_list = []
while topping != 'quit':
    toppings_list.append(topping)
    topping = input("Adding topping. \nNew topping? If you're done write 'quit': ")

print(f"Your toppings are: {', '.join(toppings_list)}.") 
print(f"Total price: {10+ 2.5*len(toppings_list)} nis.")
print("\n")

""" 
Exercise 9: Cinemax
Instructions

    A movie theater charges different ticket prices depending on a person’s age.
        if a person is under the age of 3, the ticket is free.
        if they are between 3 and 12, the ticket is $10.
        if they are over the age of 12, the ticket is $15.

    Ask a family the age of each person who wants a ticket.

    Store the total cost of all the family’s tickets and print it out.

    A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
    Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
    At the end, print the final list.
"""
print("Exercise 9")
print("Part 1\n")


ages = input("Input ages of all family members separated by a single space: ")
ages = ages.split(' ')
price = 0
for i in ages:
    if 3 < int(i) < 12:
        price += 10
    elif int(i) >= 12:
        price += 15    
print(f"Total price: {price} nis.")

print("\nPart 2\n")

name_list = input("Input names separated by a single space: ").split(' ')
for name in name_list:
    name_age = int(input(f"{name}: what's your age? "))
    if name_age <= 21:
        name_list.remove(name)
print(f"{', '.join(name_list)} are permitted to watch the movie.")        

print("\n")
""" 
Exercise 10 : Sandwich Orders
Instructions

Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

    The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
    We need to prepare the orders of the clients:
        Create an empty list called finished_sandwiches.
        One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
    After all the sandwiches have been made, print a message listing each sandwich that was made, such as:

I made your tuna sandwich
I made your avocado sandwich
I made your egg sandwich
I made your chicken sandwich
"""
print('Exercise 10\n')

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")