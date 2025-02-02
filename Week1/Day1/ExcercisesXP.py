

""" 
Exercise 1 : Hello World 
    Print the following output in one line of code:

    Hello world
    Hello world
    Hello world
    Hello world
"""

print('Exercise 1')

print("Hello world\n" * 4)


""" 
Exercise 2 : Some Math
    Write code that calculates the result of: (99^3)*8. 
"""

print('Exercise 2')

print('(99^3)*8 = ' + str((99**3)*8))


""" 
Excercise 3: predict the outcomes

   5 < 3               ## False
   3 == 3              ## True
   3 == "3"            ## False
   "3" > 3             ## Error
   "Hello" == "hello"  ## False 
"""
print("Exercise 3")
print(5 < 3)
print(3 == 3)
print(3 == "3")
#print("3" > 3)
print('Hello' == 'Hello')

""" 
Exercise 4 : Your computer brand
     Create a variable called computer_brand which value is the brand name of your computer.
     Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer". """

print('Exercise 4')
computer_brand = 'Lenovo YOGA'
print(f'I have a {computer_brand} computer')  

"""  
Exercise 5 : Your information
     Create a variable called name, and set it’s value to your name.
     Create a variable called age, and set it’s value to your age.
     Create a variable called shoe_size, and set it’s value to your shoe size.
     Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
     Have your code print the info message.
     Run your code """

print('Exercise 5')
name = 'Julieta'
age = 28
shoe_size = 37
info = f'Hi everyone, my name is {name}, I am {age} years old and in case you wish to gift me a pair of shoes, my shoe size is {shoe_size}'
print(info)

""" 
Exercise 6 : A & B
     Create two variables, a and b.
     Each variable value should be a number.
     If a is bigger then b, have your code print Hello World.
"""

print('Exercise 6')
a = 15
b = 10
if a > b:
    print('Hello world')

""" 
Exercise 7 : Odd or Even
    Write code that asks the user for a number and determines whether this number is odd or even.
"""

print('Exercise 7')

number = int(input('Write a number: '))
if number% 2 == 0:
    print('Number is even')
else:
    print('Number is odd')    

""" 
Exercise 8 : What’s your name ?
    Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.    
"""

print('Exercise 8')
username = input("What's your name?: ")
if username == 'Julieta':
    print("Mazal tov, you're one of us! Great name.")
else:
    print("Not a great name tbh.")

"""  
Exercise 9 : Tall enough to ride a roller coaster
    Write code that will ask the user for their height in centimeters.
    If they are over 145cm print a message that states they are tall enough to ride.
    If they are not tall enough print a message that says they need to grow some more to ride.
"""

user_height = int(input("What's your height (in cm)?: "))
if user_height > 145:
    print("You're tall enough to ride a roller coaster.")
else:
    print("You need to grow some more to ride the roller coaster")     