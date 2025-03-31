Introduction:
The project encompasses two Python-based games: a simple math quiz game and Tic Tac Toe. Here's a brief overview of each:

Math Quiz Game: Allows players to select a difficulty level (learner, expert, or master) and presents arithmetic problems accordingly. After completing the quiz, feedback is provided on the player's performance, with the option to play again.
Tic Tac Toe Game: Offers single or multiplayer modes. At the end of the game, the result is displayed, indicating if a player has won, if the opponent has won, or if it's a draw.
Scope:
This project aims to provide entertainment and educational value. The math quiz game enhances calculation speed and fosters focus, while Tic Tac Toe offers a relaxing gaming experience. It also serves as a learning opportunity for Python developers, utilizing modules like random and time efficiently.

Methodology:
Tic Tac Toe Game:
    Code Overview: Functions handle player turns, board display, win detection, and computer AI for single-player mode.
    Key Functions:
    User1Turn(board): Allows player 1 to input their move.
    User2Turn(board): Allows player 2 to input their move.
    constBoard(board): Displays the current state of the board.
    analyseBoard(board): Determines if there's a winner.
    minmax(board, player): Implements the Minimax algorithm for computer moves.
    CompTurn(board): Simulates the computer's turn.
    main(): Handles game flow and user input.
Calculation Master Game:
    Structure and Flow: The main() function serves as the entry point. It generates arithmetic problems based on difficulty levels, records completion time, and provides feedback.
    Features:
    Dynamic problem generation.
    Input validation.
    Timer for completion time.
    Feedback messages.
    Option to replay.

Conclusion:
The project effectively implements Tic Tac Toe and a Math Quiz Game, demonstrating core Python features. It offers room for improvement in user interface and additional features for enhanced gaming experiences.

References:
Python Documentation: Time (https://docs.python.org/3/library/time.html)
GeeksforGeeks: Playing Sound in Python (https://www.geeksforgeeks.org/play-sound-in-python/)
