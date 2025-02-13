
import random
class Game:
    def __init__(self):
        self.results = {"win": 0, "loss": 0, "draw" : 0}

    def get_user_item(self):
        """User chooses one item"""
        while 1:
            item = input("Select (r)ock, (p)aper, (s)cissor: ")
            if item == 's' or item == 'p' or item == 'r' or item.lower() == 'rock' or item.lower() == 'paper' or item.lower() == 'scissor' or item.lower() == 'scissors':
                break
        if item.lower() == 'rock':
            item = 'r'
        if item.lower() == 'paper':
            item = 'p'
        if item.lower() == 'scissor' or item.lower() == 'scissors':
            item = 's'        
        return item
    def get_computer_item(self):
        """Computer chooses one item"""
        return random.choice(['r', 'p', 's'])
    
    def get_game_result(self, user_item, computer_item):
        """Each round has 3 games. This is one individual game."""
        outcomes = ['draw', 'loss', 'win']
        items = ['r', 'p', 's']
        
        for x in items:
            counter= 0
            for y in items:
                if user_item == x and computer_item == y: 
                    outcome = outcomes[counter]
                counter += 1
            outcomes = outcomes[-1:] + outcomes[:-1]
        return outcome
    
    def play_round(self):
        """This is one round of three games."""
        iterations = 1
        score = 0
        while iterations <=3:
            
            user_item = self.get_user_item()
            computer_item = self.get_computer_item()
            outcome = self.get_game_result(user_item, computer_item)

            print(f"\nYou selected {user_item.upper()}. The computer selected {computer_item.upper()}.")
            print(outcome.upper() + "\n")
            
            if outcome == 'draw':
                score += 0
            if outcome == 'win':
                score += 1
            if outcome == 'loss':
                score += -1  
            iterations +=1

        if score > 0:
            self.results['win'] += 1
            print("This round is yours!")
        if score < 0:
            self.results['loss'] += 1
            print("Computer won!")
        if score == 0:
            self.results['draw'] += 1         
            print("It's a tie!")

        return self.results    
