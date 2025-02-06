""" Exercise 1 : What are you learning ?
Instructions

    Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
    Call the function, and make sure the message displays correctly. """

print("\nExercise 1\n")

def display_message():
    print('In this course I will learn about machine learning and GenAI')
display_message()

""" Exercise 2: What’s your favorite book ?
Instructions

    Write a function called favorite_book() that accepts one parameter called title.
    The function should print a message, such as "One of my favorite books is <title>".
    For example: “One of my favorite books is Alice in Wonderland”
    Call the function, make sure to include a book title as an argument when calling the function.
 """
print("\nExercise 2\n")

def favorite_book(title):
    print(f'One of my favorite books is {title}.')
favorite_book("The Lord of the Rings")

""" Exercise 3 : Some Geography
Instructions

    Write a function called describe_city() that accepts the name of a city and its country as parameters.
    The function should print a simple sentence, such as "<city> is in <country>".
    For example “Reykjavik is in Iceland”
    Give the country parameter a default value.
    Call your function. """

print("\nExercise 3\n")

def describe_city(city = 'Rosario',country='Argentina'):
    print(f"{city} is in {country}.")

describe_city()

print("\nExercise 4\n")

""" Exercise 4 : Random
Instructions

    Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
    Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers."""

import random
def random_game():
    number = int(input("Enter number between 1 and 100: "))
    random_integer = random.randint(1,100)
    if number == random_integer:
        print('Success!')
    else:
        print(f'Your number was {number} and the random number was {random_integer}.')

random_game()            

""" Exercise 5 : Let’s create some personalized shirts !
Instructions

    Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
    The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
    Call the function make_shirt().

    Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
    Call the function, in order to make a large shirt with the default message
    Make medium shirt with the default message
    Make a shirt of any size with a different message.

    Bonus: Call the function make_shirt() using keyword arguments. """

print("\nExercise 5\n")

def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the text is {message}.")
make_shirt('XL', 'Messi')

def make_shirt(size = "L", message = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {message}.")
make_shirt()
make_shirt('M')
make_shirt('M', "I love MESSI")


""" Exercise 6 : Magicians …
Instructions

Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

    Create a function called show_magicians(), which prints the name of each magician in the list.
    Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
    Call the function make_great().
    Call the function show_magicians() to see that the list has actually been modified. """

print("\nExercise 6\n")

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    print(f"The magicians are {', '.join(magician_names[:-1])} and {magician_names[-1]}.")
show_magicians()

def make_great(someone):
    return [s + ' the Great' for s in someone]
magician_names = make_great(magician_names)

show_magicians() 

""" Exercise 7 : Temperature Advice
Instructions

    1.Create a function called get_random_temp().
        This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
        Test your function to make sure it generates expected results.

    2.Create a function called main().
        Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
        Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

    3.Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
        below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
        between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
        between 16 and 23
        between 24 and 32
        between 32 and 40 

    4.Change the get_random_temp() function:

        Add a parameter to the function, named ‘season’.
        Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
        Now that we’ve changed get_random_temp(), let’s change the main() function:
            Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
            Use the season as an argument when calling get_random_temp().

    5.Bonus: Give the temperature as a floating-point number instead of an integer.
    6.Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.        """

print("\nExercise 7\n")

print("7.1\n")
def get_random_temp():
    return random.randint(-10,40)
print(get_random_temp())

print("\n7.2\n")
def main():
    temp = get_random_temp()
    print(f"Hello dear user, the temperature right now is {temp}ºC.")
main()


print("\n7.3\n")
def main():
    temp = get_random_temp()
    print(f"Hello dear user, the temperature right now is {temp}ºC.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0<=temp<16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16<=temp<23:
        print("Nice weather outside.")    
    elif 24<=temp<32:
        print("You won't need any extra layers today.")
    elif 32<=temp<40:
        print("Super hot outside, get inside the swimming pool or stay inside with AC.")
main()           
    

print("\n7.4\n")
def get_random_temp(season):
    if season.lower() == 'winter':
        return random.randint(-10,16)
    elif season.lower() == 'spring':
        return random.randint(18,27)
    elif season.lower() == "autumn" or season.lower() == "fall":
        return random.randint(16,23)
    elif season.lower() == "summer":
        return random.randint(26,40)
def main():
    season =  input("Enter current season: ")    
    temp = get_random_temp(season)
    print(f"Hello dear user, the temperature right now is {temp}ºC.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0<=temp<16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16<=temp<23:
        print("Nice weather outside.")    
    elif 24<=temp<32:
        print("You won't need any extra layers today.")
    elif 32<=temp<40:
        print("Super hot outside, get inside the swimming pool or stay inside with AC.")
main()               


print("\n7.5/7.6\n")
def get_random_temp(month):
    if month <= 2 or month ==12:
        return round(random.uniform(-10,16),1)
    elif 3<= month <= 5:
        return round(random.uniform(18,27),1)
    elif 9<= month <= 11:
        return rount(random.uniform(16,23),1)
    elif 6<= month <= 8:
        return round(random.uniform(26,40),1)             

def main():
    season =  int(input("Enter current month (format MM): "))    
    temp = get_random_temp(season)
    print(f"Hello dear user, the temperature right now is {temp}ºC.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0<=temp<16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16<=temp<23:
        print("Nice weather outside.")    
    elif 24<=temp<32:
        print("You won't need any extra layers today.")
    elif 32<=temp<40:
        print("Super hot outside, get inside the swimming pool or stay inside with AC.")
main()               

""" Exercise 8 : Star Wars Quiz
Instructions

This project allows users to take a quiz to test their Star Wars knowledge.
The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

    1.Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
    2.Create a function that informs the user of his number of correct/incorrect answers.
    3.Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
    If he had more than 3 wrong answers, ask him to play again.
 """
print("\nExercise 8\n")

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def star_wars_quiz():
    right_answers = []
    wrong_answers = []
    for index in range(len(data)):
        print(data[index]['question'])
        user_answer = input("Answer here: ").title()        
        if user_answer == data[index]['answer']:
            print('Correct!')
            right_answers.append(index)
        else:
            print(f'Incorrect. Answer was: {data[index]['answer']}.')  
            wrong_answers.append(index)   
    print(f"You answered {len(right_answers)} correctly and {len(wrong_answers)} incorrectly.")
    if len(wrong_answers)>3:
        print('Play again!')
star_wars_quiz()
