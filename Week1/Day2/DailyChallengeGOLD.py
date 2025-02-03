""" Instructions

    Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
    Display a little cake as seen below:

       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

Bonus : If they were born on a leap year, display two cakes ! """
import math
birthday = input("Birthday (DD/MM/YYYY): ")
day = int(birthday[:2])
month = int(birthday[3:5])
if day <= 3 and month<3:
    age = 2025 - int( birthday[-4:])
else:
    age = 2024 - int( birthday[-4:])     
print(age)

candles = int(str(age)[-1])

if candles%2==1:
    print("   "+ "_"*math.floor((11-candles)/2)+ "i"*candles + "_"*math.floor((11-candles)/2))
    print("  |:H:a:p:p:y:|")
    print("__|___________|__")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")
if candles%2==0:
    print("   "+ "_"*int((11-candles)/2)+ "i"*candles + "_"*int((11-candles)/2)+ "_")
    print("  |:H:a:p:p:y:|")
    print("__|___________|__")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")
        