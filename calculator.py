a=float(input('enter first value : '))
b=float(input('enter second value : '))
operator=input('enter operator :  ')
match operator:
      case '+':
            print('adition is ',a+b)
      case '-':
            print('subtraction is ',a-b)
      case '*':
            print('multiplication is ',a*b)
      case '/':
            print('division is ',a/b)
      case _:
            print("please enter a valid operator")