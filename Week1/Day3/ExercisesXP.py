""" 
Exercise 1 : Convert lists into dictionaries
Instructions

    Convert the two following lists, into dictionaries.
    Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""

print("\nExercise 1\n")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys,values)))


""" 
Exercise 2 : Cinemax #2
Instructions

    A movie theater charges different ticket prices depending on a person’s age.
        if a person is under the age of 3, the ticket is free.
        if they are between 3 and 12, the ticket is $10.
        if they are over the age of 12, the ticket is $15.

    Given the following object:

    family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


    How much does each family member have to pay ?
    Print out the family’s total cost for the movies.
    Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
"""
print("\nExercise 2\n")

#names_keys = input("Enter family members here: ").split()
#ages_keys = input("Enter family members ages here: ").split()
#ages_keys = [int(x) for x in ages_keys]
#family = dict(zip(names_keys, ages_keys))

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = 0
for f in family:
    if 3 <= family[f] <= 12:
        price += 10
        print(f"{f} needs to pay 10 nis.")    
    elif family[f] > 12:
        price += 15
        print(f"{f} needs to pay 15 nis.")
    else:
        print(f"{f} doesn't need to pay.")
print(f"Total price: {price} nis.")

""" 
Exercise 3: Zara
Instructions

    Here is some information about a brand.

    name: Zara 
    creation_date: 1975 
    creator_name: Amancio Ortega Gaona 
    type_of_clothes: men, women, children, home 
    international_competitors: Gap, H&M, Benetton 
    number_stores: 7000 
    major_color: 
        France: blue, 
        Spain: red, 
        US: pink, green

    2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
    The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
    3. Change the number of stores to 2.
    4. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.
    5. Add a key called country_creation with a value of Spain.
    6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
    7. Delete the information about the date of creation.
    8. Print the last international competitor.
    9. Print the major clothes colors in the US.
    10. Print the amount of key value pairs (ie. length of the dictionary).
    11. Print the keys of the dictionary.
    12. Create another dictionary called more_on_zara with the following details:

    creation_date: 1975 
    number_stores: 10 000

    13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
    14. Print the value of the key number_stores. What just happened ?
"""
print("\nExercise 3\n")
# 2
brand = {"name": "Zara", "creation_date": 1975, "creator_name": "Amancio Ortega Gaona", "type_of_clothes": ["men", "women", "children", "home"], "international_competitors": ["Gap", "H&M", "Benetton"], "number_stores": 7000,"major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}}
print(brand)
# 3
brand["number_stores"] = 2
# 4
print("Zara has stores for " + ', '.join(brand["type_of_clothes"][:-1]) + f" and also Zara {brand["type_of_clothes"][-1]}.")
# 5
brand["country_creation"]: "Spain"
# 6
print(brand["international_competitors"])
brand["international_competitors"].append("Desigual")
print(brand["international_competitors"])
# 7
del brand["creation_date"]
# 8 
print(brand["international_competitors"][-1])
# 9 
print("US major colors are " + " and ".join(brand['major_color']["US"])+ ".") 
# 10
print(len(brand))
# 11
print(brand.keys())
# 12
more_on_zara={"creation_date": 1975, "number_stores": 10000}
# 13
for data in more_on_zara:
    brand[data] = more_on_zara[data]
# 14
print(brand["number_stores"])
print("number_stores got updated on the last step.")

""" 
Exercise 4 : Disney characters
Instructions

Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

Analyse these results :

#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


    Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
    Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
    Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
    Only recreate the 1st result for:
        The characters, which names contain the letter “i”.
        The characters, which names start with the letter “m” or “p”.
"""
print("\nExercise 4\n")

print("1\n")

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
print(dict(zip(users, [i for i in range(len(users))])))

print("\n2\n")

print(dict(zip([i for i in range(len(users))],users)))

print("\n3\n")

print(dict(zip(sorted(users), [i for i in range(len(users))])))

print("\n4.1\n")

users_i = [x for x in users if 'i' in x]
print(dict(zip(users_i, [i for i in range(len(users_i))])))

print("\n4.2\n")

users_mp = [x for x in users if (x.lower()).startswith('m') or (x.lower()).startswith('p')]

print(dict(zip(users_mp, [i for i in range(len(users_mp))])))

