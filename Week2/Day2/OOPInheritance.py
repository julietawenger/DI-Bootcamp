""" OOP Inheritance, Encapsulation, Polymorphism and Multiple Inheritance """

class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barked, WAF !")

dingo = Dog("Dingo")

print(dingo.name)
dingo.bark()

#%%
class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

rex = Dog('dog', 4, "Wouaf")
print('This animal is a:', rex.type)
# >> This animal is a dog

rex.fetch_ball()
# >> I am a dog, and I love fetching balls

roger = Animal('Roger', 4, "Grr")
#roger.fetch_ball() # 'Animal' object has no attribute 'fetch_ball'. (I need to call it a dog)

#%% Exercise
class Circle:
    color = "red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle
print(nc.color)
# >> What will be the output ? blueee
#%%
class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)

nc = NewCircle(1)
print(nc.diameter) # 1

nc.grow()

print(nc.diameter) # 4
# >> What will be the output

#%%

class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

    def make_sound(self):
        print("I am an DOGGG !!! WOUAFFF!!")

rex = Dog('dog', 4, "Wouaf")
rex.make_sound()
# >> I am an DOGGG !!! WOUAFFF!!

#%% super()
class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

class Dog(Animal):
    def __init__(self, type, number_legs, sound, fetch_ball):
        super().__init__(type, number_legs, sound)
        # Or : Animal.__init__(self,type, number_legs, sound)
        self.fetch_ball = fetch_ball

rex = Dog('dog', 4, "wouaf", True)
print('This animal is a:', rex.type)
# >> This animal is a dog

print('This dog has', rex.number_legs , ' legs')
# >> This dog has 4 legs

print('This dog makes the sound ', rex.sound)
# >> This dog makes the sound wouaf

print('Does this dog fetchs balls ? ', rex.fetch_ball)
# >> Does this dog fetchs balls ? True

#%%
""" Try to recreate the class explained below:

We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

We can create a class called BlockedDoor that inherits from the base class Door.

We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those functions, which simply raises an Error that a blocked door cannot be opened or closed.
"""

class Door:
    def __init__(self, is_opened = True):
        self.is_opened = True

    def open_door(self):
        self.is_opened = True
        print(f"Is the door open? {self.is_opened}" )
    def close_door(self):
        self.is_opened = False
        print(f"Is the door open? {self.is_opened}" )

class BlockedDoor(Door):
    def __init__(self):
        super().__init__ (is_opened = False)
    
    def open_door(self):
        self.is_opened = False
        print("I can't open a blocked door")    
        print(f"Is the door open? {self.is_opened}" )

    def close_door(self):
        self.is_opened = False
        print("I can't close a blocked door")    
        print(f"Is the door open? {self.is_opened}" )

door = Door()        
door.close_door()
door.open_door()
door = BlockedDoor()
door.close_door()
door.open_door()