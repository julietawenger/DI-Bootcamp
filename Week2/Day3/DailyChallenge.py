""" Instructions :

The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

    Compute the circle’s area
    Print the attributes of the circle - use a dunder method
    Be able to add two circles together, and return a new circle with the new radius - use a dunder method
    Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
    Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
    Be able to put them in a list and sort them
    Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles
"""
import numpy as np
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2*radius
        self.area = np.round(np.pi* radius**2,2)
    def __str__(self):    
        print(f"Radius: {self.radius}, diameter: {self.diameter}, area: {self.area}")
    def __call__(self):
        return self.radius
    
    def __add__(self, other):
        return  Circle(self.radius + other.radius)()  
        
    
    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.radius > other.radius:
            return True
        else:
            return False    
    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False    
        
c1 = Circle(2)
c2 = Circle(4)
c3 = Circle(5)

print(c1())
print(c1 + c2)
print(c1>c2)
print(c2>c1)
print(c3<c2)
print(sorted([c3(),c2(),c1()]))