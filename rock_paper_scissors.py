import random

computer_win = 0
user_win = 0
game_count = 0

options = ["rock", "paper", "scissors"]

while True:
  print("")
  user_input = input("type rock / paper / scissors or q to quit? ").lower()
  if user_input == "q":
    break
  
  if user_input not in options:
    print("type a valid option, thanks.")
    continue
  
  random_number = random.randint(0, 2)
  # rock: 0, paper: 1, scissors:2
  computer_pick = options[random_number]
  game_count += 1
  print("game number", game_count)
  print("computer picked", computer_pick + ".")
  
  if user_input == "rock" and computer_pick == "scissors":
    print("you won")
    user_win += 1
  
  elif user_input == "paper" and computer_pick == "rock":
    print("you won")
    user_win += 1
  
  elif user_input == "scissors" and computer_pick == "paper":
    print("you won")
    user_win += 1
  
  elif user_input == "scissors" and computer_pick == "scissors" or user_input == "paper" and computer_pick == "paper" or user_input == "rock" and computer_pick == "rock" :
    print("tie game")
    
  else:
    print("computer wins")
    computer_win += 1
    
print("total number of games", game_count)
print("you won", user_win, "times.")
print("computer won", computer_win, "times.")
print("GoodBye")