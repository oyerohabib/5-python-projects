print("Welcome to my quiz game")

playing = input("Do you want to play my game? ")

if playing.lower() != "yes":
  quit()

print("Okay! Let's play.")
score = 0

answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
  print("correct!")
  score += 1
else:
  print("incorrect!")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
  print("correct!")
  score += 1
else:
  print("incorrect!")

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
  print("correct!")
  score += 1
else:
  print("incorrect!")

answer = input("what does PSU stands for? ")
if answer.lower() == "power supply unit":
  print("correct!")
  score += 1
else:
  print("incorrect!")
  
print("You got " + str(score) + " question correctly")
print("You had " + str((score/4) * 100) + "%.")