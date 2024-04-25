import random
print("Hey! Welcome to this amazing game of stone paper scissor")
option=["stone","paper","scissor"]

while True:
  user_input=input("enter your choice(stone/paper/scissor/q for quit the game): ").lower()
  if user_input=="q":
    print("you have succesfully quit the game ")
    break
  if user_input not in option:
    print("you have entered the wrong input please enter the appropriate input")
    continue

  random_number = random.randint(0,2)
  computer_move= option[random_number]
  print("computer picked",computer_move+".")
  if user_input=="stone" and computer_move=="scissor":
    print("you win")
  elif user_input=="paper" and computer_move=="stone":
    print("you win")
  elif user_input=="scissor" and computer_move=="paper":
    print("you win")
  elif user_input==computer_move:
    print("match is draw")
  else:
    print("you loose")