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