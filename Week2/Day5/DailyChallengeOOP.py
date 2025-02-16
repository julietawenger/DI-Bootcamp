""" Part 1 : Quizz :

Answer the following questions

    1. What is a class?
    2. What is an instance?
    3. What is encapsulation?
    4. What is abstraction?
    5. What is inheritance?
    6. What is multiple inheritance?
    7. What is polymorphism?
    8. What is method resolution order or MRO?
"""
"""
Classes in Python are blueprints for creating objects. They define the attributes (data) and methods (functions) 
that objects of the class will have. Objects are instances of classes. 
An instance is a realization of that blueprint.
When you create an instance of a class, you are essentially creating a unique copy of the class with its own set of attributes and methods. 
This allows for the creation of multiple independent objects with similar characteristics.
Encapsulation is the practice of obscuring data or implementation details within a class so that its internal operations remain hidden.
Abstraction is a process of hiding unnecessary details and showing only the essential information to the user.
Inheritance is the process by which one class takes on the attributes and methods of another.
Moreover, a class can inherit not only from one class, but from different classes. This is multiple inheritance.
In programming, polymorphism means different or related classes that use the same names for their functions.
Polymorphism allows the ability to use a standard interface for multiple forms or data types.
Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. 
Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes.
"""





""" 
Part 2: Create a deck of cards class.

The Deck of cards class should NOT inherit from a Card class.

The requirements are as follows:

    The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
    The Deck class :
        should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
        should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

 """
import random
class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

class DeckOfCards:    
    # This doesn't look particularly optimized

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A",2,3,4,5,6,7,8,9,10,"J","Q", "K"]  
    def __init__(self):
        self.deck = [Card(v,s) for s in self.suits for v in self.values]    
    def __call__(self):
        return [((self.deck[i]).value, (self.deck[i]).suit) for i in range(len(self.deck))]
       
    def shuffle(self):
        random.shuffle(self.deck)
        return [((self.deck[i]).value, (self.deck[i]).suit) for i in range(len(self.deck))]
        
    def __len__(self):
        return len(self.deck)
    
    def deal(self):
        self.deck =  [((self.deck[i]).value, (self.deck[i]).suit) for i in range(len(self.deck))]
        random_card = random.choice(self.deck) 
        self.deck.remove(random_card)
        print(f"Card dealt: {random_card[0]} of {random_card[1]}")
        return self.deck


deck = DeckOfCards()

print(deck.shuffle())

deck.deal()