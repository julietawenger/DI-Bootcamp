"""  Exercise 1 : Pets
Instructions

Using this code:

    1. Create another cat breed named Siamese which inherits from the Cat class.
    2. Create a list called all_cats, which holds three cat instances: one Bengal, one Chartreux and one Siamese.
    3. Those three cats are Sara’s pets. 
    Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
    4. Take all the cats for a walk, use the walk method.
 """
print("\nExercise 1\n")

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
      return f'{sounds}'
    

ben  = Bengal("Ben", 8)
charlie = Chartreux("Charlie", 6)
sienna = Siamese("Sienna",2) 
all_cats = [ben, charlie, sienna]
sara_pets = Pets(all_cats)
for pets in sara_pets.animals:
    print(pets.walk())

print("\nExercise 2\n")    

""" Exercise 2 : Dogs
Instructions

    Create a class called Dog with the following attributes name, age, weight.
    Implement the following methods in the Dog class:
        bark: returns a string which states: “<dog_name> is barking”.
        run_speed: returns the dogs running speed (weight/age*10).
        fight : takes a parameter which value is another Dog instance, called other_dog. 
        This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

    Create 3 dogs and run them through your class. """

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return f"Runing speed is: {round(self.weight/self.age*10,1)} km/h"
    
    def fight(self, other_dog):
        dog = self.name
        if self.run_speed()*self.weight< other_dog.run_speed()*other_dog.weight:    
            dog = other_dog.name
        return f"{dog} won the fight."

dog1 = Dog("Rubén Darío", 12, 8)
dog2 = Dog("Muñeco", 9, 10)
dog3 = Dog("Elton", 3, 8)

print(dog2.bark())
print(dog1.run_speed())
print(dog1.fight(dog3))

""" Exercise 3 : Dogs Domesticated
Instructions

    Create a new python file and import your Dog class from the previous exercise.
    In the new python file, create a class named PetDog that inherits from Dog.
    Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
    Add the following methods:
        train: prints the output of bark and switches the trained boolean to True

        play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following 
        string: “dog_names all play together”.

        do_a_trick: If the dog is trained the method should print one of the following sentences at random:
            “dog_name does a barrel roll”.
            “dog_name stands on his back legs”.
            “dog_name shakes your hand”.
            “dog_name plays dead”. """

print("\nExercise 3\n")
import random
class PetDog(Dog):
    def __init__(self, name, trained = False):
        self.trained = False
        self.name = name
        
    def train(self):
        self.trained = True    
    
    def play(self, *args):
        doggos = [self.name] + [i.name for i in args]
        print(f"{', '.join(doggos[:-1])} and {doggos[-1]}, all play together/")
    
    def do_a_trick(self):
        if self.trained == True:
            a = f"{self.name} does a barrel roll."
            b = f"{self.name} stands on his back legs."
            c = f"{self.name} shakes your hand."
            d = f"{self.name} plays dead."
            print([a,b,c,d][random.randint(0,3)])


dog1 = PetDog("Rubén Darío")
dog2 = PetDog("Muñeco")
dog3 = PetDog("Elton")

dog3.train()
dog3.do_a_trick()
dog1.play(dog2,dog3) 
#%%
""" Exercise 4 : Family
Instructions

    1.Create a class called Family and implement the following attributes:
        members: list of dictionaries
        last_name : (string)

    2.Implement the following methods:
        born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
        is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
        family_presentation: a method that prints the family’s last name and all the members’ details.

    3.Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

        [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ] """

print("\nExercise 4\n")

class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
        
    def born(self, **kwargs):
        self.members.append({k: val for k, val in kwargs.items()})    
        print(f"Congratulations on the birth of {kwargs['name']}!") 

    def is_18(self, family_member):
        for members in self.members:
            if members['name'] == family_member and members['age'] >= 18:
                return True
            elif members['name'] == family_member and members['age'] < 18:
                return False
            
    def family_presentation(self):
        print(f"Family's last name is {self.last_name} and their members are:\n")
        for members in self.members:
            sentence = ''
            for k,val in members.items():
                sentence += f"{k.capitalize()}: {val}. "
            print(sentence + "\n")    
         
addams_family = Family( [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
                        ], "Addams")

print(addams_family.is_18("Sarah"))            
addams_family.family_presentation()

addams_family.born(name = 'Emma', age= 0, gender = 'Female', is_child = True)
print(addams_family.is_18("Emma"))            

addams_family.family_presentation()
#%%
""" Exercise 5 : TheIncredibles Family
Instructions

    1.Create a class called TheIncredibles. This class should inherit from the Family class:
    This is no random family they are an incredible family, therefore the members attributes, 
    will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

    2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

    3.Add a method called incredible_presentation which :
        Print a sentence like “*Here is our powerful family **”
        Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)


    4.Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

        [
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
        ]


    Call the incredible_presentation method.

    Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.

    Call the incredible_presentation method again. """

print("\nExercise 5\n")
class TheIncredibles(Family):
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
    def use_powers(self, family_member):
        for m in self.members:
            if m['name'] == family_member and m["age"]>=18:
                print(m['power'])
            elif m["name"] == family_member and m["age"]<18:
                raise Exception('Not yet over 18 years old.')
    def incredible_presentation(self, members):
        print("*Here is our powerful family*")        
        