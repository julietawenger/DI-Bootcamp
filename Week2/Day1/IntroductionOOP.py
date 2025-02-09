"""OOD: object oriented programmig. Day 1"""

class Dog():
    def __init__(self, color, breed, floppy_ears, name):
        self.color = color              # It doesn't belong to Dog, it belongs to peanut, the Dog
        self.breed = breed
        self.floppy_ears = floppy_ears
        self.name = name
        print("A new dog has been initialized.")

    def __str__(self):
        return f"{self.color, self.breed, self.floppy_ears, self.name}"

    def bark(self):
        return f"{self.name} goes WOOF!"
    
    def walk(self, number_of_meters):
        return f"{self.name} walked {number_of_meters} meters."
    
    def sit(self): 
        print(f"{self.name} sits down.")   

peanut = Dog("brown", "beagle", True, "Peanut")
dingo = Dog("white", "cnaani", False, "Dingo")
print(peanut.breed)
print(dingo)
print(dingo.bark())
print(peanut.sit())

#%%
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

## create an instance for the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)
#%%

