n=1;bjp=0;congress=0;aap=0;others=0
while(n==1):
      name=(input("enter your name : "))
      age=int(input("enter you age : "))
      choice1=int(input(" to vote 'BJP' press 1 : \n to vote 'Congress' press 2 : \n to vote 'AAP' press 3 : \n to vote 'Others' press 4 : \n"))
      choice2=int(input("to 'continue' press 1 \nto 'exit' press 2 \n"))
      if(age>=18):
            if(choice1==1):
                  print("You have successfully voted BJP\n 'THANKS FOR VOTING':) ")
                  bjp+=1
            elif(choice1==2):
                  print("You have successfully voted Congress\n 'THANKS FOR VOTING':) ")
                  congress+=1
            elif(choice1==3):
                  print("You have successfully voted AAP\n 'THANKS FOR VOTING':) ")
                  aap+=1
            elif(choice1==4):
                  print("You have successfully voted Others\n 'THANKS FOR VOTING':) ")
                  others+=1
            elif(choice1 !=(1 or 2 or 3 or 4)):
                  print("enter valid choice for voting the party")
                  print("2 attempts left")
                  choice1=int(input("to vote 'BJP' press 1 : \n to vote 'Congress' press 2 : \n to vote 'AAP' press 3 : \n to vote 'Others' press 4 : \n"))
                  if(choice1==1):
                        print("You have successfully voted BJP\n 'THANKS FOR VOTING':) ")
                        bjp+=1
                  elif(choice1==2):
                        print("You have successfully voted Congress\n 'THANKS FOR VOTING':) ")
                        congress+=1
                  elif(choice1==3):
                        print("You have successfully voted AAP\n 'THANKS FOR VOTING':) ")
                        aap+=1
                  elif(choice1==4):
                        print("You have successfully voted Others\n 'THANKS FOR VOTING':) ")
                        others+=1
                  elif(choice1 !=(1 or 2 or 3 or 4)):
                        print("enter valid choice for voting the party")
                        print("1 attempts left")
                        choice1=int(input("to vote 'BJP' press 1 : \n to vote 'Congress' press 2 : \n to vote 'AAP' press 3 : \n to vote 'Others' press 4 : \n"))
                        if(choice1==1):
                              print("You have successfully voted BJP\n 'THANKS FOR VOTING':) ")
                              bjp+=1
                        elif(choice1==2):
                              print("You have successfully voted Congress\n 'THANKS FOR VOTING':) ")
                              congress+=1
                        elif(choice1==3):
                              print("You have successfully voted AAP\n 'THANKS FOR VOTING':) ")
                              aap+=1
                        elif(choice1==4):
                              print("You have successfully voted Others\n 'THANKS FOR VOTING':) ")
                              others+=1
            if(choice2==2):
                  if(bjp>congress and bjp>aap and bjp>congress and bjp>others):
                        print("BJP IS THE WINNER")
                  elif(congress>bjp and congress>aap and congress>others):
                        print("CONGRESS IS THE WINNER")
                  elif(aap>bjp and aap>congress and aap>others):
                        print("AAP IS THE WINNER ")
                  elif(others>bjp and others>congress and others>aap):
                        print("OTHERS IS A WINNER ")
                  elif(bjp==congress==aap==others):
                        print("All election parties got equal votes so elections is tied.")
                  elif(bjp==congress==aap):
                        print("The election is tied between BJP,CONGRESS and AAP and OTHERS has lost the match ")
                  elif(bjp==congress==others):
                        print("The election is tied between BJP,CONGRESS and OTHERS and AAP has lost the match ")
                  elif(others==congress==aap):
                        print("The election is tied between OTHERS,CONGRESS and AAP and BJP has lost the match ")
                  elif(bjp==congress):
                        if(bjp!=0 and congress!=0):
                              print("The elections has been tied between BJP and CONGRESS ")
                        elif(aap==others):
                              print("The elections has been tied between AAP and OTHERS ")
                  elif(bjp==aap):
                        if(bjp!=0 and aap!=0):
                              print("The elections has been tied between BJP and AAP ")
                        elif(congress==others):
                              print("The elections has been tied between CONGRESS and OTHERS ")
                  elif(bjp==others):
                        if(bjp!=0 and others!=0):
                              print("The elections has been tied between BJP and OTHERS ")
                        elif(congress==aap):
                              print("The elections has been tied between CONGRESS and AAP ")
                  elif(congress==aap):
                        print("The elections has been tied between CONGRESS and AAP ")
                  elif(congress==others):
                        print("The elections has been tied between CONGRESS and OTHERS ")
                  elif(aap==others):
                        print("The elections has been tied between AAP and OTHERS ")
                  n=2
            elif(choice2==1):
                  n=1
            else:
                  print("enter valid choice to continue or exit")
                  print("2 attempt left")
                  choice2=int(input("to 'continue' press 1 \nto 'exit' press 2 \n"))
                  if(choice2==2):
                        if(bjp>congress and bjp>aap and bjp>congress and bjp>others):
                              print("BJP IS THE WINNER")
                        elif(congress>bjp and congress>aap and congress>others):
                              print("CONGRESS IS THE WINNER")
                        elif(aap>bjp and aap>congress and aap>others):
                              print("AAP IS THE WINNER ")
                        elif(others>bjp and others>congress and others>aap):
                              print("OTHERS IS A WINNER ")
                        elif(bjp==congress==aap==others):
                              print("All election parties got equal votes so elections is tied.")
                        elif(bjp==congress==aap):
                              print("The election is tied between BJP,CONGRESS and AAP and OTHERS has lost the match ")
                        elif(bjp==congress):
                              if(bjp!=0 and congress!=0):
                                    print("The elections has been tied between BJP and CONGRESS ")
                              elif(aap==others):
                                    print("The elections has been tied between AAP and OTHERS ")
                        elif(bjp==aap):
                              if(bjp!=0 and aap!=0):
                                    print("The elections has been tied between BJP and AAP ")
                        elif(congress==others):
                              print("The elections has been tied between CONGRESS and OTHERS ")
                        elif(bjp==others):
                              if(bjp!=0 and others!=0):
                                    print("The elections has been tied between BJP and OTHERS ")
                              elif(congress==aap):
                                    print("The elections has been tied between CONGRESS and AAP ")
                        elif(congress==aap):
                              print("The elections has been tied between CONGRESS and AAP ")
                        elif(congress==others):
                              print("The elections has been tied between CONGRESS and OTHERS ")
                        elif(aap==others):
                              print("The elections has been tied between AAP and OTHERS ")
                        n=2
                        break
                  elif(choice2==1):
                        n=1
                        
                  else:
                        print("enter valid choice to continue or exit")
                        print("1 attempt left")
                        choice2=int(input("to 'continue' press 1 \nto 'exit' press 2 \n"))
                        if(choice2==2):
                              if(bjp>congress and bjp>aap and bjp>congress and bjp>others):
                                    print("BJP IS THE WINNER")
                              elif(congress>bjp and congress>aap and congress>others):
                                    print("CONGRESS IS THE WINNER")
                              elif(aap>bjp and aap>congress and aap>others):
                                    print("AAP IS THE WINNER ")
                              elif(others>bjp and others>congress and others>aap):
                                    print("OTHERS IS A WINNER ")
                              elif(bjp==congress==aap==others):
                                    print("All election parties got equal votes so elections is tied.")
                              elif(bjp==congress==aap):
                                    print("The election is tied between BJP,CONGRESS and AAP and OTHERS has lost the election ")
                              elif(bjp==congress):
                                    if(bjp!=0 and congress!=0):
                                          print("The elections has been tied between BJP and CONGRESS ")
                                    elif(aap==others):
                                          print("The elections has been tied between AAP and OTHERS ")
                              elif(bjp==aap):
                                    if(bjp!=0 and aap!=0):
                                          print("The elections has been tied between BJP and AAP ")
                              elif(congress==others):
                                    print("The elections has been tied between CONGRESS and OTHERS ")
                              elif(bjp==others):
                                    if(bjp!=0 and others!=0):
                                          print("The elections has been tied between BJP and OTHERS ")
                              elif(congress==aap):
                                    print("The elections has been tied between CONGRESS and AAP ")
                              elif(congress==aap):
                                    print("The elections has been tied between CONGRESS and AAP ")
                              elif(congress==others):
                                    print("The elections has been tied between CONGRESS and OTHERS ")
                              elif(aap==others):
                                    print("The elections has been tied between AAP and OTHERS ")
                              n=2
                              break
                        elif(choice2==1):
                              n=1     
      else:
            print("Age can't be smaller than 18 please enter valid age")
print("'BUT THE ULTIMATE WINNER IS ONE AND ONLY THE ' ALOO DALO SONA NIKALO ' ONE ;)'")