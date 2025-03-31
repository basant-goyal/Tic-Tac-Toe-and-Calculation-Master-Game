from playsound import playsound
def main():
  """
  The main function that runs the arithmetic quiz game.
  This function prompts the user to select a level (1, 2, or 3) and generates arithmetic problems based on the selected level.
  The user is then asked to solve the problems and the function keeps track of the number of wrong answers.
  After the specified number of problems (10), the function calculates the total time taken by the user 
  and prints a compliment based on the time and the user's level. The user is then given the option to try again.
  """
  import random
  import time
  OPERATORS = ["+", "-", "*"]
  TOTAL_PROBLEMS = 10
  def generate_problem(level):
    """
    Generates an arithmetic problem with random operands and operators based on the given level.
    The level dicides the difficulty of the problem.
    Level 1 has operands between 2 and 12.
    Level 2 has operands between 10 and 20.
    Level 3 has operands between 20 and 40.
    """
    if level==1:
      left = random.randint(2, 12)
      right = random.randint(2, 12)
    elif level==2:
      left = random.randint(10,20)
      right = random.randint(10,20)
    elif level==3:
      left = random.randint(20,40)
      right = random.randint(20,40)       
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer
  level=input("Level 1: Learner\nLevel 2: Expert\nLevel 3: Master\nEnter level number to play:")
  try:
    level = int(level)
  except:
    playsound("Assignment\\synthesize5.mp3")
    print("Please enter a valid choice and try again.")
    quit()
  if level<1 or level>3:
    print("\nPlease enter a valid input.\n")
    main()
  first_input=input("Press enter to start : ")
  print("----------------------")
  start_time = time.time()
  for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem(level)
    while True:
      guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
      if guess == str(answer):
        break
  end_time = time.time()
  print("----------------------")
  def compliment():
    """
    A function that prints different compliments based on the total time taken and the player's level.
    """
    compliments_level3=["legendary","skillful","unbelievable","unreal","godlike"]
    compliments=["good","nice","excellent","outstanding"]
    global total_time
    total_time = round(end_time - start_time, 2)
    if total_time<=30 and level<3:
        print("You finished in",total_time,"seconds! You are too good for this try next level")
    elif total_time>30  and level!=3:
        if total_time<45:
          print(random.choice(compliments),"! You finished in", total_time, "seconds!")
        else:
          print("nice You finished in", total_time, "seconds!")
    elif total_time>30  and level==3:
        if total_time<60:
          print(random.choice(compliments_level3),"! You finished in", total_time, "seconds!")
        else:
          print("nice You finished in", total_time, "seconds!")
    elif total_time<=30 and level==3:
        print("YOU ARE A GENIUS You finished in", total_time, "seconds!")
  compliment()
  playsound("Assignment\\synthesize7.mp3")
  ch1 = input("Enter y(Y) to play again : ")
  if ch1 == 'y' or ch1 == 'Y':
    main()
  playsound("Assignment\\synthesize8.mp3")