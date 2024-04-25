import random
sum=0 
csum=0
l=[1,2,3,4,5,6]
cntinue=1
print("")
print("WELCOME TO A DICE GAME :)")
print("")
while cntinue==1:
      cn=random.choice(l)
      csum=csum+cn
      while True:
            try:
                  n=int(input("enter a number you get on dice from 1 to 6 : "))
                  if n<7 and n>0:
                        sum=sum+n
                        break
                  else:
                        print('please enter number from 1 to 6 only')
                        continue
            except ValueError:
                  print("please enter numeric value only")
                  continue
      while True:
            try:
                  cntinue=int(input("to continue playing press 1 to exit press any numeric vaue other than 1 : "))
                  break
            except ValueError:
                  print("please enter numeric value only")
else:
      if sum>csum:
            print("")
            print("you won the match ! your score is ",sum,' computer score is ', csum)
      elif csum>sum:
            print('')
            print("computer won the match ! your score is ",sum,' computer score is ', csum)
      elif sum==csum:
            print('')
            print("match has been drawn ! your score is ",sum,' computer score is ', csum)
