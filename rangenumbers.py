strt_point=int(input("enter starting number : "))
end_point=int(input("enter ending point : "))
updation=int(input("enter updation value : "))
choice1=int(input("enter 1 for result in verical or enter 2 for result in horizontal : "))
choice2=int(input("enter 1 for forward order or enter 2 for reverse order : "))
if(updation<0):
      print("enter positive value")
else:
      if(strt_point<=end_point):
            if(choice2==1 and (choice1==1 or choice1==2)):
                  if(choice1==1):
                        print("forward order in vertical ")
                  else:
                        print("forward order in horizontal ")
                  for i in range (strt_point,end_point+1,updation):
                        if(choice1==1):
                                    print(i)
                        elif(choice1==2):
                              print(i,end=" ")
                        else:
                              print("enter valid choices")
            elif(choice2==2 and (choice1==1 or choice1==2)):
                  if(choice1==1):
                        print("reversed order in vertical ")
                  elif(choice1==2):
                        print("reversed order in horizontal ")
                  for i in range (end_point,strt_point,-updation):
                        if(choice1==1):
                              print(i)
                        elif(choice1==2):
                              print(i,end=" ")
                        else:
                              print("enter valid choices")
            else:
                  print("enter valid choice of order of printing ")
      else:
            if(choice2==1 and (choice1==1 or choice1==2)):
                  if(choice1==1):
                        print("forward order in vertical ")
                  elif(choice1==2):
                        print("forward order in horizontal ")
                  for i in range (end_point,strt_point+1,updation):
                        if(choice1==1):
                              print(i)
                        elif(choice1==2):
                              print(i,end=" ")
                        else:
                              print("enter valid choices")
            elif(choice2==2  and (choice1==1 or choice1==2)):
                  if(choice1==1):
                        print("reversed order in vertical ")
                  else:
                        print("reversed order in horizontal ")
                  for i in range(strt_point,end_point,-updation):
                        if(choice1==1):
                              print(i)
                        elif(choice1==2):
                              print(i,end=" ")
                        else:
                              print("enter valid choices")
            else:
                  print("enter valid choices")

print("\ntata bye-bye khatam gaya")