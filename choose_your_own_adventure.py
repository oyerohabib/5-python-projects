name = input("type your name? ")
print("welcome", name, "to this adventure")

answer = input("you are on a dirt road, you can only go left or right, which would you like to go? ").lower()

if answer == "left":
  answer = input("you come to a river, you can walk around it or swim accross it, chose swim or walk? ").lower()
  
  if answer == "swim":
    print("you swam accross the river and were eaten by a shark")
  elif answer == "walk":
    print("you walked for many miles and lost the game")
  else:
    print("you picked a wrong option, you loose")
elif answer == "right":
  answer = input("you have come to a bridge, it looks wobbly, do you wan to cross it or head back, pick(cross/back)? ").lower()
  
  if answer == "back":
    print("you go back and loose")
  elif answer == "cross":
    answer = input("you crossed the bridge and met a stranger, do you wan to talk to them? (yes/no)? ").lower()
    
    if answer == "yes":
      print("you talked to the stranger and were given a gold, you win!!!")
    elif answer == "no":
      print("you ignored the stranger, they were offended and you loose")
    else:
      print("not a valid option, you loose")
else:
  print("wrong option, you loss")
  
print("thanks for playing this game", name + ".")