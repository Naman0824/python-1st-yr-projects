inventory={'pepsi':30,'cocacola':40,'fruti':35,'fanta':30,'sprit':25}
print('')
print('PRODUCT      PRICE ')
print('-------------------')
print('pepsi     -  30rs ')
print('cocacola  -  40rs ')
print('fruti     -  35rs ')
print('fanta     -  30rs ')
print('sprit     -  25rs ')
print('-------------------')
cart={}
while True:
      prdct=input("Enter The Product Name : ")
      if prdct in inventory:
            while True:
                  try:
                        qty=int(input("Enter The Quantity : "))
                        break
                  except ValueError:
                        print("please enter a valid quantity ")
            while qty<1:
                  print("PLEASE ENTER VALID QUANTITY : ")
                  while True:
                        try:
                              qty=int(input("Enter The Quantity : "))
                              break
                        except ValueError:
                              print("please enter a valid quantity ")
            if prdct in cart:
                  cart[prdct]+=qty
            else:
                  cart[prdct]=qty
            add=(input("for adding more items press 1 \nfor exit press 2 \n: "))
            if add=='1':
                  continue
            elif add=='2':
                  break
            elif add!='1' or add!= '2' :
                  print("Press Valid Button to continue or exit (3 attempt left )")
                  add=(input("for adding more items press 1 \nfor exit press 2 \n: "))
                  if add=='1':
                        continue
                  elif add=='2':
                        break
                  elif add!='1' or add!='2':
                        print("Press Valid Button to continue or exit (2 attempt left )")
                        add=(input("for adding more items press 1 \nfor exit press 2 \n: "))

                        if add=='1':
                              continue
                        elif add=='2':
                              break
                        elif add!='1' or add!='2':
                              print("Press Valid Button to continue or exit (1 attempt left )")
                              add=(input("for adding more items press 1 \nfor exit press 2 \n: "))
      elif prdct not in inventory:
            print("")
            print("Item not available :( \nenter valid item name : ")
print("")
print('Item In Your Cart')
print('-------------------------------------------------------')
print('')
print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
sub_total=0
for prdct,qty in cart.items():
      price_per_peice=inventory[prdct]
      total_price=qty*price_per_peice
      sub_total=sub_total+total_price
      print("",prdct[0:5], "      ",qty,'    ',price_per_peice,'                  ',qty*price_per_peice)
print('')
print('-------------------------------------------------------') 
print('')
print("TOTAL CART AMOUNT IS RS. ",sub_total)
while True:
      try:
            print("")
            print("SELECT YOUR PREFFERED PAYMENT MODE")
            payment=int(input("for cash Press 1 \nfor card press 2  \nif you want to exit PRESS any other key : "))
            break
      except ValueError:
            print("")
            print('please enter valid payment mode')
cash=0
while payment==1:
      while True:
            try:
                  cash=int(input("Enter Amount You Have : "))
                  break
            except ValueError:
                  print("Please Enter Only Numbric Value")
      while cash<sub_total:
            print('')
            print("YOU DONT HAVE SUFFICEIENT BALANCE")
            while True:
                  try:
                        print("")
                        print("SELECT YOUR PREFFERED PAYMENT MODE")
                        payment=int(input("for rentering cash PRESS 1 : \nfor changing mode of payment PRESS 2 : \nto discard cart PRESS 3 : "))
                        break
                  except ValueError:
                        print("")
                        print('please enter valid payment mode')
            if payment==1:
                  while True:
                        try:
                              cash=int(input("Enter Amount You Have : "))
                              break
                        except ValueError:
                              print("Please Enter Only Numbric Value")
            else:
                  break
      else:
            print('')
            print("")
            print('Item In Your Cart')
            print('-------------------------------------------------------')
            print('')
            print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
            print('')
            for prdct,qty in cart.items():
                  price_per_peice=inventory[prdct]
                  print("",prdct[0:5:1], "      ",qty,'    ',price_per_peice,'                  ',qty*price_per_peice)
            print('-------------------------------------------------------')
            print("")
            print("BILL")
            print('----------------------------------------')
            print("AMOUNT PAID - ",sub_total)
            print("AMOUNT LEFT WITH YOU - ",cash-sub_total)
            print('----------------------------------------')
            print("THANKS FOR SHOPPING HAVE A NICE DAY :) ")
            print("")
            break
while payment==3:
      print("")
      print("YOUR CART IS DISCARDED SUCCEFULLY")
      break
while payment==2:
      while True:
            try:
                  card=int(input("Please Input Your 16 Digit Card No. (for ex- 1234123412341234) :: "))
                  break
            except ValueError:
                  print("please enter only numeric values")
      while card<1000000000000000 or card>9999999999999999:
            print("PLEASE ENTER VALID CARD NO.")
            while True:
                  try:
                        card=int(input("Please Input Your 16 Digit Card No. (for ex- 1234123412341234) :: "))
                        break
                  except ValueError:
                        print("please enter only numeric values")
      else:
            while True:
                  try:
                        exp_mon,exp_year=map(int,input("ENTER EXPIRY MONTH / ENTER EXPIRY YEAR ex-(MM/YY) : ").split('/'))
                        break
                  except ValueError:
                        print("please enter valid details")
            while True :
                  if exp_mon<1 or exp_mon>12:
                        print("PLEASE ENTER VALID YEAR AND MONTH")
                        while True:
                              try:
                                    exp_mon,exp_year=map(int,input("ENTER EXPIRY MONTH / ENTER EXPIRY YEAR ex-(MM/YY) : ").split('/'))
                                    break
                              except ValueError:
                                    print("please enter valid details")
                  elif exp_year<24 or exp_year>99:
                        print("PLEASE ENTER VALID YEAR AND MONTH")
                        while True:
                              try:
                                    exp_mon,exp_year=map(int,input("ENTER EXPIRY MONTH / ENTER EXPIRY YEAR ex-(MM/YY) : ").split('/'))
                                    break
                              except ValueError:
                                    print("please enter valid details")
                  elif exp_year==24 and exp_mon<3:
                        print("PLEASE ENTER VALID YEAR AND MONTH")
                        while True:
                              try:
                                    exp_mon,exp_year=map(int,input("ENTER EXPIRY MONTH / ENTER EXPIRY YEAR ex-(MM/YY) : ").split('/'))
                                    break
                              except ValueError:
                                    print("please enter valid details")
                  else:
                        break
      while True:
            try:
                  cvv=int(input("ENTER YOUR 3 DIGIT CVV : "))
                  break
            except ValueError:
                  print("PLEASE ENTER VALID CVV")
      while cvv<100 or cvv>999:
            print("PLEASE ENTER VALID CVV")
            while True:
                  try:
                        cvv=int(input("ENTER YOUR 3 DIGIT CVV : "))
                        break
                  except ValueError:
                        print("PLEASE ENTER VALID CVV")
      while True:
            try:
                  print("")
                  card_amt=int(input("PLEASE ENTER TOTAL AVAILABLE BALANCE IN YOUR CARD : "))
                  break
            except ValueError:
                  print("PLEASE ENTER ONLY NUMERIC VALUE")
      while card_amt<sub_total:
            print("YOU DONT HAVE SUFFICEIENT BALANCE")
            while True:
                  try:
                        print("")
                        print("SELECT YOUR PREFFERED PAYMENT MODE")
                        payment=int(input("for changing mode of payment to cash PRESS 1 : \nfor reentering amount PRESS 2 : \nto discard cart PRESS any other key : "))
                        break
                  except ValueError:
                        print("")
                        print('please enter valid payment mode')

            if payment==2:
                  while True:
                        try:
                              card_amt=int(input("Enter Amount You Have : "))
                              break
                        except ValueError:
                              print("Please Enter Only Numbric Value")
                  
                  while card_amt<sub_total:
                        print("YOU DONT HAVE SUFFICEIENT BALANCE")
                        while True:
                              try:
                                    print("")
                                    print("SELECT YOUR PREFFERED PAYMENT MODE")
                                    payment=int(input("for rentering card amount PRESS 1 : \nto discard cart PRESS any other key : "))
                                    break
                              except ValueError:
                                    print("")
                                    print('please enter valid payment mode')
                        if payment==1:
                              while True:
                                    try:
                                          card_amt=int(input("Enter Amount You Have : "))
                                          break
                                    except ValueError:
                                          print("Please Enter Only Numbric Value")
                        else:
                              print("")
                              print("YOUR CART IS DISCARDED SUCCEFULLY")
                              break
                        break
                  else:
                        print('')
                        print("")
                        print('Item In Your Cart')
                        print('-------------------------------------------------------')
                        print('')
                        print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
                        print('')
                        for prdct,qty in cart.items():
                              price_per_peice=inventory[prdct]
                              print("",prdct[0:5:1], "      ",qty,'    ',price_per_peice,'                  ',qty*price_per_peice)
                        print('-------------------------------------------------------')
                        print("")
                        print("BILL")
                        print('----------------------------------------')
                        print("AMOUNT PAID - ",sub_total)
                        print("AMOUNT LEFT WITH YOU - ",card_amt-sub_total)
                        print('----------------------------------------')
                        print("THANKS FOR SHOPPING HAVE A NICE DAY :) ")
                        print("")
                        break
                  break
            elif payment==1:
                  while True:
                        try:
                              cash=int(input("Enter Amount You Have : "))
                              break
                        except ValueError:
                              print("Please Enter Only Numbric Value")
                  while cash<sub_total:
                        print("YOU DONT HAVE SUFFICEIENT BALANCE")
                        while True:
                              try:
                                    print("")
                                    print("SELECT YOUR PREFFERED PAYMENT MODE")
                                    payment=int(input("for rentering cash PRESS 1 : \nto discard cart PRESS any other key : "))
                                    break
                              except ValueError:
                                    print("")
                                    print('please enter valid payment mode')
                        if payment==1:
                              while True:
                                    try:
                                          cash=int(input("Enter Amount You Have : "))
                                          break
                                    except ValueError:
                                          print("Please Enter Only Numbric Value")
                        else:
                              print("")
                              print("YOUR CART IS DISCARDED SUCCEFULLY")
                              break
                        break
                  else:
                        print('')
                        print("")
                        print('Item In Your Cart')
                        print('-------------------------------------------------------')
                        print('')
                        print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
                        print('')
                        for prdct,qty in cart.items():
                              price_per_peice=inventory[prdct]
                              print("",prdct[0:5:1], "      ",qty,'    ',price_per_peice,'                  ',qty*price_per_peice)
                        print('-------------------------------------------------------')
                        print("")
                        print("BILL")
                        print('----------------------------------------')
                        print("AMOUNT PAID - ",sub_total)
                        print("AMOUNT LEFT WITH YOU - ",cash-sub_total)
                        print('----------------------------------------')
                        print("THANKS FOR SHOPPING HAVE A NICE DAY :) ")
                        print("")
                        payment=0
                        break
                  break
            elif payment==3:
                  print("")
                  print("YOUR CART IS DISCARDED SUCCEFULLY")
                  break
            break
      else:
            print('')
            print("")
            print('Item In Your Cart')
            print('-------------------------------------------------------')
            print('')
            print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
            print('')
            for prdct,qty in cart.items():
                  price_per_peice=inventory[prdct]
                  print("",prdct[0:5:1], "      ",qty,'    ',price_per_peice,'                  ',qty*price_per_peice)
            print('-------------------------------------------------------')
            print("")
            print("BILL")
            print('----------------------------------------')
            print("AMOUNT PAID - ",sub_total)
            print("AMOUNT LEFT WITH YOU - ",card_amt-sub_total)
            print('----------------------------------------')
            print("THANKS FOR SHOPPING HAVE A NICE DAY :) ")
            print("")
            break
else:
      print("YOUR CART IS DISCARDED SUCCESFULLY")
