""" Exercise 1  Random Sentence Generator
Instructions

Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

Hint : The generated sentences do not have to make sense.

    1. Download this word list

    2. Save it in your development directory.

    3. Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

    4. Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
        use the words list to get your random words.
        the amount of words should be the value of the length parameter.

    5. Take the random words and create a sentence (using a python method), the sentence should be lower case.

    6. Create a function called main which will:
        Print a message explaining what the program does.

        Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
            If the user inputs incorrect data, print an error message and end the program.
            If the user inputs correct data, run your code.
 """

print("\nExercise 1\n")
import random
def get_words_from_file(file):
    f = open(file)
    return (f.read()).split()

file = r"sowpods.txt"
word_list = get_words_from_file(file)


def get_random_sentence(length):
    sentence = '' 
    for x in range(length):
        sentence +=random.choice(word_list).lower() + ' '
    return sentence 


def main():
    print("This program prints a random sentence of a requested length (between 2 and 20).")
    try:
        length = int(input("Enter sentence length: "))
        if length>20 or length<2:
            print("Error: Enter integer between 2 and 20.")
            exit()
    except ValueError:
            print("Error: Enter integer between 2 and 20.")
            exit()
    print(get_random_sentence(length))

main()        

print("\nExercise 2\n")

""" 
Exercise 2: Working with JSON
Instructions
    1.Access the nested “salary” key from the JSON-string below.
    2.Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
    3.Save the dictionary as JSON to a file.
"""
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data =  json.loads(sampleJson)
print(f"1. Salary: {data["company"]["employee"]["payable"]["salary"]}")

data["company"]["employee"]["birth_date"] = "28/11/1996" 
print(f"2. {data}")

json_file = "sampleJson.json"

with open(json_file, 'w') as file_obj:
    json.dump(data, file_obj, indent = 2, sort_keys=True)