""" 
Exercise 1: Cats
Instructions

Using this class
"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age  = cat_age


"""        
1. Instantiate three Cat objects using the code provided above.
2. Outside of the class, create a function that finds the oldest cat and returns the cat.
3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
"""
print("\nExercise 1\n")

cats = [Cat("Numpy", 3), Cat("Lizzie", 2), Cat("Frank", 5)]

print("\n2./3.\n")

def oldest_cat(cats):
    cats_list = [(cat.name, cat.age) for cat in cats]
    oldest = max(cats_list, key = lambda x: x[1])
    return oldest[0], oldest[1]

print(f"The oldest cat is {oldest_cat(cats)[0]}, and is {oldest_cat(cats)[1]} years old.")

""" 
Exercise 2 : Dogs
Instructions

    1.Create a class called Dog.
    2.In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
    3.Create a method called bark that prints the following string “<dog_name> goes woof!”.
    4.Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    5.Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
    6.Print the details of his dog (ie. name and height) and call the methods bark and jump.
    7.Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
    8.Print the details of her dog (ie. name and height) and call the methods bark and jump.
    9.Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog. 
"""

print("\nExercise 2\n")
class Dog:
    def __init__(self, name, height):
        self.name   = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes WOOF!")    
    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high.")       

davids_dog = Dog('Rex', 50 )
print(f"David's dog is called {davids_dog.name}, he is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog is called {sarahs_dog.name}, he is {sarahs_dog.height} cm tall.")  
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print("Sarah's dog is taller.")
else:
    print("David's dog is taller.")    



""" 
Exercise 3 : Who’s the song producer?
Instructions

    Define a class called Song, it will show the lyrics of a song.
    Its __init__() method should have two arguments: self and lyrics (a list).
    Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

    Create an object, for example:

    stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

    Then, call the sing_me_a_song method. The output should be:

    There’s a lady who's sure
    all that glitters is gold
    and she’s buying a stairway to heaven

"""
print("\nExercise 3\n")
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()                

""" 
Exercise 4 : Afternoon at the Zoo
Instructions

    Create a class called Zoo.
    In this class create a method __init__ that takes one parameter: zoo_name.
    It instantiates two attributes: animals (an empty list) and name (name of the zoo).
    Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
    Create a method called get_animals that prints all the animals of the zoo.
    Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

    Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
    Example

    { 
        A: "Ape",
        B: ["Baboon", "Bear"],
        C: ['Cat', 'Cougar'],
        E: ['Eel', 'Emu']
    }


    Create a method called get_groups that prints the animal/animals inside each group.
    Create an object called ramat_gan_safari and call all the methods.
    Tip: The zookeeper is the one who will use this class.
    Example

    Which animal should we add to the zoo --> Giraffe
    x.add_animal(Giraffe) 
"""

print("\nExercise 4\n")

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal): 
        if new_animal not in self.animals:   
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()  
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        return grouped_animals
    
    def get_groups(self):
        for groups in sort_animals():
            print (sort_animals()[groups])


temaiken = Zoo("Temaiken")
temaiken.add_animal("zebra")
temaiken.add_animal("owl")
temaiken.add_animal("giraffe")
temaiken.add_animal("cat")
temaiken.add_animal("cougar")
temaiken.get_animals()
temaiken.sell_animal("zebra")
temaiken.get_animals()
print(temaiken.sort_animals())
for groups in temaiken.sort_animals():
    print (temaiken.sort_animals()[groups])

