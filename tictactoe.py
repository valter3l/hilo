"""
This is a TIC-TAC-TOE game.
I started using an different aproach then I changed to a list to store the values to be in the board.
It developed fast but I took a long time to solve some loop issues in the main function; then it endend 
with what I believe to be a lot of ADJUSTMENTS or PATCHES. This is why I beleieve it is far from efficient 
or perfect; however, as long as I tested it, it seems to be working.
"""

# - Asks for player X to enter a position to put his "X" mark, checks if it is available and, if so, then substitutes the number by an "X". If not, message the user and prompt again for a valid position until it comes.
def prompt_player_x(t):
    print("Player X turn!\n")
    player_input = input ("Enter an available position for your mark, between 1 and 9: ")
    while check_position(t, player_input) == False:
        print("You entered an invalid value!")
        player_input = input ("Enter an available position for your mark, between 1 and 9: ")
    if check_position(t,player_input)==True:
        if player_input == "1":
            t[0] = "X"
        elif player_input == "2":
            t[1] = "X"
        elif player_input == "3":
            t[2] = "X"
        elif player_input == "4":
            t[3] = "X"
        elif player_input == "5":
            t[4] = "X"
        elif player_input == "6":
            t[5] = "X"
        elif player_input == "7":
            t[6] = "X"
        elif player_input == "8":
            t[7] = "X"
        elif player_input == "9":
            t[8] = "X"

# - Asks for player Y to enter a position to put his "Y" mark, checks if it is available and, if so, then substitutes the number by an "Y". If not, message the user and prompt again for a valid position until it comes.
def prompt_player_o(t):
    print("Player O turn!\n")
    player_input = input ("Enter an available position for your mark, between 1 and 9: ")
    while check_position(t, player_input) == False:
        print("You entered an invalid value!\n")
        player_input = input ("Enter an available position for your mark, between 1 and 9: ")
    if check_position(t,player_input)==True:
        if player_input == "1":
            t[0] = "O"
        elif player_input == "2":
            t[1] = "O"
        elif player_input == "3":
            t[2] = "O"
        elif player_input == "4":
            t[3] = "O"
        elif player_input == "5":
            t[4] = "O"
        elif player_input == "6":
            t[5] = "O"
        elif player_input == "7":
            t[6] = "O"
        elif player_input == "8":
            t[7] = "O"
        elif player_input == "9":
            t[8] = "O"
    return t

# - Checks if a value is in a list and returns a boolean value
def check_position(t,i):
    if i in t:
        return True
    else:
        return False

# - Checks if some repetitions occurs in a list and return a boolean value
def check_winner(t):
    if t[0] == t[1] and t[1] == t[2]:
        return True
    elif t[3] == t[4] and t[4] == t[5]:
        return True
    elif t[6] == t[7] and t[7] == t[8]:
        return True
    elif t[0] == t[3] and t[3] == t[6]:
        return True
    elif t[1] == t[4] and t[4] == t[7]:
        return True
    elif t[2] == t[5] and t[5] == t[8]:
        return True
    elif t[0] == t[4] and t[4] == t[8]:
        return True
    elif t[2] == t[4] and t[4] == t[6]:
        return True
    else:
        return False

# - Prints the board to the screen with values from a list
def print_board(t):
    print("{} | {} | {}".format(t[0],t[1],t[2]))
    print("--+---+--")
    print("{} | {} | {}".format(t[3],t[4],t[5]))
    print("--+---+--")
    print("{} | {} | {}".format(t[6],t[7],t[8]))
    print()

# - Main function - 
def main():
    #max turns possible
    turns = 9
    #welcome message
    print("Welcome to Tic Tac Toe game!\n") 
    #list to store the board values 
    t = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #call to print the list in the board format
    print_board(t)
    #loop to perform as long as there are available turns
    while (turns>0):
        #even turns - prompts player O check if there is a winner, if so, prints board and declares a O the winner and end the loop. If not, change the turn and print the new board.
        if turns%2 == 0:
            prompt_player_o(t)
            if check_winner(t)==True:
                print_board(t)
                print("O won!")
                break
            else:
                turns -= 1
                print_board(t)
        #uneven turns - prompts player X check if there is a winner, if so, prints board and declares a X the winner and end the loop. If not, change the turn and print the new board.
        else:
            prompt_player_x(t)
            if check_winner(t)==True:
                print_board(t)
                print("X won!")
                break
            else:
                turns -= 1
                print_board(t)
    #when turns ends and there are no winners
    if turns == 0:
        print("It's a draw!")

if __name__ == "__main__":
    main()