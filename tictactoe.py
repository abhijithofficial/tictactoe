from clear_screen import clear
import random

def replay():
    choice =''

    while not (choice == 'Y' or choice == 'N') :
        choice = input("Do you want to play again 'Y' for yes 'N' for No \n")

        # print (choice)

    return choice == 'Y'

def space_check(board,position):
    return board[position] == ' '

def player_choice(board):
    position = 0
    while position not in list(range(1,10)) or not space_check(board,position):
        position =  int(input("Choose a position from 1 - 9 "))
    return position

def choose_player():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player One'
    else:
        return 'Player Two'

def full_board(board):
    return ' ' not in board

def wincheck(board,mark):
    return( (board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark)
    )

def place_marker(board,marker,position):

    board[position] = marker

def playerinput():
    playerone = ""
    while not playerone != 'X' or playerone != 'O':
        playerone = input("Player 1, Choose X or O : \n")
        if playerone == 'X':
            return ('X','O')
        elif playerone == 'O':
            return ('O','X')
        else:
            print("Enter a valid choice")



def display(mylist):
    clear()
    print( mylist[7] ,"|", mylist[8] ,"|", mylist[9] )
    print("----------")
    print( mylist[4] ,"|", mylist[5] ,"|", mylist[6] )
    print("----------")
    print( mylist[1] ,"|", mylist[2] ,"|", mylist[3] )





print("Welcome to Tic Tac Toe! Dev By Abhijith")

while True:
    mylist=[' ']*10
    mylist[0] = '$'
    display(mylist)
    playerone,playertwo=playerinput()
    turn = choose_player()
    print(turn , "will go first" )

    playgame = ''

    while not (playgame == 'Y' or playgame == 'N'):
        playgame =  input('Are you ready to play Y for yes, N for no : \n')

    if playgame == 'Y':
        gamemode=True
    else:
        gamemode=False

    while gamemode:
        if turn == "Player One":
            display(mylist)
            position =  player_choice(mylist)
            place_marker(mylist,playerone,position)
            if  wincheck(mylist,playerone):
                display(mylist)
                print("Player One Won the Game ")
                gamemode = False
            else:
                if full_board(mylist):
                    display(mylist)
                    print("Game Draw")
                    gamemode = False
                else:
                    turn = 'Player Two'

        else:
            display(mylist)
            position =  player_choice(mylist)
            place_marker(mylist,playertwo,position)
            if  wincheck(mylist,playertwo):
                display(mylist)
                print("Player Two Won the Game ")
                gamemode = False
            else:
                if full_board(mylist):
                    display(mylist)
                    print("Game Draw")
                    gamemode = False
                else:
                    turn = 'Player One'



    if not replay():
        break
