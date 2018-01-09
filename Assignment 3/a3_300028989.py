#Family Name: Agarwal
#Student number:300028989
#Course: ITI 1120
#Assignment Number 3

import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)
    print("Shuffling deck...\n\n")

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for j in range(len(board)//2):
          board[j]=letter
          board[j+len(board)//2 ]=board[j]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for j in range(len(a)):
        print('{0:4}'.format(a[j]), end=' ')
    print()
    for j in range(len(a)):
        print('{0:4}'.format(str(j+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    discovered[p1 - 1] = original_board[p1 - 1]
    discovered[p2 - 1] = original_board[p2 - 1]
    for k in range(len(discovered)):
        print('{0:4}'.format(discovered[k]), end=' ')
    print()
    for k in range(len(discovered)):
        print('{0:4}'.format(str(k+1)), end=' ')
        
    

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for j in range(len(raw_board)):
        raw_board[j]=raw_board[j].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    # YOUR CODE GOES HERE
    
    l.sort()
    i = 0
    while(i < len(l)):
        if l[i] == "*":
            i = i + 1
        elif ((l.count(l[i]) % 2) == 1):
            for q in range(1, l.count(l[i])):
                playable_board = playable_board + [l[i]]
            i = i + (l.count(l[i]))
        else:
            for q in range(l.count(l[i])):
                playable_board = playable_board + [l[i]]
            i = i + (l.count(l[i]))
                
        
            
    
    return playable_board



def is_rigorous(l):
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    # YOUR CODE GOES HERE
    for i in range(len(l)):
        if l.count(l[i]) != 2:
            return False
    return True
                
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE
    unshown = len(board) * ["*"]
    guesses = 0
    while(unshown.count("*") > 0):
        print_board(unshown)

        print("\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in range [1, " +str(len(board)) + "]")
        pos1 = int(input("Enter position 1: "))
        pos2 = int(input("Enter position 2: "))
        if((pos1 <= 0 or pos1 > len(board)) or (pos2 <= 0 or pos2 > len(board)) or (pos1 == pos2)):
            flag = True
        elif((unshown[pos1-1] != "*") or (unshown[pos2-1] != "*")):
            flag = True
        else:
            flag = False
        while (flag):
            if((pos1 < 0 or pos1 > len(board)) or (pos2 < 0 or pos2 > len(board))):
                print("Position out of range.")
            elif ((unshown[pos1-1] != "*") or (unshown[pos2-1] != "*")):
                print("One or both of your chosen positions has already been paired.")
            else:
                print("You chose the same positions.")
            print("Please try again. This guess did not count. You current number of guesses is" , guesses)

            print("\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in range [1, " +str(len(board)) + "]")
            pos1 = int(input("Enter position 1: "))
            pos2 = int(input("Enter position 2: "))
            if((pos1 <= 0 or pos1 > len(board)) or (pos2 <= 0 or pos2 > len(board)) or (pos1 == pos2)):
                flag = True
            elif((unshown[pos1-1] != "*") or (unshown[pos2-1] != "*")):
                flag = True
            else:
                flag = False
        print_revealed(unshown, pos1, pos2, board)
        guesses = guesses + 1
        if (board[pos1-1] == board[pos2-1]):
            unshown[pos1-1] = board[pos1-1]
            unshown[pos2-1] = board[pos2-1]
        else:
           unshown[pos1-1] = "*"
           unshown[pos2-1] = "*"
        wait_for_player()
    amntaway = guesses - int((len(board)/2))
    print("Congratulations! You completed the game with " + str(guesses) + " guesses. That is " + str(amntaway) + " more than the best possible.")
    




# main
print("*" * 42)
print("*" + " " * 40 + "*")
print("*  __Welcome to my Concentration game__  *")
print("*" + " " * 40 + "*")
print("*" * 42)
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
print("\n\nWould you like (enter 1 or 2 to indicate your choice):")
print("(1) me to generate a rigorous deck of cards for you \n(2) or, would you like me to read a deck from a file?")
choice = int(input(""))
while(choice > 2 or choice < 1):
    print(str(choice) + " is not existing option. Please try again. Enter 1 or 2 to indicate your choice")
    choice = int(input(""))

                

# YOUR CODE FOR OPTION 1 GOES HERE
if choice == 1:
    print("You have chose to have a rigorous deck of cards generated for you")
    print("\nHow many cards do you want to play with?")
    size = int(input("Enter an even number between 0 and 52: "))
    while ((size > 52 or size < 0) or (size % 2 > 0)):
        print("\nHow many cards do you want to play with?")
        size = int(input("Enter an even number between 0 and 52: "))
    board = create_board(size)
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)

# YOUR CODE FOR OPTION 2 GOES HERE
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
else:
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)
    print()
    if (is_rigorous(board)):
        rig = "and rigorous"
    else:
        rig = "but not rigorous"
        
    deckinfo = "*  __This deck is now playable " + rig + " and it has " + str(len(board)) + " cards.__  *"
    print(len(deckinfo) * "*")
    print("*" + (len(deckinfo) - 2) * " " + "*")
    print(deckinfo)
    print("*" + (len(deckinfo) - 2) * " " + "*")
    print(len(deckinfo) * "*")
shuffle_deck(board)
wait_for_player()
if(len(board) == 0):
    print("The resulting board is empty.\nPlaying concentration game with an empty board is impossible.\nGoodbye")
else:
    play_game(board)
    
#
#print("You chose to load a deck of cards from a file")
#file=input("Enter the name of the file: ")
#file=file.strip()
#board=read_raw_board(file)
#board=clean_up_board(board)

