""" Exercise 1: Cats
Instructions

Using this class
"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

""" 
1. Instantiate three Cat objects using the code provided above.
2. Outside of the class, create a function that finds the oldest cat and returns the cat.
3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
"""

cat1 = Cat('Numpy' , 3)
cat2 = Cat("Lizzie", 2) 
def oldest_cat(cat):
    print(cat.age)

oldest_cat(cat1)    