choice1 = input("1. Tic Tac Toe \n2. Calculation Master \nEnter your choice : ")
# The user is prompted to choose between two game : Tic Tac Toe or Calculation Master.
from playsound import playsound
try:
    choice1 = int(choice1)
except:
    playsound("Assignment\\synthesize5.mp3")
    print("Please enter a valid choice and try again.")
    quit()
if choice1 == 1:
    # If the user chooses Tic Tac Toe, redirect them to the Tic Tac Toe game.
    import project
    project.main()
elif choice1 == 2:
    # If the user chooses Calculation Master, prompt them to choose a game mode.
    choice2 = input("1. Discrete Levels (3 levels) \n2. Continuous Mode (Infinite levels) \nEnter your choice : ")
    try:
        # If the user does not enter an integer, print an error message and quit the game.
        choice2 = int(choice2)
    except:
        playsound("Assignment\\synthesize5.mp3")
        print("Please enter a valid choice and try again.")
        quit()
    if choice2 == 1:
        # If the user chooses Discrete Levels, redirect them to the Discrete Levels game.
        import pro
        pro.main()
    elif choice2 == 2:
        # If the user chooses Continuous Mode, redirect them to the Continuous Mode game.
        import pro2
        pro2.main()
    else:
        # If the user enters a choice other than 1 or 2, print an error message and quit the game.
        playsound("Assignment\\synthesize5.mp3")
        print("Please enter a valid choice and try again.")
        quit()
else:
    # If the user enters a choice other than 1 or 2, print an error message and quit the game.
    playsound("Assignment\\synthesize5.mp3")
    print("Please enter a valid choice and try again.")