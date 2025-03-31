def User1Turn(board):
    """
    This function allows player 1 to take their turn in the game.
    It prompts the user to enter the position they want to place their symbol (X) on the board.
    If the position is already occupied, it prints a message and exits the program.
    Otherwise, it updates the board with the player's symbol and exits the function.
    """
    pos = int(input("Enter X's position:"))
    if(board[pos-1] != 0):
        print("Wrong Move ..!!! ")
        playsound("Assignment\\synthesize6.mp3")
        exit()
    board[pos-1]=1
def User2Turn(board):
    """
    This function allows player 2 to take their turn in the game.
    It prompts the user to enter the position they want to place their symbol (O) on the board.
    If the position is already occupied, it prints a message and exits the program.
    Otherwise, it updates the board with the player's symbol and exits the function.
    """
    pos = int(input("Enter O's position:"))
    if(board[pos-1] != 0):
        print("Wrong Move ..!!! ")
        playsound("Assignment\\synthesize6.mp3")
        exit()
    board[pos-1]=-1
def constBoard(board):
    """
    A function that displays the current state of the board with player symbols.
    """
    print("Current state of the board :- \n")
    for i in range(0, 9):
        a = " | " if (i%3==0 or (i-1)%3==0) else "   "
        if((i>0) and (i%3 == 0)):
            print("\n----|-----|-----")
        if(board[i] == 0):
            print(f" {i+1} ", end=a)
        if(board[i] == 1):
            print(" X ", end=a)
        if(board[i] ==- 1):
            print(" O ", end=a)
    print("\n")
def analyseBoard(board):
    """
    Analyzes the given board to determine if there is a winner.
    """
    cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(8):
        if((board[cb[i][0]] != 0) and (board[cb[i][0]] == board[cb[i][1]]) and (board[cb[i][1]] == board[cb[i][2]])):
            return board[cb[i][0]]
    return 0
def minmax(board,player):
    """
    Uses min-max algorithm to select the most advantageous position to place the symbol(X).
    """
    x = analyseBoard(board)
    if x!=0:
        return (x*player)
    pos = -1
    value = -2
    for i in range(9):
        if board[i]==0:
            board[i] = player
            score = -minmax(board,player*-1)
            board[i] = 0
            if score>value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value
def CompTurn(board):
    """
    A function that simulates a turn for the computer in the game.
    """
    pos = -1
    value = -2
    for i in range(9):
        if board[i]==0:
            board[i] = 1
            score = -minmax(board,-1)
            board[i] = 0
            if score>value:
                value = score
                pos = i
    board[pos] = 1
from playsound import playsound
def main():
    """
    This function is the main entry point of the program. It prompts the user to choose between single player and multiplayer mode. 
    If the user chooses single player mode, it prompts the user to choose who goes first. It then enters a loop where the 
    computer and the user take turns making moves. The loop continues until the board is full or a player wins. After the loop, 
    it checks the final state of the board and displays the result.
    If the user chooses multiplayer mode, it enters a loop in which the players take turns making moves in an order. The loop 
    continues until the board is full or a player wins.After the loop, it checks the final state of the board and displays the result.
    """
    ch1 = input("Enter 1 for single palyer and 2 for multiplayer : ")
    try:
        ch1 = int(ch1)
    except:
        playsound("Assignment\\synthesize5.mp3")
        print("Please enter a valid choice and try again.")
        quit()
    board = [0,0,0,0,0,0,0,0,0]
    if ch1 == 1:
        print("Computer : X Vs. You : O")
        player = input("Enter 1 to play first and 2 to play second : ")
        try:
            player = int(player)
        except:
            playsound("Assignment\\synthesize5.mp3")
            print("Please enter a valid choice and try again.")
            quit()
        playsound("Assignment\\synthesize4.mp3")
        if player>2 or player<1:
            playsound("Assignment\\synthesize5.mp3")
            print("Please enter a valid choice and try again.")
            quit()
        for i in range(0, 9):
            if analyseBoard(board) != 0:
                break
            if (i+player)%2==0:
                CompTurn(board)
            else:
                constBoard(board)
                User2Turn(board)
    elif ch1 == 2:
        playsound("Assignment\\synthesize4.mp3")
        for i  in range(9):
            if analyseBoard(board)!=0:
                break
            if i%2==0:
                constBoard(board)
                User1Turn(board)
            else:
                constBoard(board)
                User2Turn(board)
    else:
        playsound("Assignment\\synthesize5.mp3")
        print("Please enter a valid input.")
        quit()
    x = analyseBoard(board)
    if x==0:
        constBoard(board)
        print("It's a Draw.")
        playsound("Assignment\\synthesize1.mp3")
    elif x == -1:
        constBoard(board)
        print("Player O has won.")
        playsound("Assignment\\synthesize3.mp3")
    elif x == 1:
        constBoard(board)
        print("Player X has won.")
        playsound("Assignment\\synthesize2.mp3")