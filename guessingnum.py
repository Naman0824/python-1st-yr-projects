import random
print('')
print("WELCOME TO GUESIING THE NUMBER GAME FROM 1 TO 10")
pa=1
l=[1,2,3,4,5,6,7,8,9,10]
while pa==1:
      cg=random.choice(l)
      while True:
            try:
                  print('')
                  ug=int(input("please guess the number from 1 to 10 : "))
                  if ug<1 or ug>10:
                        print('')
                        print("please enter number from 1 to 10 only")
                        continue
                  break
            except ValueError:
                  print("")
                  print("please enter numeric value only")
      if ug != cg:
            print("you guess the wrong number computer number is",cg)
      else:
            print("you guessed the correct number ")
      while True:
            try:
                  pa=int(input('to play again press 1 to exit press any number other than 1 : '))
                  break
            except ValueError:
                  print("enter only numeric value ")
