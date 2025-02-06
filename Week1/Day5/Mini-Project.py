""" Tic Tac Toe
Instructions

    The game is played on a grid that’s 3 squares by 3 squares.
    Players take turns putting their marks (O or X) in empty squares.
    The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
    When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie. """


def display_board():
    """This function returns new, empty board"""
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
                  

def new_board(board,index,replacement):
    """Given the old board, the index of the box the user wants to update and the replacement (ie 'X' or 'O'), function returns a new board."""
    if board[index] != ' ':
        print('Try again!')
        return False
    else: 
        return f"{board[:index]}{replacement}{board[index+1:]}"

def rowcolumn_to_index(row,column):
    """User writes row and column and the function returns the index corresponding 
    to the box to be updated."""

    indexes = [1, 5, 9, 25, 29, 33, 49, 53, 57]    
    counter = 0
    for i in range(1,4):
        for j in range(1,4):
            if row == i and column == j:
                return indexes[counter]
            counter+=1

def turn(board, player):
    """One turn in the game. Returns a new board based on the input of the player."""
    row = int(input('Enter row: '))
    column = int(input('Enter column: '))
    board_2 = new_board(board, rowcolumn_to_index(row,column), player) 
    while board_2 == False:
        row = int(input('Enter row: '))
        column = int(input('Enter column: '))    
        board_2 = new_board(board, rowcolumn_to_index(row,column), player) 
      
    print('\n' + board_2)
    return board_2

def check_win(board):
    """This is ugly asf but it checks if someone won or not."""
    i = 1
    if board[rowcolumn_to_index(i   ,i  )] == board[rowcolumn_to_index(i  , i+1)]  == board[rowcolumn_to_index(i,i+2)  ] != ' ':
                return True
    if board[rowcolumn_to_index(i+1 ,i  )] == board[rowcolumn_to_index(i+1, i+1)]  == board[rowcolumn_to_index(i+1,i+2)] != ' ':
                return True    
    if board[rowcolumn_to_index(i+2 ,i  )] == board[rowcolumn_to_index(i+2, i+1)]  == board[rowcolumn_to_index(i+2,i+2)] != ' ':
                return True   
    if board[rowcolumn_to_index(i   ,i  )] == board[rowcolumn_to_index(i+1, i  )]  == board[rowcolumn_to_index(i+2,i  )] != ' ':
                return True           
    if board[rowcolumn_to_index(i   ,i+1)] == board[rowcolumn_to_index(i+1, i+1)]  == board[rowcolumn_to_index(i+2,i+1)] != ' ':
                return True           
    if board[rowcolumn_to_index(i   ,i+2)] == board[rowcolumn_to_index(i+1, i+2)]  == board[rowcolumn_to_index(i+2,i+2)] != ' ':
                return True             
    if board[rowcolumn_to_index(i   ,i  )] == board[rowcolumn_to_index(i+1, i+1)]  == board[rowcolumn_to_index(i+2,i+2)] != ' ':
                return True  
    if board[rowcolumn_to_index(i   ,i+2)] == board[rowcolumn_to_index(i+1, i+1)]  == board[rowcolumn_to_index(i+2,i  )] != ' ':
                return True  
    else:
           return False 

def whoisplaying(player):
    """Prints who's playing"""       
    print(f"\nPlayer {player}'s turn\n")    

          
initial_board = display_board()  
                
def play():
    players = ['X', 'O']
  
    print('*** TIC TAC TOE ***\n')
    print(initial_board)
    
    # First round
    val = 0
    whoisplaying(players[val])
    board = turn(initial_board, players[val])
    val ^= 1                                          # Changes player X to O to X...

    counter = 1
    while check_win(board) == False and counter < 9:  # While loop ends if one wins, or if all the grid is full.
        whoisplaying(players[val])
        board = turn(board, players[val])
        val ^= 1                                      
        counter +=1

    if counter == 9 and check_win(board) == False:
        print("It's a tie.")
    else:
        val ^= 1
        print(f"Congratulations! Player '{players[val]}' wins :)")    
play()

  

