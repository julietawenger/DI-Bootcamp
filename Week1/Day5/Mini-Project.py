""" Tic Tac Toe
Instructions

    The game is played on a grid that’s 3 squares by 3 squares.
    Players take turns putting their marks (O or X) in empty squares.
    The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
    When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie. """


def display_board():

    board = ''
    
    for i in range(5):
        if i%2 == 1:
            board += '-----------\n'
        else:        
            for j in range(5):
                if j%2 ==1:
                    board +=  '|'
                else:
                    board += ' '*3    
            board += '\n'        
    return(board)
          
board = display_board()          

def new_board(text,index,replacement):
    return f"{text[:index]}{replacement}{text[index+1:]}"

def rowcolumn_index(row,column):
    indexes = [1, 5, 9, 25, 29, 33, 49, 53, 57]    
    counter = 0
    for i in range(1,4):
        for j in range(1,4):
            if row == i and column == j:
                return indexes[counter]
            counter+=1

    


  

