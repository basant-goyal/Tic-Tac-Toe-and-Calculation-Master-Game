import random
from playsound import playsound
import time
def compliment(total_time,level):
    """This function prints the time you take to solve a particular level with some
         appreciation.."""
      
    compliments=["legendary","skillful","unbelievable","unreal","godlike"] 
    avg_compliments=["good","excellent","outstanding"] 
    if total_time<=30:
        print(f"You finished in {total_time} seconds! You are too good for this, try next level")
    elif total_time>30  and total_time<=45:
        print(f"{random.choice(compliments)}! You finished in {total_time} seconds!\nCongratulations!! You cleared the level") 
    elif total_time<=60:
        print(f"{random.choice(avg_compliments)}! You finished in {total_time} seconds!\nCongratulations!! You cleared the level")
    else:
        print(f"Sorry, you couldn't clear level {level}.")
        playsound("Assignment\\synthesize8.mp3")
        quit()  

def generate_problem(level):  
    """This Function return a arthimatic problem with a random operatorfrom OPERATORS list"""
    left=random.randint(2*level,level*10)
    right=random.randint(2*level,level*10)
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer  

OPERATORS = ["+", "-", "*"]
TOTAL_PROBLEMS = 10   #Maximum Number of Problems in each level
MAX_WRONG_QUESTIONS=5  #Maximum Number of Question that can be done wrong.
def main():
    """
    The main function of the game.
    This function starts the game by prompting the player to press enter to start or any other key to quit. 
    If the player chooses to start, the game begins with the first level. 
    The game consists of a series of arithmetic problems generated by the `generate_problem` function. 
    The player is given the problem and asked to input the answer. 
    If the player inputs the correct answer, the game moves on to the next problem. 
    If the player inputs the wrong answer three times in a row, the game ends for that problem. 
    If the player inputs the wrong answer more than five times in total, the game ends. 
    The game keeps track of the player's level and the time taken to solve each level. 
    After each level, the player is given a compliment and the game moves on to the next level. 
    The game continues until the player loses or chooses to quit.
    """
    level=1
    first_input=input("Press enter to start or anything else to quit :")
    while(True):
        if first_input!="":
            playsound("Assignment\\synthesize8.mp3")
            print("Game Over.")
            break
        print(f"Your game starts with level:{level}")
        print("--------------------------")
        wrong1 = 0
        start_time = time.time()    #time before the game 
        for i in range(TOTAL_PROBLEMS):
            expr, answer = generate_problem(level)
            wrong = 0
            while True:
                guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
                if guess == str(answer):   # you get the right answer
                    break
                wrong += 1 
                if(wrong>=3):   #it is written to track the case if you are putting wrong answer to the same question more than 4 times
                    wrong1 += 1
                    break
            if(wrong1>=MAX_WRONG_QUESTIONS):     #it is written to get you out of the game as you crossed the maximum number of wrongs you can do in this game.
                break
        end_time = time.time()     #time after the game
        print("----------------------")
        total_time = round(end_time - start_time, 2)
        if(wrong1>=MAX_WRONG_QUESTIONS):
            print("You lost this one,Better luck next time...")
            playsound("Assignment\\synthesize8.mp3")
            quit()
        else:
            compliment(total_time,level)
            playsound("Assignment\\synthesize9.mp3")
            level+=1
            input("Press anything to continue.")