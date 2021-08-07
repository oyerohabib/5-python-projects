import random

top_of_range = 0
random_number = 0
guesses = 0

def guessANumber():
  global top_of_range
  top_of_range = input("Type a number? ")

  if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
      print("please type a number greater than 0 next time")
      quit()
      
  else:
    print("please type a number next time")
    quit()
    
  global random_number
  random_number = random.randint(0, top_of_range)
    
guessANumber()

def confirm():
  user_input = input("Do you still want to play, enter yes or no? \n").lower()
  if user_input == "yes":
    guessANumber()
    playGame()
  elif user_input == "no":
    print("Thank you for playing my number guesser game")
    quit()
  else:
    print("\nEnter only yes or no(quit).")
    confirm()

def playGame():
  
  while True:
    global guesses
    guesses += 1
    user_guess = input("make a guess? ")
    
    if user_guess.isdigit():
      user_guess = int(user_guess)
      
    else:
      print("please type a number next time")
      continue
    
    if user_guess == random_number:
      print("you got it.")
      print("you got it in", guesses, "guesses.\n")
      guesses = 0
      confirm()
      break
    elif user_guess > random_number:
      print("your guess is higher than the number")
    else:
      print("your guess is lower than the number")
      
playGame()

confirm()