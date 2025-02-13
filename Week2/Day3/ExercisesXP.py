""" Exercise 1: Currencies
Instructions

    Using the code above, implement the relevant methods and dunder methods which will output the results below.
    Hint : When adding 2 currencies which don’t share the same label you should raise an error. """
""" 
>>> c1 = Currency('dollar', 5)
>>> c2 = Currency('dollar', 10)
>>> c3 = Currency('shekel', 1)
>>> c4 = Currency('shekel', 10)

>>> str(c1)
'5 dollars'

>>> int(c1)
5

>>> repr(c1)
'5 dollars'

>>> c1 + 5
10

>>> c1 + c2
15

>>> c1 
5 dollars

>>> c1 += 5
>>> c1
10 dollars

>>> c1 += c2
>>> c1
20 dollars

>>> c1 + c3
TypeError: Cannot add between Currency type <dollar> and <shekel> """

print(f"\nExercise 1\n")
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE
    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}" 
        else:
            return f"{self.amount} {self.currency}s" 
    def __int__(self):
        return int(self.amount)    
    def __repr__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}" 
        else:
            return f"{self.amount} {self.currency}s" 
        
    def __call__(self):
        return self.amount
    
    def __add__(self, other):
        if type(other) == int:
            return Currency(self.currency, self.amount + other)

        elif isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
    
    def __iadd__(self, other):
        if type(other) == int:
           self.amount+=other
           return Currency(self.currency, self.amount)
        
        elif isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return Currency(self.currency, self.amount)
            
  
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1+5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
#print(c1 + c3) # TypeError: Cannot add between Currency type <dollar> and <shekel>

""" Import
Instructions

    In a file named func.py create a function that sum 2 numbers, and prints the result
    In a file named exercise_one.py import the function and call it to print the result

Hint: You can use the the following syntaxes:

import module_name 

OR 

from module_name import function_name 

OR 

from module_name import function_name as fn 

OR

import module_name as mn
 """


print(f"\nExercise 2\n")

#import func as fn
#print(fn.add(1,2)) # 3

""" 
Exercise 3: String module
Instructions

    Generate random String of length 5
    Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
    Hint: use the string module
 """

print(f"\nExercise 3\n")
import string
import random

print(''.join([string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)] for _ in range(6)]))


""" Exercise 4 : Current Date
Instructions

    Create a function that displays the current date.
    Hint : Use the datetime module.
 """
print(f"\nExercise 4\n")

import datetime

def date_today():
    today = datetime.date.today()
    print("Today's date is: ", today)
date_today()

""" Exercise 5 : Amount of time left until January 1st
Instructions

    Create a function that displays the amount of time left from now until January 1st.
    (Example: the 1st of January is in 10 days and 10:34:01hours).
"""
print(f"\nExercise 5\n")

def time_until(d,m,y):
    now = datetime.datetime.now()
    next_date = datetime.datetime(year=y, month=m, day=d)
    time_left = next_date - now
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time left until {d}/{m}/{y} is {days} days, {hours} hours, {minutes} minutes and {seconds} seconds")

time_until(28,2,2025)

""" Exercise 6 : Birthday and minutes
Instructions

    Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
"""
def time_alive(d,m,y, hour = 0, minute = 0):
    if hour<10:
        hour = f"0{hour}"
    if minute<10:
        minute =f"0{minute}"    
    time_al = datetime.datetime.now()-datetime.datetime.fromisoformat(f'{y}-{m}-{d} {hour}:{minute}:00.000')
    days = time_al.days
    hours, remainder = divmod(time_al.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time alive from {d}/{m}/{y} is {days} days, {hours} hours, and {minutes} minutes")
    print(f"In minutes, that is {days*1440 + hours*60 + minutes} minutes.")

time_alive(28,11,1996,7,30)

""" Exercise 7 : Faker Module
Instructions

    Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
    Create an empty list called users. Tip: It should be a list of dictionaries.
    Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.
"""
from faker import Faker
    
  
fake = Faker()  
 
def input_data(x):  
    # dictionary  
    user =[] 
    for i in range(0, x):  
        user.append({})  
        user[i]['name']= fake.name()  
        user[i]['address']= fake.address()  
        user[i]['language_code']= str(fake.language_code)   
    print(user)  
input_data(5)