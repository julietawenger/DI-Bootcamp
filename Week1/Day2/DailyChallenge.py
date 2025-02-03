""" 
Challenge 1

    Ask the user for a number and a length.
    Create a program that prints a list of multiples of the number until the list length reaches length.

Examples

number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]
"""

print("Challenge 1\n")

number = int(input('Number: '))
length = int(input('Length: '))

multiples_list = []
counter = 1
while len(multiples_list) < length:
    multiple = number*counter
    multiples_list.append(multiple)
    counter +=1
print(multiples_list)    

""" 
Challenge 2

    Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

Examples

user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
"""

print("\nChallenge 2\n")

string = input("Write a string: ")
string2 = ''
for index in range(len(string)-1):
    if string[index] != string[index+1]:  # if a letter is different than the next.
        string2 += string[index]          # add it to the new string.

string2 += string[-1]                     # last letter is never compared to the next so it needs to be added manually.

print(string2)